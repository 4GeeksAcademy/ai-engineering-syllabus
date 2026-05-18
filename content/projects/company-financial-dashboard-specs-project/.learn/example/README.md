# In-Class Example: Spec-Driven Development for the Library Catalog

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain continues with the community library catalog app — same spec-driven workflow (TypeScript types, component specs, data contract docs, edge cases), but with two features instead of three, and a simpler API shape.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


The library catalog is live. The librarians using it want two new features. Before anyone writes a React component or makes an API call, your tech lead says: **"We spec first. Then we build."**

Your job is to write precise specifications for both features. Check the API documentation at `http://localhost:8000/docs` to understand the real response shapes before writing any types. Your specs should be clear enough that any developer — or AI agent — can implement the feature without asking questions.

---

## Concepts Covered

| Concept | Where it applies |
|---|---|
| TypeScript interfaces | `api-types.ts` — response shapes from real API endpoints |
| TypeScript query param types | `param-types.ts` — request parameters with JSDoc |
| Component specification | `components.md` — naming, props, conditional rendering, empty states |
| Data contract documentation | `frontend/specs/README.md` — endpoints, types, edge cases |
| Spec-driven development | Writing before building so the implementation is unambiguous |

---

## Starting Point

Continue on the same library catalog repository. Create a new branch:

```bash
git checkout -b feature/frontend-specs
mkdir -p frontend/specs
```

Start the backend and read the API docs at `http://localhost:8000/docs` before writing anything.

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

### TypeScript Types (`frontend/specs/api-types.ts`)

- [ ] `BookEntry` — a single book record (id, title, author, genre, year, available)
- [ ] `BooksResponse` — list of books returned by the search endpoint
- [ ] `GenreEntry` — a single genre row (genre name, count, percentage)
- [ ] `GenresSummaryResponse` — the full genre breakdown response

Rules:
- No `any`, no `object`
- Every property must have a JSDoc comment explaining its meaning and format

### TypeScript Param Types (`frontend/specs/param-types.ts`)

- [ ] `BookSearchParams` — the optional `title` query string parameter
- [ ] `GenresSummaryParams` — optionally accepts a `title` filter to scope the genre stats

### Component Specifications (`frontend/specs/components.md`)

For each feature, document:

**Feature 1 — Title search filter**
- Component name and where it lives in the page
- Props (if any) and their types
- What renders when the input is empty vs. when there are no results

**Feature 2 — Genre breakdown panel**
- Component name, props, and layout
- What renders when fewer than 3 genres are available
- How the panel reacts when the title filter changes

### Data Contract Documentation (`frontend/specs/README.md`)

For each feature, document:

- Which endpoint(s) it calls (verify paths against `/docs`)
- TypeScript types used for request and response
- Valid values and constraints for each parameter
- At least **2 edge cases** and what the UI must show in each case

Example edge cases to consider:
- What if `title` contains special characters like `&` or `/`?
- What if the genres endpoint returns an empty array?
- What if the book list has only 1 genre?

> ⚠️ **Important:** Do not build React components or make API calls. Your deliverables are `.ts` type files, `components.md`, and `frontend/specs/README.md`.

---

## Discussion Questions

1. Why do we write TypeScript interfaces based on the actual API response (from `/docs`) rather than guessing the shape from the component's needs?
2. The genre panel is supposed to show stats for the "filtered subset" when a title filter is active. What edge case does this create, and how should the spec address it?
3. A teammate says: "Why bother with `components.md`? The types are enough." What is the argument for writing a separate component spec?
