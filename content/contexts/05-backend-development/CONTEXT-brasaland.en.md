# CONTEXT — Milestone 5: Backend Inventory Management

## Company: Brasaland

**Path:** `05-backend-inventory-orm/CONTEXT-brasaland.md`

---

## Your Company

**Brasaland** is a grilled food restaurant chain with 14 locations across Colombia and Florida. The company processes hundreds of ingredient orders every week: meat, vegetables, sauces, beverages, packaging, and cleaning products arrive from ~20 suppliers across both countries, and those same ingredients leave each kitchen every day through preparation and — inevitably — waste.

Until now, ingredient stock at each location has been managed by the local manager via WhatsApp and spreadsheets. **Nicolás Park (CTO)** has assigned your squad to build the centralised ingredient inventory layer of the Brasaland Digital platform. This is the first time Brasaland will have a single source of truth for what is in stock across the chain.

> **From Nicolás (CTO) — Notion ticket #BRD-0512:**
> "The operations team is going in blind on ingredients. Felipe's supervisors don't know how much beef is available in Miami until they call the kitchen. Build the inventory API. Ingredient entries come from supplier deliveries; exits come from consumption logs and waste reports. Stock must be read-only — it's always the net of what arrived minus what was used. All endpoints under `/inventory`. Check the entity spec below."

---

## Entity Names and Field Specification

Use these names exactly in your models, schemas, and API responses.

### `Ingredient` (maps to README's `Product`)

| Field           | Type       | Notes                                                                                         |
| --------------- | ---------- | --------------------------------------------------------------------------------------------- |
| `id`            | `int` (PK) | Auto-increment                                                                                |
| `name`          | `str`      | e.g., `"Beef brisket"`, `"House sauce"`, `"Takeaway box (M)"`                                 |
| `sku`           | `str`      | Unique internal code, e.g., `"BRS-BEEF-001"`                                                  |
| `unit`          | `str`      | Unit of measure: `"kg"`, `"litre"`, `"unit"`                                                  |
| `category`      | `str`      | `"meat"`, `"produce"`, `"sauce"`, `"beverage"`, `"packaging"`, `"cleaning"`                   |
| `country`       | `str`      | `"CO"` (Colombia) or `"US"` (United States)                                                   |
| `current_stock` | `float`    | **Computed field — not stored.** Always derived from orders. Include in response schema only. |

### `IngredientEntry` (maps to README's `InboundOrder`)

An ingredient delivery received from a supplier.

| Field           | Type                    | Notes                                                                      |
| --------------- | ----------------------- | -------------------------------------------------------------------------- |
| `id`            | `int` (PK)              | Auto-increment                                                             |
| `ingredient_id` | `int` (FK → Ingredient) |                                                                            |
| `quantity`      | `float`                 | Amount received in the ingredient's unit                                   |
| `supplier_name` | `str`                   | Name of the supplier for this delivery                                     |
| `location_id`   | `int`                   | Receiving location (1–14). Not a FK — location data is managed separately. |
| `created_at`    | `datetime`              | Auto-set on creation                                                       |
| `user_uuid`     | `str`                   | UUID of the operations supervisor who logged the delivery (from TinyDB)    |

### `IngredientExit` (maps to README's `OutboundOrder`)

An ingredient consumption log or waste report.

| Field           | Type                    | Notes                                                      |
| --------------- | ----------------------- | ---------------------------------------------------------- |
| `id`            | `int` (PK)              | Auto-increment                                             |
| `ingredient_id` | `int` (FK → Ingredient) |                                                            |
| `quantity`      | `float`                 | Amount consumed or wasted                                  |
| `reason`        | `str`                   | `"consumption"` or `"waste"`                               |
| `location_id`   | `int`                   | Location where the exit occurred                           |
| `created_at`    | `datetime`              | Auto-set on creation                                       |
| `user_uuid`     | `str`                   | UUID of the staff member who logged the exit (from TinyDB) |

---

## API Router

All endpoints must be registered under the `/inventory` prefix. The router file lives at `services/routers/inventory.py`.

| Method | Path                         | Description                                        |
| ------ | ---------------------------- | -------------------------------------------------- |
| `GET`  | `/inventory/products`        | List all ingredients with `current_stock`          |
| `POST` | `/inventory/products`        | Create a new ingredient                            |
| `GET`  | `/inventory/products/{id}`   | Get one ingredient with current stock              |
| `POST` | `/inventory/orders/inbound`  | Log an ingredient delivery (`IngredientEntry`)     |
| `POST` | `/inventory/orders/outbound` | Log a consumption or waste exit (`IngredientExit`) |
| `GET`  | `/inventory/orders`          | List all entries and exits with ingredient data    |

---

## Business Rules

1. **`current_stock` is always computed**, never stored. For any given ingredient: `current_stock = SUM(IngredientEntry.quantity) − SUM(IngredientExit.quantity)`.
2. **An exit cannot be logged if it would result in negative stock.** Return `HTTP 400` with the message: `"Insufficient stock for ingredient '{name}'. Available: {available}, requested: {requested}."`. Reject before writing.
3. **Both Colombia and US ingredients exist in the same table.** Use the `country` field to filter by market when needed.
4. **No user table in Supabase.** The `user_uuid` fields reference TinyDB users. Do not create a User model in SQLModel.
5. **Locations are numeric IDs 1–14.** They are not foreign keys in this milestone — store only the integer.

---

## Seed Data

Create the following records when setting up your local development database. They must be present before your demo.

### Ingredients (minimum 6)

| name              | sku           | unit  | category  | country |
| ----------------- | ------------- | ----- | --------- | ------- |
| Beef brisket      | BRS-BEEF-001  | kg    | meat      | CO      |
| Pork ribs         | BRS-PORK-001  | kg    | meat      | US      |
| Chimichurri sauce | BRS-SAUCE-001 | litre | sauce     | CO      |
| House BBQ sauce   | BRS-SAUCE-002 | litre | sauce     | US      |
| Yuca (cassava)    | BRS-PROD-001  | kg    | produce   | CO      |
| Takeaway box (M)  | BRS-PKG-001   | unit  | packaging | CO      |

### IngredientEntries (minimum 4)

Log at least 2 deliveries for `BRS-BEEF-001` (e.g., 50 kg and 30 kg) and 1 delivery for each of two other ingredients. Use realistic supplier names: `"Carnes del Valle S.A."`, `"MiamiMeat Co."`, `"Salsas Artesanales Ltda."`.

### IngredientExits (minimum 3)

Log consumption exits that reduce stock without going below zero. Include at least one `"waste"` exit. Use `user_uuid` values that correspond to existing users in your TinyDB instance.

---

## File Structure (within `services/`)

```text
services/
├── main.py
├── database.py          # TinyDB client + SQLModel engine + get_db dependency
├── models.py            # Ingredient, IngredientEntry, IngredientExit (SQLModel)
├── schemas.py           # Pydantic request/response schemas
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Acceptance Notes for Brasaland

- The evaluator will create an `IngredientExit` exceeding available stock and expect `HTTP 400`.
- The evaluator will call `GET /inventory/products` and verify that `current_stock` reflects the net of seeded entries and exits.
- The `country` field must appear in both the model and the response schema.
- The `reason` field on `IngredientExit` must accept only `"consumption"` or `"waste"`.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_Milestone 5 · Brasaland scenario_
