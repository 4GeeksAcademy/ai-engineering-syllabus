# CONTEXT — Audit Log · Nexova

## 1. Why this matters to Nexova

Nexova handles candidate and client data that's commercially sensitive. If a client asks "who saw this candidate's profile and when?", Javier Almeida needs to answer with data, not assumptions — especially if there's ever a dispute over candidate exclusivity between two selection processes.

## 2. Critical actions to log

- Viewing or exporting a candidate's full profile
- Status changes for a candidate in a selection process (shortlisted, rejected, hired)
- Creation or modification of a vacancy
- Changes to the client CRM (Sales): account or negotiation status updates
- Creation, modification, or deactivation of users and their roles/departments
- Reassignment of a candidate or support ticket between consultants

## 3. Who can query the log

- **Admin** (Sergio, Laura): access to the full log across all departments.
- **Supervisor**: access to their own department's log (e.g., a Selection Supervisor only sees Selection's log, not Sales').
- **Employee**: no access to the audit viewer.

## 4. Important detail

Candidate profile queries are especially sensitive: log not only modifications, but also read-only access to a full profile, because in this domain "who saw what" matters as much as "who changed what."

## 5. Required seed data

Generate at least 15 sample audit entries covering at least four of the critical actions listed, spread across at least two different departments (e.g., Selection and Sales).
