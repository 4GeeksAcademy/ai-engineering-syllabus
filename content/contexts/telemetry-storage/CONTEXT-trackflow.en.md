# CONTEXT — TrackFlow · Telemetry Phase 3: Backend Storage

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (US) and Zaragoza (Spain). You are part of **TrackFlow Tech**. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each TrackFlow event.

| `event_type`           | `tags` content                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| `stock_entry_created`  | `{ "sku_id": 42, "quantity": 200, "warehouse": "LA", "reference": "PO-2025-8841" }`                |
| `stock_exit_created`   | `{ "sku_id": 42, "quantity": 15, "warehouse": "ZGZ", "exit_type": "dispatch" }`                    |
| `stock_exit_failed`    | `{ "error_code": "INSUFFICIENT_STOCK", "sku_id": 42, "warehouse": "LA", "exit_type": "dispatch" }` |
| `stock_entry_failed`   | `{ "error_code": "INVALID_REFERENCE", "warehouse": "ZGZ" }`                                        |
| `sku_list_viewed`      | `{ "warehouse": "LA", "item_count": 142 }`                                                         |
| `user_login_succeeded` | `{ "warehouse": "ZGZ" }`                                                                           |
| `user_login_failed`    | `{ "reason": "invalid_credentials" }`                                                              |
| `session_expired`      | `{}`                                                                                               |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The storage layer sets `service` to `backoffice` when persisting — it is not sent in the capture envelope. The `value` column can be used for `quantity` on stock entry/exit events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — TrackFlow-Specific Notes

TrackFlow's peak traffic is e-commerce dispatch windows: Black Friday, holiday season, flash sales from fashion clients. During these windows, Los Angeles operatives can generate hundreds of `stock_exit_created` and `stock_exit_failed` events within a short period. Your bulk insert must absorb these bursts without queueing up transactions.

**Rejection example for TrackFlow:** a batch arrives with 6 events. Event 4 is a `stock_exit_failed` missing `warehouse` in `tags` — it fails validation. Events 1, 2, 3, 5, 6 are valid and get inserted. The response is `{ "received": 6, "stored": 5, "rejected": 1 }`. A `stock_exit_failed` without `warehouse` is operationally useless — Andrés Kim (CTO) cannot attribute the failure to either location.

---

## Verification Checklist for TrackFlow

After replacing the stub, verify in the Supabase table editor:

- [ ] All stock entry/exit events have `warehouse` in `tags` (`"LA"` or `"ZGZ"`) — Thomas Harry (CEO) requires per-warehouse segmentation in every view
- [ ] `stock_exit_created` rows have `exit_type` in `tags` — needed for dispatch vs. loss analysis
- [ ] `reference` values in `tags` are client dispatch references — never recipient addresses or phone numbers
- [ ] No row contains recipient names, delivery addresses, or phone numbers anywhere in `tags`
- [ ] `stock_exit_failed` rows always have both `warehouse` and `exit_type` even when other properties are missing

---

_TrackFlow Tech — Internal document for 4Geeks Academy AI Engineering Track_
