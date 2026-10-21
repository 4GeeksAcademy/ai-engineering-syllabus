# BRIEFING.md — TrackFlow

## Agentic Engineering – Onboarding Agent

_Estas instrucciones están [disponibles en español](./trackflow-BRIEFING.es.md)._

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**TrackFlow** is a last-mile delivery and warehouse management company founded in 2009 in Los Angeles, United States. It operates in two markets, the United States and Spain, with warehouses in Los Angeles and Zaragoza. It employs approximately 130 people and generates around 9 million euros in annual revenue. Its clients are e-commerce fashion, electronics, and cosmetics brands that trust TrackFlow with their entire logistics operation: storage, order fulfilment, shipping through a network of 8 carriers, and returns.

---

## Your department and the problem you must solve

You are part of **TrackFlow Tech**, the internal unit created to lead the company's digital transformation, and you report to CTO Andrés Kim.

TrackFlow's corporate team is growing in both countries: new people in Technology, Commercial, Customer Experience, Reverse Logistics, and operations management. Today every new hire gets a different welcome PDF depending on the country, and an explanation of the business that depends on who gives it. A new developer in Zaragoza can spend weeks without knowing what physically happens to an order from the moment it enters the warehouse until it reaches the customer, and a new account manager in Los Angeles may not know that returns make up as much as a quarter of the volume. On top of that, system access takes days because it depends on someone remembering to request it.

Rafael Sanz, Head of People, needs an orchestrator that takes every new corporate hire through the same path, in both countries.

---

## Your stakeholder

**Rafael Sanz**, Head of People (Zaragoza)

> Hi team,
>
> Here are the requirements for the new corporate onboarding. I've also put them in Notion with the details for each stage.
>
> **Goal:** anyone joining the corporate team, in Los Angeles or Zaragoza, should understand how TrackFlow works end to end before they start making decisions about it.
>
> **Content stages:** the company, how we operate, their role, how we work, and our guidelines. Each one ends with a check. No passing, no moving on.
>
> **Warehouse visit:** every new hire spends half a day at the warehouse in their country. The warehouse manager confirms it. It's the stage people value most afterwards and the one most often forgotten when scheduling.
>
> **Approvals:** the direct manager approves the role stage. I approve the closure.
>
> **Questions:** answered from official documentation, citing where the answer comes from. If it isn't documented, it comes to me. I'd rather have an unanswered question than an invented answer.
>
> **Contract:** each country has its own labour framework. The system must know which documents apply to each and whether they've been received, but the content of those documents must not leave my team.
>
> **Target:** 10 business days.
>
> Thanks,
> Rafael

---

## Language scope

- Multilingual support is **optional but highly recommended**, since TrackFlow hires in both the United States and Spain.
- Choose one **base language** for the whole flow (content, checks, agent messages).
- If you implement a second language, the official material and the checks must exist in that language too. The agent never translates official content on the fly when that content doesn't exist.

---

## Who is being onboarded

Only TrackFlow **corporate staff**: Technology, Commercial and Client Relations, Customer Experience, Reverse Logistics, People, and operations management (shift leads, coordinators, analysts). Warehouse operatives are not included.

Each new hire has: name, role, department, country (United States or Spain), direct manager, and start date.

---

## Onboarding stages

| #   | Stage                 | Content                                                                                                                                          | Exit condition                               | Deadline | Approved by       |
| --- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | -------- | ----------------- |
| 1   | Welcome and paperwork | Receipt of signed contract and the employment documents that apply to the country                                                                | People marks documents as received           | Day 2    | People team       |
| 2   | The company           | History since 2009, value proposition for brands, client profile, the two markets                                                                | Check passed                                 | Day 3    | Automatic         |
| 3   | How we operate        | Order lifecycle: warehouse inbound → picking → carrier assignment → delivery → return. The two warehouses, the 8 carriers, the weight of returns | Check passed                                 | Day 5    | Automatic         |
| 4   | Warehouse visit       | Half a day at the warehouse in their country                                                                                                     | The warehouse manager confirms the visit     | Day 6    | Warehouse manager |
| 5   | Your role             | Role responsibilities, 90-day goals, who they work with                                                                                          | Check passed **and** direct manager approval | Day 8    | Direct manager    |
| 6   | How we work           | Tools (Slack, Notion, Linear/Jira, Google Workspace), working across two time zones 9 hours apart, technical specs and tickets                   | Check passed                                 | Day 9    | Automatic         |
| 7   | Guidelines            | Confidentiality of client brand data, end-consumer data protection, information security, code of conduct                                        | Check passed                                 | Day 9    | Automatic         |
| 8   | Access and closure    | Confirmation of active system access and onboarding closure                                                                                      | Rafael approves closure                      | Day 10   | Rafael Sanz       |

Stage 4 cannot start before stage 3 is passed.

---

## Employment documents by country

| Country       | Required documents                                                                  |
| ------------- | ----------------------------------------------------------------------------------- |
| United States | Signed contract, employee tax withholding form, employment eligibility verification |
| Spain         | Signed contract, Social Security registration details, tax withholding form         |

The system only records whether each document is **pending** or **received**.

---

## Official material you must prepare

Using TrackFlow's general briefing, create one official document per content stage (2, 3, 5, 6, and 7). For stage 5, prepare at least two role variants (e.g., TrackFlow Tech developer and account manager). These documents are the only source the agent can use.

---

## Comprehension checks

- 4 to 6 questions per content stage, based only on the official material.
- Pass threshold: 80%.
- If not passed, the agent presents the missed points again and repeats the check with different questions.
- After two failed attempts, the agent notifies the direct manager.

---

## Approvals and escalation

- **Reminder** to the new hire 24 hours before each stage's deadline.
- **Escalation** to the direct manager when a stage goes past its deadline.
- **Escalation** to Rafael when an onboarding accumulates more than 3 days of total delay.
- Reminders and escalations are sent during the recipient's local business hours, not the server's.
- If the direct manager **rejects** stage 5, the flow returns to the start of that stage with a comment visible to the new hire.

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Identity or tax document number (SSN, DNI, NIE, passport)
- Social Security registration number
- Bank details for payroll
- Salary and contract compensation terms
- Outcome of the employment eligibility verification (only its completion is recorded)

---

## Seed data

Create at least:

- 3 test onboardings with fictional data: one in the United States, one in Spain, and a third stuck at stage 4 with its deadline passed (to test escalation)
- 2 direct managers from different departments
- 2 warehouse managers, one per country, with permission to confirm the visit
- The 5 official content documents

---

## Specific restriction

The warehouse visit can only be confirmed by the warehouse manager **of the new hire's country**. A confirmation from the other warehouse's manager must be rejected.
