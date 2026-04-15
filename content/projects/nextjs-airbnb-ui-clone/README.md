# Building an Airbnb UI Clone with Next.js and React

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/nextjs-airbnb-clone/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A product design studio has just won a contract to rebuild the front end of a vacation rental platform. Before writing any custom design system, they want to validate the component architecture by cloning a well-known, production-grade interface: Airbnb. This way, the team learns what components are needed, what data each one requires, and how they connect across different views.

You have been brought in as a junior front-end engineer. Your job is to implement **three views** of the Airbnb experience in Next.js using React components: the **Home page**, the **Catalog (search results)** page, and a **Room detail** page. You will use vision prompting to convert screenshots into component specifications, and then implement those specs.

The studio's tech lead has sent you a short brief:

> #### Product brief
>
> - The implementation must be **mobile-first**. Design for a 375px viewport first; adjust for desktop at 768px and above.
> - Before writing any code, create a `context.md` file at the root of your repository. This file should describe the interface you are going to build in your own words: what each page contains, what the main components are, who the user is, and what they are trying to accomplish. Think of it as the mini-brief you would write before starting a real project.
> - Use vision prompting — attach a screenshot of the original Airbnb interface to your AI coding agent to generate a component specification, then use that spec to guide your implementation.
> - Keep components small and focused. One responsibility per component.
> - All navigation between the three pages must work without full page reloads.

This is exactly the kind of task you will encounter in your first job: a real interface to replicate, a real framework to use, and the responsibility to figure out how to structure it yourself. Start from what you can see, reason about what each piece does, and build it component by component.

---

## 🌱 How to Start the Project

There is no starter template for this project. Your first task is to ask your AI coding agent to scaffold the project for you.

Use a prompt similar to this one:

> "Set up a new Next.js 16 project with TypeScript, Tailwind CSS, and the App Router. Use `npx create-next-app` with the appropriate flags. Name the project `airbnb-clone`. Organize the folder structure with a `/components` folder for reusable UI pieces."

Once the agent generates the setup commands, review them, run them in your terminal, and make sure the dev server starts correctly before writing any component.

Then:

1. Create your own GitHub repository.
2. Initialize git inside the project folder and push your initial commit.
3. Need a refresher on project setup? [Read this guide](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### 0 — Before You Write Code

- [ ] Create a `context.md` file at the root of your project. It must include:
  - [ ] A description of the three pages you will build and what each one shows.
  - [ ] A list of the main components you identify in each view (use Airbnb.com as reference).
  - [ ] A short paragraph describing the user and what they are trying to accomplish on this platform.

### 1 — Project Setup

- [ ] Ask your AI coding agent to scaffold a Next.js 16 project with TypeScript, Tailwind CSS, and the App Router using `create-next-app`.
- [ ] Review the generated commands before running them and confirm the dev server starts correctly.
- [ ] Organize your folders: `/app` for routes, `/components` for reusable UI pieces, `/types` for TypeScript interfaces.
- [ ] Use Tailwind CSS for all styling.

### 2 — Vision Prompting Workflow

- [ ] Take a screenshot of each of the three Airbnb pages on a **mobile viewport (375px)**.
- [ ] Attach each screenshot to your AI coding agent and prompt it to generate a written component specification. Your prompt should ask the model to identify: component names, their props, and their layout relationship within the page.
- [ ] Document each generated spec as a comment in the file or in your `context.md` before you start coding that view.

⚠️ **IMPORTANT:** Do not use any pre-built UI component library (no shadcn, no MUI, no Ant Design, no Chakra). Use Tailwind utility classes and your own components only.

### 3 — Home Page (`/`)

- [ ] Implement the top navigation bar: logo, search bar input, and user menu icons.
- [ ] The search bar must use `useState` to track the typed value and filter the visible listing cards in real time as the user types. The list of cards is your local state — update it on every keystroke.
- [ ] Implement the horizontal category filter row below the navbar (icon + label per category: Beach, Mansions, Trending, etc.). Use `useState` to track the active category and highlight the selected one visually.
- [ ] Implement a responsive grid of listing cards. Each card must show: a photo placeholder, title, price per night, and a star rating.
- [ ] Use `useEffect` to simulate loading the listing data when the page mounts: start with an empty list, set a loading state to `true`, and after a short `setTimeout` (e.g. 1 second) set the data and mark loading as `false`. Show a loading indicator while the data is not yet available.
- [ ] The card grid must be a single column on mobile and expand to multiple columns on desktop.

### 4 — Catalog Page (`/catalog`)

- [ ] Implement the results header: number of results and a sort control (Ascending / Descending by price). Use `useState` to track the selected sort order and reorder the displayed cards accordingly.
- [ ] Reuse the listing card component from the Home page.
- [ ] Add a map area to the right of the card list (desktop) or below the cards (mobile). By default, render a styled placeholder — a gray box with the text "Map" is enough.
- [ ] **Optional challenge (only if you have completed all other requirements):** Replace the map placeholder with a real interactive map using a library like `react-leaflet` or the Google Maps JavaScript API. Pin each listing on the map using its coordinates.

### 5 — Room Detail Page (`/rooms/[id]`)

- [ ] Use `useEffect` to load the room data when the component mounts, using the `id` from the URL. Simulate the fetch with a `setTimeout` and show a loading state while the data is not yet available.
- [ ] Implement the photo gallery at the top. Use `useState` to track the currently displayed photo index and render Previous / Next buttons to cycle through a hardcoded array of photo placeholders.
- [ ] Implement the listing header: title, star rating, number of reviews, and location.
- [ ] Implement the host info row: avatar placeholder, host name, and years hosting.
- [ ] Implement the amenities section as a grid of icon + label pairs.
- [ ] Implement the booking card: price per night, a guest counter (use `useState` to increase or decrease the number of guests within a min/max range), and a CTA button.
- [ ] **Optional challenge (only if you have completed all other requirements):** Add functional check-in / check-out date fields using a date picker library of your choice and compute the total price based on the number of nights selected.

### 6 — Navigation

- [ ] Clicking a listing card in the Home or Catalog page must navigate to the Room Detail page.
- [ ] Use Next.js `<Link>` for all navigation between pages.
- [ ] Include a back button or breadcrumb in the Room Detail page that returns to the Catalog.

⚠️ **IMPORTANT:** Never use a plain `<a href="...">` tag for internal navigation in a Next.js app.

### 7 — Code Quality

- [ ] Each component lives in its own file inside `/components`.
- [ ] No component exceeds ~80 lines of JSX + logic. If it does, split it.
- [ ] All components are defined as `const` functional components — no class components.

---

## ✅ What We Will Evaluate

- [ ] A `context.md` file exists at the root and contains a clear description of the interface, its components, and its user.
- [ ] The project was scaffolded with Next.js 16, TypeScript, Tailwind CSS, and the App Router (no starter template used).
- [ ] Three routes are implemented and navigable: `/`, `/catalog`, and `/rooms/[id]`.
- [ ] All internal navigation uses `<Link>` — no full page reloads between views.
- [ ] The layout is mobile-first: the 375px viewport is correct before any desktop breakpoint is applied.
- [ ] The listing card component is reused across the Home and Catalog pages.
- [ ] `useState` is used in at least three distinct cases: search filtering, active category, sort order, guest counter, or photo gallery index.
- [ ] `useEffect` is used to simulate data loading on mount in at least two pages, with a visible loading state while data is not available.
- [ ] The Room Detail page includes all five sections: photo gallery (with navigation), listing header, host info, amenities, and booking card.
- [ ] Components are split into individual files, each with a single responsibility.
- [ ] No class components — all components are functional and defined with `const`.
- [ ] TypeScript types or interfaces are defined for the main data shapes (listing, room).
- [ ] Tailwind utility classes are used for all styling — no inline `style={{}}` objects.
- [ ] The vision-to-spec workflow is visible: component specs derived from screenshots are documented in `context.md` or in code comments.

> **Note:** The optional challenges (real map, functional date picker) are not part of the base evaluation. They are there for students who finish early and want to go further.

---

## 📦 How to Submit

Push your work to your GitHub repository and share the link with your instructor following their instructions. Make sure the repository is public and that `context.md` is present at the root.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/nextjs-airbnb-clone/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
