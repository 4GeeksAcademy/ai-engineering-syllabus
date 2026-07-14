# Milestone 6 — Implementing a Resilient Business Performance Pipeline (2/3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Keep your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/data-pipelines)** open while you code — it is the source of truth for KPI names, destination table schema, and the endpoint contract you implement. Also have your approved `data/pipelines/PIPELINE_DESIGN.md` from Part 1 ready.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The design document is approved. Now it's time to build it — a pipeline that reads from `telemetry_events` and produces the business-facing KPIs you scoped in Part 1, exactly as named in your `CONTEXT-company.md`. Your existing technical telemetry system (`telemetry_events`, `services/telemetry/analysis.py`, `GET /telemetry/report`) is not part of this work — it stays untouched, still serving engineering.

There is a fundamental difference between a script that works on your machine and a pipeline that can run in production unattended: resilience.

> > **Implementation Ticket — Resilient Business Performance Pipeline**
> >
> > The design is approved. Leadership wants to see this pipeline running, not just documented. Non-negotiable requirements before handoff to production:
> >
> > — The pipeline must tolerate partial failures without interrupting the entire execution.
> > — Tasks that touch external services must have retries configured.
> > — The pipeline must be runnable as a script from the command line.
> > — If a task has already run successfully in the last hour, it must not repeat unnecessarily.
> >
> > Starting point: your `data/pipelines/PIPELINE_DESIGN.md` from the previous day. Implement what you designed — reading from telemetry, writing to the new business reporting table you scoped, nothing about the existing technical report changes.

### What makes a pipeline resilient?

A resilient pipeline is not one that never fails — it is one that fails well. In Prefect, that means three concrete things:

- **Partial failure tolerance**: a failing task does not bring down the entire flow. Prefect distinguishes between critical tasks (whose failure should stop everything) and optional tasks (whose failure should be logged and allow the flow to continue).
- **Smart retries**: tasks that interact with external services (databases, APIs) are configured with `retries` and `retry_delay_seconds` to absorb transient failures without human intervention.
- **Result caching**: if a task already produced a valid result recently, Prefect can reuse it rather than repeating the computation. This is especially useful for expensive transformations.

---

## 🌱 How to Start

1. Run `git pull` on your monorepo fork to make sure you have the latest state.
2. Open your `data/pipelines/PIPELINE_DESIGN.md` — that document is your specification. Implement what you designed.
3. Keep your `CONTEXT-company.md` from the data pipelines context open while you code: it's the source of truth for the exact KPI names (its "KPIs to Measure" section), the destination table schema, and the endpoint contract you're implementing. (The event fields you're extracting from are the ones your telemetry `CONTEXT-company.md` already defined as mandatory.)
4. Write your pipeline code in `data/pipelines/`. The main entry point must be named `data/pipelines/pipeline.py`. Use `data/raw/` for input data and intermediate files, `data/process/` for reusable transformation scripts, and `data/eval/` for pipeline validation outputs.
5. The extraction task reads from `telemetry_events` (and any other domain tables you need) — read-only. The load task writes to the **new** `reporting.business_metrics` table you designed in Part 1. Do not write back into `telemetry_events` and do not modify `services/telemetry/analysis.py`.
6. Any endpoint that exposes or triggers the pipeline (for example, to query the status of the last run or launch a run manually) must be implemented in `services/reporting/`, a module separate from `services/telemetry/`, importing functions and flows from `data/pipelines/` as needed.
7. Install Prefect 3 in your environment: `uv add "prefect>=3"`.

---

## 💻 What You Need to Do

### Phase 1 — Flows and tasks

- [ ] Implement the pipeline as one or more Prefect **flows** (`@flow`) following the stage structure from your design: extraction, transformation, and load as a minimum.
- [ ] Each stage must be an independent **task** (`@task`) with explicit inputs and outputs.
- [ ] If your pipeline has optional steps (for example, notifications or secondary exports), invoke them with `return_state=True` so that a failure in them does not interrupt the main execution.

### Phase 2 — Resilience

- [ ] Add `retries` and `retry_delay_seconds` to every task that interacts with external services (database, APIs). Justify the number of retries chosen in a comment.
- [ ] Handle at least one task failure explicitly in the flow using `return_state=True` rather than letting it propagate automatically.
- [ ] Add caching (`cache_key_fn`, `cache_expiration`) to at least one expensive transformation task. Explain in a comment what defines the cache key and how long it is valid.

### Phase 3 — Idempotency

- [ ] The load phase must be idempotent: if the pipeline runs twice over the same data range, the result in your `reporting.business_metrics` table must be identical after both runs. Implement the strategy you documented in your design (upsert, control table, timestamp, or another) — the unique constraint from your `CONTEXT-company.md` schema is what your upsert should key off.
- [ ] Record in the database or in a log file the minimum execution metadata for each run: start time, end time, records processed, final status, and any captured errors.

### Phase 4 — Script-based execution

- [ ] Ensure `data/pipelines/pipeline.py` can be executed directly as a CLI script (for example, with an `if __name__ == "__main__"` block that invokes the main flow).
- [ ] Verify the full pipeline runs without errors: `python data/pipelines/pipeline.py`.
- [ ] Document the intended schedule for your company's reporting cycle in `data/pipelines/PIPELINE_DESIGN.md` and the run command in a comment or the same design doc.

### Phase 5 — Backend endpoints

- [ ] In `services/reporting/`, implement at least two endpoints related to this pipeline: one to query the status and metadata of the last run, and one to trigger a manual flow run. Keep them in their own module, separate from `services/telemetry/`.
- [ ] The endpoints must import flows or functions from `data/pipelines/` — do not duplicate pipeline logic in `services/`.
- [ ] The endpoints follow the same authentication conventions and response structure as the rest of your API, and the KPI query endpoint's response shape matches the contract in your `CONTEXT-company.md`.

⚠️ **IMPORTANT:** Flow names, task names, table names, and field names must match what is defined in `data/pipelines/PIPELINE_DESIGN.md` and your `CONTEXT-company.md` from the data pipelines context (KPIs and schema) — consistent, in turn, with the event fields already defined in your telemetry `CONTEXT-company.md`. A generic implementation that ignores your company's data model will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The file `data/pipelines/pipeline.py` exists and defines at least one flow with three or more tasks.
- [ ] At least one task has `retries` configured with a value greater than zero and a comment justifying the number chosen.
- [ ] At least one optional task is invoked with `return_state=True` and the flow continues executing when that task fails.
- [ ] At least one transformation task has caching configured with `cache_key_fn` and `cache_expiration`.
- [ ] The load phase is idempotent: running the pipeline twice over the same data does not produce duplicates in the `reporting.business_metrics` table.
- [ ] Each pipeline run records at least five metadata fields (start time, end time, records processed, status, errors) in the database or in a structured log file.
- [ ] `python data/pipelines/pipeline.py` runs the full ETL flow without errors.
- [ ] The run command is documented in `data/pipelines/PIPELINE_DESIGN.md` or inline comments.
- [ ] The pipeline writes to the new `reporting.business_metrics` table from your `CONTEXT-company.md` — `telemetry_events` and `services/telemetry/analysis.py` are untouched.
- [ ] At least one endpoint exists in `services/reporting/` that returns the metadata of the last pipeline run (status, start time, end time, records processed).
- [ ] At least one endpoint exists in `services/reporting/` that triggers a manual flow run, importing the function from `data/pipelines/` without duplicating the logic.
- [ ] The KPI values produced match the definitions in your `CONTEXT-company.md`'s "KPIs to Measure" section — not a reinterpretation of them.
- [ ] The implemented design is consistent with `data/pipelines/PIPELINE_DESIGN.md` — the stages, entities, and resilience strategies described there are reflected in the code.

---

## 📦 How to Submit

1. Make sure `data/pipelines/pipeline.py`, the endpoints in `services/reporting/`, and any supporting files are committed to your monorepo fork.
2. Commit with the message: `feat: implement resilient business performance pipeline`.
3. Push your changes to your GitHub repository and share the URL with your tech lead.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
