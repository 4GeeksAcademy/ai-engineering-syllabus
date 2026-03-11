# My first collaborative professional project

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/collaborative-project-html-tailwind-online-store/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)_.

**Before you start**:

> We need you! These exercises are built and maintained in collaboration with people like you. If you find a bug 🐞 or a typo, please contribute and/or report it.

<!-- endhide -->

---

## 🎯 Your challenge

You are working on a small development team at a consulting firm, and a new project has just landed: **a well-known French clothing brand** wants a **visual and functional prototype** for their upcoming online store.

The client has been clear about the requirements:

- **Solid SEO** (semantic structure, indexable content, best practices).
- **Modern**, consistent design.
- **Fully responsive**: mobile, tablet, and desktop.

Before moving to full development, they need to see a prototype that includes **at least 5 main views**:

1. **Home**
2. **Catalog**
3. **Product view**
4. **Cart**
5. **Payment form (checkout)**

Time to shine. The consulting firm put together a team for the project and assigned you and one other person to get it done.

### Specifications by view

Your _project manager_ has shared a document with the minimum structure for each view to avoid oversights and ensure the prototype meets the client’s expectations.

> #### 1) Home page
>
> - **Top bar (navbar)** with:
>   - Logo
>   - Search bar
>   - User account menu
> - **Hero section** highlighting special products or brand campaigns.
> - Two sections with horizontal product lists (_cards_):
>   - **New arrivals**
>   - **Best sellers**
> - **Footer** with sections:
>   - **Categories:** footwear, shirts, pants, accessories
>   - **Legal:** terms and conditions, privacy policy, about the brand
>   - **Contact**
> - **The navbar and footer are reused** across all other views.
>
> #### 2) Catalog
>
> - Keeps **navbar and footer**.
> - Includes a **filter bar** before the list:
>   - Filter by **category**
>   - Filter by **size**
> - Product list in a **4×5 grid** (20 products visible as reference).
>
> #### 3) Product view
>
> - Two-column layout:
>   - **Left:** product image taking roughly **half the width**.
>   - **Right:** main product information:
>     - Name
>     - Code or reference
>     - Size
>     - Price
>     - Quantity selector
>     - **"Add to cart"** button
> - Below, a **detailed description** section:
>   - Materials
>   - Recommended use / scenarios for wearing the item
>
> #### 4) Cart
>
> - Full cart view (not a side panel).
> - List of added products with:
>   - Thumbnail
>   - Unit price
>   - Quantity
>   - Total per product
> - Summary box with:
>   - Subtotal
>   - Tax
>   - Total
>   - **"Purchase"** button
> - Add **3 sample products** to show the visual behavior.
>
> #### 5) Payment form (Checkout)
>
> Flow in **3 steps**:
>
> 1. **Personal details**
> 2. **Shipping address**
> 3. **Card payment** (card details)

Now it’s time to build a clear, consistent, and responsive prototype that shows the store’s potential and makes it easy for the client to approve. **Let’s get to it!** 😁

> **⚠️ IMPORTANT:** In this project we will only use **HTML and Tailwind CSS**. Make sure your AI Copilot **does not include more advanced technologies** (e.g., React). State this from the beginning.

---

## 🌱 How to start the project

Open the template repository using a provisioning tool such as [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or clone it locally:

```text
https://github.com/4GeeksAcademy/html-hello
```

Follow the steps in [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

💡 **Important:** Create a new repository on GitHub for your code, update the remote (`git remote set-url origin <your-new-url>`) and push your changes with `add`, `commit` and `push`.

---

## 💻 What you need to do

Develop the e-commerce prototype **as a team**, applying what you’ve learned: **semantic HTML**, **Tailwind**, **Schema.org**, responsive design, and **Git** (branches, commits, pull requests). Use AI step by step and keep the scope to HTML + Tailwind only.

**Views to implement (and link between them):**

- [ ] **Home** — navbar, Hero, “New arrivals” and “Best sellers” product lists, footer (navbar and footer reused on all pages).
- [ ] **Catalog** — navbar, filter bar (category, size), product grid (e.g. 4×5), footer.
- [ ] **Product view** — two columns (image + details: name, code, size, price, quantity, “Add to cart”), description section; navbar and footer.
- [ ] **Cart** — full-page cart: list of items (thumbnail, unit price, quantity, line total), summary (subtotal, tax, total), “Purchase” button; e.g. 3 sample products to show behavior; navbar and footer.
- [ ] **Payment form (checkout)** — 3 steps: (1) Personal details, (2) Shipping address, (3) Card payment; navbar and footer.

**Git and collaboration (Skill 5):**

- [ ] Use **one branch per view or feature** (e.g. `feature/home`, `feature/catalog`). Do not work directly on `main`.
- [ ] **Open a pull request (PR)** for each branch before merging into `main`. Describe what the PR contains.
- [ ] **Update your branch** with `main` (e.g. `git pull origin main`) before submitting the PR to reduce conflicts.
- [ ] **Resolve conflicts** together as a team; do not force-push or overwrite each other’s work without agreeing.
- [ ] **Commit often** with clear messages (e.g. “Add navbar and hero to home”, “Add catalog grid and filters”). Prefer one logical change per commit.

---

## ✅ What we will evaluate

- [ ] **Semantic HTML:** Correct structure and landmarks; meaningful tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<form>`, etc.) across all views.
- [ ] **Tailwind CSS:** Consistent use of utility classes; responsive breakpoints (mobile, tablet, desktop); no unrelated frameworks.
- [ ] **Layout and components:** Clear layout and grouping; navbar and footer reused across views; content matches the specifications per view.
- [ ] **Responsive design:** All five views usable on different screen sizes; no broken layout or horizontal scroll on small screens.
- [ ] **Schema.org:** Structured data (e.g. Product, Organization) where it makes sense (e.g. product or home page).
- [ ] **Git workflow:** Branches used for features/views; at least one PR per major part; meaningful commits; no long-term work directly on `main`.

Deliverable: **at least 5 HTML files** (one per view), linked to each other, plus shared styles (Tailwind and any extra CSS).

---

## 📦 How to submit this project

Follow the usual submission steps to push your repository to GitHub and share it according to your instructor’s instructions.

---

## Contributors

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/collaborative-project-html-tailwind-online-store/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
