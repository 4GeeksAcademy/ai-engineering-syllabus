# CONTEXT — Nexova · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-nexova.es.md)._

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team reporting to Sergio Molina (CTO). The inventory management system you built tracks office assets and IT equipment assigned to employees — products, inbound procurement orders, and outbound assignment orders — enforcing the rule that asset availability is never edited directly.

Patricia Solís (HR Manager) and Sergio have been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | Nexova entity name | Description                                                              |
| --------------------- | ------------------ | ------------------------------------------------------------------------ |
| `Product`             | `Asset`            | A tracked item (e.g. laptop, monitor, ergonomic chair, software licence) |
| `InboundOrder`        | `ProcurementOrder` | A purchase or delivery that increases available asset stock              |
| `OutboundOrder`       | `AssignmentOrder`  | An assignment to an employee that reduces available stock                |

Key fields to reference in your event schemas:

- `Asset`: `id`, `name`, `category` (`hardware`, `software_licence`, `furniture`, `peripheral`, `consumable`), `unit`, `current_stock`, `min_stock_threshold`, `office` (`valencia` / `miami`), `assigned_to` (nullable TinyDB user UUID — only populated when `current_stock = 0` for single-unit assets)
- `ProcurementOrder`: `id`, `asset_id`, `quantity`, `vendor`, `office`, `created_by` (TinyDB user UUID), `created_at`
- `AssignmentOrder`: `id`, `asset_id`, `quantity`, `assigned_to` (employee TinyDB UUID), `office`, `created_by`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Patricia and Laura Mendoza (CEO) need from the asset management system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                       | Definition                                                                                                       | Business decision it enables                                                                                |
| --- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | **Asset assignment lead time**            | Time elapsed between an employee's first recorded access to the assignment flow and the AssignmentOrder creation | Detect friction in the onboarding asset delivery process; identify offices with slow assignment workflows   |
| 2   | **Stock-out frequency by asset category** | Number of times an asset category hit zero available units in a period, segmented by office                      | Ensure critical hardware (laptops, licences) is never unavailable at onboarding; adjust procurement cadence |
| 3   | **Procurement cycle time**                | Average days between consecutive ProcurementOrders for the same asset                                            | Identify assets procured reactively (too late) vs. proactively; optimise reorder points                     |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event              | Trigger                                                                           | Stream or batch? (your call) |
| ---------------------------- | --------------------------------------------------------------------------------- | ---------------------------- |
| `procurement_order_created`  | A ProcurementOrder is successfully registered                                     | ?                            |
| `assignment_order_created`   | An AssignmentOrder is successfully registered                                     | ?                            |
| `stock_threshold_triggered`  | An asset's stock falls to or below `min_stock_threshold` after an assignment      | ?                            |
| `direct_stock_edit_rejected` | A request to modify asset stock directly (outside an order) is blocked by the API | ?                            |
| `assignment_order_failed`    | An AssignmentOrder is rejected (e.g. insufficient stock, missing `assigned_to`)   | ?                            |
| `procurement_order_failed`   | A ProcurementOrder is rejected (e.g. unknown vendor, invalid quantity)            | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions at Nexova.

| Candidate event             | Trigger                                                     | Section        |
| --------------------------- | ----------------------------------------------------------- | -------------- |
| `user_login_succeeded`      | Successful login by an HR operator or consultant            | Authentication |
| `user_login_failed`         | Failed login attempt (wrong credentials or expired session) | Authentication |
| `session_expired`           | User session timed out and was invalidated                  | Authentication |
| `asset_list_viewed`         | User opens the asset stock list                             | Navigation     |
| `assignment_form_abandoned` | User starts but does not complete an AssignmentOrder form   | Navigation     |
| `office_filter_applied`     | User filters asset view by Valencia or Miami                | Navigation     |

---

## Business Constraints for Your Plan

- **Dual office:** assets are managed independently per office (`valencia` / `miami`). Events must include `office` so data can be segmented by location.
- **Single-unit asset sensitivity:** for assets where `current_stock` represents a single physical unit (laptops, phones), an `AssignmentOrder` effectively removes it from available stock and links it to an employee. Your event schema for `assignment_order_created` must include both `asset_id` and `assigned_to`.
- **No PII in telemetry:** `assigned_to` and `created_by` fields must be opaque TinyDB UUIDs — never employee names or email addresses.
- **Software licence compliance risk:** `AssignmentOrder` events for `category = software_licence` are subject to vendor audit. Flag these in your schema as requiring a complete and durable audit trail; document this in your risks and exclusions section.

---

## What Your Plan Should Produce for Nexova

- `telemetry-plan.md` referencing `Asset`, `ProcurementOrder`, and `AssignmentOrder` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`procurement_order_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by Nexova's operational urgency — e.g. a laptop stock-out at onboarding day for a new consultant is immediate urgency; procurement cycle reporting is weekly.
- A risks and exclusions section that addresses the dual-office constraint, the software licence audit requirement, and any events discarded.

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
