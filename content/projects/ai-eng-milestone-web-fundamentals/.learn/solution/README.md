# Milestone 1 — Your Company's Public Website — Reference Solution

## Purpose

Reference quality bar for the company's **first public website**: semantic landing page, CONTEXT-driven application form, Tailwind styling, accessibility, Schema.org, and client-side validation. No backend required.

## Expected File Structure

```text
/
├── index.html          # landing page
├── application.html    # sign-up / application form
├── validation.js       # all form validation logic
└── CONTEXT.md          # company-specific fields (from syllabus contexts)
```

Serve during development (Codespaces-compatible):

```bash
npx http-server . -p 3000 -a 0.0.0.0
```

Deploy to Vercel (or similar) before running PageSpeed Insights — Codespaces URLs block Lighthouse.

## Required Coverage (From README)

### Landing (`index.html`)

- Semantic HTML5: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- Hero with value proposition; ≥2 content sections; CTA to application form.
- Tailwind utility classes; responsive breakpoints (`sm:`, `md:`, `lg:`).
- Mobile-first layout; descriptive `alt` on images.
- Schema.org `Organization` or `LocalBusiness` JSON-LD.
- ARIA where it improves accessibility (`aria-label`, landmarks).

### Application form (`application.html`)

- All fields from student's **CONTEXT.md** with correct `name`, `type`, and labels.
- `<label for="...">` on every input; `<fieldset>`/`<legend>` for grouped fields.
- `required` on mandatory fields; submit + clear buttons.
- Tailwind focus/error/success states.

### Validation (`validation.js`)

- Real-time or `blur` validation per field.
- Specific error messages — not generic "invalid field".
- Block submit when invalid; show success message on valid simulated submit.
- CONTEXT-specific rules (email format, phone, date ranges, domain enums).

## Indicative Schema.org Block

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Your Company Name",
    "url": "https://your-deployed-site.example",
    "logo": "https://your-deployed-site.example/logo.png",
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "customer service",
      "email": "contact@example.com"
    }
  }
</script>
```

Adapt `@type` and properties to the company sector in CONTEXT.

## Indicative Validation Pattern

```javascript
function validateEmail(value) {
  if (!value.trim()) return "Email is required.";
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!pattern.test(value)) return "Enter a valid email address.";
  return null;
}

function showFieldError(inputId, message) {
  const input = document.getElementById(inputId);
  const errorEl = document.getElementById(`${inputId}-error`);
  if (message) {
    input.setAttribute("aria-invalid", "true");
    errorEl.textContent = message;
    errorEl.hidden = false;
  } else {
    input.removeAttribute("aria-invalid");
    errorEl.textContent = "";
    errorEl.hidden = true;
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const errors = collectValidationErrors();
  if (errors.length > 0) return;
  showSuccessMessage();
});
```

Wire one validator per CONTEXT field; map errors to visible elements with `aria-describedby` where appropriate.

## Responsive / Tailwind Checklist

- [ ] No hand-written CSS except rare overrides.
- [ ] Readable typography and spacing on 320px viewport.
- [ ] Navigation usable on mobile (stacked or hamburger if needed).
- [ ] Form inputs full-width on small screens.

## PageSpeed / Performance

- Target **≥ 80** on PageSpeed Insights (ideal **> 90**) on deployed URL.
- Optimise images (reasonable dimensions, modern formats).
- Minimise render-blocking scripts; load `validation.js` with `defer` where possible.

## Evaluation Checklist

- [ ] Semantic structure and Schema.org present.
- [ ] Fully responsive Tailwind layout; documented `npx http-server` command works.
- [ ] Keyboard-accessible navigation and form controls.
- [ ] All CONTEXT form fields implemented with matching validation rules.
- [ ] Error messages specific; submit blocked until valid.
- [ ] Landing content reflects company sector and tone from CONTEXT.
- [ ] PageSpeed score ≥ 80 on public deployment URL.

## Reviewer Notes

- Field names and domain values must match CONTEXT — generic forms fail context adherence criteria.
- `CONTEXT.md` in the student repo should remain the syllabus copy or a faithful import.
- Accept different section naming on the landing page if structure and intent are met.
