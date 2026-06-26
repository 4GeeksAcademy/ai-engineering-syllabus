# AI Engineering Syllabus

This repository contains the **AI Engineering syllabus** and related learning materials for 4Geeks Academy:

- **Curriculum content** (milestones, skills, contexts and theory).
- **Hands-on projects** for each skill and milestone, under `content/projects/`.
- Supporting files for the platform (`learn.json`, reference solutions, assets, etc.).

---

## Projects (hands-on practice)

You can find the practical projects in [`content/projects`](./content/projects). **Suggested order** (56 projects): web fundamentals and Tailwind first, then OpenClaw setup through memory/onboarding, TypeScript and UML modeling, React/Next.js and company milestones, AI-assisted specs and monorepo work, APIs and auth, incidents and SQL audits, inventory backend/backoffice, Docker, performance, telemetry, data pipelines, background jobs, and message queues.

**Technologies and skills developed in the projects:**

- **HTML5 & CSS3:** Semantic layout, accessibility, SEO, responsive design.
- **Tailwind CSS:** Utility-first styling for rapid and responsive UI development.
- **JavaScript & TypeScript:** Control flow, data structures, validations, error handling.
- **React & Next.js:** Components, routing, URL filters, state and props management, SSR/SSG.
- **Collaborative design & version control:** Git, branching, pull requests, best practices for teamwork.
- **Object modeling & diagrams:** UML, class design, and business model relationships.
- **Interface prototyping:** UI/UX, creation of admin panels and interactive forms.
- **APIs & Backend:** FastAPI, TinyDB, Pydantic, SQLModel, Supabase/PostgreSQL, JWT, RESTful endpoints, serialization, and caching.
- **SQL & data analysis:** Single-table and multi-table queries, data-quality audits, JOINs.
- **Integration with external tools:** OpenClaw, Telegram, Zapier, Google Drive & Calendar, 4Geeks API.
- **Agent development and automation:** Skills, memory, onboarding flows, agent loops, artifact and evidence management.
- **File and data processing:** CSV analysis, Python scripts, Pandas reporting, automated exports and summaries.
- **Systems architecture:** Proposals, diagrams, documentation, and modular application extension.
- **Cybersecurity:** Authentication flows, user state management, password resets, unit-tested auth logic.
- **Docker & containers:** Dockerfiles, Compose, multi-service local orchestration, production-ready environments.
- **Performance engineering:** Core Web Vitals, Lighthouse audits, payload optimization, frontend and API caching.
- **Telemetry:** Event design, frontend capture, batch storage, and reporting pipelines.
- **Data pipelines:** ETL design, Prefect orchestration, idempotency, subflows, and pipeline testing.
- **Background jobs:** Cron scheduling, distributed locks, job state machines, and independent CLI processes.
- **Message queues:** Producer/consumer patterns, Redis brokers, Celery workers, retries, DLQ, and Flower observability.
- **Monorepo development:** Organization and coordination of frontend, backend, and auxiliary services within a single repository.

For more detail on each item, open the project folder and read `README.md` (and `README.es.md` when available). The same ordered list lives in [`content/projects/README.md`](./content/projects/README.md). Company-specific scenario files live under [`content/contexts`](./content/contexts) (see [`content/contexts/README.md`](./content/contexts/README.md)).

---

## Structure of this repository

- `content/` — Syllabus content (milestones, skills, contexts, and projects).
  - `content/projects/` — All AI Engineering practice projects.
- `.learn/` and `learn.json` files — Integration with the 4Geeks platform.

This repository is used as the **single source of truth** for the AI Engineering program materials at 4Geeks Academy.
