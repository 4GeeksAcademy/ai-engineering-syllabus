# Building Bullet-Proof Applications — Reference Solution

## Purpose

Reference quality bar for the authentication API **test suite** — not for re-implementing auth. Students extend their existing monorepo API with `tests/`, `TESTING.md`, and optional Jest coverage for TypeScript helpers.

## Expected Repository Layout

```text
services/
  api/
    app/
      routes/
        auth.py
        users.py
        profiles.py
      core/
        security.py
      services/
        user_service.py
    tests/
      conftest.py
      test_register.py
      test_login.py
      test_token.py
      test_profiles.py
    TESTING.md
    pyproject.toml
```

Adjust paths to match the student's monorepo, but `tests/` and `TESTING.md` must live alongside the FastAPI app they are testing.

## Required Coverage (From README)

- `TESTING.md` at project root documenting: how to run tests, planned cases per endpoint, coverage results, and at least one AI-assisted discovery or bug caught by tests.
- `tests/` directory with one module per auth concern (`register`, `login`, `token`, `profiles`, etc.).
- Per endpoint: **happy path**, **edge case**, **failure mode** — asserting business logic, not HTTP serialization.
- `uv run pytest` passes from project root.
- `uv run pytest --cov` shows **≥ 70%** coverage on the authentication module.
- Optional: Jest tests for TypeScript auth utilities if present in the monorepo.

## TESTING.md Outline

A strong submission includes:

1. **How to run**
   - `uv run pytest`
   - `uv run pytest --cov=app --cov-report=term-missing`
   - `jest --coverage` (if applicable)
2. **Test plan table** — endpoint × happy / edge / failure cases planned before coding.
3. **Coverage snapshot** — paste terminal output after `--cov`.
4. **AI workflow note** — one case suggested by an agent or one bug fixed after a failing test.

## Indicative Test Cases

### `POST /users` (register)

| Tier    | Example case                                          | Assert                                   |
| ------- | ----------------------------------------------------- | ---------------------------------------- |
| Happy   | Valid email + password creates user with `role: user` | User persisted; linked `Profile` created |
| Edge    | Duplicate email                                       | Rejected before second insert            |
| Failure | Empty password or invalid email format                | Validation error before DB write         |

### `POST /auth/login`

| Tier    | Example case                          | Assert                           |
| ------- | ------------------------------------- | -------------------------------- |
| Happy   | Correct credentials return signed JWT | Token decodes to correct user id |
| Edge    | User exists but `is_active` is false  | Login rejected                   |
| Failure | Wrong password                        | No token issued                  |

### Token / `get_current_user`

| Tier    | Example case                  | Assert                                 |
| ------- | ----------------------------- | -------------------------------------- |
| Happy   | Valid token identifies user   | `GET /auth/me` returns email + profile |
| Edge    | Token near expiry still valid | Request succeeds before expiry         |
| Failure | Expired or malformed token    | `401`; no user returned                |

### `PUT /profiles/me`

| Tier    | Example case           | Assert                                  |
| ------- | ---------------------- | --------------------------------------- |
| Happy   | Owner updates `name`   | Profile field changes; `User` unchanged |
| Edge    | Empty optional `phone` | Accepted or normalized per schema       |
| Failure | Request without token  | `401`                                   |

## pytest Patterns (Indicative)

Use `httpx.AsyncClient` or FastAPI `TestClient` — but assert **outcomes**, not framework plumbing:

```python
def test_login_rejects_wrong_password(client, seeded_user):
    response = client.post("/auth/login", json={
        "email": seeded_user["email"],
        "password": "wrong-password",
    })
    assert response.status_code == 401
    assert "access_token" not in response.json()
```

```python
def test_register_defaults_role_to_user(client):
    response = client.post("/users", json={
        "email": "new@example.com",
        "password": "securepass123",
        "name": "Test User",
    })
    assert response.status_code == 201
    user = response.json()
    assert user["role"] == "user"
```

Prefer fixtures in `conftest.py` for TinyDB test DB isolation — wipe or use a temp file per test session.

## What Not to Test

- FastAPI/OpenAPI response schema generation internals
- Generic 404/422 framework messages with no business meaning
- Third-party library behaviour (`passlib`, `python-jose`) — mock only when necessary

## Evaluation Checklist

- [ ] `TESTING.md` present with plan, run commands, and coverage evidence.
- [ ] `uv run pytest` passes with happy / edge / failure cases per auth endpoint.
- [ ] Authentication module coverage ≥ 70%.
- [ ] Tests target business decisions (credentials, tokens, ownership), not serializers.
- [ ] Optional Jest suite passes if TypeScript helpers exist.
- [ ] AI-assisted workflow documented in `TESTING.md`.

## Reviewer Notes

- Quality of case selection matters more than hitting 100% coverage.
- Accept different file names if test tiers are clearly present per endpoint.
- Extra backoffice/frontend suites (API-042, FE-019) are bonus only.
