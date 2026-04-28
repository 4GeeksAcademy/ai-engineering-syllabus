# Wanderlust Explorer — Interactive React & Next.js App

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

Wanderlust Labs is a travel-tech startup building a platform where users can discover and save curated experiences around the world — from street-food tours in Bangkok to sailing trips in the Adriatic. Their product designer has already produced reference mockups (you'll find them in the brief below), and the engineering team needs a frontend developer to bring the MVP explorer to life.

You've been assigned to build the **experience explorer**: a multi-page React/Next.js application where users can browse, search, and filter experiences — all without reloading the page. The frontend lead handed you a Figma reference and a brief from the PM. Before writing a single component, spend some time finding 2–3 real interfaces you admire that match the expected feel: a clean discovery UI with cards, a search bar, and a sidebar or top filter bar. Use them to guide your design decisions and note them in your repo's README under a "Design References" section.

Your dataset will be 100 generated experiences. The PM wants the search and filters to live in the URL so that users can share links like `/experiences?search=sailing&category=adventure&destination=Croatia` and land on a pre-filtered view.

> Your PM, Lea Moreau, sent the following spec over Slack:
>
> #### Pages required
>
> - **`/`** — Home: hero section with a call-to-action button that navigates to `/experiences`
> - **`/experiences`** — Explorer: full list of experience cards with a search bar and at least two filters (category and destination). The search and active filters must be reflected in the URL as query parameters and must pre-fill the inputs on load.
> - **`/experiences/[id]`** — Detail: full information for one experience, fetched from the local dataset by ID
> - **`/favorites`** — Favorites: list of experiences the user has marked as favorite (stored in component state for now)
> - **`/profile`** — Profile: a static page with a mock user profile and a summary of their saved favorites count
>
> #### Search behavior
>
> The search should filter experiences whose title matches the search term. Use a case-insensitive regex for this — something like `/term/i`. The filter by category and destination should work independently and stack with the search.
>
> #### Dataset
>
> Use an AI coding assistant to generate an array of 100 experience objects. Each object should have at minimum: `id`, `title`, `description`, `category` (one of: Adventure, Culture, Food, Wellness, Nature), `destination` (city + country), `price`, `rating`, and `imageUrl` (any placeholder). Save it as a local TypeScript file.
>
> #### Favorites
>
> A heart icon on each card should toggle the experience in/out of the user's favorites list. Favorites are kept in a `useState` at the top level and passed down as props where needed. No persistence required yet.

This is the kind of feature that shows up in real product sprints: link-shareable filters, URL-driven state, and component composition. Build it like something you'd put in your portfolio — because you should.

---

## 🌱 How to Start the Project

This project starts from **scratch** — no template to fork. You'll create your own Next.js app from the ground up.

1. Create a new Next.js project using the official CLI (with TypeScript and the App Router):

   ```bash
   npx create-next-app@latest nextjs-wanderlust-explorer --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
   ```

2. Create a new **public repository** on your GitHub account named `nextjs-wanderlust-explorer`.

3. Connect your local project to that repo:

   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/nextjs-wanderlust-explorer.git
   git push -u origin main
   ```

4. Open the project in GitHub Codespaces or your local editor and start building.

> 📗 Need a refresher on the workflow? [How to start a coding project](https://4geeks.com/lesson/how-to-start-a-project)

---

## 💻 What You Need to Do

### 🗂️ Setup & Dataset

- [ ] Initialize the project from scratch with `create-next-app` (TypeScript + Tailwind + App Router)
- [ ] Use an AI coding assistant to generate an array of 100 experience objects and save it as `src/data/experiences.ts`
- [ ] Define a TypeScript `interface Experience` for the data shape and use it throughout the project
- [ ] Add a `## Design References` section to your `README.md` with links or screenshots of 2–3 real UIs that inspired your design

### 🏠 Pages & Routing

- [ ] Create a **Home page** (`/`) with a hero section and a button that navigates to `/experiences`
- [ ] Create an **Explorer page** (`/experiences`) with all 100 experience cards rendered in a grid
- [ ] Create a **Detail page** (`/experiences/[id]`) that reads the experience ID from the URL and displays the full card content
- [ ] Create a **Favorites page** (`/favorites`) that shows only the experiences the user has favorited
- [ ] Create a **Profile page** (`/profile`) with a mock user profile and the count of saved favorites

### 🔍 Search & Filters

- [ ] Add a **search bar** to the Explorer page that filters experiences by title
- [ ] Use a **case-insensitive regex** to match the search term against each experience's title (e.g. `new RegExp(term, 'i').test(experience.title)`)
- [ ] Add a **category filter** (dropdown or button group) using the five available categories
- [ ] Add a **destination filter** (dropdown or search) that filters by destination city or country
- [ ] All active filters and the search term must be stored as **URL query parameters** using `useSearchParams` and `usePathname` from Next.js
- [ ] On page load, read the query params from the URL and **pre-fill** the search bar and filter inputs with their values

### ❤️ Favorites

- [ ] Add a heart icon (toggle) to each experience card
- [ ] Store the list of favorite IDs in a `useState` at a shared level and pass it down via props
- [ ] The heart icon must visually reflect whether the experience is in favorites or not

### 🧩 Components & Hooks

- [ ] Create at minimum: `ExperienceCard`, `SearchBar`, `FilterBar`, `Navbar`
- [ ] Use `useEffect` in at least one component (e.g. to sync the filtered results when query params change, or to update the document title on the detail page)
- [ ] Create at least one **custom hook** (e.g. `useExperiences` or `useFilters`) that encapsulates filtering logic

### 🎨 UI & Quality

- [ ] The app must be **responsive** (mobile + desktop)
- [ ] The Explorer grid must show a **"No results found"** message when filters produce zero matches
- [ ] The Navbar must be present on all pages and show active link styles using `usePathname`

⚠️ **IMPORTANT:** Do not use any external state management library (Redux, Zustand, etc.). All state must live in React's built-in `useState` and be passed via props or custom hooks.

---

## ✅ What We Will Evaluate

- [ ] The app has at least 5 distinct pages with working client-side navigation (no full-page reloads between routes)
- [ ] Search filters results by title using a regex match
- [ ] Category and destination filters work independently and combine correctly with the search term
- [ ] Active filters and search term are reflected in the URL as query params
- [ ] On page load with existing query params, inputs are pre-filled and results are already filtered
- [ ] `useEffect` is used correctly with appropriate dependency arrays (no infinite loops, no missing dependencies)
- [ ] `useState` is used to manage favorites and passed correctly as props
- [ ] At least one custom hook exists and encapsulates meaningful logic
- [ ] Components are split logically — no single file contains the entire app
- [ ] TypeScript types/interfaces are defined and used consistently
- [ ] The app is responsive and visually coherent across pages
- [ ] Design references are documented in the README

> **Note:** Persistence of favorites across page refreshes is **not** evaluated. `localStorage` is out of scope for this project.

---

## 📦 How to Submit

1. Make sure all your work is committed and pushed to your GitHub repository.
2. Share the repository URL with your instructor following their submission instructions.
3. If you've deployed the app (e.g. on Vercel), include the live URL in your repository description — it's a bonus, not a requirement.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
