# Cooking School Platform — AI-Driven Monorepo Setup (In-Class Example)

> **Instructor note:** Simplified in-class example for the "AI-Driven Engineering" module. Use this scenario to introduce the memory bank pattern, `AGENTS.md`, agent rules, and skills in a small monorepo — completable in 1–2 hours. The official student project in the project root applies the same patterns at full scope with the student's assigned company from `CONTEXT.md`.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.

You're starting the digital platform for **Masa & Fuego**, a local cooking school. The repo is a fresh template — no application code yet. Before adding features, your tech lead wants the repo to be **AI-ready**: the coding agent must have persistent context, a defined workflow, and at least one reusable skill.

> _"Right now if I hand this repo to the agent it has no idea what we're building or how we work. Let's fix that before we go further."_  
> — Tech lead

---

## Core Concepts

| Concept         | What it is                                                  | Where it lives                   |
| --------------- | ----------------------------------------------------------- | -------------------------------- |
| **Memory bank** | Markdown files the agent reads at the start of each session | `memory-bank/`                   |
| **AGENTS.md**   | Workflow rules the agent must follow before committing      | repo root                        |
| **Rules**       | Scoped instructions for specific situations                 | `.agents/rules/`                 |
| **Skill**       | A reusable, structured task with verifiable output          | `.agents/skills/<name>/SKILL.md` |

---

## What You Need to Do

### Step 1 — Create the memory bank

Create a `memory-bank/` folder at the repo root with two files:

- [ ] **`projectbrief.md`** — Answer: What is Masa & Fuego? Who uses this platform? What problem does it solve? What are the two main parts (public site + backoffice)?
- [ ] **`techContext.md`** — Answer: What stack will you use? What are the current constraints (e.g., no database yet, greenfield project)? What folders exist in the monorepo template?

> The memory bank is **living documentation** — it must be updated every time a significant decision is made or a new feature is added. An outdated memory bank is worse than no memory bank.

### Step 2 — Write `AGENTS.md`

Create `AGENTS.md` at the repo root. It must define:

- [ ] Which memory bank files the agent reads at the start of each session (list them explicitly).
- [ ] A mandatory **pre-commit workflow** with at least 4 ordered steps. Example structure:
  1. Read memory bank files.
  2. Check that changed files follow the naming convention.
  3. Run the project's lint or validation command.
  4. Update `memory-bank/progress.md` with the change made.
- [ ] At least one folder the agent **must not modify** without developer confirmation (e.g., `memory-bank/techContext.md` — architectural decisions require human sign-off).

### Step 3 — Add a rule

Create `.agents/rules/no-hardcoded-copy.md` with:

- [ ] Scope: applies to UI/view files in `uis/` (define the file patterns your stack uses).
- [ ] Rule: business copy (headlines, course names, prices) must live in a dedicated content file or constants module — not scattered inline in view code.
- [ ] Rationale: explain in one sentence why this rule exists.

### Step 4 — Create a skill

Create `.agents/skills/add-page-section/SKILL.md` for a recurring task: adding a new section to the public website.

- [ ] **Objective:** A single sentence — what does this skill do?
- [ ] **Inputs:** What does the agent need to know before starting? (e.g., section title, content, position in the page)
- [ ] **Steps:** Numbered list of actions the agent takes.
- [ ] **Acceptance criteria:** At least 3 verifiable conditions (e.g., _"The section appears in the correct position when running the project's dev command"_).

### Step 5 — Bootstrap the application structure

- [ ] Create `uis/website/` — public-facing app for the cooking school.
  - [ ] Route `/` renders a simple homepage (school name, tagline, one section placeholder).
- [ ] Create `uis/backoffice/` — internal app for staff use.
  - [ ] Route `/` renders a basic dashboard shell (heading + placeholder content).
  - [ ] At least one piece of company-relevant data (e.g., course pricing or schedule from your memory bank) visible on screen — not only in the console.

> Both apps must start without errors using the project's dev command.

---

## Expected Repo Structure

```
.
├── AGENTS.md
├── memory-bank/
│   ├── projectbrief.md
│   └── techContext.md
├── .agents/
│   ├── rules/
│   │   └── no-hardcoded-copy.md
│   └── skills/
│       └── add-page-section/
│           └── SKILL.md
└── uis/
    ├── website/        ← public site
    └── backoffice/     ← internal app
```

---

## Checklist

- [ ] `memory-bank/projectbrief.md` describes both business and technical context (not just one).
- [ ] `AGENTS.md` specifies at least 4 ordered pre-commit steps.
- [ ] `.agents/rules/no-hardcoded-copy.md` has an explicit scope and rationale.
- [ ] `.agents/skills/add-page-section/SKILL.md` has objective, inputs, steps, and acceptance criteria.
- [ ] `uis/website/` starts without errors and renders a homepage at `/`.
- [ ] `uis/backoffice/` starts without errors and shows company-relevant content on screen.

---

## Discussion Questions

1. What is the difference between `AGENTS.md` (a rule) and a skill? When would you use one vs. the other?
2. Why should architectural decisions in `techContext.md` require human confirmation before the agent modifies them?
3. Write one more acceptance criterion for the `add-page-section` skill that verifies the agent didn't break existing sections.
