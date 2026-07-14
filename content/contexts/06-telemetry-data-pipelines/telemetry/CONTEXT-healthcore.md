# CONTEXT — HealthCore

## Telemetry Projects (Plan · Capture · Storage · Report)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-healthcore.es.md)._

<!-- endhide -->

---

## 1. Your Company

HealthCore operates 12 outpatient clinics across the United States (Texas, Florida, Georgia) and the United Kingdom (London, Manchester). The inventory system controls the **clinical supplies**: commonly used medications, wound-care material, PPE (personal protective equipment), and consultation-room consumables at each clinic.

Your Telemetry Plan, capture, storage, and technical report all revolve around that system. Later on, this same telemetry will feed the network operations dashboard and Dr. Okonkwo's monthly executive report.

> ⚠️ **Regulatory note (HIPAA / UK GDPR):** the events in this system describe **supplies and stock**, never patients. No `properties` field may contain patient names, medical record identifiers, diagnoses, or any real or simulated data that could be interpreted as protected health information (PHI). If you need to associate a supply consumption event with a clinical context, use only the `department` or service type (e.g. `general_consultation`, `chronic_care`), never a patient identifier.

---

## 2. Inventory System Entities at HealthCore

| Entity          | At HealthCore this means...                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| `Product`      | A clinical or consultation-room supply item: e.g. `nitrile gloves (box)`, `5ml syringes`, `flu vaccine`, `surgical mask`. Each product has a category (`medication`, `ppe`, `consumable`, `equipment`) and, where applicable, an expiry date. |
| `InboundOrder`  | An inbound order: receipt of supplies from a vendor at a clinic.                                                 |
| `OutboundOrder` | An outbound order: consumption of a supply during clinical care (recorded by department, not by patient).       |
| `clinic`        | One of the 12 clinics, identified by country (`US`/`UK`) and state/region.                                       |
| `department`    | Primary care, specialty care, chronic disease management, etc.                                                   |

---

## 3. Mandatory Telemetry Metrics

These are the metrics HealthCore needs to measure **from day one**, regardless of what else you identify in your own catalogue. They go straight into the floor of your Telemetry Plan (Phase 1) and must be instrumented end-to-end by the end of the project series.

> These metrics will feed, further along in the course, Dr. Okonkwo's network operations dashboard and Claire's compliance alerts. Design them with the future in mind — they will need to be aggregated by clinic and by country (US/UK), always respecting HIPAA and UK GDPR.

| `event_type`                    | Fires when...                                                                                  | Business hypothesis                                                                                              | Decision it enables                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `inbound_order_created`           | A clinic registers the receipt of supplies from a vendor                                              | We need to know how much and what supply is being purchased, by clinic and vendor                                  | Consolidate purchasing across clinics and negotiate better vendor terms                                        |
| `outbound_order_created`          | A clinic registers the consumption of a supply in a department's care activity                       | We need to know which supplies are consumed most, and at what rate, by clinic and department                       | Adjust automatic replenishment of critical supplies per clinic                                                 |
| `stock_threshold_triggered`      | A supply's stock at a clinic falls below the configured minimum                                       | We need to know how often a clinic runs short of a critical supply (e.g. PPE, medication)                          | Prioritise urgent restocking and escalate to Marcus (Clinical Operations)                                      |
| `direct_stock_edit_rejected`     | A user attempts to modify stock directly (outside an order) and the system rejects it                 | We need to know if staff are attempting to bypass supply traceability controls                                     | Reinforce training or permissions at the clinic where this happens most                                        |
| `supply_expiry_flagged`         | A supply batch (medication or material) approaches its expiry date (e.g. within 30 days)              | We need to know which supplies are about to expire before they become waste or a compliance risk                    | Prioritise use or controlled disposal of that batch before expiry                                              |

**Minimum `properties` fields for inventory events** (in addition to the standard envelope): `clinic_id`, `country` (`US`/`UK`), `product_id`, `product_category` (`medication`/`ppe`/`consumable`/`equipment`), `quantity`, `department` (only where applicable, never a patient identifier).

⚠️ **Critical reminder:** no event in this catalogue may contain PHI. `department` describes the clinical area, not the person being treated.

---

## 4. How These Metrics Connect to the Future

These metrics are not just for today's technical report. As the course progresses, this same data will be reused for automation and for executive-level reporting — at a level of aggregation and polish well beyond what you're building right now. Design them as if someone else, later on, will depend on them without being able to ask you how they work.

---

## 5. Suggested Seed Data

Generate at least:

- 8–10 distinct supply items, covering all 4 categories (`medication`, `ppe`, `consumable`, `equipment`)
- 3 clinics (at least one in the US and one in the UK)
- 15–20 inbound orders distributed across those clinics
- 15–20 outbound orders, associated only with `department`, never with a patient
- At least 2 cases that trigger `stock_threshold_triggered` and 1 case of `supply_expiry_flagged`

---

## 6. Business Constraints

- Stock is never modified directly: every modification goes through `InboundOrder` or `OutboundOrder`, traceable to a staff user (never to a patient).
- No real or simulated patient data (name, medical record identifier, diagnosis) may appear in any field of these events, not even as test data.
- Supplies with an expiry date must record that date on the `Product` model, not just on the order — this is what makes `supply_expiry_flagged` computable consistently across clinics.
