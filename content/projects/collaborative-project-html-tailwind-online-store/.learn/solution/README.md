# Collaborative project – Online store with HTML and Tailwind – Reference solution

This README describes the reference blueprint for the **"Collaborative project: online store with HTML and Tailwind"** and links to the canonical solution document in the repository.

## Repository location of the main solution

The main explanatory solution file lives at:

- [Solution document](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/collaborative-project-html-tailwind-online-store/.learn/solution/solution.md)

Use that file as the canonical reference when comparing or reviewing solutions.

## What the reference solution shows

- A **multi‑view e‑commerce prototype** defined through:
  - A shared layout (navbar + footer) reused across all views.
  - Five core views:
    1. Home.
    2. Catalog.
    3. Product detail.
    4. Cart.
    5. Checkout / Payment form.
- Detailed guidance on:
  - How each view should be structured visually.
  - How Tailwind utility classes can be used to achieve the layouts.
  - Where and how to incorporate Schema.org markup for products and navigation.

## Views covered in the solution

- **Home page**:
  - Hero section introducing the brand and a primary CTA.
  - New arrivals and best‑seller product strips using card patterns.
  - Suggestions for `Organization`, `ClothingStore`, `WebSite` and `SearchAction` schema.
- **Catalog**:
  - Filter bar with category and size filters.
  - Responsive product grid (multi‑column on desktop, stacked on mobile).
  - Suggestions for `ItemList` and `ListItem` schema around product listings.
- **Product view**:
  - Two‑column layout on desktop (image + details).
  - Clear "Add to cart" CTA, sizes, price, and description.
  - Suggestions for `Product` with nested `Offer` and breadcrumb structure.
- **Cart**:
  - List of cart items with quantity controls and line totals.
  - Summary box with subtotal, tax, and total.
  - Conceptual use of `Cart` / `ItemList` schema to represent the cart contents.
- **Checkout / Payment form**:
  - Three logical steps: personal details, shipping address, and payment details (visual only).
  - Clear final CTA to complete the order.
  - Suggestions for `CheckoutPage` schema.

## How to read and use the solution

- Treat `solution.md` as a **design and structure guide**, not as single HTML source:
  - It tells you which sections and components must exist.
  - It gives examples of Tailwind utilities and semantic markup patterns.
  - It indicates where structured data can add value.
- When evaluating a student implementation, check whether:
  - All five views exist and follow the described intent.
  - Layouts are responsive and visually coherent across breakpoints.
  - Reusable components (navbar, footer, product cards) are consistent.
  - Schema.org suggestions are at least partially implemented where relevant.
