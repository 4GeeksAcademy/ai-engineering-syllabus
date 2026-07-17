# Maple Street Library — Grant Response Generation & Evaluation (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-agentic-workflows-evaluate`. Same spine (per-department generators, parallel evaluators, bounded generator-evaluator loop, ticket status). Continues Maple Street grant desk from Part 1 class example. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

Part 1 already told the grants desk **what** Programs, Facilities, and Finance must answer. Now: draft each section automatically, then **self-evaluate** (readability, relevance, library guidelines) before a human sees it. Failures bounce back to the generator with concrete feedback — up to a hard iteration limit.

### Scope note

| Graded project (`ai-eng-milestone-agentic-workflows-evaluate`) | This class example                       |
| -------------------------------------------------------------- | ---------------------------------------- |
| Company monorepo + CONTEXT guideline rules                     | Maple Street grant desk only             |
| Full Part 1 pipeline reuse                                     | Fixture Part 1 synthesizer JSON          |
| Parallel readability / relevance / guidelines evaluators       | Three stub evaluators + fixed rules list |
| Full ticket UI updates                                         | JSON ticket status transitions           |
| Company PR with pass + fail section examples                   | Live demo + 5 automated tests            |

---

## Teaching spine (must hit live)

1. **Assignment orchestrator** maps Part 1 workstreams → department generators
2. **One generator per department** drafts its pricing/grant section
3. **Parallel evaluators** on each draft: readability, relevance, guidelines
4. **Fail → regenerate** with structured feedback (not free-form vibes)
5. **Iteration limit** — ticket stays alive; section marked `needs_human_review` if exhausted
6. **Synthesizer / handoff** packages content + eval results per department
7. Ticket states: `drafting` → `under_evaluation` → ready for Part 3

![Departmental mapping and deliverable finalization](../departmental-mapping-deliverable-finalization.jpg)

---

## Seed guidelines (indicative — not CONTEXT)

```text
[G1] Every section must name a dollar amount or "TBD with Finance".
[G2] No promises of Sunday opening without Facilities sign-off.
[G3] Tone: plain language; Flesch grade ≤ 10 for public-facing sections.
[G4] Must answer the applicant's stated ask (story hours / room / funds).
```

---

## What to build

### 1. Generators

- [ ] Programs / Facilities / Finance generators; input = Part 1 workstream summary
- [ ] Structured draft output per department

### 2. Evaluators (parallel)

- [ ] Readability → pass/fail + score
- [ ] Relevance → pass/fail + missing asks
- [ ] Guidelines → pass/fail + rule ids failed (`G1`…)

### 3. Loop

- [ ] Any fail → regenerate with evaluator feedback payload
- [ ] Cap e.g. `max_iterations=3`; then `needs_human_review`

### 4. Tests (`tests/test_grant_evaluate.py`)

| #   | Scenario                              | Expect                                                 |
| --- | ------------------------------------- | ------------------------------------------------------ |
| 1   | Clean draft                           | All evaluators pass; handoff includes content + scores |
| 2   | Missing dollar amount                 | Guidelines fail → regenerate → pass or hit limit       |
| 3   | Irrelevant about Sunday hours         | Guidelines `G2` fail with specific feedback            |
| 4   | Iteration limit hit                   | Ticket not discarded; section flagged for human        |
| 5   | Generator + one evaluator unit-tested | Mocks only                                             |

---

## Verify together

- [ ] Departments draft in parallel without blocking each other
- [ ] Feedback names the rule / missing ask (not “improve quality”)
- [ ] Ticket status flips through drafting / under_evaluation
- [ ] Handoff JSON has content **and** evaluation result per department

---

## Discussion questions

1. Why structured evaluator output beats a single “score: 7/10” string?
2. How do parallel evaluators write results without clobbering shared state?
3. Iteration limit exhausted: discard section, escalate, or ship with warning?
