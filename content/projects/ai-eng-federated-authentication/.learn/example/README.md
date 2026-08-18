# Club Locker Room — Link Google After You Already Have a Card (Class Example)

> **For instructors:** Not the student project. Live demo of the same spine as `ai-eng-federated-authentication`: federated login **does not create accounts**; linking only from an authenticated profile; OAuth `state` + `redirect_uri`; unlink must not leave zero access methods; audit rejected logins. Domain is a neighborhood sports club so students do not copy the company IdP story.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

The club already has membership numbers and passwords. Members want "Sign in with Google". The board's rule: Google may only open a **card that already exists and that the member linked from My account**. Showing up with a Google login must never mint a new membership.

### Scope note

One session. One provider (`google`), two flows (link vs login), mocked OAuth callback (no live Google Cloud project required). Drop multi-provider, Apple/Microsoft/LinkedIn, and polished UI — `/docs` plus a tiny profile page is enough. Students still follow the full brief in the project root `README.md`.

---

## What to build

### Model

- [ ] `IdentityLink`: `user_id`, `provider="google"`, `provider_user_id`, `linked_at`
- [ ] Unique `(provider, provider_user_id)`
- [ ] No plaintext Google tokens

### Two OAuth paths

- [ ] `GET /auth/google/link` — requires session; stores `state` with `intent=link`
- [ ] `GET /auth/google/login` — public; `intent=login`
- [ ] Callback: validate `state` + allowlisted `redirect_uri`
- [ ] Login miss → reject, **do not** `INSERT` user; audit `federated_login_rejected`
- [ ] Link hit on another user → 409

### Unlink

- [ ] `DELETE` link from profile
- [ ] If no password and no other link → warn + 409

---

## Verify together

- [ ] Seed member A with Google `sub=club-001`; member B with password only
- [ ] Callback with `sub=club-unknown` → reject; user count unchanged
- [ ] Anonymous `GET /auth/google/link` → 401
- [ ] Unlink member A's only Google while password exists → OK; unlink last method → 409

---

## Discussion questions

1. Why is "create user on first Google login" convenient and still wrong for a membership system?
2. Where should `intent=link|login` live so a stolen `code` cannot link someone else's account?
3. Is email a safe join key versus `provider_user_id` (`sub`)? What happens when Google email changes?
