# CONTEXT — Brasaland: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

Brasaland doesn't have a traditional "Sales" department: corporate RFPs (institutional catering contracts, co-branding partnerships, event or resort concessions) land on **Camila Ospina's** desk, **Marketing, Brand and Digital Experience**, whose team already handles campaigns and CRM and also fields and coordinates this kind of B2B opportunity. For this milestone, the Marketing team is your "Sales": they open the ticket and wait for the agentic flow's result.

Today, when one of these requests comes in, Camila forwards the PDF over WhatsApp to Felipe (Operations), Lucía (Procurement), and Jake (Training), then waits for scattered replies by email. Putting together a full proposal takes **9 business days on average**, and more than once an opportunity has been lost because a department didn't respond in time. Your agentic workflow replaces that manual coordination.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers in your code and graph state:

| `department_id` | Department                       | Owner           | What it contributes to the proposal                                                             |
| --------------- | -------------------------------- | --------------- | ----------------------------------------------------------------------------------------------- |
| `marketing`     | Marketing and Digital Experience | Camila Ospina   | Brand terms, exclusivity, co-branding, offer validity period. Owns the ticket.                  |
| `operaciones`   | Restaurant Operations            | Felipe Guerrero | Operational feasibility: kitchen/staff capacity, setup times, cost per event                    |
| `procurement`   | Procurement and Suppliers        | Lucía Fernández | Estimated ingredient cost based on volume, supplier lead times                                  |
| `training`      | Training and Quality Standards   | Jake Morrison   | If the request requires a new recipe or standard, the development and certification time needed |

Not every RFP needs all four departments: a simple catering request might not require `training` (for example, if it uses the standard menu). Your classifier/orchestrator agent must decide which departments apply based on the document's content — don't assume it's always all four.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and location, type of service requested (recurring catering, concession, co-branding), volume or scope (number of diners, locations, contract length), response deadline, and sometimes a budget range. They aren't always well structured — some are informal letters of intent.

### 2.3 Suggested Entities for Your State

Persist **Ticket**, **RFP metadata**, and **DepartmentSection** (at least `key_aspects` in Part 1; drafts/evals/approvals in later parts) in **PostgreSQL (Supabase)** via your existing SQLModel/DB layer. TinyDB or JSON files are not the source of truth for these entities.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (optional), `departments_needed`, readability metrics
- **DepartmentSection**: `department_id`, `key_aspects` (Part 1), `draft_content` (Part 2), `evaluation_results` (readability, relevance, compliance), `approval_status` (`pending`, `approved`, `rejected`), `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `total_estimated_value`, `generated_at`

**Ticket status by part** (same ticket across Parts 1–3):

| Status                 | Part | When                                                         |
| ---------------------- | ---- | ------------------------------------------------------------ |
| `analyzing`            | 1    | Upload accepted; pipeline running                            |
| `discarded`            | 1    | Classifier rejected the document                             |
| `intake_complete`      | 1    | Synthesizer done; Sales can read key aspects                 |
| `drafting`             | 2    | Generators writing proposal sections                         |
| `under_evaluation`     | 2    | Parallel evaluators / generator-evaluator loop               |
| `needs_human_review`   | 2    | Iteration limit exhausted; last draft + EvaluationResult hand off to Part 3 |
| `waiting_for_approval` | 3    | Human-in-the-loop pause per department (and CEO if required) |
| `done`                 | 3    | Final document generated                                     |

Workers receive **shared metadata + department-relevant extracts** only. If a figure (volume, budget, diner count, etc.) is absent from the RFP, record it under `open_questions` / missing fields — **never invent** numbers not present in the document.

### 2.4 Monorepo layout

- **HTTP**: extend the **existing** backend under `services/` — no new API process.
- **Pipeline / graph**: `data/pipelines/rfp_intake/` (dedicated graph; do not mix into the CX agent graph). Routers import and trigger; they do not own agent logic.
- **Standalone CLIs**: `scripts/` if needed.
- **Uploaded PDFs**: provided via `uis/backoffice`; stored under `data/raw/` as a runtime artifact of intake.

## 3. Business Metrics and KPIs

- **Proposal cycle time**: today ~9 business days → target with the agentic workflow: under 2 business days from RFP upload to a ready final document.
- **Correct classification rate**: % of documents correctly identified as RFPs vs. discarded.
- **Average iterations per section**: how many times, on average, a section bounces from evaluator back to generator before passing (target: fewer than 2).
- **Approval time per department**: from when a section is ready to when the owner approves or rejects it.

## 4. Seed Data Instructions

Use the ready-made PDFs in [`rfp-requests/brasaland/`](./rfp-requests/brasaland/) as **test uploads through the UI**. The intake process stores each uploaded PDF under `data/raw/` (do not treat curriculum seed PDFs as pre-seeded inventory in the repo). Formal and informal RFPs must both be **accepted and processed**; the invalid document must be **rejected**.

1. **`CONTEXT-brasaland-request-1.pdf` — formal RFP (accept):** _Sunset Bay Resorts_, co-branded concession across 3 Florida resorts, exclusivity + new signature menu, ~$60–75k USD/year. Triggers all four departments, including `training`. **Note:** above $50,000 USD/year → extra CEO approval (Mariana Restrepo) in Part 3.
2. **`CONTEXT-brasaland-request-2.pdf` — informal RFP (accept):** _Andes Tech Solutions_ email requesting weekly catering for 220 employees in Medellín, 12-month contract, standard menu. Triggers `marketing`, `operaciones`, and `procurement` (not necessarily `training`).
3. **`CONTEXT-brasaland-request-3.pdf` — invalid (reject):** franchise inquiry with no scope, budget, or deadline. Classifier must discard it.

## 5. Business Constraints (Guidelines for the Compliance Evaluator)

- Every price must be expressed in both COP and USD.
- Every proposal must mention, at least once, the brand's three pillars: consistent quality, warm experience, speed of service.
- No section may promise setup/delivery times shorter than 10 business days.
- No proposal may mention competitors by name.
- Every proposal must include an offer validity period (30 days from issuance).
- Estimated contracts above $50,000 USD/year require an additional CEO approval before the final document is generated.

## 6. Expected Deliverables

- **Part 1:** the ticket correctly identifies whether a document is a Brasaland RFP, extracts metadata, and splits the analysis across `marketing`, `operaciones`, `procurement`, and `training` (only the ones that apply).
- **Part 2:** each active department generates its proposal section and goes through evaluation for readability, relevance, and compliance with the guidelines in section 5.
- **Part 3:** each active department's named owner (§2.1) approves independently; when estimated contract value exceeds $50,000 USD/year, **Mariana Restrepo (CEO)** must also approve before synthesis. Do not invent further hierarchy beyond that CONTEXT rule.

## 7. Part 3 — Conflict Triggers and Fixed Arbiter

Arbitration must be a dedicated graph node driven by **detectable contradictions in structured state**, not agents negotiating among themselves.

| Trigger id            | When it fires                                                                                                   | Fixed arbiter (not an LLM)                                                              | Resolution rule                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `cost-vs-feasibility` | `procurement` ingredient/cost estimate cannot support the per-event or per-cover price implied by `operaciones` | Camila Ospina (Marketing; ticket owner)                                                 | Raise price or reduce scope; force `request_changes` on the mismatched section(s) |
| `setup-sla-breach`    | Any section promises setup/delivery under 10 business days (violates §5)                                        | Felipe Guerrero (`operaciones`) rejects; Camila escalates if other depts still embed it | Force `request_changes` until ≥10 business days everywhere                        |
| `ceo-threshold`       | Estimated annual value exceeds $50,000 USD and CEO approval still pending                                       | Mariana Restrepo (CEO)                                                                  | Block ultimate synthesizer until CEO `approve`; reject path if CEO rejects        |

Wire these trigger ids into your arbitration node. Agents may **surface** a conflict; they must not **resolve** it by free-form consensus.
