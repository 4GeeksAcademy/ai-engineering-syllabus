# CONTEXT — Centralized Incident Manager · Brasaland

## Your Company

**Brasaland** is a grilled food restaurant chain with **14 locations** operating in Colombia and Florida (USA). You employ approximately 115 people across kitchen and floor staff, operations supervisors, and the corporate team headquartered in Medellín, with a commercial office in Miami.

As part of the **Brasaland Digital** team, you have been building the company's internal platform across several milestones. This project integrates a centralized incident manager into that platform, so any location can report operational, customer-related, or internal issues — and the operations team can track them from a single panel.

---

## Who Uses It and Why

**Felipe Guerrero (Operations Director)** needs visibility into what is happening at each location without having to call each manager. Today he receives reports via WhatsApp or at the end of the week. With this manager, every incident is logged immediately, categorized, and assigned to a branch.

**Mariana Restrepo (CEO)** wants to see on the executive dashboard how many incidents are open this week, of what type, and at which locations. That visibility does not exist yet.

The form will be used by **location managers** (from a tablet in the kitchen or floor) and the **headquarters team** (from a desktop in Medellín or Miami).

---

## Brasaland Branches

The `branch` field must contain exactly one of the following values:

| Database value          | Display name                |
| ----------------------- | --------------------------- |
| `central`               | Central (Medellín / Miami)  |
| `medellin_centro`       | Medellín Centro             |
| `medellin_laureles`     | Medellín Laureles           |
| `medellin_envigado`     | Medellín Envigado           |
| `medellin_bello`        | Medellín Bello              |
| `medellin_itagui`       | Medellín Itagüí             |
| `bogota_chapinero`      | Bogotá Chapinero            |
| `bogota_usaquen`        | Bogotá Usaquén              |
| `cali_granada`          | Cali Granada                |
| `barranquilla_norte`    | Barranquilla Norte          |
| `miami_doral`           | Miami Doral                 |
| `miami_hialeah`         | Miami Hialeah               |
| `miami_kendall`         | Miami Kendall               |
| `orlando_international` | Orlando International Drive |
| `fort_lauderdale`       | Fort Lauderdale             |

When the origin is `internal` or `customer` and does not correspond to a specific location, use `central`.

---

## Incident Categories

The `category` field must contain exactly one of the following values:

| Value                | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `equipment_failure`  | Kitchen or floor equipment failure (oven, fryer, cold storage, POS terminal) |
| `supply_issue`       | Supply problem: out-of-stock ingredient, poor quality, incorrect delivery    |
| `customer_complaint` | Customer complaint or claim: product, service, wait time, experience         |
| `staff_issue`        | Staff-related incident: absence, conflict, minor workplace accident          |
| `facility_issue`     | Facility problem: water, electricity, HVAC, cleaning                         |
| `pos_system`         | POS or cash register system error                                            |
| `delivery_issue`     | Problem with delivery orders or delivery platform                            |
| `other`              | Any incident that does not fit the categories above                          |

---

## Status and Lifecycle

| Value         | Meaning at Brasaland                                        |
| ------------- | ----------------------------------------------------------- |
| `open`        | Newly registered incident, pending assignment               |
| `in_progress` | Operations team or location manager is actively handling it |
| `resolved`    | Incident closed with confirmed resolution                   |
| `discarded`   | Registered in error or duplicate — no action required       |

Valid transitions: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. The `resolved` and `discarded` states are final.

---

## Origins

| Value      | When to use it at Brasaland                                                        |
| ---------- | ---------------------------------------------------------------------------------- |
| `customer` | Complaint or incident communicated by a customer (in-location, via app, via email) |
| `branch`   | Reported by the manager or staff of a specific location                            |
| `internal` | Detected by the corporate team (operations, technology, HR)                        |

---

## Historical Data — Seed from CSV

The CSV file from the previous project contains incidents exported from the legacy customer service system. All of them originate from customers (`origin: "customer"`).

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

- The form will be used by location managers on touch devices in the kitchen or floor: fields must be large enough for touch use, and the branch dropdown must display the readable name (`Medellín Centro`), not the internal value (`medellin_centro`).
- Error messages must be in the base language chosen for the application. If you implemented bilingual support in previous milestones, maintain that logic here.
- Incidents of type `customer_complaint` with status `open` for more than 48 hours are a priority for Felipe — although the automatic alert is not part of this project, design the data model with that filter in mind so it is easy to add later.
