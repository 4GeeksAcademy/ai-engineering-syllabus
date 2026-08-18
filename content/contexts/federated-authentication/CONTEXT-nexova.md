# CONTEXT — Federated Authentication · Nexova

_Estas instrucciones también están disponibles en [español](./CONTEXT-nexova.es.md)._

> **Project:** Platform – Federated Authentication  
> **Repository path:** `content/contexts/federated-authentication/CONTEXT-nexova.md`

---

## 1. Why this matters to Nexova

Nexova deals with candidates who already keep their professional profile complete on another platform. Asking them to create and remember yet another password just to apply or track their selection process is unnecessary friction — and both Marcos Ibáñez (Sales) and Javier Almeida (Operations) agree that every extra step in the application form reduces completed applications.

## 2. Chosen identity provider

**LinkedIn** — it's where Nexova's target candidate (executive and mid-management headhunting profiles) already keeps their professional information up to date. Using LinkedIn also allows, in future phases, prefilling part of the candidate's profile — but that's not part of this project.

| `provider` code | Required? | Notes                                                              |
| --------------- | --------- | ------------------------------------------------------------------ |
| `linkedin`      | **yes**   | LinkedIn OAuth 2.0 / OIDC. Only allowed provider for this CONTEXT. |

Do **not** implement profile prefilling, CV import, or posting to LinkedIn. This project is identity linking and login only.

## 3. Where it applies

- **Candidate portal:** a candidate who already registered through the traditional method can link their LinkedIn account from their profile, for faster future sign-ins.
- **Internal use:** Nexova staff (consultants, sales, support) don't use LinkedIn as a federated provider — don't apply this project to internal staff, or use a different corporate provider if your context requires it.

## 4. Linking rule (reminder from the README)

Linking only happens from the profile of a candidate with an already-started session. A visitor who arrives with "Continue with LinkedIn" and no prior Nexova account must be directed to register first.

Unlinking lives on the same profile screen. If LinkedIn is the candidate's **only** remaining access method, the UI must warn and the API must refuse the unlink until a password exists.

A LinkedIn identity (`provider` + `provider_user_id`) cannot be linked to two candidate accounts at once.

## 5. Data model and OAuth

Store the link, not the LinkedIn session.

| Field                | Type      | Rules                                                       |
| -------------------- | --------- | ----------------------------------------------------------- |
| `user_id`            | FK → User | required; candidate only                                    |
| `provider`           | string    | `linkedin`                                                  |
| `provider_user_id`   | string    | LinkedIn member id / `sub`. Unique together with `provider` |
| `email_at_link_time` | string    | snapshot only                                               |
| `linked_at`          | datetime  | system                                                      |

Do **not** persist LinkedIn access/refresh tokens in plaintext. This project does not require storing tokens.

OAuth must validate `state` and an allowlisted `redirect_uri`.

```bash
LINKEDIN_CLIENT_ID=...
LINKEDIN_CLIENT_SECRET=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/linkedin
```

A callback with a mismatched `redirect_uri` is rejected.

## 6. Required seed data

Create at least one test candidate with LinkedIn linked and one without.

```python
USERS_SEED = [
    {
        "email": "candidate.linked@nexova.example",
        "name": "Alex Rivera",
        "audience": "candidate",
        "has_password": True,
        "linked_providers": [
            {"provider": "linkedin", "provider_user_id": "li-sub-alex-001"}
        ],
    },
    {
        "email": "candidate.unlinked@nexova.example",
        "name": "Jordan Lee",
        "audience": "candidate",
        "has_password": True,
        "linked_providers": [],
    },
]
```

A LinkedIn identity **not** in `linked_providers` (e.g. `li-sub-unknown-999`) is the rejected-login fixture.

## 7. Audit events (required)

Log these with timestamp, `user_id` (nullable on reject), `provider`, and `provider_user_id`:

| `event`                    | When                                                               |
| -------------------------- | ------------------------------------------------------------------ |
| `federated_link`           | LinkedIn linked from authenticated candidate profile               |
| `federated_unlink`         | LinkedIn unlinked                                                  |
| `federated_login_success`  | Continue with LinkedIn on an already-linked account                |
| `federated_login_rejected` | Continue with LinkedIn with no link — **no candidate row created** |

## 8. Specific acceptance criterion

A "Continue with LinkedIn" attempt from an account not linked to any existing candidate must show a clear message inviting the user to register first, without creating an empty candidate profile as a side effect.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
