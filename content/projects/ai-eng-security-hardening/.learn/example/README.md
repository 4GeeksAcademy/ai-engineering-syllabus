# Community Garden Plot API — Security Pass (Class Example)

> **For instructors:** Not the student project. Same spine as `ai-eng-security-hardening`: guided OWASP review, 3 real findings with before/after proof, rate limits, secrets audit, rotation doc. Domain = community garden plot reservations API.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

Small FastAPI serves plot reservations for a community garden. CTO blocks public demo until someone proves the app isn't trivially exploitable. One class session: find real bugs, fix one critical, document rest.

### Scope note

3 endpoints max (`POST /auth/login`, `GET /plots`, `POST /plots/{id}/reserve`). No server SSH/firewall. Students follow full brief in root `README.md`.

---

## What to build

### Audit doc

- [ ] Mini OWASP matrix (10 rows, applies/N/A)
- [ ] 3 findings with reproduce steps + impact (e.g. reserve without auth, plot IDOR, debug stack trace)

### Rate limit

- [ ] `POST /auth/login` → 429 after 5/min/IP

### Secrets

- [ ] Remove hardcoded `SECRET_KEY = "dev123"` → env
- [ ] `SECRET_ROTATION.md` one-page procedure

### Fix + proof

- [ ] Fix at least 1 critical finding
- [ ] Before curl output + after test/screenshot per fix

---

## Verify together

- [ ] Demonstrate vuln #1 live (before patch)
- [ ] Same steps fail after patch
- [ ] 6th login → 429
- [ ] `grep -r "dev123" .` clean

---

## Discussion questions

1. Why OWASP checklist without exploit steps fails CTO acceptance?
2. Rate limit by IP — what breaks behind NAT at a school?
3. When is rotating JWT secret safe without kicking all users?
