# Connecting the Lock: Authentication Flows in the Frontend — Reference Solution

## Purpose

This is a **Next.js frontend** delivery. Students wire login, register, profile, route guards, and token lifecycle against the existing FastAPI JWT API. Do **not** implement hashing, JWT signing, or `get_current_user` here — that lives in the auth API project.

## Expected file layout (indicative)

```text
uis/backoffice/          # (or the internal Next.js app that hosts account views)
├── app/
│   ├── login/page.tsx
│   ├── register/page.tsx
│   ├── account/profile/page.tsx
│   └── (authenticated)/layout.tsx   # client layout guard
├── lib/
│   ├── api.ts                       # fetch wrapper: attach Bearer, handle 401
│   └── auth.ts                      # getToken / setToken / clearToken (localStorage)
└── components/
    └── LogoutButton.tsx
```

Public website (`uis/website` / Milestone 1) must **not** import these guards.

## Required Coverage (From README)

- `/login` — email + password. On success: store JWT in `localStorage`, redirect to the main authenticated view. On failure: visible error.
- `/register` — call `POST /users` then `POST /auth/login`, store token, redirect. Field-level errors on failure.
- `/account/profile` — `GET /auth/me` shows `email` plus `Profile` (`name`, `phone`, `address`). Edit via `PUT /profiles/me` with `Authorization: Bearer`.
- Identify every authenticated view in the Next.js apps **except** the public website.
- Client layout guard or hook: if no token in `localStorage`, redirect to `/login`.
- Public website unaffected.
- Token lifecycle: store on login/register; attach Bearer on every protected API call; logout clears storage and redirects; `401` from a protected call clears storage and redirects to `/login`.

## Route protection — do not use server middleware for `localStorage`

Next.js middleware runs on the server. It **cannot** read `localStorage`. Use a `"use client"` layout (or hook) that:

1. Reads the token from `localStorage`.
2. Redirects to `/login` when missing.
3. Optionally probes `GET /auth/me` once to detect expired tokens.

Middleware is only valid if the token is **also** stored in a cookie the middleware can read — that is out of scope unless the student already did it.

## Token lifecycle (evaluator mapping)

| Event                       | Required behaviour                        |
| --------------------------- | ----------------------------------------- |
| Login / register success    | `localStorage.setItem(...)` then redirect |
| Protected API call          | `Authorization: Bearer <token>`           |
| Logout                      | `removeItem` + redirect `/login`          |
| Protected API returns `401` | clear token + redirect `/login`           |

## Indicative patterns

### Storage helpers

```ts
const KEY = "access_token";

export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(KEY);
}

export function setToken(token: string): void {
  localStorage.setItem(KEY, token);
}

export function clearToken(): void {
  localStorage.removeItem(KEY);
}
```

### API client — Bearer + 401 interceptor

```ts
export async function api(path: string, init: RequestInit = {}) {
  const token = getToken();
  const headers = new Headers(init.headers);
  if (token) headers.set("Authorization", `Bearer ${token}`);
  const res = await fetch(path, { ...init, headers });
  if (res.status === 401) {
    clearToken();
    window.location.assign("/login");
    throw new Error("Unauthorized");
  }
  return res;
}
```

### Client layout guard

```tsx
"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { getToken } from "@/lib/auth";

export default function AuthenticatedLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  useEffect(() => {
    if (!getToken()) router.replace("/login");
  }, [router]);
  return <>{children}</>;
}
```

## Validation Notes

- Verify in the **browser**, not `/docs`: register → login → profile → logout.
- Trigger a `401` (expired/malformed token) and confirm redirect to `/login` plus cleared storage.
- Confirm the public website has no token check and no redirect.
- Profile shows email from `GET /auth/me` (that endpoint is allowed to return email).

## Key implementation decisions

- Token lives in `localStorage` (README contract). No `httpOnly` cookie required.
- Guards are **client-side**. Server middleware cannot see `localStorage`.
- Password hashing / JWT issuance stay on the API (`libpass` + `python-jose`). This project only consumes the token.
- Do not duplicate `/auth/login` or `/users` in the Next.js app.
