# CONTEXT — TrackFlow · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-trackflow.es.md)._

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (US) and Zaragoza (Spain). You are part of **TrackFlow Tech**, the internal technology team led by Andrés Kim (CTO). The inventory management system you built tracks warehouse SKU stock across both locations — products, inbound receiving orders, and outbound dispatch orders — enforcing the rule that stock levels are never edited directly.

Ana Whitfield (Head of Warehouse Operations) and Thomas Harry (CEO) have been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | TrackFlow entity name | Description                                                        |
| --------------------- | --------------------- | ------------------------------------------------------------------ |
| `Product`             | `SKU`                 | A tracked stock-keeping unit stored in one or both warehouses      |
| `InboundOrder`        | `ReceivingOrder`      | A client shipment arriving at a warehouse that increases SKU stock |
| `OutboundOrder`       | `DispatchOrder`       | A customer delivery picked from stock that reduces SKU stock       |

Key fields to reference in your event schemas:

- `SKU`: `id`, `sku_code`, `name`, `category` (`fashion`, `electronics`, `cosmetics`, `home`, `other`), `unit`, `current_stock`, `min_stock_threshold`, `warehouse` (`los_angeles` / `zaragoza`), `client_id`
- `ReceivingOrder`: `id`, `sku_id`, `quantity`, `client_id`, `warehouse`, `carrier`, `created_by` (TinyDB user UUID), `created_at`
- `DispatchOrder`: `id`, `sku_id`, `quantity`, `client_id`, `destination_country`, `carrier`, `warehouse`, `created_by`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Ana and Thomas need from the warehouse inventory system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                  | Definition                                                                                        | Business decision it enables                                                                         |
| --- | ------------------------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1   | **Order fulfilment rate**            | Proportion of DispatchOrders completed successfully vs. those rejected due to insufficient stock  | Detect which SKUs or warehouses have chronic availability issues; flag clients at risk of SLA breach |
| 2   | **Stock discrepancy frequency**      | Number of direct stock edit attempts rejected by the API per warehouse per day                    | Identify warehouses where operatives attempt manual workarounds; trigger process audit               |
| 3   | **Receiving-to-dispatch cycle time** | Average time between a ReceivingOrder and the first DispatchOrder drawing from the same SKU batch | Measure warehouse processing speed per location; identify bottlenecks before they impact clients     |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event              | Trigger                                                                         | Stream or batch? (your call) |
| ---------------------------- | ------------------------------------------------------------------------------- | ---------------------------- |
| `receiving_order_created`    | A ReceivingOrder is successfully registered                                     | ?                            |
| `dispatch_order_created`     | A DispatchOrder is successfully registered                                      | ?                            |
| `stock_threshold_triggered`  | A SKU's stock falls to or below `min_stock_threshold` after a dispatch          | ?                            |
| `direct_stock_edit_rejected` | A request to modify SKU stock directly (outside an order) is blocked by the API | ?                            |
| `dispatch_order_failed`      | A DispatchOrder is rejected (e.g. insufficient stock, unknown SKU)              | ?                            |
| `receiving_order_failed`     | A ReceivingOrder is rejected (e.g. unknown client, invalid quantity)            | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions at TrackFlow.

| Candidate event            | Trigger                                                     | Section        |
| -------------------------- | ----------------------------------------------------------- | -------------- |
| `user_login_succeeded`     | Successful login by a warehouse operative or coordinator    | Authentication |
| `user_login_failed`        | Failed login attempt (wrong credentials or expired session) | Authentication |
| `session_expired`          | User session timed out and was invalidated                  | Authentication |
| `sku_list_viewed`          | User opens the SKU stock list for a warehouse               | Navigation     |
| `dispatch_form_abandoned`  | User starts but does not complete a DispatchOrder form      | Navigation     |
| `warehouse_filter_applied` | User switches the view between Los Angeles and Zaragoza     | Navigation     |

---

## Business Constraints for Your Plan

- **Dual warehouse:** every event originating from a warehouse operation must include `warehouse` (`los_angeles` / `zaragoza`) so data can be segmented by country. Thomas Harry will not accept a dashboard that mixes both warehouses without a clear split.
- **Client data isolation:** TrackFlow handles inventory for multiple client brands. Events that include `client_id` must use opaque identifiers — never brand names — to prevent accidental data leakage between client accounts.
- **No PII in telemetry:** `created_by` fields must be opaque TinyDB UUIDs — never operative names or email addresses.
- **SLA sensitivity:** DispatchOrder failures for `destination_country = US` during peak hours (Black Friday, Q4) have contractual SLA implications. Flag `dispatch_order_failed` events in your schema as requiring immediate stream processing; document the rationale in your stream/batch section.

---

## What Your Plan Should Produce for TrackFlow

- `telemetry-plan.md` referencing `SKU`, `ReceivingOrder`, and `DispatchOrder` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`receiving_order_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by TrackFlow's operational urgency — e.g. a stock-out for a high-volume fashion client in Los Angeles is immediate; a weekly receiving cycle report is not.
- A risks and exclusions section that addresses the dual-warehouse constraint, client data isolation, and any events discarded.

---

_TrackFlow Tech — Internal document for 4Geeks Academy AI Engineering Track_
