# Milestone 5 — Backend: Inventory Management with ORM & Dual Database (reference solution)

This README is the canonical reference for **"Milestone 5 — Backend: Inventory Management with ORM & Dual Database"**. It describes how a correct implementation should be structured in the student monorepo (`services/`), how dual-database access should work, and what reviewers should verify. The actual code lives in the student's fork of `ai-engineering-company-project-monorepo`; this folder documents the expected design only.

## Alignment with company context

Entity names, extra fields, validation rules, and seed data must follow the student's assigned **CONTEXT-company.md** under `content/contexts/05-backend-development/`. The README uses generic names (`Product`, `InboundOrder`, `OutboundOrder`); each CONTEXT file maps those to company-specific models (e.g. TrackFlow uses `SKU`, `StockEntry`, `StockExit` with `warehouse`, `client_name`, `exit_type`, etc.). A generic implementation that ignores CONTEXT will not pass evaluation.

## Solution architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI application                     │
├──────────────────────────┬──────────────────────────────────┤
│  TinyDB (existing)       │  Supabase / PostgreSQL (new)     │
│  • users                 │  • Product / SKU                 │
│  • auth tokens           │  • InboundOrder / StockEntry     │
│  • get_current_user()    │  • OutboundOrder / StockExit    │
└──────────────────────────┴──────────────────────────────────┘
         ▲                              ▲
         │ JWT / session lookup         │ SQLModel session per request
         │                              │ (Depends(get_db))
```

- **TinyDB** remains the single source of truth for users and authentication (from prior milestones).
- **Supabase** stores all inventory entities. No user table is replicated in PostgreSQL.
- Order records store `user_uuid` as a plain string referencing the TinyDB user who created the order.

## Recommended file structure (within `services/`)

```text
services/
├── main.py              # FastAPI app, register inventory router, create_all on startup
├── database.py          # TinyDB client + SQLModel engine + get_db dependency
├── models.py            # SQLModel table models (ORM only)
├── schemas.py           # Pydantic request/response schemas (separate from ORM)
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

Optional but recommended: `tests/test_inventory.py` for stock calculation and outbound rejection.

## Database configuration

### Supabase connection

In the Supabase dashboard (**Connect → Direct**), choose **Transaction pooler** as the connection method and **URI** as the type — then copy that string into `DATABASE_URL`. Do not use the direct connection string (port `5432`); the pooler URI uses port `6543` and a `*.pooler.supabase.com` host.

See the student-facing screenshots in the project root `.learn/` folder (`supabase-transaction-pooler-uri.png`, `supabase-transaction-pooler-connection-string.png`).

### Environment variables (`.env`)

```env
# Existing — do not remove
TINYDB_PATH=...
JWT_SECRET=...
ACCESS_TOKEN_EXPIRE_MINUTES=...

# New for this milestone — Transaction pooler URI from Supabase
DATABASE_URL=postgresql://postgres.[project-ref]:password@aws-0-region.pooler.supabase.com:6543/postgres
```

Never hardcode credentials. Confirm `.env` is listed in `.gitignore`.

### `database.py` pattern

```python
from sqlmodel import Session, SQLModel, create_engine
from tinydb import TinyDB

tinydb = TinyDB(os.getenv("TINYDB_PATH"))
engine = create_engine(os.getenv("DATABASE_URL"), echo=False)

def get_db():
    with Session(engine) as session:
        yield session
```

- Initialise **both** connections in one module (or split TinyDB vs SQLModel clearly, but both must be importable).
- `get_db` yields a session per request via `Depends()` — no global `Session` variable.

### Schema initialisation

On application startup (e.g. in `main.py` lifespan or `@app.on_event("startup")`):

```python
SQLModel.metadata.create_all(engine)
```

Acceptable for learning; production would use Alembic migrations instead.

## ORM models (`models.py`)

Minimum models (names may differ per CONTEXT):

| README name     | Typical CONTEXT alias | Required fields (minimum)                                      |
| --------------- | --------------------- | -------------------------------------------------------------- |
| `Product`       | `SKU`, `Item`, etc.   | `id`, `name`, `sku` + company-specific fields from CONTEXT     |
| `InboundOrder`  | `StockEntry`, etc.    | `id`, `product_id` (FK), `quantity`, `created_at`, `user_uuid` |
| `OutboundOrder` | `StockExit`, etc.     | `id`, `product_id` (FK), `quantity`, `created_at`, `user_uuid` |

Rules:

- Use `SQLModel, table=True` — not raw SQLAlchemy declarative models.
- Declare FK with `Field(foreign_key="product.id")` (adjust table name to match model).
- `user_uuid` is `str`, no FK to a users table in Supabase.
- **Do not** add a stored `current_stock` column on the product table.

## Pydantic schemas (`schemas.py`)

Separate request and response schemas from ORM models:

- `ProductCreate`, `ProductRead` (with computed `current_stock`)
- `InboundOrderCreate`, `InboundOrderRead`
- `OutboundOrderCreate`, `OutboundOrderRead`
- Combined list item for `GET /inventory/orders` (order + nested product summary + `user_uuid`)

Never return a raw SQLModel instance from an endpoint — map ORM → schema explicitly.

## Inventory router (`routers/inventory.py`)

Register with `prefix="/inventory"` and include in `main.py`.

| Method | Path                         | Auth     | Description                                       |
| ------ | ---------------------------- | -------- | ------------------------------------------------- |
| `GET`  | `/inventory/products`        | Public   | List products with computed `current_stock`       |
| `POST` | `/inventory/products`        | Required | Create product (starts at zero stock)             |
| `GET`  | `/inventory/products/{id}`   | Public   | Single product with `current_stock`               |
| `POST` | `/inventory/orders/inbound`  | Required | Register inbound order; increases stock           |
| `POST` | `/inventory/orders/outbound` | Required | Register outbound order; decreases stock          |
| `GET`  | `/inventory/orders`          | Public   | List all orders with product data and `user_uuid` |

Protected routes use the existing `get_current_user` dependency from prior milestones. Persist `current_user.uuid` (or equivalent) into `user_uuid` on order creation.

## Business logic — stock calculation

`current_stock` is **always computed**, never stored:

```python
def compute_stock(session: Session, product_id: int) -> int:
    inbound = session.exec(
        select(func.coalesce(func.sum(InboundOrder.quantity), 0))
        .where(InboundOrder.product_id == product_id)
    ).one()
    outbound = session.exec(
        select(func.coalesce(func.sum(OutboundOrder.quantity), 0))
        .where(OutboundOrder.product_id == product_id)
    ).one()
    return inbound - outbound
```

When CONTEXT requires per-warehouse stock (e.g. TrackFlow), filter both sums by `warehouse` before subtracting.

### Outbound validation

Before persisting an outbound order:

1. Compute available stock for the product (and warehouse if applicable).
2. If `requested_quantity > available`, return `HTTP 400` with a descriptive message.
3. Only then insert the outbound record.

Example error:

```json
{
  "detail": "Insufficient stock for SKU 'CLT-SNK-W-42'. Available: 5, requested: 10."
}
```

### N+1 avoidance

For `GET /inventory/orders`, eager-load product data in one query (e.g. `selectinload`, joined load, or a single aggregated query) instead of fetching each product inside a loop.

## Indicative API examples

### `GET /inventory/products` (excerpt)

```json
[
  {
    "id": 1,
    "name": "Classic White Sneaker - Size 42",
    "sku": "CLT-SNK-W-42",
    "current_stock": 47
  }
]
```

### `POST /inventory/orders/inbound` (request)

```json
{
  "product_id": 1,
  "quantity": 20
}
```

### `POST /inventory/orders/outbound` — rejected (400)

```json
{
  "detail": "Insufficient stock. Available: 3, requested: 5."
}
```

### `GET /inventory/orders` (excerpt)

```json
[
  {
    "id": 1,
    "order_type": "inbound",
    "product_id": 1,
    "product_name": "Classic White Sneaker - Size 42",
    "quantity": 20,
    "user_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "created_at": "2025-06-01T10:30:00Z"
  }
]
```

## Validation checklist (reviewers)

- [ ] Two DB connections active: TinyDB for auth, Supabase/SQLModel for inventory.
- [ ] All inventory routes under `/inventory` via dedicated `APIRouter`.
- [ ] SQLModel FK: inbound/outbound `product_id` → product table.
- [ ] `current_stock` computed from orders — no direct stock mutation endpoint.
- [ ] Outbound exceeding stock returns `400` **before** any write.
- [ ] Each order stores authenticated `user_uuid` from TinyDB.
- [ ] `models.py` and `schemas.py` are separate; endpoints return Pydantic schemas only.
- [ ] `get_db` injected per request; no global session.
- [ ] Connection strings in `.env`; `.env` in `.gitignore`.
- [ ] Entity and field names match the student's CONTEXT.md.

## Key implementation decisions

- Reuse existing auth layer — do not rebuild user management in Supabase.
- Keep inventory logic in the router or a thin service module; stock calculation should be a single reusable function.
- Validate outbound stock in the same transaction boundary as the insert attempt (check-then-write, or rely on application-level guard before `session.add`).
- Document any CONTEXT-specific validation (e.g. `tracking_number` required for dispatch exits) in code and tests.
