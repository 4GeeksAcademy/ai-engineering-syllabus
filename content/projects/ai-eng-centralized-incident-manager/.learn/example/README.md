# In-Class Example: Portfolio Bug Tracker

> **Instructor note:** This is a classroom example to introduce the concepts of the *Centralized Incident Manager* project using a simpler domain. It covers the same stack and patterns (data model with lifecycle, seeding, REST API, frontend form/list/summary, shared validation) but is scoped to a 1–2 hour live session. Do NOT share this file with students before they attempt the main project.

---

## The scenario

A developer maintains a personal portfolio website with several pages (Home, About, Projects, Contact). Visitors occasionally find bugs: broken links, missing images, layout issues, or typos. The developer wants a small internal tool to track these reports, assign them a priority, move them through a resolution lifecycle, and see a quick summary of what is pending.

The team already has a CSV with 10 historical bug reports that need to be imported as seed data on first run.

---

## Data model

Define a `BugReport` entity with the following fields:

| Field | Type | Notes |
|---|---|---|
| `id` | integer | Auto-generated |
| `title` | string | Required |
| `description` | string | Required |
| `page` | enum | `home`, `about`, `projects`, `contact` |
| `priority` | enum | `low`, `medium`, `high` |
| `status` | enum | `open`, `in_progress`, `resolved`, `discarded` |
| `created_at` | datetime | Auto-generated |
| `updated_at` | datetime | Auto-updated |

**Lifecycle transitions:**

```
open → in_progress → resolved
open → discarded
in_progress → discarded
resolved and discarded are final (no transitions allowed from them)
```

---

## Seed data (`/scripts`)

The following CSV represents the historical import file. Save it as `bug-reports.csv`:

```csv
title,description,page,priority,status
Broken contact form,Submit button does nothing on mobile,contact,high,open
Missing profile photo,Image returns 404,about,medium,open
Typo in hero text,"Recieve" should be "Receive",home,low,resolved
Dead project link,Link to GitHub project 404s,projects,high,open
Wrong font on mobile,Body text uses serif on iOS,home,low,open
Footer overlaps content,Footer covers last section on small screens,about,medium,in_progress
Slow image load,Hero image takes 8s to load,home,medium,open
Missing alt text,All project images have empty alt,projects,low,open
Form validation missing,Email field accepts any text,contact,high,open
Dark mode flicker,Screen flashes white on load in dark mode,home,low,discarded
```

- [ ] Create `seed.py` that reads `bug-reports.csv` and inserts each row into the database.
- [ ] Skip rows with missing required fields and print them to the console at the end.
- [ ] Make the script idempotent: check `title` before inserting to avoid duplicates.

---

## Backend (FastAPI)

- [ ] `POST /api/bugs` — create a new bug report. Return `400` with a field-level error message for any missing or invalid field.
- [ ] `GET /api/bugs` — list all bug reports. Accept optional filters: `status`, `priority`, `page`.
- [ ] `GET /api/bugs/{id}` — return a single report. Return `404` if not found.
- [ ] `PATCH /api/bugs/{id}/status` — update status. Reject invalid lifecycle transitions with `400`.
- [ ] `GET /api/bugs/summary` — return totals grouped by `status`, `priority`, and `page`. Must return zero-counts on an empty database (no errors).

**Error handling rules:**
- Unhandled exceptions return `500` with a generic message — never a Python traceback.
- Validation errors identify the field in the JSON response body.

---

## Frontend (Next.js)

**Bug report form:**

- [ ] A page with a form that includes all model fields.
- [ ] Show a loading spinner while the request is in flight; disable the submit button.
- [ ] If the API returns a field-level error, show the message next to the relevant input.
- [ ] On success, clear the form and show a confirmation message.
- [ ] Never show raw server error text to the user.

**Bug list panel:**

- [ ] A page listing all bug reports with filters for `status`, `priority`, and `page`.
- [ ] Handle three states: loading (spinner), empty (informative message), with data (table/cards).
- [ ] Allow updating the status of each report inline. If the update fails, revert the visual state and notify the user.

**Summary panel:**

- [ ] Display the totals from `/api/bugs/summary`.
- [ ] If the request fails, show an error state without breaking the rest of the page.

---

## Shared validation

- [ ] Extract the validation logic (required fields, enum values, lifecycle transitions) to a shared module reused by both the seed script and the API. No duplication.

---

## Discussion questions

1. Why is it important that the seed script is idempotent? What could go wrong if you run it twice on a production database without that check?
2. The status lifecycle prevents jumping directly from `open` to `resolved`. Can you think of a real-world reason why such constraints matter — and how you would communicate a rejected transition to the user in a friendly way?
3. The summary endpoint must return zero-counts even when the database is empty. Why return `{ "open": 0, ... }` instead of just an empty object `{}`? How does this affect the frontend code?
