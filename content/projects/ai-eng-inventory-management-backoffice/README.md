# Milestone 5 — Backoffice: Inventory Management Interface

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/05-backend-development)** before writing any component — it defines the entity names, field labels, business constraints, and domain vocabulary that must appear in the UI.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The backend team completed the inventory API and issued a **handoff** to the product team: all `/inventory` endpoints are live, authenticated, and documented. Now the operations manager has filed a **brief** with the technology unit — the staff who manage stock day to day need a working interface inside the backoffice. Until there is one, the API exists but nobody can use it without a REST client.

Your job is to build the inventory section of the backoffice: a set of views that let authenticated staff see what is in stock, register deliveries, log consumption or exits, and review the full order history — all talking to the API you built in the backend project.

This is an internal tool, not a public-facing page. The people using it are operations staff, not customers. That shapes every decision: clarity and speed matter more than marketing polish. An operations manager logging a delivery at 7am has zero patience for a broken form or a cryptic error message.

Two requirements are embedded in the brief that are easy to miss: the outbound order form must **show the current available stock** for the selected product before the user submits, and any `400` response from the API must surface a **readable error message** to the user — not a raw JSON object or a silent failure.

### Brief from your manager

> > **From:** Operations Manager
> > **To:** Technology Unit
> >
> > The backend team shipped the inventory API last sprint — great work. Now I need the interface. My team can't use Postman to log deliveries.
> >
> > Here's what I need in the backoffice:
> >
> > 1. A page that shows all products with their current stock. Color-code it — I want to see at a glance what is low.
> > 2. A form to register an inbound order (a delivery we received).
> > 3. A form to register an outbound order (a consumption or exit). It must show how much stock is available before I submit, so I don't accidentally log more than we have.
> > 4. A read-only page showing all orders — entries and exits — with the product name and who created each one.
> >
> > All of these pages require login. If a user is not authenticated, redirect them to the login page.
> >
> > **Acceptance criteria**: all four views functional, authenticated, consuming live API data, with correct error handling on API failures.

---

## 🌱 How to Start the Project

The backoffice frontend already exists in your monorepo. You are adding the inventory section to it, not creating a new app.

1. Open your existing repository (forked from `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo`).
2. Navigate to `uis/backoffice` — this is where your Next.js backoffice lives.
3. Install dependencies if needed:
   ```bash
   npm install
   ```
4. Add the inventory API base URL to your `.env.local`. It should point to your running backend:
   ```
   NEXT_PUBLIC_INVENTORY_API_URL=http://localhost:8000
   ```
5. Read your **CONTEXT-company.md** — entity names, field labels, and domain vocabulary must match what is in the API and in the UI.
6. Make sure the backend service (`services/`) is running locally before testing the frontend.

---

## 💻 What You Need to Do

### API integration layer

- [ ] Create a module (e.g., `lib/inventory.ts`) that centralises all calls to the `/inventory` endpoints. No component should call `fetch` directly.
- [ ] All requests to protected endpoints must include the `Authorization: Bearer <token>` header. Read the token from wherever your existing auth stores it (localStorage, context, cookie).
- [ ] Handle API errors explicitly: if the response status is `4xx` or `5xx`, extract the error message from the response body and surface it to the user — never swallow errors silently.

### Products page — `/backoffice/inventory/products`

- [ ] Fetch and display all products from `GET /inventory/products`.
- [ ] Show the `current_stock` value for each product alongside the entity-specific fields defined in your CONTEXT.md.
- [ ] Apply visual stock-level indicators: use colour or iconography to distinguish healthy stock from low stock. Define your own thresholds — document them in a comment.
- [ ] Include a clearly labelled link or button from each product row to create an inbound or outbound order for that product.

### Inbound order form — `/backoffice/inventory/orders/inbound`

- [ ] Render a form that submits to `POST /inventory/orders/inbound`.
- [ ] The product selector must list all available products by name. Do not ask the user to type a raw ID.
- [ ] On successful submission, clear the form and show a confirmation message. On `400`/`500`, display the API's error message in a visible element — not only in the console.
- [ ] The form must be protected: redirect unauthenticated users to the login page.

### Outbound order form — `/backoffice/inventory/orders/outbound`

- [ ] Render a form that submits to `POST /inventory/orders/outbound`.
- [ ] When the user selects a product, fetch and display its `current_stock` before they enter a quantity. This must update reactively when the product selection changes.
- [ ] If the entered quantity exceeds the displayed stock, show a client-side warning before the user submits. This is a UX guard — the API enforces the real rule.
- [ ] Handle the `HTTP 400` from the API (insufficient stock) by displaying the error message inline near the quantity field.

### Orders history page — `/backoffice/inventory/orders`

- [ ] Fetch and display all orders from `GET /inventory/orders`.
- [ ] Each row must show: product name, quantity, order type (inbound or outbound), creation date, and the `user_uuid` that created it.
- [ ] Display inbound and outbound orders with a visual distinction (e.g., colour, icon, or label).
- [ ] This page is read-only. No delete or edit actions.

### Route protection

- [ ] All four inventory pages must redirect unauthenticated users to the login page. Use the same auth check pattern already in place in the backoffice.

⚠️ **IMPORTANT:** Entity names, field labels, and vocabulary in the UI must match what is specified in your CONTEXT.md — use your company's domain language, not the generic terms in this README.

---

## ✅ What We Will Evaluate

- [ ] A dedicated API integration module exists — no raw `fetch` calls inside components.
- [ ] All requests to protected endpoints include the `Authorization` header with the current user's token.
- [ ] The products page loads live data from the API and displays `current_stock` with visual stock-level indicators.
- [ ] The inbound order form submits correctly and shows a confirmation or a readable error message on every outcome — no silent failures.
- [ ] The outbound order form displays the current stock for the selected product reactively, before the user submits.
- [ ] The outbound order form shows a client-side warning when the entered quantity exceeds available stock.
- [ ] A `400` response from the outbound endpoint surfaces the API's error message visibly in the UI.
- [ ] The orders history page displays all orders with inbound/outbound distinction, product name, quantity, date, and `user_uuid`.
- [ ] All four pages redirect unauthenticated users to login.
- [ ] Entity names and field labels in the UI match the CONTEXT.md specification.

---

## 📦 How to Submit

1. Commit and push all changes to your fork.
2. Confirm `.env.local` is in `.gitignore` — never commit API URLs or tokens.
3. Submit the URL of your fork via the student platform.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
