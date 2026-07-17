# Maple Street Library Desk Agent — Memory & Self-Improvement (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-agentic-engineering`. Same spine (explicit memory interface, structured `memory_proposal`, in-conversation propose → classified confirm → audit → consolidate). Different domain than company CONTEXT agents. Continues Maple Street Library narrative from the harness class example. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** desk agent already answers FAQ (hours, loans, fines) and refuses jailbreaks. Problem: every shift starts cold — desk staff re-explain that “large-print holds go to the yellow shelf” three times a week.

In one session: add a **tiny propose–confirm–remember** loop so corrected desk facts persist only when a human says yes.

### Scope note

| Graded project (`ai-eng-milestone-agentic-engineering`) | This class example                                      |
| ------------------------------------------------------- | ------------------------------------------------------- |
| Company monorepo + CONTEXT memory rules                 | Maple Street desk only                                  |
| Redis / VectorDB / hybrid justified from CONTEXT        | In-memory dict + optional JSON file                     |
| Full LangGraph + MCP + guardrails stack                 | Stub agent: FAQ retrieve + memory hooks                 |
| Company never-store list                                | Never store: patron phone numbers, overdue amounts owed |
| Full PR + two company evidence cycles                   | Live demo + 4 automated tests                           |

---

## Teaching spine (must hit live)

1. Explicit `read` / `write` memory API (not “stuff the system prompt”)
2. Structured turn output: `reply` + optional `memory_proposal`
3. Propose inside the same reply; **no write yet**
4. One pending proposal; silence/topic-change = reject
5. Intent classify confirm (approve / reject / unclear) — not `"yes" in text`
6. Audit log for both approve and reject
7. Tiny consolidation (e.g. max 20 entries or overwrite same `key`)

---

## Seed desk facts (indicative)

```text
[FAQ] Loan period: 21 days. Renewals: once if no holds.
[FAQ] Desk hours: Mon–Sat 09:00–20:00.
[CORRECTABLE] Large-print holds: staff say "yellow shelf" but FAQ still says "reserve desk".
```

Never-store: patron phone, exact fine balance for a named patron.

---

## What to build

### 1. Memory interface

- [ ] `memory.read(query)` / `memory.write(key, fact)` / `memory.list()`
- [ ] Backed by dict (or JSON file); document why KV is enough for desk corrections

### 2. Self-evaluation + proposal

- [ ] Structured output per turn; most turns → `memory_proposal: null`
- [ ] When staff corrects “large-print holds go to yellow shelf” → propose in reply
- [ ] Document 3 non-memorable turns (thanks, “what time do you close?”, one-off summary)

### 3. Confirm + audit

- [ ] While pending: classify next user message first
- [ ] Approve → write; reject/unclear → discard; both audited
- [ ] Block a second proposal until the first closes

### 4. Consolidation

- [ ] Same `key` overwrites; or hard cap (e.g. 20) dropping oldest
- [ ] Refuse writes that look like phone numbers / fine balances even if “approved”

### 5. Tests (`tests/test_desk_memory.py`)

| #   | Scenario                                                             | Expect                             |
| --- | -------------------------------------------------------------------- | ---------------------------------- |
| 1   | Correction → proposal → clear approve → later ask about yellow shelf | Fact used; audit `approve`         |
| 2   | Proposal → “tell me the weather” / unclear                           | No write; audit reject/discard     |
| 3   | Non-memorable “thanks”                                               | `memory_proposal` null             |
| 4   | User “approves” storing a patron phone                               | Write refused; never-store honored |

---

## Verify together

- [ ] In-domain FAQ still works without proposing every turn
- [ ] Approve cycle: second turn uses remembered yellow-shelf fact
- [ ] Reject cycle: store unchanged
- [ ] Pending blocks a second proposal
- [ ] Audit shows both outcomes

---

## Discussion questions

1. Why write-on-self-eval is worse than propose–confirm once memory is persistent?
2. When is a VectorDB unnecessary for “desk corrections,” and when would you add it?
3. How does the prior harness (never treat RAG as system) interact with memory poisoning attempts?
