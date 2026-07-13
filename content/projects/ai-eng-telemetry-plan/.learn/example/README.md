# Riverside Community Garden — Telemetry Plan (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-telemetry-plan`. Same spine (CONTEXT mandatory metrics as floor, broad opportunity catalogue, event envelope, `entity_action` events, property allowlists, stream/batch, `telemetry-plan.md` + `event-schemas.json`), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**GreenPatch Co-op** runs a small tool-lending app for community gardens: members reserve shared equipment (wheelbarrows, hoses, compost bins), check items out, and return them. Stock is never edited directly — only through **checkout** and **return** records tied to a member. The ops team cannot answer basic questions: which tools break most often, who abandons reservations, or when peak checkout happens.

In one session, draft a **mini telemetry plan** before any instrumentation code.

### Scope note

| Graded project (`ai-eng-telemetry-plan`)                                              | This class example                            |
| ------------------------------------------------------------------------------------- | --------------------------------------------- |
| Company CONTEXT + inventory monorepo                                                  | Fictional GreenPatch CONTEXT (provided below) |
| All CONTEXT mandatory metrics + broad catalogue (≥5 inventory + auth/perf/errors/nav) | 2 mandatory + 2 identified opportunities      |
| All mandatory events + ≥8 additional (≥3 categories)                                  | 4 events with envelopes                       |
| Full risks/exclusions rubric                                                          | Short exclusions paragraph                    |
| PR to student monorepo                                                                | Local `docs/telemetry/` only                  |

---

## Mini context (use instead of CONTEXT-company.md)

**Mandatory metrics (floor):**

| `event_type`         | Fires when...                   | Hypothesis                                     | Decision it enables                |
| -------------------- | ------------------------------- | ---------------------------------------------- | ---------------------------------- |
| `checkout_completed` | Member confirms a tool checkout | Peak hours and tool demand are invisible today | Staffing + tool purchase planning  |
| `tool_threshold_low` | Available count hits minimum    | Stockouts happen without early warning         | Trigger refill / recall from peers |

**Identified opportunities (ceiling):** students should still explore auth failures, reservation abandonment, and navigation — mark each as **mandatory** vs **identified opportunity**.

**Entities:** `Tool`, `Reservation`, `Checkout`, `Member`.  
**Rule:** `Tool.availableCount` changes only via `Checkout` / `Return`, never direct edits.

---

## What to build

Create in a throwaway folder or shared demo repo:

- `docs/telemetry/telemetry-plan.md`
- `docs/telemetry/event-schemas.json`

### 1. Exhaustive (mini) catalogue

- [ ] List both **mandatory** metrics from the mini context above.
- [ ] Map the **checkout flow**: login → browse tools → create reservation → confirm checkout → return. Mark **3 instrumentation points** (e.g. reservation abandoned, checkout validation failed, overdue return flagged).
- [ ] Add **1 auth or navigation** opportunity outside checkout.
- [ ] For each opportunity: golden-rule sentence + label **mandatory** or **identified opportunity**.

### 2. Event Envelope

- [ ] Document mandatory fields: `eventId`, `timestamp` (ISO 8601), `sessionId`, `userId`, `event_type`, `schemaVersion`, `requestId`, `properties`.
- [ ] State that `properties` is allowlist-only per event.

### 3. Design four events

| Event                        | Class      | Suggested processing | Notes                             |
| ---------------------------- | ---------- | -------------------- | --------------------------------- |
| `checkout_completed`         | mandatory  | batch                | Volume trends                     |
| `tool_threshold_low`         | mandatory  | stream               | Ops alert when availableCount low |
| `checkout_validation_failed` | identified | batch                | Error patterns by tool            |
| `login_failed`               | identified | stream               | Security / friction signal        |

For each event:

- [ ] Golden-rule sentence: _"We capture `[event_type]` because we need to know `[hypothesis]`, which allows us to make the decision `[decision]`."_
- [ ] Property allowlist table (name, type, required).
- [ ] Stream vs batch with **business urgency** justification.

### 4. JSON schemas

- [ ] Export the four events to `event-schemas.json` (draft-07 or documented custom structure).
- [ ] `additionalProperties: false` on `properties` objects.

### 5. Exclusions (short)

- [ ] List one event you considered and rejected (with reason).
- [ ] Note one data field you will **not** capture (e.g. member email in properties).

---

## Verify together

- [ ] Both mandatory metrics from the mini context appear and are labeled mandatory.
- [ ] Every event has hypothesis + decision; none are "just in case".
- [ ] Envelope fields consistent across all four events.
- [ ] JSON validates and matches Markdown names/properties.
- [ ] At least one stream and one batch choice with non-technical justification.
- [ ] No passwords or raw tokens in any property allowlist.

---

## Discussion questions

1. Why is `tool_threshold_low` a better stream candidate than `checkout_completed`?
2. What goes wrong if `userId` is duplicated inside `properties` instead of only in the envelope?
3. How would you extend this plan to navigation events without exploding event volume?
