# BRIEFING.md — TrackFlow

## Agentic Engineering – Monthly Financial Close

*Estas instrucciones están [disponibles en español](./trackflow-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**TrackFlow** is a last-mile delivery and warehouse management company founded in 2009 in Los Angeles, United States. It operates in the United States and Spain, with warehouses in Los Angeles and Zaragoza, employs approximately 130 people, and generates around 9 million euros in annual revenue through three services: warehousing, last mile, and reverse logistics. It operates in US dollars (USD) in the United States and euros (EUR) in Spain.

---

## Your department and the problem you must solve

You are part of **TrackFlow Tech**, the internal unit leading the company's digital transformation, and you report to CTO Andrés Kim.

Thomas Harry, the CEO, receives a report every Monday that his directors assemble by hand on Sunday evening, and the monthly close arrives even later. He has no view by country and by service against budget, and when a number surprises him, for better or worse, he has to ask three people to understand why. He wants each month's close to be automatic, comparable across countries, and explained.

---

## Your stakeholder

**Thomas Harry**, CEO (Los Angeles)

> Subject: Monthly close — what I need
>
> Team,
>
> Short version:
>
> 1. Close ready on the 3rd business day, 6am LA time. Consolidated in euros, with each country in its own currency.
> 2. Revenue by country and service: warehousing, last mile, returns. Costs by country.
> 3. Every deviation over 5% explained with data. **Both ways.** If something went better than budget, I want to know why just as much as when it went worse. Good surprises we don't understand are just as dangerous.
> 4. Carrier costs: base rate and fuel surcharge as separate lines. Carlos has been very clear on this.
> 5. Brian reviews it before it reaches me and the team. Nothing goes out without his OK.
>
> How much does it cost to run and when will it be done? Let me know.
>
> Thomas

---

## Language scope

- Multilingual support is **optional but highly recommended**, since the leadership team works in Los Angeles and Zaragoza.
- Choose one **base language** for the report.
- If you implement a second language, the figures must be identical in both versions: only the text changes.

---

## Data sources

Generate three CSV files for the **closing month** (the last full month before the load date):

| File | Columns | Content |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, service, category, description, currency, amount, source_ref` | The month's revenue and expense entries. Revenue is positive and expenses are negative. Overhead expenses use `service = general` |
| `budget.csv` | `month, country, service, category, currency, amount` | The month's budget |
| `operations.csv` | `month, country, service, metric, value` | Operational indicators that support the explanations |

Each line item must have **several entries** in `ledger.csv` whose sum exactly matches the actual figure in the table below. For supplier lines, the description includes the supplier, the component, the unit price, and the quantity. In Spain's last-mile revenue, some entries must be credit notes described as "Contract renewal discount".

---

## Budget and actual figures for the closing month

**Revenue — United States (USD)**

| Service | Budget | Actual | Deviation |
|---|---|---|---|
| Warehousing | 180,000 | 181,000 | +0.6% |
| Last mile | 260,000 | 248,000 | −4.6% |
| Reverse logistics | 40,000 | 46,000 | +15.0% |

**Revenue — Spain (EUR)**

| Service | Budget | Actual | Deviation |
|---|---|---|---|
| Warehousing | 120,000 | 120,000 | 0.0% |
| Last mile | 150,000 | 139,500 | −7.0% |
| Reverse logistics | 25,000 | 25,000 | 0.0% |

**Expenses — United States (USD)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Transport, base rate (PacificRoute Express) | 75,600 | 80,136 | +6.0% |
| Transport, fuel surcharge (PacificRoute Express) | 4,950 | 5,445 | +10.0% |
| Same-day delivery (Golden State Couriers) | 8,400 | 8,400 | 0.0% |
| Packaging (BoxLine Packaging) | 7,440 | 7,960.80 | +7.0% |
| Payroll | 210,000 | 212,000 | +1.0% |
| Warehouse rent | 65,000 | 65,000 | 0.0% |

**Expenses — Spain (EUR)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Transport (IberEnvíos) | 34,300 | 35,500.50 | +3.5% |
| Packaging (Embalajes Ebro) | 4,320 | 4,320 | 0.0% |
| Payroll | 120,000 | 119,000 | −0.8% |
| Warehouse rent | 28,000 | 28,000 | 0.0% |
| Warehouse energy | 9,000 | **No entries** | — |

**Operational indicators (`operations.csv`)**

| Country | Service | Indicator | Budget | Actual |
|---|---|---|---|---|
| United States | Reverse logistics | Returns processed | 2,000 | 2,300 |
| United States | Reverse logistics | Average revenue per return (USD) | 20.00 | 20.00 |
| Spain | Last mile | Shipments delivered | 7,500 | 7,500 |
| Spain | Last mile | Average revenue per shipment (EUR) | 20.00 | 18.60 |

**Reference data:** consolidation exchange rate, 1 USD = 0.92 EUR.

---

## Deviation threshold

A line item is a **relevant deviation** when its deviation from budget is equal to or greater than **5%**, favorable or unfavorable.

---

## Expected outcomes

| Line item | Expected outcome |
|---|---|
| US reverse logistics (+15.0%) | **Favorable** relevant deviation. Data-backed hypothesis: 15% more returns were processed at the same average revenue |
| Spain last mile (−7.0%) | Relevant deviation. Hypothesis: shipment volume held steady and average revenue per shipment fell 7%, consistent with the renewal credit notes |
| US transport, base rate (+6.0%) | Relevant deviation. Hypothesis: base rate per shipment increase, with the same number of shipments |
| US transport, fuel surcharge (+10.0%) | Relevant deviation, presented on its own line. Hypothesis: per-shipment surcharge increase |
| US packaging (+7.0%) | Relevant deviation. Hypothesis: supplier unit price increase |
| US last mile (−4.6%) and IberEnvíos (+3.5%) | Not relevant: below the threshold |
| Spain warehouse energy | **Missing data.** The report must state it, and must not treat it as 0 or as a −100% deviation |

---

## Report structure

1. **Executive summary**: five lines maximum.
2. **Consolidated result in EUR**: revenue, expenses, and result, actual versus budget.
3. **Result by country**, in local currency: revenue by service and expenses by line item.
4. **Relevant deviations**, split into **favorable** and **unfavorable**, each with its hypothesis and the figures supporting it.
5. **Missing or uncertain data**.
6. **Traceability annex**: for each figure, the `entry_id`s that produce it.

---

## Review and distribution

| Step | Detail |
|---|---|
| Run | Third business day of each month, 06:00 (Los Angeles time) |
| Review | Brian Calloway, Senior Data Analyst |
| Distribution after approval | Thomas Harry, Andrés Kim, Ana Whitfield, Carlos Vega, Sofía Ramos, Valentina Cruz, Miguel Torres, and Rafael Sanz |

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Individual salaries. Payroll is recorded **only as an aggregate per country**
- Supplier bank details

---

## Specific restriction

Favorable deviations are explained with the same rigor as unfavorable ones and appear in their own block. In addition, a carrier's base rate and fuel surcharge are always separate lines, both in the calculation and in the report: the report may show the carrier's total, but always alongside the breakdown.
