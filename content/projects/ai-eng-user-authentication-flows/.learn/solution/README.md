# Connecting the Lock: Authentication Flows in the Frontend - Reference Solution

## Purpose

This reference solution describes the expected architecture, implementation scope, and validation evidence for a complete submission.

## Solution Structure

- `app/models/` for persistence models and schema contracts.
- `app/services/` for business logic and route-independent operations.
- `app/routes/` (or equivalent) for API endpoint definitions.
- `app/core/security.py` (or equivalent) for JWT, password hashing, and auth dependencies.
- `tests/` for route, service, and auth behavior tests.

## Required Coverage (From README)

- `/login` — email and password form. On success: store the token in `localStorage`, redirect to the main authenticated view. On failure: show a clear error message.
- `/register` — registration form. On success: call `POST /users` then `POST /auth/login`, store the token, redirect. On failure: show field-level validation errors.
- `/account/profile` — displays email plus profile data from `GET /auth/me`. Allows editing name and contact via `PUT /profiles/me` with the token in the header.
- Identify every view in your Next.js applications (excluding the public website) that requires an authenticated session.
- Implement a protection mechanism — middleware, layout guard, or a custom hook — that checks for the token in `localStorage` and redirects to `/login` if it is absent or invalid.
- Ensure the public website (Milestone 1) is entirely unaffected — no token check, no redirect.
- On login and registration: store the token in `localStorage`.

## Expected API Surface

- `PUT /profiles/me`

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
