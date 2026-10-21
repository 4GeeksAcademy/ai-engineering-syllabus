# BRIEFING.md — HealthCore

## Agentic Engineering – Onboarding Agent

_Estas instrucciones están [disponibles en español](./healthcore-BRIEFING.es.md)._

> This document describes your company and the specific situation you're building this project for. Read it completely before writing any code. Everything you build must reflect this context.

---

## Your company

**HealthCore** is an outpatient healthcare services company founded in 2011 in Austin, Texas. It operates a network of 12 clinics: 9 in the United States (Texas, Florida, and Georgia) and 3 in the United Kingdom (London and Manchester), offering primary care, specialist consultations, chronic disease management, and preventive health programmes. It employs approximately 200 people and generates around 28 million dollars in annual revenue. It operates under two health data protection frameworks: HIPAA in the United States and UK GDPR in the United Kingdom.

---

## Your department and the problem you must solve

You are part of **HealthCore Digital**, the internal unit created by CEO Dr. Sandra Okonkwo to build the infrastructure clinical and operational teams need, and you report to CTO James Osei.

HealthCore's corporate team is growing in Austin and London: new people in HealthCore Digital, Revenue Cycle, Compliance, Patient Experience, and People. Onboarding is inconsistent, and Diane has already spotted the most serious problem: **some people receive access to systems with patient data before completing mandatory compliance training.** In a regulated environment, that isn't an administrative slip — it's a legal risk. On top of that, new non-clinical hires take weeks to understand what a patient's journey looks like, why the no-show rate matters so much, or what "minimum necessary" means when accessing data.

Diane Foster, VP of People, needs an orchestrator that guarantees the right order and leaves evidence of every step.

---

## Your stakeholder

**Diane Foster**, VP of People (Austin)

> Team,
>
> I've put the full spec in Notion. Here are the essentials:
>
> 1. **Order is not optional.** No new hire gets access to any system with patient information until they've passed the compliance stage and Claire has approved it. If the system allows skipping this step, it's of no use to us.
> 2. Five content blocks: the company, how we operate, their role, how we work, and our compliance guidelines. Each with a check.
> 3. Background checks are run by an external provider. The system only needs to know whether it's **completed**. The outcome must never enter the system.
> 4. The direct manager approves the role stage. Claire approves compliance. I approve the closure.
> 5. Questions are answered from official documentation, citing the relevant policy. Compliance questions that aren't covered go to Claire, not to me.
>
> Target: 10 business days. There are no shortcuts on compliance: if it takes longer, it takes longer.
>
> Thanks,
> Diane

---

## Language scope

- The base language is **English**, since both corporate offices (Austin and London) work in English.
- Spanish is **optional but recommended** for Florida hires. If you implement it, the official material and the checks must exist in Spanish too. The agent never translates official content on the fly when that content doesn't exist — least of all a compliance policy.

---

## Who is being onboarded

Only HealthCore **non-clinical corporate staff**: HealthCore Digital, Revenue Cycle and Billing, Compliance and Data Governance, Patient Experience (central coordination), People, and Executive Direction. Based in Austin or London.

Physicians, nurses, and direct-care clinic staff are not included: their onboarding has licensure and credentialing requirements that are out of scope for this project.

Each new hire has: name, role, department, office (Austin or London), applicable regulatory framework (HIPAA or UK GDPR), direct manager, and start date.

---

## Onboarding stages

| #   | Stage                 | Content                                                                                                                                           | Exit condition                                                | Deadline | Approved by      |
| --- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------- | ---------------- |
| 1   | Welcome and paperwork | Receipt of signed contract, payroll documents, and confirmation that the background check is completed                                            | People marks documents as received and the check as completed | Day 2    | People team      |
| 2   | The company           | History since 2011, the 12-clinic network, service lines, value proposition (accessibility, same-day appointments, bilingual care)                | Check passed                                                  | Day 3    | Automatic        |
| 3   | How we operate        | Patient journey: booking → visit → clinical documentation → billing → follow-up. No-shows, referrals, and billing denials as operational problems | Check passed                                                  | Day 4    | Automatic        |
| 4   | Compliance            | HIPAA and UK GDPR, the "minimum necessary" principle, incident notification (72 hours in the UK, 60 days in the US), access logging               | Check passed **and** Compliance approval                      | Day 6    | Claire Whitfield |
| 5   | Your role             | Role responsibilities, 90-day goals, who they work with                                                                                           | Check passed **and** direct manager approval                  | Day 8    | Direct manager   |
| 6   | How we work           | Tools (Jira, Notion, Slack, Microsoft 365), working between Austin and London, how a new system or integration gets approved                      | Check passed                                                  | Day 9    | Automatic        |
| 7   | Access and closure    | Access requests for the department's systems and onboarding closure                                                                               | Diane approves closure                                        | Day 10   | Diane Foster     |

Stage 4 must be **approved** before any access request to a system with patient information can be issued.

---

## Official material you must prepare

Using HealthCore's general briefing, create one official document per content stage (2, 3, 4, 5, and 6). For stage 4, prepare two variants: one for hires under HIPAA and one under UK GDPR. For stage 5, prepare at least two role variants (e.g., HealthCore Digital engineer and Revenue Cycle analyst). These documents are the only source the agent can use.

---

## Comprehension checks

- 4 to 6 questions per content stage, based only on the official material.
- Pass threshold: 80%. For stage 4 (compliance) the threshold is **100%**.
- If not passed, the agent presents the missed points again and repeats the check with different questions.
- After two failed attempts at stage 4, the agent notifies Claire Whitfield. For all other stages, the direct manager.

---

## Approvals and escalation

- **Reminder** to the new hire 24 hours before each stage's deadline.
- **Escalation** to the direct manager when a stage goes past its deadline.
- Stage 4 **doesn't escalate on deadline**: if it's delayed, Diane is notified, but no path to skip it is ever offered.
- Uncovered compliance questions are routed to Claire. All other uncovered questions, to Diane.
- If an approver **rejects** a stage, the flow returns to the start of that stage with a comment visible to the new hire.

---

## Sensitive data

Must never appear in logs, stored prompts, agent messages, or API responses:

- Identity or tax document number (SSN, National Insurance Number, passport)
- Bank details for payroll
- Salary and contract compensation terms
- **Any detail of the background check.** Only its completion is recorded, never its outcome or content

In addition, stage 3 material may describe a patient's journey, but it **must not contain real or realistic patient data**. Use generic examples.

---

## Seed data

Create at least:

- 3 test onboardings with fictional data: one in Austin, one in London, and a third that tries to request access without stage 4 approved (to test the block)
- 2 direct managers from different departments
- 1 Compliance user with permission to approve stage 4
- The official content documents, including both compliance variants

---

## Specific restriction

Any attempt to request access to a system with patient information before stage 4 is approved must be rejected, logged as a security event, and reported to Claire Whitfield.
