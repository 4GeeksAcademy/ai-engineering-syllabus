---
name: project-analyzer
description: Analyze ai-engineering-syllabus projects for inconsistencies and conflicts — within a single project (challenge vs deliverables vs evals), between a project README and its CONTEXT file(s), between a project and its reference solution, and across a group of projects. Read-only. Produces a chat report of findings plus solution alternatives. Use when the user asks to analyze, audit, review coherence of, or find conflicts/inconsistencies in one or more projects under content/projects.
---

# Project Analyzer

Read-only coherence auditor for projects under `ai-engineering-syllabus/content/projects/<slug>`.

## Scope of analysis (4 checks)

1. **INTRA** — intra-project coherence: the Challenge, _What You Need to Do_ (deliverables), and _What We Will Evaluate_ (evals) must agree. Every deliverable should be evaluated; every eval should trace to a deliverable and to the challenge.
2. **CTX** — README vs its context files under `content/contexts/`: fields, roles, deliverables, constraints referenced in the README must match the context. The script resolves the context folder by project slug or prefix-stripped slug, so it only auto-links **standalone project contexts** (topic-named folders like `supplier-directory`, `openclaw-onboarding-agent`). **Module-numbered milestone contexts** (`00-general-contexts` … `10-realtime`) are NOT auto-linked yet; for `ai-eng-milestone-*` projects, if the script returns no `context`, resolve the folder manually (slug suffix ≈ folder name minus its number) and read the English `CONTEXT-*.md` files before doing the CTX check. Many non-milestone projects have no company context — that is expected, not a finding.
3. **SOL** — `.learn/solution/README.md` vs the project's stated requirements + eval criteria: the solution must actually cover them.
4. **XPROJ** — cross-project: contradictions, overlaps, and scope collisions across a group (grouped by slug prefix or shared CONTEXT company).

**Out of scope (do not report):** `learn.json` metadata coherence, and EN/ES translation drift (`README.md` vs `README.es.md`).

**English files only.** Analyze `README.md`, `.learn/solution/README.md`, and English context files (`CONTEXT-*.en.md` or no-language `CONTEXT-*.md`) exclusively. Never read or analyze `*.es.md` files. The script already excludes Spanish bodies from its output.

## Hard rules

- **Read-only.** Never write, edit, or create files. Never modify `learn.json` or READMEs. Output is a chat report only.
- **No authoritative source.** When two documents conflict, do NOT assume which is correct. Report the conflict and offer solution alternatives in **both** directions.
- **Semantic, not string.** "Send welcome email" (deliverable) and "agent sends emails autonomously" (eval) are the same intent. Judge by meaning. The script only extracts and pairs candidates; equivalence judgment is yours.

## Workflow

### Step 1 — Extract structure (deterministic)

Run from the workspace root (`AIE-Projects`). Pick ONE scope:

```bash
# single project
python3 ai-engineering-syllabus/.cursor/skills/project-analyzer/scripts/analyze_projects.py \
  --repo-root ai-engineering-syllabus --project <slug>

# explicit list
python3 .../analyze_projects.py --repo-root ai-engineering-syllabus --projects <slug-a>,<slug-b>

# grouped by slug prefix (e.g. openclaw, ai-eng)
python3 .../analyze_projects.py --repo-root ai-engineering-syllabus --group-prefix openclaw

# grouped by shared CONTEXT company (e.g. brasaland, nexova)
python3 .../analyze_projects.py --repo-root ai-engineering-syllabus --group-context brasaland

# everything
python3 .../analyze_projects.py --repo-root ai-engineering-syllabus --all
```

The script emits JSON: per-project parsed `sections` (challenge/deliverables/evals with `checkboxes`), `solution`, discovered `context` + `context_bodies`, cheap `issues_structural` flags, and cross-project `groups`.

Flags:

- `--no-context-bodies` — for large sweeps, omit full context/solution text to save tokens (then read the specific files yourself when needed).
- `--group-by-prefix` — additionally emit the coarse `by_slug_prefix` grouping. Off by default because it lumps many unrelated projects together; `groups.by_context_company` is the reliable XPROJ grouping.

### Step 2 — Semantic analysis (LLM)

For each project in scope, reason over the extracted structure:

- **INTRA:** Pair each deliverable checkbox with eval checkbox(es) by meaning. Flag: deliverable with no matching eval; eval with no matching deliverable; challenge promise absent from both deliverables and evals; deliverable/eval that contradicts the challenge.
- **CTX:** For every fact the README asserts about the domain (fields, roles, entities, deliverables, numeric constraints), verify it against `context_bodies`. Flag mismatches, README facts absent from context, and context constraints the README ignores. When a project's context has multiple companies, check the README stays company-agnostic (or is consistent with all of them).
- **SOL:** Check the solution covers each requirement and satisfies each eval criterion. Flag requirements/evals with no corresponding solution coverage, and solution steps that contradict the stated requirements.
- **XPROJ:** Skip entirely when `scope_count == 1` (nothing to compare). Otherwise, using `groups.by_context_company` (and `by_slug_prefix` only if `--group-by-prefix` was passed), compare projects in the set. Flag contradictory instructions/facts, duplicate or near-duplicate deliverables, and scope overlaps between sibling projects.

Read additional files directly when the JSON is insufficient (e.g. full solution body, a specific English context file). Never open `*.es.md` files.

### Step 3 — Report (chat only)

Use the [report template](report-template.md). Each finding gets: a stable **issue ID**, **severity** (with emoji), **category** (with emoji), **location** (file + section), a clickable **README link** for quick access (and a context/second-README link when relevant), a one-line **description**, and **solution alternatives**. Build link paths workspace-root-relative (prefix the repo folder, e.g. `ai-engineering-syllabus/content/projects/<slug>/README.md`).

## Issue ID scheme

`<CATEGORY>-<NN>` numbered continuously across the **whole report** (per category), in report order. IDs are report-global and unique: the counter never resets per project — a multi-project run may yield `INTRA-01` (project A), `INTRA-02` (project B), `INTRA-03` (project A again). Identify which project a finding belongs to via its location + README link, not via the ID.

| Category | Emoji | Meaning                                                  |
| -------- | ----- | -------------------------------------------------------- |
| `INTRA`  | 👷‍♂️    | intra-project: challenge ↔ deliverables ↔ evals mismatch |
| `CTX`    | 📄    | context: README ↔ CONTEXT mismatch                       |
| `SOL`    | 💡    | solution ↔ requirements/evals mismatch                   |
| `XPROJ`  | ❎    | cross-project conflict/overlap                           |

## Severity

Prefix every finding's severity with its emoji:

- ⛔️ **blocker** — a student following the README cannot succeed, or a required deliverable is never evaluated / contradicts the challenge. Must fix.
- ⚠️ **warning** — real inconsistency that causes confusion or ambiguity but has a workaround.
- 🧴 **cosmetic** — minor wording drift or purely cosmetic issue.

## Anti-patterns

- Reporting string differences as conflicts when the intent is equivalent.
- Picking a "correct" side of a conflict instead of offering both alternatives.
- Reporting `learn.json` metadata or EN/ES drift (out of scope).
- Editing any file. This skill only reports.
