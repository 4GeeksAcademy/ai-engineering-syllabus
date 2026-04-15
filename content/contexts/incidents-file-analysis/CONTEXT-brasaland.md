# CONTEXT — Data Analysis Utility: Incident Report Processor

## Company: Brasaland

---

## Your Company

**Brasaland** is a grilled food restaurant chain with 14 locations across Colombia and Florida (USA). You are part of the **Brasaland Digital** internal team, working under the direction of **Nicolás Park (CTO)** and in close coordination with **Felipe Guerrero (Operations Director)**.

The Operations department tracks every operational incident that occurs across the chain: equipment failures, supply problems, customer complaints, food quality issues, and staff-related incidents. Until now, every location manager logged incidents in a shared spreadsheet. That spreadsheet has been exported as a CSV — your test file has **1,000 rows** representing one month of incident history across all 14 locations.

The goal of your script is to validate and summarise this data before it is used as the basis for the real-time operations dashboard that will replace the spreadsheet entirely.

---

## CSV Structure

**Filename:** `incidents.csv`  
**Encoding:** UTF-8  
**Separator:** comma (`,`)  
**Header row:** yes (row 1)

| Field                | Type    | Required | Allowed values / format                            |
| -------------------- | ------- | -------- | -------------------------------------------------- |
| `incident_id`        | string  | ✅       | Unique ID, format `BRS-XXXXXX` (e.g. `BRS-000001`) |
| `date`               | string  | ✅       | `YYYY-MM-DD`                                       |
| `location_id`        | string  | ✅       | One of: `COL-01` to `COL-10`, `FLA-01` to `FLA-04` |
| `category`           | string  | ✅       | See categories below                               |
| `description`        | string  | ✅       | Free text, min 5 characters                        |
| `status`             | string  | ✅       | `ABIERTO`, `CERRADO`, `DESCARTADO`                 |
| `customer_id`        | string  | ❌       | Optional. Format `CLI-XXXXXX`. Can be empty        |
| `satisfaction_score` | integer | ❌\*     | Integer 1–5. **Required if** `status = CERRADO`    |
| `reporter_id`        | string  | ✅       | Manager ID, format `MGR-XX`                        |

\*`satisfaction_score` is optional in the CSV structure, but a `CERRADO` record without it is considered **incomplete**.

### Valid categories

| Code               | Description                                        |
| ------------------ | -------------------------------------------------- |
| `QUEJA_CLIENTE`    | Customer complaint (service, wait time, treatment) |
| `EQUIPAMIENTO`     | Equipment failure or breakdown                     |
| `ABASTECIMIENTO`   | Supply or stock shortage                           |
| `CALIDAD_ALIMENTO` | Food quality issue                                 |
| `PERSONAL`         | Staff-related incident                             |

---

## Rules for Invalid Records

A record must be flagged as **invalid** if any of the following is true:

| Rule                                           | Description                                                  |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Missing `location_id`                          | The field is empty or not one of the 14 valid location codes |
| Missing or invalid `category`                  | The field is empty or not one of the 5 valid categories      |
| Empty `description`                            | The field is empty or has fewer than 5 characters            |
| Missing `reporter_id`                          | The field is empty                                           |
| `status = CERRADO` and no `satisfaction_score` | Closed case without a recorded score                         |
| `satisfaction_score` out of range              | Value present but not between 1 and 5 (inclusive)            |

Your script must report how many records fall into each rule type.

---

## Data Distribution (test file provided)

The `incidents-brasaland.csv` file has been sent as an attachment (ver ficheros `incidents-brasaland.csv`). The following values describe its contents and are what your script must produce exactly.

**Total rows:** 100

**Valid records: 96**
| Category | Count |
|---|---|
| `QUEJA_CLIENTE` | 29 |
| `EQUIPAMIENTO` | 17 |
| `ABASTECIMIENTO` | 22 |
| `CALIDAD_ALIMENTO` | 19 |
| `PERSONAL` | 9 |

| Status       | Count |
| ------------ | ----- |
| `ABIERTO`    | 32    |
| `CERRADO`    | 50    |
| `DESCARTADO` | 14    |

**Invalid records: 4**
| Rule triggered | Count |
|---|---|
| Missing `location_id` | 1 |
| Missing or invalid `category` | 1 |
| Empty or too-short `description` | 1 |
| `status = CERRADO` with no `satisfaction_score` | 1 |

**Satisfaction scores (50 closed records)**
| Score | Count |
|---|---|
| 1 | 4 |
| 2 | 6 |
| 3 | 12 |
| 4 | 19 |
| 5 | 9 |
Average: **3.46**

---

## Expected Output

When the student runs `python analyze.py incidents-brasaland.csv` against the provided file, the console output must show the following values:

```
============================================================
  BRASALAND — INCIDENT REPORT ANALYSIS
  Source file: incidents-brasaland.csv
============================================================

TOTAL RECORDS IN FILE .......... 100
  ├─ Valid records ................ 96
  └─ Invalid / incomplete .......... 4

INVALID RECORDS BREAKDOWN
  ├─ Missing location_id ........... 1
  ├─ Invalid or missing category ... 1
  ├─ Empty description ............. 1
  └─ Closed case, no score ......... 1

BREAKDOWN BY CATEGORY (valid records)
  ├─ QUEJA_CLIENTE ................ 29  (30.2%)
  ├─ EQUIPAMIENTO ................. 17  (17.7%)
  ├─ ABASTECIMIENTO ............... 22  (22.9%)
  ├─ CALIDAD_ALIMENTO ............. 19  (19.8%)
  └─ PERSONAL ...................... 9   (9.4%)

BREAKDOWN BY STATUS (valid records)
  ├─ ABIERTO ...................... 32  (33.3%)
  ├─ CERRADO ...................... 50  (52.1%)
  └─ DESCARTADO ................... 14  (14.6%)

SATISFACTION INDEX (closed cases)
  Scored cases: 50 of 50
  Average score: 3.46 / 5.00
  ├─ Score 1 (Very dissatisfied) ... 4
  ├─ Score 2 (Dissatisfied) ........ 6
  ├─ Score 3 (Neutral) ............ 12
  ├─ Score 4 (Satisfied) .......... 19
  └─ Score 5 (Very satisfied) ...... 9

============================================================
Export results to CSV? [y / n]:
```

> **Note:** Minor formatting differences (spacing, box-drawing characters) are acceptable, but all numeric values must match exactly.

---

## Stakeholder Note

> **From Nicolás Park (CTO):**
> _"Felipe's team is going to use this daily. Keep the console output clean and fast — they're running it from the terminal before the morning meeting. The CSV export is for Ashley — she needs to paste the results into a spreadsheet. Make sure the structure is sensible: one row per metric, with columns for_ `metric`, `value`_, and optionally_ `percentage`_."_

---

## Repository Path

```
incidents-analysis/CONTEXT-brasaland.md
```

---

_Internal document — 4Geeks Academy · AI Engineering Track_  
_For exclusive use in programme project generation_
