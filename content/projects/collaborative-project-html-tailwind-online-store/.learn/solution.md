# Reference solution outline (e-commerce prototype)

This document describes the reference structure for the collaborative e-commerce prototype using **HTML + Tailwind CSS** and **Schema.org**. It is not a full copy-paste implementation, but a detailed blueprint students (or an LLM) can compare against.

## Global layout and components

- **Shared layout**:
  - A base HTML structure with Tailwind via CDN (`<script src="https://cdn.tailwindcss.com"></script>`).
  - A dark header and light page background, mobile-first with responsive breakpoints (`sm:`, `md:`, `lg:`).
  - Reusable **navbar** and **footer** included on all 5 views using the same HTML snippet.
- **Navbar (top bar)**:
  - Left: brand logo + brand name.
  - Center: search input for products (used in Home and Catalog; optional in other views).
  - Right: user account icon / text link and cart icon with item count.
- **Footer**:
  - Three columns on desktop, stacked on mobile:
    - **Categories**: links to footwear, shirts, pants, accessories.
    - **Legal**: terms, privacy policy, about the brand.
    - **Contact**: email, address or contact link.

## View 1 – Home page

- **Main sections (top to bottom)**:
  - Hero section with:
    - Brand tagline and short description.
    - Main CTA button (e.g. "Shop new collection").
    - Background image or highlighted product image.
  - **New arrivals** horizontal list:
    - Tailwind grid or horizontal scroll of 4–6 product cards.
  - **Best sellers** horizontal list:
    - Same card pattern as new arrivals; just different heading.
- **Cards structure** (both lists):
  - Product image, name, price, short label ("New", "Bestseller").
  - "View product" link/button.
- **Schema.org suggestions**:
  - `Organization` or `ClothingStore` for the brand (name, url, logo, social links).
  - `WebSite` with a `SearchAction` for the site search box.
  - Optional `BreadcrumbList` for simple path: Home.

## View 2 – Catalog

- **General layout**:
  - Reuses navbar and footer.
  - Two main vertical blocks:
    - Filter bar.
    - Product grid.
- **Filter bar** (top of main content):
  - Two `<select>` or custom Tailwind-styled dropdowns:
    - Filter by **category**.
    - Filter by **size**.
  - On mobile: filters stacked; on desktop: filters on one row.
- **Product grid**:
  - Desktop: `grid grid-cols-4 gap-6` (4×5 grid as reference); fewer columns on small screens.
  - Each card:
    - Product image (fixed ratio, e.g. `aspect-[4/5]`).
    - Name, short description.
    - Price.
    - Link to product view.
- **Schema.org suggestions**:
  - Use `ItemList` for the product listing.
  - Each product card referenced as a `ListItem` with `position` and nested `Product`.
  - `BreadcrumbList` path: Home › Category.

## View 3 – Product view

- **Layout**:
  - Two-column layout on desktop, stacked on mobile.
  - Left: big product image (~50% width on large screens).
  - Right: product info block:
    - Name.
    - Reference / SKU.
    - Available sizes (buttons or dropdown).
    - Price.
    - Quantity selector.
    - **"Add to cart"** primary button.
  - Below: **Detailed description** section with:
    - Materials and care.
    - Recommended use / occasions.
- **Schema.org suggestions**:
  - Use `ItemPage` or `WebPage` with `mainEntity` a `Product`.
  - `Product` with nested `Offer` (price, currency, availability) and optional rating.
  - `BreadcrumbList` path: Home › Category › Product.

## View 4 – Cart

- **Layout**:
  - Full-width main area with:
    - Left: list of cart items.
    - Right: summary box.
- **Cart items list**:
  - Each row includes:
    - Thumbnail image.
    - Product name and selected size.
    - Unit price.
    - Quantity control.
    - Line total.
  - At least **3 sample products** to show behavior.
- **Summary box**:
  - Subtotal.
  - Tax.
  - Total.
  - **"Purchase"** button (goes to checkout).
- **Schema.org suggestions**:
  - Use `Cart` (extension of `ItemList`) to represent current cart.
  - `itemListElement` items reference `Product` or `Offer` for each line.

## View 5 – Payment form (Checkout)

- **3-step flow** (can be in one page with clear sections):
  1. **Personal details**: name, email, phone.
  2. **Shipping address**: street, city, postal code, country.
  3. **Card payment**: card holder, card number, expiry date, CVC (visual only; no real processing).
- **UX structure**:
  - On desktop: steps can be in a single form with step headers.
  - On mobile: stack sections with clear titles.
  - Clear primary CTA at the end ("Complete order").
- **Schema.org suggestions**:
  - Mark page as `CheckoutPage` (subtype of `WebPage`).
  - Use `Order` only conceptually (not required in markup for this exercise), or mention it as future extension.

## Tailwind and responsiveness

- **Mobile-first**:
  - Base classes for mobile, and `sm:`, `md:`, `lg:` utilities to enhance layout for larger screens.
- **Common patterns**:
  - Layout: `container mx-auto px-4`, `grid`, `flex`, `gap-*`.
  - Typography: `text-slate-900` on light backgrounds, `text-slate-50` on dark sections.
  - Components: cards with `rounded-xl`, `shadow`, `border`.

## Schema.org recap for the project

Students should aim to include at least:

- `Organization` / `ClothingStore` on the home (brand information).
- `WebSite` with `SearchAction` for the navbar search.
- `BreadcrumbList` on catalog and product views.
- `Product` + `Offer` on the product view.
- `ItemList` or `Cart` semantics for catalog and cart pages.

Comparing against this outline, a solution is "on track" if:

- All five views exist and are linked.
- Navbar and footer are consistent.
- Layout is responsive and visually modern in Tailwind.
- The HTML is semantic and compatible with these Schema.org patterns.
