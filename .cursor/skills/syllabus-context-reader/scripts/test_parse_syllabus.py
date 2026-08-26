#!/usr/bin/env python3
"""Tests for parse_syllabus.py — run: python3 -m unittest test_parse_syllabus.py"""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from parse_syllabus import (
    build_prior_skills,
    find_syllabus_csvs,
    load_syllabus,
    resolve_syllabus_csv,
    _lesson_index,
)

SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = SCRIPT_DIR.parents[3]  # AIE-Projects
CSV = (
    WORKSPACE_ROOT
    / "ai-engineering-syllabus"
    / "docs"
    / "syllabus"
    / "New Syllabus AI Engineer - Planificación del programa.csv"
)
# Fallback: legacy course-outline-generator path (explicit --csv still works)
LEGACY_CSV = (
    WORKSPACE_ROOT
    / "course-outline-generator"
    / "ai-engineering"
    / "New Syllabus AI Engineer - Planificación del programa.csv"
)
PY = SCRIPT_DIR / "parse_syllabus.py"


def _csv_for_integration() -> Path | None:
    if CSV.is_file():
        return CSV
    if LEGACY_CSV.is_file():
        return LEGACY_CSV
    return None


INTEGRATION_CSV = _csv_for_integration()


def run_cli(*args: str, cwd: Path | None = None) -> tuple[int, dict | list]:
    proc = subprocess.run(
        ["python3", str(PY), *args],
        text=True,
        capture_output=True,
        cwd=str(cwd) if cwd else None,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return proc.returncode, payload


class TestFindSyllabusCsvs(unittest.TestCase):
    def test_finds_only_under_syllabus_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            syllabus_dir = root / "docs" / "syllabus"
            syllabus_dir.mkdir(parents=True)
            other_dir = root / "content" / "data"
            other_dir.mkdir(parents=True)
            keep = syllabus_dir / "AI Engineer.csv"
            keep.write_text("a,b\n", encoding="utf-8")
            (other_dir / "noise.csv").write_text("x,y\n", encoding="utf-8")
            # Repo folder name containing "syllabus" must NOT match without segment
            fake_repo = root / "ai-engineering-syllabus" / "content"
            fake_repo.mkdir(parents=True)
            (fake_repo / "not-here.csv").write_text("n,o\n", encoding="utf-8")

            found = find_syllabus_csvs(root)
            self.assertEqual(found, [keep.resolve()])

    def test_skips_venv_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / ".venv" / "syllabus"
            bad.mkdir(parents=True)
            (bad / "pkg.csv").write_text("a\n", encoding="utf-8")
            good_dir = root / "syllabus"
            good_dir.mkdir()
            good = good_dir / "real.csv"
            good.write_text("a\n", encoding="utf-8")
            self.assertEqual(find_syllabus_csvs(root), [good.resolve()])


class TestResolveSyllabusCsv(unittest.TestCase):
    def test_auto_picks_single(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "syllabus"
            d.mkdir()
            only = d / "only.csv"
            only.write_text("a\n", encoding="utf-8")
            resolved = resolve_syllabus_csv(None, search_root=root)
            self.assertEqual(resolved, only.resolve())

    def test_multiple_without_csv_returns_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "syllabus"
            d.mkdir()
            (d / "AI Engineer.csv").write_text("a\n", encoding="utf-8")
            (d / "AI Native Full Stack.csv").write_text("b\n", encoding="utf-8")
            result = resolve_syllabus_csv(None, search_root=root)
            self.assertIsInstance(result, dict)
            self.assertEqual(result["error"], "multiple_syllabus_csvs")
            self.assertEqual(len(result["candidates"]), 2)

    def test_substring_disambiguates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "syllabus"
            d.mkdir()
            eng = d / "New Syllabus AI Engineer.csv"
            fs = d / "AI Native Full Stack.csv"
            eng.write_text("a\n", encoding="utf-8")
            fs.write_text("b\n", encoding="utf-8")
            resolved = resolve_syllabus_csv("Engineer", search_root=root)
            self.assertEqual(resolved, eng.resolve())

    def test_explicit_path_outside_syllabus(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            outside = root / "legacy" / "plan.csv"
            outside.parent.mkdir(parents=True)
            outside.write_text("a\n", encoding="utf-8")
            resolved = resolve_syllabus_csv(str(outside), search_root=root)
            self.assertEqual(resolved, outside.resolve())

    def test_zero_csvs_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = resolve_syllabus_csv(None, search_root=tmp)
            self.assertEqual(result["error"], "syllabus_csv_not_found")


class TestResolveCli(unittest.TestCase):
    def test_list_csvs_and_multiple_exits_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "syllabus"
            d.mkdir()
            (d / "a.csv").write_text("a\n", encoding="utf-8")
            (d / "b.csv").write_text("b\n", encoding="utf-8")
            code, payload = run_cli("--list-csvs", "--search-root", str(root))
            self.assertEqual(code, 0)
            self.assertEqual(payload["count"], 2)

            code, payload = run_cli("--list", "--search-root", str(root))
            self.assertEqual(code, 2)
            self.assertEqual(payload["error"], "multiple_syllabus_csvs")


@unittest.skipUnless(INTEGRATION_CSV is not None, "syllabus CSV not found")
class TestParseSyllabusCLI(unittest.TestCase):
    def test_list_returns_lessons(self):
        code, payload = run_cli("--csv", str(INTEGRATION_CSV), "--list")
        self.assertEqual(code, 0)
        index = payload["lessons"] if isinstance(payload, dict) else payload
        self.assertIsInstance(index, list)
        self.assertGreater(len(index), 50)
        self.assertIn("week", index[0])
        self.assertIn("skill", index[0])

    def test_extract_week_day(self):
        code, result = run_cli(
            "--csv", str(INTEGRATION_CSV), "--week", "1", "--day", "2"
        )
        self.assertEqual(code, 0)
        current = result["current"]
        self.assertEqual(current["week"], "1")
        self.assertEqual(current["day"], "2")
        self.assertTrue(current.get("content"))
        self.assertNotIn("skill_raw", current)

    def test_include_prior_smart_meta(self):
        code, result = run_cli(
            "--csv",
            str(INTEGRATION_CSV),
            "--week",
            "8",
            "--day",
            "22",
            "--include-prior",
        )
        self.assertEqual(code, 0)
        meta = result["prior_skills_meta"]
        self.assertEqual(meta["mode"], "smart")
        self.assertGreater(meta["total_prior"], 0)
        self.assertLessEqual(meta["returned"], meta["total_prior"])
        self.assertEqual(meta["returned"], len(result["prior_skills"]))

    def test_prior_full_returns_all(self):
        code, result = run_cli(
            "--csv",
            str(INTEGRATION_CSV),
            "--week",
            "8",
            "--day",
            "22",
            "--include-prior",
            "--prior-full",
        )
        self.assertEqual(code, 0)
        meta = result["prior_skills_meta"]
        self.assertEqual(meta["mode"], "full")
        self.assertEqual(meta["returned"], meta["total_prior"])

    def test_search_lightweight(self):
        code, result = run_cli(
            "--csv", str(INTEGRATION_CSV), "--search", "tailwind"
        )
        self.assertEqual(code, 0)
        self.assertGreater(result["count"], 0)
        self.assertEqual(result["count"], len(result["matches"]))
        self.assertNotIn("content", result["matches"][0])

    def test_missing_lesson_exits_nonzero(self):
        code, payload = run_cli(
            "--csv", str(INTEGRATION_CSV), "--week", "99", "--day", "1"
        )
        self.assertEqual(code, 1)
        self.assertIn("error", payload)

    def test_hito_lookup(self):
        code, listed = run_cli("--csv", str(INTEGRATION_CSV), "--list")
        self.assertEqual(code, 0)
        hito = next(l for l in listed["lessons"] if l["is_milestone"])
        code, result = run_cli(
            "--csv",
            str(INTEGRATION_CSV),
            "--week",
            hito["week"],
            "--day",
            hito["day"],
        )
        self.assertEqual(code, 0)
        self.assertTrue(result["current"]["is_milestone"])
        self.assertIn(hito["week"], result["current"]["skill"])

    def test_autodiscover_from_workspace(self):
        """When cwd is workspace and only one CSV under docs/syllabus, no --csv needed."""
        if not CSV.is_file():
            self.skipTest("docs/syllabus CSV missing")
        # Isolate: search only ai-engineering-syllabus so legacy CSVs elsewhere ignore
        code, payload = run_cli(
            "--list-csvs",
            "--search-root",
            str(WORKSPACE_ROOT / "ai-engineering-syllabus"),
        )
        self.assertEqual(code, 0)
        self.assertGreaterEqual(payload["count"], 1)
        if payload["count"] == 1:
            code, result = run_cli(
                "--week",
                "1",
                "--day",
                "2",
                "--search-root",
                str(WORKSPACE_ROOT / "ai-engineering-syllabus"),
            )
            self.assertEqual(code, 0)
            self.assertEqual(result["current"]["week"], "1")


@unittest.skipUnless(INTEGRATION_CSV is not None, "syllabus CSV not found")
class TestBuildPriorSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lessons = load_syllabus(str(INTEGRATION_CSV.resolve()))

    def test_smart_prior_is_chronological(self):
        idx = _lesson_index(self.lessons, "8", "22")
        prior, _ = build_prior_skills(
            self.lessons, idx, mode="smart", window=15)
        positions = []
        for p in prior:
            for i, lesson in enumerate(self.lessons[:idx]):
                if lesson["week"] == p["week"] and lesson["day"] == p["day"]:
                    positions.append(i)
                    break
        self.assertEqual(positions, sorted(positions))

    def test_milestones_only(self):
        idx = _lesson_index(self.lessons, "8", "22")
        prior, meta = build_prior_skills(self.lessons, idx, mode="milestones")
        self.assertTrue(all(p["is_milestone"] for p in prior))
        self.assertEqual(meta["mode"], "milestones")


if __name__ == "__main__":
    unittest.main()
