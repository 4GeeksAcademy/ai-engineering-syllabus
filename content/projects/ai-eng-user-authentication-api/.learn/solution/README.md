# Securing the API: Authentication and Route Restriction in FastAPI - Reference Solution

## Purpose

This reference solution describes the expected architecture, implementation scope, and validation evidence for a complete submission.

## Solution Structure

- `app/models/` for persistence models and schema contracts.
- `app/services/` for business logic and route-independent operations.
- `app/routes/` (or equivalent) for API endpoint definitions.
- `app/core/security.py` (or equivalent) for JWT, password hashing, and auth dependencies.
- `tests/` for route, service, and auth behavior tests.

## Required Coverage (From README)

- Create a `User` model in the database with at least: `id`, `email`, `hashed_password`, `is_active`, `created_at`.
- Implement a service layer with functions for: create user, get user by ID, get user by email, update user, delete user.
- Expose those services as REST endpoints under `/users`:
- Implement `POST /auth/login` — accepts `email` and `password`, validates credentials, returns a JWT access token.
- Implement `POST /auth/register` — creates a new user and returns a token so the caller is logged in immediately.
- Implement `GET /auth/me` (protected) — returns the profile of the currently authenticated user.
- Create a `get_current_user` dependency that: extracts the `Authorization: Bearer <token>` header, decodes and validates the JWT, retrieves the user from the database, and raises `HTTPException(401)` if anything fails.
- Set token expiry via an environment variable (e.g. `ACCESS_TOKEN_EXPIRE_MINUTES`). Store the signing secret in `.env` — never hardcode it.

## Expected API Surface

- `POST /users`
- `GET /users`
- `GET /users/{id}`
- `PUT /users/{id}`
- `DELETE /users/{id}`
- `POST /auth/login`
- `POST /auth/register`
- `GET /auth/me`

## Key Implementation Decisions

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

### Example: Accessing a protected route without token

```json
{
  "detail": "Not authenticated"
}
```

### Example: Ownership violation

```json
{
  "detail": "Forbidden"
}
```

## Validation Notes

- Verify register -> login -> authenticated request flow in `/docs`.
- Validate invalid, malformed, and expired token scenarios.
- Confirm protected and public routes behavior matches the rubric.
- Ensure the final output remains aligned with all project evaluation criteria.
