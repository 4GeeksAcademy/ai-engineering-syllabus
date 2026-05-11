# CONTEXT — Centralized Incident Manager · TrackFlow

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company with **130 employees**, operating in two markets: **Los Angeles (USA)** and **Zaragoza (Spain)**. Its services are warehouse management for e-commerce brands, last-mile delivery, and reverse logistics (returns and reconditioning).

As part of the **TrackFlow Tech** team, you have been building the internal platform across several milestones. This project integrates a centralized incident manager into that platform. At TrackFlow, incidents are part of daily operations: lost parcels, carrier failures, inventory discrepancies, mishandled returns. Until now, everything arrived by email or WhatsApp with no structured record.

---

## Who Uses It and Why

**Andrés Kim (CTO)** has no visibility into operational failures until someone messages him on WhatsApp. With this manager, every incident is logged, categorized, and traceable.

**Thomas Harry (CEO)** wants to know in real time how many critical incidents are open in Los Angeles vs. Zaragoza, and whether any has been unresolved for more than 24 hours.

**Carlos Vega (Head of Carrier Operations)** and **Ana Whitfield (Head of Warehouse Operations)** are the primary form users: they and their teams will report operational incidents from the warehouse floor or from carrier coordination.

**Valentina Cruz (CX Manager)** will log complaints from end customers and client companies that arrive through external channels.

---

## TrackFlow Warehouses and Offices

The `branch` field must contain exactly one of the following values:

| Database value       | Display name            |
| -------------------- | ----------------------- |
| `central`            | Central                 |
| `la_warehouse`       | Los Angeles — Warehouse |
| `la_office`          | Los Angeles — Office    |
| `zaragoza_warehouse` | Zaragoza — Warehouse    |
| `zaragoza_office`    | Zaragoza — Office       |

When the origin is `internal` or `customer` and does not correspond to a specific facility, use `central`.

---

## Incident Categories

The `category` field must contain exactly one of the following values:

| Value                   | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| `lost_parcel`           | Parcel lost in transit or in the warehouse                                      |
| `delivery_failure`      | Delivery failure: failed attempt, incorrect address, unmanaged absent recipient |
| `inventory_discrepancy` | Difference between recorded stock and physical stock                            |
| `carrier_issue`         | Issue attributable to a carrier: delay, damage, SLA breach                      |
| `returns_issue`         | Problem in the returns or reverse logistics process                             |
| `warehouse_incident`    | In-warehouse incident: goods damage, accident, equipment failure                |
| `system_failure`        | Technology system failure: WMS, carrier API integrations                        |
| `client_complaint`      | Complaint from a client company about TrackFlow's service                       |
| `other`                 | Any incident that does not fit the categories above                             |

---

## Status and Lifecycle

| Value         | Meaning at TrackFlow                                            |
| ------------- | --------------------------------------------------------------- |
| `open`        | Incident registered, pending assignment to the responsible team |
| `in_progress` | Coordinator or area manager is actively handling it             |
| `resolved`    | Resolved: parcel delivered, stock corrected, client informed    |
| `discarded`   | Registered in error, duplicate, or not actionable               |

Valid transitions: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. The `resolved` and `discarded` states are final.

---

## Origins

| Value      | When to use it at TrackFlow                                                |
| ---------- | -------------------------------------------------------------------------- |
| `customer` | Reported by a client company or end consumer                               |
| `branch`   | Detected and reported by warehouse or office staff at a TrackFlow facility |
| `internal` | Detected internally by technology, leadership, or operations               |

---

## Historical Data — Seed from CSV

The CSV file from the previous project contains incidents exported from TrackFlow's customer service system. All of them correspond to incidents reported by clients or end consumers (`origin: "customer"`).

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

- TrackFlow operates in two languages: English in Los Angeles and Spanish in Zaragoza. If you implemented bilingual support in previous milestones, the form and error messages must respect that. Branch dropdown labels should be displayed in the user's language.
- Incidents of type `lost_parcel` and `carrier_issue` have a direct impact on client SLAs: Thomas and Carlos will need to filter by them easily. Design the data model to make that filter straightforward, even though automatic alerts are not part of this project.
- The form will be used by warehouse operatives on terminals on the warehouse floor: design fields with enough size for touch use and avoid unnecessary free-text fields.
