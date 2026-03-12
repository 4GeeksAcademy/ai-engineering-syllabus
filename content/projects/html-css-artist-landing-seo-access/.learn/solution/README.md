# Artist landing – HTML, CSS, SEO and accessibility – Reference solution

This README describes the reference implementation for the **"Artist landing: HTML, CSS, SEO and accessibility"** project and links to the canonical solution files in the repository.

## Repository location of the main solution files

The main HTML and CSS implementation of the solution lives at:

- [Solution HTML](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/html-css-artist-landing-seo-access/.learn/solution/solution.html)
- [Solution CSS](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/html-css-artist-landing-seo-access/.learn/solution/solution.css)

Use these files as the canonical reference when comparing or reviewing solutions.

## What the reference solution shows

- A **single‑page artist landing** built with semantic HTML and custom CSS.
- A focus on:
  - **Accessibility** (landmarks, skip link, alt text, focus states).
  - **SEO** (meta tags, meaningful titles, structured data).
  - **Visual hierarchy** and clean layout for an artist portfolio.
- A structure that typically includes:
  - A top **navigation bar** with internal links (About, Career, Shows).
  - A **hero section** with a strong visual, artist name, and call‑to‑action.
  - An **About** section describing the artist.
  - A **Career / Discography** section with highlighted works.
  - An **Upcoming shows / Events** section with dates and venues.
  - A **Footer** with additional links and social profiles.

## Accessibility aspects to look for

- Use of **semantic landmarks**:
  - `header`, `nav`, `main`, `section`, `footer`.
  - A "skip to main content" link visible on focus.
- Appropriate **heading hierarchy**:
  - One main `h1` for the page.
  - Subsequent sections using `h2`, `h3`, etc. in logical order.
- **Alt text** for images:
  - Descriptive alt attributes for meaningful images.
  - Empty alt (`alt=""`) only for purely decorative images.
- Keyboard‑friendly design:
  - Focusable navigation links.
  - Visible focus states for interactive elements.

## SEO and Schema.org aspects to look for

- Basic SEO meta tags:
  - `title` with artist name and role.
  - `meta name="description"` describing the page content.
- **Schema.org structured data** using JSON‑LD:
  - `Person` describing the artist (name, jobTitle, description, image, url).
  - `CreativeWork` for at least one highlighted work (e.g. album or single).
  - `Event` for at least one upcoming show (name, startDate, location, performer).
- Clean, descriptive URLs and link texts where applicable.

## How to read and use the solution

- Use `solution.html` and `solution.css` as a **reference for structure and best practices**, not as a template to copy directly.
- When evaluating a student solution, check whether:
  - The overall layout and sections roughly mirror the same intent (hero, about, career/works, shows).
  - Accessibility features (skip link, landmarks, headings, alt text) are implemented.
  - SEO concerns (meta description, meaningful title, Schema.org block) are addressed.
- Encourage improvements that keep the **same requirements** but allow different creative design choices (colors, imagery, specific copy).
