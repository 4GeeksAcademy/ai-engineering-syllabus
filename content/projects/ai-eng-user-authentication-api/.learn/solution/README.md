# Securing the API: Authentication and Route Restriction in FastAPI - Reference Solution

## Purpose

This reference solution describes the expected architecture, implementation scope, and validation evidence for a complete submission.

## Solution Structure

- `app/models/` for persistence models and schema contracts (`User`, `Profile`).
- `app/services/` for business logic and route-independent operations.
- `app/routes/` (or equivalent) for API endpoint definitions.
- `app/core/security.py` (or equivalent) for JWT, password hashing, and auth dependencies.
- `database.py` (or equivalent) for the TinyDB client used by auth models.
- `tests/` for route, service, and auth behavior tests.

## Required Coverage (From README)

- Create a `User` model in **TinyDB** with at least: `id`, `email`, `hashed_password`, `is_active`, `role`, `created_at`. Do not store display name or contact fields on `User`.
- The `role` field accepts only `admin`, `manager`, or `user`. New registrations via `POST /users` default to `user`.
- Create a `Profile` model in **TinyDB**, linked one-to-one to `User` via `user_id`, with at least: `id`, `user_id`, `name`, `phone`, `address`.
- Implement a service layer with functions for user CRUD and profile read/update.
- Expose user services as REST endpoints under `/users`. `POST /users` creates the user and linked profile; `PUT /users/{id}` updates credential fields only.
- Expose profile routes under `/profiles`: `GET /profiles/me`, `PUT /profiles/me`.
- Implement `POST /auth/login` — accepts `email` and `password`, validates credentials, returns a JWT access token.
- Implement `GET /auth/me` (protected) — returns authenticated user email, role, plus linked profile data.
- Apply `get_current_user` to all `/users` endpoints except `POST /users`, to `/auth/me`, to `/profiles/*`, and to at least 5 other existing monorepo routes outside `/users`, `/auth`, and `/profiles`.
- Create a `get_current_user` dependency that: extracts the `Authorization: Bearer <token>` header, decodes and validates the JWT, retrieves the user from TinyDB, and raises `HTTPException(401)` if anything fails.
- Set token expiry via an environment variable (e.g. `ACCESS_TOKEN_EXPIRE_MINUTES`). Store the signing secret in `.env` — never hardcode it.

## Expected API Surface

- `POST /users`
- `GET /users`
- `GET /users/{id}`
- `PUT /users/{id}`
- `DELETE /users/{id}`
- `GET /profiles/me`
- `PUT /profiles/me`
- `POST /auth/login`
- `GET /auth/me`

## Key Implementation Decisions

- `User` and `Profile` live in **TinyDB only** — not Supabase. This does not change when Supabase is added for inventory (Milestone 5): never migrate auth models to PostgreSQL or create a SQLModel user table. JWT carries TinyDB user `id` for `user_uuid` references elsewhere.
- Passwords are never stored in plain text; use `passlib` with `bcrypt`.
- JWT creation/validation is centralized in one security module.
- `get_current_user` is used as a reusable dependency on protected routes.
- Secret keys and token TTL come from environment variables.
- Unauthorized access returns `401`; forbidden ownership actions return `403`.

## Indicative Examples

### Example: Login success response

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Example: GET /auth/me response

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "role": "user",
  "profile": {
    "name": "Alex Rivera",
    "phone": "+1 555 0100",
    "address": "123 Main St"
  }
}
```

### Example: Accessing a protected route without token

```json
{
  "detail": "Not authenticated"
}
```

## Validation Notes

- Verify register via `POST /users` → login → `GET /auth/me` → `PUT /profiles/me` in `/docs`.
- Confirm `name`, `phone`, and `address` are stored on `Profile`, not on `User`.
- Validate invalid, malformed, and expired token scenarios.
- Confirm protected and public routes behavior matches the rubric.
- Ensure the final output remains aligned with all project evaluation criteria.
