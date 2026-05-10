# In-Class Example — Community Library Loan Tracker

> **Instructor note:** This is a classroom-paced example to introduce the same concepts as the graded project (Milestone 3). Use a different domain so students don't confuse it with their own work. This scenario is intentionally small — the goal is one working session, not a finished product.

---

## The Scenario

A neighborhood library is tracking book loans on sticky notes and a whiteboard. The librarian needs a simple internal tool to see who has what book, when it's due, and add quick notes when a borrower calls.

A REST API already exists and is documented at `https://playground.4geeks.com/tracker/api/v1/docs` (use the same tracker backend). The librarian's requirements:

> - See all active loans in a list (borrower name, book title, due date, loan status).
> - Filter by status (active, returned, overdue). Search by borrower name.
> - Click a loan to see full details and update its status.
> - Add and delete short notes on any loan (e.g. "borrower called, returning Friday").
> - Register a new loan and edit an existing one when something changes.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Framework | Next.js 14 (App Router) |
| Language | TypeScript |
| Styles | Tailwind CSS |
| Data | REST API via `fetch` + `async/await` |
| State | React hooks only (no external library) |

---

## Project Structure (suggested)

```
/app
  /page.tsx              ← loan list
  /loans/[id]/page.tsx   ← loan detail
/components
  LoanCard.tsx
  LoanForm.tsx
  NoteList.tsx
  StatusBadge.tsx
/types
  loan.ts
/lib
  api.ts                 ← all fetch calls in one place
```

---

## What to Build

### Loan list page (`/`)

- [ ] Fetch all loans from `GET /records` and display: borrower name, book title, due date, status.
- [ ] Filter by status using `useSearchParams` (no full reload).
- [ ] Search by borrower name (client-side filter, no reload).
- [ ] Show a loading spinner while fetching; show an error message if the request fails.

### Loan detail page (`/loans/[id]`)

- [ ] Fetch and display all fields from `GET /records/:id`: borrower name, email, phone, book title, ISBN, due date, status, notes.
- [ ] Update loan status via `PATCH /records/:id` — a dropdown or button group is fine.
- [ ] List notes from `GET /records/:id/notes`. Add a note (`POST`) and delete a note (`DELETE`).
- [ ] Navigate back to the list without a full page reload.

### Loan management

- [ ] Form to create a new loan (`POST /records`) — validate required fields before submit.
- [ ] Form to edit an existing loan (`PUT /records/:id`) — pre-fill with current data.
- [ ] Show a success or error message after each form submission.

### Async states (apply everywhere)

- [ ] Every data operation must have at least three UI states: **loading**, **success**, **error**.
- [ ] After any mutation (`POST`, `PATCH`, `PUT`, `DELETE`), update the UI without a full reload.

### TypeScript

- [ ] Define a `Loan` type and a `Note` type that match the API response shape.
- [ ] Use those types in every component and service function.

---

## Key Concepts to Discuss in Class

| Concept | Where it appears |
|---|---|
| Dynamic routes | `/loans/[id]/page.tsx` |
| `useSearchParams` for filters | Loan list page |
| Lifting state vs. local state | LoanForm inside list vs. detail |
| Async/await + loading/error states | All `fetch` calls |
| TypeScript interfaces for API data | `/types/loan.ts` |
| Separation of concerns | `/lib/api.ts` vs. components |

---

## Discussion Questions

1. Why do we put all fetch calls in `/lib/api.ts` instead of directly inside components? What problem does that solve when the API URL changes?
2. When a user updates the loan status on the detail page, should the list page also update? How would you keep both in sync without a full page reload?
3. What happens if the `GET /records/:id` call returns a `404`? How should the UI respond, and where in the code should that be handled?
