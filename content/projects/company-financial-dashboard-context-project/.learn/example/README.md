# In-Class Example: Understanding a Library Catalog App

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain is a community library catalog app instead of a financial dashboard — same workflow of coding-agent investigation, verified understanding, engineering rules, and memory bank documentation, but scoped to a smaller, more familiar codebase.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same agent-first workflow as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.

You just joined a small team maintaining a community library catalog app. There is a frontend and a backend, but the handover was rushed: few docs, no coding standards written down, and no notes about what is finished or broken. You do **not** need prior stack knowledge. Your job is to drive a coding agent to understand what exists, derive rules from repo evidence, and leave a memory bank any future contributor (or agent) can rely on.

---

## Concepts Covered

| Concept                            | Where it applies                                                         |
| ---------------------------------- | ------------------------------------------------------------------------ |
| Agent-first codebase exploration   | Phase 1: ask, verify, correct the project summary                        |
| Evidence-based engineering findings| Phase 2: conventions and risks from the repo (not personal checklists)   |
| Repository rules (`.agents/rules`) | Phase 3: agent drafts rules; student tests them on a real task           |
| Memory bank documentation          | Phase 4: product, stack, status — agent drafts, student verifies         |
| Commit discipline                  | One commit per phase, no bundled mega-commits                            |

---

## Starting Point

Use a local example project folder with this minimal structure:

```
library-catalog/
├── frontend/
├── backend/
├── docker-compose.yml
└── README.md         ← minimal, unhelpful
```

Do **not** tell students fixed ports or frameworks up front. Ask the agent to discover how to run the app from repo evidence.

---

## What to Do

### Phase 1 — Understand the handover (with the agent)

- [ ] Ask the agent how to bring services up and how to confirm they are healthy; follow repo evidence
- [ ] Ask: _"Summarize this project: what does it do, how is it structured, how do I run it, and what is the tech stack? Cite paths."_
- [ ] Mark major claims ✅ / ❌ / ❓ against real files; correct inaccuracies with the agent
- [ ] Leave a short verification trail (commit message or `verification.md`)
- [ ] Commit: `"Phase 1: AI project summary and validation"`

### Phase 2 — Derive engineering findings (with the agent)

- [ ] Ask the agent for useful conventions and risky patterns that would hurt future agent edits
- [ ] Keep only findings tied to concrete files/behaviors; group by category
- [ ] Turn findings into proposed rules — each rule cites at least one repo fact
- [ ] Commit: `"Phase 2: engineering findings and proposed rules"`

### Phase 3 — Write and test repository rules

- [ ] Create the `.agents/rules/` directory
- [ ] Have the agent draft at least **2** rule files (e.g. frontend-scoped and backend-scoped). Each should include:
  - **Objective:** what the rule enforces
  - **Rationale:** why it matters for this project
  - **Examples:** one correct and one incorrect pattern from the actual codebase
- [ ] Test each rule: give the agent a small real task and check whether the rules steer the work; refine if not
- [ ] Commit: `"Phase 3: repository rules in .agents/rules"`

### Phase 4 — Build the memory bank

- [ ] Create a `memory-bank/` folder at the repository root
- [ ] Have the agent draft documents covering at least:
  - Product overview — what the app does, who uses it, key features
  - Tech stack — languages, frameworks, database, key dependencies
  - Current status — what works, what is incomplete, suggested next priorities
- [ ] Verify claims against the repo before committing
- [ ] Commit: `"Phase 4: memory bank — product, tech stack, and status"`

---

## Discussion Questions

1. When you asked the agent to summarize the project, did it get anything wrong? What does that tell you about trusting AI-generated documentation without verification?
2. What is the difference between a "rule" that is too generic (e.g., "write clean code") and one that is actionable for this specific project?
3. Why is it important to commit each phase separately instead of doing one large commit at the end?
4. Who should invent best practices here — the student from memory, or the student+agent from codebase evidence?
