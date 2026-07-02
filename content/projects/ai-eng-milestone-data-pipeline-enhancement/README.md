# Milestone 6 — Company's Data Pipeline Enhancement: Subflows and Tests (3/3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Make sure you have completed **[Part 2 of Milestone 6](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/ai-eng-milestone-data-pipeline-build)** — this project builds directly on `data/pipelines/pipeline.py` implemented in the previous session.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

This is **Part 3 of Milestone 6 — Telemetry and Data Pipelines**. The base pipeline already works. Today you bring it to production level: you refactor the main flow into reusable subflows, add unit tests that validate the behaviour of transformation tasks, and complete the Docker deployment with a schedule.

Your CTO has updated the ticket:

> > **Enhancement Ticket — Pipeline to Production**
> >
> > The basic pipeline is ready. Before the final handoff to the operations team, I need three more things:
> >
> > 1. The main flow is growing — refactor it into subflows so that each phase is independent, testable, and reusable.
> > 2. I need unit tests for the transformation tasks. If a test fails, I want to know before the pipeline reaches production, not after.
> > 3. The pipeline must have a working Docker deployment with its schedule. When I run `prefect deployment run`, I want to see the result in Prefect Cloud.
> >
> > Starting point: `data/pipelines/pipeline.py` from the previous session.

### Why subflows

A flow that grows without structure ends up being as hard to maintain as the script it replaced. Subflows apply the DRY principle at the orchestration level: each phase of the pipeline (extraction, transformation, load) becomes an independent flow that can be executed, monitored, and reused separately. The main flow coordinates them but does not contain their logic.

---

## 🌱 How to Start

1. Run `git pull` on your monorepo fork.
2. Open `data/pipelines/pipeline.py` — that is your starting point.
3. Keep the existing folder structure: `data/pipelines/` for flows and subflows, `data/process/` for transformation logic, `data/raw/` for input data, `data/eval/` for validation outputs.
4. Unit tests go in `tests/pipelines/` at the root of the monorepo.

---

## 💻 What You Need to Do

### Phase 1 — Refactoring into subflows

- [ ] Split the main flow into at least three subflows (`@flow`) that correspond to the stages from your design: one for extraction, one for transformation, and one for load. The main flow invokes them in sequence.
- [ ] Each subflow must have explicit inputs and outputs — do not rely on global variables between subflows.
- [ ] If you have optional steps (notifications, secondary exports), extract them as subflows too and invoke them with `allow_failure=True` from the main flow.

### Phase 2 — Unit tests

- [ ] Create the file `tests/pipelines/test_pipeline.py` with unit tests for at least three transformation tasks.
- [ ] Each test must verify the task's behaviour in isolation: it must not depend on a database or external APIs. Use in-memory test data.
- [ ] Include at least one test that verifies the defensive behaviour of a task against invalid or malformed input (for example, a null field where none is expected, or an incorrect type).
- [ ] The tests must pass with `python -m pytest tests/pipelines/test_pipeline.py` without errors.

### Phase 3 — Scheduling and Docker deployment

- [ ] Review the schedule defined in the previous session and confirm it is still the most appropriate for your company's data cycle. If you change it, justify it in a comment.
- [ ] Generate or update the Prefect deployment with Docker as the work pool infrastructure. The deployment must include a name, schedule, work pool, and the required environment variables.
- [ ] Verify the deployment from the CLI: `prefect deployment run <flow-name>/<deployment-name>` must start the flow without errors.
- [ ] Document in a comment or in `data/pipelines/PIPELINE_DESIGN.md` how to pause and resume the schedule: `prefect deployment pause-schedule` / `prefect deployment resume-schedule`.

⚠️ **IMPORTANT:** Subflow names, task names, and test names must follow the same domain vocabulary defined in `data/pipelines/PIPELINE_DESIGN.md`. A subflow named `extract_data` is not acceptable if your company has concrete entities — name it `extract_sales_events` or whatever fits your domain.

---

## ✅ What We Will Evaluate

- [ ] The main flow in `data/pipelines/pipeline.py` invokes at least three subflows (`@flow`) instead of containing all logic directly.
- [ ] Each subflow has explicit inputs and outputs and can be executed independently.
- [ ] The file `tests/pipelines/test_pipeline.py` exists and contains at least three unit tests for transformation tasks.
- [ ] At least one test verifies the defensive behaviour of a task against invalid input.
- [ ] `python -m pytest tests/pipelines/test_pipeline.py` passes without errors.
- [ ] The Prefect deployment has Docker configured as the work pool infrastructure and a defined schedule.
- [ ] `prefect deployment run <flow-name>/<deployment-name>` starts the flow without errors.
- [ ] Subflow names, task names, and test names reflect the domain vocabulary from `data/pipelines/PIPELINE_DESIGN.md`.

---

## 📦 How to Submit

1. Make sure `data/pipelines/pipeline.py` and `tests/pipelines/test_pipeline.py` are committed to your monorepo fork.
2. Commit with the message: `feat: refactor pipeline into subflows and add unit tests`.
3. Open a Pull Request with these changes — it can build on the Part 2 PR or be a new one. Share the URL with your tech lead.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
