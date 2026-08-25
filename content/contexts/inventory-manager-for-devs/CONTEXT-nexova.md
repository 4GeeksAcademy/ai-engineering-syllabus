# CONTEXT — Nexova: Inventory Manager

## 1. Company Snapshot

**Nexova** runs its consulting, selection, and outsourced-support operation from two offices — Valencia and Miami. It isn't a warehouse business, but it still holds physical stock that keeps the operation running: laptops and headsets for the 30 outsourced support agents, branded onboarding kits for new hires, and training materials — including certification exam vouchers — for **Elena Vargas**'s corporate training line. Right now that stock lives in a spreadsheet nobody trusts: when a new support agent starts, someone finds out there are no headsets left only on their first day.

You are building the inventory manager that tracks Nexova's operational and training assets across both offices, derived strictly from recorded movements, with automatic flagging when an office is about to run out of something it needs.

## 2. Domain Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Units of Measure

`unit`, `box`

### 2.2 Categories

| Value | Examples |
|---|---|
| `it_equipment` | Laptops, headsets, monitors |
| `office_supplies` | Notebooks, badges, stationery |
| `training_materials` | Printed course kits, certification exam vouchers |
| `branded_merchandise` | Onboarding kits, welcome packs |

### 2.3 Offices

Every item and movement belongs to one of Nexova's two offices: `valencia`, `miami`. Stock is tracked per office, not company-wide — a Miami stockout doesn't get silently covered by Valencia's surplus.

## 3. Entity Fields

### 3.1 Item

- `office` (§2.3)
- `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numeric, in the item's unit of measure)
- `created_at`, `updated_at`

### 3.2 Lot (required for `training_materials` with an expiry, such as certification vouchers; optional for other categories)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movement

- `item_id`, `lot_id` (nullable — only required for items with lot tracking)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (required for `adjustment`; e.g. `damaged`, `lost`, `count_correction`)
- `created_at`

## 4. The Invariant

An item's available stock at an office is the sum of its `inbound` movements minus its `outbound` movements, adjusted by any `adjustment` entries — computed, never stored as an editable field. This is the same invariant the README requires; this CONTEXT doesn't relax it for any category.

## 5. Reorder Point

`reorder_point` is set per item, per office — headset stock at Miami (30 support agents) needs a higher threshold than at Valencia. When stock at an office drops at or below `reorder_point`, the backoffice must flag it visibly.

## 6. Seed Data

Seed at least 12 items across both offices and all four categories, with:

- At least 2 items using lot tracking (certification vouchers), including one lot with an `expiry_date` in the past
- At least 2 items currently at or below their `reorder_point`
- A movement history per item deep enough to show at least one `inbound`, one `outbound`, and one `adjustment`

## 7. Business Constraints

- An `outbound` movement that would leave stock below zero must be rejected — this is the "unwanted behavior" criterion the README's spec phase requires.
- An `outbound` or `adjustment` referencing a nonexistent `item_id` or `lot_id` must be rejected.
- A `training_materials` item with lot tracking should not be issued (`outbound`) from a lot past its `expiry_date` — a certification voucher that has expired can't be assigned to a learner.

## 8. Expected Deliverables

- Spec, plan, and tasks covering item CRUD, movement logging, and the reorder-point signal, scoped to the fields in §3 and using only the catalogue values in §2.
- A test suite verifying the stock invariant (§4) and the unwanted-behavior criteria (§7).
- The reorder-point flag working per office, using the values from your seed data.
