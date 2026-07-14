# Designing your company's telemetry plan

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/telemetry)** before writing a single line — it defines the mandatory metrics, entities, and key processes of your company that this plan is built on.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company already has an inventory management system in production: a FastAPI backend with authentication, a relational data model in Supabase, and a non-negotiable business rule — stock cannot be modified directly, only through inbound and outbound orders traceable to a user. The system works. But the operations team has no idea what is happening inside it.

The management team has filed an **RFI** with the technology team: they want to know whether the system can generate actionable business information — and not just about the inventory, but about any part of the application a user or internal process touches. Your tech lead has assigned you the task of responding to that RFI with a **Telemetry Plan**: a technical document that identifies, as exhaustively as possible, what data is worth capturing today — and what could be valuable tomorrow, even if you don't have the exact business question it answers yet — before writing a single line of instrumentation.

### 📚 Complementary Knowledge — What Makes a Telemetry Event Valuable

Telemetry is not generated just to have data: it is generated to answer questions that cannot be answered today — or that will likely need answering tomorrow. The difference between a useful telemetry system and one that nobody maintains is whether each event exists for a reason.

**The golden rule:** if you cannot complete this sentence, the event does not exist — _"We capture `[event_type]` because we need to know `[hypothesis]`, which allows us to make the decision `[concrete decision]`."_

Your `CONTEXT-company.md` includes a set of **mandatory metrics** — specific indicators your company needs to measure from day one. These are folded into your plan as a floor, not a ceiling: around them, you must keep identifying every additional opportunity, technical and business, that you consider valuable.

Two concepts you will need to apply today:

- **Batch vs. stream:** Does the business need to see this data within seconds (stream), or is it sufficient to process it in periodic batches (batch)? The answer determines the technical design of the pipeline you will build in the following days.
- **Event Envelope:** the standard structure every event must follow — a unique identifier (`eventId`), ISO 8601 timestamp (`timestamp`), session/user identifiers (`sessionId`, `userId`), event type using a consistent taxonomy (`event_type` in `entity_action` format, e.g. `order_submitted`), schema version (`schemaVersion`), a correlation identifier (`requestId` to join frontend–backend–logs), and event-specific payload (`properties`).

---

> Your tech lead sent you this message:
>
> > "We've had the inventory system running for weeks and the operations team is starting to ask things we can't answer: how many outbound orders are registered per day? Which products accumulate the most validation errors? Are there users attempting to modify stock directly and getting rejected by the system? When do the minimum stock threshold alerts fire the most?
> >
> > And it's not just the inventory. The backoffice has other sections that are black boxes today: how many failed login attempts happen per day? Which sections do operators visit most? Are there flows that get abandoned halfway through? Any part of the application a user — or a process — touches is a data opportunity.
> >
> > Before we instrument anything, I need a design document. Don't limit yourself to a handful of business metrics: I want the most complete catalogue you can build, covering both the technical health of the system and the business questions — even if we don't know exactly what we'll use them for yet. I've already left you the metrics we need no matter what in your CONTEXT — implement those without fail, and keep exploring from there. Don't write code yet — write the plan the team will implement tomorrow."
> >
> > The deliverable is a **Telemetry Plan** in Markdown plus a JSON schema file. We review on Friday."

---

## 🌱 How to Start the Project

1. Open your fork of your assigned company's monorepo.
2. Read your `CONTEXT-company.md` in full and locate the **mandatory metrics**, the inventory system entities (products, orders), and the business constraints defined for your company.
3. Create the `docs/telemetry/` folder inside the monorepo.
4. Work on both deliverables inside that folder: `telemetry-plan.md` and `event-schemas.json`.

There is no new server to spin up today. The deliverable is design documentation — but documentation precise enough that another developer can instrument it into the existing system without asking you questions.

---

## 💻 What You Need to Do

### Phase 1 — Exhaustive Catalogue of Data Opportunities

- [ ] Review your `CONTEXT-company.md` and identify the **mandatory metrics** your company requires from day one. These are a floor, not a ceiling — they must be in your plan no matter what.
- [ ] Map the **inventory management flow** in your application: from when an authenticated user accesses the system to when they complete an inbound or outbound order. Identify at least **5 instrumentation points** in that flow — including direct stock modification attempts (which the system rejects), failed validations, and minimum threshold activations.
- [ ] Explore, without capping yourself at a minimum count, other backoffice sections that can also provide valuable data: authentication (login attempts, expired sessions, credential failures), performance (API response times, load times), uncaught frontend errors, and navigation (which sections operators visit most, which flows get abandoned). The goal is a broad catalogue, not a minimum list checked off as a formality.
- [ ] For each opportunity you identify, complete the sentence: _"We capture `[event_type]` because we need to know `[hypothesis]`, which allows us to make the decision `[decision]`."_ If you cannot complete it, discard the point.
- [ ] Classify every event in your catalogue into two groups: **mandatory** (comes from your CONTEXT) or **identified opportunity** (you proposed it). This gives the team visibility into what is baseline and what is exploration.

⚠️ **IMPORTANT:** The mandatory metrics, entities, and identifiers in your plan must match exactly what your `CONTEXT-company.md` specifies. In addition, the catalogue of additional opportunities is expected to be broad and well-grounded — a plan that only covers the mandatory minimum, without exploring the rest of the application, will not be accepted.

### Phase 2 — Event Envelope Design

- [ ] Define the **standard Event Envelope** your company will use: the mandatory fields every event must include (`eventId`, `timestamp` in ISO 8601, `sessionId`, `userId`, `event_type`, `schemaVersion`, `requestId` for correlation, and `properties` for event-specific payload).
- [ ] Design the complete schema for **all the mandatory metrics from your CONTEXT**, plus **at least 8 additional events** from your catalogue, covering at least 3 distinct categories (for example: business/inventory, authentication, performance, errors, navigation). Each `event_type` must follow the `entity_action` taxonomy with consistent verbs (e.g. `inbound_order_created`, `stock_threshold_triggered`, `direct_stock_edit_rejected`, `session_expired`, `api_latency_recorded`).
- [ ] For each event, define a **property allowlist**: an explicit list of the permitted keys for that event. Nothing outside the allowlist should be included — this prevents accidental data leakage.
- [ ] For each event, specify: `event_type`, description, `properties` (name, type, required/optional, description), and whether it contains sensitive data or PII — in which case document how it is anonymised or sanitised before the event is emitted.
- [ ] Export the schemas to the `event-schemas.json` file with a validatable structure (you may use JSON Schema draft-07 or a documented custom structure).

### Phase 3 — Delivery Strategy

- [ ] For each event designed, decide and justify whether it should be processed as **stream** (real time) or **batch** (periodic batches). The justification must be based on the urgency of the decision it feeds or the operational need to detect it quickly — not on technical preference.
- [ ] Document the **throttle/debounce** strategy for high-frequency events (if any exist in your design).
- [ ] Write a **risks and exclusions** section in the plan: events you considered and discarded, and why; data that will not be captured for privacy or cost reasons.

---

## ✅ What We Will Evaluate

- [ ] Every mandatory metric from `CONTEXT-company.md` is present and correctly identified in the plan
- [ ] The plan covers both **technical** opportunities (errors, performance, authentication, navigation) and **business** ones, broadly — not limited to a minimum count checked off as a formality
- [ ] Every event has a hypothesis and a business or operational decision that justifies it — no "just in case" events
- [ ] The Event Envelope is consistent across all events and contains at least: `eventId`, `timestamp` (ISO 8601), `sessionId`, `userId`, `event_type` in `entity_action` format, `schemaVersion`, `requestId`, and `properties`
- [ ] Every event has a documented **property allowlist** — only explicitly permitted keys
- [ ] The `event-schemas.json` file is valid and the schemas are consistent with the Markdown plan
- [ ] The stream/batch decision is justified by business or operational urgency, not technical preference
- [ ] Sensitive data or PII is identified and documented with its anonymisation or sanitisation strategy
- [ ] The risks and exclusions section demonstrates critical thinking: events were discarded for a reason
- [ ] The plan is precise enough for another developer to instrument it without needing clarification

---

## 📦 How to Submit

1. Make sure the files `docs/telemetry/telemetry-plan.md` and `docs/telemetry/event-schemas.json` are in your fork.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W16D46] Telemetry Design Plan`.
3. In the PR description, include:
   - The total number of events designed, and how many are mandatory (from CONTEXT) vs. identified by you
   - The categories covered (business, authentication, performance, errors, navigation, etc.)
   - One sentence explaining the hardest design decision you made

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
