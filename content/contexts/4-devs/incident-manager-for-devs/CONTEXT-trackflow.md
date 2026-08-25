# CONTEXT — TrackFlow: Centralized Incident Manager

## 1. Company Snapshot

**TrackFlow** runs warehouse management and last-mile delivery across two markets — Los Angeles and Zaragoza — for mid-sized e-commerce brands. Incidents today are scattered across carrier portals, client emails, and phone calls to **Ana Whitfield**'s warehouse team or **Carlos Vega**'s carrier operations team. When something fails in Los Angeles, the Zaragoza team finds out by WhatsApp, if at all. There's no single place to see what's broken, who's on it, and whether it's about to breach a client's delivery SLA.

You are building the backoffice tool that gives TrackFlow Tech one place to log, route, and track every operational incident across both warehouses and all carrier relationships.

## 2. Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Intake Channels

| Value | Description |
|---|---|
| `carrier_portal_alert` | Flagged automatically from a carrier's tracking system |
| `client_email` | Reported by email from a TrackFlow client (e-commerce brand) |
| `wms_alert` | Automatically flagged by the warehouse management system |
| `warehouse_call` | Called in directly by warehouse floor staff |
| `dashboard` | Entered directly into the backoffice |

### 2.2 Incident Types

| Value | Description |
|---|---|
| `lost_parcel` | A shipment is missing or untracked past expected delivery |
| `inventory_discrepancy` | Recorded stock doesn't match physical stock at a warehouse |
| `carrier_failure` | A carrier missed a pickup, delayed a route, or delivered damaged goods |
| `system_outage` | WMS, tracking, or internal tool unavailable |
| `return_dispute` | A client or end customer disputes a return's approval or condition assessment |
| `sla_breach` | A client's contracted delivery or fulfillment SLA was missed |

### 2.3 Severity Levels

| Value | Meaning | Example |
|---|---|---|
| `critical` | Client-facing SLA breached or a warehouse is non-operational | WMS down at a full warehouse during peak hours |
| `high` | Significant risk to a client shipment volume or deadline | A carrier missed pickup for a full day's outbound volume |
| `medium` | Noticeable but contained impact | Inventory discrepancy on a single SKU |
| `low` | No immediate operational impact | Cosmetic tracking-portal display issue |

### 2.4 Responsible Areas

`warehouse_operations`, `last_mile_carrier`, `reverse_logistics`, `customer_experience`, `commercial`, `technology`

## 3. Entity Fields

An incident record must include, at minimum:

- `warehouse_location` (`los_angeles` or `zaragoza`, nullable if the incident isn't warehouse-specific — e.g. a pure carrier issue)
- `client_name` (the affected e-commerce brand, nullable for internal-only incidents)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (see §4)
- `assigned_to`
- `created_at`, `updated_at`

## 4. State Lifecycle

`open → assigned → in_progress → resolved → closed`

An incident may move to `reopened` from `resolved` if the same issue recurs for the same client or warehouse before closure — this must remain visible in the change history, not overwrite it.

## 5. Traceability (non-negotiable)

Every transition between the states in §4, and every change of `assigned_to` or `responsible_area`, must be captured as a discrete, timestamped, authored record. For `sla_breach` and `carrier_failure` incidents, this record is what Commercial uses to justify a service credit or dispute a carrier invoice — it has to be reliable.

## 6. Seed Data

Seed at least 12 incidents covering:

- All four severity levels
- Both warehouse locations
- At least 4 different intake channels
- At least one `reopened` incident with a visible history of the recurrence
- At least one incident with no `client_name` (purely internal, e.g. an internal system outage)

## 7. Business Constraints

- A `critical` incident cannot be set to `closed` without passing through `resolved` first.
- An incident's `responsible_area` can change after creation (e.g. a `lost_parcel` first routed to `last_mile_carrier` may turn out to be a `warehouse_operations` picking error), and each reassignment must be traceable per §5.
- Two languages are optional but highly recommended for the backoffice UI (Spanish/English), matching TrackFlow's Los Angeles/Zaragoza operation — pick one base language and treat the second as an enhancement.

## 8. Expected Deliverables

- Incident CRUD scoped to the fields in §3, using only the catalogue values in §2.
- A view of open incidents groupable or filterable by `severity`, matching the README's "volume by severity" requirement, with both warehouses represented.
- A visible, per-incident audit trail satisfying §5.
