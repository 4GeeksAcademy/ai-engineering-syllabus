# In-Class Example: Improving the Library Catalog with Agent Skills

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain continues with the community library catalog app from the previous context session — same workflow of loading, applying, and authoring agent skills, with a more approachable codebase than the financial dashboard.

## The Scenario

The library catalog app is working, but your tech lead has flagged two areas before the branch can be merged: accessibility and deployment best practices. They have shared two agent skills to guide your AI assistant. After applying them, you will explore the skills ecosystem and write one custom skill specific to the library catalog.

---

## Concepts Covered

| Concept | Where it applies |
|---|---|
| Agent skills | Loading structured instruction sets into a coding agent |
| `accessibility` skill | Auditing and fixing aria labels, alt text, keyboard navigation |
| `vercel-react-best-practices` skill | `next/image`, metadata API, build passing without warnings |
| `npx skills find` | Discovering community skills by topic |
| Custom skill authoring | Writing a project-specific skill with clear objective and acceptance criteria |
| Memory bank update | Reflecting the session's changes in `memory-bank/status.md` |

---

## Starting Point

Continue on the same repository from the previous session (the library catalog fork). If you do not have it:

```
https://github.com/4GeeksAcademy/ai-eng-library-catalog-context-example
```

Create a new branch before starting:

```bash
git checkout -b feature/agent-skills
```

---

## What to Do

### 1. Discover and review the provided skills

- [ ] Run `npx skills find accessibility` and read through what the skill covers before loading it
- [ ] Run `npx skills find vercel-react-best-practices` and read it too
- [ ] Load both skills into your coding agent and confirm the agent understands its instructions

### 2. Apply the `accessibility` skill

- [ ] Ask the agent (with the `accessibility` skill loaded) to audit the library catalog frontend
- [ ] Fix every `aria-label` and `role` issue flagged
- [ ] Verify that the book cards, search input, and navigation links are all reachable by keyboard (`Tab` / `Enter`)
- [ ] Add or correct `alt` text on any book cover images or icons
- [ ] Check that text and button contrast meets basic readability standards

### 3. Apply the `vercel-react-best-practices` skill

- [ ] Replace any `<img>` tags rendering book covers with `next/image`
- [ ] Ensure the catalog page and book detail page have correct `<title>` and `<meta description>` via the Next.js metadata API
- [ ] Remove any anti-patterns flagged by the skill
- [ ] Confirm the build passes: `npm run build`

### 4. Explore the ecosystem

- [ ] Run `npx skills find <topic>` for at least two topics relevant to the library app (suggestions: `forms`, `seo`, `typescript`)
- [ ] Apply at least one additional skill you find valuable — add a one-sentence justification in `memory-bank/status.md`

### 5. Write a custom skill

Identify something specific to this library catalog not covered by existing skills. Good candidates:

- How book search results should be displayed and ranked
- The naming convention for API route parameters (e.g., `isbn` vs `bookId`)
- How empty states should be handled when a search returns no results

Write a skill file at `.skills/library-catalog-<topic>.md` with:

| Section | What to include |
|---|---|
| **Objective** | One sentence: what this skill enforces |
| **Inputs** | What files or components it applies to |
| **Expected output** | What a passing implementation looks like |
| **Acceptance criteria** | 2–3 checkable conditions |

- [ ] Load the skill into the agent and verify the guidance is specific and useful

### 6. Update the memory bank

- [ ] Update `memory-bank/status.md` to reflect: skills applied, changes made, and the custom skill you authored

---

## Discussion Questions

1. What is the difference between a skill and a project rule (in `.agents/rules`)? When would you use each?
2. After applying the `accessibility` skill, the agent suggested adding `aria-label` to the search button. How would you verify this actually helps a screen reader user?
3. Your custom skill is only a few lines. A teammate says it's "too short to be useful." How do you argue for keeping it concise?
