# CONTEXT — TrackFlow · Milestone 3: Talent Pipeline Tracker

> **Repository path:** `03-talent-pipeline-tracker/CONTEXT-trackflow.en.md`

---

## Your company

You are part of the **TrackFlow Tech** team, the internal technology unit of TrackFlow, a last-mile delivery and warehouse management company with operations in Los Angeles and Zaragoza. The team is in the middle of a digital transformation and every tool you build has a direct impact on the next day's operations.

---

## The assignment

Ana Whitfield, Head of Warehouse Operations, has sent the following email with Andrés Kim, CTO, on copy:

> **To:** Andrés Kim (CTO)
> **CC:** TrackFlow Tech Team
> **Subject:** URGENT — Candidate management tool — needed now
>
> Andrés,
>
> I'm copying the tech team directly because this cannot wait any longer. We are managing the **Executive Assistant** selection process for the Zaragoza headquarters in an Excel file that nobody has under control. We have over a hundred applications, three people touching the same file, and this morning we discovered that someone overwrote the notes from two interviews last week.
>
> Javier confirmed to me yesterday that the backend is live. I need someone from the team to build the frontend this week. The selection process cannot stop.
>
> What I need:
> - See all candidates at a glance: name, position, status, and stage.
> - Filter by status and stage, and search by name or email without reloading the page.
> - Open a candidate's detail and update their status or stage from there.
> - Add notes after calls and interviews, and delete them when they're no longer needed.
> - Register candidates who come through other channels and edit data when it arrives incorrectly.
>
> Thank you,
> Ana

---

## Context of the active search

| Field | Value |
|---|---|
| Position | Executive Assistant |
| Company | TrackFlow |
| Location | Zaragoza headquarters |
| Profile | Executive support experience, calendar and travel management, professional English, proficiency with office tools |

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
