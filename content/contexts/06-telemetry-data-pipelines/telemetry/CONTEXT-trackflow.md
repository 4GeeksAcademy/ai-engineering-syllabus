# CONTEXT — TrackFlow

## Telemetry Projects (Plan · Capture · Storage · Report)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-trackflow.es.md)._

<!-- endhide -->

---

## 1. Your Company

TrackFlow manages warehousing and last-mile delivery for fashion, electronics, and cosmetics brands, operating between Los Angeles and Zaragoza. The inventory system is the operational heart of the company: the stock of every client's SKU, in every warehouse.

Brasaland sells food and Nexova sells training; at TrackFlow, inventory **is literally the business**. Your Telemetry Plan, capture, storage, and technical report all revolve around that system, and they are the foundation on which, later on, TrackFlow will build Ana's operations dashboard and Thomas's global executive dashboard.

---

## 2. Inventory System Entities at TrackFlow

| Entity          | At TrackFlow this means...                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| `Product`      | A SKU belonging to a client (brand): e.g. `t-shirt size M — Fashion Co client`, `bluetooth headset — ElectroBrand client`. Each SKU has a category (fashion, electronics, cosmetics) and belongs to a client. |
| `InboundOrder`  | An inbound order: receipt of goods from a client at a warehouse (Los Angeles or Zaragoza).                       |
| `OutboundOrder` | An outbound order: picking and dispatching of an order to the carrier for delivery to the end consumer.          |
| `warehouse`     | Los Angeles or Zaragoza.                                                                                            |
| `client`        | The brand (B2B client) that owns the SKU.                                                                          |

---

## 3. Mandatory Telemetry Metrics

These are the metrics TrackFlow needs to measure **from day one**, regardless of what else you identify in your own catalogue. They go straight into the floor of your Telemetry Plan (Phase 1) and must be instrumented end-to-end by the end of the project series.

> These metrics will feed, further along in the course, Ana's warehouse operations dashboard and Thomas's global executive dashboard (volume and SLA comparison between the United States and Spain). Design them with the future in mind — they will need to be aggregated by warehouse, by client, and by country.

| `event_type`                       | Fires when...                                                                                | Business hypothesis                                                                                    | Decision it enables                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `inbound_order_created`              | A warehouse registers the receipt of goods from a client                                       | We need to know how much volume comes in, by client and by warehouse                                     | Plan warehouse capacity and staffing based on incoming volume (Ana)                              |
| `outbound_order_created`             | A warehouse completes picking and dispatch of an order                                         | We need to know how many orders are processed, by client and warehouse, and at what rate                | Detect operational bottlenecks before they affect delivery SLA (Ana)                             |
| `stock_threshold_triggered`         | A SKU's stock falls below the configured minimum for that client                               | We need to know how often a client runs out of available stock for a SKU                                 | Alert the client and the commercial team before a stockout (Miguel)                              |
| `direct_stock_edit_rejected`        | A user attempts to modify stock directly (outside an order) and the system rejects it          | We need to know if warehouse staff are attempting to bypass traceability controls                        | Reinforce training or permissions at the warehouse where this happens most                       |
| `inventory_discrepancy_detected`    | A physical count or audit detects a difference between system stock and actual stock           | We need to know which SKUs and warehouses see the most discrepancies                                      | Prioritise inventory audits on the SKUs with the highest discrepancy rate (Ana)                   |

**Minimum `properties` fields for inventory events** (in addition to the standard envelope): `warehouse` (`los_angeles`/`zaragoza`), `client_id`, `product_id` (SKU), `product_category`, `quantity`.

⚠️ Do not include end-consumer personal data (package recipient) in `properties` — these events describe warehouse inventory, not individual home deliveries (that belongs to the last-mile tracking project).

---

## 4. How These Metrics Connect to the Future

These metrics are not just for today's technical report. As the course progresses, this same data will be reused for automation and for executive-level reporting — at a level of aggregation and polish well beyond what you're building right now. Design them as if someone else, later on, will depend on them without being able to ask you how they work.

---

## 5. Suggested Seed Data

Generate at least:

- 8–10 distinct SKUs, from at least 2 different clients and covering all 3 categories (fashion, electronics, cosmetics)
- Both warehouses (Los Angeles and Zaragoza)
- 15–20 inbound orders distributed across both warehouses
- 15–20 outbound orders
- At least 2 cases that trigger `stock_threshold_triggered` and 1 case of `inventory_discrepancy_detected`

---

## 6. Business Constraints

- Stock is never modified directly: every modification goes through `InboundOrder` or `OutboundOrder`, traceable to a user.
- Each SKU belongs to a single client — do not mix inventory across clients under the same `product_id`.
- Inventory events do not include carrier or end-recipient data — that belongs to the last-mile domain, outside the scope of this system.
