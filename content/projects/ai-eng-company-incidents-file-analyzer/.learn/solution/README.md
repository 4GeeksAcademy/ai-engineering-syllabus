# Company Incident File Analysis — Reference Solution

## Purpose

Two phases, one shared core: a CLI that validates the CONTEXT CSV, then the same logic behind FastAPI + a backoffice upload page. A CLI-only submission fails the Backend/Frontend evals.

Copy the official CSV from `content/contexts/incidents-file-analysis/` (e.g. `incidents-brasaland.csv`). Expected counts in CONTEXT must match the shipped file.

## Expected layout

```text
scripts/
  analyze.py                 # Phase 1 CLI
  incidents-COMPANY.csv      # official sample
packages/shared/             # validation + metrics (script AND API)
services/api/                # POST analyze + GET export
uis/backoffice/              # upload + summary + download
```

Do **not** put `analyze.py` at the repo root. Do **not** use `uis/web`.

---

## Phase 1 — CLI (`scripts/analyze.py`)

```bash
python scripts/analyze.py scripts/incidents-COMPANY.csv
```

Functions with single responsibilities: parse args, load CSV, validate, aggregate, print, optional export.

### Validation (CONTEXT rules)

Invalid when any CONTEXT constraint fails, at minimum:

- Missing required fields
- Category/status outside the allowed set
- Incomplete description (if CONTEXT sets a min length)
- Closed incidents without score (if CONTEXT requires it)
- Scores outside the accepted range

Invalid records: counted, classified by reason, excluded from valid-only metrics, reported (never silent).

### Metrics (valid records only)

1. Total processed, valid, invalid
2. Breakdown by category
3. Breakdown by status
4. Satisfaction for closed+scored: count, average (optional score distribution)

Official sample: numeric totals must match CONTEXT **exactly**.

### CSV export prompt

`Export results to CSV? [y / n]`

- `y` → `results.csv` (`metric`, `value`, optional `percentage`)
- `n` → no file

---

## Phase 2 — Platform

Extract the same validation/metrics into `packages/shared/` (or equivalent). The router **imports** that module — it does not copy-paste the script.

### Backend

| Method | Path                            | Notes                                                 |
| ------ | ------------------------------- | ----------------------------------------------------- |
| `POST` | `/api/incidents/analyze`        | `multipart/form-data` CSV; JSON summary = CLI metrics |
| `GET`  | `/api/incidents/results/export` | last analysis as downloadable CSV                     |

Empty file / bad format → appropriate HTTP status + descriptive message (not a traceback).

### Frontend (`uis/backoffice`)

- Menu entry for incident analysis
- Upload (drag-drop or file picker) → `POST /api/incidents/analyze`
- On-screen summary: general metrics, category, status, satisfaction
- Download button → `GET /api/incidents/results/export`
- Tell the user how many invalid records (and by type)

Light and dark mode if the backoffice already has a design system.

---

## Reviewer checklist

### Script

- [ ] `python scripts/analyze.py <csv>` works without code edits
- [ ] Invalid records classified and shown
- [ ] Five required metrics; official CSV matches CONTEXT
- [ ] `y/n` export works

### Backend / frontend

- [ ] Analyze endpoint returns the same summary as the CLI
- [ ] Export endpoint downloads CSV
- [ ] Input errors → HTTP error, not 500 stack trace
- [ ] Upload UI works without the terminal
- [ ] Invalid counts visible in the UI

### Cross-cutting

- [ ] One shared module — not two divergent implementations
- [ ] Layout: `scripts/` + `services/api/` + `uis/backoffice/`

## Notes

- Console spacing/styling may vary; values and sections must be present.
- Prioritize correctness and shared logic over cosmetic formatting.
