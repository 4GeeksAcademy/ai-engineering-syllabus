# BRIEFING — HealthCore
## Onboarding Agent with Memory · W6D16

---

## The company

HealthCore operates 12 outpatient clinics in the United States (Texas, Florida, Georgia) and the United Kingdom (London and Manchester). Onboarding clinical staff involves mandatory regulatory compliance requirements: no staff member may access systems containing patient data until they have completed the required training in HIPAA (US) or UK GDPR (UK). Diane Foster (VP of People, Austin) is the HR lead and the person who interacts with the agent.

---

## HR character

| Field | Value |
|---|---|
| Name | Diane Foster |
| Role | VP of People |
| Location | Austin, TX |
| Communication style | Structured and methodical. Her messages are clear and she expects equally precise responses. |
| Telegram handle | `@diane_healthcore` |

---

## Welcome email template

> **Subject:** Welcome to HealthCore — complete your onboarding to get started
>
> Hi [name],
>
> Welcome to the HealthCore team. To ensure you're set up correctly and in compliance with our regulatory requirements, please complete your onboarding before your first day.
>
> Message our onboarding bot on Telegram at **[bot handle]** to begin. The bot will guide you through each step.
>
> Important: access to clinical systems will only be granted once all onboarding steps are confirmed.
>
> Best regards,
> **HealthCore People Team**

---

## Onboarding instructions

The agent delivers these instructions to the new hire at step 7, after identity verification:

> Welcome to HealthCore. To complete your onboarding, please provide the following information one step at a time:
>
> 1. What is your full legal name as it appears on your professional licence or ID?
> 2. Which clinic and country have you been assigned to? (e.g. "Austin Clinic 2, US" or "London North, UK")
> 3. What is your professional licence number? (If you are in an administrative role, reply "N/A".)
> 4. What is the expiry date of your professional licence? (Skip this step if you answered N/A above.)
> 5. Confirm that you have completed the mandatory compliance training module (HIPAA for US staff, UK GDPR for UK staff) and provide the date of completion.
> 6. Confirm that you have received your system login credentials from IT and provide the date you received them.
>
> Once I have received all your responses, I will mark your onboarding as complete and notify the People team.

---

## Required deliverables and how the agent verifies each one

| # | Deliverable | What the agent expects |
|---|---|---|
| 1 | Full legal name | Free text (first and last name) |
| 2 | Assigned clinic and country | Clinic name + country (e.g. "Austin Clinic 2, US") |
| 3 | Professional licence number | Number, or "N/A" for administrative roles |
| 4 | Licence expiry date | Date, or skipped if step 3 was N/A |
| 5 | Compliance training confirmation | Explicit confirmation + date (e.g. "Completed 10 May") |
| 6 | IT credentials confirmation | Explicit confirmation + date received |

The process is marked as **complete** when the agent has received a response to all applicable steps based on the employee's role.

---

## Memory schema per employee

```
employee:
  legal_name: string
  email: string
  assigned_clinic: string | null
  country: "US" | "UK" | null
  licence_number: string | null
  licence_expiry: string | null
  compliance_completed: boolean
  compliance_date: string | null
  it_credentials_received: boolean
  it_credentials_date: string | null
  status: "not_started" | "active" | "completed"
  start_date: string
  close_date: string | null
```

---

## Business rules

- The `licence_number` field is mandatory for clinical roles (physician, nurse practitioner, nurse). For administrative roles, "N/A" is accepted and steps 3 and 4 are automatically marked as complete.
- The compliance step is a hard blocker: the process cannot be marked as complete if `compliance_completed` is `false`, regardless of whether all other steps are done.
- The country determines which compliance module applies: HIPAA for US staff, UK GDPR for UK staff. The agent does not validate the content of the module — only the confirmation and the date.
- The daily summary is especially important here: Diane needs visibility on who has not completed compliance training before their first day.
