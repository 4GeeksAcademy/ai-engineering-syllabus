# BRIEFING.md — Nexova

## Agentic Engineering – Onboarding Agent

_Estas instrucciones están [disponibles en español](./nexova-BRIEFING.es.md)._

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**Nexova** is a human resources consulting and talent acquisition firm founded in 2011, headquartered in Valencia, Spain, with an expansion office in Miami, Florida. It has 120 employees and operates three business lines: executive and mid-management headhunting, customer support team outsourcing for technology companies, and corporate training in soft skills and leadership. It generates approximately 8 million dollars in annual revenue. Its clients are mainly mid-sized companies in technology, retail, and financial services.

---

## Your department and the problem you must solve

You are part of the AI Engineering team CEO Laura Mendoza assembled to turn AI into Nexova's competitive advantage, and you report to CTO Sergio Molina.

Nexova hires often: selection consultants, SDRs, support agents, trainers, and internal staff. Today, Patricia Solís sends each new hire a PDF with instructions and follows up on Slack, one message at a time. New hires take weeks to understand how the three business lines relate to each other, what a selection process looks like end to end, or why candidate data is never shared outside Selection. And the confidentiality agreement — essential in a business that handles candidate profiles and client data — sometimes gets signed after the person already has access to the ATS.

Patricia needs an orchestrator that turns that PDF and those messages into a complete, verifiable path, in the right order.

---

## Your stakeholder

**Patricia Solís**, HR Manager (Valencia)

> Hi,
>
> Here's a summary of what I need for onboarding, because I've been doing this by hand for years and I know exactly where it breaks.
>
> 1. Everyone who joins Nexova has to understand all three business lines, not just their own. A selection consultant who doesn't know what Training does misses cross-selling opportunities every single day.
> 2. Five content blocks: the company, how we operate, their role, how we work, and our guidelines. Each with a check at the end. If they don't pass, they review.
> 3. Most important: **nobody gets access to the ATS, HubSpot, or the helpdesk until they've signed the confidentiality agreement and passed the guidelines block.** This is non-negotiable. We've had scares before.
> 4. The direct manager approves the role block. I approve the closure.
> 5. If they ask something that isn't in our documentation, I don't want the system making it up. Send it to me.
>
> Target: 8 business days.
>
> Patricia

---

## Language scope

- Multilingual support is **optional but highly recommended**, since Nexova hires in both Valencia and Miami.
- Choose one **base language** for the whole flow (content, checks, agent messages).
- If you implement a second language, the official material and the checks must exist in that language too. The agent never translates official content on the fly when that content doesn't exist.

---

## Who is being onboarded

Any new member of Nexova's staff, in Valencia or Miami, in any department: Talent Selection, Sales, Customer Support, Corporate Training, Marketing, Internal HR, or Technology.

Each new hire has: name, role, department, office (Valencia or Miami), direct manager, and start date.

---

## Onboarding stages

| #   | Stage                     | Content                                                                                                                                                              | Exit condition                               | Deadline | Approved by    |
| --- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | -------- | -------------- |
| 1   | Welcome and paperwork     | Receipt of signed contract and payroll documents                                                                                                                     | HR marks documents as received               | Day 1    | HR team        |
| 2   | Confidentiality agreement | Signature of the confidentiality agreement covering candidate and client data                                                                                        | HR marks the agreement as signed             | Day 2    | HR team        |
| 3   | The company               | History, the three business lines, client profile, the AI bet, Valencia and Miami                                                                                    | Check passed                                 | Day 3    | Automatic      |
| 4   | How we operate            | A selection process end to end (briefing → search → shortlist → interviews → hire), how the outsourced support service works, and how training is sold and delivered | Check passed                                 | Day 4    | Automatic      |
| 5   | Your role                 | Role responsibilities, 90-day goals, who they work with                                                                                                              | Check passed **and** direct manager approval | Day 6    | Direct manager |
| 6   | How we work               | Tools (HubSpot, ATS, helpdesk, Slack, Google Workspace) by department, CRM logging best practices                                                                    | Check passed                                 | Day 7    | Automatic      |
| 7   | Guidelines                | Candidate and client confidentiality, GDPR, candidate exclusivity across processes, code of conduct                                                                  | Check passed                                 | Day 7    | Automatic      |
| 8   | Access and closure        | Access requests for the department's systems and onboarding closure                                                                                                  | Patricia approves closure                    | Day 8    | Patricia Solís |

The access requests in stage 8 can **only** be issued once stages 2 and 7 are complete.

---

## Official material you must prepare

Using Nexova's general briefing, create one official document per content stage (3, 4, 5, 6, and 7). For stage 5, prepare at least two role variants (e.g., selection consultant and SDR). For stage 6, the content must change according to the person's department. These documents are the only source the agent can use.

---

## Comprehension checks

- 4 to 6 questions per content stage, based only on the official material.
- Pass threshold: 80%. For stage 7 (guidelines) the threshold is **100%**: confidentiality doesn't allow approximations.
- If not passed, the agent presents the missed points again and repeats the check with different questions.
- After two failed attempts, the agent notifies the direct manager.

---

## Approvals and escalation

- **Reminder** to the new hire 24 hours before each stage's deadline.
- **Escalation** to the direct manager when a stage goes past its deadline.
- **Escalation** to Patricia when stage 2 (confidentiality) goes past its deadline, since it blocks system access.
- If the direct manager **rejects** stage 5, the flow returns to the start of that stage with a comment visible to the new hire.

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Identity document number (DNI, NIE, SSN, passport)
- Bank details for payroll
- Salary and contract compensation terms

The agent only works with the **status** of each paperwork item ("agreement signed," "documents pending"), never with its content.

---

## Seed data

Create at least:

- 3 test onboardings with fictional data: one in Valencia, one in Miami, and a third stuck at stage 2 with its deadline passed (to test escalation to Patricia)
- 2 direct managers from different departments
- The 5 official content documents

---

## Specific restriction

No access to systems holding candidate or client data (ATS, HubSpot, helpdesk) can be requested before the confidentiality agreement is signed and the guidelines stage is passed. If attempted, the system must reject it and show what's missing.
