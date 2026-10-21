# BRIEFING.md — TrackFlow

## Agentic Engineering – Supplier and Contract Management

*Estas instrucciones están [disponibles en español](./trackflow-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**TrackFlow** is a last-mile delivery and warehouse management company founded in 2009 in Los Angeles, United States. It operates in the United States and Spain, with warehouses in Los Angeles and Zaragoza, employs approximately 130 people, and generates around 9 million euros in annual revenue. It operates in two currencies: US dollars (USD) in the United States and euros (EUR) in Spain.

---

## Your department and the problem you must solve

You are part of **TrackFlow Tech**, the internal unit leading the company's digital transformation, and you report to CTO Andrés Kim.

Carriers are TrackFlow's main supplier and its largest variable cost. Their rates have several components (base rate, fuel surcharge) with different revision rules, and each contract regulates them differently. Today, Carlos Vega's team reviews each carrier's invoices by hand and catches increases late, if at all. The same happens with the packaging suppliers for both warehouses.

---

## Your stakeholder

**Carlos Vega**, Head of Carrier Operations (Zaragoza)

> Hi team,
>
> Here are the details, because with carriers the devil is in the rate components.
>
> 1. Each carrier bills a **base rate** per shipment and, in some cases, a separate **fuel surcharge**. Contracts treat each component differently: the base rate is usually fixed for a period and the surcharge adjusts to an index. If the system mixes them up, every conclusion it reaches will be wrong.
> 2. I want an alert when any component rises above the threshold, and an evaluation of whether the contract allows it, **component by component**.
> 3. If the contract requires notice for an increase and we don't have it on record, I want the system to say so. An allowed amount doesn't make the increase valid.
> 4. To renegotiate, I need the real impact on our monthly shipment volume and a comparison with the other carriers in the same country.
> 5. I approve communications with carriers. Ana Whitfield approves packaging ones. If the contract is large, Thomas approves too.
>
> Thanks,
> Carlos

---

## Language scope

- Multilingual support is **optional but highly recommended**, since TrackFlow has contracts in English (United States) and Spanish (Spain).
- Choose one **base language** for answers, briefs, and alerts.
- Contracts are analyzed in their original language. Clause quotes are reproduced in the contract's language.

---

## Suppliers

| ID | Supplier | Country | Category | Currency |
|---|---|---|---|---|
| TF-S01 | PacificRoute Express | United States | Parcel transport | USD |
| TF-S02 | Coastline Parcel | United States | Parcel transport | USD |
| TF-S03 | Golden State Couriers | United States | Same-day delivery | USD |
| TF-S04 | IberEnvíos | Spain | Parcel transport | EUR |
| TF-S05 | Ruta Norte Logística | Spain | Parcel transport | EUR |
| TF-S06 | BoxLine Packaging | United States | Packaging | USD |
| TF-S07 | Embalajes Ebro | Spain | Packaging | EUR |

Price comparisons are made **between suppliers in the same category and the same country**.

---

## Contracts

Generate one fictional PDF contract per row, with each term written as a numbered clause. Dates are relative to the data load date.

| Contract | Supplier | Expiry | Notice | Price revision | Exit and penalty | Estimated annual value |
|---|---|---|---|---|---|---|
| CT-TF-01 | PacificRoute Express | Today + 150 days | Non-renewal: 90 days before expiry | **Base rate:** fixed for the full term. **Fuel surcharge:** adjustable monthly per the published diesel index, capped at USD 1.00 per shipment | Early termination penalty of 1 month of average billing | USD 966,600 |
| CT-TF-02 | IberEnvíos | Today + 45 days | Non-renewal: 30 days before expiry | Annual, capped at Spain's CPI plus 1 point | With 30 days' notice, no penalty | EUR 411,600 |
| CT-TF-03 | BoxLine Packaging | Today + 300 days | **The contract doesn't specify a non-renewal notice period** | Quarterly, free based on raw material cost, with 30 days' written notice | No penalty | USD 89,280 |
| CT-TF-04 | Embalajes Ebro | Today + 20 days | Non-renewal: 15 days before expiry | Fixed price for the full term | No penalty | EUR 51,840 |

Coastline Parcel, Golden State Couriers, and Ruta Norte Logística **have no contract**: there are only quotes or one-off shipments.

**Reference data** for calculations:
- Spain annual CPI: 2.8%
- Reference exchange rate: 1 USD = 0.92 EUR

---

## Price history

Generate a CSV with 12 months of history (the last month is the load month) and these columns:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

Base rate and fuel surcharge are **separate rows** in the CSV.

| Supplier | Product | Unit | Base price | Monthly volume |
|---|---|---|---|---|
| TF-S01 | Standard shipment 0–2 kg, base rate | shipment | USD 8.40 | 9,000 shipments |
| TF-S01 | Fuel surcharge | shipment | USD 0.55 | 9,000 shipments |
| TF-S02 | Standard shipment 0–2 kg, base rate | shipment | USD 8.10 | 0 (quote only) |
| TF-S03 | Same-day delivery | shipment | USD 14.00 | 600 shipments |
| TF-S04 | Standard shipment 0–2 kg, base rate | shipment | EUR 4.90 | 7,000 shipments |
| TF-S05 | Standard shipment 0–2 kg, base rate | shipment | EUR 4.70 | 0 (quote only) |
| TF-S06 | Medium box | unit | USD 0.62 | 12,000 units |
| TF-S07 | Medium box | unit | EUR 0.48 | 9,000 units |

During the first 11 months, the fuel surcharge may vary by at most ±2% per month, and all other prices stay the same. In the **last month**, these scenarios must appear:

| Scenario | Supplier and component | Last-month change | Expected outcome |
|---|---|---|---|
| A1 | TF-S01, base rate | +6% | Above threshold. **Not allowed**: the base rate is fixed |
| A2 | TF-S01, fuel surcharge | +10% | Above threshold. **Allowed**: stays below the USD 1.00 per shipment cap |
| B | TF-S04 IberEnvíos | +3.5% | Above threshold. **Allowed**: below CPI + 1 point (3.8%) |
| C | TF-S06 BoxLine Packaging | +7% | Above threshold. **Allowed in amount, but not yet applicable**: the contract requires 30 days' written notice and none is on record |
| D | TF-S07 Embalajes Ebro | No change | No price alert, but its contract triggers an expiry alert |

---

## Thresholds and alerts

| Type | Rule |
|---|---|
| Price increase, transport (any component) | More than 3% versus the previous month |
| Price increase, packaging | More than 5% versus the previous month |
| Contract expiry | 90 and 30 days before |
| Notice deadline | 15 days before |

Transport alerts go to Carlos Vega. Packaging alerts go to Ana Whitfield.

---

## Approvals

| Situation | Approved by |
|---|---|
| Communication to a carrier | Carlos Vega |
| Communication to a packaging supplier | Ana Whitfield |
| Communication about a contract with an annual value above EUR 500,000 (or its USD equivalent) | The corresponding approver **and** Thomas Harry |

---

## Questions the system must be able to answer

- "Can PacificRoute raise our base rate? And the fuel surcharge?"
- "How much does PacificRoute's increase cost us per month, broken down by component?"
- "Can BoxLine's increase be applied yet?"
- "What alternative do we have to IberEnvíos in Spain, and at what price?"
- "When do we have to notify IberEnvíos if we don't want to renew?"
- "What is BoxLine's non-renewal notice period?" → the system must answer that the contract doesn't specify one.
- "Prepare a brief to renegotiate with PacificRoute Express."

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Supplier bank details included in the contracts
- Personal data of supplier contact people
- Names of TrackFlow's client brands and shipment volumes per client brand

The test contracts must include the first two types of data in a billing clause, so you can verify the system doesn't propagate it.

---

## Specific restriction

Base rate and fuel surcharge are always evaluated **separately**, each against its own contractual rule. The system never adds the two components together before deciding whether an increase is allowed. Impact reports may show the total, but always alongside the breakdown by component.
