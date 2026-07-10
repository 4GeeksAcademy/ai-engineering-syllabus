# CONTEXT — HealthCore · Telemetry Phase 3: Backend Storage

## Your Company

**HealthCore** is an outpatient healthcare services company with 12 clinics across the US and UK. You are part of **HealthCore Digital**. The `TelemetryService` in the backoffice is already sending batches of events to the stub. Today you replace that stub with the real storage layer.

This is the highest-stakes storage implementation in the programme. Every row you write to `telemetry_events` must be free of patient-identifiable information — HIPAA in the US and UK GDPR in the UK apply from the moment data is persisted, not just when it is transmitted.

---

## What Goes in `tags` for Each Event

The `tags` JSONB column stores the event-specific properties from your allowlist. This is what Supabase will receive and store for each HealthCore event.

| `event_type`                 | `tags` content                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `supply_delivery_created`    | `{ "supply_id": 3, "quantity": 500, "clinic_id": 1, "country": "US" }`                                     |
| `supply_consumption_created` | `{ "supply_id": 3, "quantity": 20, "consumption_type": "clinical_use", "clinic_id": 10, "country": "UK" }` |
| `supply_consumption_failed`  | `{ "error_code": "INSUFFICIENT_STOCK", "supply_id": 3, "clinic_id": 5, "country": "US" }`                  |
| `supply_list_viewed`         | `{ "clinic_id": 1, "country": "US", "item_count": 67 }`                                                    |
| `user_login_succeeded`       | `{ "country": "US" }`                                                                                      |
| `user_login_failed`          | `{ "reason": "session_expired" }`                                                                          |
| `session_expired`            | `{}`                                                                                                       |

The fixed columns (`event_type`, `timestamp`, `service`, `level`) are populated from the envelope fields. The storage layer sets `service` to `backoffice` when persisting — it is not sent in the capture envelope. The `value` column can be used for `quantity` on supply events if you want it queryable without parsing JSONB — document your decision.

---

## Bulk Insert — HealthCore-Specific Notes

HealthCore's 12 clinics across two jurisdictions mean events arrive from multiple time zones simultaneously. Morning shift starts in Texas and Georgia while UK clinics are already mid-day. Your bulk insert must handle cross-jurisdiction batches — events with `country: "US"` and `country: "UK"` may arrive in the same batch and must be stored identically.

**Rejection example for HealthCore:** a batch arrives with 5 events. Event 2 is a `supply_consumption_created` missing `country` in `tags` — it fails validation. Events 1, 3, 4, 5 are valid and get inserted. The response is `{ "received": 5, "stored": 4, "rejected": 1 }`. Without `country`, Claire Whitfield (CCO) cannot use that event in any compliance report — it is correctly rejected.

---

## Verification Checklist for HealthCore

After replacing the stub, verify in the Supabase table editor:

- [ ] All events have `country` in `tags` (`"US"` or `"UK"`) — Claire Whitfield (CCO) requires this for every compliance report
- [ ] All supply delivery/consumption events have `clinic_id` in `tags` (integer 1–12) — Dr. Reid (Director of Clinical Operations) needs per-clinic visibility
- [ ] `supply_consumption_created` rows have `consumption_type` in `tags` — needed for clinical vs. waste analysis
- [ ] **No row contains patient names, patient IDs, dates of birth, diagnoses, or any patient-linked data anywhere in `tags` or any other column** — this is a hard HIPAA/UK GDPR boundary; if any such data is present, the table must be considered compromised and the data purged
- [ ] `userId` values stored via the envelope are opaque TinyDB UUIDs — never staff names, emails, or clinical role titles

---

_HealthCore Digital — Internal document for 4Geeks Academy AI Engineering Track_
