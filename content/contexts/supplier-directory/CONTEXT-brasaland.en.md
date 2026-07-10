# CONTEXT — Supplier Directory · Brasaland

_Estas instrucciones también están disponibles en [español](./CONTEXT-brasaland.es.md)._

> **Milestone:** 09 — Lightweight Storage API  
> **Repository path:** `09-lightweight-storage/CONTEXT-brasaland.md`

---

## Your company

You are part of the **Brasaland Digital** team, the internal technology unit of Brasaland, a grilled-food restaurant chain with **14 locations** in Colombia and Florida. Your tech lead is **Nicolás Park**, CTO, and **Lucía Fernández**, Procurement Manager, requested this project.

Brasaland works with around **20 active suppliers** split between Colombia and Florida. Until now, Lucía manages the directory in a spreadsheet shared by email. Every time a supplier's rate changes or a new one must be added, three versions of the file circulate and no one knows which is official. This project creates the single source of truth.

---

## Supplier model

Each supplier in the Brasaland directory has the following structure:

| Field             | Type                                 | Description                                   |
| ----------------- | ------------------------------------ | --------------------------------------------- |
| `name`            | string, required                     | Supplier trade name                           |
| `country`         | string, required                     | Operating country: `"Colombia"` or `"USA"`    |
| `categories`      | list of strings, required, minimum 1 | Product categories supplied (see valid list)  |
| `rate_per_unit`   | float, required, > 0                 | Current rate per unit in the country currency |
| `currency`        | string, required                     | `"COP"` for Colombia, `"USD"` for USA         |
| `rate_updated_at` | datetime, system-generated           | Timestamp of the last rate update             |
| `status`          | string, required                     | `"active"` or `"suspended"`                   |
| `contact_email`   | string, optional                     | Supplier contact email                        |
| `notes`           | string, optional                     | Internal procurement team notes               |

### Valid categories

```python
VALID_CATEGORIES = [
    "carne",
    "verduras_y_hortalizas",
    "salsas_y_condimentos",
    "bebidas",
    "packaging",
    "productos_limpieza",
    "lacteos",
    "carbon_y_combustible"
]
```

### Valid statuses

```python
VALID_STATUSES = ["active", "suspended"]
```

---

## Seeder initial data

The seeder must load exactly the following suppliers. They are what Lucía has in her current spreadsheet — the one this project replaces.

```python
SUPPLIERS_SEED = [
    {
        "name": "Carnes del Valle S.A.S.",
        "country": "Colombia",
        "categories": ["carne"],
        "rate_per_unit": 28500.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "ventas@carnesdelvalle.co",
        "notes": "Primary beef and pork supplier for Medellín. Delivery Tuesday and Friday."
    },
    {
        "name": "Frigorífico Antioqueño",
        "country": "Colombia",
        "categories": ["carne"],
        "rate_per_unit": 27900.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "pedidos@frigorificoa.co",
        "notes": "Secondary supplier. Used when Carnes del Valle is out of stock."
    },
    {
        "name": "Verduras La Cosecha",
        "country": "Colombia",
        "categories": ["verduras_y_hortalizas"],
        "rate_per_unit": 3200.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "lacosecha@gmail.com",
        "notes": "Medellín wholesale market. Daily delivery before 7am."
    },
    {
        "name": "Condimentos El Sabor",
        "country": "Colombia",
        "categories": ["salsas_y_condimentos"],
        "rate_per_unit": 12400.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "info@elsabor.co"
    },
    {
        "name": "Distribuidora RefriCol",
        "country": "Colombia",
        "categories": ["bebidas", "lacteos"],
        "rate_per_unit": 4100.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "refricol.pedidos@gmail.com"
    },
    {
        "name": "Empaques y Más",
        "country": "Colombia",
        "categories": ["packaging"],
        "rate_per_unit": 890.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "ventas@empaquesymas.co",
        "notes": "Supplies boxes, bags, and napkins for all Colombia locations."
    },
    {
        "name": "Limpiahogar Profesional",
        "country": "Colombia",
        "categories": ["productos_limpieza"],
        "rate_per_unit": 7600.0,
        "currency": "COP",
        "status": "suspended",
        "contact_email": "limpiahogar@promail.co",
        "notes": "Suspended for delivery non-compliance. Under review by Lucía."
    },
    {
        "name": "CarboCo",
        "country": "Colombia",
        "categories": ["carbon_y_combustible"],
        "rate_per_unit": 45000.0,
        "currency": "COP",
        "status": "active",
        "contact_email": "pedidos@carboco.co",
        "notes": "Only approved charcoal supplier for the grills. Annual contract."
    },
    {
        "name": "Miami Meat Distributors LLC",
        "country": "USA",
        "categories": ["carne"],
        "rate_per_unit": 6.80,
        "currency": "USD",
        "status": "active",
        "contact_email": "orders@miamimeat.com",
        "notes": "Primary meat supplier for Florida locations."
    },
    {
        "name": "Sunshine Produce FL",
        "country": "USA",
        "categories": ["verduras_y_hortalizas"],
        "rate_per_unit": 2.15,
        "currency": "USD",
        "status": "active",
        "contact_email": "sales@sunshineproduce.com"
    },
    {
        "name": "Latin Flavors Inc.",
        "country": "USA",
        "categories": ["salsas_y_condimentos", "bebidas"],
        "rate_per_unit": 4.50,
        "currency": "USD",
        "status": "active",
        "contact_email": "orders@latinflavors.com",
        "notes": "Imports Colombian sauces for the Florida market."
    },
    {
        "name": "PackRight USA",
        "country": "USA",
        "categories": ["packaging"],
        "rate_per_unit": 0.35,
        "currency": "USD",
        "status": "active",
        "contact_email": "info@packright.us"
    },
    {
        "name": "CleanPro Florida",
        "country": "USA",
        "categories": ["productos_limpieza"],
        "rate_per_unit": 12.90,
        "currency": "USD",
        "status": "active",
        "contact_email": "orders@cleanproflorida.com"
    },
    {
        "name": "GrillFuel Supply Co.",
        "country": "USA",
        "categories": ["carbon_y_combustible"],
        "rate_per_unit": 38.50,
        "currency": "USD",
        "status": "active",
        "contact_email": "supply@grillfuel.com",
        "notes": "Charcoal supplier for Florida. Price subject to quarterly review."
    },
    {
        "name": "Bebidas Andinas",
        "country": "Colombia",
        "categories": ["bebidas"],
        "rate_per_unit": 3800.0,
        "currency": "COP",
        "status": "suspended",
        "contact_email": "ventas@bebidasandinas.co",
        "notes": "Suspended. Price above market after last renegotiation."
    }
]
```

---

## Business constraints

- **Currency by country:** A supplier from `"Colombia"` must have `currency = "COP"`. A supplier from `"USA"` must have `currency = "USD"`. The API must reject inconsistent combinations.
- **Multiple categories:** A supplier can supply more than one category (for example, beverages and dairy). The `categories` list must have at least one valid element.
- **Rate traceability:** Every time `rate_per_unit` is updated, the `rate_updated_at` field must record the exact timestamp of the change. Lucía requires this data for price audits.
- **Suspension, not deletion:** In Brasaland's real operations, suppliers are not removed from the system — they are suspended. The `DELETE` endpoint exists for correcting erroneous data, not as the usual workflow.

---

## What Lucía will see in the frontend

The directory page must allow Lucía to:

1. See all suppliers at a glance, with a clear indication of which are active and which are suspended.
2. Filter by country (Colombia / USA) to see only suppliers relevant to each market.
3. Filter by category to answer questions like "what active meat suppliers do we have in the USA?".
4. Register a new supplier from a form.
5. Update an existing supplier's rate from the interface.
6. Activate or suspend a supplier with a single click.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
