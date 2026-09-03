---
name: readme-project-orchestrator
description: Orchestrate end-to-end project creation from one or two README files in ai-engineering-syllabus: create/update translations, generate .learn/solution with the solution skill, configure learn.json with the learnpack skill, and produce preview plus sharing metadata using the social-sharing skill. Use when the user asks to create a new project from README instructions.
---

# README Project Orchestrator

## CRITICAL — first and last actions

**Do NOT scaffold projects by hand.** Manual copy of READMEs + hand-written `learn.json` skips preview generation.

### First action (required)

Run the orchestrator script from workspace root (`AIE-Projects`):

```bash
python3 ai-engineering-syllabus/.cursor/skills/readme-project-orchestrator/scripts/orchestrate_project_from_readme.py \
  --repo-root ai-engineering-syllabus \
  --target-slug "<target-slug>" \
  --source-readme "<absolute-or-relative-path-to-readme>" \
  --source-readme-es "<optional-path-to-readme-es>" \
  --classroom-example ask
```

The script bootstraps Phases 0–4 and invokes `generate-project-social-sharing` for `.learn/preview.png` + `sharing`.

### Last check before closing the task (required)

- Confirm `ai-engineering-syllabus/content/projects/<target_slug>/.learn/preview.png` **exists on disk** (not only a URL in `learn.json`).
- If missing, run Phase 4 (social-sharing script scoped to `--slug`) before reporting completion.

### Anti-patterns (invalid completion)

- Writing `README.md`, `learn.json`, and solution files without running the orchestrator script first.
- Setting `learn.json.preview` to a GitHub raw URL without generating the local `preview.png` file.
- Marking the task done when Phase 4 was never executed.
- Shipping `learn.json` **without** `telemetry.batch` (including “waiting for `asset_id`” — empty `asset_id=` is required instead).

Manual phases below are **fallback only** when the script fails or needs enrichment (solution quality, classroom brief, translation pass).

## Purpose

Use this skill to build a complete project folder under `content/projects/<slug>` from README input, applying existing specialized skills in a safe order.

This orchestrator must cover:

1. README translation (if missing or requested)
2. Solution generation
3. `learn.json` configuration
4. Social-sharing preview and sharing metadata

## Inputs required

- `source_readme_path` (required): path to source README
- `source_readme_es_path` (optional): Spanish README path
- `target_slug` (required): final project slug
- `target_projects_root` (default): `content/projects`

If `source_readme_es_path` is missing, infer translation direction from the source file name and generate the counterpart README.

## What is not a classroom example brief

Do **not** ask the user whether to include narrative blocks inside the student README (e.g. CTO briefs, quoted requirements, minimum deliverables in the challenge section). Those belong in `README.md` / `README.es.md` as provided.

A **classroom example brief** (Spanish curriculum label: _enunciado de ejemplo_) means only the instructor files under `.learn/example/` (Phase 5 + `classroom-example-brief`). Ask about that once before scaffolding if `--classroom-example ask`, or respect `yes` / `no` flags.

## Workflow

The **required default path** is the automation command at the end of this document. It runs Phases 0–4 in one step.

Use the manual phase descriptions below only as **fallback** when the script fails or when enriching outputs after a successful script run.

### Phase 0 - Prepare target project folder

1. Create target folder:
   - `content/projects/<target_slug>/`
2. Ensure structure exists:
   - `README.md`
   - `README.es.md`
   - `.learn/solution/`
3. Copy provided README files as initial content.

### Phase 1 - Translation (if needed)

Apply the repository translation rule:

- If source is `README.es.md` (or equivalent), generate/update `README.md` in English.
- If source is `README.md`, generate/update `README.es.md` in Spanish.

Do not change markdown structure, links, code blocks, or section layout.

### Phase 2 - Generate solution (specialized skill)

Use the project solution skill:

- Skill: `module-project-solution-reference-generator/SKILL.md` (project solution file workflow)
- Create/update `.learn/solution/README.md` as canonical solution entry.
- Add any additional solution artifacts only if required by the project type.

Minimum expected output:

- `.learn/solution/README.md`

### Phase 3 - Configure `learn.json` (specialized skill)

Use the LearnPack config skill:

- Skill: `learnpack-learn-json-config/SKILL.md`
- Create/update `learn.json` at project root.

Required fields baseline:

- `slug`
- `title.en`, `title.es`
- `description.en`, `description.es`
- `projectType: "project"`
- `difficulty`
- `duration`
- `technologies`
- `translations: ["es", "en"]`
- `solution`
- `preview`
- `telemetry` (**mandatory** — see below)

### Telemetry (mandatory at scaffold time)

Always write:

```json
"telemetry": {
  "batch": "https://breathecode.herokuapp.com/v1/assignment/me/telemetry?asset_id="
}
```

- The `telemetry` attribute is **required** on every new project `learn.json`.
- A numeric BreatheCode `asset_id` is **not** expected when creating the project. Do not ask for it, invent it, or omit `telemetry` while waiting for one.
- Empty `asset_id=` is the correct default. A filled id later is fine; leave existing numeric ids untouched unless asked.
- Never put `batch` at the root of `learn.json`.

Keep other values consistent with README scope and rubric.

### Phase 4 - Social sharing + preview

Skill: `ai-engineering-syllabus/.cursor/skills/generate-project-social-sharing/SKILL.md`

**This phase is not optional.** Every new project must have:

- `.learn/preview.png` on disk for the target slug
- `learn.json.preview` pointing to the raw GitHub URL
- Bilingual `learn.json.sharing` (`en` + `es`)

**Required execution** (scoped to target slug only):

```bash
python3 ai-engineering-syllabus/.cursor/skills/generate-project-social-sharing/scripts/generate_project_social_assets.py \
  --project-root ai-engineering-syllabus \
  --slug "<target-slug>" \
  --sharing-link-template "https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/{slug}"
```

The orchestrator script runs this automatically after scaffolding. If you scaffolded manually, you **must** run it before closing the task.

Do not run global regeneration across all projects unless the user explicitly requests it.

**Fallback only:** if the script is unavailable, use Playwright against `assets/cover/cover-template.html` — but prefer fixing the script environment over manual screenshots.

### Phase 5 - Classroom example brief for instructors (post-generation)

After Phases 0–4 complete, ask whether the project needs an **instructor classroom example brief** under `.learn/example/` (separate from the student README, from CTO/stakeholder quotes in the README, and from `.learn/solution/`).

- Skill: `classroom-example-brief/SKILL.md`
- Outputs when accepted: `.learn/example/README.md` and `.learn/example/README.es.md`
- Purpose: shorter parallel scenario (different domain, same technical spine) for live class demos

**How the question is asked:**

The script `orchestrate_project_from_readme.py` runs this step **after** scaffolding finishes:

| Mode                                | Behavior                                                                                                                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--classroom-example ask` (default) | Interactive `[y/N]` prompt when stdin is a TTY                                                                                                     |
| `--classroom-example yes`           | Scaffolds `.learn/example/INSTRUCTIONS.md` and reports `classroom_example=yes`; agent must still run `classroom-example-brief` to write the briefs |
| `--classroom-example no`            | Skips; reports `classroom_example=no`                                                                                                              |
| `ask` + non-interactive (agent/CI)  | Prints `classroom_example=ask_required`; agent must ask the user in chat, then re-run with `yes` or `no`, or apply the skill directly if `yes`     |

**Report requirement:** Final orchestration report must state `classroom_example: yes | no | ask_required`.

If the user answers yes, apply `classroom-example-brief` before closing the task (unless they explicitly defer generation).

## Automation command (required default path)

Run from workspace root (`AIE-Projects`) for every new project from README:

```bash
python3 ai-engineering-syllabus/.cursor/skills/readme-project-orchestrator/scripts/orchestrate_project_from_readme.py \
  --repo-root ai-engineering-syllabus \
  --target-slug "<target-slug>" \
  --source-readme "<absolute-or-relative-path-to-readme>" \
  --source-readme-es "<optional-path-to-readme-es>" \
  --classroom-example ask
```

Notes:

- The orchestrator bootstraps `README.md`, `README.es.md`, `.learn/solution/README.md`, and `learn.json`.
- It then calls `generate-project-social-sharing` scoped by `--slug` to generate `.learn/preview.png` and `sharing` for the target project only.
- If a translation file is not provided, it creates a fallback counterpart that must be replaced with a proper translation pass.
- After scaffolding, use `--classroom-example ask` (default) to prompt for instructor example briefs, or pass `yes` / `no` when running non-interactively.

## Validation checklist (must pass — task incomplete if any fail)

- [ ] Orchestrator script ran successfully (or social-sharing script ran after manual fallback).
- [ ] `README.md` and `README.es.md` both exist and are aligned.
- [ ] `.learn/solution/README.md` exists and matches project requirements.
- [ ] `learn.json` is valid JSON and includes `solution`, `preview`, and mandatory `telemetry.batch` (empty `asset_id=` OK; not a top-level `batch`).
- [ ] **`.learn/preview.png` exists on disk** and is not an empty file — a `preview` URL alone is insufficient.
- [ ] `learn.json.sharing` exists with bilingual (`en`, `es`) messages.
- [ ] All URLs in `learn.json` point to `content/projects/<target_slug>/...`.
- [ ] Phase 4 was executed (preview generated + sharing updated) before finalizing.
- [ ] Phase 5 decision recorded: `classroom_example` is `yes`, `no`, or `ask_required`.
- [ ] If `classroom_example` is `yes`, `.learn/example/README.md` and `.learn/example/README.es.md` exist (via `classroom-example-brief`).

## Response format after execution

Return a concise report with:

1. Created/updated files
2. Translation actions performed
3. Which specialized skills were used per phase
4. `classroom_example`: `yes` | `no` | `ask_required` (and next step if `yes`)
5. Final validation status (must include `preview_generated: yes` only when `.learn/preview.png` exists on disk)
