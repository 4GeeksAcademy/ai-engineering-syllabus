# CONTEXT — Nexova: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

At Nexova, RFPs go straight to **Marcos Ibáñez's** team, the **Sales Director**: prospective clients (tech, retail, or finance companies) asking for a proposal to outsource selection, customer support, or corporate training. The current sales cycle runs 3 to 8 weeks, and a good chunk of that time goes into back-and-forth emails with Selection, Training, or Support to nail down scope and price.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers:

| `department_id` | Department                     | Owner          | What it contributes to the proposal                             |
| --------------- | ------------------------------ | -------------- | --------------------------------------------------------------- |
| `seleccion`     | Talent Selection Operations    | Javier Almeida | Roles to fill, estimated time-to-close, consulting hours needed |
| `capacitacion`  | Corporate Training             | Elena Vargas   | Applicable training programs, duration, delivery format         |
| `soporte`       | Customer Support (outsourcing) | Roberto Díaz   | Agent staffing, shifts, committed response SLA                  |

Not every RFP needs all three departments: it depends on which service(s) the client is asking for (headhunting, training, outsourced support, or a combination). Your classifier/orchestrator agent must identify which departments apply by reading the document — never activate all three by default.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and headquarters (Spain or Miami — this determines the proposal's currency), requested service(s), volume (number of roles, number of agents, number of training participants), deadline, and sometimes a reference budget.

### 2.3 Suggested Entities for Your State

Persist **Ticket**, **RFP metadata**, and **DepartmentSection** (at least `key_aspects` in Part 1; drafts/evals/approvals in later parts) in **PostgreSQL (Supabase)** via your existing SQLModel/DB layer. TinyDB or JSON files are not the source of truth for these entities.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `client_hq` (Spain/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`, readability metrics
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

**Ticket status by part** (same ticket across Parts 1–3):

| Status                 | Part | When                                           |
| ---------------------- | ---- | ---------------------------------------------- |
| `analyzing`            | 1    | Upload accepted; pipeline running              |
| `discarded`            | 1    | Classifier rejected the document               |
| `intake_complete`      | 1    | Synthesizer done; Sales can read key aspects   |
| `drafting`             | 2    | Generators writing proposal sections           |
| `under_evaluation`     | 2    | Parallel evaluators / generator-evaluator loop |
| `needs_human_review`   | 2    | Iteration limit exhausted; last draft + EvaluationResult hand off to Part 3 |
| `waiting_for_approval` | 3    | Human-in-the-loop pause per department         |
| `done`                 | 3    | Final document generated                       |

Workers receive **shared metadata + department-relevant extracts** only. If volume/scope figures are missing, record open questions — **never invent** headcount, agent counts, or training seats not present in the RFP.

### 2.4 Monorepo layout

- **HTTP**: extend the **existing** backend under `services/` — no new API process.
- **Pipeline / graph**: `data/pipelines/rfp_intake/` (dedicated graph; do not mix into the CX agent graph). Routers import and trigger; they do not own agent logic.
- **Standalone CLIs**: `scripts/` if needed.
- **Uploaded PDFs**: provided via `uis/backoffice`; stored under `data/raw/` as a runtime artifact of intake.

## 3. Business Metrics and KPIs

- **Proposal drafting time**: today it eats up roughly 1 week of the total sales cycle → target: under 2 days from RFP upload to a ready final document.
- **Correct classification rate** of RFPs vs. non-RFP documents.
- **Average iterations per section** in the generator-evaluator loop (target: fewer than 2).
- **Approval time per department** from when a section is ready to the owner's decision.

## 4. Seed Data Instructions

Use the ready-made PDFs in [`rfp-requests/nexova/`](./rfp-requests/nexova/) as **test uploads through the UI**. The intake process stores each uploaded PDF under `data/raw/` (do not treat curriculum seed PDFs as pre-seeded inventory in the repo). Formal and informal RFPs must both be **accepted and processed**; the invalid document must be **rejected**.

1. **`CONTEXT-nexova-request-1.pdf` — formal RFP (accept):** _Vantex Retail Group_ (Madrid), executive search for 5 mid-management roles + quarterly leadership program. Triggers `seleccion` and `capacitacion`. Currency: EUR.
2. **`CONTEXT-nexova-request-2.pdf` — informal RFP (accept):** _NubeSoft_ (Miami SaaS) email requesting 24/7 support team of 12 agents. Triggers `soporte` (and possibly `seleccion`). Currency: USD.
3. **`CONTEXT-nexova-request-3.pdf` — invalid (reject):** inbound ATS vendor pitch — not a client RFP. Classifier must discard it.

## 5. Business Constraints (Guidelines for the Compliance Evaluator)

- Every proposal must include Nexova's standard 90-day satisfaction guarantee.
- Pricing is quoted in EUR for clients headquartered in Spain, and in USD for clients headquartered in Miami/US — determined by the `client_hq` field in the RFP metadata.
- No executive search proposal may commit to a time-to-close shorter than 15 business days.
- Every outsourced support proposal must explicitly mention the 24-hour response SLA.
- No proposal may include current client names as references without anonymizing them (use "a retail-sector client," not the real name).

## 6. Expected Deliverables

- **Part 1:** the ticket correctly identifies whether a document is a Nexova RFP, extracts metadata (including client headquarters), and splits the analysis only across the departments the requested service actually needs.
- **Part 2:** each active department generates its section and goes through evaluation for readability, relevance, and compliance with the guidelines in section 5 (including the correct currency).
- **Part 3:** each active department's named owner (§2.1) approves its section independently, without blocking the others, and the final document is generated only once all active sections are approved. Do **not** invent a multi-level approval ladder.

## 7. Part 3 — Conflict Triggers and Fixed Arbiter

Arbitration must be a dedicated graph node driven by **detectable contradictions in structured state**, not agents negotiating among themselves.

| Trigger id               | When it fires                                                                                              | Fixed arbiter (not an LLM)                                                            | Resolution rule                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ttc-vs-training-window` | `seleccion` time-to-close overlaps or contradicts `capacitacion` delivery window for the same cohort/roles | Marcos Ibáñez (Sales Director)                                                        | Sequence deliveries; force `request_changes` so training cannot start before selection commits a realistic close date (≥15 business days for executive search) |
| `support-sla-missing`    | Active `soporte` section omits the mandatory 24-hour response SLA (§5)                                     | Roberto Díaz (`soporte`) rejects; Marcos if other sections contradict staffing vs SLA | Block approval until 24h SLA is explicit; revise headcount if SLA is infeasible                                                                                |
| `currency-mismatch`      | Sections disagree on currency, or currency ≠ `client_hq` mapping (Spain→EUR, Miami/US→USD)                 | Marcos Ibáñez                                                                         | Rewrite to headquarters currency; reject if unresolved after iteration limit                                                                                   |

Wire these trigger ids into your arbitration node. Agents may **surface** a conflict; they must not **resolve** it by free-form consensus.
