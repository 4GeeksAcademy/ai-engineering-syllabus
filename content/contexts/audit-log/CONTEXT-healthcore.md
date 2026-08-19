# CONTEXT — Audit Log · HealthCore

## 1. Why this matters to HealthCore

At HealthCore, the audit log isn't a best practice — it's a HIPAA and UK GDPR requirement. In the event of a possible breach, Claire Whitfield has 72 hours to notify the ICO under UK GDPR (60 days under HIPAA for the US), and that deadline is impossible to meet if reconstructing an incident takes days.

## 2. Critical actions to log

- **Every access** (read, not just modification) to a patient's clinical record, including who viewed it, when, and from what context (e.g., "resolving referral," "routine review")
- Modification of a patient's clinical or billing data
- Approval or denial of an insurance claim
- Creation, modification, or deactivation of users and their roles/departments
- Actions executed by the clinical documentation assistant or other agents that touch patient data
- Any export of patient data, regardless of the reason

## 3. Who can query the log

- **Admin** (James, Claire, Sandra): access to the full log — but remember the restriction from the roles project: Admin sees **who accessed what**, not the clinical content of the record accessed.
- **Supervisor**: access to their own department's log.
- **Employee**: no access to the audit viewer, except possibly a "who accessed my own assigned patients" view if your implementation offers it.

## 4. Non-negotiable restriction (HIPAA / UK GDPR)

The audit log itself **cannot contain PHI** (patient name in free text, diagnosis, clinical notes). Use an opaque patient identifier (`patient_ref`) in every entry — never the name, medical history, or any directly identifiable data in the log.

## 5. Important detail

Implement detection of unusual access patterns as part of this project if time allows: for example, a user accessing a volume of patient records well above their historical average in a short period. This is what Claire would ask to see first in case of any suspicion.

## 6. Required seed data

Generate at least 15 sample audit entries with fully synthetic patients, covering at least read access, modifications, and one export.
