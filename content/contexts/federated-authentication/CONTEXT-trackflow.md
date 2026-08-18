# CONTEXT — Federated Authentication · TrackFlow

_Estas instrucciones también están disponibles en [español](./CONTEXT-trackflow.es.md)._

> **Project:** Platform – Federated Authentication  
> **Repository path:** `content/contexts/federated-authentication/CONTEXT-trackflow.md`

---

## 1. Why this matters to TrackFlow

TrackFlow's B2B clients (the brands that outsource their logistics) already manage their corporate identity with Microsoft 365, just like most of TrackFlow's own team in Los Angeles and Zaragoza. Miguel Torres (Commercial) has received more than one complaint from brand account managers asking not to have to manage yet another password for the client portal.

## 2. Chosen identity provider

**Microsoft** — it's the dominant corporate identity provider both among TrackFlow's internal team and among its brand clients, in both countries.

| `provider` code | Required? | Notes                                                                        |
| --------------- | --------- | ---------------------------------------------------------------------------- |
| `microsoft`     | **yes**   | Microsoft identity platform (OAuth 2.0 / OIDC). Minimum (and only) provider. |

## 3. Where it applies

- **Client portal (B2B brands):** an already-registered account manager from a client brand can link their company's Microsoft account from their profile.
- **Internal backoffice:** TrackFlow Tech and operations staff can link their corporate Microsoft account from their profile.

A B2B client's first access is **not** self-serve via federated login. Commercial initiates onboarding; the account already exists before Microsoft can be linked.

## 4. Linking rule (reminder from the README)

Linking only happens from the profile of a user with an already-started session. A user who arrives with "Sign in with Microsoft" and no prior TrackFlow account must be rejected and directed to register first through the appropriate channel (a B2B client's onboarding is normally initiated by the Commercial team, not by the client themselves).

Unlinking lives on the same profile screen. If Microsoft is the user's **only** remaining access method, the UI must warn and the API must refuse the unlink until a password (or another approved method) exists.

A Microsoft identity (`provider` + `provider_user_id`) cannot be linked to two TrackFlow users at once.

## 5. Data model and OAuth

Store the link, not the Microsoft session.

| Field                | Type      | Rules                                                    |
| -------------------- | --------- | -------------------------------------------------------- |
| `user_id`            | FK → User | required                                                 |
| `provider`           | string    | `microsoft`                                              |
| `provider_user_id`   | string    | Microsoft `oid` / `sub`. Unique together with `provider` |
| `email_at_link_time` | string    | snapshot only                                            |
| `linked_at`          | datetime  | system                                                   |
| `audience`           | string    | `internal` or `b2b_client` — not derived from the IdP    |

Do **not** persist Microsoft access/refresh tokens in plaintext. This project does not require storing tokens.

OAuth must validate `state` and an allowlisted `redirect_uri`.

```bash
MICROSOFT_CLIENT_ID=...
MICROSOFT_CLIENT_SECRET=...
MICROSOFT_TENANT_ID=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/microsoft
```

A callback with a mismatched `redirect_uri` is rejected. Multi-tenant is acceptable for B2B clients **only if** the TrackFlow user row already exists; the tenant must never create that row.

## 6. Required seed data

Create at least one test user (internal or B2B client) with Microsoft linked and one without.

```python
USERS_SEED = [
    {
        "email": "miguel.commercial@trackflow.example",
        "name": "Miguel Torres",
        "audience": "internal",
        "has_password": True,
        "linked_providers": [
            {"provider": "microsoft", "provider_user_id": "ms-oid-miguel-001"}
        ],
    },
    {
        "email": "brand.am@northwind.example",
        "name": "Northwind Account Manager",
        "audience": "b2b_client",
        "has_password": True,
        "linked_providers": [],
    },
]
```

A Microsoft identity **not** in `linked_providers` (e.g. `ms-oid-unknown-999`) is the rejected-login fixture.

## 7. Audit events (required)

Log these with timestamp, `user_id` (nullable on reject), `provider`, and `provider_user_id`:

| `event`                    | When                                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| `federated_link`           | Microsoft linked from authenticated profile                                                    |
| `federated_unlink`         | Microsoft unlinked                                                                             |
| `federated_login_success`  | Sign-in with an already-linked Microsoft account                                               |
| `federated_login_rejected` | Sign-in with an unlinked Microsoft account — **no user row and no client association created** |

## 8. Specific acceptance criterion

A "Sign in with Microsoft" attempt from an account not linked to any existing TrackFlow user must be explicitly rejected, without automatically creating an account or a client association.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
