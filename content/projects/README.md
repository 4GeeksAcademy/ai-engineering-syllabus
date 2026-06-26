# AI Engineering Projects

Repository of hands-on projects for the **AI Engineering** program at 4Geeks Academy. Each folder is a standalone project with its own README, evaluation criteria, and (when applicable) `learn.json` for the platform.

Projects follow a pedagogical order: from web fundamentals (HTML, CSS, SEO, accessibility) and Tailwind, through company milestones and collaboration, **OpenClaw agent setup and integrations**, then TypeScript and system design, React/Next.js and AI-assisted delivery, APIs, authentication, agents, performance, telemetry, data pipelines, background jobs, and message queues.

---

## Projects (suggested order)

0. **[Company Project Milestone: Choose Your Company](./ai-eng-milestone-choose-company)**  
   `Milestone 0` — Pick your fictional company, capture it in `CONTEXT.md`, and prepare the narrative and data you will reuse in later milestones.

1. **[Artist landing: HTML, CSS, SEO and accessibility](./html-css-artist-landing-seo-access)**  
   Accessible, SEO-optimized landing page for an artist using semantic HTML and CSS.

2. **[Simple dashboard with Tailwind CSS](./simple-dashboard-tailwind-css)**  
   Responsive dashboard with HTML and Tailwind showing KPIs, drivers, and operational details (no React).

3. **[Company Project Milestone: Web Fundamentals](./ai-eng-milestone-web-fundamentals)**  
   `Milestone 1` — Your company's public website: landing page plus application/sign-up form with semantic HTML5, Tailwind, Schema.org, and JavaScript validation. Follow `CONTEXT.md` for data and form fields.

4. **[Collaborative project: online store with HTML and Tailwind](./collaborative-project-html-tailwind-online-store)**  
   Collaborative e-commerce prototype (min. 5 pages: Home, Catalog, Product, Cart, Checkout) with HTML and Tailwind, teamwork with branches and pull requests.

5. **[Setting Up Your Personal AI Agent with OpenClaw](./openclaw-setup)**  
   Deploy and configure OpenClaw on a VPS with LiteLLM, validate local chat, and document a safe delivery package (sanitized config + proof screenshot).

6. **[Connect Your Agent: Telegram, Google Drive & Calendar](./openclaw-connection)**  
   Configuration-only project: Telegram channel, Zapier MCP, Google Drive and Calendar actions, and an end-to-end flow confirmed in screenshots (after OpenClaw is running).

7. **[My Agent, My Way: Teaching Your Personal Assistant New Skills](./openclaw-skills)**  
   Continue in your existing OpenClaw environment and repo from prior assignments: fill the five `.openclaw` briefing files, commit `SKILLS_DESIGN.md`, and implement at least two OpenClaw skills using only Composio integrations you already have (Google apps, GitHub, Telegram); add any missing paths per your instructor and OpenClaw docs.

8. **[My 4Geeks Assistant — Teaching OpenClaw to Track Your Progress](./openclaw-integration)**  
   Connect OpenClaw to the 4Geeks API with your account token so the agent can report pending projects, course progress, and related LearnPack data.

9. **[Give Your Agent a Memory](./openclaw-memory)**  
   Configure OpenClaw memory types (episodic, semantic, procedural), restructure workspace files, and validate that context persists across sessions.

10. **[Onboarding Agent with Memory](./openclaw-onboarding-agent)**  
    Build a company onboarding flow: an OpenClaw agent with memory that reads HR templates and sends personalized onboarding email from your assigned `CONTEXT-company.md`.

11. **[Cinema Seat Manager (TypeScript)](./seats-management-typescript)**  
    Command-line cinema seat reservation system using a 2D array, with reserve, count, and adjacent-seat search functions.

12. **[Music Playlist Player — Object modeling](./data-modeling-and-class-diagrams-music-player)**  
    UML-style class diagram for a music playlist player in diagram.4geeks.com: entities, data types, and relationships.

13. **[Digital Wallet — Object modeling](./data-modeling-and-class-diagrams-digital-wallet)**  
    UML-style class diagram for a digital wallet with transaction history in diagram.4geeks.com: entities, data types, and relationships.

14. **[Company Project Milestone: Coding Fundamentals (TypeScript)](./ai-eng-milestone-coding-fundamentals)**  
    `Milestone 2` — Programming fundamentals with TypeScript: small, testable modules focusing on control flow, arrays, objects, functions, and edge cases, using clean code practices.

15. **[AI Agent Rental Platform: Admin panel prototype](./agent-hub-ui-specs-and-prompts)**  
    Spec-driven frontend project for a multi-view admin panel: write `SPECS.md` first, then build dashboard and management views with HTML, Tailwind, and vanilla JavaScript interactions.

16. **[Talk to the Machine: Chat interface with a real AI API](./chat-interface-real-ai-api)**  
    Build a browser-based chat interface that calls the Groq API with `fetch`, sends full conversation history, and tracks cumulative token usage plus response metrics.

17. **[Wanderlust Explorer with React and Next.js](./nextjs-wanderlust-explorer)**  
    Next.js App Router app from scratch: experiences list with URL-driven search and filters, detail pages, favorites in state, and a local TypeScript dataset.

18. **[Building an Airbnb UI Clone with Next.js and React](./nextjs-airbnb-ui-clone)**  
    Next.js 16 + TypeScript + Tailwind UI clone from a product brief: layout, reusable components, and typed listing data.

19. **[Company Project Milestone: Talent Pipeline Tracker](./ai-eng-milestone-frontend-development)**  
    `Milestone 3` — Next.js App Router frontend for the recruitment API: candidate list and detail, filters and search, notes CRUD, register and edit forms, async UI states, and TypeScript types aligned with `CONTEXT-company.md`.

20. **[Company financial dashboard context project](./company-financial-dashboard-context-project)**  
    Module project focused on repository stewardship: fork an existing full-stack repo, validate AI-generated project understanding, define and test actionable rules under `.agents/rules`, and generate a `memory-bank` with product, stack, and current status.

21. **[Company financial dashboard specs project](./company-financial-dashboard-specs-project)**  
    Spec-first assignment on the existing financial dashboard repo: TypeScript types aligned with `/docs`, `components.md`, and a data-contract README for a date range filter, anomaly alerts table, and B2B vs B2C revenue comparison—no React implementation.

22. **[Company financial dashboard skills project](./company-financial-dashboard-skills-project)**  
    Continue on the same financial dashboard repo: apply agent skills (`accessibility`, `vercel-react-best-practices`), explore `skills.sh` with `npx skills find`, author a custom skill under `.skills/`, and update the memory bank—targeted improvements, not a full rebuild.

23. **[Milestone 4 — AI-driven Engineering](./ai-eng-milestone-ai-driven-engineering)**  
    `Milestone 4` — Monorepo layout: public Next.js site, internal backoffice, services/APIs, and integration of prior milestones with an AI-assisted delivery workflow.

24. **[Backend Architecture Proposal](./ai-eng-architectural-proposal)**  
    Produce an architecture document and diagrams for extending the company system (services, data, risks, and trade-offs).

25. **[Voice to-do list with AI API](./voice-to-do-list-api)**  
    Build a voice-powered to-do flow that captures user input, integrates with an AI API, and transforms spoken requests into actionable task management behavior.

26. **[Incident Analyzer — Script and Control Panel](./ai-eng-company-incidents-file-analyzer)**  
    Python script to validate and summarize incident CSVs (sensitive data stays internal), then FastAPI + web UI to upload files, view summaries, and export results.

27. **[AI basic Inventory Agent Loop](./ai-basic-inventory-agent-loop)**  
    Build a basic FastAPI inventory API plus a Python AI agent loop that uses API endpoints as tools, logs each interaction to CSV, and supports natural-language stock operations.

28. **[Supplier Directory — Lightweight Storage API](./ai-eng-supplier-directory)**  
    FastAPI + TinyDB + Pydantic supplier API: seeded data from `CONTEXT`, validation, CRUD, and filter endpoints (by country and category) with rate-change timestamps.

29. **[Securing the API: Authentication and Route Restriction in FastAPI](./ai-eng-user-authentication-api)**  
    JWT-based auth on the supplier API: register, login, protected routes, password hashing, and ownership checks.

30. **[Connecting the Lock: Authentication Flows in the Frontend](./ai-eng-user-authentication-flows)**  
    Frontend flows against the secured API: login, register, session handling, and protected views.

31. **[The Missing Piece: Password Reset Flow](./ai-eng-user-authentication-restore)**  
    End-to-end password reset: secure tokens, email or dev stub, and UI/API alignment.

32. **[Building Bullet-Proof Applications](./ai-eng-building-bullet-proof-applications)**  
    Add a comprehensive unit-test suite to the authentication API: token logic, validation edge cases, and endpoint behavior without testing framework plumbing.

33. **[Centralized Incident Manager](./ai-eng-centralized-incident-manager)**  
    Integrate a real-time incident manager into the company monorepo: log, query, and track incidents from the browser using your assigned `CONTEXT-company.md`.

34. **[Error Handling](./ai-eng-error-handling)**  
    Audit and fix error handling across the monorepo: API failures, loading states, user-facing messages, and script crash output before the next milestone adds complexity.

35. **[EduTrack Data Audit](./edutrack-data-audit-sql)**  
    SQL audit on a single-table enrollments dataset: data-quality checks, aggregations, and written findings for an operations lead.

36. **[EduTrack Data Audit — Related Tables](./edutrack-data-audit-sql-related-tables)**  
    Multi-table SQL on a normalized EduTrack schema: JOINs, cross-table metrics, and answers that require relating students, courses, and enrollments.

37. **[Company Project Milestone: Backend — Inventory Management](./ai-eng-milestone-backend-development)**  
    `Milestone 5` (backend) — FastAPI + SQLModel inventory API on Supabase: dual-database setup, inbound/outbound orders, and business rules from `CONTEXT-company.md`.

38. **[Company Project Milestone: Backoffice — Inventory Management](./ai-eng-inventory-management-backoffice)**  
    `Milestone 5` (frontend) — Backoffice UI for inventory operations: lists, forms, and states wired to the Milestone 5 backend API.

39. **[Launch Ready: Containerized MVP from Scratch](./launch-ready-containerized-mvp)**  
    Standalone module: Dockerize a small AI-generated MVP with Dockerfile, Compose, and reproducible local runs.

40. **[Company Monorepo Containerization](./ai-eng-container-project)**  
    Containerize the company monorepo: multi-service `docker-compose.yml`, environment configuration, and production-ready local orchestration.

41. **[Frontend Performance Audit](./ai-eng-performance-web-vitals)**  
    Lighthouse audit of corporate site and backoffice, reusable components/hooks refactor, and before/after performance report with Core Web Vitals fixes.

42. **[Backend Serialization Audit](./ai-eng-performance-serialization)**  
    Endpoint-by-endpoint serialization audit on the monorepo API: DTOs, payload shaping, and security fixes before scale.

43. **[Performance Optimisation: Caching](./ai-eng-performance-caching)**  
    Profile frontend and API hot paths, implement justified caching (TTL, `useMemo`, FastAPI cache), and document trade-offs in a technical report.

44. **[Company's Telemetry plan design](./ai-eng-telemetry-plan)**  
    Design `telemetry-plan.md` and `event-schemas.json` from inventory KPIs in `CONTEXT-company.md` before any instrumentation code.

45. **[Company's Telemetry — Frontend capture](./ai-eng-telemetry-capture)**  
    Next.js `TelemetryService`: queue, batch/debounce, `sendBeacon`, retries, and a single `track()` API posting to `POST /telemetry/events`.

46. **[Company's Telemetry — Storage](./ai-eng-telemetry-storage)**  
    Persist batched telemetry in Supabase/PostgreSQL with per-event validation, partial batch acceptance, and unchanged frontend contract.

47. **[Company's Telemetry — Report](./ai-eng-telemetry-report)**  
    Pandas pipeline plus `GET /telemetry/report` with grouped metrics, 60s response cache, and actionable inventory/usage summaries.

48. **[Designing a Data Pipeline: From Raw Data to Reliable Insights](./designing-data-pipeline)**  
    Standalone ETL design exercise for Veridian Logistics: analyze nightly CSV exports with updates-as-inserts, document deduplication and idempotency, and produce `PIPELINE_DESIGN.md` — no orchestration code.

49. **[Milestone 6 — Company's Data Pipeline Design (1/3)](./ai-eng-milestone-data-pipeline-design)**  
    `Milestone 6` (design) — Document a production-ready telemetry pipeline in the company monorepo: current state, ETL flow diagram, idempotency, execution log, and Prefect mapping before writing code.

50. **[Milestone 6 — Implementing a Resilient Data Pipeline (2/3)](./ai-eng-milestone-data-pipeline-build)**  
    `Milestone 6` (build) — Implement Prefect extract-transform-load flows in the monorepo with retries, idempotent loads, scheduled Docker deployment, and pipeline status/trigger API endpoints.

51. **[Milestone 6 — Company's Data Pipeline Enhancement: Subflows and Tests (3/3)](./ai-eng-milestone-data-pipeline-enhancement)**  
    `Milestone 6` (enhancement) — Refactor the pipeline into reusable subflows, add isolated unit tests for transformation tasks, and complete the production Docker deployment with Prefect Cloud verification.

52. **[Background Processes](./ai-eng-cronjobs)**  
    Nightly telemetry export cronjob in the company monorepo: independent CLI script, `job_runs` state machine, distributed lock, idempotent CSV export, pipeline subprocess trigger, and `TARGET_DATE` override for testing.

53. **[Branch Queue — Tagged Service Queue](./branch-queue)**  
    Terminal Python queue manager for a bank branch: one deque per service type, global ticket counter, CLI menu, and design notes on per-service queues vs a shared list — stdlib only.

54. **[Triage Queue — Priority Queue Manager](./triage-queue)**  
    Terminal Python priority queue for an emergency unit: triage levels 1–3 with FIFO within level, five core operations, CLI menu, and data-structure design notes — stdlib only.

55. **[Message Queues and Async Tasks](./ai-eng-message-queue)**  
    Decouple heavy API work with Redis and Celery in the company monorepo: `202` + `task_id`, `GET /tasks/{task_id}`, retries with backoff, Dead Letter Queue, separate worker process, and Flower monitoring.

---

Each project has detailed instructions in its folder (`README.md` and, if present, `README.es.md`). To get started, open the project folder and follow the README.
