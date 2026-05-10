# In-Class Example: Gym Membership Dashboard

> **Instructor note:** This is an in-class live example for teaching the concepts of the `simple-dashboard-tailwind-css` project. Use this scenario to walk students through building a responsive Tailwind CSS dashboard using semantic HTML and a mobile-first approach. **Do not assign this as homework — it is a guided classroom exercise.**

---

## The Scenario

A small neighborhood gym wants a simple web dashboard to track their business at a glance. The gym owner checks it every morning on their phone and on a desktop monitor at the front desk. They need to know:

- How many active members do they have this month?
- How much revenue did memberships generate?
- Which classes are filling up and which are empty?
- Are members renewing or canceling?

Your task: build a single-page dashboard in **HTML + Tailwind CSS v4** (no frameworks, no JavaScript logic) that presents this data clearly across mobile, tablet, and desktop screens.

---

## Setup

Add the Tailwind CSS v4 CDN to your `<head>`:

```html
<head>
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
```

> ⚠️ Tell your AI assistant to use **Tailwind CSS v4** and to avoid `cdn.tailwindcss.com` or any Tailwind v3 CDN.

---

## Sample Data (use this in the dashboard)

**Membership tiers:**

| Tier | Monthly Price | Active Members |
|---|---|---|
| Basic | €29 | 85 |
| Standard | €49 | 120 |
| Premium | €79 | 40 |

**Classes this week:**

| Class | Capacity | Enrolled | Day |
|---|---|---|---|
| Morning Yoga | 15 | 14 | Mon / Wed / Fri |
| HIIT | 20 | 20 | Tue / Thu |
| Spinning | 18 | 9 | Mon / Wed |
| Pilates | 12 | 12 | Tue / Fri |

**Monthly summary:**
- New members this month: **18**
- Cancellations this month: **5**
- Net growth: **+13**
- Total revenue: **€12,745**

---

## Dashboard Structure

Build the dashboard in **three vertical blocks**:

### Block 1 — KPIs (top)

Show at least **3 KPI cards**, for example:

- Total active members: **245**
- Monthly revenue: **€12,745**
- Average class fill rate: **87%**

### Block 2 — Drivers (middle)

Show at least **3 driver visualizations**, for example:

- Revenue breakdown by tier (use a simple CSS bar or Chart CSS if available)
- Member retention this month: new vs. cancellations
- Top 3 classes by fill rate

### Block 3 — Operational Details (bottom)

- Full class schedule table (name, capacity, enrolled, fill %, days)
- Membership tier table (tier, price, active members, revenue)

---

## Requirements

- [ ] Use **semantic HTML**: `<header>`, `<main>`, `<section>`, `<table>`, `<nav>` where appropriate
- [ ] Apply styles using **Tailwind utility classes only** — no custom CSS, no other framework
- [ ] Design **mobile-first**: start with a single-column layout, then expand with `sm:`, `md:`, `lg:` breakpoints
- [ ] KPI cards should look consistent (same structure, same padding, same text hierarchy)
- [ ] The layout must not break or require horizontal scrolling on small screens

---

## Discussion Questions

1. Why do we separate the dashboard into KPI / Driver / Operational blocks? What decision does each block support for the gym owner?
2. You used `sm:`, `md:`, and `lg:` breakpoints. What happens on a screen smaller than `sm:`? Why does mobile-first matter in practice?
3. The data in this dashboard is hardcoded in HTML. How would this dashboard look different if it were connected to a live database? What would need to change in the code?
