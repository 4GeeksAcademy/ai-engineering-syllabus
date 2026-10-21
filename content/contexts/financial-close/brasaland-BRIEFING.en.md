# BRIEFING.md — Brasaland

## Agentic Engineering – Monthly Financial Close

*Estas instrucciones están [disponibles en español](./brasaland-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Brasaland** is a grilled food restaurant chain founded in 2008 in Medellín, Colombia. It runs 14 company-owned restaurants in Colombia and the United States (Florida), employs approximately 115 people, and generates around 6 million dollars in annual revenue. It operates in two currencies: Colombian pesos (COP) in Colombia and US dollars (USD) in Florida.

---

## Your department and the problem you must solve

You work in **Brasaland Digital**, the internal team leading the company's digital transformation, and you report to CTO Nicolás Park.

Mariana Restrepo, the CEO, runs a two-market chain without a unified financial view. Each month's data arrives in hand-built reports, in two currencies nobody consolidates the same way twice, and when a market deviates from budget the explanation arrives days later, on a call. Mariana wants each month's close ready, consolidated, and explained, without depending on someone to assemble it.

---

## Your stakeholder

**Mariana Restrepo**, CEO (Medellín)

> *Voice note transcript:*
>
> "Hi, guys. Quick one, I'm heading into a meeting. Every month I want the close ready on the third business day, first thing. It should tell me how much we sold and how much we spent in Colombia and in Florida, each in its own currency, and the combined total in dollars. It should tell me where we deviated from budget and why, but with data, not guesses. If there's no data to explain something, just say so. Before it reaches me and the team, Felipe should review it — he knows the locations' numbers best. And if something's missing, don't dress it up: I'd rather know. Thanks, bye!"

---

## Language scope

- Multilingual support is **optional but highly recommended**, since the leadership team works in Medellín and Miami.
- Choose one **base language** for the report.
- If you implement a second language, the figures must be identical in both versions: only the text changes.

---

## Data sources

Generate three CSV files for the **closing month** (the last full month before the load date):

| File | Columns | Content |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, category, description, currency, amount, source_ref` | The month's revenue and expense entries. Revenue is positive and expenses are negative |
| `budget.csv` | `month, country, category, currency, amount` | The month's budget by country and line item |
| `operations.csv` | `month, country, metric, value` | Operational indicators that support the explanations |

Each line item must have **several entries** in `ledger.csv` whose sum exactly matches the actual figure in the table below. For supplier purchase lines, the description includes the supplier, the unit price, and the quantity.

---

## Budget and actual figures for the closing month

**Colombia (COP)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Sales revenue | 1,120,000,000 | 1,090,000,000 | −2.7% |
| Beef (Carnes del Valle) | 106,400,000 | 110,656,000 | +4.0% |
| Chicken (Avícola Antioquia) | 48,875,000 | 53,273,750 | +9.0% |
| Vegetables (Hortalizas La Sabana) | 25,200,000 | 25,200,000 | 0.0% |
| Payroll | 320,000,000 | 322,000,000 | +0.6% |
| Rent | 95,000,000 | 95,000,000 | 0.0% |
| Marketing | 30,000,000 | 30,500,000 | +1.7% |
| Utilities (power, water, gas) | 22,000,000 | 21,800,000 | −0.9% |

**Florida (USD)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Sales revenue | 230,000 | 205,000 | −10.9% |
| Beef (Sunshine Prime Meats) | 17,280 | 19,353.60 | +12.0% |
| Chicken (Gulf Poultry Co.) | 6,300 | 6,300 | 0.0% |
| Beverages (Brava Beverages FL) | 7,200 | 7,632 | +6.0% |
| Payroll | 78,000 | 77,500 | −0.6% |
| Rent | 42,000 | 42,000 | 0.0% |
| Marketing | 9,000 | 15,500 | +72.2% |
| Utilities (power, water, gas) | 6,500 | **No entries** | — |

**Operational indicators (`operations.csv`)**

| Country | Indicator | Budget | Actual |
|---|---|---|---|
| Colombia | Covers served | 28,000 | 27,250 |
| Colombia | Average ticket (COP) | 40,000 | 40,000 |
| Florida | Covers served | 9,200 | 8,200 |
| Florida | Average ticket (USD) | 25.00 | 25.00 |

**Reference data:** consolidation exchange rate, 1 USD = 4,000 COP.

---

## Deviation threshold

A line item is a **relevant deviation** when its deviation from budget is equal to or greater than **5%**, favorable or unfavorable.

---

## Expected outcomes

| Line item | Expected outcome |
|---|---|
| Florida revenue (−10.9%) | Relevant deviation. Data-backed hypothesis: covers fell 10.9% while the average ticket held steady |
| Florida beef (+12.0%) | Relevant deviation. Hypothesis: supplier unit price increase, visible in the entry descriptions |
| Colombia chicken (+9.0%) | Relevant deviation. Hypothesis: supplier unit price increase, with the same quantity purchased |
| Florida beverages (+6.0%) | Relevant deviation. Hypothesis: supplier unit price increase |
| Florida marketing (+72.2%) | Relevant deviation. The hypothesis can only rely on the entry descriptions; if they don't explain the reason, the report must say so |
| Colombia beef (+4.0%) | Not relevant: below the threshold |
| Florida utilities | **Missing data.** The report must state it, and must not treat it as 0 or as a −100% deviation |

---

## Report structure

1. **Executive summary**: five lines maximum.
2. **Consolidated result in USD**: revenue, expenses, and result, actual versus budget.
3. **Result by country**, in local currency: every line item, actual versus budget.
4. **Relevant deviations**: one per line item, with the hypothesis and the figures supporting it.
5. **Missing or uncertain data**.
6. **Traceability annex**: for each figure, the `entry_id`s that produce it.

---

## Review and distribution

| Step | Detail |
|---|---|
| Run | Third business day of each month, 06:00 (Medellín time) |
| Review | Felipe Guerrero, Operations Director |
| Distribution after approval | Mariana Restrepo, Felipe Guerrero, Nicolás Park, Lucía Fernández, Camila Ospina, Ashley Turner, and Jake Morrison |

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Individual salaries. Payroll is recorded **only as an aggregate per country**; the ledger contains no per-person payroll entry
- Supplier bank details

---

## Specific restriction

The report never adds amounts in different currencies without converting them first. Each country is presented in its local currency and the consolidated view in USD at the reference exchange rate, always stating which rate was used.
