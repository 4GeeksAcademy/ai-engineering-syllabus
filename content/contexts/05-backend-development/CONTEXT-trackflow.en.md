# CONTEXT — Milestone 5: Backend Inventory Management

## Company: TrackFlow

**Path:** `05-backend-inventory-orm/CONTEXT-trackflow.md`

---

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (USA) and Zaragoza (Spain). Its core business is managing warehouse inventory on behalf of e-commerce brands — fashion, electronics, and cosmetics — that outsource their entire logistics operation.

Every product unit that flows through TrackFlow's warehouses must be tracked precisely: when it arrives from the client brand, and when it leaves for a customer delivery. A discrepancy in stock is a contractual issue, not just an internal problem. Clients expect real-time accuracy.

Until now, each warehouse has used a different system (one commercial WMS, one advanced spreadsheet) with no shared data layer. **Andrés Kim (CTO)** has escalated this to a priority milestone.

> **From Andrés (CTO) — Linear ticket TRK-0341:**
> "This is the foundation of everything. We need a unified inventory API for SKUs across both warehouses. A 'stock entry' is a goods receipt from a client brand. A 'stock exit' is a dispatch for a customer shipment or a confirmed loss. Stock is always computed — entries minus exits — never set directly. All routes under `/inventory`. The full entity spec is below. Auth stays in TinyDB."

---

## Entity Names and Field Specification

Use these names exactly in your models, schemas, and API responses.

### `SKU` (maps to README's `Product`)

| Field           | Type       | Notes                                                                                           |
| --------------- | ---------- | ----------------------------------------------------------------------------------------------- |
| `id`            | `int` (PK) | Auto-increment                                                                                  |
| `name`          | `str`      | Product description, e.g., `"Classic White Sneaker - Size 42"`                                  |
| `sku`           | `str`      | Client-assigned code, e.g., `"CLT-SNK-W-42"`                                                    |
| `client_name`   | `str`      | The brand that owns this SKU, e.g., `"PureStep Footwear"`                                       |
| `category`      | `str`      | `"fashion"`, `"electronics"`, or `"cosmetics"`                                                  |
| `warehouse`     | `str`      | `"LA"` (Los Angeles) or `"ZGZ"` (Zaragoza)                                                      |
| `current_stock` | `int`      | **Computed field — not stored.** Derived from stock movements. Include in response schema only. |

### `StockEntry` (maps to README's `InboundOrder`)

A goods receipt: a shipment from a client brand arrives at a TrackFlow warehouse.

| Field        | Type             | Notes                                                                   |
| ------------ | ---------------- | ----------------------------------------------------------------------- |
| `id`         | `int` (PK)       | Auto-increment                                                          |
| `sku_id`     | `int` (FK → SKU) |                                                                         |
| `quantity`   | `int`            | Units received                                                          |
| `reference`  | `str`            | Client's dispatch reference (e.g., purchase order number)               |
| `warehouse`  | `str`            | `"LA"` or `"ZGZ"` — receiving warehouse                                 |
| `created_at` | `datetime`       | Auto-set on creation                                                    |
| `user_uuid`  | `str`            | UUID of the warehouse operative who confirmed the receipt (from TinyDB) |

### `StockExit` (maps to README's `OutboundOrder`)

A dispatch: units leave the warehouse for a customer delivery or are written off as a loss.

| Field             | Type             | Notes                                                                          |
| ----------------- | ---------------- | ------------------------------------------------------------------------------ |
| `id`              | `int` (PK)       | Auto-increment                                                                 |
| `sku_id`          | `int` (FK → SKU) |                                                                                |
| `quantity`        | `int`            | Units dispatched or written off                                                |
| `exit_type`       | `str`            | `"dispatch"` (customer shipment) or `"loss"` (confirmed discrepancy or damage) |
| `tracking_number` | `str \| None`    | Carrier tracking number if `exit_type = "dispatch"`. Null for losses.          |
| `warehouse`       | `str`            | `"LA"` or `"ZGZ"`                                                              |
| `created_at`      | `datetime`       | Auto-set on creation                                                           |
| `user_uuid`       | `str`            | UUID of the logistics coordinator who authorised the exit (from TinyDB)        |

---

## API Router

All endpoints must be registered under the `/inventory` prefix. The router file lives at `services/routers/inventory.py`.

| Method | Path                         | Description                               |
| ------ | ---------------------------- | ----------------------------------------- |
| `GET`  | `/inventory/products`        | List all SKUs with `current_stock`        |
| `POST` | `/inventory/products`        | Register a new SKU                        |
| `GET`  | `/inventory/products/{id}`   | Get one SKU with current stock            |
| `POST` | `/inventory/orders/inbound`  | Register a goods receipt (`StockEntry`)   |
| `POST` | `/inventory/orders/outbound` | Register a dispatch or loss (`StockExit`) |
| `GET`  | `/inventory/orders`          | List all stock movements with SKU data    |

---

## Business Rules

1. **`current_stock` is always computed**, never stored. For any SKU: `current_stock = SUM(StockEntry.quantity) − SUM(StockExit.quantity)`.
2. **A `StockExit` cannot be registered if quantity would push stock below zero.** Return `HTTP 400` with the message: `"Insufficient stock for SKU '{sku}'. Available: {available}, requested: {quantity}."`. Reject before writing.
3. **`tracking_number` is required when `exit_type = "dispatch"` and must be null when `exit_type = "loss"`**. Validate in schema or route logic.
4. **No user table in Supabase.** The `user_uuid` fields reference TinyDB users. Do not create a User model in SQLModel.
5. **Los Angeles and Zaragoza warehouses coexist in the same tables.** The `warehouse` field (`"LA"` or `"ZGZ"`) must be present on both SKU and movement records.
6. **Stock is per SKU per warehouse**, not aggregated globally. A SKU with 20 units in LA and 15 in ZGZ has two separate stock figures — not 35.

> ⚠️ Rule 6 changes the `current_stock` calculation: filter movements by `warehouse` when computing stock for a given location. When listing all SKUs, you may show total stock or per-warehouse breakdown — document your choice.

---

## Seed Data

Create the following records when setting up your local development database.

### SKUs (minimum 6)

| name                            | sku            | client_name           | category    | warehouse |
| ------------------------------- | -------------- | --------------------- | ----------- | --------- |
| Classic White Sneaker - Size 42 | CLT-SNK-W-42   | PureStep Footwear     | fashion     | LA        |
| Classic White Sneaker - Size 42 | CLT-SNK-W-42-Z | PureStep Footwear     | fashion     | ZGZ       |
| Wireless Earbuds Pro            | TEC-EAR-001    | SoundWave Electronics | electronics | LA        |
| Hydrating Face Serum 30ml       | CSM-SRM-030    | GlowLab Cosmetics     | cosmetics   | ZGZ       |
| Slim Fit Chino - Navy 32/32     | CLT-CHN-N-32   | UrbanThread           | fashion     | LA        |
| USB-C Fast Charger 65W          | TEC-CHG-065    | SoundWave Electronics | electronics | ZGZ       |

### StockEntries (minimum 4)

Log at least 2 receipts for the same SKU in different quantities. Use realistic reference codes like `"PO-2024-0098"`, `"GR-LA-0234"`. Mix both warehouses.

### StockExits (minimum 3)

Include at least one `"dispatch"` (with a `tracking_number` like `"1Z999AA10123456784"`) and one `"loss"` (with `tracking_number` as null). Quantities must not exceed seeded entries for the same warehouse.

---

## File Structure (within `services/`)

```text
services/
├── main.py
├── database.py          # TinyDB client + SQLModel engine + get_db dependency
├── models.py            # SKU, StockEntry, StockExit (SQLModel)
├── schemas.py           # Pydantic request/response schemas
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Acceptance Notes for TrackFlow

- The evaluator will register a `StockExit` exceeding warehouse stock and expect `HTTP 400`.
- The evaluator will attempt a `"dispatch"` exit without a `tracking_number` and expect a validation error.
- The evaluator will verify that stock figures are per-warehouse, not aggregated.
- The `warehouse` field must be present on SKU, StockEntry, and StockExit models and their response schemas.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_Milestone 5 · TrackFlow scenario_
