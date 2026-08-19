# CONTEXT — Audit Log · Brasaland

## 1. Why this matters to Brasaland

With 14 locations operating across two countries and a small corporate team, when something goes wrong today (an inventory discrepancy, an unauthorized price change, waste numbers that don't add up), the only way to investigate is to ask the person involved. Felipe Guerrero needs to be able to reconstruct what happened without relying on anyone's memory.

## 2. Critical actions to log

- Modification of menu or ingredient prices
- Approval or rejection of ingredient orders to suppliers
- Waste logging (product lost to expiry, cooking error, or possible theft)
- Changes to a location's configuration (hours, capacity, contact info)
- Creation, modification, or deactivation of users and their roles/departments
- Actions executed by the weekly executive report agent (if your implementation already has it)

## 3. Who can query the log

- **Admin** (Felipe, Nicolás, Mariana): access to the full log across all locations and departments.
- **Supervisor**: access only to their own location's and department's log.
- **Employee**: no access to the audit viewer.

## 4. Important detail

Brasaland operates in two currencies (COP and USD). When the audited event involves an amount (e.g., a price change), log the amount together with the currency it was executed in — don't convert it; conversion is the report's responsibility, not the audit log's.

## 5. Required seed data

Generate at least 15 sample audit entries covering at least four of the critical actions listed, spread across at least two different locations.
