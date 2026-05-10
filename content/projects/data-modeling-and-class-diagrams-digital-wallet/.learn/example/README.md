> **In-class example for instructors.** Use this scenario to introduce class diagrams in a ~1-hour session. This file is a teaching aid with a *different domain* than the assigned project. Do not share this with students as their project brief.

# Loyalty Card System — Object Modeling (In-Class Example)

## Scenario

A local coffee shop wants to build a digital loyalty card system. Before writing any code, you need to model the data layer as a class diagram.

The shop manager describes what the system must support:

> A customer can have one loyalty card. The card tracks a point balance and belongs to a reward tier (Bronze, Silver, or Gold). Every time a customer makes a purchase or redeems a reward, a point transaction is recorded. Each transaction has a type (earn or redeem), a point amount, a timestamp, and a status (pending or confirmed).

Your task is to model this system as a **class diagram** with typed properties and clearly defined relationships.

---

## What to Model

### Suggested Entities

| Model | Description |
|-------|-------------|
| `Customer` | The person who owns the loyalty card |
| `LoyaltyCard` | The card linked to a customer, tracking point balance and tier |
| `PointTransaction` | A record of every point earn or redeem event |

### Sample Typed Properties

| Model | Property | Type |
|-------|----------|------|
| `Customer` | `id` | `int` |
| `Customer` | `name` | `string` |
| `Customer` | `email` | `string` |
| `LoyaltyCard` | `id` | `int` |
| `LoyaltyCard` | `pointBalance` | `int` |
| `LoyaltyCard` | `tier` | `string` |
| `LoyaltyCard` | `isActive` | `boolean` |
| `PointTransaction` | `id` | `int` |
| `PointTransaction` | `type` | `string` |
| `PointTransaction` | `points` | `int` |
| `PointTransaction` | `createdAt` | `date` |
| `PointTransaction` | `status` | `string` |

### Relationships to Draw

- A `Customer` owns **one** `LoyaltyCard` (1 to 1)
- A `LoyaltyCard` has **many** `PointTransaction` records (1 to many)
- Each `PointTransaction` belongs to **one** `LoyaltyCard`

---

## Checklist

- [ ] Create at least **3 models** in the diagram tool
- [ ] Add every property with its **explicit data type**
- [ ] Draw **relationships** between models with correct cardinality labels
- [ ] Ensure the diagram is **readable** — no overlapping boxes, traceable arrows
- [ ] Export the result as **`loyalty-card-class-diagram.png`**

**Tool:** [diagram.4geeks.com](https://diagram.4geeks.com/)

---

## Discussion Questions

1. The `tier` property is currently a plain `string` on `LoyaltyCard`. What would change if `RewardTier` became its own model with a `minimumPoints: int` property? When is that worth the extra complexity?
2. What happens to a customer's `PointTransaction` records if they close their account? How would you represent that decision in the diagram?
3. A `PointTransaction` can represent either earning points (a purchase) or redeeming them (a reward). Should these be two separate models or one model with a `type` field? What are the trade-offs of each approach?
