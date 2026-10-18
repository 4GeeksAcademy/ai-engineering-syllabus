# BRIEFING — Nexova
## Onboarding Agent with Memory · W6D16

---

## The company

Nexova is an HR consulting and talent acquisition firm headquartered in Valencia, Spain, with an office in Miami. It onboards very different profiles — selection consultants, support agents, trainers, and administrative staff — at varying rates depending on project load. Patricia Solís (HR Manager) is the HR lead and the person who interacts with the agent.

---

## HR character

| Field | Value |
|---|---|
| Name | Patricia Solís |
| Role | HR Manager |
| Location | Valencia |
| Communication style | Direct and organised. Sends precise messages and expects equally precise responses. |
| Telegram handle | `@patricia_nexova` |

---

## Welcome email template

> **Subject:** Welcome to Nexova — complete your onboarding process
>
> Hi [name],
>
> We're delighted to have you joining the Nexova team. To make sure everything is ready before your first day, we need you to complete a few steps through our onboarding assistant.
>
> Message it on Telegram at **[bot handle]** to get started. The assistant will walk you through each step.
>
> Best,
> **Nexova People Team**

---

## Onboarding instructions

The agent delivers these instructions to the new hire at step 7, after identity verification:

> Hi! I'm Nexova's onboarding assistant. To complete your registration in our systems, please provide the following information one step at a time:
>
> 1. What is your full name as it appears on your national ID or passport?
> 2. What is your tax identification number? (NIF or NIE for Spain-based staff; Tax ID for Miami-based staff)
> 3. Which office will you be primarily working from? (Valencia / Miami)
> 4. What username would you like to use for Nexova's internal systems? (no spaces or special characters)
> 5. Confirm that you have read and accepted the Code of Conduct and provide the date you did so.
> 6. Confirm that you have had your welcome session with your manager and provide their name.
>
> Once I have received all your responses, your onboarding will be marked as complete and I will let Patricia know.

---

## Required deliverables and how the agent verifies each one

| # | Deliverable | What the agent expects |
|---|---|---|
| 1 | Full name | Free text (first and last name) |
| 2 | Tax identification number | NIF / NIE / Tax ID (free text) |
| 3 | Primary office | "Valencia" or "Miami" |
| 4 | Chosen username | Text with no spaces or special characters |
| 5 | Code of Conduct confirmation | Explicit confirmation + date (e.g. "Accepted on 8 May") |
| 6 | Welcome session confirmation | Explicit confirmation + manager's name |

The process is marked as **complete** when the agent has received a response to all six points.

---

## Memory schema per employee

```
employee:
  full_name: string
  email: string
  tax_id: string | null
  office: "Valencia" | "Miami" | null
  username: string | null
  code_of_conduct_confirmed: boolean
  code_of_conduct_date: string | null
  welcome_session_confirmed: boolean
  welcome_session_manager: string | null
  status: "not_started" | "active" | "completed"
  start_date: string
  close_date: string | null
```

---

## Business rules

- The username may not contain spaces or special characters. If the response does not meet the format, the agent must ask again before recording it.
- The tax identification number may be a NIF or NIE (for Spain-based staff) or a Tax ID (for Miami-based staff). The agent accepts any format without validating its structure.
- The process cannot be marked as complete if the tax ID or the Code of Conduct confirmation are missing, as both have legal implications.
- Patricia uses the daily summary primarily to identify employees in "not started" status: people who have been reported by HR but have not yet contacted the bot one or two days before their start date.
