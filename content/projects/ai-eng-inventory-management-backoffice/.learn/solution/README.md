# Milestone 5 — Backoffice: Inventory Management Interface (reference solution)

This README is the canonical reference for **"Milestone 5 — Backoffice: Inventory Management Interface"**. It describes how a correct backoffice implementation should be structured, how it should talk to the inventory REST API built in the backend milestone, and what reviewers should verify. The actual app lives in the student monorepo under `uis/backoffice/`; this folder documents the expected design only.

## Alignment with company briefing

All user-visible labels, entity names, and field copy must follow the student’s assigned **company-BRIEFING.md**. The API field names are defined by the backend; the UI should map those to the terminology required by the scenario (not generic placeholders like “Product” when BRIEFING says “SKU” or “Item”).

## Recommended solution structure

A reference implementation should organize the Next.js backoffice app roughly as follows:

- `app/backoffice/inventory/products/page.tsx` — product list with stock indicators
- `app/backoffice/inventory/orders/inbound/page.tsx` — inbound order form
- `app/backoffice/inventory/orders/outbound/page.tsx` — outbound order form with live stock
- `app/backoffice/inventory/orders/page.tsx` — read-only order history
- `lib/inventory.ts` — **single module** for all `/inventory` API calls (no `fetch` in components)
- `components/inventory/` — presentational pieces (product row, stock badge, order form, error banner)
- `types/inventory.ts` — TypeScript types for products, orders, and API error payloads

Reuse the existing backoffice auth pattern (layout guard, middleware, or client-side redirect) — do not invent a parallel auth system.

## Environment and API base URL

- Read the inventory API base from `process.env.NEXT_PUBLIC_INVENTORY_API_URL` (normalize trailing slash in one place).
- Never commit secrets; document `NEXT_PUBLIC_INVENTORY_API_URL` in `.env.example`.
- The backend service (`services/`) must be running locally before testing the frontend.

## REST contract the solution must implement

Assuming the API is mounted at `{NEXT_PUBLIC_INVENTORY_API_URL}`:

| Action            | Method | Path                         | Auth   | Notes                                             |
| ----------------- | ------ | ---------------------------- | ------ | ------------------------------------------------- |
| List products     | `GET`  | `/inventory/products`        | Bearer | Returns products with computed `current_stock`    |
| Get one product   | `GET`  | `/inventory/products/{id}`   | Bearer | Used for reactive stock on outbound form          |
| Register inbound  | `POST` | `/inventory/orders/inbound`  | Bearer | Body: `product_id`, `quantity` (+ BRIEFING fields) |
| Register outbound | `POST` | `/inventory/orders/outbound` | Bearer | Body: `product_id`, `quantity` (+ BRIEFING fields) |
| List all orders   | `GET`  | `/inventory/orders`          | Bearer | Combined inbound/outbound with product name       |

Every protected call must include:

```http
Authorization: Bearer <token>
```

Read the token from wherever the existing backoffice auth stores it (localStorage, React context, or cookie).

## Suggested `lib/inventory.ts` pattern

Centralize headers, auth, and error extraction once:

```ts
type ApiError = { detail?: string; message?: string };

async function inventoryFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const base = process.env.NEXT_PUBLIC_INVENTORY_API_URL!.replace(/\/$/, "");
  const token = getAuthToken(); // reuse existing backoffice helper

  const res = await fetch(`${base}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...init?.headers,
    },
  });

  if (!res.ok) {
    let message = res.statusText;
    try {
      const body = (await res.json()) as ApiError;
      message = body.detail ?? body.message ?? message;
    } catch {
      // keep statusText if body is not JSON
    }
    throw new Error(message);
  }

  if (res.status === 204) return undefined as T;
  return res.json() as Promise<T>;
}

export const listProducts = () =>
  inventoryFetch<Product[]>("/inventory/products");
export const getProduct = (id: number) =>
  inventoryFetch<Product>(`/inventory/products/${id}`);
export const createInboundOrder = (body: InboundOrderCreate) =>
  inventoryFetch<Order>("/inventory/orders/inbound", {
    method: "POST",
    body: JSON.stringify(body),
  });
export const createOutboundOrder = (body: OutboundOrderCreate) =>
  inventoryFetch<Order>("/inventory/orders/outbound", {
    method: "POST",
    body: JSON.stringify(body),
  });
export const listOrders = () =>
  inventoryFetch<OrderListItem[]>("/inventory/orders");
```

Components catch `Error` from this layer and render the message in a visible UI element — never only `console.error`.

## Products page (`/backoffice/inventory/products`)

**Data:** `GET /inventory/products` on mount.

**Display:**

- Show `current_stock` for each product alongside entity-specific fields from BRIEFING.
- Apply visual stock-level indicators (colour, icon, or badge). Define thresholds in a code comment, e.g.:
  - `current_stock <= 5` → low (red)
  - `current_stock <= 15` → warning (amber)
  - otherwise → healthy (green)

**Actions:** Each row includes clearly labelled links/buttons to create an inbound or outbound order for that product (pre-fill `product_id` via query param or route state).

**Auth:** Redirect unauthenticated users to the existing login page.

## Inbound order form (`/backoffice/inventory/orders/inbound`)

**Form fields:**

- Product selector listing products **by name** (not raw IDs).
- Quantity (and any specific-BRIEFING fields).

**Submit:** `POST /inventory/orders/inbound`.

**Outcomes:**

- Success → clear form + show confirmation banner.
- `400` / `500` → display API error message in a visible element.

## Outbound order form (`/backoffice/inventory/orders/outbound`)

**Reactive stock display:**

- When the user selects a product, fetch `GET /inventory/products/{id}` (or read from cached list) and show `current_stock` **before** quantity entry.
- Update immediately when selection changes.

**Client-side guard:**

- If entered quantity > displayed stock, show a warning near the quantity field before submit (UX only — API enforces the real rule).

**API error on submit:**

- On `HTTP 400` (insufficient stock), show the API `detail` message inline next to the quantity field.

## Orders history page (`/backoffice/inventory/orders`)

**Data:** `GET /inventory/orders`.

**Each row shows:**

- Product name
- Quantity
- Order type (inbound vs outbound) with visual distinction (colour, icon, or label)
- Creation date
- `user_uuid` of the creator

**Read-only:** No delete or edit actions.

## Route protection

All four inventory routes must redirect unauthenticated users to login using the same pattern already present in the backoffice (middleware, layout check, or shared `useAuth` hook).

## Indicative examples

### Example: product list item (API response shape)

```json
{
  "id": 1,
  "name": "Widget A",
  "sku": "WDG-001",
  "current_stock": 12
}
```

### Example: outbound insufficient stock (`400`)

```json
{
  "detail": "Insufficient stock: requested 20, available 12"
}
```

The outbound form must render that `detail` string visibly — not a raw JSON dump.

### Example: order history row

```json
{
  "id": 7,
  "product_id": 1,
  "product_name": "Widget A",
  "quantity": 5,
  "order_type": "outbound",
  "created_at": "2026-06-09T10:30:00Z",
  "user_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

## Validation checklist (reviewers)

- [ ] `lib/inventory.ts` (or equivalent) exists — no raw `fetch` in page/components.
- [ ] All protected calls send `Authorization: Bearer <token>`.
- [ ] Products page loads live data and shows `current_stock` with visual indicators.
- [ ] Inbound form submits, confirms success, and surfaces API errors visibly.
- [ ] Outbound form shows reactive `current_stock` when product selection changes.
- [ ] Outbound form warns client-side when quantity exceeds displayed stock.
- [ ] Outbound `400` responses show the API error message inline near quantity.
- [ ] Orders history lists all orders with inbound/outbound distinction, product name, quantity, date, and `user_uuid`.
- [ ] All four pages redirect unauthenticated users to login.
- [ ] UI labels and entity names match company-BRIEFING.md.
