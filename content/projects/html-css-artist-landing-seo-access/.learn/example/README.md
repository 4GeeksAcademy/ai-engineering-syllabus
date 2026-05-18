> **In-class example for instructors.** Use this scenario to introduce semantic HTML, Flexbox, accessibility, and Schema.org in a ~1–2 hour session. This file is a teaching aid with a *different domain* than the assigned project. Do not share this with students as their project brief.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

# Chef's Personal Website — HTML, CSS, SEO & Accessibility (In-Class Example)

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A freelance chef named Marco Rossi does private dinners and pop-up events. He has asked you to build a simple landing page so clients can find him online and get in touch.

After a short conversation, you both agree on the following structure:

> The page will have a **navigation bar** with links to three sections: About, Experience, and Upcoming Events. The first section will be a **hero** that greets visitors and introduces the chef. Each section should feel like a full "page" — roughly the height of the viewport. The footer will include a contact email.

The site must work for everyone, including users who rely on screen readers. It must also be discoverable by search engines using Schema.org structured data.

---

## Agreed Page Structure

| Section | Content |
|---------|---------|
| `<header>` / `<nav>` | Logo/name + links to `#about`, `#experience`, `#events` |
| Hero (`<section id="hero">`) | Chef's name, tagline, short intro |
| About (`<section id="about">`) | Bio paragraph, photo placeholder with `alt` text |
| Experience (`<section id="experience">`) | List of past venues or notable dishes |
| Upcoming Events (`<section id="events">`) | 2–3 event cards (date, location, description) |
| `<footer>` | Contact email |

---

## Checklist

### Structure & Semantic HTML

- [ ] Create `index.html` with a valid document outline (`<!DOCTYPE html>`, `<html lang="en">`, `<head>`, `<body>`)
- [ ] Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` — avoid using only `<div>`
- [ ] Each section has an `id` that matches the nav links (smooth-scroll anchor)
- [ ] Heading hierarchy is correct: one `<h1>` → `<h2>` per section → `<h3>` inside sections if needed

### Layout & Styles

- [ ] Create a separate `styles.css` file, linked from `index.html`
- [ ] Each section takes up approximately `100vh`
- [ ] Use **Flexbox** for layout (navbar, hero, event cards grid) — no `float` or `inline-block` for structure
- [ ] The nav links are horizontally aligned on desktop

### Accessibility

- [ ] The `<nav>` element has `aria-label="Main navigation"`
- [ ] All images have descriptive `alt` attributes
- [ ] Interactive elements (links, buttons) are keyboard-focusable and visible on focus
- [ ] Color contrast meets minimum readability

### SEO / Schema.org

- [ ] Add a `<title>` and `<meta name="description">` in `<head>`
- [ ] Add Schema.org structured data as a `<script type="application/ld+json">` block describing the chef as a `Person` with `jobTitle`, `name`, and `email`

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Marco Rossi",
  "jobTitle": "Freelance Chef",
  "email": "mailto:marco@example.com",
  "url": "https://marcorossi.example.com"
}
```

### File Organization

- [ ] `index.html` and `styles.css` are in the project root and correctly linked

---

## Discussion Questions

1. What is the difference between using `<div id="about">` and `<section id="about" aria-labelledby="about-title">`? Why does it matter for screen reader users?
2. The chef wants to add a contact form later. Which HTML element would you use, and what `aria` attributes would improve its accessibility?
3. Why does Google care about Schema.org markup? What does a `Person` schema tell a search engine that a plain `<h1>Marco Rossi</h1>` does not?
