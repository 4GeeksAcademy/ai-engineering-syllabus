# AI Engineering Projects

Repository of hands-on projects for the **AI Engineering** program at 4Geeks Academy. Each folder is a standalone project with its own README, evaluation criteria, and (when applicable) `learn.json` for the platform.

Projects follow a pedagogical order: from web fundamentals (HTML, CSS, SEO, accessibility) and Tailwind, through company milestones and collaboration, **OpenClaw agent setup and integrations**, then TypeScript and system design, followed by APIs, authentication, agents, and advanced milestones.

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

7. **[Cinema Seat Manager (TypeScript)](./seats-management-typescript)**  
   Command-line cinema seat reservation system using a 2D array, with reserve, count, and adjacent-seat search functions.

8. **[Music Playlist Player — Object modeling](./data-modeling-and-class-diagrams-music-player)**  
   UML-style class diagram for a music playlist player in diagram.4geeks.com: entities, data types, and relationships.

9. **[Digital Wallet — Object modeling](./data-modeling-and-class-diagrams-digital-wallet)**  
   UML-style class diagram for a digital wallet with transaction history in diagram.4geeks.com: entities, data types, and relationships.

10. **[Company Project Milestone: Coding Fundamentals (TypeScript)](./ai-eng-milestone-coding-fundamentals)**  
    `Milestone 2` — Programming fundamentals with TypeScript: small, testable modules focusing on control flow, arrays, objects, functions, and edge cases, using clean code practices.

11. **[AI Agent Rental Platform: Admin panel prototype](./agent-hub-ui-specs-and-prompts)**  
    Spec-driven frontend project for a multi-view admin panel: write `SPECS.md` first, then build dashboard and management views with HTML, Tailwind, and vanilla JavaScript interactions.

12. **[Talk to the Machine: Chat interface with a real AI API](./chat-interface-real-ai-api)**  
    Build a browser-based chat interface that calls the Groq API with `fetch`, sends full conversation history, and tracks cumulative token usage plus response metrics.

13. **[Wanderlust Explorer with React and Next.js](./nextjs-wanderlust-explorer)**  
    Next.js App Router app from scratch: experiences list with URL-driven search and filters, detail pages, favorites in state, and a local TypeScript dataset.

14. **[Building an Airbnb UI Clone with Next.js and React](./nextjs-airbnb-ui-clone)**  
    Next.js 16 + TypeScript + Tailwind UI clone from a product brief: layout, reusable components, and typed listing data.

15. **[Company Project Milestone: Talent Pipeline Tracker](./ai-eng-milestone-talent-pipeline-tracker)**  
    `Milestone 3` — Next.js App Router frontend for the recruitment API: candidate list and detail, filters and search, notes CRUD, register and edit forms, async UI states, and TypeScript types aligned with CONTEXT-company.md.

16. **[Company financial dashboard context project](./company-financial-dashboard-context-project)**  
    Module project focused on repository stewardship: fork an existing full-stack repo, validate AI-generated project understanding, define and test actionable rules under `.agents/rules`, and generate a `memory-bank` with product, stack, and current status.

17. **[Company financial dashboard specs project](./company-financial-dashboard-specs-project)**  
    Spec-first assignment on the existing financial dashboard repo: TypeScript types aligned with `/docs`, `components.md`, and a data-contract README for a date range filter, anomaly alerts table, and B2B vs B2C revenue comparison—no React implementation.

18. **[Company financial dashboard skills project](./company-financial-dashboard-skills-project)**  
    Continue on the same financial dashboard repo: apply agent skills (`accessibility`, `vercel-react-best-practices`), explore `skills.sh` with `npx skills find`, author a custom skill under `.skills/`, and update the memory bank—targeted improvements, not a full rebuild.

19. **[Voice to-do list with AI API](./voice-to-do-list-api)**  
    Build a voice-powered to-do flow that captures user input, integrates with an AI API, and transforms spoken requests into actionable task management behavior.

20. **[Supplier Directory — Lightweight Storage API](./ai-eng-supplier-directory)**  
    FastAPI + TinyDB + Pydantic supplier API: seeded data from `CONTEXT`, validation, CRUD, and filter endpoints (by country and category) with rate-change timestamps.

21. **[Securing the API: Authentication and Route Restriction in FastAPI](./ai-eng-user-authentication-api)**  
    JWT-based auth on the supplier API: register, login, protected routes, password hashing, and ownership checks.

22. **[Connecting the Lock: Authentication Flows in the Frontend](./ai-eng-user-authentication-flows)**  
    Frontend flows against the secured API: login, register, session handling, and protected views.

23. **[The Missing Piece: Password Reset Flow](./ai-eng-user-authentication-restore)**  
    End-to-end password reset: secure tokens, email or dev stub, and UI/API alignment.

24. **[Incident Analyzer — Script and Control Panel](./ai-eng-company-incidents-file-analyzer)**  
    Python script to validate and summarize incident CSVs (sensitive data stays internal), then FastAPI + web UI to upload files, view summaries, and export results.

25. **[AI basic Inventory Agent Loop](./ai-basic-inventory-agent-loop)**  
    Build a basic FastAPI inventory API plus a Python AI agent loop that uses API endpoints as tools, logs each interaction to CSV, and supports natural-language stock operations.

26. **[Backend Architecture Proposal](./ai-eng-architectural-proposal)**  
    Produce an architecture document and diagrams for extending the company system (services, data, risks, and trade-offs).

27. **[Milestone 4 — AI-driven Engineering](./ai-eng-ai-driven-engineering)**  
    `Milestone 4` — Monorepo layout: public Next.js site, internal backoffice, services/APIs, and integration of prior milestones with an AI-assisted delivery workflow.

---

Each project has detailed instructions in its folder (`README.md` and, if present, `README.es.md`). To get started, open the project folder and follow the README.
