# Cooking School Platform — AI-Driven Monorepo Setup (In-Class Example)

> **Instructor note:** This is a simplified in-class example for the "AI-Driven Engineering" milestone. Use this scenario to introduce the memory bank pattern, `AGENTS.md`, agent rules, and skills in the context of a small monorepo — completable in 1–2 hours. The original project applies the same concepts to a larger multi-company monorepo with more milestones of accumulated code.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


You're working on the digital platform for **Masa & Fuego**, a local cooking school. The repo already has a landing page (HTML) and some pricing logic (TypeScript). Before adding more features, your tech lead wants the repo to be **AI-ready**: the coding agent must have persistent context, a defined workflow, and at least one reusable skill.

> *"Right now if I hand this repo to the agent it has no idea what we're building or how we work. Let's fix that before we go further."*  
> — Tech lead

---

## Core Concepts

| Concept | What it is | Where it lives |
|---------|-----------|----------------|
| **Memory bank** | Markdown files the agent reads at the start of each session | `memory-bank/` |
| **AGENTS.md** | Workflow rules the agent must follow before committing | repo root |
| **Rules** | Scoped instructions for specific situations | `.agents/rules/` |
| **Skill** | A reusable, structured task with verifiable output | `.agents/skills/<name>/SKILL.md` |

---

## What You Need to Do

### Step 1 — Create the memory bank

Create a `memory-bank/` folder at the repo root with two files:

- [ ] **`projectbrief.md`** — Answer: What is Masa & Fuego? Who uses this platform? What problem does it solve? What are the two main parts (public site + backoffice)?
- [ ] **`techContext.md`** — Answer: What is the tech stack? What has already been built? What are the current constraints (e.g., no database yet, TypeScript only for pricing logic)?

> The memory bank is **living documentation** — it must be updated every time a significant decision is made or a new feature is added. An outdated memory bank is worse than no memory bank.

### Step 2 — Write `AGENTS.md`

Create `AGENTS.md` at the repo root. It must define:

- [ ] Which memory bank files the agent reads at the start of each session (list them explicitly).
- [ ] A mandatory **pre-commit workflow** with at least 4 ordered steps. Example structure:
  1. Read memory bank files.
  2. Check that changed files follow the naming convention.
  3. Run linting or type checks.
  4. Update `memory-bank/progress.md` with the change made.
- [ ] At least one folder the agent **must not modify** without developer confirmation (e.g., `memory-bank/techContext.md` — architectural decisions require human sign-off).

### Step 3 — Add a rule

Create `.agents/rules/no-inline-styles.md` with:

- [ ] Scope: applies to all `.tsx` and `.html` files.
- [ ] Rule: no inline `style` attributes — all styles must use Tailwind classes or a CSS module.
- [ ] Rationale: explain in one sentence why this rule exists.

### Step 4 — Create a skill

Create `.agents/skills/add-page-section/SKILL.md` for a recurring task: adding a new section to the public website.

- [ ] **Objective:** A single sentence — what does this skill do?
- [ ] **Inputs:** What does the agent need to know before starting? (e.g., section title, content, position in the page)
- [ ] **Steps:** Numbered list of actions the agent takes.
- [ ] **Acceptance criteria:** At least 3 verifiable conditions (e.g., *"The section appears in the correct position when running `npm run dev`"*).

### Step 5 — Structure the Next.js apps

- [ ] Create `uis/website/` — a Next.js + TypeScript app for the public-facing cooking school site.
  - [ ] Route `/` renders a simple homepage (school name, tagline, one section placeholder).
- [ ] Create `uis/backoffice/` — a Next.js + TypeScript app for internal use.
  - [ ] Route `/` renders a basic dashboard shell (heading + placeholder content).
  - [ ] Import and display the output of the existing pricing logic TypeScript module on screen (not just in the console).

> Both apps must start without errors with `npm run dev`.

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
│   │   └── no-inline-styles.md
│   └── skills/
│       └── add-page-section/
│           └── SKILL.md
└── uis/
    ├── website/        ← Next.js public site
    └── backoffice/     ← Next.js internal app
```

---

## Checklist

- [ ] `memory-bank/projectbrief.md` describes both business and technical context (not just one).
- [ ] `AGENTS.md` specifies at least 4 ordered pre-commit steps.
- [ ] `.agents/rules/no-inline-styles.md` has an explicit scope and rationale.
- [ ] `.agents/skills/add-page-section/SKILL.md` has objective, inputs, steps, and acceptance criteria.
- [ ] `uis/website/` starts without errors and renders a homepage at `/`.
- [ ] `uis/backoffice/` starts without errors and shows pricing logic output on screen.

---

## Discussion Questions

1. What is the difference between `AGENTS.md` (a rule) and a skill? When would you use one vs. the other?
2. Why should architectural decisions in `techContext.md` require human confirmation before the agent modifies them?
3. Write one more acceptance criterion for the `add-page-section` skill that verifies the agent didn't break existing sections.
