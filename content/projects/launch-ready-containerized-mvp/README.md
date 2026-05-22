# Launch Ready: Containerized MVP from Scratch

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/launch-ready-containerized-mvp/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

You have an idea for an MVP and you want to start building it the right way — not patching things together later, but setting up a solid, deployable foundation from the very first day.

The goal of this project is not to build a full product. It's to set up the infrastructure that makes building one possible: a containerized environment where a frontend, a backend, and a database run together through Docker Compose, consistently, on any machine.

> **What you're delivering:**
> A minimal but fully operational stack — a simple Next.js page, a FastAPI service with at least one working endpoint, and a connected PostgreSQL database — all orchestrated with Docker Compose and launchable with a single command.

Think of it as building the launchpad, not the rocket. Once this is in place, any feature you add will have a reliable, reproducible environment to run in.

### What "minimal" means here

To keep the focus on infrastructure rather than application development, each layer of your stack should be as simple as possible:

- **Frontend**: A single Next.js page that displays a title and makes one request to the backend API
- **Backend**: A FastAPI application with at least one endpoint (`GET /status` or similar) that returns a response and confirms the database connection is alive
- **Database**: A PostgreSQL instance that the backend can connect to — no tables, no data, just a live connection

The point is that all three layers talk to each other inside Docker's network. That is the deliverable.

---

## 🌱 How to Start the Project

There is no starter template for this project. Create a new GitHub repository and set it up with the following structure before writing any code:

```text
my-mvp/
├── frontend/          # Next.js app
├── backend/           # FastAPI app
├── docker-compose.yml
├── .env
└── .env.example
```

Initialize each service inside its folder (`npx create-next-app` for the frontend, a basic `main.py` for the backend). Keep both as close to their defaults as possible — you will build on top of them later.

> 📗 [Read how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) if you need a refresher on repo setup.

---

## 💻 What You Need to Do

### Minimal application layer

- [ ] **Frontend**: Create a Next.js app with a single page that displays a heading (e.g. "MVP is live") and fetches the backend status endpoint to confirm it's reachable
- [ ] **Backend**: Create a FastAPI app with at least one route — `GET /status` — that returns a JSON response (e.g. `{"status": "ok"}`) and, optionally, confirms the database connection
- [ ] **Database**: No tables or data are required — PostgreSQL just needs to be running and reachable from the backend

### Backend Dockerfile

- [ ] Create `backend/Dockerfile` using an official Python base image (`python:3.13-slim` recommended)
- [ ] Set a working directory, copy `requirements.txt`, install dependencies, expose the correct port, and define a `CMD` to start `uvicorn`
- [ ] Add `backend/.dockerignore` excluding `__pycache__`, `.env`, and virtual environment folders

### Frontend Dockerfile

- [ ] Create `frontend/Dockerfile` using a multi-stage build (build stage + production stage, `node:24-alpine` recommended)
- [ ] The build stage installs dependencies and runs `next build`; the production stage copies only the built output and starts the server
- [ ] Expose port `3000` and define the `CMD` to start Next.js
- [ ] Add `frontend/.dockerignore` excluding `node_modules`, `.next`, and `.env*` files

### Docker Compose

- [ ] Create `docker-compose.yml` at the root with three services: `frontend`, `backend`, and `db`
- [ ] `db` service: use the official `postgres` image, set credentials via environment variables, and mount a named volume for data persistence
- [ ] `backend` service: build from `./backend`, declare `depends_on: db`, and pass database connection variables from `.env`
- [ ] `frontend` service: build from `./frontend`, declare `depends_on: backend`, and map port `3000`
- [ ] Services must communicate through Docker's internal network — the backend connects to `db` by service name, not by `localhost`

### Environment variables

- [ ] Create a `.env` file at the root with all required variables: database credentials, database URL for the backend, and the backend URL for the frontend
- [ ] Create a `.env.example` with the same variable names but no values
- [ ] Add `.env` to `.gitignore`

⚠️ **IMPORTANT:** Never commit the `.env` file to GitHub. Only `.env.example` should be tracked by Git.

### Validation

- [ ] `docker compose up --build` starts all three services without errors
- [ ] The frontend is accessible at `http://localhost:3000`
- [ ] The backend status endpoint responds at its mapped port
- [ ] The frontend successfully fetches and displays data from the backend
- [ ] The database container starts and the backend connects to it without errors

---

## ✅ What We Will Evaluate

- [ ] `Dockerfile` exists for both backend and frontend and follows best practices (slim base images, `.dockerignore` present, minimal layers)
- [ ] The frontend `Dockerfile` uses a multi-stage build
- [ ] `docker-compose.yml` defines all three services with correct configuration
- [ ] Inter-service communication uses Docker's internal network (service names, not `localhost`)
- [ ] The database uses a named volume for persistence
- [ ] All credentials and URLs are managed via `.env`; `.env.example` is committed; `.env` is in `.gitignore`
- [ ] `docker compose up --build` brings the full stack up without manual steps
- [ ] All three layers are reachable and communicate correctly

> Note: The application's features and design are not evaluated. A minimal, working stack is the goal.

---

## 📦 How to Submit

Push your project to GitHub and share the repository URL following your instructor's delivery instructions. Confirm the repository is public and that `.env` is not committed — only `.env.example` should be present.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/launch-ready-containerized-mvp/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
