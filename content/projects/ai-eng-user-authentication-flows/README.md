# Connecting the Lock: Authentication Flows in the Frontend

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

In the previous delivery you secured the API. Protected routes now return `401` to anyone without a valid session — including your own frontend. It's time to close that loop.

Your tech lead has opened the next ticket:

> #### AUTH-02 — Authentication flows and protected views in the frontend
>
> The API now requires a JWT token on protected routes. This task covers the frontend side of that contract:
>
> - **Login and registration views** — forms that call the API, receive the token, and store it correctly.
> - **Account management views** — profile page and password change form.
> - **Route protection** — any view that requires a session must redirect unauthenticated users to login. This applies to all applications in the monorepo **except the public website (Milestone 1)**, which remains fully public.
>
> The token must be stored in `localStorage` and attached to every protected API call via the `Authorization: Bearer` header. On logout, the token is removed and the user is redirected to login.
>
> Do not build a separate authentication app. Integrate these flows into the existing Next.js applications inside your monorepo.

### Complementary knowledge: the frontend side of JWT

Once the API returns a token at login, the frontend's job is: store it, send it, and react to its absence. The standard pattern in Next.js is:

1. **Store** the token in `localStorage` after a successful login response.
2. **Read** the token on every protected API call and set it in the `Authorization` header: `Bearer <token>`.
3. **Protect routes** — in Next.js App Router this is handled with a middleware or a layout-level check: if there is no token, redirect to `/login`.
4. **Clear** the token on logout and redirect.

> **Note:** The temporary frontend breakage from the previous delivery ends here. By the end of this project, all protected views should be working end-to-end with real authentication.

---

## 🌱 How to Start the Project

This project continues inside your existing monorepo. Work on the same branch or open a new one: `git checkout -b feature/auth-frontend`.

Make sure your API from the previous delivery is running and reachable from the frontend before you start.

---

## 💻 What You Need to Do

### Authentication views

- [ ] `/login` — email and password form. On success: store the token in `localStorage`, redirect to the main authenticated view. On failure: show a clear error message.
- [ ] `/register` — registration form. On success: store the token, redirect. On failure: show field-level validation errors.

### Account management views

- [ ] `/account/profile` — displays the current user's data (name, email). Allows editing name. Calls `PUT /users/{id}` with the token in the header.
- [ ] `/account/change-password` — form with current password, new password, and confirmation. Validates that the new password and confirmation match before calling the API.

### Route protection

- [ ] Identify every view in your Next.js applications (excluding the public website) that requires an authenticated session.
- [ ] Implement a protection mechanism — middleware, layout guard, or a custom hook — that checks for the token in `localStorage` and redirects to `/login` if it is absent or invalid.
- [ ] Ensure the public website (Milestone 1) is entirely unaffected — no token check, no redirect.

### Token lifecycle

- [ ] On login and registration: store the token in `localStorage`.
- [ ] On every protected API call: read the token and attach it as `Authorization: Bearer <token>`.
- [ ] On logout: remove the token from `localStorage` and redirect to `/login`.
- [ ] If a protected API call returns `401`: clear the token and redirect to `/login`.

---

## ✅ What We Will Evaluate

- [ ] Login and registration forms work end-to-end: the token is stored after a successful call.
- [ ] Protected views redirect to `/login` when there is no valid token in storage.
- [ ] The public website (Milestone 1) continues to work without any authentication check.
- [ ] The profile view displays and updates the current user's data using the token.
- [ ] Logout removes the token and redirects correctly.
- [ ] A `401` response from any protected API call clears the session and redirects to `/login`.

---

## 📦 How to Submit

Push your branch and open a pull request against `main` in your monorepo. The PR description should include: which views are now protected and confirmation that the public website was not affected.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
