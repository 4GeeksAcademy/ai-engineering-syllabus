# CONTEXT — Nexova · Telemetry Phase 3: Backend Storage

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each Nexova event.

| `event_type` | `tags` content |
|---|---|
| `procurement_order_created` | `{ "asset_id": "...", "quantity": 5, "office": "valencia" }` |
| `assignment_order_created` | `{ "asset_id": "...", "quantity": 1, "office": "miami" }` |
| `assignment_order_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "asset_id": "...", "office": "valencia" }` |
| `procurement_order_failed` | `{ "error_code": "UNKNOWN_VENDOR", "office": "miami" }` |
| `asset_list_viewed` | `{ "office": "valencia", "item_count": 18 }` |
| `user_login_succeeded` | `{ "office": "miami" }` |
| `user_login_failed` | `{ "reason": "session_expired" }` |
| `session_expired` | `{}` |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The `value` column can be used for `quantity` on order events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — Nexova-Specific Notes

Nexova's Valencia and Miami offices operate in different time zones. Onboarding days — when multiple `assignment_order_created` events fire in sequence for a new hire — are the highest-traffic moments for the telemetry system. Your bulk insert must handle a burst of assignment events without degrading response time for the backoffice user.

**Rejection example for Nexova:** a batch arrives with 4 events. Event 2 is an `assignment_order_created` missing the `office` field in `tags` — it fails validation. Events 1, 3, 4 are valid and get inserted. The response is `{ "received": 4, "stored": 3, "rejected": 1 }`. Without `office`, Sergio Molina (CTO) cannot segment Valencia vs. Miami — the event is correctly discarded.

---

## Verification Checklist for Nexova

After replacing the stub, verify in the Supabase table editor:

- [ ] `procurement_order_created` and `assignment_order_created` rows have `office` in `tags` — without it cross-office segmentation is impossible
- [ ] `assignment_order_created` rows do **not** contain employee names or email addresses in `tags` — only opaque UUIDs if any employee reference is needed
- [ ] `assignment_order_failed` rows have both `error_code` and `asset_id` in `tags` — needed to identify which asset type generates the most friction
- [ ] No row contains software licence keys or vendor contract values anywhere in `tags`

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
