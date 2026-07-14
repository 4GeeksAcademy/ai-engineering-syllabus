# Milestone 6 — Business Performance Pipeline Enhancement: Subflows and Tests (3/3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Make sure you have completed **Part 2 of Milestone 6** — this project builds directly on `data/pipelines/pipeline.py` implemented in the previous session. Keep your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/data-pipelines)** open — KPI names, schema, and stakeholder audience come from there.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

This is **Part 3 of Milestone 6 — Telemetry and Data Pipelines**. Your business performance pipeline already works: it reads from `telemetry_events` and produces the KPIs leadership asked for — the ones named in your `CONTEXT-company.md` — without touching the existing technical telemetry system. Today you bring it to production level: you refactor the main flow into reusable subflows, add unit tests that validate the behaviour of transformation tasks, ensure the pipeline runs directly from the command line, and — this is the part leadership actually cares about — put those KPIs in front of a dashboard someone can read.

> > **Enhancement Ticket — Pipeline to Production**
> >
> > The basic pipeline is ready. Before the final handoff to the operations team, I need four more things:
> >
> > 1. The main flow is growing — refactor it into subflows so that each phase is independent, testable, and reusable.
> > 2. I need unit tests for the transformation tasks. If a test fails, I want to know before the pipeline reaches production, not after.
> > 3. The pipeline must be runnable as a script. When I execute `python data/pipelines/pipeline.py`, the full ETL flow must complete without errors.
> > 4. I need a dashboard. Nobody on the leadership team is going to query an endpoint — put the KPIs somewhere they can actually look at them.
> >
> > Starting point: `data/pipelines/pipeline.py` from the previous session.

### Why subflows

A flow that grows without structure ends up being as hard to maintain as the script it replaced. Subflows apply the DRY principle at the orchestration level: each phase of the pipeline (extraction, transformation, load) becomes an independent flow that can be executed, monitored, and reused separately. The main flow coordinates them but does not contain their logic.

---

## 🌱 How to Start

1. Run `git pull` on your monorepo fork.
2. Open `data/pipelines/pipeline.py` — that is your starting point.
3. Keep your `CONTEXT-company.md` at hand: subflow, task, and test names should reflect the KPI names from its "KPIs to Measure" section and the schema you implemented — not generic labels.
4. Keep the existing folder structure: `data/pipelines/` for flows and subflows, `data/process/` for transformation logic, `data/raw/` for input data, `data/eval/` for validation outputs.
5. Unit tests go in `tests/pipelines/` at the root of the monorepo.
6. The dashboard page goes in `uis/backoffice/`, fetching from the `services/reporting/` endpoint you already built in Part 2.
7. Ensure Prefect 3 is installed from Part 2: `uv add "prefect>=3"`.

---

## 💻 What You Need to Do

### Phase 1 — Refactoring into subflows

- [ ] Split the main flow into at least three subflows (`@flow`) that correspond to the stages from your design: one for extraction (from `telemetry_events` and any other domain tables), one for transformation, and one for load (into your `reporting.business_metrics` table). The main flow invokes them in sequence.
- [ ] Each subflow must have explicit inputs and outputs — do not rely on global variables between subflows.
- [ ] If you have optional steps (notifications, secondary exports), extract them as subflows too and invoke them with `return_state=True` from the main flow.

### Phase 2 — Unit tests

- [ ] Create the file `tests/pipelines/test_pipeline.py` with unit tests for at least three transformation tasks — the ones that compute the KPIs from your `CONTEXT-company.md`.
- [ ] Each test must verify the task's behaviour in isolation: it must not depend on a database or external APIs. Use in-memory test data shaped like your telemetry events (per your `CONTEXT-company.md`).
- [ ] Include at least one test that verifies the defensive behaviour of a task against invalid or malformed input (for example, a null field where none is expected, or an incorrect type).
- [ ] Include at least one test that asserts a computed KPI value matches the definition in your `CONTEXT-company.md` for a known, hand-calculated input.
- [ ] The tests must pass with `python -m pytest tests/pipelines/test_pipeline.py` without errors.

### Phase 3 — Script-based execution

- [ ] Ensure `data/pipelines/pipeline.py` can be executed directly as a CLI script (for example, with an `if __name__ == "__main__"` block that invokes the main flow).
- [ ] Verify the full pipeline runs without errors: `python data/pipelines/pipeline.py`.
- [ ] Document the run command in a comment or in `data/pipelines/PIPELINE_DESIGN.md`.

### Phase 4 — Business dashboard (mandatory)

Your pipeline produces KPIs — but a table nobody looks at isn't a deliverable. This phase is not optional: leadership needs to actually _see_ the numbers, not query an endpoint with curl.

- [ ] Build a page in `uis/backoffice/` (e.g. `/reporting`) that fetches your `services/reporting/` endpoint and renders every KPI from your `CONTEXT-company.md`'s "KPIs to Measure" section — a chart or a table per KPI is enough.
- [ ] Label each KPI clearly with the same name it has in your `CONTEXT-company.md`, and show the period (week or month, per your cadence) the data covers.
- [ ] This dashboard is business-facing, not a developer tool: it should be legible to the stakeholder named in your `CONTEXT-company.md` (e.g. the CEO or department head) without needing anything translated or explained.
- [ ] No need for visual polish — a working, correctly labeled view of real data from `reporting.business_metrics` is the goal.

⚠️ **IMPORTANT:** Subflow names, task names, and test names must follow the same domain vocabulary defined in `data/pipelines/PIPELINE_DESIGN.md` and your `CONTEXT-company.md`. A subflow named `extract_data` is not acceptable if your company has concrete entities and KPI names — name it after the actual business metric this pipeline produces.

### 🔵 Additional Activity — Extra Enhancements from Your Design Questions

- [ ] Go back to the "Questions to Help You Design the Pipeline" section from Part 1. If, while answering those questions, you identified resilience or observability enhancements beyond what Phases 1–3 already cover (for example, a heartbeat plus silence alert, a concurrency lock for overlapping runs, or an `Idempotency-Key` pattern for retries) and haven't implemented them yet, this is the place to do it.
- [ ] For each enhancement you add, note in `data/pipelines/PIPELINE_DESIGN.md` which question it answers and why you prioritized it.
- [ ] This is optional — only pick it up if your own design doc actually flagged something worth building. Don't invent an enhancement just to check a box.

---

## ✅ What We Will Evaluate

- [ ] The main flow in `data/pipelines/pipeline.py` invokes at least three subflows (`@flow`) instead of containing all logic directly.
- [ ] Each subflow has explicit inputs and outputs and can be executed independently.
- [ ] The file `tests/pipelines/test_pipeline.py` exists and contains at least three unit tests for transformation tasks.
- [ ] At least one test verifies the defensive behaviour of a task against invalid input.
- [ ] At least one test validates a KPI's computed value against its definition in `CONTEXT-company.md`.
- [ ] `python -m pytest tests/pipelines/test_pipeline.py` passes without errors.
- [ ] `python data/pipelines/pipeline.py` runs the full ETL flow without errors.
- [ ] The run command is documented in `data/pipelines/PIPELINE_DESIGN.md` or inline comments.
- [ ] Subflow names, task names, and test names reflect the domain vocabulary and KPI names from `CONTEXT-company.md`.
- [ ] `telemetry_events` and `services/telemetry/analysis.py` remain unmodified throughout the refactor.
- [ ] A dashboard exists in `uis/backoffice/` that displays every KPI from `CONTEXT-company.md`'s "KPIs to Measure" section, correctly labeled, sourced from your `services/reporting/` endpoint.
- [ ] The dashboard is legible to a non-technical business stakeholder, not just to another engineer.

---

## 📦 How to Submit

1. Make sure `data/pipelines/pipeline.py`, `tests/pipelines/test_pipeline.py`, and the dashboard page in `uis/backoffice/` are committed to your monorepo fork.
2. Commit with the message: `feat: refactor business performance pipeline into subflows, add unit tests, and add reporting dashboard`.
3. Open a Pull Request with these changes — it can build on the Part 2 PR or be a new one. In the PR description, mention whether you implemented any additional enhancement from the design questions, and which one. Share the URL with your tech lead.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
