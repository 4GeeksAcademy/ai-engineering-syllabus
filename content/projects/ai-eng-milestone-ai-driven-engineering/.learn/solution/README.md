# Milestone 4 — AI-driven Engineering (reference solution)

This README is the canonical reference for **"Milestone 4 — AI-driven Engineering"**. It describes what a correct delivery should include inside the student fork of [ai-engineering-company-project-monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo). This folder documents expected structure and reviewer checks only; it is not runnable code.

## Alignment with company briefing

All memory-bank content, `AGENTS.md` guardrails, `.agents/rules`, and the reusable skill must reflect the student’s assigned **company-BRIEFING.md** (and related BRIEFING files). Generic placeholders that ignore sector, KPIs, naming, or constraints from the scenario should be treated as incomplete.

---

## Part A — Agent infrastructure

### `memory-bank/` (repository root)

A valid solution includes at least:

| File                          | Purpose                                                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `memory-bank/projectbrief.md` | Business description, project goals, and the problem the product solves—grounded in the assigned BRIEFING.                   |
| `memory-bank/techContext.md`  | Stack, architectural decisions already taken, and technical constraints (tooling, monorepo layout, deployment assumptions). |
| `memory-bank/progress.md`     | What is implemented today, what is in flight, and sensible next steps—updated like a living log, not a marketing roadmap.   |

Quality bar:

- Business context and technical context are both present and cross-referenced where useful (for example: a KPI ties to a specific module or dataset).
- Statements are specific enough that a new contributor (or agent) can act on them without guessing.

### `AGENTS.md` (repository root)

Should explicitly define:

1. **Session start:** which `memory-bank/*.md` files must be read before edits (list them by path).
2. **Pre-commit workflow:** at least **four ordered, explicit steps** (for example: run formatter/linter, run tests or typecheck, update `progress.md` if behavior changed, self-review diff scope). Steps must be actionable verbs, not vague “check everything”.
3. **Protected areas:** folders or files that must **not** be modified without explicit human confirmation (for example: generated lockfiles, CI config, or another app’s package—whatever matches the real monorepo).

### `.agents/` rules

- At least **one** rule file under `.agents/rules/` (or the structure described in the project README).
- Each rule states **scope** clearly: always-on, path-pattern based, or agent-requested.
- Rules are **concrete** (naming, imports, where new code lives, how to run checks)—not generic “write clean code”.

### At least one agent skill

Under `.agents/skills/<skill-name>/SKILL.md` (or equivalent per tooling), include:

- **Single objective** (one sentence).
- **Documented inputs** (what the human or agent must provide).
- **Explicit, verifiable acceptance criteria** (checkboxes or measurable outcomes—something a reviewer can validate without subjective judgment).

Example categories that fit this milestone: “run delivery checklist before PR”, “update memory-bank after a feature”, “add a new internal route following layout conventions”—as long as criteria are testable.

---

## Part B — Monorepo folder map (no app bootstrap in this milestone)

This milestone does **not** require creating Next.js apps. A correct delivery documents (in `memory-bank/` and/or agent rules) where product code belongs when those folders are used:

| Path               | What goes here when created                                  |
| ------------------ | ------------------------------------------------------------ |
| `/uis`             | Frontend projects                                            |
| `./uis/website`    | Public corporate website (home `/`, brand/copy from BRIEFING) |
| `./uis/backoffice` | Internal app (own layout; entry view on `/`)                 |
| `/services`        | Backend APIs and services                                    |

Students must not invent a parallel frontend or API tree. Prefer the template’s own folder READMEs over generic examples.

---

## Validation checklist (reviewers)

Use this checklist against student submissions:

### Agent infrastructure

- [ ] `memory-bank/` exists with `projectbrief.md`, `techContext.md`, and `progress.md`.
- [ ] Memory bank reflects **both** business and technical context tied to company-BRIEFING.md.
- [ ] `AGENTS.md` lists mandatory memory-bank reads at session start.
- [ ] `AGENTS.md` defines a **minimum four-step ordered** workflow before commit.
- [ ] `AGENTS.md` lists paths the agent must not touch without explicit confirmation.
- [ ] `.agents/rules/` contains at least one scoped, actionable rule.
- [ ] At least one skill exists with one objective, documented inputs, and verifiable acceptance criteria.

### Folder conventions

- [ ] Memory bank and/or agent rules state where `/uis/website`, `/uis/backoffice`, and `/services` fit.
- [ ] No invented parallel app folders outside the monorepo map.

### Delivery

- [ ] Branch name is `feature/agent-memory-bank` (per project instructions).
- [ ] PR targets `main` on the student fork and includes a link to `AGENTS.md` as required.

---

## Notes for reviewers

- The rubric prioritizes **governance artifacts** (memory bank, agent protocol, rules, skill) and **correct folder mapping** — not shipping UI in this milestone.
- If the template repository’s folder names differ from the table above, evaluate against the **template’s own README** and the student’s documented decisions in `techContext.md`.
