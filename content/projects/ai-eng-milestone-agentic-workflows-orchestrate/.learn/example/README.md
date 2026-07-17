# Maple Street Library — RFP Intake & Orchestration (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-agentic-workflows-orchestrate`. Same spine (PDF → Markdown, classifier gate, orchestrator-worker-synthesizer, ticket lifecycle). Different domain than company CONTEXT agents. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** receives municipal grant applications (PDF) from neighborhood groups asking for funding for reading programs. The grants desk is drowning: every application needs input from **Programs**, **Facilities**, and **Finance** — and nobody can tell, from a quick read, who must answer what.

In one session: build the **first stretch** of an agentic workflow that receives these PDFs, decides whether they are real grant applications, and splits analysis across department workers before a synthesizer hands Sales a routing summary.

### Scope note

| Graded project (`ai-eng-milestone-agentic-workflows-orchestrate`) | This class example                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| Company monorepo + CONTEXT departments / RFP format               | Maple Street grant desk only                                        |
| Full `uis/backoffice` ticket UI                                   | CLI upload + JSON status file                                       |
| MarkItDown + py-readability-metrics in Docker services            | Stub converter + fixed readability fixture                          |
| Full LangGraph + MCP stack from Milestone 8                       | Minimal pipeline: classifier → orchestrator → workers → synthesizer |
| Company-specific PR + sample RFP                                  | Live demo + 5 automated tests                                       |

---

## Teaching spine (must hit live)

1. **Ticket lifecycle** — `analyzing` → `waiting_for_approval` / `done` / `discarded`
2. **PDF → Markdown** before any LLM call (token cost lesson)
3. **Classifier gate** — non-grant PDF stops pipeline; ticket = `discarded`
4. **Metadata + readability** stored per document (processing cost estimate)
5. **Orchestrator** decomposes document into per-department workstreams
6. **Workers** run in parallel; each returns department-specific aspects + contact hint
7. **Synthesizer** merges into one Sales-facing summary (no monolithic single agent)

![Initial analysis and workstream isolation](../rfp-intake-workstream-isolation.jpg)

---

## Seed departments (indicative)

| Department | Worker responsibility                                 |
| ---------- | ----------------------------------------------------- |
| Programs   | Curriculum fit, audience, schedule conflicts          |
| Facilities | Room capacity, ADA access, after-hours constraints    |
| Finance    | Budget line items, matching funds, payment milestones |

Sample grant snippet (Markdown after conversion):

```markdown
# Neighborhood Reading Circle — Grant Application 2026

Applicant: Riverside Community Association
Requested amount: $12,400
Programs: weekly story hours for ages 6–10, summer reading kickoff
Facilities: needs Meeting Room B Saturday mornings; wheelchair ramp noted
Finance: 60% upfront, 40% on attendance report; requires 501(c)(3) letter
```

Non-grant counterexample: a restaurant menu PDF → classifier → `discarded`.

---

## What to build

### 1. Intake + ticket state

- [ ] CLI or minimal endpoint: upload PDF path → create ticket id + status `analyzing`
- [ ] Persist status transitions in JSON or sqlite stub

### 2. Ingestion

- [ ] Convert PDF to Markdown (stub OK if instructor provides `.md` sidecar)
- [ ] Extract metadata: applicant, date, departments mentioned
- [ ] Attach readability score (fixture or real `py-readability-metrics`)

### 3. Classifier agent

- [ ] Output: `{ "is_grant_application": bool, "confidence": float, "reason": str }`
- [ ] If false → ticket `discarded`; do not invoke orchestrator

### 4. Orchestrator-worker-synthesizer

- [ ] Orchestrator emits work items: `[{ "department": "Programs", "sections": [...] }, ...]`
- [ ] One worker per department; structured output per worker
- [ ] Synthesizer produces final routing table for the grants desk

### 5. Tests (`tests/test_grant_orchestration.py`)

| #   | Scenario                                         | Expect                                       |
| --- | ------------------------------------------------ | -------------------------------------------- |
| 1   | Valid grant PDF                                  | Status `done`; synthesizer has 3 departments |
| 2   | Menu PDF                                         | Status `discarded`; no worker calls          |
| 3   | Grant missing Finance section                    | Finance worker returns "not mentioned"       |
| 4   | Orchestrator output                              | ≥2 parallel work items                       |
| 5   | Classifier + one worker unit-tested in isolation | Mocks only; no live LLM required             |

---

## Verify together

- [ ] Ticket status matches pipeline stage at each step
- [ ] Classifier rejection does not crash the system
- [ ] Workers receive scoped context (not always full doc — discuss trade-off)
- [ ] Synthesizer output readable without opening original PDF
- [ ] Diagram pattern visible in code structure (separate modules/agents)

---

## Discussion questions

1. Why convert PDF → Markdown before the classifier instead of after?
2. When should the orchestrator pass full document vs. section slices to workers?
3. What happens if Programs and Finance contradict each other on budget — who wins in the synthesizer?
4. How does ticket mode differ from a fire-and-forget background job?
