# Company's Telemetry – Frontend capture

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: You need the approved `telemetry-plan.md` and `event-schemas.json` from Phase 1 — they are the contract you will implement today. If they are not approved, resolve that before writing any code.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The telemetry plan is approved. Today you implement the half the user never sees but that makes everything possible: the capture system in the frontend.

Every event you designed in Phase 1 must be captured at the exact moment it occurs in the backoffice, accumulated in a local queue, and sent to the backend in batches — never one by one. To verify that events are arriving correctly, you will also create a minimal receiver endpoint in FastAPI: it does not persist anything yet, it only validates the format and responds 200. Real database persistence is the work of Phase 3.

> Your tech lead sent you this message:
>
> > "I want to see events flowing before we build the storage layer. Create the `TelemetryService` in the backoffice and instrument the inventory flow with the events from the plan. So you can verify the payload is arriving correctly, add a stub endpoint in the backend — validate the format and return 200, without writing to the database yet.
> >
> > One important thing: configure the endpoint URL as an environment variable from the start. In the next phase we will replace the stub with the real implementation and the frontend should not need to change anything.
> >
> > I don't want tracking scattered across every component. Everything goes through a single `track()` function — nothing else."

---

### 📚 Complementary Knowledge — How the Capture System Works

The frontend capture service does not fire an HTTP call for every event — that would generate hundreds of requests per minute in an active application and overwhelm the backend. The correct pattern has three mechanisms working together:

**Local queue + batch:** events accumulate in memory as an array. Every N seconds, or when the queue reaches a maximum size, the service sends the full batch in a single request (`events: []`). The timestamp of each event is the moment of capture, not the moment of sending.

**Reliable flush with `sendBeacon`:** when the user closes the tab or navigates away, the browser cancels in-flight HTTP requests. `navigator.sendBeacon` solves this — it sends the pending batch asynchronously and reliably even when the page is being destroyed.

**Retry with backoff:** if the network fails, the service retries with exponential wait. If it still fails after N attempts, it discards the batch — telemetry data is not critical and must not block the application.

**The endpoint as an environment variable:** in real environments, frontend and backend teams work in parallel. The frontend points to `NEXT_PUBLIC_TELEMETRY_ENDPOINT` — today that variable points to the stub; tomorrow it will point to the real endpoint with persistence. The frontend does not change.

**The profile/usage separation:** user data (name, role, preferences) is persistent state that lives in the main database. Usage data is `append-only` events that go to telemetry. Never mix the two.

---

## 🌱 How to Start the Project

1. Open your fork of the monorepo and locate `uis/backoffice/` (frontend) and `services/` (FastAPI backend).
2. Retrieve your `docs/telemetry/event-schemas.json` — it is the contract that will guide the entire implementation.
3. Add `NEXT_PUBLIC_TELEMETRY_ENDPOINT` to your `.env.local` pointing to the stub endpoint you will create: `http://localhost:8000/telemetry/events`.
4. Follow the phase order: stub → service → instrumentation. Do not instrument before you have the service.

---

## 💻 What You Need to Do

### Phase 1 — Stub Endpoint in FastAPI

> ⚠️ This endpoint is **temporary and for verification purposes**. Its only purpose is to let you check that the payload arrives with the correct format. In Phase 3 (next project) you will replace it with the real implementation including full validation and persistence in Supabase.

- [ ] Create the `POST /telemetry/events` endpoint in the backend, in its own router inside `services/`. For now it should:
  - Accept a body with the shape `{ "events": [...] }`
  - Log the number of events received and the `event_type` of each one
  - Return `200 OK` with `{ "received": N }` where N is the number of events in the batch
- [ ] Define the Pydantic model `TelemetryEvent` with the standard envelope fields from your plan (`eventId`, `timestamp`, `sessionId`, `userId`, `event_type`, `schemaVersion`, `properties`). This model will be reused and extended in Phase 3 — define it properly from the start.
- [ ] Read the endpoint URL from the `TELEMETRY_ENDPOINT` environment variable in the backend, even if you are not using it to redirect traffic yet. Establish the pattern from the beginning.

### Phase 2 — TelemetryService in the Frontend

- [ ] Create `uis/backoffice/src/services/telemetry.ts` (or equivalent) with the following responsibilities:
  - **Local queue:** accumulate events in memory as an internal array
  - **Batch + debounce:** send the queue to `NEXT_PUBLIC_TELEMETRY_ENDPOINT` every 10 seconds or when the queue reaches 20 events, whichever comes first
  - **Reliable flush:** use `navigator.sendBeacon` on the `visibilitychange` event to guarantee pending events are sent when the tab is closed or hidden
  - **Retry with backoff:** if sending fails, retry up to 3 times with exponential wait before discarding the batch
- [ ] The service must automatically add to each event: `sessionId` (generated at login and stored in session memory), `timestamp` in ISO 8601 at the moment of capture, and `schemaVersion` from a shared constant.
- [ ] Expose a single public function `track(eventType: string, properties: Record<string, unknown>): void`. All backoffice tracking goes through this function — never through direct `fetch` or `axios`.

### Phase 3 — Inventory Flow Instrumentation

- [ ] Instrument in the backoffice the events defined in your plan for the inventory module. At a minimum these must be covered:
  - Inbound order creation completed successfully
  - Outbound order creation completed successfully
  - Failed order attempt (validation error or insufficient stock)
  - Product/stock list viewed
- [ ] Every call to `track()` must include only the properties from the **allowlist** defined for that event in your `event-schemas.json`. Do not add extra properties "just in case".
- [ ] Verify in the browser DevTools (Network tab) that batches are reaching the stub endpoint with the correct format and that the backend responds 200.

### 🔵 Additional Activity — Authentication Flow Instrumentation

- [ ] Instrument the authentication events defined in your plan: successful login, failed login, and session expired. Capture them in the authentication hooks or components — not in each page individually.
- [ ] The failed login event must include in `properties` the reason for the failure (`invalid_credentials`, `session_expired`, `network_error`) but **never** the value entered by the user as password or email.

---

## ✅ What We Will Evaluate

- [ ] The stub `POST /telemetry/events` endpoint exists, accepts arrays with the `TelemetryEvent` model, and returns `{ "received": N }`
- [ ] The Pydantic model `TelemetryEvent` reflects the standard envelope from the Phase 1 plan with all its fields
- [ ] The endpoint URL is read from `NEXT_PUBLIC_TELEMETRY_ENDPOINT` — it is not hardcoded
- [ ] The backend declares `TELEMETRY_ENDPOINT` in its environment configuration to establish the pattern from the start
- [ ] The `TelemetryService` implements local queue, batch+debounce (10s / 20 events), flush with `sendBeacon`, and retry with backoff
- [ ] The service generates `sessionId` and `timestamp` automatically — the component calling `track()` does not pass them manually
- [ ] There are no direct `fetch`/`axios` calls for telemetry outside the `TelemetryService`
- [ ] Inventory flow events are instrumented respecting the allowlist of properties for each event
- [ ] Failed order attempts (validation error or insufficient stock) are tracked from the catch blocks
- [ ] Product/stock list viewed is tracked when the products page loads
- [ ] There is no PII (email, name, password) in any event sent
- [ ] The DevTools Network tab shows batches arriving at the endpoint with the correct format and a 200 response

---

## 📦 How to Submit

1. Make sure the changes are in your fork: stub endpoint in `services/` and `TelemetryService` + instrumentation in `uis/backoffice/`.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W16D47] Telemetry Frontend`.
3. In the PR description, include:
   - The list of instrumented events and which component or hook captures each one
   - A DevTools screenshot showing a batch of events arriving at the stub with a 200 response
   - Whether you implemented the additional authentication activity

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
