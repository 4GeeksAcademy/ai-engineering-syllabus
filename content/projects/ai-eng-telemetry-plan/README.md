# Company's Telemetry plan design

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing a single line — it defines the KPIs, entities, and key processes of your company, which are the foundation on which you will build this plan.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company already has an inventory management system in production: a FastAPI backend with authentication, a relational data model in Supabase, and a non-negotiable business rule — stock cannot be modified directly, only through inbound and outbound orders traceable to a user. The system works. But the operations team has no idea what is happening inside it.

The management team has filed an RFI with the technology team: they want to know whether the inventory system can generate actionable business information — consumption trends, early stock alerts, error patterns — or whether they need external tools for that. Your tech lead has assigned you the task of responding to that RFI with a **Telemetry Plan**: a technical document that identifies what data is worth capturing from the inventory system, why, and how to structure it before writing a single line of instrumentation.

### 📚 Complementary Knowledge — What Makes a Telemetry Event Valuable

Telemetry is not generated just to have data: it is generated to answer business questions that cannot be answered today. The difference between a useful telemetry system and one that nobody maintains is whether each event exists for a reason.

**The golden rule:** if you cannot complete this sentence, the event does not exist — _"We capture `[event_name]` because we need to know `[hypothesis]`, which allows us to make the decision `[concrete decision]`."_

Two concepts you will need to apply today:

- **Batch vs. stream:** Does the business need to see this data within seconds (stream), or is it sufficient to process it in periodic batches (batch)? The answer determines the technical design of the pipeline you will build in the following days.
- **Event Envelope:** the standard structure every event must follow — a unique identifier (`eventId`), ISO 8601 timestamp (`timestamp`), session/user identifiers (`sessionId`, `userId`), the event name using a consistent taxonomy (`entity_action`, e.g. `order_submitted`), schema version (`schemaVersion`), a correlation identifier (`requestId`/`traceId` to join frontend–backend–logs), and the event-specific properties. A well-designed envelope today prevents duplicates, makes debugging easier, and keeps the pipeline robust.

---

> Your tech lead sent you this message:
>
> > "We've had the inventory system running for weeks and the operations team is starting to ask things we can't answer: how many outbound orders are registered per day? Which products accumulate the most validation errors? Are there users attempting to modify stock directly and getting rejected by the system? When do the minimum stock threshold alerts fire the most?
> >
> > And it's not just the inventory. The backoffice has other sections that are black boxes today: how many failed login attempts happen per day? Which sections do operators visit most? Are there flows that get abandoned halfway through? Any part of the application a user touches is a data opportunity.
> >
> > Before we instrument anything, I need a design document. Start from the model we already have — `Product`, `InboundOrder`, `OutboundOrder`, the `/inventory` router — but don't stop there. Identify the three main business KPIs, map the events that feed them, define their full envelope, and justify whether each should be processed as stream or batch. Don't write code yet — write the plan the team will implement tomorrow.
> >
> > The deliverable is a **Telemetry Plan** in Markdown plus a JSON schema file. We review on Friday."

---

## 🌱 How to Start the Project

1. Open your fork of your assigned company's monorepo.
2. Read your `CONTEXT-company.md` in full and locate the KPIs, the inventory system entities (products, orders), and the business constraints defined for your company.
3. Create the `docs/telemetry/` folder inside the monorepo.
4. Work on both deliverables inside that folder: `telemetry-plan.md` and `event-schemas.json`.

There is no new server to spin up today. The deliverable is design documentation — but documentation precise enough that another developer can instrument it into the existing inventory system without asking you questions.

---

## 💻 What You Need to Do

### Phase 1 — KPI Analysis and Data Opportunities

- [ ] Identify the **3 main KPIs** of your company from your `CONTEXT-company.md`. For each KPI, answer: what data makes it up? Where is that data generated in the system?
- [ ] Map the **inventory management flow** in your application: from when an authenticated user accesses the system to when they complete an inbound or outbound order. Identify at least **5 instrumentation points** in that flow — including direct stock modification attempts (which the system rejects), failed validations, and minimum threshold activations.
- [ ] Explore other backoffice sections that can also provide valuable data: authentication (login attempts, expired sessions, credential failures), navigation (which sections operators visit and how often), and any flow a user might abandon before completing. Document at least **2 additional opportunities** outside the inventory module.
- [ ] For each instrumentation point, complete the sentence: _"We capture `[event]` because we need to know `[hypothesis]`, which allows us to make the decision `[decision]`."_ If you cannot complete it, discard the point.

⚠️ **IMPORTANT:** The KPIs, entities, and identifiers in your plan must match exactly what your CONTEXT.md specifies. A generic implementation that ignores your company's context will not be accepted.

### Phase 2 — Event Envelope Design

- [ ] Define the **standard Event Envelope** your company will use: the mandatory fields every event must include (`eventId`, `timestamp` in ISO 8601, `sessionId`, `userId`, event name, `schemaVersion`, `requestId`/`traceId` for correlation, and event-specific properties).
- [ ] Design the complete schema for **at least 5 events** derived from the flow mapped in Phase 1. Each event must be named following the `entity_action` taxonomy with consistent verbs (e.g. `inbound_order_created`, `stock_threshold_triggered`, `direct_stock_edit_rejected`, `session_expired`).
- [ ] For each event, define a **property allowlist**: an explicit list of the permitted keys for that event. Nothing outside the allowlist should be included — this prevents accidental data leakage.
- [ ] For each event, specify: name, description, properties (name, type, required/optional, description), and whether it contains sensitive data or PII — in which case document how it is anonymised or sanitised before the event is emitted.
- [ ] Export the schemas to the `event-schemas.json` file with a validatable structure (you may use JSON Schema draft-07 or a documented custom structure).

### Phase 3 — Delivery Strategy

- [ ] For each event designed, decide and justify whether it should be processed as **stream** (real time) or **batch** (periodic batches). The justification must be based on the urgency of the business decision it feeds, not on technical preference.
- [ ] Document the **throttle/debounce strategy** for high-frequency events (if any exist in your design).
- [ ] Write a **risks and exclusions** section in the plan: events that were discarded and why, data that will not be captured for privacy or cost reasons.

---

## ✅ What We Will Evaluate

- [ ] The 3 KPIs identified are representative of the assigned company's business and are justified with data from `CONTEXT-company.md`
- [ ] Every event has a hypothesis and a business decision that justifies it — no "just in case" events
- [ ] The Event Envelope is consistent across all events and contains at least: `eventId`, `timestamp` (ISO 8601), `sessionId`, `userId`, event name in `entity_action` format, `schemaVersion`, and `requestId`/`traceId`
- [ ] Every event has a documented **property allowlist** — only explicitly permitted keys
- [ ] The `event-schemas.json` file is valid and the schemas are consistent with the Markdown plan
- [ ] The stream/batch decision is justified by business urgency, not technical preference
- [ ] Sensitive data or PII is identified and documented with its anonymisation or sanitisation strategy
- [ ] The risks and exclusions section demonstrates critical thinking: events were discarded for a reason
- [ ] The plan is precise enough for another developer to instrument it without needing clarification

---

## 📦 How to Submit

1. Make sure the files `docs/telemetry/telemetry-plan.md` and `docs/telemetry/event-schemas.json` are in your fork.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W16D46] Telemetry Design Plan`.
3. In the PR description, include:
   - The 3 KPIs identified (one line each)
   - The number of events designed
   - One sentence explaining the hardest design decision you made

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
