# BRIEFING.md — Nexova

## Agentic Engineering – Supplier and Contract Management

*Estas instrucciones están [disponibles en español](./nexova-BRIEFING.es.md).*

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Nexova** is a human resources consulting and talent acquisition firm founded in 2011, headquartered in Valencia, Spain, with an expansion office in Miami, Florida. It has 120 employees, runs three business lines (headhunting, customer support outsourcing, and corporate training), and generates around 8 million dollars in annual revenue. It operates in two currencies: euros (EUR) in Spain and US dollars (USD) in the United States.

---

## Your department and the problem you must solve

You are part of Nexova's AI Engineering team and report to CTO Sergio Molina.

Nexova's three business lines depend on service suppliers: candidate sourcing platforms, psychometric assessment tools, the telephony platform for the support service, and the rooms where training is delivered. Many of these subscriptions renew automatically and go up in price every year. Javier Almeida, Operations Manager, discovers increases on the invoice, and sometimes discovers an automatic renewal when it's already too late to cancel.

---

## Your stakeholder

**Javier Almeida**, Operations Manager (Valencia)

> Hi,
>
> Let me tell you how this works in practice, because I don't want a tool nobody uses.
>
> Last year the candidate sourcing platform raised the license price for our 40 consultants and nobody noticed until the invoice. When we went to negotiate, the cancellation date had already passed and we were locked in for another year. That can't happen again.
>
> What I need is simple: warn me when a supplier raises prices above what's reasonable, tell me whether the contract allows it, and warn me in time before something renews on its own. If we need to negotiate, I want a summary of what we pay, what others charge, and what the contract lets us do. A summary, not a twenty-page report.
>
> And one very important thing: nothing goes to a supplier without me seeing it first. And we never share information about our candidates or our clients with them, not even "for context."
>
> Javier

---

## Language scope

- Multilingual support is **optional but highly recommended**, since Nexova has contracts in Spanish (Spain) and English (United States).
- Choose one **base language** for answers, briefs, and alerts.
- Contracts are analyzed in their original language. Clause quotes are reproduced in the contract's language.

---

## Suppliers

| ID | Supplier | Country | Category | Currency |
|---|---|---|---|---|
| NX-S01 | JobReach Pro | Spain | Candidate sourcing platform | EUR |
| NX-S02 | TalentPool Network | Spain | Candidate sourcing platform | EUR |
| NX-S03 | AssessPro | Spain | Psychometric assessment | EUR |
| NX-S04 | MindMetrics | Spain | Psychometric assessment | EUR |
| NX-S05 | VoxCloud Contact | United States | Support telephony | USD |
| NX-S06 | RingStack | United States | Support telephony | USD |
| NX-S07 | Espacios Turia | Spain | Training rooms | EUR |
| NX-S08 | Miami Training Rooms | United States | Training rooms | USD |

Price comparisons are made **between suppliers in the same category and the same country**.

---

## Contracts

Generate one fictional PDF contract per row, with each term written as a numbered clause. Dates are relative to the data load date.

| Contract | Supplier | Expiry | Notice | Price revision | Exit and penalty | Estimated annual value |
|---|---|---|---|---|---|---|
| CT-NX-01 | JobReach Pro | Today + 80 days | Auto-renews for 12 months unless notice is given 60 days before expiry | Annual, capped at 3%, announced 60 days in advance | Early termination penalty of 3 months' fees | EUR 312,000 |
| CT-NX-02 | AssessPro | Today + 240 days | Non-renewal: 30 days before expiry | Once a year, capped at 5% | **The contract has no early exit clause** | EUR 136,800 |
| CT-NX-03 | VoxCloud Contact | Today + 400 days | Non-renewal: 90 days before expiry | Annual, tied to US CPI, capped at 4% | Early termination penalty of 50% of remaining fees | USD 34,200 |
| CT-NX-04 | Espacios Turia | Today + 25 days | Non-renewal: 15 days before expiry | Fixed price for the full term | No penalty | EUR 60,480 |

TalentPool Network, MindMetrics, RingStack, and Miami Training Rooms **have no contract**: there are only quotes or one-off purchases.

**Reference data** for calculations:
- US annual CPI: 2.9%
- Reference exchange rate: 1 USD = 0.92 EUR

---

## Price history

Generate a CSV with 12 months of history (the last month is the load month) and these columns:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

| Supplier | Product | Unit | Base price | Monthly volume |
|---|---|---|---|---|
| NX-S01 | Recruiter license | license/month | EUR 650 | 40 licenses |
| NX-S02 | Recruiter license | license/month | EUR 610 | 0 (quote only) |
| NX-S03 | Psychometric assessment | assessment | EUR 38 | 300 assessments |
| NX-S04 | Psychometric assessment | assessment | EUR 35 | 0 (quote only) |
| NX-S05 | Agent seat | seat/month | USD 95 | 30 seats |
| NX-S06 | Agent seat | seat/month | USD 89 | 0 (quote only) |
| NX-S07 | Training room | day | EUR 420 | 12 days |
| NX-S08 | Training room | day | USD 480 | 4 days |

During the first 11 months, prices don't change, except NX-S03 and NX-S07, which may vary by at most ±1% per month. In the **last month**, these scenarios must appear:

| Scenario | Supplier | Last-month change | Expected outcome |
|---|---|---|---|
| A | NX-S01 JobReach Pro | +8% | Above threshold. **Not allowed**: exceeds the 3% annual cap |
| B | NX-S03 AssessPro | +4% | Above threshold. **Allowed**: within the 5% annual cap |
| C | NX-S05 VoxCloud Contact | +6% | Above threshold. **Not allowed**: the contract limits it to US CPI (2.9%) |
| D | NX-S07 Espacios Turia | +2% | Below threshold. Still **not allowed**, because the price is fixed; its contract also triggers an expiry alert |

---

## Thresholds and alerts

| Type | Rule |
|---|---|
| Price increase, any category | More than 3% versus the previous month |
| Contract expiry | 90 and 30 days before |
| Notice deadline | 15 days before |

Alerts go to Javier Almeida.

Scenario D is intentional: a small increase that doesn't trigger the price alert is still an increase the contract doesn't allow. The system must catch it when evaluating the contract, even if the threshold doesn't.

---

## Approvals

| Situation | Approved by |
|---|---|
| Any communication to a supplier | Javier Almeida |
| Communication about a contract with an annual value above EUR 150,000 (or its USD equivalent) | Javier Almeida **and** Laura Mendoza |

---

## Questions the system must be able to answer

- "Can JobReach Pro raise our price by 8%?"
- "How much does VoxCloud's increase cost us per year?"
- "Until when can we cancel JobReach Pro without being locked in for another year?"
- "What alternative do we have to AssessPro, and at what price?"
- "Can we exit the AssessPro contract early?" → the system must answer that the contract has no early exit clause.
- "Can Espacios Turia raise our price?"
- "Prepare a summary to renegotiate with JobReach Pro."

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Supplier bank details included in the contracts
- Personal data of supplier contact people

The test contracts must include this data in a billing clause, so you can verify the system doesn't propagate it.

---

## Specific restriction

No brief and no supplier communication may include Nexova candidate or client data: no names, no client companies, no usage volumes per client. If a request tries to include it, the system must exclude that data and state that it has done so.
