# Milestone 6 — Designing a Business Performance Data Pipeline (1/3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/data-pipelines)** before writing a single line — it defines the business deliverable, audience, cadence, KPIs to measure, and mandatory metrics this pipeline must produce.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Over the past weeks you captured telemetry events, stored them in `telemetry_events`, and built a technical report — event volume, error rates, latency — for your own engineering team. **That system stays exactly as it is.** You are not touching `telemetry_events`, `services/telemetry/analysis.py`, or the `GET /telemetry/report` endpoint in this milestone.

Today your tech lead is asking for something different: a **new** data pipeline, designed from scratch, whose only job is to turn that same telemetry into data that describes how the business is performing — the kind of numbers a department head or the CEO would read, not the kind an engineer uses to debug a service.

> > **Technical Brief — Business Performance Data Pipeline (Design Phase)**
> >
> > Before writing a single line of orchestration code, I need you to document the design of a new data pipeline. This one isn't for us — it's for the business side: the leadership team that's been asking for a real report instead of a PDF someone assembles by hand every week.
> >
> > This is a **new** pipeline, built on top of the telemetry you already have. Your existing `telemetry_events` table, your technical report, and the `GET /telemetry/report` endpoint don't change — they keep serving engineering exactly as before. What you're building now reads from the same source but produces a different kind of output: numbers a non-technical stakeholder can act on.
> >
> > Deliverable: a design document in Markdown, committed to the monorepo. No orchestration code yet — design first, implementation next.

### What makes a data pipeline robust?

A data pipeline is not simply a script that moves data from one place to another. A production pipeline has well-defined stages, handles failures predictably, and can be audited. The three key attributes that separate a robust pipeline from one that "just works" are:

- **Idempotency**: running the pipeline twice on the same data produces the same result — no duplicates, no corruption.
- **Observability**: every run leaves enough traces to know what happened, when, and why.
- **Recoverability**: when the pipeline fails mid-way, the next run knows exactly where to resume.

These three attributes are what your design document must demonstrate you have thought through deeply.

### Build this pipeline around a real business need

A data pipeline is not infrastructure for its own sake — even less so this one. Its only reason to exist is a business question that your `CONTEXT-company.md` already scopes for you, but that nobody is answering reliably today.

Before you design extraction, transformation, or load stages, read your `CONTEXT-company.md` from the data pipelines context — it names the one concrete business deliverable your company needs, who it's for, at what cadence, the exact KPIs it must compute (see its "KPIs to Measure" section), and which mandatory metrics feed them. (This is the follow-through on what your telemetry `CONTEXT-company.md` flagged back in section 4, "How These Metrics Connect to the Future" — this is that moment, now spelled out concretely.)

Design the pipeline to produce exactly the data that deliverable needs — at the right freshness, granularity, and audit trail. Don't invent a generic KPI; the one your company needs is already scoped for you in `CONTEXT-company.md`.

**This is a new pipeline, not a replacement.** The technical telemetry report you built earlier keeps answering technical questions for engineers (volume, errors, latency). This pipeline answers a different question, for a different audience, and its output lives in different tables and different endpoints. Nothing from the earlier project changes.

When you write the pipeline purpose in Phase 2, name the business deliverable you're targeting and the mandatory metric(s) that feed it. If a stage in your design doesn't support that deliverable, question whether it belongs in v1.

---

## 🌱 How to Start

1. Run `git pull` on your monorepo fork to make sure you have the latest state.
2. Explore the [`data/`](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/tree/main/data) folder in the monorepo — it contains the subfolders `raw/`, `process/`, `pipelines/`, and `eval/` that you will use throughout this module. Orchestration code will live in `data/pipelines/`; reusable transformation scripts in `data/process/`; HTTP endpoints that query or trigger the pipeline will live in `services/` and import from `data/pipelines/` — not the other way around.
3. Create the file `data/pipelines/PIPELINE_DESIGN.md` — that is where your design document goes.
4. Read your `CONTEXT-company.md` from the data pipelines context — its "KPIs to Measure" section names the exact numbers this pipeline must produce, and it also states the audience, cadence, required aggregation, and destination table. (The mandatory metrics feeding those KPIs are the ones from your telemetry `CONTEXT-company.md`, already familiar from the earlier milestone.)
5. This pipeline's output does **not** belong in `telemetry_events`. All new destination tables live under a dedicated `reporting` schema, named `reporting.business_metrics` — and are exposed through a new `services/reporting/` module, kept separate from `services/telemetry/` and the `GET /telemetry/report` endpoint.

> **Note on tooling:** Today you are introduced to **Prefect** as an orchestration framework — flows, tasks, states, and configuration blocks. Your design document should reflect how you would organize your pipeline using these concepts, even though the code implementation comes over the next days.

---

## 💻 What You Need to Do

### Phase 1 — Current state analysis

- [ ] Document in a "Current State" section what you already have: the telemetry events captured so far, where they're stored, and what your existing technical report already answers for engineering.
- [ ] Identify the gap: which business question from your `CONTEXT-company.md` is still unanswered by that technical report, and would require a dedicated pipeline?

### Phase 2 — Pipeline design

- [ ] Define the **purpose** of the pipeline in a single concrete sentence: name the specific business deliverable you're targeting (e.g., "produce the daily rollup that feeds [role]'s weekly executive report"), the KPI(s) it computes (from your `CONTEXT-company.md`'s "KPIs to Measure" section), and the mandatory metric(s) from your telemetry CONTEXT it's built on.
- [ ] Specify the **extraction format**: your source is `telemetry_events` (plus any other existing domain tables you need) — in what format the data arrives, and how often it's updated.
- [ ] Design the **data flow** with a text or Mermaid diagram showing at least three clearly separated stages: extraction, transformation, and load.
- [ ] Describe how you would handle a source that **updates existing records** rather than always inserting new ones — explain the concrete strategy to avoid duplicates in your specific case.
- [ ] Name the **new destination table(s)** under the `reporting` schema (`reporting.business_metrics`) where this pipeline's output will live, and the **new endpoint(s) in `services/reporting/`** that will expose it — explicitly separate from `telemetry_events` and `GET /telemetry/report`.

### Phase 3 — Resilience and idempotency

- [ ] Define your **idempotency strategy**: if the pipeline fails during the load phase and is re-run, explain exactly how you guarantee that already-loaded data is neither corrupted nor duplicated.
- [ ] Design your **execution log**: specify the minimum fields you would record in every run (start time, end time, records processed, status, errors) and explain why each field is necessary to audit the pipeline in production.

### Phase 4 — Mapping to Prefect

- [ ] Map your design to Prefect concepts: identify which parts would be **flows**, which would be **tasks**, and which **states** (Running, Completed, Failed) are relevant for your pipeline.
- [ ] Indicate which configuration or credentials you would manage as **Prefect blocks** (for example, the connection to Supabase).

### Phase 5 — Application integration (design only)

- [ ] Sketch the **new endpoint(s) in `services/reporting/`** the business side will use to query the resulting metric(s) and/or trigger a run — kept separate from `services/telemetry/` and the `GET /telemetry/report` endpoint.
- [ ] For each endpoint, state which **function or flow in `data/pipelines/`** it will call — no ETL logic belongs in `services/`.

⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your design must match your company's domain vocabulary in the monorepo. A generic design that ignores your company's data model will not be accepted.

---

## ❓ Questions to Help You Design the Pipeline

Before writing `PIPELINE_DESIGN.md`, answer in writing — even as a draft — how you would handle each case in **your** monorepo.

### Idempotency

1. **Duplicates at the source** — How do you prevent counting the same action twice in `telemetry_events` and your business aggregates? Which envelope field is your dedup key, and at which layer?

   <details>
   <summary>See example and hint</summary>

   An operator confirms `outbound_order_created` twice within 300 ms; two rows arrive with the same `eventId` but different receive timestamps.

   **Hint:** upsert on `eventId` at ingest.

   </details>

2. **Re-run after failure** — If the pipeline dies during load with partial data inserted, what happens when you re-run it? How do you guarantee the same outcome as a clean run?

   <details>
   <summary>See example and hint</summary>

   The 02:00 run loaded 847 of 1,412 rows into your new reporting table and failed on a Supabase timeout.

   **Hint:** upsert by daily partition key.

   </details>

3. **Late events** — How do you recompute a published daily business metric when a delayed event arrives, without inflating numbers or losing audit trail?

   <details>
   <summary>See example and hint</summary>

   At 23:50 a `stock_waste_registered` event is stored with a noon `timestamp`; that day's aggregate is already on the report.

   **Hint:** recompute window; log invalidating run.

   </details>

### Observability

4. **Silence vs. true absence** — How do you tell zero activity from failed capture or a pipeline that never ran? What minimum signals would you record?

   <details>
   <summary>See example and hint</summary>

   Between 14:00 and 15:00 there are no relevant events recorded, but the business kept operating normally.

   **Hint:** heartbeat plus silence alert.

   </details>

5. **Collection traceability** — What traces reconstruct the path event → business report and detect gaps, bursts, or interval drift?

   <details>
   <summary>See example and hint</summary>

   Your metric spikes at 09:00 and flatlines at 09:15 — real activity or a batch that processed two windows at once?

   **Hint:** correlate `requestId` and `run_id`.

   </details>

6. **Growth vs. data loss** — If event volume swings day to day, how do you know the business is growing vs. losing or duplicating measurements?

   <details>
   <summary>See example and hint</summary>

   Mondays: 12,000 events; Sundays: 800 — normal activity pattern or intermittent `POST /telemetry` failures?

   **Hint:** compare events to active sessions or locations reporting in.

   </details>

### Recoverability

7. **Database outage** — Where do you resume if the connection drops mid-pipeline? What checkpoint do you persist?

   <details>
   <summary>See example and hint</summary>

   Pandas finished grouping by entity, but Supabase dropped on `INSERT` into the reporting table.

   **Hint:** phase checkpoint in `pipeline_runs`.

   </details>

8. **Frontend buffer** — Does buffering offline events in the browser make sense? What risks does it introduce, and which layer should own them?

   <details>
   <summary>See example and hint</summary>

   An operator loses WiFi for 20 minutes; the browser stores 45 events in `localStorage` and sends them in one batch on reconnect.

   **Hint:** client buffer; server-side dedup.

   </details>

9. **Transmission retry** — How do you design retries on `POST /telemetry` without breaking idempotency? What server response means "already stored" vs. "retry"?

   <details>
   <summary>See example and hint</summary>

   The client gets a timeout, retries, but the server already persisted the event on the slow first request.

   **Hint:** `Idempotency-Key`; return 200 if exists.

   </details>

### Cross-cutting

10. **Concurrent runs** — What do you observe, how do you avoid load race conditions, and how do you recover when cron and a manual trigger from `services/` overlap?

    <details>
    <summary>See example and hint</summary>

    The scheduled flow starts at 02:00; at 02:05 someone clicks "Run pipeline now" in the backoffice.

    **Hint:** window lock; unique `run_id`.

    </details>

---

## ✅ What We Will Evaluate

- [ ] The file `data/pipelines/PIPELINE_DESIGN.md` exists in the monorepo and is written in readable Markdown.
- [ ] The pipeline purpose is defined in a single concrete sentence that names the business deliverable and KPI(s) from the company's `CONTEXT-company.md` — not a generic or technical KPI.
- [ ] The design does not modify `telemetry_events`, `services/telemetry/analysis.py`, or `GET /telemetry/report` — the new pipeline's output lives in new tables under a `reporting` schema and is exposed through a new `services/reporting/` module.
- [ ] The data flow diagram shows at least three distinct stages (extraction, transformation, load) with the real entity or table names from the company.
- [ ] The strategy for handling updates to existing records is documented with a concrete mechanism (e.g., upsert by primary key, last-modified timestamp, control table).
- [ ] The idempotency strategy is explicit: it describes what happens on the second run after a load-phase failure, not just what would be desirable.
- [ ] The execution log specifies at least five fields with the field name, data type, and justification for why that field is necessary for auditing.
- [ ] The Prefect mapping identifies at least two flows and three tasks with concrete names aligned with the pipeline stages.
- [ ] The design documents at least two planned `services/reporting/` endpoints (status query and manual trigger) and names the `data/pipelines/` functions each will import.
- [ ] The design is consistent with the telemetry events and mandatory metrics already defined in the company's CONTEXT file.

---

## 📦 How to Submit

1. Make sure `data/pipelines/PIPELINE_DESIGN.md` is committed to your monorepo fork.
2. Commit with the message: `feat: add business performance pipeline design document`.
3. Push your changes to your GitHub repository and share the URL with your tech lead.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
