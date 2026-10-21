# Harbor City Library — Vendor Price & Contract Desk (Class Example)

> **For instructors:** Live-demo brief for `ai-eng-supplier-contracts`. Same spine (supervisor + pricing/contracts specialists, traceable sources and clause/page cites, deterministic calc tools, consultation budget, human approval before vendor messages, per-agent audit identity). Different domain: public-library print/ebook vendors, not corporate carrier or packaging suppliers. Scope: ~60–90 minutes. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Harbor City Library** buys print and ebook packages from a handful of vendors. Price bumps show up on the invoice; renewal clauses live in scattered PDFs. You will demo a **supervisor + two specialists** that detect a price jump, check whether the contract allows it, compute impact with code (not the LLM), and draft a vendor email that **cannot send** until the acquisitions librarian approves.

### Scope note

| Graded project (`ai-eng-supplier-contracts`)     | This class example                                    |
| ------------------------------------------------ | ----------------------------------------------------- |
| Full company briefing (multi-supplier, FX, etc.) | 3 vendors, 1 currency (USD), fixed 8% alert threshold |
| Full PDF pipeline + confidence flags             | 1 short markdown “contract” per vendor + page labels  |
| Full renegotiation product brief                 | One merged JSON/markdown brief is enough              |
| Multi-role approval matrix                       | Single approver: `acquisitions_librarian`             |
| Production audit/privacy suite                   | Log `agent_id`; redact `vendor_bank_iban` only        |

---

## What to build

### 1. Tiny dataset

| Vendor ID | Category | Old unit price | New unit price | Volume / month |
| --------- | -------- | -------------- | -------------- | -------------- |
| HCL-V01   | Print    | 12.00          | 13.50          | 400            |
| HCL-V02   | Print    | 11.80          | 11.80          | 200            |
| HCL-V03   | Ebook    | 4.00           | 4.10           | 1000           |

Toy contract excerpt for `HCL-V01` (treat as page 3, clause `B.2`):

```text
Price revisions may not exceed 8% within a calendar year without 30 days written notice.
Either party may exit with 45 days notice; early exit fee = 1 month of average spend.
```

- [ ] Ingest prices with `source_ref` (e.g. `price_history:HCL-V01:2026-04-01`)
- [ ] Store clause text with `clause_id` + `page`

### 2. Pricing specialist

- [ ] Detect increases where `delta_pct >= 8`
- [ ] `impact = volume * (new - old)` as a **pure function** with a unit test
- [ ] Compare against peers in the same category (print vs ebook)

### 3. Contracts specialist

- [ ] Answer: does `HCL-V01`’s jump fit clause `B.2`? Cite page + clause
- [ ] If written notice is not in the toy data → return `missing`, do not invent it
- [ ] Stub: alert if renew/exit notice window is within 14 days (hard-coded toy date OK)

### 4. Supervisor

- [ ] On threshold hit: call pricing **and** contracts, merge one response
- [ ] Cap specialist calls (e.g. ≤ 4) per request
- [ ] On request: produce a short renegotiation brief (history, peer, impact, leverage)

### 5. Human approval + audit

- [ ] Draft vendor email allowed; send blocked until role `acquisitions_librarian` approves
- [ ] Log actions with `agent_id` (`supervisor` / `pricing` / `contracts`)
- [ ] Never log `vendor_bank_iban`

---

## Verify together

- [ ] `HCL-V01` alerts; `HCL-V03` does not (under 8%)
- [ ] Impact for V01 = `400 * 1.50 = 600` from the calc tool, not the model
- [ ] Contracts answer cites `B.2` / page 3; missing notice stated explicitly
- [ ] Attempt send without librarian role → blocked
- [ ] Show one audit line per agent; no IBAN in logs

---

## Discussion questions

1. Why split pricing vs contracts into specialists instead of one agent with every tool?
2. What fails if the LLM “estimates” impact when volume is missing?
3. Where should the consultation budget live — supervisor policy, graph edge limit, or both?
