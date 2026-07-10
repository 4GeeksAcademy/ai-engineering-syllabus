# CONTEXT — Milestone 5: Backend Inventory Management

## Company: Nexova

**Path:** `05-backend-inventory-orm/CONTEXT-nexova.md`

---

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with 120 employees across Valencia (Spain) and Miami (USA). Its three business lines — executive headhunting, customer support outsourcing, and corporate training — all depend on technology equipment being allocated correctly to the right people at the right time.

With 6 offices, 30 outsourced support agents, and constant hiring cycles, Nexova's IT and operations team has zero visibility into what hardware and equipment is in stock, who has been issued what, and what has been consumed. Laptops go missing. Equipment is double-allocated. Office supplies run out without warning.

**Sergio Molina (CTO)** has assigned this milestone to your squad as part of the Nexova platform build.

> **From Sergio (CTO) — Jira ticket NXV-0201:**
> "We need an equipment and supplies inventory API. An 'asset entry' is a purchase or delivery received by the company. An 'asset exit' is an allocation to an employee or a consumption event. Stock is always the net result of entries minus exits — you cannot set it directly. All routes under `/inventory`. See the entity spec. Use the TinyDB user UUID on every order."

---

## Entity Names and Field Specification

Use these names exactly in your models, schemas, and API responses.

### `Asset` (maps to README's `Product`)

| Field           | Type       | Notes                                                                                  |
| --------------- | ---------- | -------------------------------------------------------------------------------------- |
| `id`            | `int` (PK) | Auto-increment                                                                         |
| `name`          | `str`      | e.g., `"Laptop 14\" Business"`, `"Ergonomic mouse"`, `"A4 paper ream"`                 |
| `sku`           | `str`      | Unique code, e.g., `"NXV-IT-001"`, `"NXV-OFF-003"`                                     |
| `category`      | `str`      | `"hardware"`, `"peripherals"`, `"office_supplies"`, `"training_materials"`             |
| `office`        | `str`      | `"Valencia"` or `"Miami"`                                                              |
| `current_stock` | `int`      | **Computed field — not stored.** Derived from orders. Include in response schema only. |

### `AssetEntry` (maps to README's `InboundOrder`)

A purchase or supplier delivery received by Nexova.

| Field        | Type               | Notes                                                                    |
| ------------ | ------------------ | ------------------------------------------------------------------------ |
| `id`         | `int` (PK)         | Auto-increment                                                           |
| `asset_id`   | `int` (FK → Asset) |                                                                          |
| `quantity`   | `int`              | Units received                                                           |
| `supplier`   | `str`              | Supplier or vendor name                                                  |
| `office`     | `str`              | `"Valencia"` or `"Miami"` — receiving office                             |
| `created_at` | `datetime`         | Auto-set on creation                                                     |
| `user_uuid`  | `str`              | UUID of the IT/operations manager who registered the entry (from TinyDB) |

### `AssetExit` (maps to README's `OutboundOrder`)

An asset allocation to an employee or a consumption event.

| Field         | Type               | Notes                                                                               |
| ------------- | ------------------ | ----------------------------------------------------------------------------------- |
| `id`          | `int` (PK)         | Auto-increment                                                                      |
| `asset_id`    | `int` (FK → Asset) |                                                                                     |
| `quantity`    | `int`              | Units allocated or consumed                                                         |
| `exit_type`   | `str`              | `"allocation"` (assigned to an employee) or `"consumption"` (consumed, e.g., paper) |
| `assigned_to` | `str \| None`      | Employee name or ID if `exit_type = "allocation"`. Null for consumptions.           |
| `office`      | `str`              | `"Valencia"` or `"Miami"`                                                           |
| `created_at`  | `datetime`         | Auto-set on creation                                                                |
| `user_uuid`   | `str`              | UUID of the manager who registered the exit (from TinyDB)                           |

---

## API Router

All endpoints must be registered under the `/inventory` prefix. The router file lives at `services/routers/inventory.py`.

| Method | Path                         | Description                                         |
| ------ | ---------------------------- | --------------------------------------------------- |
| `GET`  | `/inventory/products`        | List all assets with `current_stock`                |
| `POST` | `/inventory/products`        | Register a new asset                                |
| `GET`  | `/inventory/products/{id}`   | Get one asset with current stock                    |
| `POST` | `/inventory/orders/inbound`  | Register an asset delivery (`AssetEntry`)           |
| `POST` | `/inventory/orders/outbound` | Register an allocation or consumption (`AssetExit`) |
| `GET`  | `/inventory/orders`          | List all entries and exits with asset data          |

---

## Business Rules

1. **`current_stock` is always computed**, never stored. For any given asset: `current_stock = SUM(AssetEntry.quantity) − SUM(AssetExit.quantity)`.
2. **An exit cannot be processed if it would exceed available stock.** Return `HTTP 400` with the message: `"Insufficient stock for asset '{name}'. Available: {available}, requested: {quantity}."`. Reject before writing.
3. **`assigned_to` is required when `exit_type = "allocation"` and must be null when `exit_type = "consumption"`**. Validate this in the request schema or route logic.
4. **No user table in Supabase.** The `user_uuid` fields reference TinyDB users. Do not create a User model in SQLModel.
5. **Both offices coexist in the same tables.** Use the `office` field to filter by location when needed.

---

## Seed Data

Create the following records when setting up your local development database.

### Assets (minimum 6)

| name                         | sku         | category           | office   |
| ---------------------------- | ----------- | ------------------ | -------- |
| Laptop 14" Business          | NXV-IT-001  | hardware           | Valencia |
| Laptop 14" Business          | NXV-IT-002  | hardware           | Miami    |
| Ergonomic mouse              | NXV-PER-001 | peripherals        | Valencia |
| USB-C Hub                    | NXV-PER-002 | peripherals        | Miami    |
| A4 paper ream                | NXV-OFF-001 | office_supplies    | Valencia |
| Leadership training workbook | NXV-TRN-001 | training_materials | Valencia |

### AssetEntries (minimum 4)

Log at least 2 deliveries for `NXV-IT-001` (e.g., 10 and 5 units) and 1 delivery for two other assets. Use supplier names like `"TechDistrib Valencia S.L."`, `"Office Depot Miami"`.

### AssetExits (minimum 3)

Include at least one `"allocation"` exit (with `assigned_to` populated) and one `"consumption"` exit (with `assigned_to` as null). Quantities must not exceed the seeded entries.

---

## File Structure (within `services/`)

```text
services/
├── main.py
├── database.py          # TinyDB client + SQLModel engine + get_db dependency
├── models.py            # Asset, AssetEntry, AssetExit (SQLModel)
├── schemas.py           # Pydantic request/response schemas
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Acceptance Notes for Nexova

- The evaluator will attempt an `AssetExit` with a quantity exceeding stock and expect `HTTP 400`.
- The evaluator will attempt an `AssetExit` with `exit_type = "allocation"` and no `assigned_to` value and expect a validation error.
- The evaluator will call `GET /inventory/products` and verify `current_stock` reflects the net of seeded data.
- The `office` field must appear in both models and response schemas.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_Milestone 5 · Nexova scenario_
