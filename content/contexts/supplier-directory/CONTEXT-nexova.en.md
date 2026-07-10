# CONTEXT — Supplier Directory · Nexova

_Estas instrucciones también están disponibles en [español](./CONTEXT-nexova.es.md)._

> **Milestone:** 09 — Lightweight Storage API  
> **Repository path:** `09-lightweight-storage/CONTEXT-nexova.md`

---

## Your company

You are part of the AI Engineering team at **Nexova**, a human resources and talent acquisition consultancy headquartered in Valencia (Spain) with an office in Miami (Florida). Your tech lead is **Sergio Molina**, CTO, and the project was requested by **Patricia Solís**, HR Manager, in coordination with the operations area.

Nexova hires external services on a recurring basis: job posting platforms, selection tools, training providers, corporate software, and outsourcing services. Until now, this registry lives in a spreadsheet that Patricia updates manually and shares by email whenever there is a change. The result is multiple versions circulating in parallel with no one knowing which is current. This project creates the official, single source of truth.

---

## Supplier model

Each supplier in the Nexova directory has the following structure:

| Field                   | Type                                 | Description                                   |
| ----------------------- | ------------------------------------ | --------------------------------------------- |
| `name`                  | string, required                     | Supplier or platform trade name               |
| `country`               | string, required                     | Active contract country: `"Spain"` or `"USA"` |
| `categories`            | list of strings, required, minimum 1 | Type of service provided (see valid list)     |
| `monthly_rate`          | float, required, > 0                 | Current monthly cost in the contract currency |
| `currency`              | string, required                     | `"EUR"` for Spain, `"USD"` for USA            |
| `rate_updated_at`       | datetime, system-generated           | Timestamp of the last rate update             |
| `status`                | string, required                     | `"active"` or `"suspended"`                   |
| `contract_renewal_date` | string, optional                     | Contract renewal date (format `YYYY-MM-DD`)   |
| `contact_email`         | string, optional                     | Supplier account manager email                |
| `notes`                 | string, optional                     | Internal notes                                |

### Valid categories

```python
VALID_CATEGORIES = [
    "job_boards",
    "ats_software",
    "assessment_tools",
    "training_platforms",
    "payroll_and_hr_software",
    "video_interview",
    "background_check",
    "office_and_facilities",
    "it_and_software_licenses"
]
```

### Valid statuses

```python
VALID_STATUSES = ["active", "suspended"]
```

---

## Seeder initial data

The seeder must load exactly the following suppliers, representing Patricia's current directory state.

```python
SUPPLIERS_SEED = [
    {
        "name": "LinkedIn Talent Solutions",
        "country": "Spain",
        "categories": ["job_boards"],
        "monthly_rate": 1200.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-03-31",
        "contact_email": "account@linkedin.com",
        "notes": "Corporate license for job posting and candidate search."
    },
    {
        "name": "InfoJobs Premium",
        "country": "Spain",
        "categories": ["job_boards"],
        "monthly_rate": 490.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-06-30",
        "contact_email": "empresas@infojobs.net"
    },
    {
        "name": "Indeed Sponsored",
        "country": "USA",
        "categories": ["job_boards"],
        "monthly_rate": 850.0,
        "currency": "USD",
        "status": "active",
        "contact_email": "sales@indeed.com",
        "notes": "Pay-per-click campaigns for customer support profiles in Miami."
    },
    {
        "name": "Workable",
        "country": "Spain",
        "categories": ["ats_software"],
        "monthly_rate": 299.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-09-15",
        "contact_email": "support@workable.com",
        "notes": "Primary ATS for the Valencia selection team."
    },
    {
        "name": "Greenhouse",
        "country": "USA",
        "categories": ["ats_software"],
        "monthly_rate": 620.0,
        "currency": "USD",
        "status": "suspended",
        "contact_email": "accounts@greenhouse.io",
        "notes": "Suspended after non-renewal. Sergio is evaluating migrating everything to Workable."
    },
    {
        "name": "Thomas International",
        "country": "Spain",
        "categories": ["assessment_tools"],
        "monthly_rate": 380.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-12-01",
        "contact_email": "clientes@thomas.es",
        "notes": "Personality and aptitude tests for middle-management hiring processes."
    },
    {
        "name": "HireVue",
        "country": "USA",
        "categories": ["video_interview"],
        "monthly_rate": 540.0,
        "currency": "USD",
        "status": "active",
        "contract_renewal_date": "2025-08-31",
        "contact_email": "support@hirevue.com"
    },
    {
        "name": "Udemy Business",
        "country": "Spain",
        "categories": ["training_platforms"],
        "monthly_rate": 420.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2026-01-15",
        "contact_email": "business@udemy.com",
        "notes": "Licenses for the internal team. Managed by Elena Vargas."
    },
    {
        "name": "Coursera for Teams",
        "country": "USA",
        "categories": ["training_platforms"],
        "monthly_rate": 399.0,
        "currency": "USD",
        "status": "suspended",
        "contact_email": "teams@coursera.com",
        "notes": "Suspended due to low usage. Review before Q4."
    },
    {
        "name": "Sage HR",
        "country": "Spain",
        "categories": ["payroll_and_hr_software"],
        "monthly_rate": 310.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-10-01",
        "contact_email": "soporte@sage.com",
        "notes": "Payroll and personnel management software for the Valencia headquarters."
    },
    {
        "name": "Gusto",
        "country": "USA",
        "categories": ["payroll_and_hr_software"],
        "monthly_rate": 280.0,
        "currency": "USD",
        "status": "active",
        "contact_email": "support@gusto.com",
        "notes": "Payroll management for Miami office employees."
    },
    {
        "name": "Checkr",
        "country": "USA",
        "categories": ["background_check"],
        "monthly_rate": 195.0,
        "currency": "USD",
        "status": "active",
        "contract_renewal_date": "2025-11-30",
        "contact_email": "sales@checkr.com"
    },
    {
        "name": "Microsoft 365 Business",
        "country": "Spain",
        "categories": ["it_and_software_licenses"],
        "monthly_rate": 760.0,
        "currency": "EUR",
        "status": "active",
        "contact_email": "enterprise@microsoft.com",
        "notes": "Licenses for the entire Valencia and Miami workforce."
    },
    {
        "name": "Regus Valencia",
        "country": "Spain",
        "categories": ["office_and_facilities"],
        "monthly_rate": 2400.0,
        "currency": "EUR",
        "status": "active",
        "contract_renewal_date": "2025-07-01",
        "contact_email": "valencia@regus.com",
        "notes": "Lease for the main Valencia office. Includes meeting room."
    },
    {
        "name": "WeWork Miami",
        "country": "USA",
        "categories": ["office_and_facilities"],
        "monthly_rate": 3100.0,
        "currency": "USD",
        "status": "active",
        "contract_renewal_date": "2025-09-30",
        "contact_email": "miami@wework.com"
    }
]
```

---

## Business constraints

- **Currency by country:** A supplier from `"Spain"` must have `currency = "EUR"`. A supplier from `"USA"` must have `currency = "USD"`. The API must reject inconsistent combinations.
- **Rate traceability:** Every update to `monthly_rate` must automatically record `rate_updated_at`. Patricia uses this data to justify budget variations to management.
- **Upcoming renewals:** The `contract_renewal_date` field is optional but relevant — suppliers with renewal within the next 60 days must be visually highlighted in the frontend.
- **Controlled suspension:** Suspended suppliers are not deleted. They remain in the directory with `"suspended"` status to preserve commercial relationship history.

---

## What Patricia will see in the frontend

The directory page must allow Patricia to:

1. See all suppliers grouped or filterable by country (Spain / USA).
2. Filter by category to answer questions like "what active ATS tools do we have?".
3. Distinguish active suppliers from suspended ones at a glance.
4. Register a new supplier from a form.
5. Update a supplier's monthly rate and see the change reflected immediately.
6. Activate or suspend a supplier with a visible control in each row.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
