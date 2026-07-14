# Maple Street Library — Frontend Telemetry Capture (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-telemetry-capture`. Same spine (FastAPI stub, `TelemetryService`, queue/batch/sendBeacon/retry, single `track()`, env endpoint, mandatory metrics + technical baseline), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** has a desk app (`desk-app`, Next.js) and a small API (`library-api`, FastAPI). Librarians check books in/out; the CTO wants usage events flowing **before** building analytics storage.

In one session: stub receiver + frontend capture service + instrument **mandatory** desk metrics plus a tiny technical baseline.

### Scope note

| Graded project (`ai-eng-telemetry-capture`)                                | This class example                             |
| -------------------------------------------------------------------------- | ---------------------------------------------- |
| Company CONTEXT + Phase 1 schemas                                          | Mini library event contract (below)            |
| All CONTEXT mandatory metrics + technical baseline + prioritised catalogue | 2 mandatory desk events + 1 technical + 1 auth |
| Batch 10s / 20 events                                                      | Batch 5s / 10 events (demo speed)              |
| PR to student fork                                                         | Local demo only                                |

**Mini event contract (use as `event-schemas.json` for class):**

| Event                     | Class                   | Properties allowlist                                |
| ------------------------- | ----------------------- | --------------------------------------------------- |
| `book_checkout_completed` | mandatory               | `loanId`, `bookId`                                  |
| `book_checkout_failed`    | mandatory               | `reason`, `bookId`                                  |
| `page_viewed`             | technical baseline      | `route`                                             |
| `login_failed`            | identified / additional | `reason` (`invalid_credentials` \| `network_error`) |

---

## What to build

### 1. FastAPI stub (`library-api`)

- [ ] `POST /telemetry/events` accepts `{ "events": [...] }`
- [ ] Pydantic model with `eventId`, `timestamp`, `sessionId`, `userId`, `event_type`, `schemaVersion`, `requestId`, `properties`
- [ ] Log count + `event_type`; return `{ "received": N }`
- [ ] Read `TELEMETRY_ENDPOINT` from env (unused OK)

### 2. `TelemetryService` (`desk-app/src/services/telemetry.ts`)

- [ ] In-memory queue; flush every **5s** or **10 events**
- [ ] `track(eventType, properties)` — only public API
- [ ] Auto-add `eventId`, `sessionId`, `userId`, `timestamp`, `schemaVersion`, `requestId`
- [ ] `visibilitychange` → `sendBeacon`
- [ ] 3 retries with exponential backoff, then drop batch
- [ ] URL from `NEXT_PUBLIC_TELEMETRY_ENDPOINT`

### 3. Instrumentation

- [ ] On successful book checkout → `track("book_checkout_completed", { loanId, bookId })`
- [ ] On validation/API error → `track("book_checkout_failed", { reason, bookId })`
- [ ] On main desk route enter → `track("page_viewed", { route })`
- [ ] In auth hook → `track("login_failed", { reason })` — never email/password

---

## Verify together

- [ ] Network tab shows **one batch** with multiple events after activity burst
- [ ] Stub returns `200` and `{ "received": N }`
- [ ] Both mandatory metrics instrumented
- [ ] No `fetch` for telemetry outside `telemetry.ts`
- [ ] Failed login `properties` contain `reason` only — no credentials

---

## Discussion questions

1. Why batch instead of one HTTP call per `track()`?
2. When does `sendBeacon` matter more than `fetch`?
3. What breaks if `NEXT_PUBLIC_TELEMETRY_ENDPOINT` is hardcoded?
