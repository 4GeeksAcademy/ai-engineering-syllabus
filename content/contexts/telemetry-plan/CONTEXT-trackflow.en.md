# CONTEXT — TrackFlow · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-trackflow.es.md)._

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (US) and Zaragoza (Spain). You are part of **TrackFlow Tech**, the internal technology team led by Andrés Kim (CTO). The inventory management system you built tracks warehouse SKU stock across both locations — SKUs, inbound stock entries, and outbound stock exits — enforcing the rule that stock levels are never edited directly.

Ana Whitfield (Head of Warehouse Operations) and Thomas Harry (CEO) have been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | TrackFlow entity name | Description                                                        |
| --------------------- | --------------------- | ------------------------------------------------------------------ |
| `Product`             | `SKU`                 | A tracked stock-keeping unit stored in one or both warehouses      |
| `InboundOrder`        | `StockEntry`          | A client shipment arriving at a warehouse that increases SKU stock |
| `OutboundOrder`       | `StockExit`           | A customer dispatch or confirmed loss that reduces SKU stock       |

Key fields to reference in your event schemas:

- `SKU`: `id`, `sku`, `name`, `client_name`, `category` (`fashion`, `electronics`, `cosmetics`), `warehouse` (`"LA"` / `"ZGZ"`), `current_stock`
- `StockEntry`: `id`, `sku_id`, `quantity`, `reference`, `warehouse`, `user_uuid`, `created_at`
- `StockExit`: `id`, `sku_id`, `quantity`, `exit_type` (`dispatch` / `loss`), `tracking_number` (nullable), `warehouse`, `user_uuid`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Ana and Thomas need from the warehouse inventory system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                  | Definition                                                                                             | Business decision it enables                                                                         |
| --- | ------------------------------------ | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| 1   | **Order fulfilment rate**            | Proportion of StockExit dispatches completed successfully vs. those rejected due to insufficient stock | Detect which SKUs or warehouses have chronic availability issues; flag clients at risk of SLA breach |
| 2   | **Stock discrepancy frequency**      | Number of direct stock edit attempts rejected by the API per warehouse per day                         | Identify warehouses where operatives attempt manual workarounds; trigger process audit               |
| 3   | **Receiving-to-dispatch cycle time** | Average time between a StockEntry and the first StockExit drawing from the same SKU batch              | Measure warehouse processing speed per location; identify bottlenecks before they impact clients     |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event              | Trigger                                                                         | Stream or batch? (your call) |
| ---------------------------- | ------------------------------------------------------------------------------- | ---------------------------- |
| `stock_entry_created`        | A StockEntry is successfully registered                                         | ?                            |
| `stock_exit_created`         | A StockExit is successfully registered                                          | ?                            |
| `stock_threshold_triggered`  | A SKU's stock falls to or below `min_stock_threshold` after an exit             | ?                            |
| `direct_stock_edit_rejected` | A request to modify SKU stock directly (outside an order) is blocked by the API | ?                            |
| `stock_exit_failed`          | A StockExit is rejected (e.g. insufficient stock, unknown SKU)                  | ?                            |
| `stock_entry_failed`         | A StockEntry is rejected (e.g. invalid reference, invalid quantity)             | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions at TrackFlow.

| Candidate event            | Trigger                                                     | Section        |
| -------------------------- | ----------------------------------------------------------- | -------------- |
| `user_login_succeeded`     | Successful login by a warehouse operative or coordinator    | Authentication |
| `user_login_failed`        | Failed login attempt (wrong credentials or expired session) | Authentication |
| `session_expired`          | User session timed out and was invalidated                  | Authentication |
| `sku_list_viewed`          | User opens the SKU stock list for a warehouse               | Navigation     |
| `dispatch_form_abandoned`  | User starts but does not complete a StockExit form          | Navigation     |
| `warehouse_filter_applied` | User switches the view between Los Angeles and Zaragoza     | Navigation     |

---

## Business Constraints for Your Plan

- **Dual warehouse:** every event originating from a warehouse operation must include `warehouse` (`"LA"` / `"ZGZ"`) so data can be segmented by country. Thomas Harry will not accept a dashboard that mixes both warehouses without a clear split.
- **Client data isolation:** TrackFlow handles inventory for multiple client brands. Events must use `reference` and SKU identifiers — never brand names in free-text telemetry fields — to prevent accidental data leakage between client accounts.
- **No PII in telemetry:** `user_uuid` fields must be opaque TinyDB UUIDs — never operative names or email addresses.
- **SLA sensitivity:** StockExit failures with `exit_type = dispatch` during peak hours (Black Friday, Q4) have contractual SLA implications. Flag `stock_exit_failed` events in your schema as requiring immediate stream processing; document the rationale in your stream/batch section.

---

## What Your Plan Should Produce for TrackFlow

- `telemetry-plan.md` referencing `SKU`, `StockEntry`, and `StockExit` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`stock_entry_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by TrackFlow's operational urgency — e.g. a stock-out for a high-volume fashion client in Los Angeles is immediate; a weekly receiving cycle report is not.
- A risks and exclusions section that addresses the dual-warehouse constraint, client data isolation, and any events discarded.

---

_TrackFlow Tech — Internal document for 4Geeks Academy AI Engineering Track_
