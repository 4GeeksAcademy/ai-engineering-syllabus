# Maple Street Library — Telemetry Storage (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-telemetry-storage`. Same spine (Supabase `telemetry_events`, bulk insert, per-event validation, partial batch acceptance, unchanged frontend), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** already has `desk-app` sending batched events to a FastAPI stub. Today: create the real storage layer. The desk app does **not** change.

### Scope note

| Graded project (`ai-eng-telemetry-storage`) | This class example                            |
| ------------------------------------------- | --------------------------------------------- |
| Company CONTEXT + Phase 1 `tags` mapping    | Mini library event contract from capture demo |
| Full monorepo + Phase 2 `TelemetryEvent`    | Mini `library-api` + existing capture service |
| 8-column table + 3 indexes                  | Same schema, smaller dataset                  |
| Inventory E2E test                          | 2 book-checkout events in demo                |
| PR to student fork                          | Local Supabase project                        |

---

## What to build

### 1. Supabase table `telemetry_events`

- [ ] Create table with columns: `id`, `timestamp`, `service`, `event_type`, `level`, `value`, `message`, `tags`
- [ ] Indexes on `timestamp`, `event_type`, GIN on `tags`
- [ ] No UPDATE/DELETE logic

### 2. Replace stub endpoint

- [ ] `POST /telemetry/events` — same path and body as stub
- [ ] Validate each event with existing `TelemetryEvent` model (do not modify)
- [ ] Bulk insert valid rows in **one** transaction
- [ ] Return `{ "received", "stored", "rejected" }`
- [ ] Invalid events rejected individually; valid siblings still stored

### 3. Verify

- [ ] Checkout a book in `desk-app` → rows appear in Supabase
- [ ] `curl` mixed valid/invalid batch → counts match reality
- [ ] Confirm zero changes under `desk-app/`

---

## Verify together

- [ ] `SELECT count(*) FROM telemetry_events` increases after desk activity
- [ ] `tags` JSONB contains envelope `properties` from allowlist (`loanId`, `bookId`)
- [ ] Mixed batch: `stored + rejected === received`
- [ ] Frontend git diff empty

---

## Discussion questions

1. Why is bulk insert critical when batches arrive every 10 seconds from many users?
2. Why must invalid events not roll back the whole batch?
3. What breaks if the frontend starts parsing `{ stored, rejected }` from the response body?
