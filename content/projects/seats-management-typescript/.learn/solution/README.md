# Cinema Seat Manager (TypeScript) – Reference solution

This README describes the reference implementation for the **"Cinema Seat Manager (TypeScript)"** project and links to the canonical solution file in the repository.

## Repository location of the main solution

The main TypeScript implementation of the solution lives at:

- [Solution TypeScript](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/seats-management-typescript/.learn/solution/solution.ts)

Use that file as the canonical reference when comparing or reviewing solutions.

## What the reference solution shows

- A **TypeScript CLI-style program** that manages a cinema seating map using a 2D array.
- A clear separation of concerns into **small functions**:
  - `createSeatingMatrix` to initialise the seating matrix.
  - `printSeating` to display the room with a legend (occupied vs free).
  - `reserveSeat` to book a specific seat with proper validations.
  - `countSeats` to compute occupied vs available seats.
  - `findAdjacentSeats` to search for the first pair of adjacent available seats.
- A `demo` function that:
  - Builds the matrix.
  - Reserves some example seats.
  - Prints the room before and after.
  - Logs the counts of occupied and available seats.
  - Logs the result of searching for adjacent free seats.

## Elements you should be able to find

When comparing a student implementation with the reference:

- Use of **TypeScript types** (e.g. `number[][]`, return types) for clarity.
- Input validation when reserving a seat:
  - Coordinates translated from 1‑based input to 0‑based indices.
  - Guard clauses for out‑of‑range positions.
  - Meaningful return messages for invalid or already‑occupied seats.
- A clear textual **representation of the room**:
  - Header row with column numbers.
  - Each row prefixed with its index.
  - Distinct symbols for occupied vs free seats.
- Logic to **scan for adjacent available seats** row by row, returning the first valid pair.

## How to read and use the solution

- Treat `solution.ts` as a **reference for structure and edge‑case handling**:
  - Encourage students to follow similar function decomposition, even if their naming differs.
  - Check whether they validate indices and avoid accessing the matrix out of bounds.
  - Check whether they provide clear console output that a user could understand.
- Use the `demo` flow as a benchmark:
  - A student solution should, at minimum, be able to initialise the room, reserve seats, print the map, and derive basic statistics from the matrix.
