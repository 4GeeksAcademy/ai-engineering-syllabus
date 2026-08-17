# Makerspace Tool Desk — Roles vs Departments (Class Example)

> **For instructors:** Not the student project. Live demo of the same spine as `ai-eng-roles-permissions`: two independent axes (role = capability, department = data scope), one FastAPI permission dependency, explicit **403**, Admin-only admin view. Domain is a campus makerspace so students do not copy the company story.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

A campus makerspace API treats every logged-in member the same. Legal (the faculty advisor) wants **two mechanisms**, not one table: **role** (what you can do) and **shop** (which tools/notes you see). A Woodshop Lab Lead and an Electronics Lab Lead have the same lead powers — they must not see each other's incident notes.

### Scope note

One session. Three roles, two shops, one scoped collection (`shop-notes`), centralized `require_role` + `require_shop_scope`. Drop full monorepo mapping, seed of 5+ company users, and a polished Admin UI — a single Admin page or `/docs` is enough. Students still follow the full brief in the project root `README.md`.

---

## What to build

### Model

- [ ] `Role`: `maker` (rank 1), `lab_lead` (rank 2), `admin` (rank 3)
- [ ] `Shop` (department axis): `woodshop`, `electronics` — independent from role
- [ ] `User.role_id` and `User.shop_id` as separate FKs
- [ ] `ShopNote`: `id`, `shop_id`, `title`, `body`

### Centralized checks

- [ ] `require_role(*codes_or_min_rank)` dependency — insufficient role → **403**
- [ ] `require_shop_scope` — `GET` other shop's note by id → **403** (not empty 200)
- [ ] Routes declare dependencies; no copied `if user.role == ...` in handlers

### API (minimum)

| Method   | Path                     | Who                                          |
| -------- | ------------------------ | -------------------------------------------- |
| `GET`    | `/shop-notes`            | maker+: own shop (admin: all)                |
| `GET`    | `/shop-notes/{id}`       | own shop or admin; else 403                  |
| `PUT`    | `/shop-notes/{id}`       | lab_lead+ own shop; admin any                |
| `DELETE` | `/shop-notes/{id}`       | admin                                        |
| `GET`    | `/roles`                 | admin only → 403 otherwise                   |
| `PATCH`  | `/users/{id}/assignment` | admin; change role **or** shop independently |

### UI (thin)

- [ ] Hide delete for non-admin
- [ ] List shows only own shop notes
- [ ] Admin can open roles/shops assignment (others 403)

---

## Verify together

- [ ] Maker `PUT` a note → **403**
- [ ] Woodshop lab lead `GET` electronics note by id → **403**
- [ ] `PATCH` only `shop_id` → role unchanged
- [ ] `GET /roles` as lab lead → **403**

---

## Discussion questions

1. Why is returning `200 []` for a forbidden action worse than **403** when Legal audits the API?
2. If Admin can see every shop, did we mix the two axes — or is cross-shop visibility a **role** capability?
3. Where should the rank comparison live so a fourth role does not fork every endpoint?
