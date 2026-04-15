---
name: learnpack-learn-json-config
description: Configure and validate LearnPack `learn.json` files for 4Geeks/learnpack repositories, including `projectType`, `grading`, `localhostOnly`, `gitpod`, delivery, editor, and metadata fields, plus mapping to BreatheCode asset behavior (`interactive`, `gitpod`, modal/iframe flows). Use when asked to create, update, review, or troubleshoot `learn.json` configuration.
---

# LearnPack `learn.json` Configuration (4Geeks + LearnPack)

## Purpose

Use this skill to create, update, or audit `learn.json` so the repository behaves correctly in:

- LearnPack local/editor flows.
- 4Geeks BreatheCode asset sync and UI behavior (interactive CTA, cloud provisioning, local clone modal).

## Step 1 - Locate and load configuration

Before editing:

1. Locate the active config file in this order:
   - `learn.json`
   - `.learn/learn.json`
   - `bc.json`
   - `.learn/bc.json`
2. Read the full current file.
3. Preserve existing valid fields unless the user asked to change them.

## Step 2 - Apply core LearnPack fields

When creating/updating `learn.json`, prioritize these keys:

- `slug`, `title`, `description`, `preview`
- `projectType` (`tutorial`, `exercise`, or `project` according to repo intent)
- `grading` (`incremental` or `isolated`)
- `localhostOnly`
- `gitpod` (optional explicit override)
- `technologies`
- `difficulty`
- `editor` (`mode`, `agent`, `version`)
- `delivery` (instructions, formats, regex/quantity when needed)
- `duration`, `video`, `authentication`, `assessment` when requested
- `repository` (recommended, especially for cloud provisioning and Codespaces links)
- `autoPlay` (optional behavior control)
- `sharing` (recommended social copy in multilingual assets)

Keep language objects consistent when multilingual content exists (for example `title.en`/`title.es`).

## Step 2.1 - Baseline templates by asset type

Use the correct baseline depending on whether the asset is an `exercise` or a `project`.

### Dual-coverage baseline (exercise or project)

These fields are recommended for both asset types:

- `slug`
- `title` (prefer multilingual object: at least `en` and `es`)
- `description` (prefer multilingual object: at least `en` and `es`)
- `difficulty` (`beginner`, `easy`, `intermediate`, `hard`)
- `projectType` (must match real intent)
- `preview`
- `sharing` (array with bilingual entries for social share copy)
- `technologies`
- `grading`
- `localhostOnly`
- `gitpod` (optional explicit override)
- `editor`
- `delivery` (if submission constraints are required)

### Project-only recommended additions

When `projectType` is `project`, additionally recommend:

- `duration`
- `autoPlay` (explicit true/false)
- `repository`
- `template_url` only when project template behavior is expected

### Exercise-only considerations

When `projectType` is `exercise`:

- Keep config lean; include `delivery` only if needed.
- Avoid `template_url` unless explicitly supported by the current backend flow.

## Step 3 - Enforce 4Geeks asset behavior rules

For BreatheCode sync, these are the critical rules:

1. `interactive` is not a direct top-level config in practice for BreatheCode mapping; it is derived from `projectType`, `grading`, and `localhostOnly`.
2. If `projectType` is `tutorial` -> interactive flow is enabled; `gitpod` depends on `localhostOnly`.
3. If `grading` is `incremental` or `isolated` -> interactive flow is enabled; `gitpod` defaults to `!localhostOnly`.
4. If `gitpod` is explicitly provided, it overrides the computed `gitpod`.
5. **Set `gitpod: true` when the repository contains runnable code at its root** (e.g., `app.py`, `index.js`, `main.ts`, `Dockerfile`, etc.) instead of just a project brief README. This signals that the repo needs a cloud environment to run. If it is not clear whether the repo is code-first or brief-only, **ask the user before deciding**.

Use these presets:

### Interactive + cloud provisioning enabled (typical)

```json
{
  "projectType": "exercise",
  "grading": "incremental",
  "localhostOnly": false,
  "gitpod": true
}
```

### Interactive but without cloud provisioning links in modal

```json
{
  "projectType": "exercise",
  "grading": "incremental",
  "localhostOnly": true,
  "gitpod": false
}
```

## Step 4 - Distinguish learn.json vs registry-only fields

Do not attempt to set `learnpack_deploy_url` in `learn.json` (registry/admin-side field).

Remember:

- `learnpack_deploy_url` + cohort SaaS availability controls iframe/start-interactive header flow.
- `gitpod: true` + provisioning vendors control cloud links in clone/provisioning modal.
- Repository URL quality affects Codespaces link generation.

## Step 5 - Validate project-specific constraints

Before finalizing:

- If `projectType` is `project`, `template_url` may be valid (for example `"self"`).
- If asset is exercise-style, avoid `template_url` unless explicitly supported.
- Choose `grading` semantically:
  - `incremental`: cumulative progression.
  - `isolated`: independent steps.
- Ensure `delivery` matches expected submission type (`url`, `flags`, etc.).
- Validate `difficulty` against allowed values only: `beginner`, `easy`, `intermediate`, `hard`. Propose a value based on the project scope and perceived complexity if not already set:
  - `beginner`: single concept, minimal setup, very guided.
  - `easy`: a few concepts, some autonomy, clear steps.
  - `intermediate`: multiple concepts, moderate autonomy, some design decisions.
  - `hard`: complex scope, significant autonomy, architecture or integration decisions required.
- Prefer multilingual consistency (`title.en`/`title.es`, `description.en`/`description.es`) in 4Geeks content.
- Ensure `preview` and `repository` URLs are valid and stable.

### Project-only validation

Apply these checks only when `projectType` is `project`:

- `duration` is present with realistic estimation.
- `repository` points to the canonical student/template repository.
- `sharing` entries, if present, include both `en` and `es`.
- `template_url` is coherent with project template strategy.

### Exercise-only validation

Apply these checks only when `projectType` is `exercise`:

- Do not require `duration` or `template_url`.
- Confirm `grading` and progression model reflect exercise design (incremental vs isolated).

## Step 5.1 - Disallowed/deprecated keys guard

Unless explicitly required by a legacy workflow, avoid adding:

- `assignments`
- `builder`

If they already exist, preserve them only when the user asks for backward compatibility.

## Step 6 - Output behavior

When responding after edits:

1. Briefly state what changed in `learn.json`.
2. Explain expected runtime/UI behavior (interactive, cloud/local options).
3. Flag any required non-repo actions (for example registry `learnpack_deploy_url` setup).

## Quick checklist

- [ ] Config file path detected correctly.
- [ ] JSON remains valid and consistent.
- [ ] `projectType` and `grading` align with pedagogy.
- [ ] `localhostOnly` and `gitpod` produce intended cloud/local UX.
- [ ] No registry-only fields were incorrectly added to `learn.json`.
- [ ] Delivery/editor fields match the learning flow.
- [ ] `difficulty` uses only allowed values.
- [ ] Multilingual fields are consistent when bilingual content is expected.
- [ ] Project-only fields were applied only to `project` assets.
- [ ] Exercise configs remain minimal and do not force project-only fields.
- [ ] No disallowed keys (`assignments`, `builder`) were introduced unintentionally.

## References

- LearnPack docs: [learnpack-configuration.md](https://raw.githubusercontent.com/learnpack/docs/refs/heads/main/learnpack-configuration.md)
- BreatheCode mapping + UI behavior: [LEARNPACK_CONFIGURATION.es.md](https://raw.githubusercontent.com/breatheco-de/apiv2/794d6c969a9b70e73157ba9a25c5aeafc32d079e/breathecode/registry/LEARNPACK_CONFIGURATION.es.md)
