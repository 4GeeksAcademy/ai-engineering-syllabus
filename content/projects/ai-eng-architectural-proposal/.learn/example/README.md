# Recipe Sharing Platform — Backend Architecture Proposal (In-Class Example)

> **Instructor note:** This is a simplified in-class example for the "Backend Architecture Proposal" project. Use this scenario to practice writing a technical architecture document before writing any code — completable in 1–2 hours. The original project applies the same concepts to a student's own company monorepo accumulated over several milestones.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


You've just joined the backend team at **Dishcraft**, a startup building an online recipe-sharing platform. Users can publish their own recipes, browse by category, leave ratings, and save favorites.

Before anyone writes a line of code, the CTO sent this message:

> *"I need a short architecture document first. Tell me how you'd organize the backend, which pattern you'd use and why, and how the frontend and backend would communicate. Don't start coding — just write the document. A Markdown file is fine."*

Your deliverable is `ARCHITECTURE_PROPOSAL.md` inside the project's `/docs` folder.

---

## What Makes a Good Architecture Document?

An architecture document is **documented technical reasoning** — not a list of technologies. It explains *what*, *why*, and anticipates consequences. A good document allows any team member to understand the decisions without asking.

---

## What You Need to Do

Create `docs/ARCHITECTURE_PROPOSAL.md` covering the following sections:

### 1. Architectural Pattern

- [ ] Choose one pattern: **layered architecture (MVC)**, **serverless**, or another justified alternative.
- [ ] Write 2–3 sentences explaining *why* this pattern fits Dishcraft's needs — connect your reasoning to the nature of the product (recipe CRUD, user-generated content, ratings).
- [ ] Mention one trade-off: what does this pattern make harder?

### 2. Folder and Module Structure

Propose a folder structure for the FastAPI project. It must reflect the pattern you chose and the business domains of the product.

Example for a layered approach:

```
dishcraft-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── recipes/
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── users/
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── ratings/
│       ├── router.py
│       └── service.py
├── tests/
└── requirements.txt
```

- [ ] Include at least 3 domain folders (e.g., `recipes/`, `users/`, `ratings/`).
- [ ] For each folder, write one sentence describing its responsibility.

### 3. Router and Endpoint Organization

List the main API routes grouped by domain. No code needed — just describe them in a table:

| Domain | Method | Path | Description |
|--------|--------|------|-------------|
| Recipes | GET | `/recipes` | List all recipes (with filters) |
| Recipes | POST | `/recipes` | Create a new recipe |
| Recipes | GET | `/recipes/{id}` | Get one recipe by ID |
| Users | POST | `/users/register` | Register a new user |
| Users | POST | `/users/login` | Authenticate and get a token |
| Ratings | POST | `/recipes/{id}/ratings` | Submit a rating for a recipe |

- [ ] Add at least 2 more routes that make sense for this domain.
- [ ] Note which routes require authentication.

### 4. Frontend–Backend Separation

Describe how the Next.js frontend and the FastAPI backend will coexist. Address:

- [ ] Will they live in the same repo (monorepo) or separate repos? Justify your choice.
- [ ] How will the frontend call the API? (base URL, fetch vs. axios, environment variables)
- [ ] What CORS configuration is needed and why?

### 5. Risks and Points of Attention

- [ ] List **at least 2 risks** your team should know about before starting to code. Examples of useful risks: *"If all routes go in a single `main.py`, the file will become unmaintainable as the API grows"* or *"Without a shared naming convention for response schemas, the frontend team will encounter unexpected field names."*

---

## Acceptance Criteria

| # | Criterion |
|---|-----------|
| 1 | The architectural pattern is justified with arguments specific to Dishcraft — not generic preferences |
| 2 | The folder structure is consistent with the chosen pattern and separates domains clearly |
| 3 | All routers are grouped by domain, not dumped in a single file |
| 4 | The document addresses frontend–backend communication and CORS |
| 5 | At least 2 concrete risks are identified |

---

## Discussion Questions

1. A classmate chose serverless functions instead of a layered FastAPI app. What domains of this project might benefit from serverless? Which ones would be harder to implement that way?
2. Why does it matter that `router.py`, `service.py`, and `models.py` are kept separate within each domain folder? What happens when you put all of that in one file?
3. What would you add to the architecture document if the product needed to support real-time notifications (e.g., "your recipe got a new rating")?
