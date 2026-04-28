# The Missing Piece: Password Reset Flow

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

The authentication system is working. Users can register, log in, manage their profile, and change their password — as long as they remember it.

But what happens when they don't?

Right now, a user who forgets their password has no way to recover their account. And beyond that: in any production system, periodically changing passwords is a basic security practice. Your platform has no mechanism for either.

Your tech lead has opened the ticket:

> #### AUTH-03 — Password reset flow
>
> The platform needs a full password reset mechanism. This covers both the API and the frontend:
>
> **Backend:**
> - `POST /auth/forgot-password` — receives an email, validates the user exists, generates a signed short-lived reset token, and sends a reset link to the user's email address.
> - `POST /auth/reset-password` — receives the reset token and a new password, validates the token (signature + expiry), hashes the new password, and updates the user record. The token must be invalidated after use.
>
> **Frontend:**
> - `/forgot-password` — form where the user enters their email. Always shows a confirmation message after submission, regardless of whether the address exists, to prevent user enumeration.
> - `/reset-password` — form where the user sets a new password. Reads the reset token from the URL query string and submits it to the API alongside the new password. On success, redirects to `/login`.
>
> For email delivery, choose one of the following services and integrate it:
> - [Mailgun](https://www.mailgun.com/)
> - [MailerSend](https://www.mailersend.com/)
> - [SendGrid (Twilio)](https://www.twilio.com/en-us/sendgrid)
>
> All three offer a free tier sufficient for development. API keys must be stored in environment variables — never hardcoded.

### Complementary knowledge: how a password reset flow works

The flow has three steps and two separate moments in time:

1. **Request** — the user submits their email. The server generates a reset token (a signed JWT or a random string stored in the database), builds a reset URL containing that token (`/reset-password?token=<token>`), and sends it to the user's email via a transactional email service.

2. **Reset** — the user clicks the link, lands on the `/reset-password` page, enters a new password, and submits. The frontend sends the token (read from the URL) and the new password to the API. The server validates the token — if the signature is valid and it hasn't expired — updates the password, and invalidates the token so it can't be reused.

3. **Confirmation** — the user is redirected to `/login` and can sign in with the new password.

**Why always show a confirmation message?** If the form shows "email not found" for addresses that don't exist, an attacker can use that to enumerate which emails are registered. Always responding with "if that address is in our system, you'll receive a link" prevents this.

**Token expiry matters.** A reset token should have a short lifespan — 15 to 60 minutes is standard. After it's used or after it expires, it should be unusable. If you use a JWT, encode the expiry in the payload. If you use a random string stored in the database, store the expiry timestamp alongside it.

---

## 🌱 How to Start the Project

This project continues inside your existing monorepo. Open a new branch: `git checkout -b feature/password-reset`.

Before you start, sign up for one of the email services listed above and obtain an API key. Store it in your `.env` file. Make sure `.env` is in your `.gitignore` — never commit API keys.

---

## 💻 What You Need to Do

### Backend

- [ ] `POST /auth/forgot-password` — accepts `{ email }`. If the user exists, generate a reset token with a short expiry (15–60 minutes) and send an email containing the reset link. Always return a `200` response regardless of whether the email was found.
- [ ] `POST /auth/reset-password` — accepts `{ token, new_password }`. Validate the token (signature and expiry). If valid, hash the new password, update the user record, and invalidate the token. Return `400` for invalid or expired tokens.
- [ ] Integrate one transactional email service (Mailgun, MailerSend, or SendGrid) to send the reset email. The email must include the reset link and be readable on mobile.
- [ ] Store the email service API key in an environment variable. Document which variable name to set in your `README` or `.env.example`.

### Frontend

- [ ] `/forgot-password` — email input form. On submit, call `POST /auth/forgot-password` and display a confirmation message ("If that address is registered, you'll receive a link shortly"). The form should be disabled after submission to prevent duplicate requests.
- [ ] `/reset-password` — new password form with a confirmation field. Read the `token` from the URL query string. On submit, call `POST /auth/reset-password`. On success, redirect to `/login` with a success message. On failure (expired or invalid token), show a clear error and a link back to `/forgot-password`.
- [ ] Add a "Forgot your password?" link on the `/login` page pointing to `/forgot-password`.

### Security

- [ ] Reset tokens must expire and be invalidated after use — a token cannot be used twice.
- [ ] The `/forgot-password` endpoint must always return `200`, never reveal whether an email is registered.
- [ ] API keys must never appear in the codebase — use environment variables exclusively.

---

## 🚀 Going Further (optional)

These are not evaluated but are valid extensions if time allows:

- **HTML email template** — send a styled email instead of a plain-text link.
- **Rate limiting** — limit the number of reset requests per email address per hour to prevent abuse.
- **Audit log** — record each password reset event (timestamp, IP address) in the database.

---

## ✅ What We Will Evaluate

- [ ] `POST /auth/forgot-password` sends a real email containing the reset link when called with a registered address.
- [ ] `POST /auth/forgot-password` returns `200` even when the address is not registered — no information is leaked.
- [ ] The reset token expires after the configured window and cannot be used after expiry.
- [ ] `POST /auth/reset-password` updates the password and invalidates the token on success.
- [ ] `POST /auth/reset-password` returns `400` for expired or already-used tokens.
- [ ] `/forgot-password` shows a confirmation message after submission regardless of the result.
- [ ] `/reset-password` reads the token from the URL, submits the form, and redirects to `/login` on success.
- [ ] `/reset-password` shows a clear error with a link back to `/forgot-password` when the token is invalid or expired.
- [ ] The `/login` page has a visible "Forgot your password?" link.
- [ ] No API keys are hardcoded — all secrets are loaded from environment variables.

---

## 📦 How to Submit

Push your branch and open a pull request against `main` in your monorepo. The PR description should include: which email service you chose, the environment variable name required to run the feature, and confirmation that you tested the full flow end-to-end.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
