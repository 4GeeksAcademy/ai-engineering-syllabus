# Riverside Community Theater — Weekly Box Office Close (Class Example)

> **For instructors:** Live-demo brief for `ai-eng-financial-close`. Same spine (ingest with `source_ref`, deterministic calc tools for totals / actual vs budget / deviations, single agent that interprets but does not invent arithmetic, declare missing data, human approval before distribution, agent audit identity + redaction). Different domain: community theater weekly box office and house costs, not corporate monthly close. Scope: ~60–90 minutes. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Riverside Community Theater** closes the box office every Monday for the prior week. Staff paste ticket CSV exports and a tiny budget sheet into email. Numbers disagree; explanations are guesswork. You will demo a **single closing agent with tools** that builds a one-page weekly report, flags deviations over a fixed threshold, and **cannot distribute** until the house manager approves.

### Scope note

| Graded project (`ai-eng-financial-close`) | This class example                                       |
| ----------------------------------------- | -------------------------------------------------------- |
| Full company briefing (multi-country, FX) | 1 venue, 1 currency (USD), fixed 10% deviation threshold |
| Multiple source files + ops metrics       | 2 CSVs: `tickets.csv`, `budget.csv`                      |
| Scheduled background close                | Manual “run close for week W” is enough                  |
| Multi-recipient distribution              | Single reviewer: `house_manager`; recipients = board CC  |
| Full privacy suite                        | Log `agent_id`; redact `patron_email` only               |

---

## What to build

### 1. Tiny dataset (week `2026-W12`)

`tickets.csv` (actuals — one row per show night):

| entry_id | date       | show          | category    | amount | source_ref                |
| -------- | ---------- | ------------- | ----------- | ------ | ------------------------- |
| T-01     | 2026-03-16 | Our Town      | box_office  | 4200   | tickets:T-01              |
| T-02     | 2026-03-17 | Our Town      | box_office  | 3800   | tickets:T-02              |
| T-03     | 2026-03-18 | Our Town      | concessions | 900    | tickets:T-03              |
| T-04     | 2026-03-19 | Our Town      | box_office  | null   | tickets:T-04 (incomplete) |
| T-05     | 2026-03-20 | Rentals: hall | rental      | 1500   | tickets:T-05              |

`budget.csv`:

| week     | category    | amount |
| -------- | ----------- | ------ |
| 2026-W12 | box_office  | 9000   |
| 2026-W12 | concessions | 800    |
| 2026-W12 | rental      | 1200   |

- [ ] Ingest both files; keep `source_ref` on every figure
- [ ] Flag `T-04` as `uncertain` / incomplete — do not invent 0 or fill by eye

### 2. Deterministic calc tools

- [ ] `sum_by_category(rows)` → totals with `source_refs[]`
- [ ] `actual_vs_budget(actual, budget)` → absolute + `%` deviation
- [ ] `flag_above_threshold(deviations, 10)` → categories that breach
- [ ] Unit tests: same inputs → same outputs; known totals match by hand

### 3. Closing agent

- [ ] Call tools; model writes hypotheses only from tool results + cited refs
- [ ] Report sections: totals by category, deviations ≥ 10%, incomplete list
- [ ] For `box_office`: incomplete night stated; do not claim a full-week actual

### 4. Human approval + audit

- [ ] Draft report allowed; distribute blocked until role `house_manager` approves
- [ ] Rejection with comment → new version that addresses the comment
- [ ] Log actions with `agent_id=close_agent`; never log `patron_email`

---

## Verify together

- [ ] Concessions deviation = `(900 - 800) / 800 = +12.5%` → flagged; figure from tool, not model
- [ ] Box office: incomplete declared; no fake Thursday total
- [ ] Attempt distribute without house manager → blocked
- [ ] Re-run same week → identical non-hypothesis figures
- [ ] Show one audit line; no `patron_email` in logs

---

## Discussion questions

1. Why is a convincing wrong sum worse than an obvious missing figure in a close report?
2. Where does the agent’s job end and the calc tool’s job begin?
3. What should happen when the reviewer rejects with “explain rental spike”?
