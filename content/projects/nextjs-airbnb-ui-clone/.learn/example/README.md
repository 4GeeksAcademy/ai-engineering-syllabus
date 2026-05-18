> **In-class example for instructors.** Use this scenario to introduce Next.js App Router, React hooks, mobile-first Tailwind, and vision prompting in a ~1–2 hour session. This file is a teaching aid with a *different domain* than the assigned project. Do not share this with students as their project brief.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

# Car Rental UI — Next.js & React In-Class Example

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A car rental agency wants a modern, mobile-first interface where users can browse available cars, see search results, and view the detail page for a specific vehicle. The tech lead has defined three pages and a set of components to implement.

> #### Product brief
>
> Build three views of a car rental experience in Next.js using React components:
> - **Home (`/`)** — search bar + vehicle type filter chips + rental card grid
> - **Fleet (`/fleet`)** — sorted list of available cars + a map placeholder
> - **Car Detail (`/cars/[id]`)** — photo gallery, car specs, booking widget
>
> The implementation must be **mobile-first** (375px first, desktop at 768px+). No pre-built component libraries — Tailwind utility classes only.

---

## Pages & Components

### Home Page (`/`)

| Component | What it does | Hook used |
|-----------|-------------|-----------|
| `Navbar` | Logo + search input + user icon | — |
| `SearchBar` | Controlled text input that filters cards in real time | `useState` |
| `CategoryFilter` | Horizontal row of chips: Economy, SUV, Electric, Luxury | `useState` (active category) |
| `CarCard` | Photo placeholder, model name, price/day, star rating | — |
| `CarGrid` | Responsive grid of `CarCard` (1 col → multi col) | `useEffect` (simulate data load) |

### Fleet Page (`/fleet`)

| Component | What it does | Hook used |
|-----------|-------------|-----------|
| `ResultsHeader` | "X cars available" + sort toggle (Asc/Desc by price) | `useState` |
| `CarCard` | Reused from Home | — |
| `MapPlaceholder` | Gray box with "Map" text (right on desktop, below on mobile) | — |

### Car Detail Page (`/cars/[id]`)

| Component | What it does | Hook used |
|-----------|-------------|-----------|
| `PhotoGallery` | Array of photo placeholders + Prev/Next buttons | `useState` (photo index) |
| `CarHeader` | Model, year, rating, number of reviews |  — |
| `SpecsGrid` | Seats, transmission, fuel type, doors | — |
| `BookingCard` | Price/day + day counter (min 1, max 30) + CTA button | `useState` (days) |

---

## Checklist

### 0 — Before Writing Code

- [ ] Create `context.md` at the project root describing each page, its main components, and the target user

### 1 — Project Setup

- [ ] Scaffold with `npx create-next-app` (TypeScript + Tailwind + App Router)
- [ ] Folder structure: `/app` for routes, `/components` for reusable UI, `/types` for TypeScript interfaces

### 2 — Vision Prompting Workflow

- [ ] Take a screenshot of any real car rental site (e.g. Hertz, Enterprise) at 375px viewport
- [ ] Attach the screenshot to your AI coding agent and prompt it to generate a component spec
- [ ] Document the generated spec in `context.md` before coding that view

### 3 — Implementation

- [ ] Home: `SearchBar` filters cards in real time using `useState`; `CategoryFilter` highlights the active chip; `CarGrid` loads data with `useEffect` + loading state
- [ ] Fleet: `ResultsHeader` with sort toggle (Asc/Desc price) using `useState`; reuse `CarCard`; `MapPlaceholder`
- [ ] Car Detail: `PhotoGallery` with `useState` index; `BookingCard` with day counter using `useState`; data loaded with `useEffect`

### 4 — Navigation & Quality

- [ ] Clicking a `CarCard` navigates to `/cars/[id]` using Next.js `<Link>`
- [ ] Car Detail has a back button that returns to `/fleet`
- [ ] No `<a href="...">` tags for internal navigation
- [ ] All components are `const` functional components — no class components
- [ ] TypeScript interfaces defined for the `Car` data shape

⚠️ **IMPORTANT:** No pre-built component libraries (no shadcn, MUI, Chakra). Tailwind classes only.

---

## Discussion Questions

1. The `SearchBar` filters cards using `useState`. What would need to change if the search term had to survive a page refresh (e.g. shared via URL)? What Next.js API would you use?
2. Why does Next.js recommend `<Link>` over `<a href>` for internal navigation? What happens under the hood when you use `<Link>`?
3. The `useEffect` in `CarGrid` simulates a data fetch with `setTimeout`. What would you change to replace it with a real API call, and what edge cases (loading, error, empty state) would you need to handle?
