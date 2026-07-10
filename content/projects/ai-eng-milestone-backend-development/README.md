# Milestone 5 — Backend: Inventory Management with ORM & Dual Database

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/05-backend-development)** before writing any code — it defines the specific company entities, field names, and business constraints for your implementation.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You've already built the API and the authentication layer. Now the operations team has submitted an **RFP** to the technology unit: the company needs a centralised inventory management system, and it must be live before the next operational review.

Your tech lead has translated that RFP into an architectural decision that shapes everything you build here: **authentication stays in TinyDB** (fast, local, document-based lookups), and **all business data — products, inbound orders, and outbound orders — moves to Supabase** (a hosted PostgreSQL database). Your FastAPI application will maintain two simultaneous database connections and must use each one deliberately: every request reaches the right store.

This is not just a persistence exercise. The operations team embedded a non-negotiable constraint in the **brief**:

> _"Stock levels cannot be modified directly. The only way to change inventory is by registering an order — either an inbound order that adds stock, or an outbound order that removes it. Every order must be traceable to the user who created it."_

Your job is to enforce that rule at the API and model level, using an ORM to translate Python classes into relational tables in Supabase. All inventory endpoints must be grouped under the `/inventory` router prefix.

### What is an ORM — and why does it matter here?

An ORM (Object-Relational Mapper) is a translation layer: a Python class becomes a table, an instance becomes a row, and an attribute becomes a column. It does not replace knowing SQL — understanding what the ORM generates under the hood is what lets you use it correctly and debug it when something breaks. In this milestone you will use **SQLModel**, which combines SQLAlchemy's ORM engine with Pydantic's type system. Do not use raw SQLAlchemy directly.

One pattern you must be aware of before writing any query: the **N+1 problem**. If you load a list of orders and then access each order's product data inside a loop, you generate one additional query per element — degrading performance silently. Structure your queries to load related data upfront, not on access.

### Brief from your tech lead

> > **From:** Tech Lead
> > **Subject:** Milestone 5 — dual database architecture + inventory ORM
> >
> > The **PRD** is ready. Here is what the system must do:
> >
> > 1. The FastAPI app connects to **two databases simultaneously**: TinyDB (existing, for users and auth) and Supabase (new, for inventory and orders).
> > 2. Products and stock quantities live in Supabase. Stock **must not be a directly editable column** — it is always derived from the order history.
> > 3. **Inbound orders** increase stock; **outbound orders** decrease it. Both are stored in Supabase and reference the user UUID from TinyDB — no user table is replicated in Supabase.
> > 4. ORM models use **SQLModel**. Pydantic schemas for request and response are in a separate file from ORM models — never return a raw ORM object from an endpoint.
> > 5. All inventory routes must be registered under the `/inventory` prefix using a dedicated `APIRouter`.
> > 6. Check your CONTEXT.md — entity names, field constraints, and business rules are company-specific.
> >
> > **Acceptance criteria**: all endpoints functional under `/inventory`, FK relationships enforced at database level, no direct stock mutation, both DB connections active and correctly used.

---

## 🌱 How to Start the Project

This milestone extends the FastAPI service already present in your monorepo. You will not create a new service — you will add the inventory layer to it.

1. Open your existing repository (forked from `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo`).
2. Navigate to `services/` — this is where your FastAPI application lives.
3. Install new dependencies:

   ```bash
   uv add sqlmodel psycopg2-binary
   ```

4. Add your Supabase connection string to `.env`. Your TinyDB configuration is already there — do not change it.
5. Read your **CONTEXT-company.md** before defining any model — entity names and field constraints are specified there.

### Supabase Connection Settings

In the Supabase dashboard (**Connect → Direct**), use **Transaction pooler** as the connection method and **URI** as the type — then copy that string into `DATABASE_URL`.

![Supabase connection settings: Transaction pooler method and URI type](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-backend-development/.learn/supabase-transaction-pooler-uri.png)

![Supabase connection string: Transaction pooler URI details](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-backend-development/.learn/supabase-transaction-pooler-connection-string.png)

---

## 💻 What You Need to Do

### Database configuration

- [ ] Add the Supabase PostgreSQL connection string to `.env`. Never hardcode credentials.
- [ ] In `database.py` (or equivalent), initialise **both** database connections: the existing TinyDB client and a new SQLModel engine pointing to Supabase.
- [ ] Create a `get_db` dependency that yields a SQLModel session per request via `Depends()`. No global session variable.

### ORM models — `models.py`

- [ ] Define a `Product` model using `SQLModel, table=True`, with at minimum: `id`, `name`, `sku`, and any company-specific fields from your CONTEXT.md.
- [ ] Define an `InboundOrder` model with: `id`, `product_id` (FK → Product), `quantity`, `created_at`, and `user_uuid` (string — references the TinyDB user; no FK, no user table replication).
- [ ] Define an `OutboundOrder` model with: `id`, `product_id` (FK → Product), `quantity`, `created_at`, and `user_uuid`.
- [ ] Call `SQLModel.metadata.create_all(engine)` on application startup to initialise the schema in Supabase.

  > ⚠️ `create_all()` is acceptable for development and learning contexts. In a production system, schema changes are always managed through migration files (e.g., Alembic) that keep a versioned history of every change. Never use `create_all()` against a shared or production database.

### Pydantic schemas — `schemas.py`

- [ ] Define request and response schemas for Product, InboundOrder, and OutboundOrder as standalone Pydantic models — separate from the ORM models.
- [ ] The Product response schema must include a `current_stock` field (computed, not stored).
- [ ] ORM models and Pydantic schemas must live in **separate files**. They are different classes, even if some fields overlap.

### Inventory router — `routers/inventory.py`

- [ ] Create a dedicated `APIRouter` with `prefix="/inventory"` and register it in the main FastAPI app.
- [ ] Implement the following endpoints inside this router:

| Method | Path                         | Description                                       |
| ------ | ---------------------------- | ------------------------------------------------- |
| `GET`  | `/inventory/products`        | List all products with computed `current_stock`   |
| `POST` | `/inventory/products`        | Create a product (requires auth)                  |
| `GET`  | `/inventory/products/{id}`   | Get a single product with its current stock       |
| `POST` | `/inventory/orders/inbound`  | Register an inbound order (requires auth)         |
| `POST` | `/inventory/orders/outbound` | Register an outbound order (requires auth)        |
| `GET`  | `/inventory/orders`          | List all orders with product data and `user_uuid` |

### Business rules

- [ ] `current_stock` is always computed as `SUM(inbound quantities) − SUM(outbound quantities)` for each product. It is never stored as a column that can be set directly.
- [ ] A product starts with zero stock at creation and can only accumulate stock through inbound orders.
- [ ] Every order creation endpoint requires authentication. The authenticated user's UUID (from TinyDB) must be stored in the order's `user_uuid` field.
- [ ] An outbound order that would result in negative stock must be rejected **before the order is persisted**, returning `HTTP 400` with a descriptive error message.

⚠️ **IMPORTANT:** Entity names, field names, and domain-specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] Two database connections are demonstrably present and used correctly: TinyDB for auth and user lookups; Supabase (SQLModel) for all inventory entities.
- [ ] All inventory endpoints are grouped under `/inventory` via a dedicated `APIRouter`.
- [ ] SQLModel ORM models correctly declare FK relationships: `InboundOrder.product_id` and `OutboundOrder.product_id` reference the `Product` table.
- [ ] `current_stock` is computed from orders — no endpoint allows direct modification of a stock field on the Product.
- [ ] An outbound order that exceeds available stock is rejected with `HTTP 400` before any write occurs.
- [ ] Every order stores the `user_uuid` of the authenticated creator (sourced from TinyDB).
- [ ] ORM models (`models.py`) and Pydantic schemas (`schemas.py`) are in separate files and are structurally different — no endpoint returns a raw SQLModel object.
- [ ] The SQLModel session is injected per request via `Depends()` — no global session exists in the codebase.
- [ ] All connection parameters live in `.env`; `.env` is listed in `.gitignore`.
- [ ] Entity names and field names match the student's CONTEXT.md specification.

---

## 📦 How to Submit

1. Commit and push all changes to your fork.
2. Confirm `.env` is in `.gitignore` — never commit credentials.
3. Submit the URL of your fork via the student platform.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
