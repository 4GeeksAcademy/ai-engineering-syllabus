# BRIEFING — Brasaland
## Onboarding Agent with Memory · W6D16

---

## The company

Brasaland is a grilled food restaurant chain with 14 locations in Colombia and Florida. Kitchen and floor staff turn over frequently, making onboarding processes constant and often simultaneous. Ashley Turner (People Manager, Miami) is the HR lead for the entire chain and the person who interacts with the agent.

---

## HR character

| Field | Value |
|---|---|
| Name | Ashley Turner |
| Role | People Manager |
| Location | Miami |
| Communication style | Short and direct messages. Expects concrete confirmations with no small talk. |
| Telegram handle | `@ashley_brasaland` |

---

## Welcome email template

> **Subject:** Welcome to Brasaland — next steps to complete your onboarding
>
> Hi [name],
>
> We're glad to have you joining the Brasaland team. Before your first day, we need to complete a few steps to get you set up.
>
> Please message our onboarding bot on Telegram to continue the process. You'll find it at **[bot handle]**.
>
> Once you make contact, the bot will guide you through everything you need to do.
>
> See you soon,
> **Brasaland People Team**

*Note: the email is sent in English because Ashley operates from Miami and the corporate template is in English. If the student has implemented bilingual support, a Spanish version may be sent to staff at Colombian locations.*

---

## Onboarding instructions

The agent delivers these instructions to the new hire at step 7, after identity verification:

> Welcome to the Brasaland team. To complete your onboarding, please confirm the following points one at a time:
>
> 1. What is your full name as it appears on your ID document?
> 2. Which location have you been assigned to? (city and location name)
> 3. What is your bank account number for payroll?
> 4. What is your uniform size? (XS / S / M / L / XL / XXL)
> 5. Confirm that you have read the Food Handling Manual and provide the date you completed it.
> 6. Confirm that you have completed the kitchen walkthrough with your supervisor and provide their name.
>
> Once I have received all your responses, I will mark your onboarding as complete and notify HR.

---

## Required deliverables and how the agent verifies each one

| # | Deliverable | What the agent expects |
|---|---|---|
| 1 | Full name | Free text (first and last name) |
| 2 | Assigned location | City + location name (e.g. "Miami, Brickell") |
| 3 | Bank account number | Account number (free text) |
| 4 | Uniform size | One of: XS / S / M / L / XL / XXL |
| 5 | Manual confirmation | Explicit confirmation + date (e.g. "Read on 12 May") |
| 6 | Walkthrough confirmation | Explicit confirmation + supervisor's name |

The process is marked as **complete** when the agent has received a response to all six points.

---

## Memory schema per employee

```
employee:
  full_name: string
  email: string
  assigned_location: string | null
  uniform_size: string | null
  bank_account: string | null
  manual_confirmed: boolean
  manual_date: string | null
  walkthrough_confirmed: boolean
  walkthrough_supervisor: string | null
  status: "not_started" | "active" | "completed"
  start_date: string
  close_date: string | null
```

---

## Business rules

- An employee can be assigned to any of the 14 locations. The agent does not validate which one — it only records what it is told.
- The bank account number may be Colombian (savings or current account) or American (routing + account number). The agent accepts any format.
- The process has no forced deadline, but the daily summary allows Ashley to detect cases that have been inactive for more than 48 hours.
