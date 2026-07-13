# CONTEXT — Nexova

## Telemetry Projects (Plan · Capture · Storage · Report)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-nexova.es.md)._

<!-- endhide -->

---

## 1. Your Company

Nexova is an HR consulting firm with three business lines: headhunting, customer support outsourcing, and corporate training. Unlike a restaurant chain or a logistics operator, Nexova doesn't sell physical products — but it does manage a real inventory that is critical to the business: the **training and certification material** that Elena (L&D) produces and distributes to clients, candidates, and Nexova's own consultants, and the **onboarding kits** (laptops, credentials, manuals) that Patricia (HR) hands out to every new hire, including Roberto's 30 outsourced support agents.

The inventory system controls that material: how many kits of each programme exist, how many have been delivered, and when they need restocking.

Your Telemetry Plan, capture, storage, and technical report all revolve around that system. Later on, this same telemetry will feed Elena's L&D dashboard and Laura's weekly executive report.

---

## 2. Inventory System Entities at Nexova

| Entity          | At Nexova this means...                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| `Product`      | A training or onboarding material item: e.g. `B2B sales certification kit`, `support onboarding manual`, `access credential`, `temporary assignment laptop`. Each product has a category (`training_kit`, `certification`, `onboarding_equipment`) and belongs to a programme or area. |
| `InboundOrder`  | An inbound order: arrival of a new batch of material from a supplier (printer, e-learning platform, hardware vendor). |
| `OutboundOrder` | An outbound order: delivery of a kit or certificate to a client, candidate, consultant, or support agent.       |
| `office`        | Valencia or Miami.                                                                                               |
| `programme`     | The training or certification programme the material belongs to (e.g. `b2b-sales`, `basic-leadership`).        |

---

## 3. Mandatory Telemetry Metrics

These are the metrics Nexova needs to measure **from day one**, regardless of what else you identify in your own catalogue. They go straight into the floor of your Telemetry Plan (Phase 1) and must be instrumented end-to-end by the end of the project series.

> These metrics will feed, further along in the course, Elena's L&D dashboard (enrolments by programme, completion rate) and Laura's weekly executive report. Design them with the future in mind — they will need to be aggregated by office and by programme.

| `event_type`                    | Fires when...                                                                                | Business hypothesis                                                                                        | Decision it enables                                                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `inbound_order_created`           | A new batch of training or onboarding material arrives from a supplier                            | We need to know how much material is being produced/purchased, for which programme, and at what cost           | Plan material production based on expected enrolment demand (Elena)                                     |
| `outbound_order_created`          | A kit or certificate is delivered to a client, candidate, consultant, or agent                     | We need to know which programmes consume the most material, and at what rate                                    | Anticipate restocking needs before a large enrolment wave (Elena)                                       |
| `stock_threshold_triggered`       | The stock of a material item falls below the configured minimum                                    | We need to know how often a programme runs out of available material                                            | Adjust the minimum threshold or speed up reprinting/reproduction of that material                        |
| `direct_stock_edit_rejected`      | A user attempts to modify stock directly (outside an order) and the system rejects it              | We need to know if staff are attempting to bypass material traceability controls                                 | Reinforce training or permissions at the office where this happens most (Patricia)                       |
| `kit_cost_variance_detected`      | The unit cost of an inbound order varies more than a threshold (e.g. 10%) from the historical value for that material/supplier | We need to know when a material supplier raises prices abnormally                                               | Alert Elena and Laura to renegotiate or find an alternate supplier                                        |

**Minimum `properties` fields for inventory events** (in addition to the standard envelope): `office` (`valencia`/`miami`), `product_id`, `product_category` (`training_kit`/`certification`/`onboarding_equipment`), `programme_id`, `quantity`, `currency` (`EUR`/`USD`).

⚠️ Do not include candidate, client, or consultant names in `properties` — use only the programme or kit identifier, never personal data.

---

## 4. How These Metrics Connect to the Future

These metrics are not just for today's technical report. As the course progresses, this same data will be reused for automation and for executive-level reporting — at a level of aggregation and polish well beyond what you're building right now. Design them as if someone else, later on, will depend on them without being able to ask you how they work.

---

## 5. Suggested Seed Data

Generate at least:

- 6–8 distinct material items, covering all 3 categories (`training_kit`, `certification`, `onboarding_equipment`)
- At least 3 distinct programmes
- 12–15 inbound orders distributed between Valencia and Miami
- 12–15 outbound orders (deliveries)
- At least 2 cases that trigger `stock_threshold_triggered` and 1 case of `kit_cost_variance_detected`

---

## 6. Business Constraints

- Amounts must be recorded in the office's local currency (`EUR` for Valencia, `USD` for Miami) — do not convert currencies at the telemetry layer.
- Stock is never modified directly: every modification goes through `InboundOrder` or `OutboundOrder`, traceable to a user.
- Do not mix interface language (Spanish/English) with office — these are independent dimensions.
