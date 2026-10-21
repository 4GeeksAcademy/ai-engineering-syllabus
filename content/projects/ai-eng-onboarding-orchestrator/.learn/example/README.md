# Northside Makerspace — Safety Orientation Orchestrator (Class Example)

> **For instructors:** Live-demo brief for `ai-eng-onboarding-orchestrator`. Same spine (explicit stage graph, single LangGraph agent, checkpointer resume, comprehension gates, official-doc lookup with no hallucination, human approval interrupt, overdue escalation, agent audit identity). Different domain: makerspace safety orientation, not corporate People onboarding. Scope: ~60–90 minutes. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Northside Makerspace** lets new members use power tools only after a short safety orientation. Today the desk hands out a PDF and hopes for the best. You will demo a **single stateful agent** that walks a new member through a tiny stage graph, pauses for a shop mentor approval, answers only from a small official handbook, and survives a process restart mid-flow.

### Scope note

| Graded project (`ai-eng-onboarding-orchestrator`)                   | This class example                                |
| ------------------------------------------------------------------- | ------------------------------------------------- |
| Full company briefing stages (days/weeks, multi-country, contracts) | 4 stages, ~3 business-day toy deadlines           |
| Full RAG index over official onboarding corpus                      | 1 markdown handbook + keyword/vector stub         |
| People + new-hire production views                                  | Print/JSON progress dump is enough                |
| Durable DB checkpointer                                             | `MemorySaver` (or sqlite) is enough               |
| Full reminder/escalation productization                             | One reminder function + one overdue escalate stub |
| Sensitive employment documents                                      | Redact `member_phone` only                        |

---

## What to build

### 1. Stage graph

| #   | Stage                     | Exit condition                            | Deadline | Approver            |
| --- | ------------------------- | ----------------------------------------- | -------- | ------------------- |
| 1   | Welcome + waiver received | Staff marks waiver received               | Day 1    | Staff (manual flag) |
| 2   | Shop rules                | Comprehension check passed                | Day 2    | Automatic           |
| 3   | Tool safety               | Check passed **and** shop mentor approval | Day 3    | Shop mentor         |
| 4   | Closed                    | Agent marks orientation complete          | Day 3    | Automatic           |

- [ ] Model stages as an explicit graph (nodes + edges), not an if/else spaghetti script
- [ ] Content stages cannot advance without a passed check

### 2. Single agent + checkpointer

- [ ] One compiled LangGraph (or equivalent) orchestrator — justify “one agent” verbally
- [ ] Persist state with a checkpointer keyed by `member_id` / `thread_id`
- [ ] Demo: kill the process mid-stage 2 → restart → resume at stage 2

### 3. Official handbook lookup

Provide a tiny corpus, e.g.:

```text
# Northside Safety Handbook (excerpt)
- Eye protection required in the wood shop at all times.
- Never leave a running saw unattended.
- Report injuries to the desk before leaving the building.
```

- [ ] Tool answers only from this material and cites the line/section
- [ ] Question outside the handbook → “not in official material” + route to desk staff (no invented rules)

### 4. Human approval interrupt

- [ ] Stage 3 pauses until a user with role `shop_mentor` submits approve/reject
- [ ] Reject returns to stage 2 (re-check) — say so in the graph

### 5. Overdue stub + audit

- [ ] If stage 2 past deadline → escalate to `shop_mentor` (log or print is fine)
- [ ] Log actions with `actor_type=agent`; never log `member_phone`

---

## Verify together

- [ ] Fail a check on purpose → content reinforced → cannot skip to next stage
- [ ] Ask “Can I bring my own laser cutter?” → routed, not invented
- [ ] Restart mid-flow → same stage
- [ ] Mentor without role `shop_mentor` cannot approve
- [ ] Show one audit line with agent identity and no phone number

---

## Discussion questions

1. Why is a single long-running orchestrator a better fit here than three specialized agents (content, Q&A, approvals)?
2. What breaks if “opened the handbook” counts as stage completion instead of a comprehension check?
3. Where would you store sensitive fields so the checkpointer and LLM prompts never see them?
