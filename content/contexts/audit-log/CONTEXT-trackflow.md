# CONTEXT — Audit Log · TrackFlow

## 1. Why this matters to TrackFlow

TrackFlow manages inventory and shipments belonging to third parties (client brands). An inventory discrepancy or an incorrect return approval can directly cost a client money — and Andrés Kim needs to be able to show that brand, with data, what happened and who authorized it.

## 2. Critical actions to log

- Manual inventory adjustments (corrections outside the normal inbound/outbound flow)
- Approval or rejection of a return
- Changes to carrier assignment for a shipment
- Modification of a client's contract or commercial terms
- Creation, modification, or deactivation of users and their roles/departments
- Actions executed by the automatic returns approval engine (if your implementation already has it)

## 3. Who can query the log

- **Admin** (Andrés, Thomas): access to the full log across both countries and all departments.
- **Supervisor**: access to their own department's log (e.g., Ana only sees the Warehouse log).
- **Employee**: no access to the audit viewer.

## 4. Important detail

When the audited event occurs at a specific warehouse, log the country and the warehouse identifier along with the event — this lets Executive Direction later compare patterns between Los Angeles and Zaragoza, though that analysis isn't part of this project.

## 5. Required seed data

Generate at least 15 sample audit entries covering at least four of the critical actions listed, spread across at least two different departments.
