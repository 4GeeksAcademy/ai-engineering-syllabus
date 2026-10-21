# BRIEFING.md — HealthCore

## Agentic Engineering – Monthly Financial Close

*Estas instrucciones están [disponibles en español](./healthcore-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**HealthCore** is an outpatient healthcare services company founded in 2011 in Austin, Texas. It runs 12 clinics, 9 in the United States and 3 in the United Kingdom, employs approximately 200 people, and generates around 28 million dollars in annual revenue. It operates in US dollars (USD) and pounds sterling (GBP), and under two health data protection frameworks: HIPAA in the United States and UK GDPR in the United Kingdom.

---

## Your department and the problem you must solve

You are part of **HealthCore Digital**, the internal unit building the company's infrastructure, and you report to CTO James Osei.

Dr. Sandra Okonkwo, the CEO, receives the month's financial data in reports each department prepares separately, in different formats, with figures that sometimes contradict each other because they come from different systems. US revenue depends on insurers and public programmes with claim denial rates that change from month to month, and the CEO needs to see that effect in the close without waiting for the Revenue Cycle report.

---

## Your stakeholder

**Dr. Sandra Okonkwo**, CEO (Austin)

> Subject: Monthly financial close
>
> Team,
>
> 1. I need each month's close on the third business day, first thing Austin time.
> 2. Revenue by country and by payer (commercial insurance, Medicare/Medicaid, private, NHS contract), and expenses by country. Consolidated in dollars.
> 3. Every deviation of 5% or more must be explained with data. I won't accept explanations without figures to support them.
> 4. Tom Callahan reviews the report before it reaches the leadership team.
> 5. This is a financial report. It must not contain any patient data, in any section, under any circumstances. If any source record contains it, I want to know — but without the data appearing in the report.
>
> Sandra

---

## Language scope

- The base language is **English**, since the leadership team works in Austin and London.
- Spanish is **optional**. If you implement it, the figures must be identical in both versions: only the text changes.

---

## Data sources

Generate three CSV files for the **closing month** (the last full month before the load date):

| File | Columns | Content |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, payer, category, description, currency, amount, source_ref` | The month's revenue and expense entries. Revenue is positive and expenses are negative. Expenses use `payer = n/a` |
| `budget.csv` | `month, country, payer, category, currency, amount` | The month's budget |
| `operations.csv` | `month, country, payer, metric, value` | **Aggregated** operational indicators that support the explanations |

Each line item must have **several entries** in `ledger.csv` whose sum exactly matches the actual figure in the table below. Revenue is recorded **aggregated by clinic and payer**, never per patient. For supplier lines, the description includes the supplier, the unit price, and the quantity.

Intentionally include **one expense entry** whose description contains a fictional patient's name (for example, a mis-recorded refund), to test the specific restriction.

---

## Budget and actual figures for the closing month

**Revenue — United States (USD)**

| Payer | Budget | Actual | Deviation |
|---|---|---|---|
| Commercial insurance | 1,150,000 | 1,120,000 | −2.6% |
| Medicare / Medicaid | 520,000 | 468,000 | −10.0% |

**Revenue — United Kingdom (GBP)**

| Payer | Budget | Actual | Deviation |
|---|---|---|---|
| Private | 260,000 | 271,000 | +4.2% |
| NHS contract | 75,000 | 75,000 | 0.0% |

**Expenses — United States (USD)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Clinical consumables (MedSupply Partners) | 44,800 | 46,816 | +4.5% |
| Laboratory (ClearPath Labs) | 45,000 | 48,150 | +7.0% |
| Medical interpreting (LinguaCare Interpreting) | 17,550 | 17,550 | 0.0% |
| Payroll | 1,050,000 | 1,060,000 | +1.0% |
| Clinic rent | 180,000 | 180,000 | 0.0% |

**Expenses — United Kingdom (GBP)**

| Line item | Budget | Actual | Deviation |
|---|---|---|---|
| Clinical consumables (BritMed Supplies) | 9,450 | 9,450 | 0.0% |
| Laboratory (Thames Pathology) | 10,150 | 10,353 | +2.0% |
| Payroll | 210,000 | 209,000 | −0.5% |
| Clinic rent | 52,000 | 52,000 | 0.0% |
| Clinical software licences | 8,000 | **No entries** | — |

**Operational indicators (`operations.csv`)**

| Country | Payer | Indicator | Budget | Actual |
|---|---|---|---|---|
| United States | Medicare / Medicaid | Claims submitted | 4,000 | 4,000 |
| United States | Medicare / Medicaid | Denial rate | 14.0% | 22.6% |
| United States | Commercial insurance | Claims submitted | 6,500 | 6,400 |
| United States | Commercial insurance | Denial rate | 12.0% | 12.0% |

**Reference data:** consolidation exchange rate, 1 GBP = 1.27 USD.

---

## Deviation threshold

A line item is a **relevant deviation** when its deviation from budget is equal to or greater than **5%**, favorable or unfavorable.

---

## Expected outcomes

| Line item | Expected outcome |
|---|---|
| Medicare / Medicaid (−10.0%) | Relevant deviation. Data-backed hypothesis: the same number of claims was submitted, but the denial rate rose from 14.0% to 22.6% |
| US laboratory (+7.0%) | Relevant deviation. Hypothesis: per-test price increase, with the same number of tests |
| US clinical consumables (+4.5%) and UK private (+4.2%) | Not relevant: below the threshold |
| UK clinical software licences | **Missing data.** The report must state it, and must not treat it as 0 or as a −100% deviation |
| Entry with a patient name | Flagged as uncertain and listed in the uncertain data section **by its `entry_id`**, without reproducing its description |

---

## Report structure

1. **Executive summary**: five lines maximum.
2. **Consolidated result in USD**: revenue, expenses, and result, actual versus budget.
3. **Revenue by country and payer**, in local currency.
4. **Expenses by country**, in local currency.
5. **Relevant deviations**: one per line item, with the hypothesis and the figures supporting it.
6. **Missing or uncertain data**.
7. **Traceability annex**: for each figure, the `entry_id`s that produce it.

---

## Review and distribution

| Step | Detail |
|---|---|
| Run | Third business day of each month, 06:00 (Austin time) |
| Review | Tom Callahan, Revenue Cycle Director |
| Distribution after approval | Dr. Sandra Okonkwo, James Osei, Dr. Marcus Reid, Priya Nair, Tom Callahan, Claire Whitfield, and Diane Foster |

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- **Any patient data** (names, identifiers, diagnoses, services received by a specific person)
- Individual salaries. Payroll is recorded **only as an aggregate per country**
- Supplier bank details

---

## Specific restriction

Before any record reaches the agent, the system must check whether its description contains data that could identify a patient. If it does, the record is flagged as uncertain, its description is **not sent to the model**, and the report only mentions it by its `entry_id`. Compliance (Claire Whitfield) receives a notification with that `entry_id` for review.
