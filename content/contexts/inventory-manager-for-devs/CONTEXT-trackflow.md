# CONTEXT — TrackFlow: Inventory Manager

## 1. Company Snapshot

**TrackFlow** runs warehouses in Los Angeles and Zaragoza for mid-sized fashion, electronics, and cosmetics brands that outsource their entire logistics operation. Each warehouse uses a different, disconnected system today, and **Ana Whitfield** (Head of Warehouse Operations) cannot answer "how many units of this SKU do we have across both countries?" without calling both sites. Inventory discrepancies are frequent and caught late.

You are building the inventory manager that gives TrackFlow a real-time, per-warehouse view of client stock, derived strictly from recorded movements, with automatic flagging when a SKU is about to run out.

## 2. Domain Catalogues

Use these exact values. Do not invent additional ones or rename them.

### 2.1 Units of Measure

`unit`, `box`, `kg`

### 2.2 Categories

| Value | Examples |
|---|---|
| `fashion` | Apparel, footwear, accessories |
| `electronics` | Small devices, accessories, components |
| `cosmetics` | Skincare, makeup, personal care |

### 2.3 Warehouses

Every item and movement belongs to one of TrackFlow's two warehouses: `los_angeles`, `zaragoza`. Stock is tracked per warehouse — TrackFlow doesn't ship a client's stock across the Atlantic to cover a shortfall, so the two never net against each other.

## 3. Entity Fields

### 3.1 Item

- `warehouse` (§2.3), `client_name` (the e-commerce brand that owns the SKU)
- `sku`, `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numeric, in the item's unit of measure)
- `created_at`, `updated_at`

### 3.2 Lot (required for `cosmetics`; optional for other categories)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movement

- `item_id`, `lot_id` (nullable — only required for items with lot tracking)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (required for `adjustment`; e.g. `damaged`, `count_correction`, `return_restock`)
- `created_at`

## 4. The Invariant

An item's available stock at a warehouse is the sum of its `inbound` movements minus its `outbound` movements, adjusted by any `adjustment` entries — computed, never stored as an editable field. This is the same invariant the README requires; this CONTEXT doesn't relax it for any category.

## 5. Reorder Point

`reorder_point` is set per item, per warehouse — the same SKU can have a different threshold at the higher-volume Los Angeles warehouse than at Zaragoza. When stock at a warehouse drops at or below `reorder_point`, the backoffice must flag it visibly, matching the low-stock alert the client and procurement team rely on.

## 6. Seed Data

Seed at least 15 items across both warehouses, at least 3 different clients, and all three categories, with:

- At least 3 `cosmetics` items using lot tracking, including one lot with an `expiry_date` in the past
- At least 2 items currently at or below their `reorder_point`
- A movement history per item deep enough to show at least one `inbound`, one `outbound`, and one `adjustment`, including at least one `return_restock` adjustment tied to a reverse-logistics flow

## 7. Business Constraints

- An `outbound` movement that would leave stock below zero must be rejected — this is the "unwanted behavior" criterion the README's spec phase requires.
- An `outbound` or `adjustment` referencing a nonexistent `item_id` or `lot_id` must be rejected.
- Two items with the same `sku` but different `client_name` are different inventory records — SKUs are not globally unique across clients, only within a client.

## 8. Expected Deliverables

- Spec, plan, and tasks covering item CRUD, movement logging, and the reorder-point signal, scoped to the fields in §3 and using only the catalogue values in §2.
- A test suite verifying the stock invariant (§4) and the unwanted-behavior criteria (§7).
- The reorder-point flag working per warehouse, using the values from your seed data.
