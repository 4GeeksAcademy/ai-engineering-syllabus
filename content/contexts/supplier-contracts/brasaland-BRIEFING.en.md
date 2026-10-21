# BRIEFING.md — Brasaland

## Agentic Engineering – Supplier and Contract Management

*Estas instrucciones están [disponibles en español](./brasaland-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Brasaland** is a grilled food restaurant chain founded in 2008 in Medellín, Colombia. It runs 14 company-owned restaurants in Colombia and the United States (Florida), employs approximately 115 people, and generates around 6 million dollars in annual revenue. It works with about 20 suppliers across both countries, with different suppliers in each market, and operates in two currencies: Colombian pesos (COP) and US dollars (USD).

---

## Your department and the problem you must solve

You work in **Brasaland Digital**, the internal team leading the company's digital transformation, and you report to CTO Nicolás Park.

Beef is Brasaland's largest cost line, and its price moves differently in Colombia and in Florida. Today, Lucía Fernández's Procurement team finds out about price increases when the invoice arrives. Supplier contracts are PDFs scattered across emails and folders, and nobody remembers when each one expires, how much notice it requires, or which increases it allows. Felipe Guerrero, Operations Director, feels the consequences in every location's margins and wants a system that connects prices and contracts.

---

## Your stakeholder

**Felipe Guerrero**, Operations Director (Medellín)

> Team,
>
> - Beef price increases are eating my margin and I find out late.
> - I need an alert when a supplier raises a price above normal.
> - With the alert, I want to know whether the contract allows it. Yes or no, and why.
> - If it doesn't, I want a brief to renegotiate: history, comparison with other suppliers of the same product, how much it costs us, and what the contract says about walking away.
> - Warn me before a contract expires or a notice deadline passes. One already renewed itself because nobody gave notice in time.
> - Nothing goes out to a supplier without my sign-off. If the contract is large, Mariana's too.
>
> Felipe

---

## Language scope

- Multilingual support is **optional but highly recommended**, since Brasaland has contracts in Spanish (Colombia) and English (Florida).
- Choose one **base language** for answers, briefs, and alerts.
- Contracts are analyzed in their original language. Clause quotes are reproduced in the contract's language, even if the answer is in the other language.

---

## Suppliers

| ID | Supplier | Country | Category | Currency |
|---|---|---|---|---|
| BR-S01 | Carnes del Valle S.A.S. | Colombia | Beef | COP |
| BR-S02 | Avícola Antioquia | Colombia | Chicken | COP |
| BR-S03 | Hortalizas La Sabana | Colombia | Vegetables | COP |
| BR-S04 | Frigorífico Andino | Colombia | Beef | COP |
| BR-S05 | Sunshine Prime Meats | United States | Beef | USD |
| BR-S06 | Gulf Coast Beef Co. | United States | Beef | USD |
| BR-S07 | Gulf Poultry Co. | United States | Chicken | USD |
| BR-S08 | Brava Beverages FL | United States | Beverages | USD |

Price comparisons are made **between suppliers in the same category and the same country**.

---

## Contracts

Generate one fictional PDF contract per row, with each term written as a numbered clause. Dates are relative to the data load date, so alerts can be tested at any time.

| Contract | Supplier | Expiry | Notice | Price revision | Exit and penalty | Estimated annual value |
|---|---|---|---|---|---|---|
| CT-BR-01 | Carnes del Valle | Today + 120 days | Non-renewal: 60 days before expiry | Every six months, capped at Colombia's annual CPI plus 1 point, with 30 days' written notice | Either party, with 60 days' notice, no penalty | COP 1,276,800,000 |
| CT-BR-02 | Sunshine Prime Meats | Today + 75 days | Auto-renews for 12 months unless notice is given 45 days before expiry | Fixed price for the term, unless the beef reference index rises more than 10% in the quarter, with 30 days' written notice | Early termination penalty of 2 months of average purchases | USD 207,360 |
| CT-BR-03 | Avícola Antioquia | Today + 200 days | **The contract has no notice clause** | Annual, capped at 5% | With 90 days' notice, no penalty | COP 586,500,000 |
| CT-BR-04 | Brava Beverages FL | Today + 20 days | Non-renewal: 15 days before expiry | Free, per the supplier's quarterly price list | No penalty | USD 86,400 |

Hortalizas La Sabana, Frigorífico Andino, Gulf Coast Beef Co., and Gulf Poultry Co. **have no contract**: purchases are made per order.

**Reference data** for calculations:
- Colombia annual CPI: 5.2%
- Reference exchange rate: 1 USD = 4,000 COP

---

## Price history

Generate a CSV with 12 months of history (the last month is the load month) and these columns:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

| Supplier | Product | Unit | Base price | Monthly volume |
|---|---|---|---|---|
| BR-S01 | Punta de anca (rump cap) | kg | COP 38,000 | 2,800 kg |
| BR-S04 | Punta de anca (rump cap) | kg | COP 36,500 | 0 (quote only) |
| BR-S05 | Picanha | lb | USD 7.20 | 2,400 lb |
| BR-S06 | Picanha | lb | USD 7.05 | 0 (quote only) |
| BR-S02 | Whole chicken | kg | COP 11,500 | 4,250 kg |
| BR-S07 | Whole chicken | lb | USD 2.10 | 3,000 lb |
| BR-S03 | Mixed vegetables | kg | COP 4,200 | 6,000 kg |
| BR-S08 | Beverages (case) | case | USD 24.00 | 300 cases |

During the first 11 months, prices may vary by at most ±1% per month. In the **last month**, these scenarios must appear:

| Scenario | Supplier | Last-month change | Expected outcome |
|---|---|---|---|
| A | BR-S05 Sunshine Prime Meats | +12% | Above threshold. **Not allowed**: the contract requires written notice and proof of the index, and there is no record of either |
| B | BR-S01 Carnes del Valle | +4% | Above threshold. **Allowed**: below CPI + 1 point (6.2%) |
| C | BR-S02 Avícola Antioquia | +9% | Above threshold. **Not allowed**: exceeds the 5% annual cap |
| D | BR-S08 Brava Beverages FL | +6% | Below threshold. No price alert, but its contract triggers an expiry alert |

---

## Thresholds and alerts

| Type | Rule |
|---|---|
| Price increase, beef | More than 3% versus the previous month |
| Price increase, other categories | More than 8% versus the previous month |
| Contract expiry | 90 and 30 days before |
| Notice deadline | 15 days before |

Alerts go to Lucía Fernández (Procurement) and Felipe Guerrero.

---

## Approvals

| Situation | Approved by |
|---|---|
| Any communication to a supplier | Felipe Guerrero |
| Communication about a contract with an annual value above USD 200,000 (or its COP equivalent) | Felipe Guerrero **and** Mariana Restrepo |

---

## Questions the system must be able to answer

- "Does the contract allow Sunshine Prime Meats' price increase?"
- "How much does Avícola Antioquia's increase cost us per month?"
- "What alternative do we have to Carnes del Valle, and at what price?"
- "When do we have to notify Sunshine Prime Meats if we don't want to renew?"
- "What is Avícola Antioquia's notice period?" → the system must answer that the contract doesn't specify one.
- "What does the Hortalizas La Sabana contract say?" → the system must answer that there is no contract.
- "Prepare a brief to renegotiate with Sunshine Prime Meats."

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Supplier bank details included in the contracts
- Personal data of supplier contact people (personal phone and email)

The test contracts must include this data in a billing clause, so you can verify the system doesn't propagate it.

---

## Specific restriction

Renegotiation briefs and alerts compare prices only within the same country. If someone asks to compare a Colombian supplier with a Florida one, the system may do it by converting at the reference exchange rate, but it must state that these are different markets and that the comparison is only indicative.
