# CONTEXT — Centralized Incident Manager · Nexova

## Your Company

**Nexova** is a human resources consulting and talent acquisition firm with **120 employees**, headquartered in Valencia, Spain, with an expansion office in Miami, Florida. It operates across three business lines: executive and mid-management headhunting, customer support team outsourcing for technology companies, and corporate training in soft skills and leadership.

As part of the **Nexova AI Engineering** team, you have been building the internal platform across several milestones. This project integrates a centralized incident manager into that platform. At Nexova, incidents are not just infrastructure failures: they also include complaints from corporate clients, errors in selection processes, and issues from the outsourced support team.

---

## Who Uses It and Why

**Sergio Molina (CTO)** needs centralized visibility into all technical and operational issues that currently arrive by email, Slack, or word of mouth. Without a structured record, he cannot measure or improve resolution times.

**Roberto Díaz (Customer Support Lead)** manages 30 agents handling incidents for Nexova's clients. They currently work with a legacy helpdesk and no centralized knowledge base. This manager is the first step toward a structured system.

**Laura Mendoza (CEO)** wants to know how many critical incidents are open right now, from which office they originate, and how long they have been unresolved.

---

## Nexova Offices

The `branch` field must contain exactly one of the following values:

| Database value        | Display name             |
| --------------------- | ------------------------ |
| `central`             | Central — Valencia HQ    |
| `valencia_operations` | Valencia — Operations    |
| `miami_office`        | Miami Office             |
| `remote`              | Remote (no fixed office) |

Use `central` when the incident has no specific office — for example, `internal` leadership reports or `customer` complaints with no associated office. `central` is Nexova's headquarters in Valencia; do not use a separate headquarters value.

---

## Incident Categories

The `category` field must contain exactly one of the following values:

| Value               | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| `technical_failure` | System or technology tool failure (ATS, HubSpot, Zendesk, infrastructure) |
| `process_error`     | Error in an operational process: selection, onboarding, training, billing |
| `client_complaint`  | Complaint or claim from a corporate client about the service provided     |
| `candidate_issue`   | Issue reported by or related to a candidate in a selection process        |
| `staff_issue`       | Internal HR incident: absence, conflict, accident, sick leave             |
| `sla_breach`        | Breach of a committed SLA with a client                                   |
| `data_quality`      | Error or inconsistency in candidate, client, or reporting data            |
| `other`             | Any incident that does not fit the categories above                       |

---

## Status and Lifecycle

| Value         | Meaning at Nexova                                                |
| ------------- | ---------------------------------------------------------------- |
| `open`        | Incident registered, no owner assigned yet                       |
| `in_progress` | Assigned to a team or person, actively being handled             |
| `resolved`    | Resolved and confirmed by the reporter or the responsible person |
| `discarded`   | Registered in error, duplicate, or out of scope                  |

Valid transitions: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. The `resolved` and `discarded` states are final.

---

## Origins

| Value      | When to use it at Nexova                                                    |
| ---------- | --------------------------------------------------------------------------- |
| `customer` | Reported by a corporate client (a company that contracts Nexova's services) |
| `branch`   | Reported by staff at one of Nexova's offices                                |
| `internal` | Detected internally by technology, operations, or leadership                |

---

## Historical Data — Seed from CSV

The CSV file from the **incidents-file-analyzer** project (`incidents-nexova.csv` in `content/contexts/incidents-file-analysis/`) contains incidents exported from the customer support helpdesk. All of them correspond to complaints or issues reported by corporate clients (`origin: "customer"`).

The analyzer CSV schema uses different field names, status values, and category codes than this manager. **Do not insert CSV rows directly.** Reuse the shared validation logic from the analyzer, then apply the transformations below before insert.

**Idempotency identifier:** use `ticket_id` from the CSV to prevent duplicate records. If that field does not exist, use the combination `title + created_at`.

### Direct field mapping

| CSV field     | Model field   | Transformation                                                                   |
| ------------- | ------------- | -------------------------------------------------------------------------------- |
| `ticket_id`   | —             | Duplicate control only — not stored                                              |
| `description` | `title`       | First 120 characters of `description`, trimmed. Discard row if empty after trim  |
| `description` | `description` | Copy verbatim                                                                    |
| `date`        | `created_at`  | Parse `YYYY-MM-DD` as midnight UTC. Set `updated_at` to the same value on insert |
| —             | `origin`      | Always `"customer"` for all seed records                                         |
| —             | `branch`      | Always `"central"` for all seed records (CSV has no office field)                |

### Status mapping

| CSV `status` | Model `status` |
| ------------ | -------------- |
| `OPEN`       | `open`         |
| `CLOSED`     | `resolved`     |
| `DISCARDED`  | `discarded`    |

### Category mapping (Nexova)

| CSV `category` | Model `category`    |
| -------------- | ------------------- |
| `TECHNICAL`    | `technical_failure` |
| `BILLING`      | `process_error`     |
| `ACCESS`       | `technical_failure` |
| `HR_QUERY`     | `process_error`     |
| `COMPLAINT`    | `client_complaint`  |

Records that fail validation or cannot be mapped are discarded and reported to the console.

---

## Expected Values After Seeding

Once the CSV is correctly loaded, `/api/incidents/summary` must return totals by **model** `status` and `category` that match the transformed counts below. These correspond to the **96 valid records** from `incidents-nexova.csv` in the analyzer project (invalid rows excluded).

**By model `status`:**

| Model `status` | Count |
| -------------- | ----- |
| `open`         | 27    |
| `resolved`     | 56    |
| `discarded`    | 13    |

**By model `category`:**

| Model `category`    | Count |
| ------------------- | ----- |
| `technical_failure` | 49    |
| `process_error`     | 35    |
| `client_complaint`  | 12    |

Cross-check these against your analyzer script output: the raw CSV breakdown uses `OPEN`/`CLOSED`/`DISCARDED` and `TECHNICAL`/`BILLING`/etc. — the seed totals above are the **post-transformation** values your manager must produce.

---

## Implementation Notes

- Nexova operates in two languages: Valencia staff work in Spanish and Miami staff in English. If you implemented bilingual support in previous milestones, the form and error messages must respect that here too.
- Incidents of type `sla_breach` are critical for Roberto and Laura: although the automatic alert is not part of this project, design the data model so that filter is trivial to add later.
- The `remote` value in `branch` is common at Nexova — many employees have no fixed office. Make sure it appears clearly in the dropdown and does not create ambiguity with `central` (headquarters) or `valencia_operations` (operations office).
