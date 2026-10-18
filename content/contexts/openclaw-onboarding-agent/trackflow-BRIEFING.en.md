# BRIEFING — TrackFlow
## Onboarding Agent with Memory · W6D16

---

## The company

TrackFlow manages warehouses and last-mile delivery in Los Angeles and Zaragoza. It primarily onboards warehouse operatives, logistics coordinators, and customer experience agents, with frequent hiring cycles during peak volume periods. The two operations run under different labour frameworks (California / Spain) with separate teams. The People function is led by the manager responsible for both operations, based in Zaragoza.

---

## HR character

| Field | Value |
|---|---|
| Name | Elena Morales |
| Role | People & Culture Manager |
| Location | Zaragoza |
| Communication style | Practical and efficient. Prefers concrete data and unambiguous confirmations. |
| Telegram handle | `@elena_trackflow` |

---

## Welcome email template

> **Subject:** Welcome to TrackFlow — start your onboarding process
>
> Hi [name],
>
> We're excited to have you joining the TrackFlow team. To make sure everything is ready for your first day, we need to complete a few steps beforehand.
>
> Message our onboarding assistant on Telegram at **[bot handle]**. It will walk you through each step.
>
> See you soon,
> **TrackFlow People Team**

*Note: if the employee is assigned to Los Angeles, the agent may send the email in English. If the student has implemented bilingual support, the English template is the default for US-based staff.*

---

## Onboarding instructions

The agent delivers these instructions to the new hire at step 7, after identity verification:

> Welcome to TrackFlow! To complete your onboarding, please confirm the following details one at a time:
>
> 1. What is your full name as it appears on your ID document or passport?
> 2. Which operation will you be working at? (Los Angeles / Zaragoza)
> 3. What is your assigned shift? (morning / afternoon / night)
> 4. What is your PPE size? Please provide your glove size (S / M / L / XL) and your vest size (S / M / L / XL / XXL).
> 5. Confirm that you have completed the warehouse safety training and provide the date you finished it.
> 6. Confirm that you have met your direct supervisor and provide their name.
>
> Once I have received all your responses, I will mark your onboarding as complete and let Elena know.

---

## Required deliverables and how the agent verifies each one

| # | Deliverable | What the agent expects |
|---|---|---|
| 1 | Full name | Free text (first and last name) |
| 2 | Assigned operation | "Los Angeles" or "Zaragoza" |
| 3 | Assigned shift | "morning", "afternoon", or "night" |
| 4 | PPE size | Glove size + vest size (e.g. "gloves M, vest L") |
| 5 | Safety training confirmation | Explicit confirmation + date (e.g. "Completed 3 May") |
| 6 | Supervisor confirmation | Explicit confirmation + supervisor's name |

The process is marked as **complete** when the agent has received a response to all six points.

---

## Memory schema per employee

```
employee:
  full_name: string
  email: string
  operation: "Los Angeles" | "Zaragoza" | null
  shift: "morning" | "afternoon" | "night" | null
  glove_size: string | null
  vest_size: string | null
  safety_training_completed: boolean
  safety_training_date: string | null
  supervisor_confirmed: boolean
  supervisor_name: string | null
  status: "not_started" | "active" | "completed"
  start_date: string
  close_date: string | null
```

---

## Business rules

- The assigned operation (`operation` field) determines the employment context: Los Angeles operates under California law, Zaragoza under Spanish law. The agent applies no differential logic — it only records the value.
- Safety training is mandatory for all warehouse roles. The process cannot be marked as complete if `safety_training_completed` is `false`.
- For night shifts, Elena requires the supervisor's name as an explicit confirmation, since night shift assignment requires additional sign-off from the operations lead. The agent records the name without validating it.
- The daily summary is especially useful for Elena during high-volume hiring periods: it gives her an at-a-glance view of how many processes are open simultaneously and how many have gone more than 24 hours without progress.
