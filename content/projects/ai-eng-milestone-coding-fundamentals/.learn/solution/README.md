# Milestone 2 — Building Scripts to Automate Tasks — Reference Solution

## Purpose

Reference quality bar for the TypeScript **data-processing utilities** milestone. Students implement company-specific logic from their `CONTEXT-*.md` in `02-coding-fundamentals` — not a generic demo.

## Expected File Structure

```text
src/
├── types/
│   └── models.ts          # Interfaces from CONTEXT
├── utils/
│   ├── collections.ts     # filter, sort, group
│   ├── search.ts          # linearSearch, binarySearch
│   ├── transformations.ts # aggregations and reports
│   └── validations.ts     # business rules from CONTEXT
├── demo.ts                # optional: console demos
└── index.html             # optional: manual test page
```

Validation command (document in README or `package.json`):

```bash
npx tsc --noEmit
```

## Required Coverage (From README)

- Interfaces model **all main entities** named in the student's CONTEXT.
- **Filter** and **sort** functions with explicit parameter/return types.
- **Linear search** on unsorted arrays; **binary search** on sorted arrays (return index or `-1`).
- **Aggregations**: count by category, sum, average, min, max — typed returns.
- **Validations** enforce CONTEXT business rules before processing.
- Pure functions — no global mutable state.
- Edge cases: empty arrays, not found, invalid input.

## Indicative Interface Pattern (Adapt to CONTEXT)

Entity names, fields, and rules must come from the company CONTEXT — this Brasaland-style sketch shows structure only:

```typescript
// src/types/models.ts
export interface Price {
  USD: number;
  COP: number;
}

export interface MenuItem {
  id: string;
  name: string;
  category: MenuCategory;
  basePrice: Price;
  ingredientCost: Price;
  prepTimeMinutes: number;
  isAvailableInColombia: boolean;
  isAvailableInUSA: boolean;
  allergens: string[];
  status: MenuItemStatus;
}

export type MenuCategory = "Meat" | "Side" | "Beverage" | "Dessert" | "Combo";
export type MenuItemStatus = "Active" | "Seasonal" | "Discontinued";
```

## Indicative Utility Patterns

### collections.ts

```typescript
export function filterByCategory<T extends { category: string }>(
  items: T[],
  category: string,
): T[] {
  return items.filter((item) => item.category === category);
}

export function sortByNumericField<T>(
  items: T[],
  field: keyof T,
  direction: "asc" | "desc" = "asc",
): T[] {
  return [...items].sort((a, b) => {
    const left = Number(a[field]);
    const right = Number(b[field]);
    return direction === "asc" ? left - right : right - left;
  });
}
```

### search.ts

```typescript
export function linearSearch<T>(
  items: T[],
  predicate: (item: T) => boolean,
): T | undefined {
  for (const item of items) {
    if (predicate(item)) return item;
  }
  return undefined;
}

export function binarySearch(sortedIds: string[], target: string): number {
  let low = 0;
  let high = sortedIds.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (sortedIds[mid] === target) return mid;
    if (sortedIds[mid] < target) low = mid + 1;
    else high = mid - 1;
  }
  return -1;
}
```

### transformations.ts

```typescript
export function countByCategory<T extends { category: string }>(
  items: T[],
): Record<string, number> {
  return items.reduce<Record<string, number>>((acc, item) => {
    acc[item.category] = (acc[item.category] ?? 0) + 1;
    return acc;
  }, {});
}
```

### validations.ts

```typescript
export function validateMenuItem(item: MenuItem): string[] {
  const errors: string[] = [];
  if (!item.name.trim()) errors.push("name is required");
  if (item.basePrice.USD <= 0 || item.basePrice.COP <= 0) {
    errors.push("prices must be positive");
  }
  if (!item.isAvailableInColombia && !item.isAvailableInUSA) {
    errors.push("item must be available in at least one country");
  }
  return errors;
}
```

## CONTEXT Adaptation Rules

- Replace entity names (`MenuItem`, `SaleTransaction`, etc.) with those in **your** CONTEXT file.
- Validation messages and thresholds must match CONTEXT rules exactly.
- Reports listed in CONTEXT (e.g. location performance, waste totals) must have corresponding aggregation functions.

## Evaluation Checklist

- [ ] Interfaces match CONTEXT entities, fields, and types.
- [ ] Filter, sort, linear search, and binary search behave correctly on edge cases.
- [ ] Aggregations return correct totals, averages, counts, min/max.
- [ ] Validations reject invalid objects per CONTEXT rules.
- [ ] `npx tsc --noEmit` (or equivalent) passes with no errors.
- [ ] Code split by responsibility; functions are pure and single-purpose.

## Reviewer Notes

- Reject generic implementations that ignore company-specific entities.
- Optional `index.html` test page is not required for a passing grade.
- Binary search must operate on a **pre-sorted** array — document that precondition in comments if needed.
