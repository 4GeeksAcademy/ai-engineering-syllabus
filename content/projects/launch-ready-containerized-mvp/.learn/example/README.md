# Class Example: Neighborhood Gym — Live Check-in Board (Docker Compose)

> **For instructors:** This is not the student deliverable. Use it as a 60–90 minute live demo of the same technical spine as `launch-ready-containerized-mvp`: one Next.js view, one FastAPI endpoint, one PostgreSQL container — all wired with Docker Compose. Domain is a gym front-desk screen, not a generic product MVP.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

You are setting up a **gym check-in board** for a small neighborhood gym. Reception needs a browser page that shows whether the booking API is up and whether the database is reachable — nothing more. No memberships, no payments, no admin panel.

### Scope note

Compared with the official student project, this example keeps the **same three-container pattern** but narrows the story:

- **One** Next.js page (no routing, no design system).
- **One** backend route: `GET /status`.
- **One** database check (connection only; no tables).
- Instructors may skip multi-stage Dockerfile polish in class and add it as homework; students must still deliver the full rubric from the root README.

---

## What to build

### Containers (three services)

| Service    | Role                                                             |
| ---------- | ---------------------------------------------------------------- |
| `frontend` | Next.js — single page "Gym board is live" + fetch backend status |
| `backend`  | FastAPI — `GET /status` returns JSON health                      |
| `db`       | PostgreSQL — running; backend pings with `SELECT 1`              |

### Frontend checklist

- [ ] Create `frontend/` with Next.js defaults (`npx create-next-app@latest`).
- [ ] One page shows a title and the parsed JSON from `GET /status`.
- [ ] Read API base URL from `NEXT_PUBLIC_API_URL` in `.env`.

### Backend checklist

- [ ] Create `backend/main.py` with FastAPI and `GET /status`.
- [ ] Response shape (example):

```json
{
  "status": "ok",
  "service": "gym-check-in-api",
  "database": "connected"
}
```

- [ ] Connect to Postgres using hostname **`db`** (not `localhost`).

### Docker Compose checklist

- [ ] Root `docker-compose.yml` with services `frontend`, `backend`, `db`.
- [ ] `depends_on`: `backend` → `db`, `frontend` → `backend`.
- [ ] Named volume on `db` for persistence.
- [ ] Root `.env` + `.env.example`; `.env` in `.gitignore`.

### Run together

- [ ] `docker compose up --build` starts all three services.
- [ ] Open `http://localhost:3000` and confirm status JSON appears on screen.
- [ ] Hit backend status URL directly and confirm JSON.

---

## Verify together

- [ ] All three containers stay up after a restart (`docker compose down && docker compose up`).
- [ ] Frontend fails clearly if backend URL is wrong (quick teachable moment).
- [ ] Backend logs show successful DB ping, not connection refused to `localhost`.

---

## Discussion questions

1. Why must the backend use the service name `db` instead of `localhost` inside Compose?
2. What breaks if `NEXT_PUBLIC_API_URL` points to `http://backend:8000` from the browser?
3. What would you add next (healthchecks, migrations, CI) before calling this production-ready?
