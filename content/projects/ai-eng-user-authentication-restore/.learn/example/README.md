# In-Class Example — Password Reset for a Pet Health Tracker

> **Instructor note:** This is a classroom-paced example to introduce the same concepts as the graded project (password reset flow). Use a different domain so students don't confuse it with their own work. A pet health tracker is concrete and personal — users care about their account, which makes the "forgot my password" scenario feel real. The goal is to work through the full reset flow together: backend endpoints, transactional email, and frontend pages.

---

## The Scenario

**PawLog** is an app where pet owners log their animals' vaccinations, vet visits, and medications. The auth system (register, login, profile) is already working. The missing piece: users who forget their password have no way to recover their account.

Today we build the full password reset flow — API endpoints + frontend pages + one transactional email.

---

## How the Flow Works

```
1. /forgot-password  →  POST /auth/forgot-password { email }
                    ←  200 OK (always, even if email not found)
                    →  Email sent with link: /reset-password?token=<token>

2. User clicks link → /reset-password?token=<token>
                    →  POST /auth/reset-password { token, new_password }
                    ←  200 OK → redirect to /login
                    ←  400 Bad Request (expired or already used) → show error

3. /login  ← user signs in with new password
```

---

## Backend

### `POST /auth/forgot-password`

- [ ] Accept `{ email }` in the request body.
- [ ] If the user exists: generate a short-lived reset token (JWT with a 30-minute expiry is fine for class, or a random string stored in a `reset_tokens` table).
- [ ] Send an email with the reset link: `http://localhost:3000/reset-password?token=<token>`.
- [ ] **Always return `200`** — never reveal whether the email is registered.

```python
# Example payload for a JWT reset token
{
  "sub": user.id,
  "type": "password_reset",
  "exp": datetime.utcnow() + timedelta(minutes=30)
}
```

### `POST /auth/reset-password`

- [ ] Accept `{ token, new_password }`.
- [ ] Validate the token: check signature and expiry.
- [ ] If valid: hash the new password, update the user record, invalidate the token (mark as used if stored in DB, or rely on expiry for JWT).
- [ ] Return `200` on success.
- [ ] Return `400` for invalid, expired, or already-used tokens.

### Email integration

Choose one free-tier service:

| Service | Free tier |
|---|---|
| [MailerSend](https://www.mailersend.com/) | 3,000 emails/month |
| [Mailgun](https://www.mailgun.com/) | 100 emails/day |
| [SendGrid](https://sendgrid.com/) | 100 emails/day |

- [ ] Store the API key in `.env` (e.g. `MAILERSEND_API_KEY`). Never hardcode it.
- [ ] The email must contain the reset link and be readable on mobile. A plain-text body is fine for class.

---

## Frontend

### `/forgot-password`

- [ ] Email input form.
- [ ] On submit: call `POST /auth/forgot-password`.
- [ ] **Always show this confirmation message** (regardless of whether the email exists):
  > "If that address is in our system, you'll receive a reset link shortly."
- [ ] Disable the form after submission to prevent duplicate requests.
- [ ] Link back to `/login`.

### `/reset-password`

- [ ] Read the `token` from the URL query string: `new URLSearchParams(window.location.search).get('token')`.
- [ ] Show a new password field and a confirmation field.
- [ ] On submit: call `POST /auth/reset-password` with `{ token, new_password }`.
- [ ] On success: redirect to `/login` with a success message (e.g. via a query param or `localStorage` toast).
- [ ] On failure (400 from API): show *"This link has expired or has already been used. [Request a new one](/forgot-password)."*

### `/login` update

- [ ] Add a **"Forgot your password?"** link pointing to `/forgot-password`.

---

## Security Checklist

- [ ] The `/forgot-password` endpoint returns `200` even for unregistered emails.
- [ ] Reset tokens expire (15–60 minutes).
- [ ] A used token cannot be reused — it must be invalidated after a successful reset.
- [ ] No API keys are in the source code — only in `.env`.

---

## Key Concepts to Discuss in Class

| Concept | Where it appears |
|---|---|
| Signed short-lived token for reset | JWT with `"type": "password_reset"` claim |
| User enumeration prevention | Always returning `200` from forgot-password |
| Token invalidation after use | DB flag or JWT-only expiry trade-offs |
| Transactional email integration | API key in `.env`, HTTP call to email service |
| Reading query params in Next.js | `useSearchParams()` or `URLSearchParams` |
| Disable form after submit | Prevent duplicate reset requests |

---

## Discussion Questions

1. Why do we always return `200` from `/forgot-password`, even if the email is not found? What attack does this prevent?
2. We're using a short-lived JWT as the reset token. What is the advantage of this over storing a random string in the database? What is the disadvantage?
3. A user requests a reset link, then requests another one before the first expires. Should the first link still work? How would you design the system to handle this?
