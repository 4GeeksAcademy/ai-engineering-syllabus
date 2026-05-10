# In-Class Example: Error Handling Audit — Recipe App

> **Instructor note:** This is a classroom example to introduce the concepts of the *Error Handling* project using a simpler domain. It covers the same patterns (three-state UI, scoped try/catch, no stack traces to client, script exit codes, optional chaining, finally blocks) applied to a small pre-built recipe app. Use this to demonstrate the audit workflow before students apply it to their own monorepo. Do NOT share this file with students before they attempt the main project.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A small team built a recipe discovery app last sprint. It works most of the time — but when things go wrong, the experience breaks down badly. Users see raw error messages, pages go blank, and scripts crash with no useful output.

Your job is to audit the codebase and apply a consistent error handling strategy across all three layers: the Next.js frontend, the FastAPI backend, and the Python data-import script.

> **From the tech lead's review ticket:**
>
> - No error should crash the app or leave the user in an undefined state.
> - Every async operation must have three visible states: loading, success, and error.
> - Error messages shown to users must be human-readable — never a raw status code, stack trace, or JSON parsing error.
> - Every error state must offer a clear exit: a retry button, a back link, or a contact support prompt.
> - On the backend, exceptions must be caught at the right scope — not with one giant try/except.
> - Scripts must exit with a non-zero code on critical failure and print errors to `stderr`.

---

## Codebase overview

The app has three layers:

```text
frontend/          Next.js + TypeScript
  pages/
    index.tsx      Recipe list page — fetches from API on load
    [id].tsx       Recipe detail page — fetches a single recipe
    submit.tsx     Recipe submission form — POSTs to API
backend/           FastAPI
  main.py          Routes: GET /recipes, GET /recipes/{id}, POST /recipes
scripts/
  import_recipes.py  Reads a JSON file and bulk-inserts recipes into the DB
```

---

## Audit checklist

### Frontend (Next.js / TypeScript)

**`pages/index.tsx` — Recipe list**

- [ ] The `useEffect` fetches recipes but has no `try/catch` — if the request fails, the component crashes silently.
- [ ] There is no loading state: the page renders an empty list while data is being fetched.
- [ ] If the fetch fails, nothing is shown — no message, no retry option.
- [ ] **Fix:** Implement the three-state pattern with `isLoading`, `error`, and `data` states. Show a spinner while loading, an error message with a "Try again" button on failure, and the list on success.

**`pages/[id].tsx` — Recipe detail**

- [ ] `recipe.ingredients.map(...)` will throw if `ingredients` is `undefined` or `null`.
- [ ] A `404` from the API renders a blank white page.
- [ ] **Fix:** Add `optional chaining` (`recipe.ingredients?.map(...)`), a fallback for missing fields, and a user-friendly "Recipe not found" page for `404` responses.

**`pages/submit.tsx` — Submission form**

- [ ] The submit handler has no `try/catch` — a network error causes an unhandled promise rejection.
- [ ] The button stays enabled while the request is in flight — users can submit twice.
- [ ] On API error, the raw JSON from the server is rendered directly inside a `<p>` tag.
- [ ] There is no `finally` block, so `isLoading` never resets to `false` if the request throws.
- [ ] **Fix:** Wrap the fetch in `try/catch/finally`, disable the button during the request, translate API errors into human-readable messages, and always reset `isLoading` in `finally`.

---

### Backend (FastAPI)

**`GET /recipes` and `GET /recipes/{id}`**

- [ ] A database connection error causes FastAPI to return a raw Python traceback as the response body.
- [ ] `GET /recipes/{id}` with a non-integer `id` (e.g. `/recipes/abc`) crashes with an unhandled `ValueError`.
- [ ] **Fix:** Add a global exception handler that returns `{"error": "Something went wrong"}` for uncaught exceptions. Handle `ValueError` with a `400` response.

**`POST /recipes`**

- [ ] The route handler has one large `try/except Exception` that swallows all errors and always returns `200`.
- [ ] Validation errors (missing `title`, empty `ingredients`) return the internal Python object representation, not a clean JSON message.
- [ ] **Fix:** Break the broad catch into specific, scoped catches. Return `400` for validation errors with a field-level JSON body. Reserve the generic `500` handler for truly unexpected errors.

**Sensitive data:**

- [ ] The database connection string appears in error logs that are returned to the client.
- [ ] **Fix:** Log the full error server-side, return only a safe generic message to the client.

---

### Script (`scripts/import_recipes.py`)

- [ ] The script opens the JSON file without a `try/except` — if the file is missing or malformed, it crashes with a raw Python traceback printed to `stdout`.
- [ ] When a recipe fails to insert, the script continues silently — the user never knows some records were skipped.
- [ ] The script always exits with code `0`, even on critical failure.
- [ ] **Fix:** Wrap file I/O and JSON parsing in `try/except` with informative messages printed to `stderr`. Collect and report skipped records at the end. Call `sys.exit(1)` if the file cannot be opened.

---

## What we will evaluate

- [ ] All three frontend pages implement the loading / success / error three-state pattern.
- [ ] `try/catch` blocks are scoped to specific operations, not wrapped around entire functions.
- [ ] `finally` blocks are used to reset loading state in all form submissions.
- [ ] `optional chaining` and fallbacks prevent render errors from undefined data.
- [ ] Backend routes return structured JSON error responses with the correct HTTP status codes.
- [ ] No Python traceback or database connection string reaches the client.
- [ ] The import script handles file errors, reports skipped records, and exits with `sys.exit(1)` on critical failure.

---

## Discussion questions

1. The backend route currently has one large `try/except Exception` that catches everything. Why is this considered bad practice? What kinds of errors get hidden behind it, and how does scoped error handling give you better visibility?
2. The frontend submit button doesn't use a `finally` block to reset the loading state. Walk through a scenario where skipping `finally` leaves the UI in a broken state permanently — even after the user's network recovers.
3. The script exits with code `0` even when it fails. Why does the exit code matter in a CI/CD pipeline or automated workflow? What could silently go wrong downstream?
