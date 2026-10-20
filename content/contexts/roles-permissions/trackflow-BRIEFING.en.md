# CONTEXT — Roles and Permissions · TrackFlow

## 1. Why this matters to TrackFlow

TrackFlow manages warehousing and last-mile delivery in Los Angeles and Zaragoza for e-commerce brands that trust the company with their entire logistics operation. A warehouse operative, a carrier coordinator, and an account manager currently have the same level of system access — meaning anyone could, in theory, view a client's commercial contract, modify another country's inventory, or look up a colleague's employment data without anyone noticing.

## 2. TrackFlow's roles

Use exactly these three roles as a minimum:

| System role | Who holds it at TrackFlow | Typical capabilities |
|---|---|---|
| **Employee** | Warehouse operatives, carrier coordinators, CX agents, corporate staff | Log picking activity, update incident status, view shipment status within their work queue, view their own employment data |
| **Supervisor** | Ana Whitfield (Warehouse), Carlos Vega (Carriers), Valentina Cruz (CX), Sofía Ramos (Returns), Rafael Sanz (People) | Everything Employee has + view their area's operations dashboard, approve exceptions, reassign work within their team |
| **Admin** | Andrés Kim (CTO), Thomas Harry (CEO) | Everything above + manage users, view data across both countries and all departments, configure roles and departments |

## 3. TrackFlow's departments

- **Warehouse Operations**
- **Last Mile and Carrier Management**
- **Reverse Logistics (Returns)**
- **Customer Experience (CX)**
- **Commercial and Client Relations**
- **People**
- **Technology**
- **Executive Direction**

## 4. Rules for what information concerns each department

- A **Warehouse Supervisor** sees inventory, discrepancies, and incoming orders, but not clients' commercial contracts (that's Commercial).
- A **Commercial Supervisor** sees each client's account status and renewal data, but not per-warehouse operational inventory detail.
- A **CX** user sees tickets and their SLA, but not per-carrier financial performance (that's Last Mile/Commercial combined with Executive Direction).
- A **People** user sees TrackFlow staff employment data (contracts, absences, leave, onboarding progress), but not client, inventory, or shipment data.
- No Supervisor from another department sees their team members' employment data beyond what's operational (schedules and assignments). Contracts, justified absences, and personal data belong exclusively to People.
- Any **Employee** can view their own employment data, never anyone else's.
- Only **Executive Direction** sees the consolidated view across the United States and Spain at once.

## 5. Important detail

TrackFlow operates in two countries with distinct client brands, but **this is not multi-tenancy** — it's scoping by department and, optionally, by country. Don't model end-client data isolation in this project; that belongs to a different platform project. The relevant axis here is role × department.

People works under two different labour frameworks (United States and Spain). You can model country as an additional attribute of the employment record, but you don't need to isolate People data by country in this project.

## 6. Minimum seed data

Create at least:
- 3 Employee users (from different departments: Warehouse, Carriers, and one more)
- 2 Supervisor users (one of them from People)
- 1 Admin user
- The 8 departments listed above

## 7. Specific acceptance criteria

- A Warehouse Supervisor who tries to query a client's contract renewal status (Commercial department) must receive a rejection.
- A Warehouse Supervisor who tries to view the contract or absences of an operative on their own team (People data) must receive a rejection.
