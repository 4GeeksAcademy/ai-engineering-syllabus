# Milestone 3 — Talent Pipeline Tracker (reference solution)

This README is the canonical reference for **"Milestone 3 — Talent Pipeline Tracker"**. It describes how a correct implementation should be structured, how it should talk to the course REST API, and what reviewers should verify. The actual app lives in the student monorepo under `apps/talent-pipeline-tracker/`; this folder documents the expected design only.

## Alignment with company context

All user-visible labels, option values for status/stage, and field copy must follow the student’s assigned **CONTEXT-company.md** (and related CONTEXT files). The API field names and enums are defined by the backend documentation; the UI should map those to the terminology required by the scenario (not generic placeholders like “Status 1”).

## Recommended solution structure

A reference implementation should organize the Next.js App Router app roughly as follows:

- `app/page.tsx` — candidate list (`/`)
- `app/candidates/[id]/page.tsx` — candidate detail (`/candidates/[id]`)
- `app/layout.tsx` — root layout, fonts, global styles
- `components/` — presentational pieces (list row, filters, note item, forms, loading and error banners)
- `lib/api.ts` or `services/records.ts` — thin wrappers around `fetch` for each endpoint
- `types/` — TypeScript types (or interfaces) for API payloads: candidate, note, list responses, PATCH bodies, etc.

Optional:

- `hooks/useRecordsFilters.ts` — encapsulate URL sync + local search if it keeps `page.tsx` readable

Do **not** introduce Redux, Zustand, Jotai, or similar; local `useState` / `useReducer` per view or small hooks is enough.

## Environment and API base URL

- Read the base URL from `process.env.NEXT_PUBLIC_API_URL` (no trailing slash ambiguity: normalize in one place, e.g. `const base = process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "")`).
- Never commit secrets; document `NEXT_PUBLIC_API_URL` in `.env.example`.

## REST contract the solution must implement

Assuming the API is mounted at `{NEXT_PUBLIC_API_URL}` (for example `https://host/api/v1`):

| Action            | Method   | Path                          | Notes                                              |
| ----------------- | -------- | ----------------------------- | -------------------------------------------------- |
| List candidates   | `GET`    | `/records`                    | Returns an array (or paginated shape per API docs) |
| Get one candidate | `GET`    | `/records/:id`                | Full record                                        |
| Create candidate  | `POST`   | `/records`                    | Body per API schema                                |
| Replace candidate | `PUT`    | `/records/:id`                | Full update per API                                |
| Partial update    | `PATCH`  | `/records/:id`                | At least status and/or stage from the detail view  |
| List notes        | `GET`    | `/records/:id/notes`          |                                                    |
| Add note          | `POST`   | `/records/:id/notes`          | Body typically `{ content }` or per docs           |
| Delete note       | `DELETE` | `/records/:id/notes/:note_id` |                                                    |

Every call should use `async/await`, check `response.ok`, and parse JSON only when appropriate. Surface HTTP errors and malformed responses in the UI.

## Suggested `fetch` helper pattern

Centralize headers and error handling once:

```ts
async function api<T>(path: string, init?: RequestInit): Promise<T> {
  const base = process.env.NEXT_PUBLIC_API_URL!.replace(/\/$/, "");
  const res = await fetch(`${base}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...init?.headers,
    },
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  if (res.status === 204) return undefined as T;
  return res.json() as Promise<T>;
}
```

Adjust if the real API uses a different envelope (e.g. `{ data: [...] }`).

## List page (`/`)

**Data:** `GET /records` on mount (client component with `useEffect`, or server component with `fetch` + revalidation strategy—both are valid if the milestone’s “no full reload” and mutation refresh requirements are met).

**Query parameters (`useSearchParams`):**

- Persist **status** and **stage** filters in the URL (e.g. `?status=...&stage=...`).
- On change, build `URLSearchParams`, delete keys when empty, and `router.push(\`${pathname}?${params}\`)`or`router.replace` so shared links restore the same filters.

**Search (name / email):**

- Filter **in the client** over the loaded list (case-insensitive `includes`), or refetch if the API supports a query parameter—follow the official API documentation. The requirement is: no full page reload when typing; `useState` for the search string is typical.

**UI states:** loading spinner/skeleton while fetching, error message on failure, empty state when the filtered list is empty.

## Detail page (`/candidates/[id]`)

**Data:** `GET /records/:id` and `GET /records/:id/notes` (can run in parallel with `Promise.all`).

**Display:** All fields required by the project brief (name, email, phone, position, LinkedIn, CV link, years of experience, status, stage, application date)—use exact API property names in types; map to labels from CONTEXT.

**Updates:**

- Controls for **status** and **stage** that call `PATCH /records/:id` with the minimal body the API expects.
- After success, update local state (or refetch the record) so the UI reflects changes **without** a full document reload.

**Notes:**

- Render the notes list; **Add** submits `POST /records/:id/notes`; **Delete** calls `DELETE` with the note id, then remove that note from state or refetch notes.

## Create and edit flows

- **New candidate:** a form on the list page or a dedicated route/modal that `POST /records` with validated required fields before submit.
- **Edit candidate:** a form (on the detail page or separate route) that `PUT /records/:id` with the full resource or the shape required by the API.

Show inline or banner **success** and **error** feedback after each submission attempt.

## TypeScript

- Define types for: candidate (record), note, create/update payloads, and any wrapper objects the API returns.
- Use these types in the API layer and in component props to avoid `any`.

## Validation checklist (reviewers)

Use this checklist against student submissions:

- [ ] `/` lists candidates from `GET /records` with name, position, status, and stage visible.
- [ ] Status and stage filters are driven by URL query parameters and restore on refresh/share.
- [ ] Name/email search works without full page reload.
- [ ] `/candidates/[id]` loads the correct record and shows all required fields.
- [ ] Status and stage can be updated from the detail view via `PATCH`.
- [ ] Notes list, add (`POST`), and delete (`DELETE`) work and the UI updates without a full reload.
- [ ] New candidate `POST` and edit `PUT` forms validate required fields and show success/error feedback.
- [ ] Loading, success, and error states are visible for async operations.
- [ ] No external global state libraries; navigation uses Next.js App Router (`Link`, dynamic segments).
- [ ] Folder layout separates components, types, and API access; types match API structures.
- [ ] Terminology and labels reflect the assigned company CONTEXT, not a generic HR template.

## Notes for reviewers

- Visual polish is not the primary rubric; clarity, correctness, and resilient async UX are.
- Exact JSON shapes and status/stage enums come from the course API documentation; the reference solution is behavioral and structural—students must still match the live contract.
