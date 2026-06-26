# In-Class Example: Nightly Report Sync — Community Garden App

> **For instructors:** Parallel classroom scenario for `ai-eng-cronjobs`. Same spine (independent CLI script, `job_runs` state machine, distributed lock, idempotency, CSV export, subprocess trigger, `TARGET_DATE`, structured logs), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_These instructions are also available in [Spanish](./README.es.md)._

---

## The challenge

### Scope note

This example is scoped for one live classroom session. It keeps the same patterns as the official student project but uses a tiny pre-built **community garden** app: volunteer shift sign-ups instead of company telemetry. Secondary requirements (full Prefect pipeline, production Docker cron) are simplified — see notes below.

A local garden collective tracks volunteer shifts in a SQLite database. Every night, a coordinator used to manually export yesterday's sign-ups and run a small aggregation script. Your job is to automate that with a background job that never blocks the Flask admin UI.

> **From the tech lead's ticket:**
>
> - The nightly script is a standalone process — not part of the Flask request cycle.
> - If a run is already `processing`, the next trigger aborts silently.
> - Failed runs must end as `failed`, never stuck in `processing`.
> - Running twice for the same date must not duplicate the CSV or re-run the aggregator.
> - Every run is logged with timestamp, job name, and status.

---

## Codebase overview

```text
admin/                 Flask read-only dashboard (do not modify request handlers for the job)
db/
  shifts.db            SQLite: volunteer_shift table
scripts/
  nightly_sync.py      ← implement this
  aggregate_shifts.py  Pre-built: reads CSV, prints summary to stdout (simulates pipeline)
services/
  job_runner.py        ← implement this
data/raw/              CSV output directory
```

---

## What to build

### Data model

- [ ] Create `job_runs` table (same fields as the student project: `id`, `job_name`, `status`, `started_at`, `finished_at`, `error_message`, `created_at`).
- [ ] Add optional `target_date` column for idempotency checks.

### `services/job_runner.py`

- [ ] Functions to create, update, and query `job_runs`.
- [ ] `has_processing_lock('nightly_sync')` and `has_completed_for_date('nightly_sync', date)`.

### `scripts/nightly_sync.py`

- [ ] Read `TARGET_DATE` env or default to yesterday.
- [ ] Distributed lock: abort silently if another `processing` row exists.
- [ ] Idempotency: skip if `completed` exists for `target_date`.
- [ ] Export `volunteer_shift` rows for `target_date` to `data/raw/shifts_YYYY-MM-DD.csv` **only if file missing**.
- [ ] Run `python scripts/aggregate_shifts.py data/raw/shifts_YYYY-MM-DD.csv` as subprocess.
- [ ] Update `job_runs` through full state machine; catch exceptions → `failed`.

### Trigger (classroom simplification)

- [ ] For class: run manually and demonstrate two terminals launching the script at once.
- [ ] Homework extension: add a crontab line `0 2 * * *` in the PR notes (not required live).

### Logging

- [ ] INFO for start, complete, skip, cancel; ERROR for failures.
- [ ] Each line: timestamp, `nightly_sync`, resulting status.

---

## Verify together

- [ ] `python scripts/nightly_sync.py` works without starting Flask.
- [ ] CSV appears in `data/raw/` with correct date in filename.
- [ ] Two simultaneous runs: one completes, one logs cancellation.
- [ ] Second run same day: skip log, no new subprocess call.
- [ ] Break aggregator (bad path): `job_runs` shows `failed`, not `processing`.
- [ ] `TARGET_DATE=2025-06-01 python scripts/nightly_sync.py` exports that date.

---

## Discussion questions

1. Why must the nightly script be a separate process instead of a Flask background thread started on first request?
2. The distributed lock uses a `processing` row in the database. What happens if the server crashes mid-run before `failed` or `completed` is written? How would you recover in production?
3. Idempotency checks both the `job_runs` table and the CSV file existence. Why are both layers useful instead of relying on only one?
