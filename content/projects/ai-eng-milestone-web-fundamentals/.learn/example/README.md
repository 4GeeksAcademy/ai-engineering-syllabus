# In-Class Example — Local Bakery Website

> **Instructor note:** This is a classroom-paced example to introduce the same concepts as the graded project (Milestone 1). Use a different domain so students don't confuse it with their own work. A bakery is a concrete, familiar business that everyone can reason about — ideal for a live coding session.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


**Sweet Corner Bakery** has been baking artisan bread and pastries in the same neighborhood for 12 years. Their customers know them by word of mouth, but they have zero online presence. The owner wants two things:

1. A professional landing page that shows what they make and where they are.
2. A custom order form where customers can pre-order a cake or catering box for an event.

No backend is needed yet — just validate the form with JavaScript and show a success message.

---

## What to Build

### File structure

```
/
├── index.html        ← landing page
├── order.html        ← custom order form
└── validation.js     ← all form validation logic
```

Serve with: `npx http-server . -p 3000 -a 0.0.0.0`

---

### Landing Page (`index.html`)

- [ ] `<header>` with the bakery name and navigation links to the sections below and to `order.html`.
- [ ] Hero section: tagline ("Artisan bread baked fresh every morning"), a short description, and a CTA button linking to the order form.
- [ ] Features section: at least 3 items (e.g. "No artificial preservatives", "Baked daily", "Custom orders welcome") with an icon or emoji.
- [ ] Location & hours section with address and opening times.
- [ ] `<footer>` with contact email and social links.

**Technical requirements:**

- [ ] Use semantic HTML tags: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- [ ] All images have descriptive `alt` attributes.
- [ ] ARIA attributes where they help (`aria-label` on the nav, `role="banner"` on the header if needed).
- [ ] Schema.org markup for the bakery as a `LocalBusiness`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Bakery",
  "name": "Sweet Corner Bakery",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "14 Maple Street",
    "addressLocality": "Springfield"
  },
  "openingHours": "Mo-Sa 07:00-19:00",
  "telephone": "+1-555-0183"
}
</script>
```

- [ ] All styles use **Tailwind CSS** (CDN is fine for class). No hand-written CSS unless strictly necessary.
- [ ] Responsive: looks correct on mobile (`sm:`), tablet (`md:`), and desktop (`lg:`).

---

### Order Form (`order.html`)

The owner needs to capture these fields from customers:

| Field | Input type | Required | Validation rule |
|---|---|---|---|
| Full name | `text` | Yes | Min 2 characters |
| Email | `email` | Yes | Valid email format |
| Phone | `tel` | Yes | 7–15 digits |
| Event date | `date` | Yes | Must be at least 3 days from today |
| Number of guests | `number` | Yes | Between 5 and 500 |
| Product type | `select` | Yes | Cake / Catering box / Bread assortment |
| Special requests | `textarea` | No | Max 300 characters |

- [ ] Each field has a `<label>` correctly linked with `for` / `id`.
- [ ] Group "Event details" fields with `<fieldset>` and `<legend>`.
- [ ] Mark required fields visually and with the `required` attribute.
- [ ] **Submit** button and a **Clear** button that resets the form.
- [ ] Responsive form layout.

---

### Validation (`validation.js`)

- [ ] Validate every required field on **blur** (when the user leaves the field).
- [ ] Show a specific error message below each field, not a generic alert.
- [ ] Prevent form submission if any field is invalid.
- [ ] After all validations pass, show a success message: *"Your order request has been received! We'll contact you within 24 hours."*
- [ ] Style error state: red border + red error text. Style success state: green border.

**Example error messages:**

```
Full name: "Please enter your full name (at least 2 characters)."
Email: "Please enter a valid email address."
Event date: "Please choose a date at least 3 days from today."
Number of guests: "Please enter a number between 5 and 500."
```

---

## Key Concepts to Discuss in Class

| Concept | Where it appears |
|---|---|
| Semantic HTML | `<section>`, `<article>`, `<nav>` on the landing page |
| Schema.org structured data | `<script type="application/ld+json">` |
| Tailwind responsive breakpoints | `sm:`, `md:`, `lg:` classes |
| `<fieldset>` + `<legend>` | Grouping event detail fields |
| JS form validation (blur events) | `validation.js` |
| Preventing default form submission | `event.preventDefault()` in JS |
| ARIA for accessibility | `aria-describedby` on fields with errors |

---

## Discussion Questions

1. Why do we use semantic tags like `<section>` and `<article>` instead of `<div>` everywhere? Who benefits from this choice — users, developers, or search engines?
2. The event date validation needs to calculate "3 days from today" dynamically. How would you write that check in JavaScript without a library?
3. If we wanted to actually send the form data to a server later, what would we need to add or change? What stays the same?
