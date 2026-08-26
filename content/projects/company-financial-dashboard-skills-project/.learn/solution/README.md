# Enhacing development with agent skills - Financial dashboard — Reference solution

This README defines what a correct reference delivery should include for **Enhacing development with agent skills - Financial dashboard**.

The goal is not to rebuild the dashboard. The goal is **targeted improvements** on the inherited repo from the context project — driven by agent skills, verified by the student, plus one internal project skill and updated memory.

Students continue the same fork with `memory-bank/` and `.agents/rules` already in place. The coding agent applies skills; the student drives, verifies outcomes, and keeps changes traceable.

**Stack-agnostic here means student prior knowledge, not project technology.** The dashboard has a predefined stack (documented in the context project memory bank). Assigned community skills match that stack — students are not expected to pick alternate skills because they lack Next or a11y background.

## Expected deliverables

A valid solution should include all of the following:

- Branch `feature/agent-skills` (or equivalent) with commits that map to skill applications where possible.
- Measurable accessibility improvements aligned with the `accessibility` skill (keyboard use, `aria-*`, `alt`, contrast) — agent-led, student-verified.
- Deployment-oriented improvements aligned with `vercel-react-best-practices` (`next/image`, metadata API, reduced layout shift, clean build using the repo's documented command).
- Evidence of exploring the ecosystem: at least two `npx skills find <topic>` explorations and **at least one additional** applied skill with a short written justification (PR comment, commit message, or `memory-bank`).
- An **internal project skill file** under `.skills/` with objective, inputs, outputs, and acceptance criteria — specific to this repo (commits, deployment, testing/QA, dashboard conventions, API patterns, etc.).
- Updated `memory-bank/progress.md` (or equivalent) describing skills used, verified changes, ecosystem skill choice, and the authored internal skill.

## Phase 1 — Load and apply required skills

The solution should demonstrate:

- Discovery via `npx skills find accessibility` and `npx skills find vercel-react-best-practices` before loading them into the agent.
- Agent-led audit and fixes traceable to those skills (not unrelated refactors or manual checklist work disconnected from skill instructions).
- Student verification of proposals before commit.

## Phase 2 — Ecosystem exploration

Minimum expected:

- At least two topic searches with `npx skills find` relevant to the project (e.g. performance, seo, forms, typescript, testing).
- At least one extra skill installed or applied beyond the two required, with justification.

## Phase 3 — Author an internal project skill

The custom skill should:

- Address a gap not covered well by off-the-shelf skills — including workflow topics like commit conventions, deployment steps, or testing/QA checks for this dashboard.
- Be derived from repo evidence (often discovered with the agent during earlier phases).
- Be short, precise, and verifiable — not generic boilerplate.
- Produce actionable guidance when loaded into the agent on a real task.

## Phase 4 — Memory bank and submission

- `memory-bank` reflects the session accurately.
- Pull request opened against `main` with a clear description linking changes to skills.

## Validation checklist

Use this checklist to review submissions:

- [ ] `accessibility` skill was applied agent-first; keyboard navigation and assistive-tech basics hold up in manual checks.
- [ ] `vercel-react-best-practices` skill was applied agent-first; frontend build succeeds without new unjustified warnings.
- [ ] At least two `npx skills find` topic searches were performed; at least one extra skill was applied with justification.
- [ ] `.skills/` contains a well-structured **internal** skill with project-specific guidance (commits, deployment, testing/QA, or repo-derived topic).
- [ ] Memory bank updated; branch/PR workflow followed.
- [ ] No full-dashboard rewrite; changes remain traceable to skill instructions and were verified by the student.

## Notes for reviewers

- Prefer evidence (PR description, commit messages, memory bank) over volume of code churn.
- The internal skill should be **specific to this inherited repo**; penalize copy-pasted generic checklists disguised as a skill.
- Penalize work that reads like the student fixed everything manually without loading or following skills.
