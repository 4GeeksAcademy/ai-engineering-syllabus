# Milestone 1 — Your Company's Public Website

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your here: **[CONTEXT.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing any code — it defines the specific company data, field names, domain values, and constraints for your implementation. Also read the [instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

---

## 🎯 The Challenge. Are you ready?

Your company has been successfully operating in a traditional way for years, but the world has changed. Customers search for information online before making decisions. Competitors already have a digital presence. And your company, despite its experience and quality, remains invisible on the internet.

Management has decided to begin the digital transformation. Your task is to build the company's first digital touchpoint: a professional public website that presents what they do and captures information from interested people through an application or sign-up form.

This site must work on any device, meet web accessibility standards, be optimized for search engines, and deliver a polished, professional user experience. It's not just "a pretty page" — it's the first step toward modernizing a company that wants to remain relevant.

### 📋 Manager's Brief

> **From:** Your Manager  
> **To:** You  
> **Subject:** Public website — first version
>
> Hi,
>
> As you know, we've decided to make the leap to digital. We need to launch our public website as soon as possible. Check the `CONTEXT.md` to understand exactly what our company does and what information we need to capture from interested people.
>
> The site should have two parts:
>
> **1. Landing page** — A presentation page with:
>
> - Header with clear navigation
> - Hero section explaining what we do and why they should choose us
> - Section highlighting our main features or key benefits (based on our industry experience)
> - Contact information or call to action
> - Professional footer
>
> **2. Application/sign-up form** — A separate page where people can:
>
> - Fill in their personal details
> - Provide the specific information we need (see `CONTEXT.md`)
> - Submit their application (you don't need to connect it to anything yet, just validate the data)
>
> **Technical requirements you must meet:**
>
> - Responsive: must look good on mobile, tablet, and desktop
> - Accessible: use semantic HTML, ARIA tags when needed, and alt attributes on images
> - SEO optimized: implement Schema.org to mark up company information
> - Full form validation with JavaScript — all fields must be validated before "submitting"
> - Clear error messages when something isn't correct
>
> Use Tailwind CSS for all design. I don't want to see custom hand-written CSS unless it's absolutely necessary.
>
> Make it professional. This is our digital debut and we want to make a good impression.
>
> Best,  
> Your Manager

---

## 🌱 How to Start This Project

Do not clone this repository because we are going to use a different template.

1. Go to your company project repository that you already have. If you haven't created it yet, go to the [transversal project template repository](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) and click the "Use this template" button on the right, then select [Create a new repository](https://github.com/new?template_name=ai-engineering-company-project-monorepo&template_owner=4GeeksAcademy).

2. Once you have your own repository, open it in a Codespace or clone it locally.

3. Read your [`CONTEXT.md`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/01-web-fundamentals) file completely — it contains your company's specific data, the exact fields your form must include, and any domain-specific validation rules or constraints.

4. Create the basic structure of your project:

   ```markdown
   /
   ├── index.html (landing page)
   ├── application.html (application/sign-up form)
   ├── styles.css (only if Tailwind CDN isn't enough)
   └── validation.js (form validation logic)
   ```

5. Start with the landing page HTML structure, then add Tailwind styles, then work on the form, and finally implement validation.

---

## 💻 What You Need to Do

### Landing Page

- [ ] Create `index.html` with semantic HTML5 structure
- [ ] Implement a `<header>` with company logo/name and navigation
- [ ] Create a hero section that presents the company and its value proposition
- [ ] Add at least two additional sections (features, benefits, how it works, experience, etc.)
- [ ] Implement a `<footer>` with contact information
- [ ] Include a link/button that directs to the application form
- [ ] Apply styles with Tailwind CSS using utility classes
- [ ] Make the design responsive with breakpoints for mobile, tablet, and desktop
- [ ] Implement mobile-first design
- [ ] Add descriptive `alt` tags to all images
- [ ] Use semantic HTML tags (`<section>`, `<article>`, `<nav>`, etc.)
- [ ] Implement ARIA attributes where appropriate (`aria-label`, `role`)
- [ ] Add Schema.org markup for company information (Organization or LocalBusiness type)

### Application/Sign-up Form

- [ ] Create `application.html` with a structured form
- [ ] Include the fields specified in your `CONTEXT.md`
- [ ] Use appropriate input types (`email`, `tel`, `date`, `number`, etc.)
- [ ] Add `<label>` correctly associated with each input (using `for` attribute)
- [ ] Group related fields using `<fieldset>` and `<legend>` where appropriate
- [ ] Mark required fields with the `required` attribute
- [ ] Implement responsive form design
- [ ] Apply Tailwind styles for the form (spacing, sizes, focus states)
- [ ] Add submit button and secondary button to clear the form
- [ ] Create `validation.js` to validate all form fields
- [ ] Implement real-time validation (as the user types or on blur)
- [ ] Display specific error messages for each type of validation
- [ ] Style error messages clearly and visibly
- [ ] Prevent form submission if there are validation errors
- [ ] Show a success message when validation is correct (simulate submission)

⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

---

## ✅ What We Will Evaluate

### HTML Structure and Semantics

- [ ] HTML uses appropriate semantic tags instead of generic `<div>`s
- [ ] All images have descriptive `alt` attributes
- [ ] Forms use `<label>` correctly associated with inputs
- [ ] Schema.org markup is present and correctly implemented
- [ ] Document structure is logical and hierarchical

### Responsive Design and Tailwind

- [ ] The site is fully responsive (adapts to mobile, tablet, and desktop)
- [ ] Mobile-first design is used
- [ ] All styles use Tailwind utility classes
- [ ] Tailwind breakpoints (`sm:`, `md:`, `lg:`) are used appropriately
- [ ] There is no unnecessary custom CSS (only Tailwind)
- [ ] The design is visually coherent and professional
- [ ] Performance is verified on the public URL with [PageSpeed Insights](https://pagespeed.web.dev/) with a minimum score of **80** (ideal: **above 90**). You will have to publish your page to vercel in order to run google page speed because Codespaces has a warning message that blocks google page speed from visiting your website. 

### Accessibility

- [ ] All interactive elements are keyboard accessible
- [ ] ARIA attributes are used where they improve accessibility
- [ ] Color contrast meets minimum standards
- [ ] Navigation is logical and predictable
- [ ] Error messages are announced appropriately

### Form and Validation

- [ ] All fields specified in CONTEXT.md are present
- [ ] Input types are appropriate for each field
- [ ] JavaScript validation works correctly for all fields
- [ ] Error messages are specific and helpful (not just "invalid field")
- [ ] Validation prevents submission of incorrect data
- [ ] Form visual states are clear (focus, error, success)
- [ ] The clear form button works correctly

### Context Adherence

- [ ] The landing page faithfully reflects the company type and sector specified in CONTEXT.md
- [ ] Content presents the company's experience and competitive advantages
- [ ] Form fields exactly match those required in CONTEXT.md
- [ ] Any domain-specific validation rules are implemented
- [ ] Tone and content are consistent with an established company going digital

---

## 📦 How to Submit

1. Make sure your code is pushed to your repository

2. Verify that the main files are present:
   - `index.html`
   - `application.html`
   - `validation.js`
   - `CONTEXT.md` (unmodified)

3. Test your site by opening `index.html` in different browser window sizes

4. Test all form validations to ensure they work

5. Submit the URL of your repository for evaluation

**Tip:** Use browser DevTools (F12) to test different screen sizes and verify there are no console errors.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. Find out more about our programs: [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [Full-Stack Software Development with AI](https://4geeksacademy.com/en/career-programs/full-stack).
