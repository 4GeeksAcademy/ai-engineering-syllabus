# In-Class Example: Spec-Driven Development for the Library Catalog

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain continues with the community library catalog app from the **context project** — same agent-first spec-driven workflow (explore `/docs`, TypeScript types, component specs, data contract docs, edge cases), but with two features instead of three, and a simpler API shape.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same agent-first workflow and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.

You continue on the **inherited library catalog repo** from the context project. Librarians want two new features. Before anyone writes a React component, your tech lead says: **"We spec first. Then we build."**

Your coding agent explores `/docs`; you verify types and rules against live API evidence. Specs must be clear enough that any coding agent can implement without follow-up questions.

---

## Concepts Covered

| Concept                      | Where it applies                                                     |
| ---------------------------- | -------------------------------------------------------------------- |
| Agent-first API exploration  | Phase 1: map endpoints and shapes from `/docs` with the agent        |
| TypeScript interfaces        | `api-types.ts` — response shapes verified against OpenAPI          |
| TypeScript query param types | `param-types.ts` — request parameters with JSDoc                     |
| Component specification      | `components.md` — naming, props, conditional rendering, empty states |
| Data contract documentation  | `frontend/specs/README.md` — endpoints, types, edge cases            |
| Spec-driven development      | Specify before build so implementation is unambiguous                |

---

## Starting Point

Continue in the same local library catalog example project from the context project. Confirm `memory-bank/` and `.agents/rules` exist.

Create a new branch:

```bash
git switch -c feature/frontend-specs
mkdir -p frontend/specs
```

Ask the agent to start the backend and explore `/docs` before writing anything.

---

## Feature Requests

> #### Feature 1 — Title search filter
>
> The librarians want to filter the book list by partial title. Add a text input at the top of the catalog page that filters the displayed books in real time. The search is case-insensitive. When the input is empty, all books are shown. When there are no matching books, display an explicit "No books found" message — not an empty grid.
>
> Relevant endpoint: `GET /api/books?title=<string>`
>
> ---
>
> #### Feature 2 — Genre breakdown panel
>
> Below the book list, add a panel showing the top 3 genres in the catalog with their book count and percentage of the total collection. The panel has a compact table: genre name, number of books, and percentage. It updates automatically when the title filter in Feature 1 is active (i.e., shows genre stats for the filtered subset, not the whole catalog). If the filtered result has fewer than 3 genres, show only the available ones with an explicit note.
>
> Relevant endpoint: `GET /api/books/genres/summary`

---

## What to Produce

### Phase 1 — Explore `/docs` (with the agent)

- [ ] Map endpoints, response shapes, and parameters for both features
- [ ] Note mismatches between PM wording and actual API fields

### Phase 2 — TypeScript types (agent drafts, you verify)

**`frontend/specs/api-types.ts`**

- [ ] `BookEntry`, `BooksResponse`, `GenreEntry`, `GenresSummaryResponse`
- [ ] No `any`, no `object`; JSDoc on every property; verify against `/docs`

**`frontend/specs/param-types.ts`**

- [ ] `BookSearchParams`, `GenresSummaryParams`

### Phase 3 — Component specs (agent drafts, you verify)

**`frontend/specs/components.md`** — for each feature: component names, props, layout, empty states, filter interaction between Feature 1 and 2.

### Phase 4 — Data contract

**`frontend/specs/README.md`** — endpoints, types, parameter constraints, ≥ 2 edge cases per feature with UI behavior.

> ⚠️ **Important:** Do not build React components or make API calls. Deliverables: `.ts` type files, `components.md`, and `frontend/specs/README.md`.

---

## Discussion Questions

1. Why verify TypeScript interfaces against `/docs` instead of guessing from component needs?
2. The genre panel shows stats for the filtered subset when a title filter is active. What edge case does this create?
3. A teammate says: "Why bother with `components.md`? The types are enough." What's the counter-argument?
4. Who should discover API field names — the student from memory, or the student+agent from `/docs`?
