# CONTEXT — Brasaland: Centralized Incident Manager

## 1. Company Snapshot

**Brasaland** is a grilled food restaurant chain with 14 company-owned locations across Colombia and Florida. Restaurant Operations, run by **Felipe Guerrero**, has no centralized visibility into what goes wrong at each location day to day: equipment failures, food safety concerns, staffing gaps, and supplier delays are currently reported by WhatsApp or phone call and vanish into individual chat threads. Felipe finds out about problems late, and there is no way to answer "how many incidents did the Medellín downtown location have this month?"

You are building the backoffice tool that lets any location report an incident, routes it to the right team, and gives Felipe and the other department heads a live picture of what's open, what's overdue, and who's accountable.

## 2. Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Intake Channels

| Value | Description |
|---|---|
| `whatsapp` | Reported via the location manager's WhatsApp group |
| `phone_call` | Called in directly to Operations |
| `pos_alert` | Automatically flagged by the POS terminal (e.g. no sales registered for 2+ hours) |
| `in_person` | Logged by a supervisor visiting the location |
| `dashboard` | Entered directly into the backoffice by a manager |

### 2.2 Incident Types

| Value | Description |
|---|---|
| `food_safety` | Spoilage, contamination risk, temperature control failure |
| `equipment_failure` | Grill, refrigeration, POS terminal, or kitchen equipment down |
| `staffing_gap` | Location understaffed for a shift |
| `supplier_delay` | Ingredient delivery late or incomplete |
| `customer_complaint` | Escalated complaint requiring management response |
| `system_outage` | POS, ordering app, or internal tool unavailable |

### 2.3 Severity Levels

| Value | Meaning | Example |
|---|---|---|
| `critical` | Location cannot operate or a food safety risk is active | Refrigeration failure with product at risk |
| `high` | Significant service degradation | One of two grills down during peak hours |
| `medium` | Noticeable but manageable impact | Minor ingredient shortage, workaround available |
| `low` | No immediate operational impact | Cosmetic POS glitch |

### 2.4 Responsible Areas

`restaurant_operations`, `procurement`, `marketing`, `people_and_culture`, `training_and_quality`, `technology`

## 3. Entity Fields

An incident record must include, at minimum:

- `location_id` and `location_name` (one of the 14 Brasaland locations — seed at least 4, mixing Colombia and Florida)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (see §4)
- `assigned_to` (a team member name or role)
- `created_at`, `updated_at`
- Currency-neutral: Brasaland operates in both COP and USD locations, but incidents themselves carry no monetary field — don't invent one.

## 4. State Lifecycle

`open → assigned → in_progress → resolved → closed`

An incident may also move to `reopened` from `resolved` if the same issue recurs within a location before closure — this must remain visible in the change history, not overwrite it.

## 5. Traceability (non-negotiable)

Every transition between the states in §4, and every change of `assigned_to` or `responsible_area`, must be captured as a discrete, timestamped, authored record — not just reflected in the current field value. Felipe needs to be able to open an incident and see its full history: who assigned it, when it moved to `in_progress`, who reassigned it and why the responsible area changed, if it did.

## 6. Seed Data

Seed at least 12 incidents covering:

- All four severity levels
- At least 4 different locations across both countries
- At least 4 different intake channels
- At least one `reopened` incident with a visible history of the recurrence
- At least one incident still `open` with no assignment (to exercise the "unassigned" view)

## 7. Business Constraints

- A `critical` incident cannot be set to `closed` without passing through `resolved` first — there is no shortcut state transition.
- An incident's `responsible_area` can change after creation (e.g. a `system_outage` first routed to `technology` may turn out to be a `procurement` issue), and each reassignment must be traceable per §5.
- Two languages are optional but highly recommended for the backoffice UI (Spanish/English), matching Brasaland's cross-country operation — pick one base language and treat the second as an enhancement.

## 8. Expected Deliverables

- Incident CRUD scoped to the fields in §3, using only the catalogue values in §2.
- A view of open incidents grouped or filterable by `severity`, matching the README's "volume by severity" requirement.
- A visible, per-incident audit trail satisfying §5 — this is what Felipe's sign-off checks first.
