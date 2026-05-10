# In-Class Example: Parking Lot Space Manager

> **Instructor note:** This is an in-class live example for teaching the concepts of the `seats-management-typescript` project. Use this scenario to demonstrate 2D arrays, matrix traversal, and function design in TypeScript. **Do not assign this as homework — it is a guided classroom exercise.**

---

## The Scenario

A small municipal parking lot with **4 rows and 6 spaces per row** needs a simple management tool. The attendant currently tracks availability with a paper grid. Your team will build a TypeScript command-line program that lets the attendant see which spaces are free, reserve a space for a vehicle, and find two adjacent free spaces for oversized vehicles (e.g., a van or trailer).

**What you are learning:**
- How to represent a physical space as a 2D array (matrix)
- How to traverse and mutate a matrix with loops and conditionals
- How to design functions with parameters and return values in TypeScript
- How to search for a pattern (adjacent free cells) inside a matrix

---

## Data Model

```
Row 0:  [ 0, 0, 1, 0, 0, 1 ]
Row 1:  [ 1, 0, 0, 0, 1, 0 ]
Row 2:  [ 0, 0, 0, 1, 0, 0 ]
Row 3:  [ 0, 1, 0, 0, 0, 0 ]
```

- `0` = free space
- `1` = occupied space

Console display uses `_` (free) and `X` (occupied), with row and column labels.

---

## Tasks

### Core Functions

- [ ] `initLot(): number[][]` — creates a 4×6 matrix initialized to `0` (all spaces free)
- [ ] `displayLot(lot: number[][]): void` — prints the lot to the console with row/column labels:

  ```
      C0  C1  C2  C3  C4  C5
  R0 [  _   _   X   _   _   X ]
  R1 [  X   _   _   _   X   _ ]
  ...
  ```

- [ ] `reserveSpace(lot: number[][], row: number, col: number): string` — marks a space as occupied (`0 → 1`); returns `"Reserved R{row}C{col}"` or `"Space already occupied"` if it was taken
- [ ] `countSpaces(lot: number[][]): { free: number; occupied: number }` — returns the count of free and occupied spaces

### Advanced Function

- [ ] `findAdjacentPair(lot: number[][]): [number, number][] | null` — searches each row for two consecutive free spaces (`0, 0`) and returns their `[row, col]` positions; returns the first pair found, or `null` if none exist

### Test Scenarios

Run your program with these four states and print the lot after each:

- [ ] Empty lot — all spaces free
- [ ] Partially occupied (manually set a few spaces to `1`)
- [ ] Nearly full (only one or two isolated free spaces)
- [ ] Completely full — confirm `findAdjacentPair` returns `null`

---

## Expected Console Output (Example)

```
=== PARKING LOT STATUS ===
      C0  C1  C2  C3  C4  C5
  R0 [  _   _   X   _   _   X ]
  R1 [  X   _   _   _   X   _ ]
  R2 [  _   _   _   X   _   _ ]
  R3 [  _   X   _   _   _   _ ]

Free: 16  |  Occupied: 8

Reserving R0C0... Reserved R0C0
Reserving R0C0 again... Space already occupied

Adjacent pair for oversized vehicle: R0C3 and R0C4
```

---

## Constraints

> ⚠️ Do **not** use classes or objects to store the lot data. The matrix must be a plain `number[][]`. Use function parameters and return values to pass state around.

---

## Discussion Questions

1. Why is a 2D array a natural fit for representing a parking lot? What would break if you used a flat 1D array instead?
2. The `reserveSpace` function currently only reserves spaces, never frees them. How would you add a `releaseSpace` function, and what validation would it need?
3. If the parking lot grew to 100 rows × 200 columns, which function would become the slowest? How could you optimize it?
