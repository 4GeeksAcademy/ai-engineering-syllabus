# Designing a Data Pipeline: From Raw Data to Reliable Insights

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

**Veridian Logistics** is a mid-size freight company that routes cargo across five regional hubs. Their operations team has been exporting daily activity reports as CSV files from their fleet management system — dispatches, delivery completions, route changes, and vehicle status updates all land in the same flat export every night.

The problem: the file includes both new records and updates to existing ones. When a package status changes (say, from _in transit_ to _delivered_), the system generates a new row instead of modifying the original. Over time, the exported files have started showing the same shipment multiple times at different lifecycle stages — which means any pipeline that blindly loads these records into a database ends up with duplicates and incorrect aggregations.

The CTO has asked you to design a data pipeline that handles this data correctly before it ever reaches a reporting table. She's not asking for a working implementation yet — she needs a **design document** that her team can review, critique, and hand off to an engineer. You've been brought in as the data engineer responsible for the architecture.

> Your technical lead has shared the following brief:
>
> #### Pipeline Design Document — Veridian Logistics
>
> Produce a `PIPELINE_DESIGN.md` file documenting the architecture of the ETL pipeline. The document must address:
>
> - **Purpose**: What business problem does this pipeline solve? What are the outputs?
> - **Data format analysis**: The current export is CSV. Is that the right format for this use case? Would a different format perform better at scale?
> - **Data flow diagram**: A visual diagram of each stage from source to destination — extraction, transformation, load, and any intermediate steps.
> - **Deduplication strategy**: The source updates records by adding new rows. How will the pipeline detect and handle these without loading duplicates?
> - **Idempotency plan**: If the pipeline fails mid-load, how does the next run avoid corrupting or double-loading already-processed data?
> - **Execution log specification**: What minimum fields must every pipeline run log so the system can be audited in production?
> - **Robustness criteria**: What separates a pipeline that simply works from one that is production-ready? List at least three concrete characteristics.

This is a design-first exercise. No code will be written. The deliverable is a planning document rigorous enough that another engineer could implement it from scratch.

Think carefully about each decision — format choices, storage choices, and failure handling strategies all have trade-offs. Your document should show that you understand _why_ each choice was made, not just what the choice is.

---

## 🌱 How to Start the Project

This project does not require a starter repository — the deliverable is a design document only.

1. Create a new GitHub repository for this project (for example, `veridian-pipeline-design`).
2. Clone it locally or open it in a GitHub Codespace.
3. Create the file `PIPELINE_DESIGN.md` at the root of the repository and start your design there.

You can use [this Mermaid editor](https://waficmikati.github.io/mermaid/) to build and embed your data flow diagram.

---

## 💻 What You Need to Do

### Phase 1 — Understand the scenario

- [ ] Read the brief carefully and identify the key constraints: mixed inserts/updates, nightly CSV export, multi-hub operation.
- [ ] List the questions you would ask the client before designing anything (at least three).

### Phase 2 — Design the pipeline architecture

- [ ] Create `PIPELINE_DESIGN.md` at the root of the project.
- [ ] Write a **Purpose** section explaining what problem the pipeline solves and what its outputs are.
- [ ] Write a **Data Format Analysis** section. Evaluate the current CSV format: when does it work well, when does it fall short? Would you recommend an alternative (e.g. JSON, Parquet) for any stage of the pipeline? Justify your answer.
- [ ] Create a **Data Flow Diagram** showing every stage: source → extract → transform → load → destination. Label each stage and annotate any key decisions (e.g. "deduplication happens here").
- [ ] Write a **Deduplication Strategy** section. Explain how your pipeline identifies and resolves duplicate records from a source that updates by inserting new rows.
- [ ] Write an **Idempotency Plan** section. Describe what happens if the pipeline fails halfway through the load phase and how the next execution recovers without corrupting data.
- [ ] Write an **Execution Log Specification** section. Define the minimum fields every pipeline run must log (e.g. run ID, start time, rows extracted, rows loaded, status, errors).
- [ ] Write a **Robustness Criteria** section. Name at least three concrete characteristics that distinguish a production-ready pipeline from one that "just works."

### Phase 3 — Review and commit

- [ ] Re-read the document as if you were another engineer who has never seen the scenario. Are all decisions explained?
- [ ] Commit `PIPELINE_DESIGN.md` with the message: `feat: add pipeline design document`.

⚠️ **IMPORTANT:** This project requires **no code implementation**. Do not include Python scripts, database migrations, or working ETL code. The deliverable is exclusively the `PIPELINE_DESIGN.md` design document.

---

## ✅ What We Will Evaluate

- [ ] `PIPELINE_DESIGN.md` is present, committed, and complete.
- [ ] Purpose section clearly states the business problem and expected outputs.
- [ ] Data format analysis includes a justified recommendation — not just a description of the formats.
- [ ] Data flow diagram covers all pipeline stages and is legible.
- [ ] Deduplication strategy addresses the specific constraint (updates-as-inserts) rather than the generic case.
- [ ] Idempotency plan explains a concrete recovery mechanism (e.g. staging tables, upsert logic, checkpointing).
- [ ] Execution log specification lists at least five concrete fields with a rationale for each.
- [ ] Robustness criteria are specific and actionable — not generic qualities like "good code."
- [ ] Decisions throughout the document include trade-off reasoning, not just conclusions.

> Note: The quality of the diagram and the technical depth of each section matter more than document length. A short, precise document with clear reasoning outscores a long one with vague answers.

---

## 📦 How to Submit

Push your repository to GitHub and share the link according to your instructor's instructions. Make sure `PIPELINE_DESIGN.md` is committed on the main branch before submitting.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
