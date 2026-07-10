# CONTEXT — Nexova · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-nexova.es.md)._

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team reporting to Sergio Molina (CTO). The inventory management system you built tracks office assets and IT equipment — assets, inbound entries, and outbound exits — enforcing the rule that asset availability is never edited directly.

Patricia Solís (HR Manager) and Sergio have been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | Nexova entity name | Description                                                             |
| --------------------- | ------------------ | ----------------------------------------------------------------------- |
| `Product`             | `Asset`            | A tracked item (e.g. laptop, monitor, ergonomic chair, office supplies) |
| `InboundOrder`        | `AssetEntry`       | A purchase or delivery that increases available asset stock             |
| `OutboundOrder`       | `AssetExit`        | An allocation to an employee or a consumption event that reduces stock  |

Key fields to reference in your event schemas:

- `Asset`: `id`, `name`, `sku`, `category` (`hardware`, `peripherals`, `office_supplies`, `training_materials`), `office` (`"Valencia"` / `"Miami"`), `current_stock`
- `AssetEntry`: `id`, `asset_id`, `quantity`, `supplier`, `office`, `user_uuid`, `created_at`
- `AssetExit`: `id`, `asset_id`, `quantity`, `exit_type` (`allocation` / `consumption`), `assigned_to` (nullable), `office`, `user_uuid`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Patricia and Laura Mendoza (CEO) need from the asset management system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                       | Definition                                                                                           | Business decision it enables                                                                                   |
| --- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1   | **Asset assignment lead time**            | Time elapsed between an employee's first recorded access to the exit flow and the AssetExit creation | Detect friction in the onboarding asset delivery process; identify offices with slow assignment workflows      |
| 2   | **Stock-out frequency by asset category** | Number of times an asset category hit zero available units in a period, segmented by office          | Ensure critical hardware (laptops, peripherals) is never unavailable at onboarding; adjust procurement cadence |
| 3   | **Procurement cycle time**                | Average days between consecutive AssetEntry events for the same asset                                | Identify assets procured reactively (too late) vs. proactively; optimise reorder points                        |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event              | Trigger                                                                           | Stream or batch? (your call) |
| ---------------------------- | --------------------------------------------------------------------------------- | ---------------------------- |
| `asset_entry_created`        | An AssetEntry is successfully registered                                          | ?                            |
| `asset_exit_created`         | An AssetExit is successfully registered                                           | ?                            |
| `stock_threshold_triggered`  | An asset's stock falls to or below `min_stock_threshold` after an exit            | ?                            |
| `direct_stock_edit_rejected` | A request to modify asset stock directly (outside an order) is blocked by the API | ?                            |
| `asset_exit_failed`          | An AssetExit is rejected (e.g. insufficient stock, validation error)              | ?                            |
| `asset_entry_failed`         | An AssetEntry is rejected (e.g. unknown supplier, invalid quantity)               | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions at Nexova.

| Candidate event             | Trigger                                                     | Section        |
| --------------------------- | ----------------------------------------------------------- | -------------- |
| `user_login_succeeded`      | Successful login by an HR operator or consultant            | Authentication |
| `user_login_failed`         | Failed login attempt (wrong credentials or expired session) | Authentication |
| `session_expired`           | User session timed out and was invalidated                  | Authentication |
| `asset_list_viewed`         | User opens the asset stock list                             | Navigation     |
| `assignment_form_abandoned` | User starts but does not complete an AssetExit form         | Navigation     |
| `office_filter_applied`     | User filters asset view by Valencia or Miami                | Navigation     |

---

## Business Constraints for Your Plan

- **Dual office:** assets are managed independently per office (`"Valencia"` / `"Miami"`). Events must include `office` so data can be segmented by location.
- **Exit type sensitivity:** `AssetExit` events with `exit_type = allocation` link stock to an employee in business data — telemetry tracks the action with `exit_type` only, never employee names.
- **No PII in telemetry:** `user_uuid` fields must be opaque TinyDB UUIDs — never employee names or email addresses.
- **Hardware audit risk:** AssetExit events for `category = hardware` may be subject to vendor audit. Flag these in your schema as requiring a complete audit trail; document this in your risks and exclusions section.

---

## What Your Plan Should Produce for Nexova

- `telemetry-plan.md` referencing `Asset`, `AssetEntry`, and `AssetExit` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`asset_entry_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by Nexova's operational urgency — e.g. a laptop stock-out at onboarding day for a new consultant is immediate urgency; procurement cycle reporting is weekly.
- A risks and exclusions section that addresses the dual-office constraint, hardware audit requirements, and any events discarded.

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
