#!/usr/bin/env python3
"""
parse_syllabus.py — Extracts structured context from the AI Engineer (or AI Native Full Stack) syllabus CSV.

Usage:
  python3 parse_syllabus.py --week <n> --day <n>
  python3 parse_syllabus.py --csv <path-or-name> --week <n> --day <n>
  python3 parse_syllabus.py --week <n> --day <n> --include-prior
  python3 parse_syllabus.py --list
  python3 parse_syllabus.py --list-csvs
  python3 parse_syllabus.py --search "keyword"

CSV resolution: if --csv omitted, searches **/syllabus/**/*.csv under --search-root
(default: cwd). One match → use it. Zero → error. Multiple → error with candidates
(agent must ask user which program/file). --csv may be a path or unique name substring.

Output: compact JSON by default (use --pretty for indented). Search returns index
        rows only; run --week/--day for full lesson context. With --include-prior,
        prior_skills uses smart mode (all prior milestones + last N regular lessons).
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

import pandas as pd

DEFAULT_PRIOR_WINDOW = 15
SKIP_DIR_NAMES = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    ".superpowers",
    ".cursor",
}


# ---------------------------------------------------------------------------
# CSV discovery / resolution
# ---------------------------------------------------------------------------

def find_syllabus_csvs(search_root: str | Path | None = None) -> list[Path]:
    """
    Find *.csv files under directories named exactly `syllabus`.

    Walks `search_root` (default: cwd) recursively, skipping common junk dirs.
    Only paths with a `syllabus` path segment qualify (e.g. docs/syllabus/*.csv).
    """
    root = Path(search_root or Path.cwd()).resolve()
    found: list[Path] = []
    for path in root.rglob("*.csv"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if "syllabus" not in path.parts:
            continue
        found.append(path.resolve())
    # Stable unique list
    return sorted(set(found), key=lambda p: str(p).lower())


def resolve_syllabus_csv(
    csv_arg: str | None = None,
    *,
    search_root: str | Path | None = None,
) -> Path | dict:
    """
    Resolve which syllabus CSV to use.

    Returns a Path on success, or an error dict:
      {"error": "...", "candidates": [...], "hint": "..."}

    Rules:
      - --csv path that exists → that file
      - --csv substring → filter discovered CSVs by name; must be unique
      - no --csv → auto-pick if exactly one discovered; else error dict
    """
    candidates = find_syllabus_csvs(search_root)
    candidate_strs = [str(p) for p in candidates]

    if csv_arg:
        explicit = Path(csv_arg).expanduser()
        if explicit.is_file():
            return explicit.resolve()

        needle = csv_arg.lower()
        matches = [
            p for p in candidates
            if needle in p.name.lower() or needle in str(p).lower()
        ]
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            return {
                "error": "multiple_syllabus_csvs",
                "query": csv_arg,
                "candidates": [str(p) for p in matches],
                "hint": (
                    "Pass --csv with a full path or a unique filename substring, "
                    "or ask the user which syllabus CSV to use."
                ),
            }
        return {
            "error": "syllabus_csv_not_found",
            "query": csv_arg,
            "candidates": candidate_strs,
            "hint": (
                "No CSV matched that path/name under a `syllabus/` directory. "
                "Pass an existing path or run --list-csvs."
            ),
        }

    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) == 0:
        return {
            "error": "syllabus_csv_not_found",
            "candidates": [],
            "hint": (
                "No *.csv found under a `syllabus/` directory. "
                "Place the planning CSV in docs/syllabus/ (or any **/syllabus/) "
                "or pass --csv <path>."
            ),
        }
    return {
        "error": "multiple_syllabus_csvs",
        "candidates": candidate_strs,
        "hint": (
            "Multiple syllabus CSVs found. Ask the user which one, then re-run "
            "with --csv <path or unique name substring>."
        ),
    }


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _dump(data, *, pretty: bool = False) -> None:
    """Print JSON; compact by default to reduce token usage."""
    if pretty:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def _lesson_ref(lesson: dict) -> dict:
    return {
        "week": lesson["week"],
        "day": lesson["day"],
        "skill": lesson["skill_name"],
        "is_milestone": lesson["is_milestone"],
    }


def build_prior_skills(
    lessons: list[dict],
    idx: int,
    *,
    mode: str = "smart",
    window: int = DEFAULT_PRIOR_WINDOW,
) -> tuple[list[dict], dict]:
    """
    Build prior_skills list and metadata.

    Modes:
      full       — every lesson before idx
      milestones — milestones only
      smart      — all prior milestones + last `window` regular (non-milestone) lessons
    """
    prior = lessons[:idx]
    total = len(prior)

    if mode == "full":
        refs = [_lesson_ref(l) for l in prior]
        return refs, {"mode": "full", "total_prior": total, "returned": len(refs)}

    if mode == "milestones":
        refs = [_lesson_ref(l) for l in prior if l["is_milestone"]]
        return refs, {
            "mode": "milestones",
            "total_prior": total,
            "returned": len(refs),
        }

    # smart: milestones in order + recent regular lessons
    regular_positions = [
        i for i, lesson in enumerate(prior) if not lesson["is_milestone"]
    ]
    recent_positions = set(
        regular_positions[-window:]) if window > 0 else set()
    refs = [
        _lesson_ref(lesson)
        for i, lesson in enumerate(prior)
        if lesson["is_milestone"] or i in recent_positions
    ]
    return refs, {
        "mode": "smart",
        "window": window,
        "total_prior": total,
        "returned": len(refs),
    }


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _clean(val) -> str | None:
    """Return stripped string or None for NaN / empty."""
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    s = str(val).strip()
    return s if s else None


def _is_day_row(row) -> bool:
    """A day/session row has a numeric (or special) week AND a Skill: description."""
    week_raw = _clean(row.iloc[0])
    day_raw = _clean(row.iloc[1])
    content = _clean(row.iloc[2])
    if not week_raw or not day_raw or not content:
        return False
    return "skill:" in content.lower()


def _is_milestone_row(row) -> bool:
    """Milestones have 'HITO' in column 0."""
    week_raw = _clean(row.iloc[0])
    return bool(week_raw and week_raw.upper().startswith("HITO"))


def _parse_week_day(row):
    """Returns (week_str, day_str) from a day row."""
    return _clean(row.iloc[0]), _clean(row.iloc[1])


def _extract_milestone_title(milestone_id: str, content: str) -> str:
    """
    For milestone rows, try to find the human-readable title embedded in the
    content (e.g. '🎨 Hito 4 — ...', 'Hito 3 —...', '⚛️ Hito 3 —...').
    Falls back to first non-empty line of content.
    """
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.search(r"[Hh]ito\s+\d+\s*[—–-]", line):
            return f"[{milestone_id}] {line}"
    first = next((l.strip() for l in content.splitlines() if l.strip()), "")
    return f"[{milestone_id}] {first[:80]}" if first else milestone_id


def _extract_skill_name(content: str) -> str:
    """Pull the human-readable skill name from 'Skill: ...' lines."""
    lines = [l.strip() for l in content.splitlines() if "skill:" in l.lower()]
    skills = []
    for line in lines:
        match = re.search(r"[Ss]kill\s*:\s*(.+)", line)
        if match:
            skills.append(match.group(1).strip())
    return " | ".join(skills) if skills else content.strip()


def _build_content_block(row) -> dict:
    """Convert a content/project row into a structured dict."""
    return {
        "status":         _clean(row.iloc[1]),
        "content":        _clean(row.iloc[2]),
        "how_to_think":   _clean(row.iloc[3]),
        "best_practices": _clean(row.iloc[4]),
        "patterns":       _clean(row.iloc[5]),
        "anti_patterns":  _clean(row.iloc[6]),
        "limitaciones":   _clean(row.iloc[7]),
    }


# ---------------------------------------------------------------------------
# Main loader
# ---------------------------------------------------------------------------

def load_syllabus(csv_path: str) -> list[dict]:
    """
    Parse the CSV into a list of lesson dicts, each with:
      week, day, skill_raw, skill_name, blocks (list of content dicts),
      is_milestone, milestone_id
    """
    df = pd.read_csv(csv_path, header=None, dtype=str)
    lessons = []
    current_lesson = None

    for _, row in df.iterrows():
        content_val = _clean(row.iloc[2])
        if content_val and content_val.startswith("---"):
            if current_lesson:
                lessons.append(current_lesson)
                current_lesson = None
            continue

        if content_val and content_val.startswith("###"):
            continue

        if _is_milestone_row(row):
            if current_lesson:
                lessons.append(current_lesson)
            milestone_id = _clean(row.iloc[0])
            skill_name = _extract_milestone_title(
                milestone_id, content_val or "")
            current_lesson = {
                "week":         milestone_id,
                "day":          _clean(row.iloc[1]),
                "skill_raw":    content_val or "",
                "skill_name":   skill_name,
                "is_milestone": True,
                "milestone_id": milestone_id,
                "blocks":       [],
            }
            block = _build_content_block(row)
            if any(v for v in block.values()):
                current_lesson["blocks"].append(block)
            continue

        if _is_day_row(row):
            if current_lesson:
                lessons.append(current_lesson)
            week_str, day_str = _parse_week_day(row)
            current_lesson = {
                "week":         week_str,
                "day":          day_str,
                "skill_raw":    content_val or "",
                "skill_name":   _extract_skill_name(content_val or ""),
                "is_milestone": False,
                "milestone_id": None,
                "blocks":       [],
            }
            continue

        if current_lesson is not None and content_val:
            block = _build_content_block(row)
            current_lesson["blocks"].append(block)

    if current_lesson:
        lessons.append(current_lesson)

    return lessons


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def _lesson_index(lessons: list[dict], week: str, day: str) -> int | None:
    """Return the list index of the requested lesson, or None."""
    for i, lesson in enumerate(lessons):
        if lesson["week"] == week and lesson["day"] == day:
            return i
    return None


def _merge_blocks(blocks: list[dict]) -> dict:
    """Merge multiple content blocks into one, concatenating non-null fields."""
    merged = {
        "content":        [],
        "how_to_think":   [],
        "best_practices": [],
        "patterns":       [],
        "anti_patterns":  [],
        "limitaciones":   [],
        "statuses":       [],
    }
    for b in blocks:
        for key in ("content", "how_to_think", "best_practices", "patterns",
                    "anti_patterns", "limitaciones"):
            val = b.get(key)
            if val:
                merged[key].append(val)
        if b.get("status"):
            merged["statuses"].append(b["status"])

    return {k: "\n\n---\n\n".join(v) if v else None for k, v in merged.items()}


def format_lesson(lesson: dict, include_raw: bool = False) -> dict:
    """Return a clean, serialisable representation of a lesson."""
    merged = _merge_blocks(lesson["blocks"])
    out = {
        "week":         lesson["week"],
        "day":          lesson["day"],
        "is_milestone": lesson["is_milestone"],
        "skill":        lesson["skill_name"],
        **merged,
    }
    if include_raw:
        out["skill_raw"] = lesson["skill_raw"]
    return out


def _search_haystack(lesson: dict) -> str:
    return (
        lesson["skill_name"]
        + lesson["skill_raw"]
        + " ".join(b.get("content") or "" for b in lesson["blocks"])
    ).lower()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Query the AI Engineer or AI Native Full Stack syllabus.")
    parser.add_argument(
        "--csv",
        help=(
            "Syllabus CSV path, or unique name substring. "
            "If omitted, auto-discovers **/syllabus/**/*.csv under --search-root"
        ),
    )
    parser.add_argument(
        "--search-root",
        default=None,
        help="Root directory for syllabus CSV discovery (default: cwd)",
    )
    parser.add_argument(
        "--list-csvs",
        action="store_true",
        help="List discovered syllabus CSVs under **/syllabus/ and exit",
    )
    parser.add_argument("--week", help="Week number (e.g. 1, 2, 0)")
    parser.add_argument("--day", help="Day number (e.g. 1, -1, 4 y 5)")
    parser.add_argument(
        "--include-prior",
        action="store_true",
        help=(
            "Include prior_skills (default mode: all prior milestones + last "
            f"{DEFAULT_PRIOR_WINDOW} regular lessons; use --prior-full for all)"
        ),
    )
    parser.add_argument(
        "--prior-full",
        action="store_true",
        help="With --include-prior: return every lesson before the target day",
    )
    parser.add_argument(
        "--prior-milestones-only",
        action="store_true",
        help="With --include-prior: return only prior milestones",
    )
    parser.add_argument(
        "--prior-window",
        type=int,
        metavar="N",
        default=DEFAULT_PRIOR_WINDOW,
        help=(
            f"With --include-prior (smart mode): include last N regular lessons "
            f"(default {DEFAULT_PRIOR_WINDOW})"
        ),
    )
    parser.add_argument("--list", action="store_true",
                        help="List all lessons (week, day, skill)")
    parser.add_argument(
        "--search",
        help="Search keyword; returns index rows only (then run --week/--day)",
    )
    parser.add_argument(
        "--search-full",
        action="store_true",
        help="With --search: return full lesson payloads (legacy, token-heavy)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON with indentation (default: compact)",
    )
    parser.add_argument(
        "--include-raw",
        action="store_true",
        help="Include skill_raw on the current lesson",
    )
    args = parser.parse_args()

    if args.prior_window < 0:
        parser.error("--prior-window must be >= 0")

    pretty = args.pretty

    if args.list_csvs:
        csvs = find_syllabus_csvs(args.search_root)
        _dump(
            {
                "count": len(csvs),
                "candidates": [str(p) for p in csvs],
                "search_root": str(Path(args.search_root or Path.cwd()).resolve()),
            },
            pretty=pretty,
        )
        return

    resolved = resolve_syllabus_csv(args.csv, search_root=args.search_root)
    if isinstance(resolved, dict):
        _dump(resolved, pretty=pretty)
        sys.exit(2)

    csv_path = resolved
    lessons = load_syllabus(str(csv_path))

    if args.list:
        index = [_lesson_ref(l) for l in lessons]
        _dump({"csv": str(csv_path), "lessons": index}, pretty=pretty)
        return

    if args.search:
        kw = args.search.lower()
        matches = []
        for lesson in lessons:
            if kw in _search_haystack(lesson):
                if args.search_full:
                    matches.append(format_lesson(lesson))
                else:
                    matches.append(_lesson_ref(lesson))
        _dump(
            {
                "csv": str(csv_path),
                "query": args.search,
                "count": len(matches),
                "matches": matches,
                "next": (
                    "Run --week and --day on a match for full lesson context."
                    if matches and not args.search_full
                    else None
                ),
            },
            pretty=pretty,
        )
        return

    if not args.week or not args.day:
        parser.error(
            "Provide --week and --day (or --list / --search / --list-csvs).")

    idx = _lesson_index(lessons, args.week, args.day)
    if idx is None:
        _dump(
            {
                "csv": str(csv_path),
                "error": f"No lesson found for week={args.week} day={args.day}",
            },
            pretty=pretty,
        )
        sys.exit(1)

    result = {
        "csv": str(csv_path),
        "current": format_lesson(lessons[idx], include_raw=args.include_raw),
    }

    if args.include_prior and idx > 0:
        if args.prior_full:
            mode = "full"
        elif args.prior_milestones_only:
            mode = "milestones"
        else:
            mode = "smart"
        prior, meta = build_prior_skills(
            lessons,
            idx,
            mode=mode,
            window=args.prior_window,
        )
        result["prior_skills"] = prior
        result["prior_skills_meta"] = meta

    _dump(result, pretty=pretty)


if __name__ == "__main__":
    main()
