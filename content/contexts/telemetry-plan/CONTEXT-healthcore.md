# CONTEXT — HealthCore · Telemetry Phase 1: Company's Telemetry plan design

_Estas instrucciones también están disponibles en [español](./CONTEXT-healthcore.es.md)._

## Your Company

**HealthCore** is an outpatient healthcare services company with 12 clinics across the US (Texas, Florida, Georgia) and UK (London, Manchester). You are part of **HealthCore Digital**, the internal technology team led by James Osei (CTO). The inventory management system you built tracks medical supply stock across clinic locations — products, inbound supply orders, and outbound dispensing orders — enforcing the rule that supply levels are never edited directly.

Dr. Marcus Reid (Director of Clinical Operations) and Claire Whitfield (Chief Compliance Officer) have been asking questions the system cannot yet answer. Your telemetry plan will define exactly what data to capture to answer them.

---

## Your Inventory System Entities

These are the canonical entity names you established in the backend. Your telemetry plan must reference them exactly.

| Generic name (README) | HealthCore entity name | Description                                                                             |
| --------------------- | ---------------------- | --------------------------------------------------------------------------------------- |
| `Product`             | `MedicalSupply`        | A tracked consumable or equipment item (e.g. gloves, syringes, blood pressure monitors) |
| `InboundOrder`        | `SupplyDelivery`       | A vendor delivery that increases medical supply stock at a clinic                       |
| `OutboundOrder`       | `DispensingOrder`      | A clinical use record that reduces supply stock                                         |

Key fields to reference in your event schemas:

- `MedicalSupply`: `id`, `name`, `category` (`consumable`, `diagnostic_equipment`, `ppe`, `medication_adjacent`, `cleaning`), `unit`, `current_stock`, `min_stock_threshold`, `clinic_id`, `jurisdiction` (`us` / `uk`)
- `SupplyDelivery`: `id`, `supply_id`, `quantity`, `vendor`, `clinic_id`, `jurisdiction`, `created_by` (TinyDB user UUID), `created_at`
- `DispensingOrder`: `id`, `supply_id`, `quantity`, `clinical_context` (`procedure`, `routine_care`, `emergency`, `waste_disposal`), `clinic_id`, `jurisdiction`, `created_by`, `created_at`

---

## Your 3 KPIs

These are the primary metrics Dr. Reid and Dr. Okonkwo (CEO) need from the medical supply system. Your plan must justify how telemetry feeds each one.

| #   | KPI                                   | Definition                                                                                                      | Business decision it enables                                                                      |
| --- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1   | **Critical supply availability rate** | Percentage of time that PPE and high-priority consumables remain above `min_stock_threshold` across all clinics | Prevent clinical care disruption; trigger emergency procurement when availability drops below 95% |
| 2   | **Emergency dispensing frequency**    | Number of DispensingOrders with `clinical_context = emergency` per clinic per week                              | Identify clinics with recurring emergency supply needs; adjust standard stock levels proactively  |
| 3   | **Stock-out incident rate**           | Number of times any supply's stock hit zero, segmented by clinic and jurisdiction                               | Compare US vs. UK supply chain reliability; inform vendor performance reviews                     |

---

## Candidate Events — Inventory Module

These are suggested starting points. You may refine, split, merge, or discard them — but every event you keep must survive the golden rule test.

| Candidate event                | Trigger                                                                            | Stream or batch? (your call) |
| ------------------------------ | ---------------------------------------------------------------------------------- | ---------------------------- |
| `supply_delivery_created`      | A SupplyDelivery is successfully registered                                        | ?                            |
| `dispensing_order_created`     | A DispensingOrder is successfully registered                                       | ?                            |
| `stock_threshold_triggered`    | A supply's stock falls to or below `min_stock_threshold` after a dispensing        | ?                            |
| `direct_stock_edit_rejected`   | A request to modify supply stock directly (outside an order) is blocked by the API | ?                            |
| `dispensing_order_failed`      | A DispensingOrder is rejected (e.g. insufficient stock, invalid clinical context)  | ?                            |
| `emergency_dispensing_flagged` | A DispensingOrder with `clinical_context = emergency` is created                   | ?                            |

---

## Candidate Events — Backoffice (Beyond Inventory)

These cover other sections of the backoffice application. Pick the ones that produce data relevant to your KPIs or to operational decisions at HealthCore.

| Candidate event             | Trigger                                                           | Section        |
| --------------------------- | ----------------------------------------------------------------- | -------------- |
| `user_login_succeeded`      | Successful login by a clinic manager or administrator             | Authentication |
| `user_login_failed`         | Failed login attempt (wrong credentials or expired session)       | Authentication |
| `session_expired`           | User session timed out and was invalidated                        | Authentication |
| `supply_list_viewed`        | User opens the medical supply stock list for a clinic             | Navigation     |
| `dispensing_form_abandoned` | User starts but does not complete a DispensingOrder form          | Navigation     |
| `clinic_filter_applied`     | User filters the supply view by a specific clinic or jurisdiction | Navigation     |

---

## Business Constraints for Your Plan

- **Dual jurisdiction — HIPAA and UK GDPR:** any event that could be linked to a patient — directly or indirectly — falls under HIPAA (US) or UK GDPR (UK). `DispensingOrder` events tied to a specific patient procedure must not include patient identifiers; use `clinic_id` and `clinical_context` only. Document this explicitly in your risks and exclusions section.
- **Jurisdiction field is mandatory:** every event originating from a clinic operation must include `jurisdiction` (`us` / `uk`) and `clinic_id`. Claire Whitfield requires jurisdiction-segmented audit trails for compliance reporting.
- **No PII in telemetry:** `created_by` fields must be opaque TinyDB UUIDs — never staff names or email addresses.
- **Emergency events require stream processing:** any event with `clinical_context = emergency` or a `stock_threshold_triggered` for PPE or critical consumables must be treated as a stream event. A stockout of surgical gloves is not a batch-reporting problem. Document the clinical rationale in your stream/batch justification.
- **Audit trail durability:** unlike other companies, HealthCore's telemetry events for supply movements may be subpoenaed as part of a clinical audit. Your schema must include `schemaVersion` and events must be treated as immutable once created.

---

## What Your Plan Should Produce for HealthCore

- `telemetry-plan.md` referencing `MedicalSupply`, `SupplyDelivery`, and `DispensingOrder` by name, with events justified against the three KPIs above.
- `event-schemas.json` with at least 5 complete event schemas using `entity_action` naming (`supply_delivery_created`, `stock_threshold_triggered`, etc.), each including a documented **property allowlist** — only explicitly declared keys are permitted in that event.
- A stream/batch decision for each event justified by clinical urgency — emergency supply events are non-negotiable stream; routine replenishment reporting is batch.
- A risks and exclusions section that addresses HIPAA/UK GDPR constraints, the prohibition on patient identifiers in telemetry, and any events discarded.

---

_HealthCore Digital — Internal document for 4Geeks Academy AI Engineering Track_
