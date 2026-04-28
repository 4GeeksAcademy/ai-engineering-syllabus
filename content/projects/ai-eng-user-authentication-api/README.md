# Securing the API: Authentication and Route Restriction in FastAPI

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/fastapi-auth/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

Your company's API is growing. You've built endpoints that serve data to the frontend, query the database, and process records — but right now, anyone who knows a URL can call any of them. Before the platform goes into its next phase, the CTO has made it clear: **no route that modifies or exposes sensitive data should be reachable without a valid session.**

Your tech lead has just dropped a ticket in your queue:

> #### AUTH-01 — Implement authentication and route protection
>
> The API currently has no authentication layer. This task covers:
>
> - A `users` module with full CRUD (create, read, update, delete).
> - A login endpoint that validates credentials and returns a signed JWT token.
> - A reusable `get_current_user` dependency that decodes the token and identifies the caller.
> - Application of that dependency to all routes that should not be publicly accessible.
>
> Use `OAuth2PasswordBearer` from FastAPI and `python-jose` for token signing. Passwords must be hashed — never stored or compared in plain text. The token should carry the user's ID at minimum and expire after a configurable window.
>
> All auth-related routes must live under `/auth`. User management routes under `/users`.

This is a security concern, not a feature: the work you do here protects everything that was built before it and everything that comes after. Do it right.

> **Note:** Once you protect your routes, some frontend calls may stop working temporarily — that's expected. The frontend will be updated to send the token in subsequent work. For now, focus on securing the API to prevent data leaks and unauthorized access.

### Complementary knowledge: how JWT authentication works in FastAPI

If you haven't implemented JWT auth before, here's the mental model: when a user logs in, the server signs a small JSON payload (the "claims") using a secret key and returns the result as a token string. On subsequent requests, the client sends that token in the `Authorization` header. The server decodes it — if the signature is valid and the token hasn't expired, the request proceeds; if not, it gets a `401`.

In FastAPI, this flow is implemented as a dependency. You write a function that extracts the token from the request, validates it, and returns the user object. Any route that declares that function as a dependency will automatically require authentication.

---

## 🌱 How to Start the Project

This project is an extension of your existing transversal project API. **Do not create a new repository.** Work inside your company's current backend codebase.

1. Open your existing project in Codespaces or clone it locally.
2. Create a new branch for this feature: `git checkout -b feature/auth`.
3. Install the required packages:
   ```bash
   pip install python-jose[cryptography] passlib[bcrypt]
   ```
4. Add them to your `requirements.txt`.



---

## 💻 What You Need to Do

### User model and CRUD

- [ ] Create a `User` model in the database with at least: `id`, `email`, `hashed_password`, `is_active`, `created_at`.
- [ ] Implement a service layer with functions for: create user, get user by ID, get user by email, update user, delete user.
- [ ] Expose those services as REST endpoints under `/users`:
  - `POST /users` — register a new user (hash the password before storing).
  - `GET /users` — list all users (protected).
  - `GET /users/{id}` — get a single user (protected).
  - `PUT /users/{id}` — update a user (protected; only the user themselves or an admin).
  - `DELETE /users/{id}` — delete a user (protected).

### Authentication endpoints

- [ ] Implement `POST /auth/login` — accepts `email` and `password`, validates credentials, returns a JWT access token.
- [ ] Implement `POST /auth/register` — creates a new user and returns a token so the caller is logged in immediately.
- [ ] Implement `GET /auth/me` (protected) — returns the profile of the currently authenticated user.

### Token and dependency

- [ ] Create a `get_current_user` dependency that: extracts the `Authorization: Bearer <token>` header, decodes and validates the JWT, retrieves the user from the database, and raises `HTTPException(401)` if anything fails.
- [ ] Set token expiry via an environment variable (e.g. `ACCESS_TOKEN_EXPIRE_MINUTES`). Store the signing secret in `.env` — never hardcode it.

### Route protection

- [ ] Apply `get_current_user` as a dependency to every route that should not be publicly accessible. At minimum: all `/users` endpoints except `POST /users`, and `/auth/me`.
- [ ] Return `401 Unauthorized` for unauthenticated requests and `403 Forbidden` when a user tries to access a resource they don't own.

### Testing

- [ ] Verify the full flow manually using the FastAPI interactive docs (`/docs`): register → login → copy token → use token on a protected route.
- [ ] Confirm that calling a protected route without a token returns `401`.
- [ ] Confirm that calling a protected route with an expired or malformed token returns `401`.

⚠️ **IMPORTANT:** Do not use session-based or cookie-based authentication. This project implements stateless JWT auth only.

⚠️ **IMPORTANT:** Never store plain-text passwords. Use `passlib` with the `bcrypt` scheme for all password operations.

---

## ✅ What We Will Evaluate

- [ ] User CRUD is fully implemented and reachable via the API.
- [ ] Passwords are hashed at creation and compared correctly at login — plain text never touches the database.
- [ ] Login endpoint returns a valid, signed JWT token.
- [ ] `get_current_user` dependency correctly decodes the token and identifies the user.
- [ ] Protected routes return `401` when called without a valid token.
- [ ] Token expiry and signing secret are read from environment variables, not hardcoded.
- [ ] Auth routes are under `/auth` and user routes are under `/users` — clean, consistent structure.
- [ ] The existing routes of the project continue to work (no regressions).

> Note: Role-based access control (admin vs. regular user) is not required for this delivery, though it is a valid extension if time allows.

---

## 📦 How to Submit

Push your branch to GitHub and open a pull request against `main` in your transversal project repository. Share the PR link with your instructor. The PR description should include a brief note on which routes are now protected and how you verified it.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/fastapi-auth/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
