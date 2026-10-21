# BRIEFING.md — HealthCore

## Agentic Engineering – Supplier and Contract Management

*Estas instrucciones están [disponibles en español](./healthcore-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**HealthCore** is an outpatient healthcare services company founded in 2011 in Austin, Texas. It runs 12 clinics, 9 in the United States and 3 in the United Kingdom, employs approximately 200 people, and generates around 28 million dollars in annual revenue. It operates in two currencies, US dollars (USD) and pounds sterling (GBP), and under two health data protection frameworks: HIPAA in the United States and UK GDPR in the United Kingdom.

---

## Your department and the problem you must solve

You are part of **HealthCore Digital**, the internal unit building the company's infrastructure, and you report to CTO James Osei.

The clinics depend on suppliers of clinical consumables, diagnostic laboratories, and medical interpreting services for patients who don't speak English. Prices go up without anyone noticing until the invoice arrives, and contracts are split between Clinical Operations and Compliance. There's also a risk that doesn't exist in other sectors: several of these suppliers process patient data, and the law requires them to have a signed data protection agreement. Today nobody systematically checks that those agreements exist.

---

## Your stakeholder

**Dr. Marcus Reid**, Director of Clinical Operations (Austin)

> Team,
>
> Here's a summary of what we discussed on the phone, so it's in writing.
>
> - I want to know when a clinical supplier raises prices above what's reasonable, and whether the contract allows it.
> - I want advance warning before a contract expires. Being left without a lab or without interpreting on a Monday morning is not an option for our patients.
> - If we need to renegotiate, a summary with the history, what other suppliers charge, and what the contract allows us to do.
> - The labs and the interpreting service handle patient data. Claire insists, rightly, that the system always checks they have a signed data protection agreement. If one is missing, she needs to know first, before we talk about prices.
> - No communication goes to a supplier without my approval. If the supplier handles patient data, Claire's approval too.
>
> Marcus

---

## Language scope

- The base language is **English**: all contracts and supplier communications are in English.
- Spanish is **optional** for the system's internal answers.

---

## Suppliers

| ID | Supplier | Country | Category | Currency | Processes patient data? |
|---|---|---|---|---|---|
| HC-S01 | MedSupply Partners | United States | Clinical consumables | USD | No |
| HC-S02 | CareSource Medical | United States | Clinical consumables | USD | No |
| HC-S03 | ClearPath Labs | United States | Laboratory | USD | Yes |
| HC-S04 | Lone Star Diagnostics | United States | Laboratory | USD | Yes |
| HC-S05 | BritMed Supplies | United Kingdom | Clinical consumables | GBP | No |
| HC-S06 | Thames Pathology | United Kingdom | Laboratory | GBP | Yes |
| HC-S07 | LinguaCare Interpreting | United States | Medical interpreting | USD | Yes |

Price comparisons are made **between suppliers in the same category and the same country**.

---

## Contracts

Generate one fictional PDF contract per row, in English, with each term written as a numbered clause. Dates are relative to the data load date.

| Contract | Supplier | Expiry | Notice | Price revision | Exit and penalty | Data protection agreement | Estimated annual value |
|---|---|---|---|---|---|---|---|
| CT-HC-01 | MedSupply Partners | Today + 180 days | Non-renewal: 60 days before | Annual, capped at 5% | With 90 days' notice, no penalty | Not applicable | USD 537,600 |
| CT-HC-02 | ClearPath Labs | Today + 60 days | Non-renewal: 45 days before | Annual, capped at US CPI | Early termination penalty of 2 months of average billing | BAA signed, annexed to the contract | USD 540,000 |
| CT-HC-03 | Thames Pathology | Today + 210 days | Non-renewal: 90 days before | Annual, capped at 3% | With 90 days' notice, no penalty | **The contract includes no DPA** | GBP 121,800 |
| CT-HC-04 | LinguaCare Interpreting | Today + 28 days | Non-renewal: 15 days before | Fixed price for the full term | No penalty | BAA signed, annexed to the contract | USD 210,600 |

CareSource Medical, Lone Star Diagnostics, and BritMed Supplies **have no contract**: there are only quotes or one-off orders.

**Reference data** for calculations:
- US annual CPI: 2.9%
- Reference exchange rate: 1 GBP = 1.27 USD

---

## Price history

Generate a CSV with 12 months of history (the last month is the load month) and these columns:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

Volumes are **monthly aggregates**. The CSV never contains per-patient data.

| Supplier | Product | Unit | Base price | Monthly volume |
|---|---|---|---|---|
| HC-S01 | Disposable consultation kit | kit | USD 3.20 | 14,000 kits |
| HC-S02 | Disposable consultation kit | kit | USD 3.05 | 0 (quote only) |
| HC-S03 | Basic metabolic panel | test | USD 18.00 | 2,500 tests |
| HC-S04 | Basic metabolic panel | test | USD 17.20 | 0 (quote only) |
| HC-S05 | Disposable consultation kit | kit | GBP 2.70 | 3,500 kits |
| HC-S06 | Basic metabolic panel | test | GBP 14.50 | 700 tests |
| HC-S07 | Medical interpreting | minute | USD 1.95 | 9,000 minutes |

During the first 11 months, prices may vary by at most ±1% per month. In the **last month**, these scenarios must appear:

| Scenario | Supplier | Last-month change | Expected outcome |
|---|---|---|---|
| A | HC-S03 ClearPath Labs | +7% | Above threshold. **Not allowed**: the contract caps it at US CPI (2.9%). Its contract also triggers a notice deadline alert |
| B | HC-S01 MedSupply Partners | +4.5% | Above threshold. **Allowed**: within the 5% annual cap |
| C | HC-S06 Thames Pathology | +2% | Below threshold and allowed, but when evaluating the contract the system must detect that **the DPA is missing** and alert Compliance |
| D | HC-S07 LinguaCare Interpreting | No change | No price alert, but its contract triggers an expiry alert |

---

## Thresholds and alerts

| Type | Rule |
|---|---|
| Price increase, any category | More than 4% versus the previous month |
| Contract expiry | 90 and 30 days before |
| Notice deadline | 15 days before |
| Supplier processing patient data without a BAA (US) or DPA (UK) | Immediate, as soon as detected |

Price, expiry, and notice alerts go to Dr. Marcus Reid. Data protection agreement alerts go to Claire Whitfield.

---

## Approvals

| Situation | Approved by |
|---|---|
| Any communication to a supplier | Dr. Marcus Reid |
| Communication to a supplier that processes patient data | Dr. Marcus Reid **and** Claire Whitfield |
| Communication about a contract with an annual value above USD 500,000 (or its GBP equivalent) | The applicable approvers above **and** Dr. Sandra Okonkwo |

---

## Questions the system must be able to answer

- "Can ClearPath Labs raise our price by 7%?"
- "How much does ClearPath Labs' increase cost us per year?"
- "What alternative do we have to ClearPath Labs, and at what price?"
- "Which suppliers process patient data without a signed data protection agreement?"
- "When do we have to notify ClearPath Labs if we don't want to renew?"
- "What does the BritMed Supplies contract say?" → the system must answer that there is no contract.
- "Prepare a brief to renegotiate with ClearPath Labs."

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Supplier bank details included in the contracts
- Personal data of supplier contact people
- **Any patient data.** The system works only with aggregated prices and volumes. If a request asks for per-patient usage data, the system must reject it

The test contracts must include the first two types of data in a billing clause, so you can verify the system doesn't propagate it.

---

## Specific restriction

Before generating a renegotiation brief or drafting any communication for a supplier that processes patient data, the system must check that its data protection agreement is signed (BAA in the United States, DPA in the United Kingdom). If it's missing, the system stops the brief, alerts Claire Whitfield, and says so in the response. The brief can only be generated once Compliance confirms it may proceed.
