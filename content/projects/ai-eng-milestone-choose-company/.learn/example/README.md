# In-Class Example: Choose a Local Business to Digitize

> **Instructor note:** This is a classroom example to introduce the concepts of the *Milestone 0 — Choose Your Company* project using a simpler, more relatable domain. It covers the same skills (reading a context document, making a structured decision, proposing an AI agent idea, setting up a development environment) but with three small local businesses instead of a large corporate scenario. Use this as a 30–45 minute warm-up activity before students tackle the main milestone. Do NOT share this file with students before they attempt the main project.

---

## The activity

You are about to start a short project sprint. Over the next few sessions you will build a digital tool for a local business — and this decision shapes everything you build from here.

Below are three small business profiles. Each one has real operational problems that software and AI could solve. **Read all three carefully**, then pick the one that motivates you most.

---

## Business profiles

### Option A — The Neighborhood Bakery 🧁

**Overview:** A family-run bakery with one physical location. They make 15–20 types of products daily, take orders over WhatsApp, and track everything in a paper notebook.

**Current problems:**

| Department | Problem |
|---|---|
| Orders | Orders arrive via WhatsApp and are written by hand — easy to lose or forget |
| Inventory | Ingredients are tracked in a notebook; they often run out mid-day |
| Delivery | Delivery slots are written on sticky notes; coordination is chaotic |

**What they want to build:** An order management page, an ingredient stock tracker, and a daily production planner.

**A possible AI challenge:** An agent that reads the day's orders and automatically suggests how many units of each product to bake, based on historical order patterns.

---

### Option B — The Vintage Bookshop 📚

**Overview:** A second-hand bookshop with 2,000+ titles spread across shelves that are only partially catalogued. They sell in-store and occasionally online via a basic Instagram page.

**Current problems:**

| Department | Problem |
|---|---|
| Catalog | Most books are not in any digital system — staff rely on memory |
| Customer requests | Customers ask for specific titles; staff have no way to check availability quickly |
| Events | Monthly reading club events are announced on paper flyers only |

**What they want to build:** A searchable book catalog, a customer wish-list system, and an events page.

**A possible AI challenge:** An agent that scans a photo of a book cover and automatically fills in the title, author, and genre when adding it to the catalog.

---

### Option C — The Local Gym 🏋️

**Overview:** An independent gym with 150 active members. Memberships are managed via spreadsheet. Class schedules are posted on a whiteboard and updated manually.

**Current problems:**

| Department | Problem |
|---|---|
| Memberships | Staff manually check spreadsheets to verify if a member's plan is still active |
| Classes | No way for members to reserve a class — they just show up and hope there's space |
| Attendance | No attendance history — the gym can't tell which classes are most popular |

**What they want to build:** A membership tracker, a class reservation system, and an attendance dashboard.

**A possible AI challenge:** An agent that analyses attendance data from the past 3 months and recommends the optimal class schedule for the next month.

---

## What you need to do

- [ ] **Read all three profiles** carefully. Do not skim — the details matter for your design decisions later.
- [ ] **Choose one business** and record your decision in a `business-choice.md` file:
  - State clearly: which business you chose and why (3–5 sentences minimum).
  - Identify the **two departments** whose problems you find most interesting to solve.
  - Identify the **one feature** from the build list you are most looking forward to building.
- [ ] **Set up your environment:**
  - Clone the starter repo (your instructor will provide the link).
  - Open it in GitHub Codespaces or locally.
  - Confirm everything loads without errors.
- [ ] **Propose an AI Agent solution** for the AI challenge in your chosen business:
  - Describe in plain language: what the agent would do, what data it would need, and what it would produce or trigger.
  - No code needed — a short paragraph or bullet list is enough.
  - Add this to `business-choice.md` under a section titled `## My AI Agent Idea`.

---

## What we will evaluate

- [ ] `business-choice.md` exists and is committed.
- [ ] A specific business has been chosen with a justification of at least 3 sentences.
- [ ] Two departments are identified with a brief explanation of why they are interesting.
- [ ] One specific feature to build is named.
- [ ] The AI agent proposal describes what the agent does, what it needs, and what it produces.
- [ ] The development environment opens correctly with no errors.

---

## Discussion questions

1. You can only choose one business. What criteria did you use to make your decision — familiarity with the domain, the complexity of the problems, or something else? How might a different choice have changed the features you'd build?
2. Look at the AI agent challenge for your chosen business. What data would the agent need access to? Where does that data currently live (paper, spreadsheet, memory)? What would need to change before the agent could work?
3. All three businesses have a "staff relies on memory" problem. Why is this a common pattern in small businesses? What does it tell you about the most valuable thing a digital system can provide — beyond just automation?
