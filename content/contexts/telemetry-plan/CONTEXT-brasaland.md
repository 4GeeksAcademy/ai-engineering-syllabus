# CONTEXT — Brasaland · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-brasaland.es.md)._

## Your Company

**Brasaland** is a grilled food restaurant chain with 14 locations across Colombia and Florida. You are part of **Brasaland Digital**, the internal technology team led by Nicolás Park (CTO). The inventory management system you built tracks ingredient stock across all locations — products, inbound supply orders, and outbound consumption orders — enforcing the rule that stock levels are never edited directly.

The operations team (Felipe Guerrero, Operations Director) has been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | Brasaland entity name | Description                                                     |
| --------------------- | --------------------- | --------------------------------------------------------------- |
| `Product`             | `Ingredient`          | A tracked ingredient (e.g. beef cut, sauce, packaging material) |
| `InboundOrder`        | `SupplyOrder`         | A supplier delivery that increases ingredient stock             |
| `OutboundOrder`       | `ConsumptionOrder`    | A kitchen consumption record that reduces ingredient stock      |

Key fields to reference in your event schemas:

- `Ingredient`: `id`, `name`, `category` (`meat`, `produce`, `sauce`, `beverage`, `packaging`, `cleaning`), `unit`, `current_stock`, `min_stock_threshold`, `location_id`, `currency` (`COP` / `USD`)
- `SupplyOrder`: `id`, `ingredient_id`, `quantity`, `supplier_id`, `location_id`, `created_by` (TinyDB user UUID), `created_at`
- `ConsumptionOrder`: `id`, `ingredient_id`, `quantity`, `reason` (`kitchen_use`, `waste`, `spoilage`, `theft`), `location_id`, `created_by`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Felipe and Mariana (CEO) need from the inventory system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                                   | Definition                                                                                     | Business decision it enables                                                   |
| --- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1   | **Daily consumption rate by ingredient and location** | Units consumed per ingredient per location per day (via ConsumptionOrders)                     | Detect locations overconsuming relative to sales; adjust supplier orders       |
| 2   | **Stock-out frequency**                               | Number of times an ingredient's stock hit zero or triggered the minimum threshold in a period  | Identify chronically under-stocked ingredients; renegotiate supply contracts   |
| 3   | **Waste and loss ratio**                              | Proportion of ConsumptionOrders with `reason = waste / spoilage / theft` vs. total consumption | Flag locations with abnormal waste patterns; trigger operational investigation |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event              | Trigger                                                                      | Stream or batch? (your call) |
| ---------------------------- | ---------------------------------------------------------------------------- | ---------------------------- |
| `supply_order_created`       | A SupplyOrder is successfully registered                                     | ?                            |
| `consumption_order_created`  | A ConsumptionOrder is successfully registered                                | ?                            |
| `stock_threshold_triggered`  | An ingredient's stock falls to or below `min_stock_threshold` after an order | ?                            |
| `direct_stock_edit_rejected` | A request to modify stock directly (outside an order) is blocked by the API  | ?                            |
| `consumption_order_failed`   | A ConsumptionOrder is rejected (e.g. insufficient stock, validation error)   | ?                            |
| `supply_order_failed`        | A SupplyOrder is rejected (e.g. unknown supplier, invalid quantity)          | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions for Brasaland.

| Candidate event           | Trigger                                                                  | Section        |
| ------------------------- | ------------------------------------------------------------------------ | -------------- |
| `user_login_succeeded`    | Successful login by a location manager or operator                       | Authentication |
| `user_login_failed`       | Failed login attempt (wrong credentials or expired session)              | Authentication |
| `session_expired`         | User session timed out and was invalidated                               | Authentication |
| `ingredient_list_viewed`  | User opens the ingredient stock list for a location                      | Navigation     |
| `order_form_abandoned`    | User starts but does not complete a SupplyOrder or ConsumptionOrder form | Navigation     |
| `location_filter_applied` | User filters stock view by a specific location                           | Navigation     |

---

## Business Constraints for Your Plan

- **Dual currency:** ingredients in Colombian locations are valued in COP; Florida locations in USD. Events that include cost or value fields must carry a `currency` property.
- **Multi-location sensitivity:** any event that originates from a specific restaurant location must include `location_id` so data can be segmented by country and city.
- **No PII in telemetry:** `created_by` fields must be included as opaque TinyDB UUIDs — never as names or email addresses.
- **Waste and theft are sensitive:** `ConsumptionOrder` events with `reason = theft` should be flagged in your schema as requiring restricted access; document this in your risks and exclusions section.

---

## What Your Plan Should Produce for Brasaland

- `telemetry-plan.md` referencing `Ingredient`, `SupplyOrder`, and `ConsumptionOrder` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`supply_order_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by Brasaland's operational urgency — e.g. a stock-out in a high-volume Miami location on a Friday night is not the same urgency as a weekly waste summary.
- A risks and exclusions section that addresses the dual-currency and multi-location constraints, and explains any events discarded.

---

_Brasaland Digital — Internal document for 4Geeks Academy AI Engineering Track_
