# Launch Ready: Containerized MVP from Scratch — Reference Solution

## Purpose

Reference architecture for a minimal three-service stack: Next.js frontend, FastAPI backend, and PostgreSQL — all orchestrated with Docker Compose and started with a single command.

## Expected Repository Layout

```
my-mvp/
├── frontend/              # Next.js (App Router or Pages — keep defaults)
│   ├── Dockerfile
│   └── .dockerignore
├── backend/
│   ├── main.py            # FastAPI app + GET /status
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── docker-compose.yml
├── .env                   # gitignored
├── .env.example
└── .gitignore
```

## Solution Structure

### Frontend (`frontend/`)

- Single page with a heading (e.g. "MVP is live").
- Fetches `GET /status` from the backend using the URL from environment variables (e.g. `NEXT_PUBLIC_API_URL`).
- Displays the JSON response on the page to prove inter-service communication works.

### Backend (`backend/`)

- FastAPI app with one route: `GET /status`.
- Returns JSON such as `{"status": "ok", "database": "connected"}`.
- Optional: run a lightweight DB ping (`SELECT 1`) using `DATABASE_URL` to confirm PostgreSQL is reachable by **service name** `db`, not `localhost`.

### Database (`db` service)

- Official `postgres` image with credentials from `.env`.
- Named volume for data persistence.
- No migrations, tables, or seed data required.

### Docker Compose

| Service   | Build context | Depends on | Host port (example) |
| --------- | ------------- | ---------- | ------------------- |
| `db`      | image only    | —          | (internal only)     |
| `backend` | `./backend`   | `db`       | `8000:8000`         |
| `frontend`| `./frontend`  | `backend`  | `3000:3000`         |

- Backend connects to PostgreSQL with hostname `db` (Docker network DNS).
- Frontend calls backend via `NEXT_PUBLIC_API_URL` pointing at the published backend port or internal URL as configured.

## Dockerfiles (high level)

**Backend:** `python:3.13-slim`, copy `requirements.txt`, `pip install`, expose `8000`, `CMD` runs `uvicorn main:app --host 0.0.0.0 --port 8000`.

**Frontend:** multi-stage `node:24-alpine` — build stage runs `npm ci` + `next build`; production stage copies `.next` output and runs `next start` on port `3000`.

## Environment Variables (`.env.example`)

| Variable | Used by | Purpose |
| -------- | ------- | ------- |
| `POSTGRES_USER` | db, backend | DB credentials |
| `POSTGRES_PASSWORD` | db, backend | DB credentials |
| `POSTGRES_DB` | db, backend | Database name |
| `DATABASE_URL` | backend | SQLAlchemy/asyncpg or psycopg connection string (`postgresql://...@db:5432/...`) |
| `NEXT_PUBLIC_API_URL` | frontend | Backend base URL for browser fetch |

Only `.env.example` is committed; `.env` is listed in `.gitignore`.

## Expected API Surface

- `GET /status` — returns health JSON; optionally includes database connectivity flag.

### Example response

```json
{
  "status": "ok",
  "database": "connected"
}
```

## Key Implementation Decisions

- **Service discovery:** backend uses hostname `db`; frontend never hardcodes `localhost` for the database.
- **Single command startup:** `docker compose up --build` must bring up all three services without manual steps.
- **Multi-stage frontend image:** smaller production image; build artifacts stay in the build stage.
- **`.dockerignore` on both apps:** exclude `node_modules`, `.next`, `__pycache__`, `.env`, and virtualenv folders.
- **Named volume on `db`:** data survives container restarts.

## Validation Notes

- [ ] `docker compose up --build` completes without errors.
- [ ] `http://localhost:3000` shows the page and backend status payload.
- [ ] Backend status endpoint responds on its mapped port.
- [ ] PostgreSQL container is healthy and backend reports a successful connection.
- [ ] `.env` is not in the repository; `.env.example` is present.
