# CONTEXT — TrackFlow · Telemetry Phase 3: Backend Storage

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (US) and Zaragoza (Spain). You are part of **TrackFlow Tech**. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each TrackFlow event.

| `event_type` | `tags` content |
|---|---|
| `receiving_order_created` | `{ "sku_id": "...", "quantity": 200, "warehouse": "los_angeles", "client_id": "client_uuid_..." }` |
| `dispatch_order_created` | `{ "sku_id": "...", "quantity": 15, "warehouse": "zaragoza", "destination_country": "ES" }` |
| `dispatch_order_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "sku_id": "...", "warehouse": "los_angeles", "destination_country": "US" }` |
| `receiving_order_failed` | `{ "error_code": "UNKNOWN_CLIENT", "warehouse": "zaragoza" }` |
| `sku_list_viewed` | `{ "warehouse": "los_angeles", "item_count": 142 }` |
| `user_login_succeeded` | `{ "warehouse": "zaragoza" }` |
| `user_login_failed` | `{ "reason": "invalid_credentials" }` |
| `session_expired` | `{}` |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The `value` column can be used for `quantity` on order events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — TrackFlow-Specific Notes

TrackFlow's peak traffic is e-commerce dispatch windows: Black Friday, holiday season, flash sales from fashion clients. During these windows, Los Angeles operatives can generate hundreds of `dispatch_order_created` and `dispatch_order_failed` events within a short period. Your bulk insert must absorb these bursts without queueing up transactions.

**Rejection example for TrackFlow:** a batch arrives with 6 events. Event 4 is a `dispatch_order_failed` missing `warehouse` in `tags` — it fails validation. Events 1, 2, 3, 5, 6 are valid and get inserted. The response is `{ "received": 6, "stored": 5, "rejected": 1 }`. A `dispatch_order_failed` without `warehouse` is operationally useless — Andrés Kim (CTO) cannot attribute the failure to either location.

---

## Verification Checklist for TrackFlow

After replacing the stub, verify in the Supabase table editor:

- [ ] All order events have `warehouse` in `tags` (`los_angeles` or `zaragoza`) — Thomas Harry (CEO) requires per-warehouse segmentation in every view
- [ ] `dispatch_order_created` rows have `destination_country` in `tags` — needed for the US vs. Spain SLA analysis
- [ ] `client_id` values in `tags` are opaque UUIDs — never brand names or company names
- [ ] No row contains recipient names, delivery addresses, or phone numbers anywhere in `tags`
- [ ] `dispatch_order_failed` rows always have both `warehouse` and `destination_country` even when other properties are missing

---

_TrackFlow Tech — Internal document for 4Geeks Academy AI Engineering Track_
