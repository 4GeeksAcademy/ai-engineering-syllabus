# Platform – Audit Log - Reference Solution

## Purpose

This reference solution describes the expected architecture, implementation scope, and validation evidence for a complete submission.

## Solution Structure

- `app/models/` for persistence models and schema contracts.
- `app/services/` for business logic and route-independent operations.
- `app/routes/` (or equivalent) for API endpoint definitions.
- `app/core/security.py` (or equivalent) for JWT, password hashing, and auth dependencies.
- `tests/` for route, service, and auth behavior tests.

## Required Coverage (From README)

- Design a dedicated append-only table or collection for the audit log, separate from the system's operational tables
- Each entry includes at minimum: actor (user or process), action performed, affected resource, timestamp, and origin (IP or process identifier)
- Implement a mechanism that makes any later alteration of an already-written entry evident (e.g., hash chaining)
- Guarantee, at the database or application level, that there's no `UPDATE` or `DELETE` path onto this table from the application
- Instrument audit capture on the sensitive actions identified in your initial inventory
- Log actions executed by automated processes or agents, clearly distinguishing them from human actions
- Log relevant authentication events (successful login, failed login, permission changes) if your system already has those flows
- Implement a backoffice view to query the log, with filters by actor, action type, resource, and date range

## Expected API Surface

- Implement and validate the required routes from the README.

## Key Implementation Decisions

- Passwords are never stored in plain text; use `libpass` with `bcrypt`.
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
