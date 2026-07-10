# CONTEXT — Centralized Incident Manager · HealthCore

## Your Company

**HealthCore** is an outpatient healthcare services company with **12 clinics** — 9 in the USA (Texas, Florida, and Georgia) and 3 in the UK (London and Manchester). It employs approximately 200 people across clinical staff, operations, administration, and technology. Annual revenue is around $28 million.

As part of the **HealthCore Digital** team, you have been building the internal platform across several milestones. This project integrates a centralized incident manager into that platform. At HealthCore, an incident is not a minor concern: it may affect patient safety, regulatory compliance (HIPAA in the USA, UK GDPR in the UK), or the billing cycle. Structured incident recording is also an audit requirement.

> ⚠️ **Regulatory note:** This manager **must not store identifying patient data** (name, date of birth, medical record number, contact details). If an incident involves a patient, they must be referenced only by an opaque internal identifier. Any free-text field must include a visible warning to the user not to enter identifying patient data.

---

## Who Uses It and Why

**James Osei (CTO)** needs a traceable record of technology failures. No system currently records what failed, when, at which clinic, and how long it took to resolve.

**Claire Whitfield (Chief Compliance Officer)** needs to be able to audit incidents related to patient data access or procedural breaches. The system must be queryable by type and date to respond to regulatory audits.

**Dr. Marcus Reid (Director of Clinical Operations)** wants to know whether any clinic is accumulating clinical or equipment incidents that may affect patient care.

**Dr. Sandra Okonkwo (CEO)** wants executive visibility: how many critical incidents are open across the network, broken down by country.

---

## HealthCore Clinics

The `branch` field must contain exactly one of the following values:

| Database value       | Display name                 |
| -------------------- | ---------------------------- |
| `central`            | Central — Austin Main Clinic |
| `austin_north`       | Austin — North               |
| `dallas_uptown`      | Dallas Uptown                |
| `houston_med_center` | Houston Medical Center       |
| `san_antonio_west`   | San Antonio West             |
| `miami_brickell`     | Miami Brickell               |
| `miami_doral`        | Miami Doral                  |
| `orlando_east`       | Orlando East                 |
| `tampa_bay`          | Tampa Bay                    |
| `atlanta_midtown`    | Atlanta Midtown              |
| `savannah`           | Savannah                     |
| `london_city`        | London City                  |
| `london_west`        | London West End              |
| `manchester_central` | Manchester Central           |

Use `central` when the incident has no specific clinic — for example, `internal` reports from corporate leadership or `customer` complaints that cannot be tied to a clinic. `central` is HealthCore's headquarters in Austin (Main Clinic); it is also the branch for clinic code `US-TX-01`.

---

## Incident Categories

The `category` field must contain exactly one of the following values:

| Value                | Description                                                                           |
| -------------------- | ------------------------------------------------------------------------------------- |
| `clinical_equipment` | Clinical equipment failure or issue (no patient data involved)                        |
| `it_system`          | Technology system failure: EHR, patient portal, billing platform, integrations        |
| `billing_error`      | Error in the billing or claims coding process                                         |
| `compliance_breach`  | Potential regulatory non-compliance (HIPAA / UK GDPR) — no identifying patient data   |
| `patient_experience` | Patient experience issue: appointment, communication, wait time (no identifying data) |
| `staff_issue`        | Staff incident: absence, conflict, mandatory training overdue                         |
| `facility_issue`     | Facility problem: water, electricity, HVAC, cleaning                                  |
| `referral_issue`     | Problem in the inter-clinic referral process                                          |
| `other`              | Any incident that does not fit the categories above                                   |

---

## Status and Lifecycle

| Value         | Meaning at HealthCore                                             |
| ------------- | ----------------------------------------------------------------- |
| `open`        | Incident registered, pending assignment to the responsible person |
| `in_progress` | Owner identified and handling in progress                         |
| `resolved`    | Incident closed with corrective action documented                 |
| `discarded`   | Registered in error, duplicate, or out of scope                   |

Valid transitions: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. The `resolved` and `discarded` states are final.

---

## Origins

| Value      | When to use it at HealthCore                                        |
| ---------- | ------------------------------------------------------------------- |
| `customer` | Reported by a patient or their representative (no identifying data) |
| `branch`   | Reported by clinical or administrative staff at a specific clinic   |
| `internal` | Detected by technology, compliance, or corporate leadership         |

---

## Historical Data — Seed from CSV

The CSV file from the **incidents-file-analyzer** project (`incidents-<company>.csv` in `content/contexts/incidents-file-analysis/`) contains incidents exported from HealthCore's legacy patient services system. All of them correspond to incidents reported by patients or their representatives (`origin: "customer"`). The CSV does not contain identifying patient data — it was anonymised before extraction.

The analyzer CSV schema uses different field names, status values, and category codes than this manager. **Do not insert CSV rows directly.** Reuse the shared validation logic from the analyzer, then apply the transformations below before insert.

**Idempotency identifier:** use `incident_id` from the CSV to prevent duplicate records. If that field does not exist, use the combination `title + created_at`.

### Direct field mapping

| CSV field     | Model field   | Transformation                                                                   |
| ------------- | ------------- | -------------------------------------------------------------------------------- |
| `incident_id` | —             | Duplicate control only — not stored                                              |
| `description` | `title`       | First 120 characters of `description`, trimmed. Discard row if empty after trim  |
| `description` | `description` | Copy verbatim                                                                    |
| `date`        | `created_at`  | Parse `YYYY-MM-DD` as midnight UTC. Set `updated_at` to the same value on insert |
| —             | `origin`      | Always `"customer"` for all seed records                                         |

### Status mapping

| CSV `status` | Model `status` |
| ------------ | -------------- |
| `OPEN`       | `open`         |
| `CLOSED`     | `resolved`     |
| `DISCARDED`  | `discarded`    |

### Category mapping (HealthCore)

| CSV `category`   | Model `category`     |
| ---------------- | -------------------- |
| `APPOINTMENT`    | `patient_experience` |
| `BILLING`        | `billing_error`      |
| `CLINICAL_CARE`  | `patient_experience` |
| `ACCESSIBILITY`  | `patient_experience` |
| `ADMINISTRATIVE` | `other`              |

### Branch mapping (HealthCore)

Map CSV `clinic_id` to model `branch`. If `clinic_id` is missing or unmapped, use `central`.

| CSV `clinic_id` | Model `branch`       |
| --------------- | -------------------- |
| `US-TX-01`      | `central`            |
| `US-TX-02`      | `austin_north`       |
| `US-TX-03`      | `houston_med_center` |
| `US-FL-01`      | `miami_brickell`     |
| `US-FL-02`      | `orlando_east`       |
| `US-FL-03`      | `tampa_bay`          |
| `US-GA-01`      | `atlanta_midtown`    |
| `US-GA-02`      | `atlanta_midtown`    |
| `US-GA-03`      | `savannah`           |
| `UK-LON-01`     | `london_city`        |
| `UK-LON-02`     | `london_west`        |
| `UK-MAN-01`     | `manchester_central` |

Records that fail validation or cannot be mapped are discarded and reported to the console.

---

## Expected Values After Seeding

Once the CSV is correctly loaded, `/api/incidents/summary` must return totals by **model** `status` and `category` that match the transformed counts below. These correspond to the **94 valid records** from `incidents-healthcore.csv` in the analyzer project (invalid rows excluded).

**By model `status`:**

| Model `status` | Count |
| -------------- | ----- |
| `open`         | 28    |
| `resolved`     | 52    |
| `discarded`    | 14    |

**By model `category`:**

| Model `category`     | Count |
| -------------------- | ----- |
| `patient_experience` | 61    |
| `billing_error`      | 20    |
| `other`              | 13    |

**By model `branch`:**

| Model `branch`       | Count |
| -------------------- | ----- |
| `manchester_central` | 15    |
| `atlanta_midtown`    | 12    |
| `savannah`           | 10    |
| `austin_north`       | 9     |
| `london_west`        | 9     |
| `london_city`        | 9     |
| `miami_brickell`     | 8     |
| `tampa_bay`          | 7     |
| `central`            | 7     |
| `houston_med_center` | 4     |
| `orlando_east`       | 4     |

Cross-check these against your analyzer script output: the raw CSV breakdown uses `OPEN`/`CLOSED`/`DISCARDED` and `APPOINTMENT`/`BILLING`/etc. — the seed totals above are the **post-transformation** values your manager must produce.

---

## Implementation Notes

- **Patient data warning:** the form must display a prominent notice before the `description` field reminding the user not to enter identifying patient data. This warning is not optional — it is a compliance requirement.
- Incidents of type `compliance_breach` are the highest priority for Claire: although the automatic alert is not part of this project, design the data model so that filter is immediate to implement when needed.
- HealthCore operates in the USA and the UK. Interface labels must be in English for all clinics. If you implemented multilingual support in previous milestones, English is the mandatory base language for this project.
- The `description` field is free text and the highest-risk point for accidental patient data entry. The warning must be prominent — not small grey text that users will ignore.
