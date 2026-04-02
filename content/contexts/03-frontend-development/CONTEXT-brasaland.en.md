# CONTEXT — Brasaland · Milestone 3: Talent Pipeline Tracker

> **Repository path:** `03-talent-pipeline-tracker/CONTEXT-brasaland.en.md`

---

## Your company

You are part of the **Brasaland Digital** team, the internal technology unit of Brasaland, a grilled food restaurant chain with 14 locations in Colombia and Florida. Your job is to build the tools that operational teams will use every day.

---

## The assignment

Ashley Turner, People Manager, has sent the following email with Nicolás Park, CTO, on copy:

> **To:** Nicolás Park (CTO)
> **CC:** Brasaland Digital Team
> **Subject:** URGENT — We need the candidate management tool this week
>
> Nicolás,
>
> I'm writing to you directly because we can no longer manage the **Executive Assistant** selection process in a Google Sheet. We have over a hundred applications and three people editing the same file at the same time. This morning we lost the data of two candidates due to a save conflict.
>
> I understand the backend is ready. I need someone from the team to build the frontend this week — this cannot wait any longer.
>
> What I need the tool to do:
> - Show all candidates at a glance: name, position, status, and stage.
> - Filter by status and stage, and search by name or email without reloading the page.
> - Open a candidate's detail and update their status or stage from there.
> - Add internal notes after each call or interview, and delete them when they're no longer needed.
> - Register candidates who apply through other channels and correct data when it comes in wrong.
>
> Thank you for escalating this.
>
> Ashley

---

## Context of the active search

| Field | Value |
|---|---|
| Position | Executive Assistant |
| Company | Brasaland |
| Location | Corporate headquarters, Medellín |
| Profile | Executive support experience, calendar and travel management, professional English |

---

## API and data

The mock API is centrally deployed and shared across all company contexts in the course. Fields, values, and structure are as defined in the backend technical specification. No adaptation is required.

### `status` values

| API value | UI label |
|---|---|
| `received` | Received |
| `in_progress` | In progress |
| `selected` | Selected |
| `discarded` | Discarded |

### `stage` values

| API value | UI label |
|---|---|
| `pending` | Pending review |
| `review` | Under review |
| `personal_interview` | Personal interview |
| `technical_interview` | Technical interview |
| `offer_presented` | Offer presented |

> Raw API values (`in_progress`, `personal_interview`, etc.) must never be visible in the interface. Always use the labels from this table.

---

## Specific acceptance criteria

- Status and stage fields show human-readable labels, never raw API values.
- Notes are visible only within the candidate detail view.
- The registration form includes all fields required by the API.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_For exclusive use in programme project generation_
