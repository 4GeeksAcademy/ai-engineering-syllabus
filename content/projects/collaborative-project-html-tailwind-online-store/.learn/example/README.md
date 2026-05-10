# In-Class Example: Local Coffee Shop Website

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain is a neighborhood coffee shop website instead of a clothing brand online store — same HTML + Tailwind skills, Git collaboration workflow, and semantic structure, but with 3 views instead of 5.

## The Scenario

A local coffee shop wants a simple prototype website to showcase their menu and allow customers to place a pre-order. You are working in pairs: one person handles the Home and Menu views, the other handles the Pre-order form. You will use Git branches and pull requests to merge your work together at the end.

---

## Concepts Covered

| Concept | Where it appears |
|---|---|
| Semantic HTML | `<header>`, `<nav>`, `<main>`, `<section>`, `<form>` |
| Tailwind CSS utility classes | Layout, spacing, typography, responsive breakpoints |
| Responsive design | Mobile-first, `sm:` / `md:` / `lg:` prefixes |
| Schema.org structured data | `CafeOrCoffeeShop`, `MenuItem` on relevant pages |
| Git branching | One branch per view (`feature/home`, `feature/menu`, `feature/order`) |
| Pull requests | Open a PR per branch before merging to `main` |

> ⚠️ **Important:** Only use **HTML and Tailwind CSS**. Do not add React, JavaScript, or any other framework. Tell your AI copilot this restriction from the first message.

---

## Views to Build (3 total)

### 1) Home page (`index.html`)

- **Navbar** with: logo (text is fine), links to Menu and Pre-order
- **Hero section** with a welcoming headline and a call-to-action button linking to Menu
- **Two featured items** shown as cards (name, short description, price)
- **Footer** with: address, opening hours, and a link to the Pre-order page
- The navbar and footer must be copy-pasted consistently across all pages

### 2) Menu page (`menu.html`)

- Reuse navbar and footer
- A **category filter bar** with buttons for: Coffee, Tea, Food (purely visual — no JavaScript needed)
- A **grid of at least 8 items** (4×2), each card showing: item image (use a placeholder), name, and price

### 3) Pre-order form (`order.html`)

- Reuse navbar and footer
- A **form** collecting:
  - Customer name
  - Pickup time (a `<select>` with 3–4 time slots)
  - Item selection (at least 3 checkboxes)
  - Special instructions (`<textarea>`)
  - A "Place Order" submit button
- Use proper `<label>` elements linked to each input

---

## Git Workflow Checklist

- [ ] Partner A: create branch `feature/home` and build `index.html`
- [ ] Partner B: create branch `feature/menu` and build `menu.html`
- [ ] Either partner: create branch `feature/order` and build `order.html`
- [ ] Open a **pull request** for each branch — describe what the PR contains in the PR body
- [ ] Pull latest `main` before merging to reduce conflicts: `git pull origin main`
- [ ] Resolve any merge conflicts together before pushing
- [ ] Use clear commit messages: e.g., `"Add hero section to home page"`, `"Add menu grid with 8 items"`

---

## Evaluation Checklist

- [ ] All 3 pages use semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, `<form>`)
- [ ] Tailwind utility classes used consistently — no raw CSS files added
- [ ] Layout is readable on mobile and desktop (test by resizing the browser)
- [ ] Navbar and footer are identical across all 3 pages
- [ ] At least one Schema.org type added (e.g., `CafeOrCoffeeShop` on the home page, `MenuItem` on the menu page)
- [ ] Git history shows at least one branch and one PR per major view
- [ ] No work committed directly to `main`

---

## Discussion Questions

1. Why do we use `<nav>`, `<main>`, and `<section>` instead of just `<div>` everywhere? Who benefits from semantic HTML?
2. What is the purpose of adding Schema.org structured data to a coffee shop page — who reads it, and why does it matter?
3. If two teammates edit `index.html` at the same time on different branches, what happens when you try to merge? How do you resolve it?
