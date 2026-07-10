#!/usr/bin/env python3
"""Structural extractor for the project-analyzer skill.

Deterministic layer: parses project READMEs, contexts, solutions, and
cross-project groups into a single JSON payload. Semantic equivalence
judgments are left to the LLM that consumes this output.

Usage (from AIE-Projects workspace root):

  python3 ai-engineering-syllabus/.cursor/skills/project-analyzer/scripts/analyze_projects.py \
    --repo-root ai-engineering-syllabus [SCOPE]

SCOPE (choose one; default --all):
  --project SLUG              single project
  --projects a,b,c            explicit list
  --group-prefix openclaw     all projects whose slug starts with prefix
  --group-context brasaland   all projects whose linked context folder has CONTEXT-<company>.*
  --all                       every project folder

Output: JSON to stdout. Never writes files.
"""

import argparse
import json
import os
import re
import sys

# --- section detection -------------------------------------------------------

# Ordered by specificity: multi-word phrases are matched before the single-word
# "challenge" so a heading like "Challenge evaluation" cannot be miscategorised,
# and bare "evaluation" is intentionally excluded so an "### ... evaluation"
# subheading is not promoted into a top-level evals section.
SECTION_KEYS = (
    ("deliverables", ["what you need to do", "what you have to do"]),
    ("evals", ["what we will evaluate", "what we'll evaluate",
               "what will be evaluated", "what we evaluate", "evaluation criteria"]),
    ("submit", ["how to submit", "how to deliver"]),
    ("start", ["how to start"]),
    ("challenge", ["challenge"]),
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
CHECKBOX_RE = re.compile(r"^\s*[-*]\s*\[( |x|X)\]\s+(.*)$")
# Context-file references are always uppercase (CONTEXT-brasaland.md). Case-sensitive
# on purpose so lowercase project-name suffixes (e.g. "...-context-project") don't match.
CONTEXT_REF_RE = re.compile(r"CONTEXT-[A-Za-z0-9_]+")
# CONTEXT-<company>.<lang>.md  OR  CONTEXT-<company>.md
CONTEXT_FILE_RE = re.compile(
    r"^CONTEXT-([A-Za-z0-9_]+?)(?:\.([a-z]{2}))?\.md$")
# project slug prefixes stripped when matching a topic-based context folder
SLUG_PREFIXES = ("ai-eng-", "openclaw-")


def _normalize_heading(text):
    # strip emojis / non-word leading chars, collapse, lowercase
    t = re.sub(r"[^0-9A-Za-z' ]+", " ", text)
    return re.sub(r"\s+", " ", t).strip().lower()


def _classify_heading(norm):
    for key, needles in SECTION_KEYS:
        for n in needles:
            if n in norm:
                return key
    return None


def parse_markdown(path):
    """Return {sections: {key: {title, raw, subheadings[], checkboxes[]}}, context_refs[], headings[]}."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    sections = {}
    headings = []
    context_refs = set()

    current = None

    for line in lines:
        for m in CONTEXT_REF_RE.findall(line):
            context_refs.add(m)

        hm = HEADING_RE.match(line.rstrip("\n"))
        if hm:
            level = len(hm.group(1))
            title = hm.group(2).strip()
            norm = _normalize_heading(title)
            headings.append({"level": level, "title": title})

            key = _classify_heading(norm)
            if key:
                current = {"title": title, "raw": [],
                           "subheadings": [], "checkboxes": []}
                sections[key] = current
            elif level <= 2:
                # a non-matching top-level heading closes the current section
                current = None
            elif current is not None:
                current["subheadings"].append(title)

        if current is not None:
            current["raw"].append(line.rstrip("\n"))
            cb = CHECKBOX_RE.match(line)
            if cb:
                current["checkboxes"].append(cb.group(2).strip())

    for sec in sections.values():
        sec["raw"] = "\n".join(sec["raw"]).strip()

    return {
        "sections": sections,
        "headings": headings,
        "context_refs": sorted(context_refs),
    }


# --- context discovery -------------------------------------------------------

def _context_candidates(slug):
    """Context folders are topic-based; project slugs carry course prefixes."""
    cands = [slug]
    for pfx in SLUG_PREFIXES:
        if slug.startswith(pfx):
            cands.append(slug[len(pfx):])
    seen = set()
    return [c for c in cands if not (c in seen or seen.add(c))]


def discover_context(repo_root, slug):
    """Return {folder, matched_by, companies[], files[]} for the project's context folder.

    Tries exact slug, then slug with course prefix stripped. Companies come from
    CONTEXT-<company>[.lang].md files and from per-company subdirectories.
    """
    base = os.path.join(repo_root, "content", "contexts")
    for cand in _context_candidates(slug):
        ctx_dir = os.path.join(base, cand)
        if not os.path.isdir(ctx_dir):
            continue
        companies = set()
        files = []
        for fn in sorted(os.listdir(ctx_dir)):
            files.append(fn)
            cm = CONTEXT_FILE_RE.match(fn)
            if cm:
                companies.add(cm.group(1))
            elif os.path.isdir(os.path.join(ctx_dir, fn)) and not fn.startswith("."):
                companies.add(fn)  # per-company subfolder layout
        return {
            "folder": os.path.relpath(ctx_dir, repo_root),
            "matched_by": "exact" if cand == slug else "prefix-stripped",
            "companies": sorted(companies),
            "files": files,
        }
    return None


def is_english_md(fn):
    """English files only: CONTEXT-x.en.md or no-language CONTEXT-x.md. Exclude *.es.md."""
    if not fn.endswith(".md"):
        return False
    return not fn.endswith(".es.md")


def read_context_files(repo_root, ctx):
    """Attach English context bodies so the LLM can compare README claims vs context facts."""
    if not ctx:
        return {}
    out = {}
    base = os.path.join(repo_root, ctx["folder"])
    for fn in ctx["files"]:
        if not is_english_md(fn):
            continue
        p = os.path.join(base, fn)
        try:
            with open(p, "r", encoding="utf-8") as fh:
                out[fn] = fh.read()
        except OSError:
            out[fn] = None
    return out


# --- project extraction ------------------------------------------------------

def load_learn_json(project_dir):
    p = os.path.join(project_dir, "learn.json")
    if not os.path.isfile(p):
        return None
    try:
        with open(p, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return {"_parse_error": str(exc)}


def extract_project(repo_root, slug):
    project_dir = os.path.join(repo_root, "content", "projects", slug)
    result = {"slug": slug, "dir": os.path.relpath(
        project_dir, repo_root), "issues_structural": []}

    readme = os.path.join(project_dir, "README.md")
    if os.path.isfile(readme):
        result["readme"] = parse_markdown(readme)
    else:
        result["readme"] = None
        result["issues_structural"].append({"id": "INTRA-STRUCT", "severity": "blocker",
                                            "msg": "README.md missing"})

    learn = load_learn_json(project_dir)
    result["learn_json"] = learn

    sol_path = os.path.join(project_dir, ".learn", "solution", "README.md")
    if os.path.isfile(sol_path):
        result["solution"] = parse_markdown(sol_path)
        result["solution"]["exists"] = True
    else:
        result["solution"] = {"exists": False}

    ctx = discover_context(repo_root, slug)
    result["context"] = ctx
    result["context_bodies"] = read_context_files(repo_root, ctx)

    _structural_checks(result)
    return result


def _structural_checks(p):
    """Cheap deterministic flags. Semantic pairing is the LLM's job."""
    issues = p["issues_structural"]
    rd = p.get("readme")
    if not rd:
        return
    secs = rd["sections"]

    for key, code in [("challenge", "INTRA-STRUCT"), ("deliverables", "INTRA-STRUCT"),
                      ("evals", "INTRA-STRUCT")]:
        if key not in secs:
            issues.append({"id": code, "severity": "warning",
                           "msg": f"README has no detected '{key}' section"})

    n_deliv = len(secs.get("deliverables", {}).get("checkboxes", []))
    n_eval = len(secs.get("evals", {}).get("checkboxes", []))
    p["counts"] = {"deliverable_items": n_deliv, "eval_items": n_eval}

    if "deliverables" in secs and n_deliv == 0:
        issues.append({"id": "INTRA-STRUCT", "severity": "warning",
                       "msg": "deliverables section has no checkbox items — nothing to match against evals"})
    if "evals" in secs and n_eval == 0:
        issues.append({"id": "INTRA-STRUCT", "severity": "warning",
                       "msg": "evals section has no checkbox items — deliverables cannot be traced to evaluation"})

    # context reference vs existence. "CONTEXT-company" is the template placeholder,
    # not a real company reference, so it does not by itself imply a missing folder.
    refs = rd.get("context_refs", [])
    real_refs = [r for r in refs if r.lower() not in (
        "context-company", "context-companyname")]
    ctx = p.get("context")
    if real_refs and not ctx:
        issues.append({"id": "CTX-STRUCT", "severity": "warning",
                       "msg": f"README references {real_refs} but no matching content/contexts/ folder found"})
    if ctx and not refs:
        issues.append({"id": "CTX-STRUCT", "severity": "cosmetic",
                       "msg": f"context folder {ctx['folder']} exists but README.md has no CONTEXT-* reference"})

    if not p["solution"]["exists"]:
        issues.append({"id": "SOL-STRUCT", "severity": "warning",
                       "msg": ".learn/solution/README.md missing — solution vs requirements check not possible"})


# --- scope resolution --------------------------------------------------------

def list_all_projects(repo_root):
    base = os.path.join(repo_root, "content", "projects")
    return sorted(
        d for d in os.listdir(base)
        if os.path.isdir(os.path.join(base, d)) and not d.startswith(".")
    )


def resolve_scope(repo_root, args):
    if args.project:
        return [args.project]
    if args.projects:
        return [s.strip() for s in args.projects.split(",") if s.strip()]
    if args.group_prefix:
        return [s for s in list_all_projects(repo_root) if s.startswith(args.group_prefix)]
    if args.group_context:
        target = args.group_context.lower()
        out = []
        for slug in list_all_projects(repo_root):
            ctx = discover_context(repo_root, slug)
            if ctx and target in [c.lower() for c in ctx["companies"]]:
                out.append(slug)
        return out
    return list_all_projects(repo_root)


# --- cross-project grouping (metadata for XPROJ checks) ----------------------

def _slug_group_key(slug):
    """Group by a known course prefix when present, else the first token."""
    for pfx in SLUG_PREFIXES:
        if slug.startswith(pfx):
            return pfx.rstrip("-")
    return slug.split("-")[0] if "-" in slug else slug


def build_groups(projects, include_prefix=False):
    """Cross-project grouping metadata for XPROJ.

    by_context_company (always) groups projects sharing a CONTEXT company.
    by_slug_prefix (opt-in via include_prefix) groups by course prefix; it is
    coarse and off by default because it lumps many unrelated projects together.
    """
    by_company = {}
    for p in projects:
        slug = p["slug"]
        ctx = p.get("context")
        if ctx:
            for c in ctx["companies"]:
                by_company.setdefault(c, []).append(slug)
    groups = {"by_context_company": {k: v for k,
                                     v in by_company.items() if len(v) > 1}}

    if include_prefix:
        by_prefix = {}
        for p in projects:
            by_prefix.setdefault(_slug_group_key(
                p["slug"]), []).append(p["slug"])
        groups["by_slug_prefix"] = {k: v for k,
                                    v in by_prefix.items() if len(v) > 1}

    return groups


def main():
    ap = argparse.ArgumentParser(
        description="Structural extractor for project-analyzer skill")
    ap.add_argument("--repo-root", default="ai-engineering-syllabus")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--project")
    g.add_argument("--projects")
    g.add_argument("--group-prefix")
    g.add_argument("--group-context")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--no-context-bodies", action="store_true",
                    help="omit full context/solution text to save tokens")
    ap.add_argument("--group-by-prefix", action="store_true",
                    help="also emit coarse by_slug_prefix grouping (off by default)")
    args = ap.parse_args()

    repo_root = args.repo_root
    if not os.path.isdir(os.path.join(repo_root, "content", "projects")):
        print(f"ERROR: {repo_root}/content/projects not found (run from AIE-Projects root)",
              file=sys.stderr)
        sys.exit(2)

    slugs = resolve_scope(repo_root, args)
    if not slugs:
        print("ERROR: scope resolved to zero projects", file=sys.stderr)
        sys.exit(1)

    projects = []
    for slug in slugs:
        pdir = os.path.join(repo_root, "content", "projects", slug)
        if not os.path.isdir(pdir):
            projects.append(
                {"slug": slug, "error": "project folder not found"})
            continue
        projects.append(extract_project(repo_root, slug))

    if args.no_context_bodies:
        for p in projects:
            p.pop("context_bodies", None)
            if isinstance(p.get("solution"), dict):
                p["solution"].pop("raw", None)

    payload = {
        "repo_root": repo_root,
        "scope_count": len(projects),
        "projects": projects,
        "groups": build_groups([p for p in projects if "error" not in p],
                               include_prefix=args.group_by_prefix),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
