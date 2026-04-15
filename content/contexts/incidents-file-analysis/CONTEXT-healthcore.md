# CONTEXT — Data Analysis Utility: Incident Report Processor

## Company: HealthCore

---

## Your Company

**HealthCore** is an outpatient healthcare company operating 12 clinics across the United States (Texas, Florida, and Georgia) and the United Kingdom (London and Manchester). You are part of the **HealthCore Digital** internal team, working under the direction of **James Osei (CTO)**.

Your point of contact for this project is **Priya Nair (Head of Patient Experience)**. Her team of patient coordinators logs every patient-reported incident across the network: appointment problems, billing disputes, clinical care concerns, accessibility barriers, and administrative issues.

Until now, incident reports have been collected in different formats depending on the clinic and entered manually into a shared spreadsheet. That spreadsheet has been exported as a CSV — your test file has **1,000 rows** covering one month of incident history across all 12 locations.

This data **cannot be sent to any external AI tool.** It contains patient identifiers protected under **HIPAA** (US clinics) and **UK GDPR** (UK clinics). Any script that processes this file must handle patient data with zero exposure — no patient ID, no personal detail may appear in any output, log, or export.

The goal of your script is to give Priya a reliable, accurate summary of the incident data. If the script works correctly on the 1,000-record sample, it will be run on the full historical archive before being integrated into the patient experience dashboard.

---

## CSV Structure

**Filename:** `incidents.csv`  
**Encoding:** UTF-8  
**Separator:** comma (`,`)  
**Header row:** yes (row 1)

| Field                | Type    | Required | Allowed values / format                                   |
| -------------------- | ------- | -------- | --------------------------------------------------------- |
| `incident_id`        | string  | ✅       | Unique ID, format `HC-XXXXXX` (e.g. `HC-000001`)          |
| `date`               | string  | ✅       | `YYYY-MM-DD`                                              |
| `clinic_id`          | string  | ✅       | One of the 12 valid clinic codes (see below)              |
| `country`            | string  | ✅       | `US` or `UK` — must match the clinic's country            |
| `category`           | string  | ✅       | See categories below                                      |
| `description`        | string  | ✅       | Free text, min 5 characters                               |
| `status`             | string  | ✅       | `OPEN`, `CLOSED`, `DISCARDED`                             |
| `patient_id`         | string  | ✅       | Format `PAT-XXXXXX` — **protected under HIPAA / UK GDPR** |
| `satisfaction_score` | integer | ❌\*     | Integer 1–5. **Required if** `status = CLOSED`            |

\*`satisfaction_score` is optional in the CSV structure, but a `CLOSED` record without it is considered **incomplete**.

> ⚠️ The `patient_id` field is protected health information (PHI) under HIPAA in the US and personal data under UK GDPR in the UK. **Your script must never print, log, or export any `patient_id` value in any output** — not even in error messages. If a record has an invalid `patient_id`, report the rule violation only (e.g. "Missing patient_id: 7 records"), never the value itself.

### Valid clinic codes

| Code        | Country | Location               |
| ----------- | ------- | ---------------------- |
| `US-TX-01`  | US      | Austin, TX — Main      |
| `US-TX-02`  | US      | Austin, TX — North     |
| `US-TX-03`  | US      | Houston, TX            |
| `US-FL-01`  | US      | Miami, FL              |
| `US-FL-02`  | US      | Orlando, FL            |
| `US-FL-03`  | US      | Tampa, FL              |
| `US-GA-01`  | US      | Atlanta, GA — Midtown  |
| `US-GA-02`  | US      | Atlanta, GA — Buckhead |
| `US-GA-03`  | US      | Savannah, GA           |
| `UK-LON-01` | UK      | London — Canary Wharf  |
| `UK-LON-02` | UK      | London — Kensington    |
| `UK-MAN-01` | UK      | Manchester             |

A record is **invalid** if the `country` field does not match the country of the declared `clinic_id`.

### Valid categories

| Code             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `APPOINTMENT`    | Scheduling problem, excessive wait time, cancellation, no-show handling |
| `BILLING`        | Billing dispute, insurance confusion, unexpected charge                 |
| `CLINICAL_CARE`  | Patient concern about care quality, diagnosis, or treatment             |
| `ACCESSIBILITY`  | Language barrier, physical access, communication difficulty             |
| `ADMINISTRATIVE` | Records request, referral delay, paperwork error                        |

---

## Rules for Invalid Records

A record must be flagged as **invalid** if any of the following is true:

| Rule                                          | Description                                                            |
| --------------------------------------------- | ---------------------------------------------------------------------- |
| Missing or invalid `clinic_id`                | Empty or not one of the 12 valid clinic codes                          |
| Country/clinic mismatch                       | `country` field does not match the country of the declared `clinic_id` |
| Missing or invalid `category`                 | Empty or not one of the 5 valid categories                             |
| Empty `description`                           | Empty or fewer than 5 characters                                       |
| Missing `patient_id`                          | Empty or does not match format `PAT-XXXXXX`                            |
| `status = CLOSED` and no `satisfaction_score` | Closed incident without a recorded score                               |
| `satisfaction_score` out of range             | Value present but not between 1 and 5 (inclusive)                      |

Your script must report how many records fall into each rule type — **without exposing any patient data**.

---

## Data Distribution (test file provided)

The `incidents-healthcore.csv` file has been sent as an attachment (ver ficheros `incidents-healthcore.csv`). The following values describe its contents and are what your script must produce exactly.

**Total rows:** 100

**Valid records: 94**
| Category | Count |
|---|---|
| `APPOINTMENT` | 30 |
| `BILLING` | 20 |
| `CLINICAL_CARE` | 14 |
| `ACCESSIBILITY` | 17 |
| `ADMINISTRATIVE` | 13 |

| Status      | Count |
| ----------- | ----- |
| `OPEN`      | 28    |
| `CLOSED`    | 52    |
| `DISCARDED` | 14    |

| Country | Count |
| ------- | ----- |
| `US`    | 61    |
| `UK`    | 33    |

**Invalid records: 6**
| Rule triggered | Count |
|---|---|
| Missing or invalid `clinic_id` | 1 |
| Country/clinic mismatch | 1 |
| Missing or invalid `category` | 1 |
| Empty or too-short `description` | 1 |
| Missing `patient_id` | 1 |
| `status = CLOSED` with no `satisfaction_score` | 1 |

**Satisfaction scores (52 closed records)**
| Score | Count |
|---|---|
| 1 | 3 |
| 2 | 5 |
| 3 | 12 |
| 4 | 23 |
| 5 | 9 |
Average: **3.58**

---

## Expected Output

When the student runs `python analyze.py incidents-healthcore.csv` against the provided file, the console output must show the following values:

```
============================================================
  HEALTHCORE — PATIENT INCIDENT REPORT ANALYSIS
  Source file: incidents-healthcore.csv
============================================================

TOTAL RECORDS IN FILE .......... 100
  ├─ Valid records ................ 94
  └─ Invalid / incomplete .......... 6

INVALID RECORDS BREAKDOWN
  ├─ Invalid or missing clinic_id .. 1
  ├─ Country/clinic mismatch ....... 1
  ├─ Invalid or missing category ... 1
  ├─ Empty description ............. 1
  ├─ Missing patient_id ............ 1
  └─ Closed case, no score ......... 1

BREAKDOWN BY CATEGORY (valid records)
  ├─ APPOINTMENT .................. 30  (31.9%)
  ├─ BILLING ...................... 20  (21.3%)
  ├─ CLINICAL_CARE ................ 14  (14.9%)
  ├─ ACCESSIBILITY ................ 17  (18.1%)
  └─ ADMINISTRATIVE ............... 13  (13.8%)

BREAKDOWN BY STATUS (valid records)
  ├─ OPEN ......................... 28  (29.8%)
  ├─ CLOSED ....................... 52  (55.3%)
  └─ DISCARDED .................... 14  (14.9%)

BREAKDOWN BY COUNTRY (valid records)
  ├─ US ........................... 61  (64.9%)
  └─ UK ........................... 33  (35.1%)

SATISFACTION INDEX (closed cases)
  Scored cases: 52 of 52
  Average score: 3.58 / 5.00
  ├─ Score 1 (Very dissatisfied) ... 3
  ├─ Score 2 (Dissatisfied) ........ 5
  ├─ Score 3 (Neutral) ............ 12
  ├─ Score 4 (Satisfied) .......... 23
  └─ Score 5 (Very satisfied) ...... 9

============================================================
Export results to CSV? [y / n]:
```

> **Note:** Minor formatting differences (spacing, box-drawing characters) are acceptable, but all numeric values must match exactly. The country breakdown is specific to HealthCore — include it even though it is not required in the generic README.

---

## Stakeholder Note

> **From Priya Nair (Head of Patient Experience):**
> _"The ACCESSIBILITY category is particularly important to me — if those numbers are high in the Florida clinics, I need to escalate to Sandra today, not next week. Make sure the country breakdown is visible in the console output. And I want to be explicit: no patient identifier of any kind may appear anywhere in your output. James already flagged it with Claire — this is a compliance requirement, not a preference. If your script prints a_ `patient_id` _for any reason, the output cannot be used."_

> **From James Osei (CTO):**
> _"The CSV export should be consistent and simple: one row per metric, with columns for_ `metric`, `value`_, and optionally_ `percentage`_. Tom's billing team will use it directly in their reporting spreadsheet. Add a_ `by_country` _section in the console output specific to HealthCore."_

---

## Repository Path

```
incidents-analysis/CONTEXT-healthcore.md
```

---

_Internal document — 4Geeks Academy · AI Engineering Track_  
_For exclusive use in programme project generation_
