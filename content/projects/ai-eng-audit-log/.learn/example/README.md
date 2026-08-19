# Neighborhood Warehouse Ledger — Audit Trail (Class Example)

> **For instructors:** Not the student project. Live demo of same spine as `ai-eng-audit-log`: append-only records, hash chaining for tamper evidence, human vs process actors, and scoped viewer access. Domain changed to a neighborhood warehouse to avoid copying company story.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

Small warehouse tracks stock moves in a web app. Manager asks simple question after incident: "Who changed quantity of SKU W-42 last night?" Team has regular logs, but edits can be overwritten. Need audit trail that answers **who / what / when** and detects tampering.

### Scope note

One 60–120 minute class session. Keep one audited resource (`stock_adjustments`) plus auth events. No full monorepo integration required. Students still follow full project brief in root `README.md`.

---

## What to build

### Audit model

- [ ] `audit_log` append-only table/collection
- [ ] Fields: `actor_type`, `actor_id`, `action`, `resource`, `resource_id`, `origin`, `created_at`, `prev_hash`, `entry_hash`
- [ ] `entry_hash = sha256(canonical_payload + prev_hash)`

### Capture

- [ ] Log manual inventory adjust create/update/delete-attempt
- [ ] Log process action (`nightly_reconciliation_bot`)
- [ ] Log auth success/fail

### Viewer

- [ ] Filter by actor, action, resource, date range
- [ ] Admin sees all; Supervisor sees own department; Employee sees none
- [ ] Add pagination (`limit/offset`)

### Guard rails

- [ ] API has no `UPDATE`/`DELETE` route for `audit_log`
- [ ] Manual tamper test breaks hash chain validation

---

## Verify together

- [ ] Create 5+ entries from user actions + 1 bot action
- [ ] Attempt to edit stored row directly in DB fixture; run chain check; verify `invalid_from_index`
- [ ] Call viewer as Supervisor from another department; verify access denied or scoped response

---

## Discussion questions

1. Why append-only in app layer still weak without DB constraints?
2. If actor is process, what identity should be persisted to keep accountability?
3. When log volume hits millions, where should pagination and retention policy live?
