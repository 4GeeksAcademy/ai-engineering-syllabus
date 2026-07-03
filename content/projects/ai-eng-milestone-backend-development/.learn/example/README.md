# In-Class Example — Campus Coffee Cart Pantry (FastAPI + SQLModel + Dual DB)

> **Instructor note:** Classroom-paced parallel to `ai-eng-milestone-backend-development`. Same stack and patterns (TinyDB auth + Supabase inventory + SQLModel ORM + computed stock), different domain so students don't confuse it with their company monorepo work. Target: one 60–90 minute live session.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The challenge

A campus coffee cart tracks supplies on a whiteboard: beans, cups, lids. The student-run cart needs a tiny internal API so volunteers can register **restocks** (supplier delivery) and **usage withdrawals** (end-of-shift consumption) without editing stock numbers by hand.

Non-negotiable rule from the cart lead:

> _"Nobody edits stock directly. Restock adds units; usage removes them. Every movement must record which volunteer logged it."_

Build this on the **same FastAPI service** students already use for auth — extend it, don't start a new repo.

### Scope note

| Kept (same spine as graded project)             | Simplified for class                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| TinyDB + Supabase dual connection               | No CONTEXT.md — generic `Product` only (`id`, `name`, `sku`) |
| SQLModel models + separate Pydantic schemas     | No company-specific fields (`warehouse`, `exit_type`, etc.)  |
| `/inventory` router with all 6 endpoints        | No seed-data script required in class                        |
| Computed `current_stock` from orders            | Single location — no per-warehouse stock split               |
| Auth on create endpoints; `user_uuid` on orders | Reuse existing `get_current_user` from prior milestone       |
| `400` before persist on insufficient stock      | —                                                            |

Students still follow the full rubric in the project root `README.md`.

---

## Tech stack

| Layer           | Tool                          |
| --------------- | ----------------------------- |
| API             | FastAPI                       |
| Auth store      | TinyDB (existing)             |
| Inventory store | Supabase / PostgreSQL         |
| ORM             | SQLModel                      |
| Session         | `Depends(get_db)` per request |

---

## Suggested file layout (`services/`)

```text
services/
├── main.py
├── database.py          # TinyDB + SQLModel engine + get_db
├── models.py            # Product, InboundOrder, OutboundOrder
├── schemas.py           # Pydantic request/response (separate file)
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Data model (class example only)

### `Product`

| Field  | Type     | Notes                      |
| ------ | -------- | -------------------------- |
| `id`   | int (PK) | Auto-increment             |
| `name` | str      | e.g. `"Arabica Beans 1kg"` |
| `sku`  | str      | e.g. `"BEAN-AR-1K"`        |

`current_stock` appears **only** in response schemas — never as a DB column.

### `InboundOrder` (restock)

| Field        | Type               | Notes                                             |
| ------------ | ------------------ | ------------------------------------------------- |
| `id`         | int (PK)           |                                                   |
| `product_id` | int (FK → Product) |                                                   |
| `quantity`   | int                | Units received                                    |
| `created_at` | datetime           | Auto-set                                          |
| `user_uuid`  | str                | Volunteer from TinyDB — no user table in Supabase |

### `OutboundOrder` (usage)

Same shape as inbound; represents units consumed during a shift.

---

## What to build

### Database setup

- [ ] Add `DATABASE_URL` to `.env` using the Supabase **Transaction pooler** URI (**Connect → Direct** → Transaction pooler → URI). Keep existing TinyDB vars.
- [ ] In `database.py`, expose both TinyDB client and SQLModel `engine`.
- [ ] Implement `get_db()` generator; inject with `Depends()` — no global session.

### ORM + schemas

- [ ] `models.py`: `Product`, `InboundOrder`, `OutboundOrder` with `SQLModel, table=True` and FK on `product_id`.
- [ ] `schemas.py`: separate create/read schemas; `ProductRead` includes computed `current_stock`.
- [ ] Call `SQLModel.metadata.create_all(engine)` on startup.

### Inventory router (`/inventory`)

| Method | Path                         | Auth | Action                                        |
| ------ | ---------------------------- | ---- | --------------------------------------------- |
| `GET`  | `/inventory/products`        | —    | List products + `current_stock`               |
| `POST` | `/inventory/products`        | ✓    | Create product (starts at 0 stock)            |
| `GET`  | `/inventory/products/{id}`   | —    | One product + stock                           |
| `POST` | `/inventory/orders/inbound`  | ✓    | Register restock                              |
| `POST` | `/inventory/orders/outbound` | ✓    | Register usage                                |
| `GET`  | `/inventory/orders`          | —    | All movements with product name + `user_uuid` |

### Business rules (demo these live)

- [ ] `current_stock = SUM(inbound qty) − SUM(outbound qty)` per product.
- [ ] Store authenticated user's UUID in `user_uuid` on order create.
- [ ] Reject outbound when stock would go negative → `HTTP 400` **before** `session.commit()`.
- [ ] Endpoints return Pydantic schemas, never raw SQLModel instances.

### Tiny seed for live demo (optional)

| name              | sku        |
| ----------------- | ---------- |
| Arabica Beans 1kg | BEAN-AR-1K |
| Paper Cups 12oz   | CUP-12-P   |

Walkthrough: create product → inbound 50 beans → outbound 12 → outbound 40 (should 400).

---

## Key concepts to discuss in class

| Concept                     | Where it appears                                    |
| --------------------------- | --------------------------------------------------- |
| Dual DB routing             | TinyDB in auth dep; SQLModel in inventory routes    |
| ORM vs schema split         | `models.py` vs `schemas.py`                         |
| Derived state               | `current_stock` computed, not stored                |
| FK without user replication | `user_uuid` string, no Supabase users table         |
| Guard before write          | Stock check on outbound                             |
| N+1 awareness               | Mention when listing orders — load products eagerly |

---

## Verify together

- [ ] `GET /inventory/products` shows `current_stock: 0` on new product.
- [ ] After inbound 50, stock shows 50 without a stock column in DB.
- [ ] Outbound 60 returns `400`; DB still shows 50 available.
- [ ] `GET /inventory/orders` lists movements with `user_uuid` populated.
- [ ] `/docs` shows all routes under `/inventory`.

---

## Discussion questions

1. Why keep users in TinyDB instead of copying a `users` table into Supabase? What breaks if we duplicate user rows?
2. Where should stock calculation live — inline in the route, a service function, or a SQL aggregate? What are the trade-offs for testing?
3. If `GET /inventory/orders` loads 20 orders and fetches each product in a loop, what happens to performance? How would you fix it in one query?
