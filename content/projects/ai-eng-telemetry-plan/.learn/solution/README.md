# Telemetry — Phase 1: Company's Telemetry plan design — Reference Solution

This reference solution defines the expected quality bar for deliverables in the student's company monorepo fork:

- `docs/telemetry/telemetry-plan.md`
- `docs/telemetry/event-schemas.json`

The deliverable is **design documentation**, not executable instrumentation. Another developer should be able to implement events from these files without follow-up questions.

## Alignment with company context

All KPIs, entity names, identifiers, and business constraints must come from the student's assigned **CONTEXT-company.md**. Generic placeholders that ignore sector-specific KPIs or naming should be treated as incomplete.

---

## Expected deliverable structure

### `docs/telemetry/telemetry-plan.md`

A complete plan should include at least:

1. **Executive summary** — why telemetry is needed now (operations questions the system cannot answer today).
2. **KPI analysis** — three company KPIs with data sources and system touchpoints.
3. **Flow mapping** — inventory path from authenticated access through inbound/outbound order completion, with ≥5 instrumentation points (including rejected direct stock edits, validation failures, and threshold triggers).
4. **Backoffice opportunities** — ≥2 instrumentation points outside inventory (auth, navigation, abandoned flows).
5. **Event Envelope** — mandatory fields for every event.
6. **Event catalog** — ≥5 events with hypothesis → decision justification, property allowlists, PII notes, and stream/batch rationale.
7. **High-frequency strategy** — throttle/debounce notes where applicable.
8. **Risks and exclusions** — discarded events and data not captured (privacy, cost, low signal).

### `docs/telemetry/event-schemas.json`

Valid JSON describing each event schema. Acceptable formats:

- JSON Schema draft-07 per event, or
- A documented custom structure with the same fields as the Markdown plan.

Schemas must stay consistent with `telemetry-plan.md` (names, properties, required flags).

---

## Standard Event Envelope (reference)

Every event in the plan should share this envelope:

| Field                   | Type              | Required | Notes                                               |
| ----------------------- | ----------------- | -------- | --------------------------------------------------- |
| `eventId`               | string (UUID)     | yes      | Idempotency and deduplication                       |
| `timestamp`             | string (ISO 8601) | yes      | UTC recommended                                     |
| `sessionId`             | string            | yes      | Browser or API session                              |
| `userId`                | string            | yes      | Authenticated operator; hash if PII policy requires |
| `eventName`             | string            | yes      | `entity_action` taxonomy                            |
| `schemaVersion`         | string            | yes      | e.g. `1.0.0`                                        |
| `requestId` / `traceId` | string            | yes      | Correlates frontend, API, logs                      |
| `properties`            | object            | yes      | Event-specific payload (allowlist only)             |

---

## Indicative example — strong KPI block

```markdown
### KPI 1: Outbound order fulfillment rate

- **Definition:** % of outbound orders completed without validation errors in the last 7 days.
- **Data components:** `OutboundOrder` status transitions, validation error counts per order.
- **System touchpoints:** `POST /inventory/outbound-orders`, order validation service, product stock checks.
- **Telemetry need:** distinguish user errors (bad quantity) from system errors (race on stock).
```

Each KPI should follow the same pattern: definition → components → where generated → why telemetry helps.

---

## Indicative example — instrumentation justification

> We capture `direct_stock_edit_rejected` because we need to know **how often operators attempt to bypass order-based stock changes**, which allows us to make the decision **whether to add UX guardrails or training on the inbound/outbound workflow**.

If the hypothesis or decision is missing, the event should not appear in the plan.

---

## Indicative example — event definition

### `outbound_order_created` (batch)

| Property      | Type    | Required | Allowlist | PII |
| ------------- | ------- | -------- | --------- | --- |
| `orderId`     | string  | yes      | yes       | no  |
| `productId`   | string  | yes      | yes       | no  |
| `quantity`    | integer | yes      | yes       | no  |
| `warehouseId` | string  | no       | yes       | no  |

- **Stream vs batch:** batch — used for daily ops dashboards; sub-minute latency not required.
- **Sanitization:** none; no user-identifying fields in properties (user in envelope only).

### `stock_threshold_triggered` (stream)

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
        "eventName",
        "schemaVersion",
        "requestId",
        "properties"
      ],
      "properties": {
        "eventId": { "type": "string", "format": "uuid" },
        "timestamp": { "type": "string", "format": "date-time" },
        "sessionId": { "type": "string" },
        "userId": { "type": "string" },
        "eventName": { "type": "string", "pattern": "^[a-z]+_[a-z_]+$" },
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
            "eventName": { "const": "outbound_order_created" },
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

A passing plan typically designs at least:

| Event                        | Domain     | Why it matters            |
| ---------------------------- | ---------- | ------------------------- |
| `inbound_order_created`      | Inventory  | Inbound volume KPI        |
| `outbound_order_created`     | Inventory  | Consumption trends        |
| `direct_stock_edit_rejected` | Inventory  | Policy enforcement signal |
| `order_validation_failed`    | Inventory  | Error pattern analysis    |
| `stock_threshold_triggered`  | Inventory  | Alert timing              |
| `login_failed`               | Auth       | Security / UX friction    |
| `section_viewed`             | Navigation | Backoffice usage          |

Names and properties must match the student's CONTEXT entities, not this table verbatim.

---

## Stream vs batch decision rubric

| Urgency                     | Processing | Example                                      |
| --------------------------- | ---------- | -------------------------------------------- |
| Ops must act within minutes | stream     | stock threshold, repeated auth failures      |
| Daily/weekly reporting      | batch      | order volume aggregates, navigation heatmaps |
| Analytics only              | batch      | section popularity trends                    |

Justifications must cite **business decision timing**, not developer preference.

---

## Common mistakes (incomplete submissions)

- Events without the golden-rule sentence (hypothesis + decision).
- Properties not restricted to an explicit allowlist.
- KPIs copied from generic inventory tutorials instead of CONTEXT-company.md.
- `event-schemas.json` out of sync with Markdown (missing events, different field names).
- Stream chosen for all events without urgency rationale.
- Capturing raw passwords, tokens, or full PII in `properties`.

---

## Evaluation checklist

- [ ] Three KPIs grounded in CONTEXT-company.md with data sources identified.
- [ ] ≥5 inventory-flow instrumentation points including rejections and thresholds.
- [ ] ≥2 non-inventory opportunities documented.
- [ ] Consistent Event Envelope across all events.
- [ ] ≥5 fully specified events with allowlists and PII handling.
- [ ] Valid `event-schemas.json` aligned with the plan.
- [ ] Stream/batch choices justified by business urgency.
- [ ] Risks and exclusions section shows deliberate scope cuts.
- [ ] PR title `[W16D46] Telemetry Design Plan` with KPI summary in description.

---

## Reviewer notes

- Grade reasoning and precision, not code.
- Accept different valid event sets if justification and CONTEXT alignment are strong.
- Treat property allowlists and PII documentation as security requirements, not optional detail.
