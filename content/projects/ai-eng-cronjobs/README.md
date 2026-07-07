# Background Processes

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company has a data pipeline and an API with instrumented telemetry. The problem is that someone has to run the pipeline every night. Your tech lead has filed the following ticket:

> > **Ticket #DEV-53 — Nightly Telemetry Script**
> >
> > We need a script that runs automatically every night without manual intervention. The script must export the previous day's telemetry data to CSV (if not already done), trigger the data pipeline, and record in the database what happened and when.
> >
> > **Acceptance criteria:**
> >
> > - The script is a fully independent process from the API — it must not block any endpoint or run on FastAPI's main thread.
> > - If the script is already running when the next cycle fires, the second instance must abort silently. No two parallel executions.
> > - If the script fails, that run's record in the database must end up as `failed`, not `processing`. No record may remain as a zombie.
> > - The script must be idempotent: running it twice on the same day must produce the same result as running it once.
> > - Every execution is logged with a timestamp, status (`pending` → `processing` → `completed` | `failed`), and, on error, the exception message.
> >
> > Put the script in `scripts/` and the status logic in `services/`. The trigger goes in crontab or the framework scheduler — your call, justify it in the PR.

### 📚 Complementary Knowledge — Background Task Lifecycle

Before writing a single line of code, there is an architectural concept you need to internalise: **in background processing, a piece of data doesn't just exist as "data" — it exists as a state.**

The canonical state machine for this kind of task is:

```
pending → processing → completed
                    ↘ failed
```

Each transition matters:

- **`pending`** — the task is waiting to be executed. The record is created before any work begins.
- **`processing`** — updated at the very start of execution, before doing any work. This is what prevents another process from picking up the same task.
- **`completed`** — updated only if everything finished successfully.
- **`failed`** — updated if any exception is caught. Must never remain as `processing`.

The **distributed lock is the `processing` status itself** — not a separate table, column, or flag. When the script starts, it transitions a `job_runs` row to `processing`. If another instance finds an existing `processing` row for `nightly_export`, it aborts silently. When the script finishes — successfully or not — the row moves to `completed` or `failed`, which releases the lock. Do not implement a second locking mechanism.

A script that implements this state machine can fail, restart, or run out of schedule and will always leave the system in a known, recoverable state.

### 📚 Complementary Knowledge — How This Fits the Monorepo

**`job_runs` ≠ `pipeline_runs`** — they are not duplicates:

| Table           | Layer                                | What it records                                                               |
| --------------- | ------------------------------------ | ----------------------------------------------------------------------------- |
| `job_runs`      | Nightly orchestration (this project) | CSV export, pipeline subprocess trigger, lock, and idempotency for the script |
| `pipeline_runs` | Internal ETL (Milestone 6)           | Extract/transform/load phases, watermark, rows processed                      |

The nightly script writes to `job_runs`. The pipeline subprocess writes to `pipeline_runs` during its own execution.

**CSV is a backup, not the pipeline input.** The script exports `telemetry_events` from the database to `data/raw/telemetry_YYYY-MM-DD.csv` for audit and recovery. The data pipeline you built in Milestone 6 reads from `telemetry_events` in the database (via SQL/watermark) — it does **not** read the CSV file. Do not wire the pipeline to consume the export file.

**Date and subprocess conventions:**

- **"Yesterday"** means the previous calendar day in **UTC** (`datetime.now(timezone.utc).date() - timedelta(days=1)`).
- **`TARGET_DATE=YYYY-MM-DD`** overrides the target date for testing without code changes.
- **Pipeline subprocess** (reference — adjust to your Milestone 6 entry point if different):

```bash
python -m data.pipelines.telemetry_kpi_daily.run --no-prefect
```

---

## 🌱 How to Start the Project

1. Review your monorepo: identify the existing telemetry tables and the naming conventions you have already used for paths and fields.
2. Create the job control table in the database (you can add it to the existing schema or create a new migration).
3. Implement the script in `scripts/nightly_export.py` and the status control service in `services/`.
4. Configure the trigger via OS `crontab` (recommended) or a dedicated scheduler container — not inside the FastAPI process. Document the cron expression in the PR.

---

## 💻 What You Need to Do

### Data model

- [ ] Create a `job_runs` table with at least the following fields: `id`, `job_name`, `target_date` (date — **required** for per-day idempotency), `status` (`pending` | `processing` | `completed` | `failed`), `started_at`, `finished_at`, `error_message`, `created_at`.
- [ ] Add an index on `(job_name, target_date)` so idempotency checks are efficient.
- [ ] Add the migration or SQL statement needed to create the table in the monorepo schema.
- [ ] Do **not** merge `job_runs` with `pipeline_runs` from Milestone 6 — they serve different layers (see architecture note above).

### Main script (`scripts/nightly_export.py`)

- [ ] Resolve `target_date` from `TARGET_DATE` env or default to **yesterday in UTC**.
- [ ] The script exports rows from `telemetry_events` for `target_date` to a CSV file in `data/raw/` (e.g. `telemetry_2025-01-15.csv`), **only if that file does not already exist**. The CSV is a backup/audit snapshot — the pipeline reads from the database, not this file.
- [ ] The script triggers the data pipeline as a subprocess once the export is complete (reference command: `python -m data.pipelines.telemetry_kpi_daily.run --no-prefect`, or your Milestone 6 CLI entry point).
- [ ] The script writes to `job_runs` the result of the execution (final status + `target_date` + timestamp + error if any).
- [ ] The script is executable directly from the command line: `python scripts/nightly_export.py`.

### Idempotency and locking

- [ ] **Lock via `processing`:** if a `job_runs` record already exists with `status = 'processing'` for `nightly_export`, the script aborts silently and logs the cancellation. No separate lock table or column.
- [ ] **Idempotency via `target_date`:** if a `completed` record already exists for `(job_name='nightly_export', target_date)`, the script does not re-export the CSV or re-trigger the pipeline. It logs that the execution was skipped as a duplicate. Checking only `job_name` without `target_date` is not sufficient.

### Status control (`services/`)

- [ ] Implement a `job_runner` module in `services/` with functions to create, update, and query `job_runs` records (including `has_processing_lock` and `has_completed_for_date`).
- [ ] Any unhandled exception must be caught, update the status to `failed` with the error message, and propagate the error to the log.
- [ ] No record may remain in `processing` status after a failed execution.

### Trigger

- [ ] Configure the cronjob via OS `crontab` or a **dedicated scheduler container** — recommended for production.
- [ ] **Do not** run the nightly script inside the FastAPI process (no `APScheduler`, `@repeat_every`, or lifespan hooks on the API server). A separate worker process is acceptable only if it does not share the API's main thread.
- [ ] Document the cron expression and implementation decision in the PR body.
- [ ] Add an optional `TARGET_DATE` environment variable (`YYYY-MM-DD`) to override the target date for testing without modifying the code.

### Observability

- [ ] Generate execution logs at `INFO` level for normal events (start, finish, skipped as duplicate) and `ERROR` for exceptions.
- [ ] Each log line includes a timestamp, job name, and resulting status.

---

## ✅ What We Will Evaluate

- [ ] The script is an independent process: it does not import or execute FastAPI code on the application's main thread.
- [ ] The `pending → processing → completed | failed` state machine is implemented and `job_runs` records reflect the actual status of each execution, including `target_date`.
- [ ] The `processing` status acts as the distributed lock (no separate lock mechanism): demonstrable by launching two instances of the script simultaneously.
- [ ] The script is idempotent per `target_date`: running it twice for the same day produces the same result as running it once, without duplicating CSV files or pipeline executions.
- [ ] No record remains in `processing` status after a failure: the `try/except/finally` block guarantees the transition to `failed`.
- [ ] The CSV output exists in `data/raw/` with the correct name and contains telemetry data exported from `telemetry_events` for the target date (backup only — pipeline reads from DB).
- [ ] `job_runs` and `pipeline_runs` coexist without duplication of responsibilities.
- [ ] Logs include timestamp, job name, and status on every relevant event.
- [ ] The trigger is configured and the cron expression documented in the PR.
- [ ] `TARGET_DATE` allows the script to run on arbitrary dates without modifying the code.

---

## 📦 How to Submit

1. Make sure all checklist items are completed.
2. Push your branch to the repository.
3. Open a **Pull Request** from your branch to `main`.
4. In the PR body include:
   - The cron expression configured and the method chosen (crontab vs. framework scheduler), with a brief justification.
   - A sample log of a successful execution and one of a failed or blocked execution.
   - A screenshot or excerpt of the generated CSV (first few rows).
5. Add the `cronjob` label to the PR before submitting it for review.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
