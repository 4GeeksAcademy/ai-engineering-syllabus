# In-Class Example — Securing a Plant Swap API

> **Instructor note:** This is a classroom-paced example to introduce the same concepts as the graded project (user authentication API). Use a different domain so students don't confuse it with their own work. A community plant swap platform is concrete and low-stakes — good for live coding. The goal is to work through the JWT + FastAPI pattern together, not to finish a production app.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.

A small community has a FastAPI backend for listing and claiming plants that members want to swap. Right now any request — including creating, editing, and deleting listings — is fully public. Before the next version goes live, the maintainer needs the API secured: only authenticated members can post or manage listings.

---

## Tech Stack

| Layer        | Tool                                     |
| ------------ | ---------------------------------------- |
| Framework    | FastAPI                                  |
| Auth         | JWT (`python-jose`) + bcrypt (`passlib`) |
| Token scheme | `OAuth2PasswordBearer`                   |
| Database     | TinyDB (auth models only)                |
| Config       | `.env` + `python-dotenv`                 |

Install the auth dependencies:

```bash
uv add "python-jose[cryptography]" "passlib[bcrypt]"
```

---

## Data Model

### User table (TinyDB)

| Column            | Type     | Notes                                         |
| ----------------- | -------- | --------------------------------------------- |
| `id`              | str/uuid | primary key                                   |
| `email`           | str      | unique, required                              |
| `hashed_password` | str      | never store plain text                        |
| `is_active`       | bool     | default `True`                                |
| `role`            | str      | `admin`, `manager`, or `user`; default `user` |
| `created_at`      | datetime | auto                                          |

### Profile table (TinyDB)

| Column    | Type | Notes                            |
| --------- | ---- | -------------------------------- |
| `id`      | str  | primary key                      |
| `user_id` | str  | one-to-one link to `User.id`     |
| `name`    | str  | display name — **not** on `User` |
| `phone`   | str  | contact data                     |
| `address` | str  | contact data                     |

---

## What to Build

### User CRUD (`/users`)

- [ ] `POST /users` — register a new user and create the linked profile. Hash the password with `bcrypt` before saving. **Public** (no token required).
- [ ] `GET /users` — list all users. **Protected**.
- [ ] `GET /users/{id}` — get one user. **Protected**.
- [ ] `PUT /users/{id}` — update credential fields such as email. **Protected** — only the user themselves.
- [ ] `DELETE /users/{id}` — delete a user and linked profile. **Protected** — only the user themselves.

### Profile endpoints (`/profiles`)

- [ ] `GET /profiles/me` — return the authenticated member's profile. **Protected**.
- [ ] `PUT /profiles/me` — update `name`, `phone`, and `address`. **Protected**.

### Auth endpoints (`/auth`)

- [ ] `POST /auth/login` — accepts `email` + `password`. Validate credentials; if correct, return a signed JWT access token.
- [ ] `GET /auth/me` — returns email plus linked profile data. **Protected**.

### Token and dependency

- [ ] Create a `get_current_user` dependency that:
  1. Reads the `Authorization: Bearer <token>` header.
  2. Decodes and validates the JWT (signature + expiry).
  3. Retrieves the user from the database.
  4. Raises `HTTPException(401)` if anything is wrong.
- [ ] Store the JWT signing secret in `.env` as `SECRET_KEY`. Never hardcode it.
- [ ] Store token expiry in `.env` as `ACCESS_TOKEN_EXPIRE_MINUTES`.

### Route protection

- [ ] Apply `get_current_user` as a `Depends(...)` argument to every route that should not be public.
- [ ] Return `401 Unauthorized` for missing or invalid tokens.
- [ ] Return `403 Forbidden` when a valid user tries to modify another user's record.

---

## Mental Model: How JWT Works in FastAPI

```
1. Client → POST /auth/login  { email, password }
2. Server validates password hash → signs JWT → returns token
3. Client stores token

4. Client → GET /auth/me
   Headers: Authorization: Bearer <token>
5. get_current_user dependency decodes JWT → retrieves user → passes to route
6. Route returns user data

7. Client → GET /auth/me (token expired or missing)
   Server → 401 Unauthorized
```

---

## Manual Verification Checklist

Work through these steps in the FastAPI `/docs` UI:

- [ ] Register a new user → confirm password is not visible in the response.
- [ ] Login → copy the returned token.
- [ ] Click "Authorize" in `/docs`, paste the token → call `GET /auth/me` → see your profile.
- [ ] Call `GET /users` **without** a token → confirm you get `401`.
- [ ] Wait for the token to expire (or manually set a 1-minute expiry for class) → call a protected route → confirm `401`.

---

## Key Concepts to Discuss in Class

| Concept                                  | Where it appears                             |
| ---------------------------------------- | -------------------------------------------- |
| Password hashing                         | `passlib.hash.bcrypt.hash()` on registration |
| JWT structure (header.payload.signature) | `python-jose` token creation                 |
| `OAuth2PasswordBearer`                   | Token extraction from `Authorization` header |
| FastAPI `Depends()`                      | `get_current_user` injected into routes      |
| Environment variables for secrets        | `SECRET_KEY` in `.env`                       |
| `401` vs `403`                           | Missing token vs. wrong user                 |

---

## Discussion Questions

1. Why do we hash passwords instead of encrypting them? What is the practical difference when a database is breached?
2. The `get_current_user` dependency raises a `401` if the token is expired. Should the client be able to renew the token automatically, and how would a refresh token pattern work?
3. Right now, `GET /users` returns all users to any authenticated user. Is that appropriate? What would you change if you wanted only admins to see the full list?
