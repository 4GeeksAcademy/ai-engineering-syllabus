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

| Database value       | Display name              |
| -------------------- | ------------------------- |
| `central`            | Central (Austin / London) |
| `austin_main`        | Austin — Main Clinic      |
| `austin_north`       | Austin — North            |
| `dallas_uptown`      | Dallas Uptown             |
| `houston_med_center` | Houston Medical Center    |
| `san_antonio_west`   | San Antonio West          |
| `miami_brickell`     | Miami Brickell            |
| `miami_doral`        | Miami Doral               |
| `orlando_east`       | Orlando East              |
| `atlanta_midtown`    | Atlanta Midtown           |
| `london_city`        | London City               |
| `london_west`        | London West End           |
| `manchester_central` | Manchester Central        |

When the origin is `internal` or `customer` and does not correspond to a specific clinic, use `central`.

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

The CSV file from the previous project contains incidents exported from HealthCore's legacy patient services system. All of them correspond to incidents reported by patients or their representatives (`origin: "customer"`). The CSV does not contain identifying patient data — it was anonymised before extraction.

**Idempotency identifier:** use the `incident_id` field from the CSV to prevent duplicate records. If that field does not exist in your CSV, use the combination `title + created_at`.

**CSV → model field mapping:**

| CSV field     | Model field   | Notes                                       |
| ------------- | ------------- | ------------------------------------------- |
| `incident_id` | —             | Used only for duplicate control, not stored |
| `title`       | `title`       |                                             |
| `description` | `description` |                                             |
| `category`    | `category`    | Verify the value is in the allowed list     |
| `status`      | `status`      | Verify the value is in the allowed list     |
| `created_at`  | `created_at`  | Preserve the original date                  |
| —             | `origin`      | Always `"customer"` for all seed records    |
| —             | `branch`      | Always `"central"` for all seed records     |

Records with a `category` or `status` value outside the allowed lists are discarded and reported to the console.

---

## Expected Values After Seeding

Once the CSV is correctly loaded, the `/api/incidents/summary` endpoint must return values consistent with the validated CSV file from the previous project. Cross-check the totals by category and status against the results from the analysis script — they must match (excluding invalid records discarded by the seed).

---

## Implementation Notes

- **Patient data warning:** the form must display a prominent notice before the `description` field reminding the user not to enter identifying patient data. This warning is not optional — it is a compliance requirement.
- Incidents of type `compliance_breach` are the highest priority for Claire: although the automatic alert is not part of this project, design the data model so that filter is immediate to implement when needed.
- HealthCore operates in the USA and the UK. Interface labels must be in English for all clinics. If you implemented multilingual support in previous milestones, English is the mandatory base language for this project.
- The `description` field is free text and the highest-risk point for accidental patient data entry. The warning must be prominent — not small grey text that users will ignore.
