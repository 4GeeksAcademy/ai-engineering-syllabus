# CONTEXT — TrackFlow: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

At TrackFlow, RFPs land on **Miguel Torres's** desk, the **Commercial Director**: e-commerce brands (fashion, electronics, cosmetics) that want to outsource their logistics — warehousing, last mile, returns, or a combination — in the United States, Spain, or both. Today, each account manager builds the proposal by hand, coordinating by email with Warehouse, Last Mile, and Reverse Logistics; the process is slow, and sometimes a proposal arrives after the prospect has already signed with another provider.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers:

| `department_id` | Department                       | Owner         | What it contributes to the proposal                                     |
| --------------- | -------------------------------- | ------------- | ----------------------------------------------------------------------- |
| `warehouse`     | Warehouse Operations             | Ana Whitfield | Storage capacity, cost per pallet/SKU, onboarding time                  |
| `lastmile`      | Last Mile and Carrier Management | Carlos Vega   | Cost per shipment, available carriers by destination, delivery SLA      |
| `reverse`       | Reverse Logistics                | Sofía Ramos   | Returns processing cost and turnaround time (if the client requests it) |

Not every RFP needs all three departments: a client might request only warehousing and returns, without last mile (because they use their own carrier), for example. Your classifier/orchestrator agent must decide which departments apply based on the requested scope.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and country of origin (US or Spain — determines the currency), requested services (warehousing, last mile, reverse logistics), estimated volume (orders/month), deadline, and sometimes a reference budget.

### 2.3 Suggested Entities for Your State

Persist **Ticket**, **RFP metadata**, and **DepartmentSection** (at least `key_aspects` in Part 1; drafts/evals/approvals in later parts) in **PostgreSQL (Supabase)** via your existing SQLModel/DB layer. TinyDB or JSON files are not the source of truth for these entities.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`, readability metrics
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

Workers receive **shared metadata + department-relevant extracts** only. Example: `warehouse` gets warehousing slices / metadata — if monthly volume is missing, record an open question; **never invent** pallet/SKU/order volumes not present in the RFP.

### 2.4 Monorepo layout

- **HTTP**: extend the **existing** backend under `services/` — no new API process.
- **Pipeline / graph**: `data/pipelines/rfp_intake/` (dedicated graph; do not mix into the CX agent graph). Routers import and trigger; they do not own agent logic.
- **Standalone CLIs**: `scripts/` if needed.
- **Uploaded PDFs**: provided via `uis/backoffice`; stored under `data/raw/` as a runtime artifact of intake.

## 3. Business Metrics and KPIs

- **Proposal build time**: today it's several days of manual coordination → target: under 2 days from RFP upload to a ready final document.
- **Correct classification rate** of RFPs vs. non-RFP documents.
- **Average iterations per section** in the generator-evaluator loop (target: fewer than 2).
- **Approval time per department** from when a section is ready to the owner's decision.

## 4. Seed Data Instructions

Use the ready-made PDFs in [`rfp-requests/trackflow/`](./rfp-requests/trackflow/) as **test uploads through the UI**. The intake process stores each uploaded PDF under `data/raw/` (do not treat curriculum seed PDFs as pre-seeded inventory in the repo). Formal and informal RFPs must both be **accepted and processed**; the invalid document must be **rejected**.

1. **`CONTEXT-trackflow-request-1.pdf` — formal RFP (accept):** _ModaViva_ (Spain), warehousing + returns only (own carrier for last mile). Triggers `warehouse` and `reverse`, not `lastmile`. Currency: EUR.
2. **`CONTEXT-trackflow-request-2.pdf` — informal RFP (accept):** _Luna Cosmetics_ (LA) email requesting warehousing + last mile for US, ~5,000 orders/month. Triggers `warehouse` and `lastmile`. Currency: USD.
3. **`CONTEXT-trackflow-request-3.pdf` — invalid (reject):** inbound carrier rate pitch — not a client RFP. Classifier must discard it.

## 5. Business Constraints (Guidelines for the Compliance Evaluator)

- Pricing is quoted in USD for US operations and in EUR for Spain operations — determined by the `client_country` field.
- Every proposal must state the on-time delivery SLA (%) TrackFlow is committing to.
- No proposal may promise returns processing in under 48 hours.
- Every proposal must include a volume-based discount tier table.
- No proposal may disclose negotiated rates with specific carriers — only the final cost offered to the client.

## 6. Expected Deliverables

- **Part 1:** the ticket correctly identifies whether a document is a TrackFlow RFP, extracts metadata (including the client's country), and splits the analysis only across the departments the requested scope actually needs.
- **Part 2:** each active department generates its section and goes through evaluation for readability, relevance, and compliance with the guidelines in section 5 (including the correct currency and SLA).
- **Part 3:** each active department's named owner (§2.1) approves its section independently, without blocking the others, and the final document is generated only once all active sections are approved. Do **not** invent a multi-level approval ladder — TrackFlow has peer department owners only.

## 7. Part 3 — Conflict Triggers and Fixed Arbiter

Arbitration must be a dedicated graph node driven by **detectable contradictions in structured state**, not agents negotiating among themselves.

| Trigger id           | When it fires                                                                                                                 | Fixed arbiter (not an LLM)                                                                | Resolution rule                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `volume-vs-capacity` | `warehouse` committed capacity (pallets/SKU or onboarding throughput) cannot support the monthly volume assumed by `lastmile` | Miguel Torres (Commercial Director)                                                       | Cap the proposal volume to warehouse capacity; `lastmile` must revise quoted volume/cost downward |
| `returns-sla-breach` | `reverse` (or any section) promises returns turnaround under 48 hours (violates §5)                                           | Sofía Ramos rejects her section; if another dept still embeds that promise, Miguel Torres | Force `request_changes` on every section stating under-48h returns; no final doc until compliant  |
| `currency-mismatch`  | Two active sections quote different currencies, or currency ≠ `client_country` mapping (US→USD, Spain→EUR)                    | Miguel Torres                                                                             | Rewrite offending sections to the country currency; reject if unresolved after iteration limit    |

Wire these trigger ids into your arbitration node. Agents may **surface** a conflict; they must not **resolve** it by free-form consensus.
