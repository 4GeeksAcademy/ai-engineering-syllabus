# In-Class Example: Movie Collection Manager (TypeScript)

> **Instructor note:** This is a classroom example to introduce the concepts of the *Milestone 2 — Building Scripts to Automate Tasks* project using a simpler domain. It covers the same TypeScript skills (interfaces, filtering, sorting, linear search, binary search, aggregations, business validations, pure functions) but with a movie collection as the data model. Scope: 1–2 hour live session. Do NOT share this file with students before they attempt the main project.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A developer wants to build a personal movie collection manager. They have a list of movies stored as plain objects in TypeScript and need a set of reusable utility functions to filter, search, sort, and summarise the collection.

There is no database or API yet — this milestone is purely about the logic layer.

---

## Data model

Define the following interfaces in `src/types/models.ts`:

```typescript
type Genre = "action" | "comedy" | "drama" | "horror" | "sci-fi" | "documentary" | "animation";
type WatchStatus = "watched" | "watchlist" | "dropped";

interface Director {
  id: number;
  name: string;
  nationality: string;
}

interface Movie {
  id: number;
  title: string;
  year: number;           // 1888–current year
  genre: Genre;
  director: Director;
  rating: number;         // 0.0–10.0
  durationMinutes: number; // must be > 0
  status: WatchStatus;
}
```

### Sample data

Use this starter dataset in `src/data/movies.ts`:

```typescript
export const movies: Movie[] = [
  { id: 1,  title: "Inception",              year: 2010, genre: "sci-fi",      director: { id: 1, name: "Christopher Nolan",    nationality: "British"    }, rating: 8.8, durationMinutes: 148, status: "watched"   },
  { id: 2,  title: "The Dark Knight",        year: 2008, genre: "action",      director: { id: 1, name: "Christopher Nolan",    nationality: "British"    }, rating: 9.0, durationMinutes: 152, status: "watched"   },
  { id: 3,  title: "Parasite",               year: 2019, genre: "drama",       director: { id: 2, name: "Bong Joon-ho",         nationality: "Korean"     }, rating: 8.6, durationMinutes: 132, status: "watched"   },
  { id: 4,  title: "Spirited Away",          year: 2001, genre: "animation",   director: { id: 3, name: "Hayao Miyazaki",       nationality: "Japanese"   }, rating: 8.6, durationMinutes: 125, status: "watched"   },
  { id: 5,  title: "Get Out",                year: 2017, genre: "horror",      director: { id: 4, name: "Jordan Peele",         nationality: "American"   }, rating: 7.7, durationMinutes: 104, status: "watched"   },
  { id: 6,  title: "Everything Everywhere", year: 2022, genre: "sci-fi",      director: { id: 5, name: "Daniels",              nationality: "American"   }, rating: 7.8, durationMinutes: 139, status: "watchlist" },
  { id: 7,  title: "Knives Out",             year: 2019, genre: "comedy",      director: { id: 6, name: "Rian Johnson",         nationality: "American"   }, rating: 7.9, durationMinutes: 130, status: "watchlist" },
  { id: 8,  title: "Dune",                   year: 2021, genre: "sci-fi",      director: { id: 7, name: "Denis Villeneuve",     nationality: "Canadian"   }, rating: 8.0, durationMinutes: 155, status: "watched"   },
  { id: 9,  title: "The Power of the Dog",   year: 2021, genre: "drama",       director: { id: 8, name: "Jane Campion",         nationality: "New Zealand"}, rating: 6.9, durationMinutes: 126, status: "dropped"   },
  { id: 10, title: "Free Guy",               year: 2021, genre: "comedy",      director: { id: 9, name: "Shawn Levy",           nationality: "Canadian"   }, rating: 7.1, durationMinutes: 115, status: "watchlist" },
];
```

---

## File structure

```text
src/
├── types/
│   └── models.ts          # Interfaces and types
├── data/
│   └── movies.ts          # Sample dataset
├── utils/
│   ├── collections.ts     # filter, sort functions
│   ├── search.ts          # linearSearch, binarySearch
│   ├── transformations.ts # aggregations and reports
│   └── validations.ts     # business validations
└── demo.ts                # Manual test runner
```

---

## What to implement

### `src/utils/collections.ts` — Filtering and sorting

- [ ] `filterByGenre(movies: Movie[], genre: Genre): Movie[]`
- [ ] `filterByStatus(movies: Movie[], status: WatchStatus): Movie[]`
- [ ] `filterByYearRange(movies: Movie[], from: number, to: number): Movie[]`
- [ ] `filterByMinRating(movies: Movie[], minRating: number): Movie[]`
- [ ] `sortByRating(movies: Movie[], order: "asc" | "desc"): Movie[]`
- [ ] `sortByYear(movies: Movie[], order: "asc" | "desc"): Movie[]`
- [ ] `sortByTitle(movies: Movie[]): Movie[]` — alphabetical, ascending

All functions must be **pure**: they return a new array and do not mutate the input.

---

### `src/utils/search.ts` — Search algorithms

- [ ] `linearSearchByTitle(movies: Movie[], title: string): Movie | null`
  - Works on any array regardless of order.
  - Returns the first exact match (case-insensitive) or `null` if not found.

- [ ] `binarySearchById(sortedMovies: Movie[], id: number): Movie | null`
  - The input array **must** be sorted by `id` ascending.
  - Returns the matching movie or `null` if not found.
  - Must implement the binary search algorithm — do not use `.find()`.

Add a comment explaining why binary search requires a sorted array.

---

### `src/utils/transformations.ts` — Aggregations

- [ ] `countByGenre(movies: Movie[]): Record<Genre, number>` — returns a count for every genre, including genres with 0 movies
- [ ] `countByStatus(movies: Movie[]): Record<WatchStatus, number>`
- [ ] `averageRating(movies: Movie[]): number` — returns `0` for an empty array
- [ ] `topRated(movies: Movie[], n: number): Movie[]` — returns the top `n` movies by rating (descending)
- [ ] `totalDuration(movies: Movie[]): number` — sum of `durationMinutes` for all movies in the input

---

### `src/utils/validations.ts` — Business rules

- [ ] `isValidMovie(movie: unknown): movie is Movie` — returns `true` only if:
  - `title` is a non-empty string
  - `year` is between 1888 and the current year (inclusive)
  - `genre` is one of the allowed values
  - `rating` is between 0 and 10 (inclusive)
  - `durationMinutes` is greater than 0
  - `status` is one of the allowed values
  - `director.name` is a non-empty string

- [ ] `validateMovieOrThrow(movie: unknown): Movie` — calls `isValidMovie`; throws a descriptive `Error` if invalid, otherwise returns the typed movie.

---

### `src/demo.ts` — Manual test runner

- [ ] Call each utility with the sample data and print results to the console.
- [ ] Run it with: `npx tsx src/demo.ts`

Example output:

```
--- Filter: sci-fi movies ---
Inception, Dune, Everything Everywhere

--- Sort: by rating DESC ---
The Dark Knight (9.0), Inception (8.8), ...

--- Linear search: "Dune" ---
Found: Dune (2021)

--- Binary search by id: 5 ---
Found: Get Out

--- Count by genre ---
action: 1, comedy: 2, drama: 2, horror: 1, sci-fi: 3, documentary: 0, animation: 1

--- Average rating ---
8.04

--- Validation: invalid movie ---
Error: "year" must be between 1888 and 2026
```

---

## Code quality rules

- [ ] All function parameters and return values have explicit TypeScript types (no `any`)
- [ ] Use `const` by default; `let` only when the value must change
- [ ] Handle edge cases: empty arrays return sensible defaults (empty array, `0`, `null`)
- [ ] Each function does exactly one thing (single responsibility)
- [ ] No TypeScript compilation errors: verify with `npx tsc --noEmit`

---

## Discussion questions

1. `linearSearchByTitle` works on any array, but `binarySearchById` requires the array to be sorted first. For a collection of 10 movies, does the sorting overhead make binary search worth it? At what collection size does the answer change, and why?
2. `countByGenre` returns a count for every genre, including genres with zero movies. Why is returning `{ ..., "documentary": 0 }` better than omitting the key entirely? How does this affect code that consumes the result?
3. `isValidMovie` accepts `unknown` as the input type instead of `Movie`. Why is this safer than accepting `Movie` directly? Can you think of a situation where you would receive data of unknown type that needs to be validated before use?
