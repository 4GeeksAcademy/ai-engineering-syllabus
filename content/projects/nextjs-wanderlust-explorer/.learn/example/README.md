> **In-class example for instructors.** Use this scenario to introduce URL-driven state, custom hooks, `useSearchParams`, and multi-page Next.js apps in a ~1–2 hour session. This file is a teaching aid with a *different domain* than the assigned project. Do not share this with students as their project brief.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

# Recipe Explorer — Next.js In-Class Example

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A food blog wants a recipe discovery app where users can search and filter recipes, save their favorites, and view a detail page for any recipe. The PM has sent the following spec:

> #### Pages required
>
> - **`/`** — Home: hero with a CTA button that navigates to `/recipes`
> - **`/recipes`** — Explorer: recipe card grid with a search bar and two filters (cuisine and difficulty). Search and active filters must be reflected in the URL as query params and must pre-fill the inputs on load.
> - **`/recipes/[id]`** — Detail: full recipe information fetched from the local dataset by ID
> - **`/saved`** — Saved Recipes: list of recipes the user has bookmarked (stored in component state)
> - **`/profile`** — Profile: static page with a mock user and a count of saved recipes
>
> #### Dataset
>
> Use an AI assistant to generate an array of **30 recipe objects** saved as `src/data/recipes.ts`. Each recipe must have: `id`, `title`, `description`, `cuisine` (one of: Italian, Mexican, Japanese, Indian, American), `difficulty` (Easy, Medium, Hard), `cookTimeMinutes`, `rating`, and `imageUrl`.
>
> #### Search behavior
>
> Search filters recipes whose `title` matches the search term using a case-insensitive regex (`new RegExp(term, 'i')`). Cuisine and difficulty filters stack with search.

---

## Pages & Key Components

| Page | Key components | Hooks |
|------|---------------|-------|
| Home `/` | `Hero`, `Navbar` | — |
| Explorer `/recipes` | `SearchBar`, `FilterBar`, `RecipeCard`, `RecipeGrid` | `useState`, `useEffect`, `useSearchParams` |
| Detail `/recipes/[id]` | `RecipeHeader`, `IngredientsList`, `StepsList` | `useEffect` (load by ID) |
| Saved `/saved` | `RecipeCard` (reused) | `useState` (favorites list) |
| Profile `/profile` | `ProfileCard` | — |

---

## Checklist

### Setup & Dataset

- [ ] Scaffold with `npx create-next-app` (TypeScript + Tailwind + App Router)
- [ ] Generate 30 recipe objects using an AI assistant and save as `src/data/recipes.ts`
- [ ] Define a TypeScript `interface Recipe` and use it throughout the project

### Pages & Routing

- [ ] Create all 5 pages: `/`, `/recipes`, `/recipes/[id]`, `/saved`, `/profile`
- [ ] All navigation uses Next.js `<Link>` — no `<a href>` for internal links
- [ ] `Navbar` is present on all pages and highlights the active route using `usePathname`

### Search & Filters

- [ ] `SearchBar` filters recipes by title using a case-insensitive regex
- [ ] `FilterBar` has a cuisine dropdown and a difficulty dropdown
- [ ] Active search term and filters are stored as **URL query params** using `useSearchParams`
- [ ] On page load, inputs are pre-filled from the URL and results are already filtered
- [ ] The grid shows a **"No recipes found"** message when filters return zero results

### Favorites

- [ ] Each `RecipeCard` has a bookmark icon that toggles the recipe in/out of saved list
- [ ] The saved list is managed with `useState` at a shared level and passed via props
- [ ] `/saved` shows only bookmarked recipes

### Custom Hook

- [ ] Create a `useRecipes` custom hook that encapsulates filtering logic (search + cuisine + difficulty)
- [ ] Use `useEffect` in at least one component with a correct dependency array

### Code Quality

- [ ] All components are `const` functional — no class components
- [ ] No inline `style={{}}` — Tailwind utility classes only
- [ ] TypeScript types are defined and used consistently

⚠️ **IMPORTANT:** No external state management (Redux, Zustand). State lives in `useState` and props only.

---

## Discussion Questions

1. Why store the search term and filters in the URL instead of `useState`? What does a user gain when filters live in query params?
2. The `useRecipes` hook receives `search`, `cuisine`, and `difficulty` as parameters and returns the filtered list. What are the advantages of extracting this logic into a custom hook instead of writing it directly inside the component?
3. Currently, saved recipes are lost on page refresh because they live in `useState`. How would you persist them using `localStorage`? What React pattern would you use to load from `localStorage` on mount and write on every change?
