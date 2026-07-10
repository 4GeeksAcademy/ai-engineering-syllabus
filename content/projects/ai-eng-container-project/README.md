# Company Monorepo Containerization

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The monorepo is up and running: the team has built the Next.js frontends, the FastAPI service, and the supporting scripts. Everything works on your machine. The problem is that it only works on your machine.

The infrastructure team has raised an internal RFP to the squad: every time a new developer joins, onboarding takes hours because of Node and Python version conflicts, globally installed dependencies, and configuration steps nobody has fully documented. The goal of this project is to solve that at the root: **the development environment must be defined as code, versioned alongside the project, and run identically on any team member's machine without manual configuration**.

Your tech lead has assigned the ticket to the squad. The brief is direct: dockerize the entire monorepo for development. Both frontends — the public-facing site (`/uis/website`) and the internal admin panel (`/uis/backoffice`) — must run from a **single UI container**. The FastAPI service goes in its own container. Both must start with hot reloading, read configuration from environment variables, and communicate with each other by service name inside the Docker network — not by `localhost`.

> **Technical brief — Ticket #infra-40**
>
> > The team needs reproducible development environments. Every time someone new clones the repository, onboarding turns into a dependency debugging session.
> >
> > **Scope**: dockerize `/uis` (website + backoffice in a single UI container with hot reloading) and `/services` (FastAPI with `--reload`). Orchestration is managed with Docker Compose.
> >
> > **Acceptance criteria**: any team member can run `docker compose up` from the repository root and have the full platform running without additional steps.
> >
> > Services communicate with each other **by Docker service name**, not by `localhost`. Review all inter-service connection URLs before sign-off.

---

## 🌱 How to Start the Project

1. Make sure you have Docker Desktop (or Docker Engine + Docker Compose CLI v2) installed and running.
2. Work from your fork of the base repository:

   ```text
   https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo
   ```

3. Review the current monorepo structure. You will need to create `Dockerfile` and `.dockerignore` files in `/uis/` and in `/services/`. The `docker-compose.yml` file goes in the repository root.
4. Create a `.env` file at the root before writing any `docker-compose.yml`. The environment variable names for your project are already familiar — you have been working with them for weeks.

---

## 💻 What You Need to Do

### UI Dockerfile (`/uis/Dockerfile`)

- [ ] Create a `Dockerfile` in `/uis/` based on an official Node image (Alpine). It must install the dependencies for `/uis/website` and `/uis/backoffice` separately.
- [ ] The default `CMD` of the Dockerfile must invoke a `start.sh` script that starts both Next.js applications on separate ports (`website` on 3000, `backoffice` on 3001).
- [ ] Create a `.dockerignore` in `/uis/` that excludes at minimum: `node_modules`, `.next`, `.env*`, and `*.log`.

### Backend Dockerfile (`/services/Dockerfile`)

- [ ] Create a `Dockerfile` in `/services/` based on an official Python image. It must install `uv`, install dependencies from `requirements.txt` with `uv pip install -r requirements.txt`, and start the Uvicorn server with `--reload` enabled.
- [ ] Create a `.dockerignore` in `/services/` that excludes at minimum: `__pycache__`, `*.pyc`, `.env*`, `tests/`, and `*.log`.

### Docker Compose (`docker-compose.yml`)

- [ ] Create `docker-compose.yml` at the repository root with two services: the UI service (built from `/uis/`, with a bind mount on the source code and `next dev` commands for both apps) and the backend service (built from `/services/`, with a bind mount and `--reload`).
- [ ] Expose the correct ports in each service so they are accessible from the host.
- [ ] Connect both services on an explicitly named Docker network. Verify that inter-service connection URLs use the service name as the host, not `localhost`.

> 🔐 **Never include real secrets, API keys, or passwords in `docker-compose.yml` or in any `Dockerfile`.** These files are versioned in Git and anyone with access to the repository can read them. Credentials belong exclusively in `.env`, which must be in `.gitignore`. If you accidentally commit a secret, consider it compromised and rotate it immediately.

- [ ] Define all environment variables for each service via a `.env` file at the repository root (not hardcoded in the YAML).
- [ ] Confirm that `.env` is in the repository's `.gitignore`.

---

## ✅ What We Will Evaluate

- [ ] `docker compose up` from the repository root starts the full platform without errors and without additional configuration steps.
- [ ] Code changes on the host are reflected in the browser without rebuilding the image (bind mounts working on both services).
- [ ] The UI service starts both Next.js applications on separate ports (3000 and 3001) from a single container.
- [ ] Services communicate internally by Docker service name, not by `localhost` or hardcoded IP.
- [ ] No secrets, API keys, or passwords are hardcoded in any `Dockerfile` or in `docker-compose.yml`.
- [ ] The `.env` file is in `.gitignore` and does not appear in the commit history.
- [ ] `.dockerignore` files exist in `/uis/` and in `/services/`.

---

## 📦 How to Submit

1. Push all changes to your branch on GitHub.
2. Open a Pull Request from your branch to `main`.
3. Include in the PR description a screenshot showing the running containers (`docker compose ps` or the output of `docker compose up`).
4. Share the PR link with your tech lead for final sign-off.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
