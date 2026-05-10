# In-Class Example — Auth Flows for a Recipe Box App

> **Instructor note:** This is a classroom-paced example to introduce the same concepts as the graded project (frontend authentication flows). Use a different domain so students don't confuse it with their own work. A personal recipe collection is simple enough to reason about in class while covering all the key patterns: token storage, protected routes, profile management, and logout.

---

## The Scenario

**Recipe Box** is a Next.js app where users save and organize their favorite recipes. The API already requires a JWT token on protected routes (implemented in the previous class). Now students need to wire up the frontend: login, registration, profile page, and route protection so that only signed-in users can access their recipe collection.

---

## Prerequisites

- The FastAPI auth API from the previous class is running and reachable.
- `NEXT_PUBLIC_API_URL` is set in `.env.local`.

---

## What to Build

### Auth views

**`/login`**

- [ ] Email and password form.
- [ ] On success: store the JWT token in `localStorage` as `access_token`, then redirect to `/recipes`.
- [ ] On failure: show a clear, field-level error message (e.g. "Invalid email or password").
- [ ] Link to `/register` for new users.

**`/register`**

- [ ] Name, email, and password form with a password confirmation field.
- [ ] Validate that password and confirmation match before calling the API.
- [ ] On success: store the token, redirect to `/recipes`.
- [ ] On failure: show specific validation errors per field.

---

### Account views

**`/account/profile`**

- [ ] Fetch `GET /auth/me` (with the token in the `Authorization` header) and display the user's name and email.
- [ ] Allow editing the name. Call `PUT /users/{id}` with the token.
- [ ] Show a success message after saving.

**`/account/change-password`**

- [ ] Form with: current password, new password, confirmation.
- [ ] Validate that new password and confirmation match **before** calling the API.
- [ ] On success: show confirmation. On failure: show the API error.

---

### Route protection

- [ ] Every page under `/recipes` and `/account` requires a valid token in `localStorage`.
- [ ] Implement a layout guard or middleware: if no token is found, redirect to `/login`.
- [ ] The home page (`/`) and `/login` and `/register` must remain fully public — no token check.

```
Protected routes: /recipes, /account/profile, /account/change-password
Public routes:    /, /login, /register
```

---

### Token lifecycle

| Event | Action |
|---|---|
| Successful login / register | Store token → `localStorage.setItem('access_token', token)` |
| Every protected API call | Read token → set `Authorization: Bearer <token>` header |
| Logout | Remove token → `localStorage.removeItem('access_token')` → redirect to `/login` |
| API responds with `401` | Clear token → redirect to `/login` |

---

## Suggested Helper (to reuse in every fetch call)

```ts
// lib/api.ts
export function authHeader(): HeadersInit {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}
```

---

## Key Concepts to Discuss in Class

| Concept | Where it appears |
|---|---|
| `localStorage` for token storage | `setItem` / `getItem` / `removeItem` |
| Attaching `Authorization` header | Every protected `fetch` call |
| Next.js middleware / layout guard | `middleware.ts` or layout-level check |
| Redirect on missing token | `useRouter().push('/login')` |
| Handling `401` from the API | Clear session and redirect |
| Password confirmation validation | Client-side before API call |

---

## Discussion Questions

1. We're storing the token in `localStorage`. What are the security risks of this approach compared to `httpOnly` cookies? When would you choose one over the other?
2. The layout guard redirects to `/login` if there's no token. But what if the token is present but has expired? How would you detect that without making an extra API call on every page load?
3. If a user has the app open in two browser tabs and logs out in one, what happens in the other tab? How would you handle that gracefully?
