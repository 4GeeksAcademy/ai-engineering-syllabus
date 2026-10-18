# BRIEFING — Brasaland

**Milestone 2: Programming Fundamentals**  
**Company:** Brasaland — Grilled Food Restaurant Chain  
**Your Role:** Junior Developer, Brasaland Digital Team  
**Project Owner:** Felipe Guerrero, Operations Director

---

## About Brasaland

Brasaland is a grilled food restaurant chain with 14 company-owned locations across Colombia and the United States (Florida). The company focuses on consistent product quality, warm customer experience, and speed of service. You're part of Brasaland Digital, the internal team leading the company's digital transformation.

---

## Your Assignment

Felipe Guerrero, the Operations Director, needs you to build the core data processing logic for Brasaland's restaurant operations system. Currently, location managers handle everything manually — tracking sales, calculating margins, managing waste, and ordering ingredients. This milestone focuses on building the TypeScript functions that will power sales analytics, waste control, and location performance scoring.

This is pure programming — no AI, no prompting. Felipe needs code that works reliably across 14 locations in two countries with different currencies and regulations.

---

## What You're Building

You will implement a set of TypeScript utilities to:

1. **Model menu items, sales, and locations** using interfaces
2. **Filter and search sales data** by location, date, and product
3. **Calculate location performance scores** based on multiple metrics
4. **Compute financial metrics** (revenue, cost, margin) in multiple currencies
5. **Generate operations reports** with aggregated data
6. **Validate data** before processing

---

## Business Entities

### MenuItem

Represents an item on Brasaland's menu.

**Interface: `MenuItem`**

```typescript
interface MenuItem {
  id: string; // Menu item ID (e.g., "ITEM-PICANHA-250")
  name: string; // Item name (e.g., "Picanha 250g")
  category: MenuCategory; // Food category
  basePrice: Price; // Base price (can vary by location)
  ingredientCost: Price; // Cost of ingredients per unit
  prepTimeMinutes: number; // Average preparation time
  isAvailableInColombia: boolean;
  isAvailableInUSA: boolean;
  allergens: string[]; // List of allergens
  status: MenuItemStatus;
}

interface Price {
  USD: number; // Price in US Dollars
  COP: number; // Price in Colombian Pesos
}

type MenuCategory = "Meat" | "Side" | "Beverage" | "Dessert" | "Combo";
type MenuItemStatus = "Active" | "Seasonal" | "Discontinued";
```

**Validation Rules:**

- Both `USD` and `COP` prices must be > 0
- `prepTimeMinutes` must be > 0 and <= 60
- `name` must not be empty
- Item must be available in at least one country

---

### SaleTransaction

Represents a sale made at a Brasaland location.

**Interface: `SaleTransaction`**

```typescript
interface SaleTransaction {
  id: string; // Transaction ID (e.g., "TXN-2024-15482")
  locationId: string; // Location where sale occurred
  itemId: string; // Menu item sold
  quantity: number; // Number of units sold
  totalPrice: Price; // Total price charged
  paymentMethod: PaymentMethod; // How customer paid
  timestamp: Date; // When the sale occurred
  waiterName: string; // Staff member who served
}

type PaymentMethod = "Cash" | "Credit card" | "Debit card" | "Digital wallet";
```

**Validation Rules:**

- `quantity` must be > 0
- Both price values must be > 0
- `waiterName` must not be empty

---

### Location

Represents a Brasaland restaurant location.

**Interface: `Location`**

```typescript
interface Location {
  id: string; // Location ID (e.g., "LOC-MEDELLIN-01")
  name: string; // Location name
  city: string; // City name
  country: Country; // Colombia or USA
  openingYear: number; // Year opened
  seatingCapacity: number; // Maximum number of customers
  staffCount: number; // Number of employees
  monthlyRentCost: Price; // Monthly rent
  averageMonthlyUtilities: Price; // Average monthly utilities
  manager: string; // Location manager name
  status: LocationStatus;
}

type Country = "Colombia" | "USA";
type LocationStatus = "Active" | "Temporarily closed" | "Under renovation";
```

**Validation Rules:**

- `openingYear` must be >= 2008 and <= current year
- `seatingCapacity` must be > 0
- `staffCount` must be > 0
- Both rent and utilities costs must be > 0

---

### WasteRecord

Tracks food waste at a location.

**Interface: `WasteRecord`**

```typescript
interface WasteRecord {
  id: string; // Waste record ID
  locationId: string; // Location where waste occurred
  itemId: string; // Menu item wasted
  quantity: number; // Number of units wasted
  reason: WasteReason; // Why it was wasted
  cost: Price; // Cost of wasted items
  timestamp: Date; // When it was recorded
  reportedBy: string; // Staff member who reported it
}

type WasteReason =
  | "Expired"
  | "Cooking error"
  | "Customer return"
  | "Damage"
  | "Other";
```

---

## Required Functions

Implement these functions in the appropriate files according to the structure in the README.

### 1. Collection Operations (`src/utils/collections.ts`)

**`filterSalesByLocation(sales: SaleTransaction[], locationId: string): SaleTransaction[]`**

- Returns all sales from the specified location

**`filterSalesByDateRange(sales: SaleTransaction[], startDate: Date, endDate: Date): SaleTransaction[]`**

- Returns sales that occurred between start and end dates (inclusive)

**`filterMenuItemsByCategory(items: MenuItem[], category: MenuCategory): MenuItem[]`**

- Returns menu items in the specified category

**`filterActiveLocations(locations: Location[]): Location[]`**

- Returns locations with status "Active"

**`sortLocationsByCapacity(locations: Location[], order: "asc" | "desc"): Location[]`**

- Returns locations sorted by seating capacity
- Should not mutate the original array

**`sortMenuItemsByPrice(items: MenuItem[], currency: "USD" | "COP", order: "asc" | "desc"): MenuItem[]`**

- Returns menu items sorted by price in the specified currency
- Should not mutate the original array

---

### 2. Search Operations (`src/utils/search.ts`)

**`findLocationById(locations: Location[], id: string): Location | null`**

- Performs linear search to find a location by ID
- Returns the location if found, null otherwise

**`findMenuItemByName(items: MenuItem[], name: string): MenuItem | null`**

- Performs linear search to find a menu item by name
- Name comparison should be case-insensitive
- Returns the item if found, null otherwise

**`binarySearchLocationByCapacity(sortedLocations: Location[], targetCapacity: number): number`**

- Assumes the array is already sorted by seating capacity (ascending)
- Performs binary search to find the index of a location with the target capacity
- Returns the index if found, -1 otherwise

---

### 3. Financial Calculations (`src/utils/transformations.ts`)

**`calculateDailyRevenue(sales: SaleTransaction[], date: Date, currency: "USD" | "COP"): number`**

- Calculates total revenue for a specific date in the specified currency
- Returns total rounded to 2 decimal places

**`calculateLocationMargin(sales: SaleTransaction[], menuItems: MenuItem[], locationId: string, currency: "USD" | "COP"): number`**

- Calculates profit margin for a location
- Formula: ((Total Revenue - Total Ingredient Cost) / Total Revenue) \* 100
- Uses sales from that location only
- Joins sales with menu items to get ingredient costs
- Returns margin as percentage (0-100), rounded to 2 decimal places

**`calculateWasteCost(wasteRecords: WasteRecord[], locationId: string, currency: "USD" | "COP"): number`**

- Calculates total cost of waste for a location in the specified currency
- Returns total rounded to 2 decimal places

**`convertCurrency(amount: number, fromCurrency: "USD" | "COP", toCurrency: "USD" | "COP"): number`**

- Converts between USD and COP using a fixed exchange rate
- Use rate: 1 USD = 4000 COP
- Returns converted amount rounded to 2 decimal places
- If from and to are the same, return the original amount

---

### 4. Location Performance Scoring (`src/utils/transformations.ts`)

**`scoreLocationPerformance(location: Location, sales: SaleTransaction[], wasteRecords: WasteRecord[], menuItems: MenuItem[]): number`**

Calculates a performance score (0-100) for a location based on:

- **Revenue performance (40 points max):**
  - Calculate daily average revenue (total revenue / number of operating days)
  - Operating days = days since opening (estimate from openingYear)
  - Score: (avg daily revenue in USD / 1000) \* 40, capped at 40

- **Efficiency (30 points max):**
  - Calculate seats efficiency: (total sales count / seating capacity) \* 30, capped at 30
  - Represents how well the location uses its capacity

- **Waste control (20 points max):**
  - Calculate waste percentage: (total waste cost / total revenue) \* 100
  - Score: 20 - (waste percentage \* 2), minimum 0
  - Lower waste = higher score

- **Profit margin (10 points max):**
  - Use calculateLocationMargin function
  - Score: margin / 10, capped at 10

Returns total score rounded to 2 decimal places

**`rankLocationsByPerformance(locations: Location[], sales: SaleTransaction[], wasteRecords: WasteRecord[], menuItems: MenuItem[]): Array<{location: Location, score: number}>`**

- Scores all locations
- Returns them sorted by score (highest first)
- Each element contains the location and its score

---

### 5. Aggregations and Reports (`src/utils/transformations.ts`)

**`countSalesByPaymentMethod(sales: SaleTransaction[]): Record<PaymentMethod, number>`**

- Returns count of sales for each payment method

**`calculateAverageTicket(sales: SaleTransaction[], currency: "USD" | "COP"): number`**

- Returns average sale value in the specified currency
- Round to 2 decimal places

**`findTopSellingItems(sales: SaleTransaction[], menuItems: MenuItem[], topN: number): Array<{item: MenuItem, totalSold: number}>`**

- Finds the N most sold menu items
- Joins sales with menu items
- Returns them sorted by quantity sold (highest first)
- Each element contains the menu item and total quantity sold

**`groupWasteByReason(wasteRecords: WasteRecord[]): Record<WasteReason, WasteRecord[]>`**

- Groups waste records by reason
- Returns an object where keys are waste reasons and values are arrays of records

**`calculateCountryComparison(sales: SaleTransaction[], locations: Location[], menuItems: MenuItem[]): {Colombia: CountryMetrics, USA: CountryMetrics}`**

Returns comparative metrics for each country:

```typescript
interface CountryMetrics {
  totalLocations: number;
  totalRevenue: Price;
  averageRevenuePerLocation: Price;
  totalSales: number;
}
```

---

### 6. Validations (`src/utils/validations.ts`)

**`validateMenuItem(item: MenuItem): { valid: boolean, errors: string[] }`**

- Validates all business rules for a menu item
- Returns an object with:
  - `valid`: true if all validations pass, false otherwise
  - `errors`: array of error messages (empty if valid)

**`validateSaleTransaction(sale: SaleTransaction): { valid: boolean, errors: string[] }`**

- Validates all business rules for a sale
- Returns an object with:
  - `valid`: true if all validations pass, false otherwise
  - `errors`: array of error messages (empty if valid)

**`validateLocation(location: Location): { valid: boolean, errors: string[] }`**

- Validates all business rules for a location
- Returns an object with:
  - `valid`: true if all validations pass, false otherwise
  - `errors`: array of error messages (empty if valid)

---

## Sample Data

Use this data to test your functions:

### Sample Menu Items

```typescript
const sampleMenuItems: MenuItem[] = [
  {
    id: "ITEM-PICANHA-250",
    name: "Picanha 250g",
    category: "Meat",
    basePrice: { USD: 18.5, COP: 74000 },
    ingredientCost: { USD: 7.2, COP: 28800 },
    prepTimeMinutes: 15,
    isAvailableInColombia: true,
    isAvailableInUSA: true,
    allergens: [],
    status: "Active",
  },
  {
    id: "ITEM-FRIES",
    name: "French Fries",
    category: "Side",
    basePrice: { USD: 4.5, COP: 18000 },
    ingredientCost: { USD: 1.2, COP: 4800 },
    prepTimeMinutes: 8,
    isAvailableInColombia: true,
    isAvailableInUSA: true,
    allergens: [],
    status: "Active",
  },
  {
    id: "ITEM-COKE",
    name: "Coca-Cola",
    category: "Beverage",
    basePrice: { USD: 2.5, COP: 10000 },
    ingredientCost: { USD: 0.8, COP: 3200 },
    prepTimeMinutes: 2,
    isAvailableInColombia: true,
    isAvailableInUSA: true,
    allergens: [],
    status: "Active",
  },
];
```

### Sample Locations

```typescript
const sampleLocations: Location[] = [
  {
    id: "LOC-MEDELLIN-01",
    name: "Brasaland Medellín Centro",
    city: "Medellín",
    country: "Colombia",
    openingYear: 2008,
    seatingCapacity: 80,
    staffCount: 12,
    monthlyRentCost: { USD: 1500, COP: 6000000 },
    averageMonthlyUtilities: { USD: 400, COP: 1600000 },
    manager: "Carlos Jiménez",
    status: "Active",
  },
  {
    id: "LOC-MIAMI-01",
    name: "Brasaland Miami Beach",
    city: "Miami",
    country: "USA",
    openingYear: 2018,
    seatingCapacity: 100,
    staffCount: 15,
    monthlyRentCost: { USD: 5500, COP: 22000000 },
    averageMonthlyUtilities: { USD: 800, COP: 3200000 },
    manager: "Jake Morrison",
    status: "Active",
  },
];
```

### Sample Sales

```typescript
const sampleSales: SaleTransaction[] = [
  {
    id: "TXN-2024-15482",
    locationId: "LOC-MEDELLIN-01",
    itemId: "ITEM-PICANHA-250",
    quantity: 2,
    totalPrice: { USD: 37.0, COP: 148000 },
    paymentMethod: "Credit card",
    timestamp: new Date("2024-03-15T19:30:00"),
    waiterName: "María González",
  },
  {
    id: "TXN-2024-15483",
    locationId: "LOC-MIAMI-01",
    itemId: "ITEM-FRIES",
    quantity: 3,
    totalPrice: { USD: 13.5, COP: 54000 },
    paymentMethod: "Cash",
    timestamp: new Date("2024-03-15T20:15:00"),
    waiterName: "John Smith",
  },
];
```

---

## Acceptance Criteria

Your implementation will be evaluated on:

1. **Type Safety:** All interfaces defined correctly with appropriate types
2. **Function Correctness:** Each function produces the expected output for the given inputs
3. **Edge Case Handling:** Functions handle empty arrays, null values, and invalid data gracefully
4. **Validation Logic:** Business rules are enforced accurately
5. **Code Organization:** Functions are in the correct files according to responsibility
6. **Naming Conventions:** Variables, functions, and types follow TypeScript conventions
7. **No Mutations:** Sorting and filtering functions don't modify the original arrays
8. **Pure Functions:** Functions only work with parameters, no global variables
9. **Currency Handling:** All financial calculations work correctly in both USD and COP

---

## What Felipe Expects

> "Mira, we have 14 locations running every day. Your code needs to handle Colombian pesos and US dollars correctly, work with different time zones, and give me accurate numbers I can trust. No shortcuts. If the margin calculation is wrong, I'm making bad decisions. Build it right."  
> — Felipe Guerrero, Operations Director

---

## Questions?

If you're unsure about any requirement, ask your mentor. In a real work environment, you'd message Felipe on Slack .

---

_This is a real Brasaland project. What you build here will become part of the production operations system used across 14 locations in Colombia and Florida._
