# In-Class Example: Improving the Library Catalog with Agent Skills

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain continues with the community library catalog app from the context project — same agent-first workflow of loading, applying, and authoring skills on an inherited codebase, with a smaller repo than the financial dashboard.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same agent-first workflow and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.

You continue on the **inherited library catalog repo** from the context project. Your `memory-bank/` and `.agents/rules` are already in place. The app runs, but your tech lead wants two quality bars raised before merge: accessibility and deployment best practices. They shared two agent skills for your coding agent. After applying them (agent-led, you verify), explore the skills ecosystem and write one **internal project skill** — commits, deployment, testing, or something catalog-specific discovered in the codebase.

---

## Concepts Covered

| Concept                             | Where it applies                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| Agent-first skill application       | Agent audits and proposes; student verifies before commit                     |
| `accessibility` skill               | Auditing and fixing aria labels, alt text, keyboard navigation                |
| `vercel-react-best-practices` skill | `next/image`, metadata API, build passing without warnings                    |
| `npx skills find`                   | Discovering community skills by topic                                         |
| Internal skill authoring            | Repo-specific skill (commits, deployment, QA, or domain rules) with acceptance criteria |
| Memory bank update                  | Reflecting verified changes in `memory-bank/status.md`                        |

---

## Starting Point

Continue from the local example project used in the context project. Confirm `memory-bank/` and `.agents/rules` exist.

Create a new branch before starting:

```bash
git switch -c feature/agent-skills
```

Ask the agent how to run the app and which build command validates the frontend.

---

## What to Do

### 1. Discover and review the provided skills

- [ ] Run `npx skills find accessibility` and read what the skill covers before loading it
- [ ] Run `npx skills find vercel-react-best-practices` and read it too
- [ ] Load both skills into your coding agent and confirm the agent understands its instructions

### 2. Apply the `accessibility` skill (agent-led, you verify)

- [ ] Ask the agent (with the `accessibility` skill loaded) to audit the library catalog frontend and propose fixes
- [ ] Review each proposal; accept only changes tied to a file and skill instruction
- [ ] Verify outcomes: book cards, search input, and navigation reachable by keyboard; `alt` text; basic contrast
- [ ] Commit referencing the `accessibility` skill

### 3. Apply the `vercel-react-best-practices` skill (agent-led, you verify)

- [ ] Ask the agent to audit deployment-oriented patterns and apply fixes the skill flags
- [ ] Review proposals — e.g. `next/image` for covers, metadata on catalog and detail pages
- [ ] Confirm the repo's build command passes without new unjustified warnings
- [ ] Commit referencing the `vercel-react-best-practices` skill

### 4. Explore the ecosystem

- [ ] Run `npx skills find <topic>` for at least two topics relevant to the library app (suggestions: `forms`, `seo`, `typescript`, `testing`)
- [ ] Apply at least one additional skill — add a one-sentence justification in `memory-bank/status.md`

### 5. Write an internal project skill

With the agent, identify a gap specific to this inherited repo that community skills do not cover well. Good candidates:

- Commit or PR conventions for this team repo
- How to run smoke checks before merge (testing/QA)
- How book search results should be displayed and ranked
- Empty-state handling when search returns no results

Write a skill file at `.skills/library-catalog-<topic>.md` with:

| Section                 | What to include                          |
| ----------------------- | ---------------------------------------- |
| **Objective**           | One sentence: what this skill enforces   |
| **Inputs**              | What files or components it applies to   |
| **Expected output**     | What a passing implementation looks like |
| **Acceptance criteria** | 2–3 checkable conditions                 |

- [ ] Load the skill into the agent and verify guidance is specific and useful on a real task

### 6. Update the memory bank

- [ ] Update `memory-bank/status.md` to reflect: skills applied, verified changes, ecosystem skill chosen, and the internal skill you authored

---

## Discussion Questions

1. What is the difference between a skill and a project rule (in `.agents/rules`)? When would you use each?
2. After applying the `accessibility` skill, the agent suggested adding `aria-label` to the search button. How would you verify this actually helps a screen reader user?
3. Why author an internal skill for commits or testing when community skills exist?
4. Your internal skill is only a few lines. A teammate says it's "too short to be useful." How do you argue for keeping it concise?
