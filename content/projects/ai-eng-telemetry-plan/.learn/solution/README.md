# Telemetry — Phase 1: Designing your company's telemetry plan — Reference Solution

This reference solution defines the expected quality bar for deliverables in the student's company monorepo fork:

- `docs/telemetry/telemetry-plan.md`
- `docs/telemetry/event-schemas.json`

The deliverable is **design documentation**, not executable instrumentation. Another developer should be able to implement events from these files without follow-up questions.

## Alignment with company context

All **mandatory metrics**, entity names, identifiers, and business constraints must come from the student's assigned **CONTEXT-company.md** under `content/contexts/06-telemetry-data-pipelines/telemetry/`. Generic placeholders that ignore sector-specific metrics or naming should be treated as incomplete. Mandatory metrics are a **floor**, not a ceiling — a plan that only covers the CONTEXT table without exploring the rest of the application will not pass.

---

## Expected deliverable structure

### `docs/telemetry/telemetry-plan.md`

A complete plan should include at least:

1. **Executive summary** — why telemetry is needed now (operations questions the system cannot answer today).
2. **Mandatory metrics** — every CONTEXT metric listed and labeled as **mandatory**, with data sources and system touchpoints.
3. **Flow mapping** — inventory path from authenticated access through inbound/outbound order completion, with ≥5 instrumentation points (including rejected direct stock edits, validation failures, and threshold triggers).
4. **Broad opportunity catalogue** — authentication, performance, frontend errors, navigation / abandoned flows, and other backoffice sections. Events labeled **mandatory** vs **identified opportunity**.
5. **Event Envelope** — mandatory fields for every event.
6. **Event catalog** — schemas for **all CONTEXT mandatory metrics** plus **≥8 additional events** covering **≥3 distinct categories**, each with hypothesis → decision, property allowlists, PII notes, and stream/batch rationale.
7. **High-frequency strategy** — throttle/debounce notes where applicable.
8. **Risks and exclusions** — discarded events and data not captured (privacy, cost, low signal).

### `docs/telemetry/event-schemas.json`

Valid JSON describing each event schema. Acceptable formats:

- JSON Schema draft-07 per event, or
- A documented custom structure with the same fields as the Markdown plan.

Schemas must stay consistent with `telemetry-plan.md` (`event_type` values, `properties`, required flags).

---

## Standard Event Envelope (reference)

Every event in the plan should share this envelope:

| Field           | Type              | Required | Notes                                               |
| --------------- | ----------------- | -------- | --------------------------------------------------- |
| `eventId`       | string (UUID)     | yes      | Idempotency and deduplication                       |
| `timestamp`     | string (ISO 8601) | yes      | UTC recommended                                     |
| `sessionId`     | string            | yes      | Browser or API session                              |
| `userId`        | string            | yes      | Authenticated operator; hash if PII policy requires |
| `event_type`    | string            | yes      | `entity_action` taxonomy                            |
| `schemaVersion` | string            | yes      | e.g. `1.0.0`                                        |
| `requestId`     | string            | yes      | Correlates frontend, API, logs                      |
| `properties`    | object            | yes      | Event-specific payload (allowlist only)             |

---

## Indicative example — mandatory metric block

```markdown
### Mandatory: `stock_threshold_triggered`

- **Class:** mandatory (from CONTEXT)
- **Definition:** fires when product stock reaches the configured minimum threshold.
- **Data components:** product id, current stock, threshold, location/warehouse.
- **System touchpoints:** outbound order completion, stock recalculation service.
- **Hypothesis → decision:** We capture `stock_threshold_triggered` because we need to know **when replenishment risk appears by location**, which allows us to decide **whether to reorder or redistribute stock that day**.
```

Every CONTEXT row should follow the same pattern and appear in both the Markdown plan and `event-schemas.json`.

---

## Indicative example — instrumentation justification

> We capture `direct_stock_edit_rejected` because we need to know **how often operators attempt to bypass order-based stock changes**, which allows us to make the decision **whether to add UX guardrails or training on the inbound/outbound workflow**.

If the hypothesis or decision is missing, the event should not appear in the plan.

---

## Indicative example — event definition

### `outbound_order_created` (batch) — identified opportunity or mandatory if in CONTEXT

| Property      | Type    | Required | Allowlist | PII |
| ------------- | ------- | -------- | --------- | --- |
| `orderId`     | string  | yes      | yes       | no  |
| `productId`   | string  | yes      | yes       | no  |
| `quantity`    | integer | yes      | yes       | no  |
| `warehouseId` | string  | no       | yes       | no  |

- **Stream vs batch:** batch — used for daily ops dashboards; sub-minute latency not required.
- **Sanitization:** none; no user-identifying fields in properties (user in envelope only).

### `stock_threshold_triggered` (stream) — typically mandatory

| Property       | Type    | Required | Allowlist | PII |
| -------------- | ------- | -------- | --------- | --- |
| `productId`    | string  | yes      | yes       | no  |
| `currentStock` | integer | yes      | yes       | no  |
| `threshold`    | integer | yes      | yes       | no  |

- **Stream vs batch:** stream — replenishment alerts need near-real-time notification.
- **Throttle:** debounce repeated triggers for the same `productId` within 15 minutes.

---

## Indicative `event-schemas.json` fragment

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": {
    "eventEnvelope": {
      "type": "object",
      "required": [
        "eventId",
        "timestamp",
        "sessionId",
        "userId",
        "event_type",
        "schemaVersion",
        "requestId",
        "properties"
      ],
      "properties": {
        "eventId": { "type": "string", "format": "uuid" },
        "timestamp": { "type": "string", "format": "date-time" },
        "sessionId": { "type": "string" },
        "userId": { "type": "string" },
        "event_type": { "type": "string", "pattern": "^[a-z]+_[a-z_]+$" },
        "schemaVersion": { "type": "string" },
        "requestId": { "type": "string" },
        "properties": { "type": "object" }
      },
      "additionalProperties": false
    },
    "outbound_order_created": {
      "allOf": [
        { "$ref": "#/definitions/eventEnvelope" },
        {
          "properties": {
            "event_type": { "const": "outbound_order_created" },
            "properties": {
              "type": "object",
              "required": ["orderId", "productId", "quantity"],
              "properties": {
                "orderId": { "type": "string" },
                "productId": { "type": "string" },
                "quantity": { "type": "integer", "minimum": 1 },
                "warehouseId": { "type": "string" }
              },
              "additionalProperties": false
            }
          }
        }
      ]
    }
  }
}
```

---

## Minimum event coverage (inventory + beyond)

A passing plan typically designs:

| Event                           | Domain      | Class typically         |
| ------------------------------- | ----------- | ----------------------- |
| CONTEXT mandatory `event_type`s | Business    | **mandatory** (all)     |
| `inbound_order_created`         | Inventory   | mandatory or identified |
| `outbound_order_created`        | Inventory   | mandatory or identified |
| `direct_stock_edit_rejected`    | Inventory   | identified              |
| `order_validation_failed`       | Inventory   | identified              |
| `login_failed`                  | Auth        | identified              |
| `api_latency_recorded`          | Performance | identified              |
| `frontend_error_caught`         | Errors      | identified              |
| `section_viewed`                | Navigation  | identified              |

Names and `properties` must match the student's CONTEXT entities, not this table verbatim. Count requirement: **all CONTEXT mandatory events** + **≥8 additional** across **≥3 categories**.

---

## Stream vs batch decision rubric

| Urgency                     | Processing | Example                                      |
| --------------------------- | ---------- | -------------------------------------------- |
| Ops must act within minutes | stream     | stock threshold, repeated auth failures      |
| Daily/weekly reporting      | batch      | order volume aggregates, navigation heatmaps |
| Analytics only              | batch      | section popularity trends                    |

Justifications must cite **business or operational decision timing**, not developer preference.

---

## Common mistakes (incomplete submissions)

- Events without the golden-rule sentence (hypothesis + decision).
- Properties not restricted to an explicit allowlist.
- Only covering CONTEXT mandatory metrics with no broader catalogue.
- Mandatory metrics renamed or omitted relative to CONTEXT-company.md.
- `event-schemas.json` out of sync with Markdown (missing events, different field names).
- Stream chosen for all events without urgency rationale.
- Capturing raw passwords, tokens, or full PII in `properties`.

---

## Evaluation checklist

- [ ] Every mandatory metric from CONTEXT-company.md present and labeled mandatory.
- [ ] Broad catalogue covering technical and business opportunities (not minimum-only).
- [ ] ≥5 inventory-flow instrumentation points including rejections and thresholds.
- [ ] Every event has hypothesis + decision; none are "just in case".
- [ ] Consistent Event Envelope across all events.
- [ ] All mandatory events + ≥8 additional across ≥3 categories, with allowlists and PII handling.
- [ ] Valid `event-schemas.json` aligned with the plan.
- [ ] Stream/batch choices justified by business or operational urgency.
- [ ] Risks and exclusions section shows deliberate scope cuts.
- [ ] PR title `[W16D46] Telemetry Design Plan` with mandatory vs identified counts in description.

---

## Reviewer notes

- Grade reasoning and precision, not code.
- Accept different valid opportunity sets if justification and CONTEXT alignment are strong — mandatory CONTEXT events are non-negotiable.
- Treat property allowlists and PII documentation as security requirements, not optional detail.
