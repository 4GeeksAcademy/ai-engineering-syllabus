# Milestone 6 — Company's Data Pipeline Design (1/3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Over the past weeks you captured telemetry events, stored them in a database, and generated basic reports with Pandas. Your tech lead now wants something more: a data pipeline that is robust, auditable, and that your team can run confidently in production.

Your CTO has sent you this brief through the team's task manager:

> > **Technical Brief — Data Pipeline (Design Phase)**
> >
> > Before writing a single line of orchestration code, I need you to document the design of our data pipeline. The data team has received an internal RFP from the operations area: they want to know exactly how data flows from the moment it is captured in the application to the moment it reaches the dashboards. They also want guarantees around idempotency and auditability before they sign off on moving this to production.
> >
> > Deliverable: a design document in Markdown, committed to the monorepo. No orchestration code yet — design first, implementation next.

### What makes a data pipeline robust?

A data pipeline is not simply a script that moves data from one place to another. A production pipeline has well-defined stages, handles failures predictably, and can be audited. The three key attributes that separate a robust pipeline from one that "just works" are:

- **Idempotency**: running the pipeline twice on the same data produces the same result — no duplicates, no corruption.
- **Observability**: every run leaves enough traces to know what happened, when, and why.
- **Recoverability**: when the pipeline fails mid-way, the next run knows exactly where to resume.

These three attributes are what your design document must demonstrate you have thought through deeply.

---

## 🌱 How to Start

1. Run `git pull` on your monorepo fork to make sure you have the latest state.
2. Explore the [`data/`](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/tree/main/data) folder in the monorepo — it contains the subfolders `raw/`, `process/`, `pipelines/`, and `eval/` that you will use throughout this module.
3. Create the file `data/pipelines/PIPELINE_DESIGN.md` — that is where your design document goes.
4. Review the telemetry events, KPIs, and domain entities already in your monorepo to identify what data your pipeline must process.

> **Note on tooling:** Today you are introduced to **Prefect** as an orchestration framework — flows, tasks, states, and configuration blocks. Your design document should reflect how you would organize your pipeline using these concepts, even though the code implementation comes over the next days.

---

## 💻 What You Need to Do

### Phase 1 — Current state analysis

- [ ] Document in a "Current State" section the data you already have: which telemetry events you have captured, where they are stored, and which reports you already generate with Pandas.
- [ ] Identify the limitations of your current implementation: what happens if the script fails mid-run? Can you tell whether data has already been processed?

### Phase 2 — Pipeline design

- [ ] Define the **purpose** of the pipeline in a single concrete sentence: what problem it solves and what value it delivers to your company.
- [ ] Specify the **extraction format**: where data comes from (table, endpoint, file), in what format it arrives, and how often it is updated.
- [ ] Design the **data flow** with a text or Mermaid diagram showing at least three clearly separated stages: extraction, transformation, and load.
- [ ] Describe how you would handle a source that **updates existing records** rather than always inserting new ones — explain the concrete strategy to avoid duplicates in your specific case.

### Phase 3 — Resilience and idempotency

- [ ] Define your **idempotency strategy**: if the pipeline fails during the load phase and is re-run, explain exactly how you guarantee that already-loaded data is neither corrupted nor duplicated.
- [ ] Design your **execution log**: specify the minimum fields you would record in every run (start time, end time, records processed, status, errors) and explain why each field is necessary to audit the pipeline in production.

### Phase 4 — Mapping to Prefect

- [ ] Map your design to Prefect concepts: identify which parts would be **flows**, which would be **tasks**, and which **states** (Running, Completed, Failed) are relevant for your pipeline.
- [ ] Indicate which configuration or credentials you would manage as **Prefect blocks** (for example, the connection to Supabase).

⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your design must match your company's domain vocabulary in the monorepo. A generic design that ignores your company's data model will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The file `data/pipelines/PIPELINE_DESIGN.md` exists in the monorepo and is written in readable Markdown.
- [ ] The pipeline purpose is defined in a single concrete sentence that mentions the company's business, not only the technology.
- [ ] The data flow diagram shows at least three distinct stages (extraction, transformation, load) with the real entity or table names from the company.
- [ ] The strategy for handling updates to existing records is documented with a concrete mechanism (e.g., upsert by primary key, last-modified timestamp, control table).
- [ ] The idempotency strategy is explicit: it describes what happens on the second run after a load-phase failure, not just what would be desirable.
- [ ] The execution log specifies at least five fields with the field name, data type, and justification for why that field is necessary for auditing.
- [ ] The Prefect mapping identifies at least two flows and three tasks with concrete names aligned with the pipeline stages.
- [ ] The design is consistent with the telemetry events and KPIs already captured in your monorepo.

---

## 📦 How to Submit

1. Make sure `data/pipelines/PIPELINE_DESIGN.md` is committed to your monorepo fork.
2. Commit with the message: `feat: add pipeline design document`.
3. Push your changes to your GitHub repository and share the URL with your tech lead.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
