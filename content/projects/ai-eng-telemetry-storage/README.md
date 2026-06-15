# Company's Telemetry – Storage

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: You need the `TelemetryService` working in the frontend and sending batches to the stub from the previous project. If events are not reaching the stub with a 200 response, resolve that before continuing — today you build the real destination for those events.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Events are flowing from the frontend. The stub receives them and throws them away. Today you build what the stub promised: the system that actually saves them.

The deliverable is a single change in the backend — but a change that transforms everything: the stub becomes a real endpoint that validates each event against the Phase 1 schema contract, persists the valid ones in Supabase in a single operation, and reports exactly what was stored and what was rejected. The frontend does not change a single line.

> Your tech lead sent you this message:
>
> > "The stub has done its job — I know the events arrive with the correct format. Now I need you to save them.
> >
> > Create the table in Supabase and replace the stub with the real endpoint. The Pydantic model you defined in the previous phase is the contract — use it to validate. Events that don't meet the contract are rejected individually, but the rest of the batch is persisted regardless.
> >
> > The frontend doesn't touch anything. The endpoint URL is the same — only what happens inside the backend when the batch arrives changes. If the frontend needs to change anything for this to work, the design is wrong."

---

### 📚 Complementary Knowledge — Why Bulk Insert Matters

Telemetry is not written the same way as business data. An inventory form generates one INSERT when the user clicks "Save". The `TelemetryService` can send 20 events at once every 10 seconds from multiple users in parallel.

If the endpoint does one INSERT per event, each batch of 20 opens 20 separate transactions in the database. With 10 active users that is 200 transactions per flush cycle — and that is in a small system. In production, that pattern collapses the connection pool.

Bulk insert solves this: all valid events in a batch are inserted in a single transaction. The difference between the two is invisible when the table has 100 rows; it is catastrophic when it has 10 million.

**The telemetry table is not a CRUD table.** Its invariants are different:

- Write-only, never updated or deleted — events are immutable facts
- The fixed columns (`event_type`, `timestamp`, `service`) are what support the analytical queries of the next project
- The `tags` JSONB column absorbs the event-specific properties without needing to alter the schema

---

## 🌱 How to Start the Project

1. Open your fork of the monorepo and locate `services/` (FastAPI backend).
2. Have your `docs/telemetry/event-schemas.json` at hand — the stub's Pydantic model already follows it; today you use it to validate before persisting.
3. The frontend is not touched. Verify that `NEXT_PUBLIC_TELEMETRY_ENDPOINT` still points to the same endpoint — only what happens inside the backend changes.
4. Follow the order: table in Supabase → real endpoint → end-to-end verification.

---

## 💻 What You Need to Do

### Phase 1 — Storage Table in Supabase

- [ ] Create the `telemetry_events` table in Supabase with the following structure:

  | Column       | Type                                   | Description                                           |
  | ------------ | -------------------------------------- | ----------------------------------------------------- |
  | `id`         | `uuid` PK, default `gen_random_uuid()` | Unique record identifier                              |
  | `timestamp`  | `timestamptz` NOT NULL                 | Event timestamp in ISO 8601                           |
  | `service`    | `text` NOT NULL                        | Event origin (`backoffice`, `api`)                    |
  | `event_type` | `text` NOT NULL                        | Event name in `entity_action` format                  |
  | `level`      | `text` default `'info'`                | Severity: `info`, `warn`, `error`                     |
  | `value`      | `numeric` nullable                     | Numeric value associated with the event if applicable |
  | `message`    | `text` nullable                        | Human-readable description of the event               |
  | `tags`       | `jsonb` default `'{}'`                 | Event-specific properties                             |

- [ ] Create the three indexes that make the table queryable at scale: on `timestamp`, on `event_type`, and a GIN index on `tags` for searches inside the JSONB.
- [ ] Confirm the table has no UPDATE or DELETE logic — telemetry events are immutable once recorded.

### Phase 2 — Real Endpoint in FastAPI

- [ ] Replace the stub `POST /telemetry/events` with the full implementation. The real endpoint must:
  - Accept the same body as the stub: `{ "events": list[TelemetryEvent] }`
  - Validate each event against the `TelemetryEvent` Pydantic model — the same one defined in the previous phase, without modifying it
  - Reject individually the events that don't meet the contract, **without cancelling the batch** — valid events in the same batch are persisted regardless
  - Insert the valid events into `telemetry_events` in a single bulk insert operation
  - Return `{ "received": N, "stored": M, "rejected": R }` where N is the total received, M the persisted, and R the rejected
- [ ] Verify that the real endpoint's response is compatible with the existing frontend — the `TelemetryService` only looks at the HTTP status code, not the response body.

### Phase 3 — End-to-End Verification

- [ ] With the real endpoint active, use the backoffice to generate real events: register at least one inbound order and one outbound order in the inventory module.
- [ ] Query the `telemetry_events` table directly in Supabase and confirm that events appear with the correct fields — especially `event_type`, `timestamp`, and `tags`.
- [ ] Test the rejection behaviour: send manually (with curl or your preferred HTTP client) a batch that mixes valid and invalid events and verify that the response correctly reflects `stored` and `rejected`.

---

## ✅ What We Will Evaluate

- [ ] The `telemetry_events` table exists in Supabase with the eight columns, the three indexes, and no UPDATE/DELETE logic
- [ ] The `POST /telemetry/events` endpoint does bulk insert and returns `{ "received", "stored", "rejected" }`
- [ ] Invalid events are rejected individually without cancelling the batch — valid ones are persisted
- [ ] The `TelemetryEvent` Pydantic model has not been modified from the previous project — it is reused as-is
- [ ] The frontend has not changed a single line — the stub → real substitution is completely transparent
- [ ] Events appear in `telemetry_events` with `event_type`, `timestamp`, and `tags` correctly populated
- [ ] The insert is a single operation per batch, not one INSERT per event

---

## 📦 How to Submit

1. Make sure the changes are in your fork: table created in Supabase and real endpoint in `services/`.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W16D48] Telemetry Storage`.
3. In the PR description, include:
   - A screenshot of the `telemetry_events` table in Supabase with at least 5 rows of real events
   - The JSON response of a batch mixing valid and invalid events (showing `received`, `stored`, and `rejected`)
   - Explicit confirmation that the frontend did not change

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
