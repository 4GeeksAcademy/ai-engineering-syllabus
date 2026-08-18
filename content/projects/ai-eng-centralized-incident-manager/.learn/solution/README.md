# Centralized Incident Manager — Reference Solution

## Purpose

This is an **incident manager** delivery (model + seed + REST + three UI panels). It is **not** an auth project. Do not document JWT, password hashing, login responses, or `get_current_user` here — those live in the user-authentication projects.

Field names, categories, branch values, and CSV → model maps come from the student's `CONTEXT-company.md` under `content/contexts/centralized-incident-manager/`.

## Expected layout

```text
scripts/
  seed_incidents.py
  incidents-COMPANY.csv          # from the analyzer project / CONTEXT
packages/shared/                 # CSV validation reused from analyzer
services/api/                    # FastAPI incident routes
uis/backoffice/                  # registration, list, summary
```

## Required coverage (from README)

### Model

`Incident` with: `id`, `title`, `description`, `category` (CONTEXT set), `status` (`open` | `in_progress` | `resolved` | `discarded`), `origin` (`customer` | `branch` | `internal`), `branch` (CONTEXT values including `central`), `created_at`, `updated_at`. Constraints on required fields and allowed enums.

### Seed (`scripts/seed_incidents.py`)

- Read the analyzer CSV; assign `origin: "customer"` to every inserted row.
- Apply CONTEXT maps **before** insert: status, category, `description` → `title`, `date` → `created_at`, location → `branch`.
- Reuse analyzer validation from `packages/shared/` — invalid rows are skipped and printed at the end.
- Idempotent: a second run does not duplicate (match on a stable CSV identity field).

After seed, `GET /api/incidents/summary` totals by **model** `status` and `category` must match the transformed expected values in CONTEXT (same valid-record set as the analyzer).

### Backend

| Method  | Path                         | Notes                                                                 |
| ------- | ---------------------------- | --------------------------------------------------------------------- |
| `POST`  | `/api/incidents`             | `400` with `{ field, message }` on validation errors                  |
| `GET`   | `/api/incidents`             | filters: `status`, `origin`, `branch`, `category`; empty list if none |
| `GET`   | `/api/incidents/{id}`        | `404` if missing                                                      |
| `PATCH` | `/api/incidents/{id}/status` | lifecycle only (see below)                                            |
| `GET`   | `/api/incidents/summary`     | totals by status, category, origin, branch; zeros if empty            |

**Lifecycle:** `open` → `in_progress` \| `discarded`; `in_progress` → `resolved` \| `discarded`; `resolved` and `discarded` are final. Invalid transition → `400`. Unhandled errors → `500` generic body, never a stack trace.

### Frontend (`uis/backoffice`)

**Registration form**

- All model fields; `branch` always visible/required; options = CONTEXT values with **display labels** (not raw slugs).
- When `origin` is `branch`, visually highlight the `branch` field.
- Loading: disable submit; field-level plain-language errors; success clears the form.

**List**

- Filters: `status`, `origin`, `branch`.
- States: loading, empty (message, not a blank table), data.
- Inline status update; on failure revert UI and notify.

**Summary**

- Consume `/api/incidents/summary`. Failure/loading must not break the rest of the page.

## Indicative API responses

### `GET /api/incidents/summary` (after seed)

```json
{
  "by_status": { "open": 12, "in_progress": 4, "resolved": 80, "discarded": 4 },
  "by_category": {},
  "by_origin": { "customer": 100, "branch": 0, "internal": 0 },
  "by_branch": {}
}
```

Totals must match CONTEXT after the CSV → model transform. Do not copy the numbers above.

### Invalid status transition

```json
{
  "field": "status",
  "message": "Cannot move from resolved to open."
}
```

## Validation notes

- Seed twice; row count unchanged.
- `PATCH` a `resolved` incident to `open` → `400`.
- Empty DB: list `[]`, summary zeros, no 500.
- Browser: register (highlight when origin=branch) → list filters → summary.
- No JWT/login checks belong in this rubric.

## Reviewer checklist

- [ ] Model + enums match CONTEXT
- [ ] Seed transforms CSV → model; invalid rows reported; idempotent
- [ ] Five endpoints + lifecycle + no stack traces
- [ ] Form, list (3 states), summary; branch highlight when `origin=branch`
- [ ] Shared validation in `packages/shared/`
