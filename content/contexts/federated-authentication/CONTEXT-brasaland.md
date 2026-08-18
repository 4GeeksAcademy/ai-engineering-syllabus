# CONTEXT — Federated Authentication · Brasaland

_Estas instrucciones también están disponibles en [español](./CONTEXT-brasaland.es.md)._

> **Project:** Platform – Federated Authentication  
> **Repository path:** `content/contexts/federated-authentication/CONTEXT-brasaland.md`

---

## 1. Why this matters to Brasaland

Brasaland's customers use the ordering app and loyalty program from their phones, and they hate creating yet another password. Location staff also log into the internal system daily from shared tablets. Reducing login friction matters in both cases, but account security matters even more: no outsider should be able to get into an account with accumulated points or an employee's data.

## 2. Chosen identity provider

**Google** — it's the provider with the highest usage rate among Brasaland's consumers in both markets (Colombia and Florida), and it's already the de facto standard for restaurant apps in the region.

If your implementation justifies it, you may offer a second provider (Apple, common in the Florida market, for example), but Google is the minimum requirement.

| `provider` code | Required? | Notes                                                        |
| --------------- | --------- | ------------------------------------------------------------ |
| `google`        | **yes**   | OAuth 2.0 / OIDC. Minimum for this CONTEXT.                  |
| `apple`         | optional  | Only if you implement a second provider. Same linking rules. |

## 3. Where it applies

- **Customer app (Brasa Points):** the end customer can link their Google account from their profile, after having registered through the traditional method.
- **Internal backoffice:** corporate staff (not location staff, who typically share a device) can link their corporate Google account from their user profile.

Do **not** enable federated login on shared location tablets. A shared device plus "Sign in with Google" is an account-mix risk.

## 4. Linking rule (reminder from the README)

Linking happens **only** from the profile of a user with an already-started session. A customer who arrives for the first time with "Sign in with Google" and has no prior account must be rejected and directed to create their account first through the traditional method.

Unlinking lives on the same profile screen. If Google is the user's **only** remaining access method (no password set, no second provider), the UI must warn and the API must refuse the unlink until another method exists.

A Google identity (`provider` + `provider_user_id`) cannot be linked to two Brasaland users at once.

## 5. Data model and OAuth

Store the link, not the Google session.

| Field                | Type      | Rules                                         |
| -------------------- | --------- | --------------------------------------------- |
| `user_id`            | FK → User | required                                      |
| `provider`           | string    | `google` (or `apple` if offered)              |
| `provider_user_id`   | string    | Google `sub`. Unique together with `provider` |
| `email_at_link_time` | string    | snapshot only — not a live identity key       |
| `linked_at`          | datetime  | system                                        |

Do **not** persist Google access/refresh tokens in plaintext. If you must keep a token, encrypt it; this project does not require storing tokens at all.

OAuth must validate `state` (CSRF / session fixation) and an allowlisted `redirect_uri`.

```bash
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/google
```

Allowed redirect URIs are an exact-match allowlist. A callback with a different `redirect_uri` is rejected.

## 6. Required seed data

Create at least one test customer with a linked Google account and one without, so you can test both paths of the login flow.

```python
USERS_SEED = [
    {
        "email": "camila.points@brasaland.example",
        "name": "Camila Ospina",
        "has_password": True,
        "linked_providers": [
            {"provider": "google", "provider_user_id": "google-sub-camila-001"}
        ],
    },
    {
        "email": "guest.unlinked@brasaland.example",
        "name": "Unlinked Guest",
        "has_password": True,
        "linked_providers": [],
    },
]
```

A third Google identity that is **not** in `linked_providers` is the rejected-login fixture (e.g. `provider_user_id: "google-sub-unknown-999"`).

## 7. Audit events (required)

Log these with timestamp, `user_id` (nullable on reject), `provider`, and `provider_user_id`:

| `event`                    | When                                                        |
| -------------------------- | ----------------------------------------------------------- |
| `federated_link`           | Provider linked from authenticated profile                  |
| `federated_unlink`         | Provider unlinked                                           |
| `federated_login_success`  | Sign-in with an already-linked provider                     |
| `federated_login_rejected` | Sign-in with an unlinked provider — **no user row created** |

## 8. Specific acceptance criterion

A "Sign in with Google" attempt from an email that was never linked to any Brasaland account must show a clear message inviting the user to register first — it must never silently create a new account with zero points.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
