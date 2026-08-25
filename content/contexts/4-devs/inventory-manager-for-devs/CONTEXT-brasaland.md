# CONTEXT — Brasaland: Inventory Manager

## 1. Company Snapshot

**Brasaland** runs 14 grilled-food restaurants across Colombia and Florida. Ingredient ordering today happens by WhatsApp or phone call, each location manager ordering what they think they need — the result is overstock at some locations and stockouts at others, with no visibility for **Felipe Guerrero** (Operations Director) or **Lucía Fernández** (Procurement Manager) into what's actually on hand anywhere in the chain.

You are building the inventory manager that gives each location an accurate, real-time view of stock, derived strictly from recorded movements, with automatic flagging when a location is about to run out of something it needs for service.

## 2. Domain Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Units of Measure

`kg`, `g`, `l`, `ml`, `unit`

### 2.2 Categories

| Value | Examples |
|---|---|
| `meat` | Beef cuts, chicken, pork |
| `produce` | Vegetables, herbs |
| `sauces_condiments` | House sauces, marinades |
| `beverages` | Soft drinks, juices |
| `packaging` | Takeout containers, napkins |
| `cleaning_supplies` | Sanitizer, degreaser |

### 2.3 Locations

Every item and movement belongs to one of Brasaland's 14 locations. Seed at least 4, mixing Colombia and Florida — locations are a first-class dimension here, not an afterthought: stock is tracked per location, not chain-wide.

## 3. Entity Fields

### 3.1 Item

- `location_id`
- `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numeric, in the item's unit of measure)
- `created_at`, `updated_at`

### 3.2 Lot (required for `meat` and `produce`; optional for other categories)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movement

- `item_id`, `lot_id` (nullable — only required for items with lot tracking)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (required for `adjustment`; e.g. `waste`, `theft`, `count_correction`)
- `created_at`

## 4. The Invariant

An item's available stock at a location is the sum of its `inbound` movements minus its `outbound` movements, adjusted by any `adjustment` entries — computed, never stored as an editable field. This is the same invariant the README requires; this CONTEXT doesn't relax it for any category, including `cleaning_supplies`.

## 5. Reorder Point

`reorder_point` is set per item, per location — the same ingredient can have a different threshold at a high-volume Medellín location than at a smaller Florida one. When stock at a location drops at or below `reorder_point`, the backoffice must flag it visibly.

## 6. Seed Data

Seed at least 15 items across at least 4 locations and all six categories, with:

- At least 3 items using lot tracking, including one lot with an `expiry_date` in the past (to exercise expired-stock handling)
- At least 2 items currently at or below their `reorder_point`
- A movement history per item deep enough to show at least one `inbound`, one `outbound`, and one `adjustment`

## 7. Business Constraints

- An `outbound` movement that would leave stock below zero must be rejected — this is the "unwanted behavior" criterion the README's spec phase requires.
- An `outbound` or `adjustment` referencing a nonexistent `item_id` or `lot_id` must be rejected.
- `waste` and `theft` adjustment reasons should be distinguishable in any stock report, since Felipe's team tracks them separately.

## 8. Expected Deliverables

- Spec, plan, and tasks covering item CRUD, movement logging, and the reorder-point signal, scoped to the fields in §3 and using only the catalogue values in §2.
- A test suite verifying the stock invariant (§4) and the unwanted-behavior criteria (§7).
- The reorder-point flag working per location, using the values from your seed data.
