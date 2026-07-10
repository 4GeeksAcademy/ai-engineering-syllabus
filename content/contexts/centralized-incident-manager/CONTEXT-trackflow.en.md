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

The CSV file from the **incidents-file-analyzer** project (`incidents-trackflow.csv` in `content/contexts/incidents-file-analysis/`) contains incidents exported from TrackFlow's customer service system. All of them correspond to incidents reported by clients or end consumers (`origin: "customer"`).

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

### Category mapping (TrackFlow)

| CSV `category`     | Model `category`   |
| ------------------ | ------------------ |
| `LOST_PARCEL`      | `lost_parcel`      |
| `DELAYED_DELIVERY` | `carrier_issue`    |
| `WRONG_ADDRESS`    | `delivery_failure` |
| `RETURN_REQUEST`   | `returns_issue`    |
| `DAMAGE`           | `carrier_issue`    |

### Branch mapping (TrackFlow)

Map CSV `country` to model `branch` for seed records:

| CSV `country` | Model `branch`    |
| ------------- | ----------------- |
| `US`          | `la_office`       |
| `ES`          | `zaragoza_office` |

Records that fail validation or cannot be mapped are discarded and reported to the console.

---

## Expected Values After Seeding

Once the CSV is correctly loaded, `/api/incidents/summary` must return totals by **model** `status` and `category` that match the transformed counts below. These correspond to the **95 valid records** from `incidents-trackflow.csv` in the analyzer project (invalid rows excluded).

**By model `status`:**

| Model `status` | Count |
| -------------- | ----- |
| `open`         | 29    |
| `resolved`     | 52    |
| `discarded`    | 14    |

**By model `category`:**

| Model `category`   | Count |
| ------------------ | ----- |
| `lost_parcel`      | 14    |
| `carrier_issue`    | 45    |
| `delivery_failure` | 19    |
| `returns_issue`    | 17    |

Cross-check these against your analyzer script output: the raw CSV breakdown uses `OPEN`/`CLOSED`/`DISCARDED` and `LOST_PARCEL`/`DELAYED_DELIVERY`/etc. — the seed totals above are the **post-transformation** values your manager must produce.

---

## Implementation Notes

- TrackFlow operates in two languages: English in Los Angeles and Spanish in Zaragoza. If you implemented bilingual support in previous milestones, the form and error messages must respect that. Branch dropdown labels should be displayed in the user's language.
- Incidents of type `lost_parcel` and `carrier_issue` have a direct impact on client SLAs: Thomas and Carlos will need to filter by them easily. Design the data model to make that filter straightforward, even though automatic alerts are not part of this project.
- The form will be used by warehouse operatives on terminals on the warehouse floor: design fields with enough size for touch use and avoid unnecessary free-text fields.
