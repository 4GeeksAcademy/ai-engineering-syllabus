# CONTEXT — HealthCore: Inventory Manager

## 1. Company Snapshot

**HealthCore** runs 12 outpatient clinics across the US and UK. Clinical supplies — PPE, consumables, over-the-counter medication, and equipment — are tracked inconsistently across locations, with no shared visibility for **Dr. Marcus Reid**'s clinical operations team into what's on hand where. A clinic running out of a basic consumable mid-shift is a patient-experience problem, not just a logistics one.

You are building the inventory manager that gives HealthCore a real-time, per-clinic view of supply stock, derived strictly from recorded movements, with automatic flagging when a clinic is about to run out of something it needs.

## 2. ⚠️ Non-Negotiable Data Constraint

**No PHI, patient identifiers, or HIPAA/UK GDPR-regulated data may appear in any log, event, table, endpoint response, or system output.** This inventory manager tracks supply stock, not clinical usage per patient — an item and its movements must never reference an individual patient by name, medical record number, date of birth, or any other identifier. A movement's `reason` field describes the operational cause of a stock change (received, used in a procedure category, damaged, expired) and never the patient it was used on. If your implementation cannot describe a movement without patient detail, the description is wrong, not the constraint.

## 3. Domain Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 3.1 Units of Measure

`unit`, `box`, `ml`, `tablet`

### 3.2 Categories

| Value | Examples |
|---|---|
| `ppe` | Gloves, masks, gowns |
| `medical_consumables` | Syringes, gauze, test strips |
| `otc_medication` | Over-the-counter medication kept on-site |
| `clinical_equipment` | Thermometers, BP cuffs, small reusable devices |

### 3.3 Locations

Every item and movement belongs to one of HealthCore's 12 clinics, and each clinic has a `country` (`us` or `uk`). Seed at least 4 clinics across both countries — stock is tracked per clinic, not network-wide.

## 4. Entity Fields

### 4.1 Item

- `clinic_location`, `country` (`us` or `uk`)
- `name`, `category` (§3.2), `unit_of_measure` (§3.1)
- `reorder_point` (numeric, in the item's unit of measure)
- `created_at`, `updated_at`

### 4.2 Lot (required for `medical_consumables` and `otc_medication`; optional for other categories)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 4.3 Movement

- `item_id`, `lot_id` (nullable — only required for items with lot tracking)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (required for `adjustment`; e.g. `damaged`, `expired`, `count_correction` — never a patient reference; see §2)
- `created_at`

## 5. The Invariant

An item's available stock at a clinic is the sum of its `inbound` movements minus its `outbound` movements, adjusted by any `adjustment` entries — computed, never stored as an editable field. This is the same invariant the README requires; this CONTEXT doesn't relax it for any category.

## 6. Reorder Point

`reorder_point` is set per item, per clinic — a higher-volume clinic needs a higher threshold for a fast-moving consumable than a smaller one. When stock at a clinic drops at or below `reorder_point`, the backoffice must flag it visibly.

## 7. Seed Data

Seed at least 15 items across at least 4 clinics in both countries and all four categories, with:

- At least 4 items using lot tracking, including one lot with an `expiry_date` in the past
- At least 2 items currently at or below their `reorder_point`
- A movement history per item deep enough to show at least one `inbound`, one `outbound`, and one `adjustment`
- Zero items, movements, or seed records anywhere in the set that violate §2 — this is graded, not advisory

## 8. Business Constraints

- An `outbound` movement that would leave stock below zero must be rejected — this is the "unwanted behavior" criterion the README's spec phase requires.
- An `outbound` or `adjustment` referencing a nonexistent `item_id` or `lot_id` must be rejected.
- An `outbound` movement should not be issued from a lot past its `expiry_date` — expired medical consumables and OTC medication can't leave inventory for use.
- Every field, log line, and generated document produced by this feature must be checked against §2 before it's considered complete — including console output, seed scripts, and any AI-generated summary text.

## 9. Expected Deliverables

- Spec, plan, and tasks covering item CRUD, movement logging, and the reorder-point signal, scoped to the fields in §4 and using only the catalogue values in §3, respecting §2 without exception.
- A test suite verifying the stock invariant (§5) and the unwanted-behavior criteria (§8).
- The reorder-point flag working per clinic, using the values from your seed data.
