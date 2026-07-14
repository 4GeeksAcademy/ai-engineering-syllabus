# CONTEXT — Brasaland

## Telemetry Projects (Plan · Capture · Storage · Report)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-brasaland.es.md)._

<!-- endhide -->

---

## 1. Your Company

Brasaland is a grilled-food restaurant chain with 14 locations across Colombia and Florida. The inventory management system is what every location uses to control its ingredients: meats, vegetables, sauces, beverages, and packaging. That system is already in production — but, as your tech lead put it, "operations has no idea what's happening inside it."

Your Telemetry Plan, capture, storage, and technical report all revolve around that inventory system, and they are the foundation on which, later on, Brasaland will build its executive dashboard and business reports (sales per location, Colombia vs. Florida comparison, strategic alerts for Mariana and Felipe).

---

## 2. Inventory System Entities at Brasaland

| Entity          | At Brasaland this means...                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------ |
| `Product`      | An ingredient or supply item: e.g. `beef loin`, `whole chicken`, `house sauce`, `takeout packaging`. Each product has a unit of measure (kg, unit, liter) and belongs to a category (protein, vegetable, sauce, beverage, packaging, cleaning). |
| `InboundOrder`  | An inbound order: goods received from a supplier at a specific location.                        |
| `OutboundOrder` | An outbound order: ingredient consumption in dish preparation, or recorded waste (expired product, kitchen error, theft). |
| `location`      | Each of the 14 locations, identified by country (`CO`/`US`) and city.                            |
| `supplier`      | One of Brasaland's ~20 suppliers, different per country.                                        |

---

## 3. Mandatory Telemetry Metrics

These are the metrics Brasaland needs to measure **from day one**, regardless of what else you identify in your own catalogue. They go straight into the floor of your Telemetry Plan (Phase 1) and must be instrumented end-to-end (capture → storage) by the end of the project series.

> These metrics are not just for today: further along in the course, they will feed Felipe's operations dashboard and Mariana's weekly executive report. Design them with the future in mind — they will need to be aggregated by location, by country, and by week.

| `event_type`                          | Fires when...                                                                       | Business hypothesis                                                                                       | Decision it enables                                                                            |
| --------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `inbound_order_created`               | A location registers the arrival of goods from a supplier                              | We need to know how much and what is being purchased, by location and supplier                              | Consolidate purchasing across locations to negotiate better prices (Lucía)                          |
| `outbound_order_created`              | A location registers ingredient consumption in dish preparation                        | We need to know which ingredients are consumed most, and at what rate, by location                          | Adjust the automatic supplier order suggestion (Felipe)                                             |
| `stock_waste_registered`              | A location registers waste (expired product, kitchen error, or loss/theft)             | We need to know how much product is lost, why, and at which location                                        | Prioritise waste audits at the worst-performing locations (Felipe)                                  |
| `stock_threshold_triggered`           | A product's stock at a location falls below the configured minimum                     | We need to know how often a location runs short of a key ingredient                                          | Adjust the minimum threshold or the replenishment frequency for that product                        |
| `direct_stock_edit_rejected`          | A user attempts to modify stock directly (outside an order) and the system rejects it  | We need to know if staff are attempting to bypass traceability controls                                      | Reinforce training or permissions at the locations where this happens most (Jake)                    |
| `ingredient_price_variance_detected`  | The unit cost of an inbound order varies more than a threshold (e.g. 10%) from the historical value for that product/supplier | We need to know when a key ingredient (e.g. beef) rises in price abnormally                                  | Alert Lucía and Mariana to renegotiate or find an alternate supplier                                 |

**Minimum `properties` fields for inventory events** (in addition to the standard envelope): `location_id`, `country` (`CO`/`US`), `product_id`, `product_category`, `quantity`, `unit`, `currency` (`COP`/`USD`), and for `outbound_order_created`/`stock_waste_registered` also `reason` (waste only: `expired`, `kitchen_error`, `theft_suspected`).

⚠️ Do not include employee names or customer data in `properties` — these events describe products and locations, not people.

---

## 4. How These Metrics Connect to the Future

These metrics are not just for today's technical report. As the course progresses, this same data will be reused for automation and for executive-level reporting — at a level of aggregation and polish well beyond what you're building right now. Design them as if someone else, later on, will depend on them without being able to ask you how they work.

Designing the envelope and the property allowlist well today saves you from having to re-instrument these events later.

---

## 5. Suggested Seed Data

Generate at least:

- 8–10 distinct products, covering at least 3 categories (protein, vegetable/sauce, packaging)
- 3 locations (at least one in Colombia and one in Florida)
- 15–20 inbound orders distributed across those locations and at least 3 suppliers
- 15–20 outbound orders, including at least 3 waste records with different reasons
- At least 2 cases that trigger `stock_threshold_triggered` and 1 case of `ingredient_price_variance_detected`

---

## 6. Business Constraints

- Amounts must be recorded in the location's local currency (`COP` for Colombia, `USD` for Florida) — do not convert currencies at the telemetry layer, that is the job of the executive reporting pipeline later.
- Stock is never modified directly: every modification goes through `InboundOrder` or `OutboundOrder`, traceable to a user.
- Any event related to interface language (Spanish/English) is independent from these metrics — do not mix UI language with the location's `country`.
