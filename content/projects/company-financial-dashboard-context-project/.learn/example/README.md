# In-Class Example: Understanding a Library Catalog App

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain is a community library catalog app instead of a financial dashboard — same workflow of AI-assisted codebase understanding, engineering rules, and memory bank documentation, but scoped to a smaller, more familiar codebase.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


You just joined a small team maintaining a community library catalog app. There is a React frontend and a FastAPI backend, but the handover was rushed: there are no docs, no coding standards written down, and no notes about what is finished or broken. Your job is to use your AI coding assistant to understand what exists, define rules to keep it maintainable, and leave behind a memory bank that any future contributor can rely on.

---

## Concepts Covered

| Concept | Where it applies |
|---|---|
| AI-assisted codebase exploration | Phase 1: generating and validating a project summary |
| Engineering practice analysis | Phase 2: identifying good and bad patterns |
| Repository rules (`.agents/rules`) | Phase 3: writing actionable governance files |
| Memory bank documentation | Phase 4: product overview, tech stack, current status |
| Commit discipline | One commit per phase, no bundled mega-commits |

---

## Starting Repository

Use this fictional repository as your starting point (your instructor will share the real link):

```
https://github.com/4GeeksAcademy/ai-eng-library-catalog-context-example
```

Expected structure after cloning:

```
library-catalog/
├── frontend/         ← React (Vite)
├── backend/          ← FastAPI + SQLite
├── docker-compose.yml
└── README.md         ← minimal, unhelpful
```

---

## What to Do

### Phase 1 — Understand the handover

- [ ] Fork and clone the repository
- [ ] Run `docker compose up` and verify the app loads at `http://localhost:5173` and API docs at `http://localhost:8000/docs`
- [ ] Ask your AI assistant: *"Summarize this project: what does it do, how is it structured, and what is the tech stack?"*
- [ ] Read the generated summary and check it against what you actually see in the code — correct any inaccuracies
- [ ] Commit: `"Phase 1: AI project summary and validation"`

### Phase 2 — Analyze engineering practices

- [ ] Review the frontend and backend code and identify:
  - At least **3 good practices** (e.g., clear component separation, consistent naming)
  - At least **3 risky or bad practices** (e.g., missing error handling, hardcoded values, no tests)
- [ ] Group findings by category:

| Category | Finding | Good / Bad |
|---|---|---|
| Error handling | No try/catch on fetch calls | Bad |
| Naming | Components use PascalCase consistently | Good |
| ... | ... | ... |

- [ ] Commit: `"Phase 2: engineering practice analysis"`

### Phase 3 — Write repository rules

- [ ] Create the `.agents/rules/` directory
- [ ] Write at least **2 rule files** — one for the frontend, one for the backend. Each rule file must include:
  - **Objective:** what the rule enforces
  - **Rationale:** why it matters for this project
  - **Examples:** one correct and one incorrect pattern from the actual codebase
- [ ] Test each rule: ask your AI assistant to apply it and verify the guidance makes sense
- [ ] Commit: `"Phase 3: repository rules in .agents/rules"`

### Phase 4 — Build the memory bank

- [ ] Create a `memory-bank/` folder at the repository root
- [ ] Add three documents:
  - `product.md` — what the app does, who uses it, key features
  - `tech-stack.md` — frontend framework, backend framework, database, key dependencies and their versions
  - `status.md` — what is working, what is incomplete or broken, suggested next priorities
- [ ] Commit: `"Phase 4: memory bank — product, tech stack, and status"`

---

## Discussion Questions

1. When you asked the AI to summarize the project, did it get anything wrong? What does that tell you about trusting AI-generated documentation without verification?
2. What is the difference between a "rule" that is too generic (e.g., "write clean code") and one that is actionable for this specific project?
3. Why is it important to commit each phase separately instead of doing one large commit at the end?
