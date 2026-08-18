# CONTEXT — Federated Authentication · HealthCore

_Estas instrucciones también están disponibles en [español](./CONTEXT-healthcore.es.md)._

> **Project:** Platform – Federated Authentication  
> **Repository path:** `content/contexts/federated-authentication/CONTEXT-healthcore.md`

---

## 1. Why this matters to HealthCore

HealthCore is a regulated environment: any mechanism for accessing an account with patient data must be as defensible to a HIPAA or UK GDPR auditor as the rest of the system. James Osei (CTO) wants to offer federated login to clinical and administrative staff — who already use Microsoft 365 for corporate email — but only if the mechanism doesn't weaken existing access control.

## 2. Chosen identity provider

**Microsoft** — it's the identity provider already deployed for HealthCore's corporate email in both the US and UK, allowing reuse of account management that IT already audits.

| `provider` code | Required? | Notes                                                                  |
| --------------- | --------- | ---------------------------------------------------------------------- |
| `microsoft`     | **yes**   | Microsoft identity platform (OAuth 2.0 / OIDC). Only allowed provider. |

Do **not** add Google, Apple, or LinkedIn for this CONTEXT. Mixing consumer IdPs with staff access to clinical systems fails the audit story.

## 3. Where it applies

This project applies **only to HealthCore's internal staff** (clinical, administrative, billing, compliance) — never to patients. The patient portal has its own identity rules and must not be mixed with this flow.

## 4. Linking rule (reminder from the README, reinforced here)

Linking only happens from the profile of an employee with a session already started through the traditional method, and **only after IT has provisioned that person in the system**. Federated login must never be the way a new employee gets onboarded — that would be equivalent to letting anyone with a Microsoft account reach patient data without going through the access provisioning process.

Unlinking lives on the same profile screen. If Microsoft is the employee's **only** remaining access method, the UI must warn and the API must refuse the unlink until a password (or another approved method) exists.

A Microsoft identity (`provider` + `provider_user_id`) cannot be linked to two HealthCore staff users at once.

## 5. Data model and OAuth

Store the link, not the Microsoft session.

| Field                | Type      | Rules                                                    |
| -------------------- | --------- | -------------------------------------------------------- |
| `user_id`            | FK → User | required; staff user only                                |
| `provider`           | string    | `microsoft`                                              |
| `provider_user_id`   | string    | Microsoft `oid` / `sub`. Unique together with `provider` |
| `email_at_link_time` | string    | snapshot only                                            |
| `linked_at`          | datetime  | system                                                   |
| `provisioned_by_it`  | bool      | must be `true` before linking is allowed                 |

Do **not** persist Microsoft access/refresh tokens in plaintext. This project does not require storing tokens.

OAuth must validate `state` and an allowlisted `redirect_uri`.

```bash
MICROSOFT_CLIENT_ID=...
MICROSOFT_CLIENT_SECRET=...
MICROSOFT_TENANT_ID=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/microsoft
```

Use a **single-tenant** (or explicit tenant) configuration — not "any Microsoft account". A callback with a mismatched `redirect_uri` is rejected.

## 6. Required seed data

Create at least one test user (clinical or administrative staff) with Microsoft linked and one without, both with fully synthetic data.

```python
USERS_SEED = [
    {
        "email": "marcus.clinical@healthcore.example",
        "name": "Dr. Marcus Reid",
        "audience": "staff",
        "has_password": True,
        "provisioned_by_it": True,
        "linked_providers": [
            {"provider": "microsoft", "provider_user_id": "ms-oid-marcus-001"}
        ],
    },
    {
        "email": "priya.access@healthcore.example",
        "name": "Priya Nair",
        "audience": "staff",
        "has_password": True,
        "provisioned_by_it": True,
        "linked_providers": [],
    },
]
```

A Microsoft identity **not** in `linked_providers` (e.g. `ms-oid-unknown-999`) is the rejected-login fixture. Do not seed real patient identities.

## 7. Audit events (required)

Log these with timestamp, `user_id` (nullable on reject), `provider`, and `provider_user_id`. Rejected staff Microsoft logins are a **security event**, not a UX miss.

| `event`                    | When                                                                 |
| -------------------------- | -------------------------------------------------------------------- |
| `federated_link`           | Provider linked from authenticated staff profile                     |
| `federated_unlink`         | Provider unlinked                                                    |
| `federated_login_success`  | Sign-in with an already-linked Microsoft account                     |
| `federated_login_rejected` | Sign-in with an unlinked Microsoft account — **no user row created** |

## 8. Specific acceptance criterion

A "Sign in with Microsoft" attempt from a valid corporate account not linked to any existing HealthCore user must be explicitly rejected and logged in the audit trail — because in this context, that attempt could represent a security risk, not just a user error.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
