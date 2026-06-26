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

The **Distributed Lock** pattern complements the state machine: on startup, the script writes a "lock" to the database. If the next execution detects the lock, it aborts silently. When the script finishes — successfully or not — the lock is released.

A script that implements both patterns can fail, restart, or run out of schedule and will always leave the system in a known, recoverable state.

---

## 🌱 How to Start the Project

1. Review your monorepo: identify the existing telemetry tables and the naming conventions you have already used for paths and fields.
2. Create the job control table in the database (you can add it to the existing schema or create a new migration).
3. Implement the script in `scripts/nightly_export.py` and the status control service in `services/`.
4. Configure the trigger in crontab or your framework's scheduler and document the cron expression in the PR.

---

## 💻 What You Need to Do

### Data model

- [ ] Create a `job_runs` table with at least the following fields: `id`, `job_name`, `status` (`pending` | `processing` | `completed` | `failed`), `started_at`, `finished_at`, `error_message`, `created_at`.
- [ ] Add the migration or SQL statement needed to create the table in the monorepo schema.

### Main script (`scripts/nightly_export.py`)

- [ ] The script exports the previous day's telemetry records to a CSV file in `data/raw/`, with a name that includes the date (e.g. `telemetry_2025-01-15.csv`), **only if that file does not already exist**.
- [ ] The script triggers the data pipeline as a subprocess once the export is complete.
- [ ] The script writes to `job_runs` the result of the execution (final status + timestamp + error if any).
- [ ] The script is executable directly from the command line: `python scripts/nightly_export.py`.

### Idempotency and locking

- [ ] Implement a **Distributed Lock**: if a `job_runs` record already exists with `status = 'processing'` for the `nightly_export` job, the script aborts silently and logs the cancellation.
- [ ] Implement **idempotency**: if a `completed` record already exists for yesterday's date, the script does not re-export the CSV or re-trigger the pipeline. It logs that the execution was skipped as a duplicate.

### Status control (`services/`)

- [ ] Implement a `job_runner` module in `services/` with functions to create, update, and query `job_runs` records.
- [ ] Any unhandled exception must be caught, update the status to `failed` with the error message, release the lock, and propagate the error to the log.
- [ ] No record may remain in `processing` status after a failed execution.

### Trigger

- [ ] Configure the cronjob via the OS `crontab` **or** via your framework's scheduler (e.g. `fastapi-utils`, `APScheduler`).
- [ ] Document the cron expression and implementation decision in the PR body.
- [ ] Add an optional `TARGET_DATE` environment variable to override the target date, so the script can be tested at any time without modifying the code.

### Observability

- [ ] Generate execution logs at `INFO` level for normal events (start, finish, skipped as duplicate) and `ERROR` for exceptions.
- [ ] Each log line includes a timestamp, job name, and resulting status.

---

## ✅ What We Will Evaluate

- [ ] The script is an independent process: it does not import or execute FastAPI code on the application's main thread.
- [ ] The `pending → processing → completed | failed` state machine is implemented and `job_runs` records reflect the actual status of each execution.
- [ ] The Distributed Lock prevents parallel executions: demonstrable by launching two instances of the script simultaneously.
- [ ] The script is idempotent: running it twice on the same day produces the same result as running it once, without duplicating CSV files or pipeline executions.
- [ ] No record remains in `processing` status after a failure: the `try/except/finally` block guarantees the transition to `failed` and the release of the lock.
- [ ] The CSV output exists in `data/raw/` with the correct name and contains the previous day's telemetry data.
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
