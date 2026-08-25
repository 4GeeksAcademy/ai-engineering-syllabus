# CONTEXT — HealthCore: Centralized Incident Manager

## 1. Company Snapshot

**HealthCore** operates 12 outpatient clinics across the US and UK. Operational incidents — an EHR outage, a billing system failure, a compliance concern, a staffing gap — are reported today by phone, informal email, or word of mouth between **Dr. Marcus Reid**'s clinical team, **Tom Callahan**'s revenue cycle team, and **Claire Whitfield**'s compliance team, with no shared record. Nobody can answer "how many system incidents did we have in UK clinics this quarter?" and Claire has no reliable way to demonstrate incident response times during a regulatory review.

You are building the backoffice tool that gives HealthCore Digital a single, auditable place to log and track every operational incident — clinical operations, billing, compliance, staffing, and technology — across all 12 locations in both countries.

## 2. ⚠️ Non-Negotiable Data Constraint

**No PHI, patient identifiers, or HIPAA/UK GDPR-regulated data may appear in any log, event, table, endpoint response, or system output.** This incident manager tracks operational and system incidents — it is not a clinical record and must never reference an individual patient by name, medical record number, date of birth, or any other identifier. If an incident genuinely involves a specific patient (e.g. a documentation error affecting one patient's record), reference it only through an opaque `patient_ref` token that carries no clinical meaning on its own — never a name or record number. If your implementation cannot describe an incident without patient detail, the description is wrong, not the constraint.

## 3. Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 3.1 Intake Channels

| Value | Description |
|---|---|
| `internal_ticket` | Raised through HealthCore's internal ticketing system |
| `phone` | Called in directly to the relevant department |
| `monitoring_alert` | Automatically flagged by a system health monitor |
| `compliance_escalation` | Escalated by email from the Compliance team |
| `dashboard` | Entered directly into the backoffice |

### 3.2 Incident Types

| Value | Description |
|---|---|
| `system_outage` | EHR, billing platform, or scheduling system unavailable |
| `billing_issue` | Claims processing failure, denial spike, or coding error pattern |
| `compliance_concern` | A potential HIPAA or UK GDPR compliance issue (access anomaly, policy gap, vendor agreement lapse) |
| `staffing_gap` | A clinic understaffed for scheduled patient volume |
| `data_integrity` | A system integration or data sync issue not tied to a specific patient record |
| `vendor_sla_breach` | A technology or service vendor missed a contracted SLA |

### 3.3 Severity Levels

| Value | Meaning | Regulatory framing |
|---|---|---|
| `critical` | Active compliance exposure or a clinic cannot operate | Anything with a plausible breach-notification clock running (60 days under HIPAA, 72 hours to the ICO under UK GDPR) is `critical` by default |
| `high` | Significant clinical or financial risk, contained for now | EHR degraded but functional; a denial spike affecting one payer |
| `medium` | Noticeable but contained impact | A single clinic short-staffed for one shift |
| `low` | No immediate operational impact | Cosmetic dashboard display issue |

### 3.4 Responsible Areas

`clinical_operations`, `patient_experience`, `revenue_cycle`, `compliance`, `people_and_workforce`, `technology`

## 4. Entity Fields

An incident record must include, at minimum:

- `clinic_location` (one of the 12 HealthCore clinics; nullable if the incident is network-wide, e.g. a central system outage) and `country` (`us` or `uk`)
- `channel` (§3.1), `type` (§3.2), `severity` (§3.3), `responsible_area` (§3.4)
- `title`, `description` — must comply with §2
- `status` (see §5)
- `assigned_to`
- `patient_ref` (nullable, opaque token only — see §2; never a name, MRN, or DOB)
- `created_at`, `updated_at`

## 5. State Lifecycle

`open → assigned → in_progress → resolved → closed`

An incident may move to `reopened` from `resolved` if the same issue recurs at the same clinic or system before closure — this must remain visible in the change history, not overwrite it.

## 6. Traceability (non-negotiable)

Every transition between the states in §5, and every change of `assigned_to` or `responsible_area`, must be captured as a discrete, timestamped, authored record. This is not optional documentation hygiene here — it's what Claire's team pulls during a regulatory review to demonstrate response times, and it is the access-audit-log habit this milestone is meant to build ahead of any pipeline that will later touch real patient data.

## 7. Seed Data

Seed at least 12 incidents covering:

- All four severity levels
- Both countries (`us` and `uk`)
- At least one `compliance_concern` incident at `critical` severity
- At least one `reopened` incident with a visible history of the recurrence
- At least one incident using a `patient_ref` token, to confirm no real patient data leaks into the field
- Zero incidents anywhere in the seed set that violate §2 — this is graded, not advisory

## 8. Business Constraints

- A `critical` incident cannot be set to `closed` without passing through `resolved` first.
- Every field, log line, and generated document produced by this feature must be checked against §2 before it's considered complete — including console output, seed scripts, and any AI-generated summary text.
- The backoffice UI's base language is English; Spanish is optional and not required for this milestone (HealthCore's multilingual commitment applies to patient-facing tools, not this internal one).

## 9. Expected Deliverables

- Incident CRUD scoped to the fields in §4, using only the catalogue values in §3, and respecting §2 without exception.
- A view of open incidents groupable or filterable by `severity`, matching the README's "volume by severity" requirement.
- A visible, per-incident audit trail satisfying §6.
