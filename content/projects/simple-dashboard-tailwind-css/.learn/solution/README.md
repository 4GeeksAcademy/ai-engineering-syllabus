# Simple dashboard with Tailwind CSS – Reference solution

This README describes the reference implementation for the **"Simple dashboard with Tailwind CSS"** project and links to the canonical solution file in the repository.

## Repository location of the main solution

The main HTML implementation of the solution lives at:

- [Solution HTML](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/simple-dashboard-tailwind-css/.learn/solution/solution.html)

Use that file as the canonical reference when comparing or reviewing solutions.

## What the reference solution shows

- **HTML + Tailwind only**: A single-page dashboard implemented with semantic HTML and Tailwind CSS via CDN (no React, no frameworks).
- **Three conceptual blocks**:
  - **Top block – KPIs**: Cards showing key performance indicators (e.g., revenue, conversions, engagement).
  - **Middle block – Drivers**: Sections and widgets explaining why those KPIs move (per platform, per product, per campaign).
  - **Bottom block – Operational details**: Tables and lists with more granular data (campaigns, products, or platforms).
- **Mobile‑first layout**:
  - Stacks content in a single column on small screens.
  - Uses Tailwind responsive utilities (`sm:`, `md:`, `lg:`) to move to multi‑column layouts on tablets and desktop.
- **Consistent component patterns**:
  - Reusable card styles for KPIs and drivers.
  - Repeated table patterns for detailed data (e.g., products and platforms).

## Elements you should be able to find

When comparing a student implementation with the reference:

- A clear **page structure** using semantic landmarks:
  - `header` and/or sidebar for navigation.
  - `main` wrapping the core dashboard content.
  - Sections for KPIs, drivers, and detailed tables.
- **KPI cards** that:
  - Group the most important metrics at the top.
  - Use visual hierarchy (font size, color, spacing) to highlight primary numbers.
- **Driver sections** that:
  - Break down performance by platform, product, or campaign.
  - Help explain _why_ the KPIs look the way they do.
- **Operational tables or lists** that:
  - Show structured data (e.g., products with price, conversions, ROI).
  - Use Tailwind utilities for borders, padding, and typography.

## How to read and use the solution

- Treat the HTML file as a **reference layout and component library**, not as something to copy verbatim.
- Check whether a student solution:
  - Respects the three‑block structure (KPIs, drivers, details).
  - Uses Tailwind utilities correctly for spacing, color, typography, and responsive behavior.
  - Provides a clear and readable dashboard that would make sense to a non‑technical user.
