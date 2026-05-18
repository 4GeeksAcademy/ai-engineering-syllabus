---
name: readme-project-orchestrator
description: Orchestrate end-to-end project creation from one or two README files in ai-engineering-syllabus: create/update translations, generate .learn/solution with the solution skill, configure learn.json with the learnpack skill, and produce preview plus sharing metadata using the social-sharing skill. Use when the user asks to create a new project from README instructions.
---

# README Project Orchestrator

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

## Workflow

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

- Skill: `project-solution-generator/SKILL.md` (project solution file workflow)
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
- `telemetry.batch` (BreatheCode assignment telemetry URL; must live under a `telemetry` object, not as a top-level `batch` key)

Example:

```json
"telemetry": {
  "batch": "https://breathecode.herokuapp.com/v1/assignment/me/telemetry?asset_id="
}
```

Keep values consistent with README scope and rubric.

### Phase 4 - Social sharing + preview (specialized skill)

Use the social-sharing skill:

- Skill: `generate-project-social-sharing/SKILL.md`
- Generate `.learn/preview.png` for the **target project only**
- Update `learn.json.preview` with the raw GitHub URL
- Generate/refresh bilingual `learn.json.sharing`

This phase is **mandatory** for every new project created with this orchestrator.

Recommended execution for single-project scope:

1. Generate preview image directly from the cover template (target project only):

```bash
npx playwright screenshot --viewport-size=1024,576 "file://<repo-root>/assets/cover/cover-template.html?title=<url-encoded-title-en>&author=by%204Geeks%20Academy&image=<url-encoded-image-path>" "content/projects/<target_slug>/.learn/preview.png"
```

2. Set in `content/projects/<target_slug>/learn.json`:

```json
"preview": "https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/<target_slug>/.learn/preview.png"
```

3. Add or refresh `sharing` with at least 2 bilingual entries (`en` + `es`) and project URL based on `<target_slug>`.

If you choose to run the automation script from `generate-project-social-sharing`, you must ensure the change set is limited to `content/projects/<target_slug>/...` and avoid unintended updates to other projects.

Safety rule:

- Do not run global regeneration across all projects unless the user explicitly requests it.
- Apply social-sharing only to the target project.

### Phase 5 - Classroom example brief for instructors (post-generation)

After Phases 0–4 complete, the orchestrator script asks whether the project needs an **instructor classroom example brief** under `.learn/example/` (separate from the student README and from `.learn/solution/`).

- Skill: `classroom-example-brief/SKILL.md`
- Outputs when accepted: `.learn/example/README.md` and `.learn/example/README.es.md`
- Purpose: shorter parallel scenario (different domain, same technical spine) for live class demos

**How the question is asked**

The script `orchestrate_project_from_readme.py` runs this step **after** scaffolding finishes:

| Mode | Behavior |
|------|----------|
| `--classroom-example ask` (default) | Interactive `[y/N]` prompt when stdin is a TTY |
| `--classroom-example yes` | Scaffolds `.learn/example/INSTRUCTIONS.md` and reports `classroom_example=yes`; agent must still run `classroom-example-brief` to write the briefs |
| `--classroom-example no` | Skips; reports `classroom_example=no` |
| `ask` + non-interactive (agent/CI) | Prints `classroom_example=ask_required`; agent must ask the user in chat, then re-run with `yes` or `no`, or apply the skill directly if `yes` |

**Report requirement:** Final orchestration report must state `classroom_example: yes | no | ask_required`.

If the user answers yes, apply `classroom-example-brief` before closing the task (unless they explicitly defer generation).

## Automation command (recommended)

Use this command as the default execution path for new projects from README:

```bash
python3 .cursor/skills/readme-project-orchestrator/scripts/orchestrate_project_from_readme.py \
  --repo-root . \
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

## Validation checklist (must pass)

- [ ] `README.md` and `README.es.md` both exist and are aligned.
- [ ] `.learn/solution/README.md` exists and matches project requirements.
- [ ] `learn.json` is valid JSON and includes `solution`, `preview`, and `telemetry.batch` (not a top-level `batch`).
- [ ] `.learn/preview.png` exists and is not an empty placeholder.
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
5. Final validation status
