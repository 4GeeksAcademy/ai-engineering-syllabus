# CONTEXT — TrackFlow: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

At TrackFlow, RFPs land on **Miguel Torres's** desk, the **Commercial Director**: e-commerce brands (fashion, electronics, cosmetics) that want to outsource their logistics — warehousing, last mile, returns, or a combination — in the United States, Spain, or both. Today, each account manager builds the proposal by hand, coordinating by email with Warehouse, Last Mile, and Reverse Logistics; the process is slow, and sometimes a proposal arrives after the prospect has already signed with another provider.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers:

| `department_id` | Department                         | Owner            | What it contributes to the proposal                                          |
| ---------------- | ------------------------------------- | ------------------ | ----------------------------------------------------------------------------------- |
| `warehouse`         | Warehouse Operations                    | Ana Whitfield          | Storage capacity, cost per pallet/SKU, onboarding time                              |
| `lastmile`           | Last Mile and Carrier Management         | Carlos Vega            | Cost per shipment, available carriers by destination, delivery SLA                  |
| `reverse`            | Reverse Logistics                       | Sofía Ramos            | Returns processing cost and turnaround time (if the client requests it)             |

Not every RFP needs all three departments: a client might request only warehousing and returns, without last mile (because they use their own carrier), for example. Your classifier/orchestrator agent must decide which departments apply based on the requested scope.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and country of origin (US or Spain — determines the currency), requested services (warehousing, last mile, reverse logistics), estimated volume (orders/month), deadline, and sometimes a reference budget.

### 2.3 Suggested Entities for Your State

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `waiting_for_approval`, `drafting`, `under_evaluation`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

## 3. Business Metrics and KPIs

- **Proposal build time**: today it's several days of manual coordination → target: under 2 days from RFP upload to a ready final document.
- **Correct classification rate** of RFPs vs. non-RFP documents.
- **Average iterations per section** in the generator-evaluator loop (target: fewer than 2).
- **Approval time per department** from when a section is ready to the owner's decision.

## 4. Seed Data Instructions

Create at least 3 test documents in `data/raw/`:

1. **Valid RFP (full scope):** *Luna Cosmetics*, a DTC brand based in Los Angeles, requests warehousing and last mile for the US market, ~5,000 orders/month. Deadline: 20 days. Triggers `warehouse` and `lastmile`. Currency: USD.
2. **Valid RFP (partial scope):** *Zaragoza ModaViva*, a Spanish fashion brand, requests only warehousing and returns management (it uses its own carrier for last mile). Deadline: 25 days. Triggers `warehouse` and `reverse`, not `lastmile`. Currency: EUR.
3. **Document that is NOT an RFP:** an email from a carrier company offering TrackFlow new shipping rates. It's an inbound pitch from a vendor, not a request from a client. Your classifier should discard it.

## 5. Business Constraints (Guidelines for the Compliance Evaluator)

- Pricing is quoted in USD for US operations and in EUR for Spain operations — determined by the `client_country` field.
- Every proposal must state the on-time delivery SLA (%) TrackFlow is committing to.
- No proposal may promise returns processing in under 48 hours.
- Every proposal must include a volume-based discount tier table.
- No proposal may disclose negotiated rates with specific carriers — only the final cost offered to the client.

## 6. Expected Deliverables

- **Part 1:** the ticket correctly identifies whether a document is a TrackFlow RFP, extracts metadata (including the client's country), and splits the analysis only across the departments the requested scope actually needs.
- **Part 2:** each active department generates its section and goes through evaluation for readability, relevance, and compliance with the guidelines in section 5 (including the correct currency and SLA).
- **Part 3:** each department approves its section independently, without blocking the others, and the final document is generated only once all active sections are approved.
