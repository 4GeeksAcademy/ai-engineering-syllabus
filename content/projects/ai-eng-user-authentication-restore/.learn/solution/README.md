# The Missing Piece: Password Reset Flow - Reference Solution

## Purpose

This reference solution describes the expected architecture, implementation scope, and validation evidence for a complete submission.

## Solution Structure

- `app/models/` for persistence models and schema contracts.
- `app/services/` for business logic and route-independent operations.
- `app/routes/` (or equivalent) for API endpoint definitions.
- `app/core/security.py` (or equivalent) for JWT, password hashing, and auth dependencies.
- `tests/` for route, service, and auth behavior tests.

## Required Coverage (From README)

- `POST /auth/forgot-password` — accepts `{ email }`. If the user exists, generate a reset token with a short expiry (15–60 minutes) and send an email containing the reset link. Always return a `200` response regardless of whether the email was found.
- `POST /auth/reset-password` — accepts `{ token, new_password }`. Validate the token (signature and expiry). If valid, hash the new password, update the user record, and invalidate the token. Return `400` for invalid or expired tokens.
- Integrate one transactional email service (Mailgun, MailerSend, or SendGrid) to send the reset email. The email must include the reset link and be readable on mobile.
- Store the email service API key in an environment variable. Document which variable name to set in your `README` or `.env.example`.
- `/forgot-password` — email input form. On submit, call `POST /auth/forgot-password` and display a confirmation message ("If that address is registered, you'll receive a link shortly"). The form should be disabled after submission to prevent duplicate requests.
- `/reset-password` — new password form with a confirmation field. Read the `token` from the URL query string. On submit, call `POST /auth/reset-password`. On success, redirect to `/login` with a success message. On failure (expired or invalid token), show a clear error and a link back to `/forgot-password`.
- Add a "Forgot your password?" link on the `/login` page pointing to `/forgot-password`.
- Reset tokens must expire and be invalidated after use — a token cannot be used twice.

## Expected API Surface

- `POST /auth/forgot-password`
- `POST /auth/reset-password`

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
