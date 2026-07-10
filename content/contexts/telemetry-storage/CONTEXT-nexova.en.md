# CONTEXT — Nexova · Telemetry Phase 3: Backend Storage

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each Nexova event.

| `event_type`           | `tags` content                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `asset_entry_created`  | `{ "asset_id": 8, "quantity": 5, "office": "Valencia", "supplier": "Dell Technologies" }` |
| `asset_exit_created`   | `{ "asset_id": 8, "quantity": 1, "office": "Miami", "exit_type": "allocation" }`          |
| `asset_exit_failed`    | `{ "error_code": "INSUFFICIENT_STOCK", "asset_id": 8, "office": "Valencia" }`             |
| `asset_entry_failed`   | `{ "error_code": "UNKNOWN_SUPPLIER", "office": "Miami" }`                                 |
| `asset_list_viewed`    | `{ "office": "Valencia", "item_count": 18 }`                                              |
| `user_login_succeeded` | `{ "office": "Miami" }`                                                                   |
| `user_login_failed`    | `{ "reason": "session_expired" }`                                                         |
| `session_expired`      | `{}`                                                                                      |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The storage layer sets `service` to `backoffice` when persisting — it is not sent in the capture envelope. The `value` column can be used for `quantity` on asset entry/exit events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — Nexova-Specific Notes

Nexova's Valencia and Miami offices operate in different time zones. Onboarding days — when multiple `asset_exit_created` events fire in sequence for a new hire — are the highest-traffic moments for the telemetry system. Your bulk insert must handle a burst of exit events without degrading response time for the backoffice user.

**Rejection example for Nexova:** a batch arrives with 4 events. Event 2 is an `asset_exit_created` missing the `office` field in `tags` — it fails validation. Events 1, 3, 4 are valid and get inserted. The response is `{ "received": 4, "stored": 3, "rejected": 1 }`. Without `office`, Sergio Molina (CTO) cannot segment Valencia vs. Miami — the event is correctly discarded.

---

## Verification Checklist for Nexova

After replacing the stub, verify in the Supabase table editor:

- [ ] `asset_entry_created` and `asset_exit_created` rows have `office` in `tags` — without it cross-office segmentation is impossible
- [ ] `asset_exit_created` rows do **not** contain employee names or email addresses in `tags`
- [ ] `asset_exit_failed` rows have both `error_code` and `asset_id` in `tags` — needed to identify which asset type generates the most friction
- [ ] No row contains software licence keys or vendor contract values anywhere in `tags`

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
