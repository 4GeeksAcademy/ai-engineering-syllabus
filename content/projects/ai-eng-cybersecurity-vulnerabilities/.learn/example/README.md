# Maple Street Library — OWASP Top 10 Audit (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-cybersecurity-vulnerabilities`. Same spine (server hardening checklist, OWASP matrix for backend / frontend / agent, critical fix + before/after proof). Different domain than company CONTEXT audits. Builds on the Maple Street Library narrative from earlier class examples. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** runs a tiny desk API (`GET /faq`, `POST /chat`) and a desk agent with one tool: `waive_overdue_fine`. The stack was deployed on a classroom VM with root SSH, port 8000 wide open, and debug mode enabled. Security wants a **one-session OWASP pass** before the board demo.

### Scope note

| Graded project (`ai-eng-cybersecurity-vulnerabilities`) | This class example                              |
| ------------------------------------------------------- | ----------------------------------------------- |
| Company monorepo + CONTEXT-company.md                   | Maple Street desk API + agent only              |
| Full server hardening on prod VM                        | Documented hardening steps on classroom VM      |
| 10 OWASP categories × 3 lanes                           | Short matrix + focus on A01, A02, A05 for agent |
| PR to company fork                                      | Local checklist + demo commands                 |

---

## Teaching spine (must hit live)

1. Baseline: note root SSH, open ports, debug flag
2. Non-root user + `PermitRootLogin no` (or classroom equivalent)
3. Firewall: only 22 (SSH) + 8000 (app) — close everything else on paper
4. OWASP matrix: backend (`/faq`, `/chat`), frontend (static desk page if any), agent (waive tool)
5. Fix ≥2 critical issues (e.g. debug off, tool ACL, env secrets)
6. Before/after command or test for each fix

---

## Seed vulnerabilities (indicative)

```text
- API runs with DEBUG=true exposing stack traces (A05)
- waive_overdue_fine callable without role check (A01)
- OPENAI_API_KEY in source file (A02)
- Agent process runs as root on VM (A05)
```

Audit scope: **desk FAQ API + waive agent** — not the whole library ERP.

---

## Mini OWASP matrix (fill in class)

| Category             | Backend       | Frontend | Agent                  | Applies? |
| -------------------- | ------------- | -------- | ---------------------- | -------- |
| A01 Access control   | `/chat` open? | —        | waive without role?    | yes      |
| A02 Crypto failures  | TLS? secrets? | —        | API key storage        | yes      |
| A05 Misconfiguration | DEBUG=true    | —        | runs as root           | yes      |
| A03 Injection        | chat input    | —        | poison in FAQ retrieve | discuss  |
| Others               | …             | …        | …                      | document |

---

## What to build (checklist)

- [ ] `docs/security/baseline.md` — ports, SSH user, debug flags before fixes
- [ ] Hardening notes: non-root user, SSH policy, firewall rules (even if simulated)
- [ ] `docs/security/owasp-top10-report.md` — all 10 rows with evidence or justified N/A
- [ ] Fix DEBUG / secrets / waive ACL — pick two as **critical**
- [ ] `tests/security/test_access_control.py` or curl script showing before/after
- [ ] Agent audited separately from API routes

---

## Verify together

- [ ] Root SSH blocked (or documented classroom substitute)
- [ ] Non-root deploy user named in hardening doc
- [ ] Firewall/port list matches teaching VM
- [ ] 10 OWASP rows filled
- [ ] Agent row not empty
- [ ] Two critical fixes demonstrated live

---

## Discussion questions

1. Why audit the agent separately if it calls the same API?
2. Which OWASP category is DEBUG=true — and why isn't logging enough?
3. How would Maple Street's open port list differ from a CONTEXT company's SSE/MCP ports?
