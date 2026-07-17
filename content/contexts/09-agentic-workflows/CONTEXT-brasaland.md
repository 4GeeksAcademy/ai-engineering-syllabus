# CONTEXT — Brasaland: Milestone 9, Agentic Workflow Generation (Parts 1, 2 and 3)

> This document applies to all three parts of Milestone 9. Read it in full before starting Part 1 — Parts 2 and 3 reuse the same departments, RFP format, and guidelines defined here.

## 1. Introduction

Brasaland doesn't have a traditional "Sales" department: corporate RFPs (institutional catering contracts, co-branding partnerships, event or resort concessions) land on **Camila Ospina's** desk, **Marketing, Brand and Digital Experience**, whose team already handles campaigns and CRM and also fields and coordinates this kind of B2B opportunity. For this milestone, the Marketing team is your "Sales": they open the ticket and wait for the agentic flow's result.

Today, when one of these requests comes in, Camila forwards the PDF over WhatsApp to Felipe (Operations), Lucía (Procurement), and Jake (Training), then waits for scattered replies by email. Putting together a full proposal takes **9 business days on average**, and more than once an opportunity has been lost because a department didn't respond in time. Your agentic workflow replaces that manual coordination.

## 2. Departments and Data Structures

### 2.1 Departments Involved in the Proposal

Use exactly these department identifiers in your code and graph state:

| `department_id` | Department                     | Owner            | What it contributes to the proposal                                                        |
| ---------------- | -------------------------------- | ------------------ | -------------------------------------------------------------------------------------------- |
| `marketing`         | Marketing and Digital Experience  | Camila Ospina        | Brand terms, exclusivity, co-branding, offer validity period. Owns the ticket.                |
| `operaciones`        | Restaurant Operations              | Felipe Guerrero       | Operational feasibility: kitchen/staff capacity, setup times, cost per event                  |
| `procurement`        | Procurement and Suppliers          | Lucía Fernández       | Estimated ingredient cost based on volume, supplier lead times                                |
| `training`           | Training and Quality Standards     | Jake Morrison         | If the request requires a new recipe or standard, the development and certification time needed |

Not every RFP needs all four departments: a simple catering request might not require `training` (for example, if it uses the standard menu). Your classifier/orchestrator agent must decide which departments apply based on the document's content — don't assume it's always all four.

### 2.2 What a Real RFP Looks Like

RFPs arrive as PDFs and typically include: client name and location, type of service requested (recurring catering, concession, co-branding), volume or scope (number of diners, locations, contract length), response deadline, and sometimes a budget range. They aren't always well structured — some are informal letters of intent.

### 2.3 Suggested Entities for Your State

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `waiting_for_approval`, `drafting`, `under_evaluation`, `done`, `discarded`), `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (optional), `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects` (Part 1), `draft_content` (Part 2), `evaluation_results` (readability, relevance, compliance), `approval_status` (`pending`, `approved`, `rejected`), `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `total_estimated_value`, `generated_at`

## 3. Business Metrics and KPIs

- **Proposal cycle time**: today ~9 business days → target with the agentic workflow: under 2 business days from RFP upload to a ready final document.
- **Correct classification rate**: % of documents correctly identified as RFPs vs. discarded.
- **Average iterations per section**: how many times, on average, a section bounces from evaluator back to generator before passing (target: fewer than 2).
- **Approval time per department**: from when a section is ready to when the owner approves or rejects it.

## 4. Seed Data Instructions

Create at least 3 test documents in `data/raw/`:

1. **Valid RFP (routine):** *Andes Tech Solutions*, a Bogotá-based tech company, requests weekly catering for 220 employees at its Medellín office, a 12-month contract, deadline in 15 days. Should trigger `marketing`, `operaciones`, and `procurement` (not necessarily `training`, since it uses the standard menu).
2. **Valid RFP (complex, high value):** *Sunset Bay Resorts*, a Florida hotel chain, requests a co-branded concession in 3 of its resorts, with an exclusivity clause and a new signature menu. Estimated contract value over $60,000 USD/year, deadline in 30 days. Should trigger all four departments, including `training` because of the new menu. **Note:** since it exceeds $50,000 USD/year, this proposal requires an additional approval from Mariana Restrepo (CEO) before closing — implement this as an extra approval step in your Part 3.
3. **Document that is NOT an RFP:** a client's email informally asking about franchising opportunities, with no scope, budget, or deadline. Your classifier agent should discard it.

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
- **Part 3:** each department (and, when applicable, the CEO for the $50,000 USD/year threshold) approves its section independently, without blocking the others, and the final document is generated only once all required approvals are complete.
