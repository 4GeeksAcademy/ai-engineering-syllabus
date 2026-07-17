# CONTEXT — Nexova: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

At Nexova, RFPs go straight to **Marcos Ibáñez's** team, the **Sales Director**: prospective clients (tech, retail, or finance companies) asking for a proposal to outsource selection, customer support, or corporate training. The current sales cycle runs 3 to 8 weeks, and a good chunk of that time goes into back-and-forth emails with Selection, Training, or Support to nail down scope and price.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers:

| `department_id` | Department                        | Owner            | What it contributes to the proposal                                       |
| ---------------- | ------------------------------------ | ------------------ | ------------------------------------------------------------------------------ |
| `seleccion`         | Talent Selection Operations           | Javier Almeida        | Roles to fill, estimated time-to-close, consulting hours needed               |
| `capacitacion`       | Corporate Training                    | Elena Vargas           | Applicable training programs, duration, delivery format                       |
| `soporte`            | Customer Support (outsourcing)         | Roberto Díaz           | Agent staffing, shifts, committed response SLA                                |

Not every RFP needs all three departments: it depends on which service(s) the client is asking for (headhunting, training, outsourced support, or a combination). Your classifier/orchestrator agent must identify which departments apply by reading the document — never activate all three by default.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and headquarters (Spain or Miami — this determines the proposal's currency), requested service(s), volume (number of roles, number of agents, number of training participants), deadline, and sometimes a reference budget.

### 2.3 Suggested Entities for Your State

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `waiting_for_approval`, `drafting`, `under_evaluation`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_hq` (Spain/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

## 3. Business Metrics and KPIs

- **Proposal drafting time**: today it eats up roughly 1 week of the total sales cycle → target: under 2 days from RFP upload to a ready final document.
- **Correct classification rate** of RFPs vs. non-RFP documents.
- **Average iterations per section** in the generator-evaluator loop (target: fewer than 2).
- **Approval time per department** from when a section is ready to the owner's decision.

## 4. Seed Data Instructions

Create at least 3 test documents in `data/raw/`:

1. **Valid RFP (headhunting + training):** *Vantex Retail Group* (Madrid) requests an executive search for 5 mid-management positions plus a quarterly leadership program. Deadline: 15 days. Triggers `seleccion` and `capacitacion`. Currency: EUR.
2. **Valid RFP (outsourced support):** *NubeSoft* (a Miami-based SaaS startup) requests a 24/7 customer support team of 12 agents. Deadline: 20 days. Triggers `soporte` (and possibly `seleccion` to recruit the agents). Currency: USD.
3. **Document that is NOT an RFP:** an email from a software vendor pitching Nexova a new ATS tool. It has no client, scope, or expected response deadline from Nexova to a third party — it's an inbound pitch, not a request for proposal. Your classifier should discard it.

## 5. Business Constraints (Guidelines for the Compliance Evaluator)

- Every proposal must include Nexova's standard 90-day satisfaction guarantee.
- Pricing is quoted in EUR for clients headquartered in Spain, and in USD for clients headquartered in Miami/US — determined by the `client_hq` field in the RFP metadata.
- No executive search proposal may commit to a time-to-close shorter than 15 business days.
- Every outsourced support proposal must explicitly mention the 24-hour response SLA.
- No proposal may include current client names as references without anonymizing them (use "a retail-sector client," not the real name).

## 6. Expected Deliverables

- **Part 1:** the ticket correctly identifies whether a document is a Nexova RFP, extracts metadata (including client headquarters), and splits the analysis only across the departments the requested service actually needs.
- **Part 2:** each active department generates its section and goes through evaluation for readability, relevance, and compliance with the guidelines in section 5 (including the correct currency).
- **Part 3:** each department approves its section independently, without blocking the others, and the final document is generated only once all active sections are approved.
