# CONTEXT — Nexova: Centralized Incident Manager

## 1. Company Snapshot

**Nexova** is an HR consulting firm operating across three business lines — executive headhunting, outsourced customer support (30 agents serving Nexova's own clients), and corporate training — from Valencia and Miami. Incidents today live wherever they happened to land: a Slack DM to **Roberto Díaz**'s support team, an email to Operations Manager **Javier Almeida**, or a call nobody wrote down. There's no shared view of what's open across the three business lines, and SLA breaches on the outsourced support contracts go unnoticed until a client complains.

You are building the backoffice tool that centralizes incident intake across all of Nexova's business lines and makes SLA risk visible before it becomes a client escalation.

## 2. Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Intake Channels

| Value | Description |
|---|---|
| `email` | Reported by email to a department head |
| `slack` | Reported in an internal Slack channel |
| `helpdesk_ticket` | Raised through the outsourced support helpdesk |
| `client_call` | Called in directly by a Nexova client |
| `dashboard` | Entered directly into the backoffice |

### 2.2 Incident Types

| Value | Description |
|---|---|
| `sla_breach` | An outsourced support SLA commitment was missed or is at risk |
| `client_escalation` | A client has escalated dissatisfaction beyond the assigned consultant/agent |
| `system_outage` | ATS, CRM, or helpdesk tool unavailable |
| `data_issue` | Candidate or client data entered incorrectly, duplicated, or lost |
| `staffing_gap` | Outsourced support team understaffed for contracted coverage |
| `compliance_flag` | A potential HR or labor-law compliance concern raised internally |

### 2.3 Severity Levels

| Value | Meaning | Example |
|---|---|---|
| `critical` | Contractual SLA breached or client threatening to churn | 24h SLA missed by 20+ hours on a key account |
| `high` | Significant risk to a client relationship or deliverable | Selection process stalled with client deadline in 48h |
| `medium` | Noticeable but contained impact | Single candidate record needs correction |
| `low` | No immediate business impact | Minor helpdesk tool glitch |

### 2.4 Responsible Areas

`marketing`, `sales`, `hr_internal`, `talent_selection`, `corporate_training`, `customer_support`, `technology`

## 3. Entity Fields

An incident record must include, at minimum:

- `client_name` (nullable — not every incident is tied to an external client; internal HR or tooling incidents may have none)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (see §4)
- `assigned_to`
- `sla_deadline` (nullable — only populated when `type` is `sla_breach` or the incident is tied to a contracted SLA)
- `created_at`, `updated_at`

## 4. State Lifecycle

`open → assigned → in_progress → resolved → closed`

An incident may move to `reopened` from `resolved` if the same issue recurs on the same account or system before closure — this must remain visible in the change history, not overwrite it.

## 5. Traceability (non-negotiable)

Every transition between the states in §4, and every change of `assigned_to` or `responsible_area`, must be captured as a discrete, timestamped, authored record. This matters most for `sla_breach` incidents: if a client disputes when Nexova became aware of a problem, the audit trail is the evidence.

## 6. Seed Data

Seed at least 12 incidents covering:

- All four severity levels
- At least 3 different `responsible_area` values, including `customer_support`
- At least one `sla_breach` incident with a populated `sla_deadline` that has already passed
- At least one `reopened` incident with a visible history of the recurrence
- At least one incident with no `client_name` (internal-only)

## 7. Business Constraints

- Incidents of `type = sla_breach` must have a non-null `sla_deadline`; incidents of any other type must not populate it.
- A `critical` incident cannot be set to `closed` without passing through `resolved` first.
- Two languages are optional but highly recommended for the backoffice UI (Spanish/English), matching Nexova's Valencia/Miami operation — pick one base language and treat the second as an enhancement.

## 8. Expected Deliverables

- Incident CRUD scoped to the fields in §3, using only the catalogue values in §2.
- A view of open incidents groupable or filterable by `severity`, matching the README's "volume by severity" requirement, with SLA-breach incidents distinguishable at a glance.
- A visible, per-incident audit trail satisfying §5.
