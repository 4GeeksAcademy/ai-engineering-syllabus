# Library Admin Panel — In-Class Example

> **Instructor note:** This is a simplified in-class example for the "Agent Hub UI Specs and Prompts" project. Use this scenario to introduce the spec-first workflow and core UI interactions (sidebar, modals, dropdowns, dark mode) in 1–2 hours. The original project covers the same technical concepts in a larger, more complex domain.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A small public library called **Bookshelf Community Library** needs a basic admin panel to manage its catalog and loan activity. You've been brought in to prototype it. Before touching any HTML, you must write a specification document (`SPECS.md`) that describes what you'll build — precise enough that another developer (or an AI agent) could implement it without asking questions.

The librarian has shared this brief:

> *"I need to see the books we have, who has borrowed them, and flag overdue loans. Keep it simple. I use a laptop, so desktop-first is fine."*

---

## Sections to Build

The panel must have **three sections** accessible from a persistent left sidebar:

### 1. Books Catalog

A table listing all books: title, author, genre, and availability status (Available / On Loan / Overdue). Each row has a `⋮` action dropdown with two options: **"View detail"** (opens a modal with full book info) and **"Remove"**.

### 2. Active Loans

A table showing current loans: borrower name, book title, loan date, and due date. Overdue loans are highlighted with a color-coded badge. Each row has a `⋮` dropdown with **"View detail"** and **"Mark as returned"**.

### 3. Members

A list of registered library members: name, email, and how many active loans they currently have. Each member has a `⋮` dropdown with **"View detail"** (opens a modal with full member record).

---

## What You Need to Do

### Step 1 — Write the specification first

- [ ] Create `SPECS.md` at the root of the project **before** writing any HTML.
- [ ] `SPECS.md` must include:
  - [ ] A one-paragraph product description (what the panel is, who uses it).
  - [ ] Tech stack and constraints: HTML, Tailwind CSS via CDN, vanilla JS only — no frameworks, no build tools.
  - [ ] **At least 2 specifications per section** — each naming a component, describing its contents, and defining its behavior.
  - [ ] A component inventory listing reusable elements: sidebar, table row, action dropdown, modal, status badge, dark mode toggle.
  - [ ] At least 4 acceptance criteria (one per interactive behavior).
- [ ] Commit `SPECS.md` before writing the first line of HTML.

> A good spec entry looks like this: *"Each row in the Books table has a `⋮` button. Clicking it opens a dropdown menu with 'View detail' and 'Remove'. The dropdown closes when the user clicks outside it."*

### Step 2 — Build the prototype

- [ ] Build the panel as a single `index.html` file.
- [ ] Use **Tailwind CSS via CDN** — no custom CSS files, no inline `style` attributes.
- [ ] Implement a persistent **sidebar** with navigation links to all three sections.

#### Books Catalog

- [ ] Table with at least 5 hardcoded books (title, author, genre, status badge).
- [ ] `⋮` action dropdown per row: "View detail" opens a modal; "Remove" is present but can be a no-op.
- [ ] Modal shows full book details and closes via a close button and backdrop click.

#### Active Loans

- [ ] Table with at least 4 hardcoded loans (borrower, book, loan date, due date).
- [ ] Overdue loans visually distinguished with a red badge.
- [ ] `⋮` dropdown per row: "View detail" and "Mark as returned" (no-op is fine).

#### Members

- [ ] List with at least 3 hardcoded members (name, email, active loans count).
- [ ] `⋮` dropdown per row: "View detail" opens a modal with the member's full record.

#### Global interactions

- [ ] **Dark/light mode toggle** in the top bar switches the full panel using Tailwind's `dark:` utilities.
- [ ] All dropdowns close when clicking outside.
- [ ] All modals close via close button and backdrop click.
- [ ] Active section is highlighted in the sidebar.

> **Important:** All interactivity must be vanilla JavaScript — no libraries, no frameworks.

---

## Acceptance Criteria

| # | Criterion |
|---|-----------|
| 1 | `SPECS.md` is committed before any HTML file (Git history verifiable) |
| 2 | All three sections are reachable from the sidebar |
| 3 | "View detail" opens a modal in at least two sections |
| 4 | All modals close via close button and backdrop click |
| 5 | Dark/light mode toggle switches the entire panel |
| 6 | All `⋮` dropdowns close on outside click |

---

## Tech Stack Reference

| Layer | Technology |
|-------|------------|
| Markup | HTML5 (semantic tags: `nav`, `main`, `section`, `table`) |
| Styling | Tailwind CSS via CDN |
| Interactivity | Vanilla JavaScript |
| Data | Hardcoded in HTML |

---

## Discussion Questions

1. Why is writing the specification before the HTML an advantage when working with an AI coding agent? What could go wrong if you skip it?
2. What is the relationship between the component inventory in `SPECS.md` and how you structure your JavaScript code?
3. If you needed to add a fourth section (e.g., "Late Fees"), what would you add to `SPECS.md` before touching the HTML? Write one specification entry as an example.
