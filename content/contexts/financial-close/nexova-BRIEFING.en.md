# BRIEFING.md — Nexova

## Agentic Engineering – Monthly Financial Close

*Estas instrucciones están [disponibles en español](./nexova-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Nexova** is a human resources consulting and talent acquisition firm founded in 2011, headquartered in Valencia, Spain, with an expansion office in Miami, Florida. It has 120 employees, runs three business lines (headhunting, customer support outsourcing, and corporate training), and generates around 8 million dollars in annual revenue. It operates in euros (EUR) in Spain and US dollars (USD) in the United States.

---

## Your department and the problem you must solve

You are part of Nexova's AI Engineering team and report to CTO Sergio Molina.

Laura Mendoza, the CEO, receives weekly PDF reports each manager prepares by hand, and doesn't get a financial view of the month by business line until several days after the close. When a line deviates, she has to call its manager to understand why. She wants each month's close to arrive ready, by business line, with the deviations explained.

---

## Your stakeholder

**Laura Mendoza**, CEO (Valencia)

> Subject: Monthly close
>
> Hi,
>
> I want to stop waiting for the month's close. Here's what I need:
>
> - Each month's close, on the third business day, first thing in the morning.
> - Revenue by business line (Selection, Support, and Training) and expenses by country, against budget. The consolidated total in euros.
> - The important deviations, with a data-based explanation. If we don't know why, it should say so.
> - Before it reaches me, Tom should review it: he knows the numbers best and always asks to see the detail.
> - One important thing: the whole leadership team will read this report. I don't want client names in it.
>
> Thanks,
> Laura

---

## Language scope

- Multilingual support is **optional but highly recommended**, since the leadership team works in Valencia and Miami.
- Choose one **base language** for the report.
- If you implement a second language, the figures must be identical in both versions: only the text changes.

---

## Data sources

Generate three CSV files for the **closing month** (the last full month before the load date):

| File | Columns | Content |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, business_line, category, description, currency, amount, source_ref` | The month's revenue and expense entries. Revenue is positive and expenses are negative. Overhead expenses use `business_line = general` |
| `budget.csv` | `month, country, business_line, category, currency, amount` | The month's budget |
| `operations.csv` | `month, business_line, metric, value` | Operational indicators that support the explanations |

Each line item must have **several entries** in `ledger.csv` whose sum exactly matches the actual figure in the table below. Revenue descriptions **include the (fictional) client company name**. For supplier lines, the description includes the supplier, the unit price, and the quantity.

---

## Budget and actual figures for the closing month

**Revenue by business line**

| Line | Country | Currency | Budget | Actual | Deviation |
|---|---|---|---|---|---|
| Talent selection | Spain | EUR | 300,000 | 312,000 | +4.0% |
| Outsourced support | United States | USD | 190,000 | 168,000 | −11.6% |
| Corporate training | Spain | EUR | 120,000 | 96,000 | −20.0% |

**Expenses — Spain (EUR)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Sourcing platform (JobReach Pro) | 26,000 | 28,080 | +8.0% |
| Psychometric assessment (AssessPro) | 11,400 | 11,856 | +4.0% |
| Training rooms (Espacios Turia) | 5,040 | 5,140.80 | +2.0% |
| Payroll | 380,000 | 383,000 | +0.8% |
| Office rent | 18,000 | 18,000 | 0.0% |
| Marketing | 12,000 | 12,400 | +3.3% |
| Travel | 6,000 | **No entries** | — |

**Expenses — United States (USD)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Support telephony (VoxCloud Contact) | 2,850 | 3,021 | +6.0% |
| Payroll | 95,000 | 94,000 | −1.1% |
| Office rent | 14,000 | 14,000 | 0.0% |

**Operational indicators (`operations.csv`)**

| Line | Indicator | Budget | Actual |
|---|---|---|---|
| Talent selection | Processes closed | 25 | 26 |
| Talent selection | Average fee per process (EUR) | 12,000 | 12,000 |
| Outsourced support | Billed hours | 4,750 | 4,200 |
| Outsourced support | Hourly rate (USD) | 40 | 40 |
| Corporate training | Training days delivered | 15 | 12 |
| Corporate training | Average revenue per day (EUR) | 8,000 | 8,000 |

**Reference data:** consolidation exchange rate, 1 USD = 0.92 EUR.

---

## Deviation threshold

A line item is a **relevant deviation** when its deviation from budget is equal to or greater than **5%**, favorable or unfavorable.

---

## Expected outcomes

| Line item | Expected outcome |
|---|---|
| Outsourced support (−11.6%) | Relevant deviation. Data-backed hypothesis: billed hours fell 11.6% with a steady rate |
| Corporate training (−20.0%) | Relevant deviation. Hypothesis: 12 training days were delivered versus 15 budgeted |
| JobReach Pro (+8.0%) | Relevant deviation. Hypothesis: per-license price increase, with the same number of licenses |
| VoxCloud Contact (+6.0%) | Relevant deviation. Hypothesis: per-seat price increase, with the same number of seats |
| Talent selection (+4.0%) | Not relevant: below the threshold |
| Travel | **Missing data.** The report must state it, and must not treat it as 0 or as a −100% deviation |

---

## Report structure

1. **Executive summary**: five lines maximum.
2. **Consolidated result in EUR**: revenue, expenses, and result, actual versus budget.
3. **Revenue by business line**, in local currency and in EUR.
4. **Expenses by country**, in local currency.
5. **Relevant deviations**: one per line item, with the hypothesis and the figures supporting it.
6. **Missing or uncertain data**.
7. **Traceability annex**: for each figure, the `entry_id`s that produce it.

---

## Review and distribution

| Step | Detail |
|---|---|
| Run | Third business day of each month, 06:00 (Valencia time) |
| Review | Tom Reeves, Senior Sales Analyst |
| Distribution after approval | Laura Mendoza, Javier Almeida, Marcos Ibáñez, Elena Vargas, Roberto Díaz, Patricia Solís, Carmen Ruiz, and Sergio Molina |

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Individual salaries. Payroll is recorded **only as an aggregate per country**
- Supplier bank details
- Candidate data

---

## Specific restriction

The report **shows no client names** in any section, even though they appear in the ledger descriptions. Revenue is presented aggregated by business line, and the annex's traceability uses `entry_id`s without reproducing descriptions. If a hypothesis needs to mention a specific client, the report must state that a relevant client exists and refer to the reviewer, without naming it.
