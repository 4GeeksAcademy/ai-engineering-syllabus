# CONTEXT — Brasaland · Telemetry Phase 3: Backend Storage

## Your Company

**Brasaland** is a grilled food restaurant chain with 14 locations across Colombia and Florida. You are part of **Brasaland Digital**. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each Brasaland event.

| `event_type`               | `tags` content                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| `ingredient_entry_created` | `{ "ingredient_id": 12, "quantity": 50.0, "location_id": 3, "supplier_name": "Carnes del Valle" }` |
| `ingredient_exit_created`  | `{ "ingredient_id": 12, "quantity": 12.0, "reason": "consumption", "location_id": 7 }`             |
| `ingredient_exit_failed`   | `{ "error_code": "INSUFFICIENT_STOCK", "ingredient_id": 12, "location_id": 3 }`                    |
| `ingredient_entry_failed`  | `{ "error_code": "UNKNOWN_SUPPLIER", "location_id": 7 }`                                           |
| `ingredient_list_viewed`   | `{ "location_id": 3, "item_count": 34 }`                                                           |
| `user_login_succeeded`     | `{ "location_id": 7 }`                                                                             |
| `user_login_failed`        | `{ "reason": "invalid_credentials" }`                                                              |
| `session_expired`          | `{}`                                                                                               |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The storage layer sets `service` to `backoffice` when persisting — it is not sent in the capture envelope. The `value` column can be used for `quantity` on order events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — Brasaland-Specific Notes

Brasaland's 14 locations mean multiple managers may be logged in simultaneously, each generating events. A Friday evening service rush in Miami can produce dozens of `ingredient_exit_created` events per minute. Your bulk insert must handle this without opening one transaction per event.

**Rejection example for Brasaland:** a batch arrives with 5 events. Event 3 is missing `location_id` in `tags` — it fails the schema validation. Events 1, 2, 4, 5 are valid and get inserted. The response is `{ "received": 5, "stored": 4, "rejected": 1 }`. The missing `location_id` means that event would have been useless for segmentation anyway — rejecting it is the right call.

---

## Verification Checklist for Brasaland

After replacing the stub, verify in the Supabase table editor:

- [ ] `ingredient_entry_created` rows have `location_id` in `tags` — without it Nicolás Park (CTO) cannot segment by country
- [ ] `ingredient_exit_created` rows have `reason` in `tags` — without it the waste ratio KPI is uncalculable
- [ ] No row contains email addresses, manager names, or COP/USD amounts anywhere in `tags`
- [ ] Rows from Colombian locations and Florida locations are distinguishable by `location_id` (integer 1–14) inside `tags`

---

_Brasaland Digital — Internal document for 4Geeks Academy AI Engineering Track_
