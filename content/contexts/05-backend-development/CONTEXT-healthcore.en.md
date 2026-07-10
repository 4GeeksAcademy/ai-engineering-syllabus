# CONTEXT — Milestone 5: Backend Inventory Management

## Company: HealthCore

**Path:** `05-backend-inventory-orm/CONTEXT-healthcore.md`

---

## Your Company

**HealthCore** is an outpatient healthcare services company operating 12 clinics across the USA (Texas, Florida, Georgia) and the UK (London, Manchester). Each clinic consumes medical supplies daily — syringes, PPE, wound care materials, rapid diagnostic tests, and medications — and receives restocking shipments from certified healthcare vendors.

Tracking what supplies are available at each clinic is both an operational necessity and a compliance requirement. Running out of PPE mid-shift or using expired supplies creates clinical risk. Until now, each location has managed stock in a local spreadsheet with no central visibility.

**James Osei (CTO)** has prioritised this as part of the HealthCore Digital platform build.

> **From James (CTO) — Jira ticket HCR-0188:**
> "We need a medical supply inventory API as the foundation for the clinical operations dashboard. Supply entries are deliveries from vendors. Supply exits are clinical consumptions logged by clinic staff. Stock is always the net of entries minus exits — direct modification is not allowed. All routes under `/inventory`. User UUIDs come from TinyDB. Claire has confirmed: supply inventory data is operational, not PHI — no HIPAA barriers on this API, but access must be authenticated."

---

## Entity Names and Field Specification

Use these names exactly in your models, schemas, and API responses.

### `MedicalSupply` (maps to README's `Product`)

| Field           | Type       | Notes                                                                                            |
| --------------- | ---------- | ------------------------------------------------------------------------------------------------ |
| `id`            | `int` (PK) | Auto-increment                                                                                   |
| `name`          | `str`      | e.g., `"Nitrile gloves (box of 100)"`, `"Rapid strep test kit"`                                  |
| `sku`           | `str`      | Internal catalogue code, e.g., `"HCR-PPE-001"`, `"HCR-DIAG-003"`                                 |
| `category`      | `str`      | `"ppe"`, `"wound_care"`, `"diagnostics"`, `"medications"`, `"consumables"`                       |
| `unit`          | `str`      | `"box"`, `"unit"`, `"pack"`, `"vial"`                                                            |
| `country`       | `str`      | `"US"` or `"UK"` — regulatory jurisdiction                                                       |
| `current_stock` | `int`      | **Computed field — not stored.** Derived from supply movements. Include in response schema only. |

### `SupplyDelivery` (maps to README's `InboundOrder`)

A vendor shipment received at a HealthCore clinic.

| Field         | Type                       | Notes                                                                     |
| ------------- | -------------------------- | ------------------------------------------------------------------------- |
| `id`          | `int` (PK)                 | Auto-increment                                                            |
| `supply_id`   | `int` (FK → MedicalSupply) |                                                                           |
| `quantity`    | `int`                      | Units received                                                            |
| `vendor_name` | `str`                      | e.g., `"MedLine Industries"`, `"Cardinal Health UK"`                      |
| `clinic_id`   | `int`                      | Receiving clinic (1–12). Not a FK — clinic data is managed separately.    |
| `created_at`  | `datetime`                 | Auto-set on creation                                                      |
| `user_uuid`   | `str`                      | UUID of the clinic administrator who confirmed the delivery (from TinyDB) |

### `SupplyConsumption` (maps to README's `OutboundOrder`)

A clinical use event: supplies consumed during patient care.

| Field              | Type                       | Notes                                                                               |
| ------------------ | -------------------------- | ----------------------------------------------------------------------------------- |
| `id`               | `int` (PK)                 | Auto-increment                                                                      |
| `supply_id`        | `int` (FK → MedicalSupply) |                                                                                     |
| `quantity`         | `int`                      | Units consumed                                                                      |
| `consumption_type` | `str`                      | `"clinical_use"` (used in patient care) or `"expiry_waste"` (expired and discarded) |
| `clinic_id`        | `int`                      | Clinic where consumption occurred                                                   |
| `created_at`       | `datetime`                 | Auto-set on creation                                                                |
| `user_uuid`        | `str`                      | UUID of the clinical or admin staff member who logged the consumption (from TinyDB) |

---

## API Router

All endpoints must be registered under the `/inventory` prefix. The router file lives at `services/routers/inventory.py`.

| Method | Path                         | Description                                           |
| ------ | ---------------------------- | ----------------------------------------------------- |
| `GET`  | `/inventory/products`        | List all medical supplies with `current_stock`        |
| `POST` | `/inventory/products`        | Register a new supply item                            |
| `GET`  | `/inventory/products/{id}`   | Get one supply with current stock                     |
| `POST` | `/inventory/orders/inbound`  | Log a vendor delivery (`SupplyDelivery`)              |
| `POST` | `/inventory/orders/outbound` | Log a clinical consumption (`SupplyConsumption`)      |
| `GET`  | `/inventory/orders`          | List all deliveries and consumptions with supply data |

---

## Business Rules

1. **`current_stock` is always computed**, never stored. For any supply: `current_stock = SUM(SupplyDelivery.quantity) − SUM(SupplyConsumption.quantity)`.
2. **A `SupplyConsumption` cannot be registered if it would result in negative stock.** Return `HTTP 400` with the message: `"Insufficient stock for supply '{name}'. Available: {available}, requested: {quantity}."`. Reject before writing.
3. **`consumption_type` must be either `"clinical_use"` or `"expiry_waste"`**. Validate in the request schema.
4. **No user table in Supabase.** The `user_uuid` fields reference TinyDB users. Do not create a User model in SQLModel.
5. **US and UK supplies coexist in the same table.** The `country` field (`"US"` or `"UK"`) identifies the regulatory jurisdiction. It must be present in both the model and response schema.
6. **Clinic IDs range from 1–12** (9 US clinics, 3 UK clinics). They are stored as integers, not as foreign keys in this milestone.

---

## Seed Data

Create the following records when setting up your local development database.

### MedicalSupplies (minimum 6)

| name                           | sku          | category    | unit | country |
| ------------------------------ | ------------ | ----------- | ---- | ------- |
| Nitrile gloves (box of 100)    | HCR-PPE-001  | ppe         | box  | US      |
| Surgical mask (pack of 50)     | HCR-PPE-002  | ppe         | pack | UK      |
| Adhesive wound dressing        | HCR-WND-001  | wound_care  | box  | US      |
| Rapid strep test kit           | HCR-DIAG-001 | diagnostics | unit | US      |
| Blood glucose test strips (50) | HCR-DIAG-002 | diagnostics | box  | UK      |
| 0.9% Saline solution 500ml     | HCR-MED-001  | medications | vial | US      |

### SupplyDeliveries (minimum 4)

Log at least 2 deliveries for `HCR-PPE-001` in different quantities. Use vendor names like `"MedLine Industries"`, `"Cardinal Health UK"`, `"Bound Tree Medical"`. Mix clinic IDs across both countries.

### SupplyConsumptions (minimum 3)

Include at least one `"clinical_use"` and one `"expiry_waste"` event. Quantities must not exceed seeded deliveries for the affected supply. Use `user_uuid` values from your TinyDB instance.

---

## File Structure (within `services/`)

```text
services/
├── main.py
├── database.py          # TinyDB client + SQLModel engine + get_db dependency
├── models.py            # MedicalSupply, SupplyDelivery, SupplyConsumption (SQLModel)
├── schemas.py           # Pydantic request/response schemas
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Acceptance Notes for HealthCore

- The evaluator will log a `SupplyConsumption` exceeding available stock and expect `HTTP 400`.
- The evaluator will attempt a `SupplyConsumption` with an invalid `consumption_type` value and expect a validation error.
- The evaluator will verify that `current_stock` in `GET /inventory/products` reflects the net of seeded deliveries and consumptions.
- The `country` field must be present in both the model and response schema.
- The `clinic_id` field must be present on both `SupplyDelivery` and `SupplyConsumption`.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_Milestone 5 · HealthCore scenario_
