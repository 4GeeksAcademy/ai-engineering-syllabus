# BRIEFING.md — Brasaland

## Agentic Engineering – Onboarding Agent

_Estas instrucciones están [disponibles en español](./brasaland-BRIEFING.es.md)._

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Brasaland** is a grilled food restaurant chain founded in 2008 in Medellín, Colombia. What began as a single family-run location has grown into a chain of 14 company-owned restaurants operating in Colombia and the United States (Florida). The company employs approximately 115 people between kitchen and floor staff, operations management, and the corporate team headquartered in Medellín with a commercial office in Miami. Annual revenue sits around 6 million dollars. The brand is built on three pillars: consistent product quality across every location, a warm and reliable customer experience, and speed of service.

---

## Your department and the problem you must solve

You work in **Brasaland Digital**, the internal team created by CEO Mariana Restrepo to lead the company's digital transformation, and you report to CTO Nicolás Park.

Brasaland's corporate team is growing: new people in Brasaland Digital, Marketing, Procurement, Operations, and People, in both Medellín and Miami. Every new hire gets a welcome PDF, a call with their manager, and access to a Google Drive folder nobody can navigate. New corporate staff take weeks to understand how a Brasaland restaurant works on the inside, why the company operates in two currencies, or what "consistency" means for the brand. And the paperwork (contract, documents, system access) depends on Ashley remembering to chase each person.

Ashley Turner, People Manager, needs an orchestrator that takes every new corporate hire through a complete, verifiable path.

---

## Your stakeholder

**Ashley Turner**, People Manager (Miami)

> Hi team,
>
> Following up on our conversation about corporate onboarding. Here is what I need, in order of priority:
>
> 1. Every new corporate hire, whether in Medellín or Miami, must go through the same five content stages: the company, how our restaurants operate, their role, how we work, and our guidelines. No skipping, no shortcuts.
> 2. Each content stage must end with a short check. If they don't pass it, they review the material again. I don't want "I read it" — I want evidence they understood it.
> 3. Every new hire must spend one shadowing day at a restaurant before finishing onboarding. Corporate people who have never seen a kitchen at peak hour make poor decisions about it. Felipe's team must confirm the day happened.
> 4. Their direct manager signs off the role stage, and I sign off the final closure. Nobody else.
> 5. Questions must be answered from our official documents only. If the answer isn't there, route the question to me.
> 6. Contract and payroll documents are handled by my team. The system should know whether they've been received, but I don't want IDs or bank details floating around in chat logs. That's a legal risk in both countries.
>
> Target: full onboarding in 10 business days.
>
> Thanks,
> Ashley

---

## Language scope

- Multilingual support is **optional but highly recommended**, since Brasaland hires people in both Colombia and the United States.
- Choose one **base language** for the whole flow (content, checks, agent messages).
- If you implement a second language, treat it as an enhancement: the official material and the checks must exist in that language too. The agent never translates official content on the fly when that content doesn't exist.

---

## Who is being onboarded

Only Brasaland **corporate staff**: Brasaland Digital, Marketing, Procurement, Operations (supervisors and central team, not floor or kitchen staff), People, and Training. Based in Medellín or Miami.

Each new hire has: name, role, department, office (Medellín or Miami), direct manager, and start date.

---

## Onboarding stages

| #   | Stage                     | Content                                                                                                                        | Exit condition                               | Deadline | Approved by           |
| --- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | -------- | --------------------- |
| 1   | Welcome and paperwork     | Receipt of signed contract and payroll documents                                                                               | People marks documents as received           | Day 2    | People team           |
| 2   | The company               | History since 2008, the three brand pillars, the 14 locations, the two markets                                                 | Check passed                                 | Day 3    | Automatic             |
| 3   | How a restaurant operates | Shifts, covers, average ticket, ingredient orders, waste control, operating in COP and USD                                     | Check passed                                 | Day 5    | Automatic             |
| 4   | Shadowing day             | One full day at a restaurant in their city                                                                                     | An Operations supervisor confirms the day    | Day 7    | Operations supervisor |
| 5   | Your role                 | Role responsibilities, 90-day goals, who they work with                                                                        | Check passed **and** direct manager approval | Day 8    | Direct manager        |
| 6   | How we work               | Tools (Slack, Notion, Google Workspace, backoffice), Notion specs with acceptance criteria, working between Medellín and Miami | Check passed                                 | Day 9    | Automatic             |
| 7   | Guidelines                | Brand guide, data protection policy, code of conduct, labour differences between Colombia and the US                           | Check passed                                 | Day 9    | Automatic             |
| 8   | Access and closure        | Confirmation of active system access and onboarding closure                                                                    | Ashley approves closure                      | Day 10   | Ashley Turner         |

Stage 4 cannot start before stage 3 is passed.

---

## Official material you must prepare

Using Brasaland's general briefing, create one official document per content stage (2, 3, 5, 6, and 7). For stage 5, prepare at least two role variants (e.g., Brasaland Digital analyst and Marketing coordinator). These documents are the only source the agent can use to present content and answer questions.

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
- **Escalation** to Ashley when an onboarding accumulates more than 3 days of total delay.
- If the direct manager **rejects** stage 5, the flow returns to the start of that stage with a comment visible to the new hire.

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Identity document number (cédula, SSN, passport)
- Bank details for payroll
- Salary and contract compensation terms

The agent only works with the **status** of each paperwork item ("contract received," "payroll documents pending"), never with its content.

---

## Seed data

Create at least:

- 3 test onboardings with fictional data: one in Medellín, one in Miami, and a third stuck at stage 4 with its deadline passed (to test escalation)
- 2 direct managers from different departments
- 1 Operations supervisor with permission to confirm the shadowing day
- The 5 official content documents

---

## Specific restriction

The orchestrator is for **corporate staff**. If someone tries to start an onboarding for a floor or kitchen role, the system must reject it with the message: "This flow is for corporate team hires. Restaurant hires are managed with their location manager."
