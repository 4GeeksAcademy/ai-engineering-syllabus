# CONTEXT — Registro de Auditoría · HealthCore

## 1. Por qué le importa a HealthCore

En HealthCore, el registro de auditoría no es una buena práctica — es un requisito de HIPAA y UK GDPR. Ante una posible brecha, Claire Whitfield tiene 72 horas para notificar al ICO bajo UK GDPR (60 días bajo HIPAA para EE. UU.), y ese plazo es imposible de cumplir si reconstruir un incidente toma días.

## 2. Acciones críticas a registrar

- **Todo acceso** (lectura, no solo modificación) a un registro clínico de paciente, incluyendo quién lo consultó, cuándo, y desde qué contexto (ej. "resolviendo referral", "revisión rutinaria")
- Modificación de datos clínicos o de facturación de un paciente
- Aprobación o denegación de una reclamación de seguro
- Creación, modificación o desactivación de usuarios y sus roles/departamentos
- Acciones ejecutadas por el asistente de documentación clínica u otros agentes que toquen datos de pacientes
- Cualquier exportación de datos de pacientes, sea cual sea el motivo

## 3. Quién puede consultar el registro

- **Admin** (James, Claire, Sandra): acceso al registro completo — pero recuerda la restricción del proyecto de roles: Admin ve **quién accedió a qué**, no el contenido clínico del registro accedido.
- **Supervisor**: acceso al registro de su propio departamento.
- **Empleado**: sin acceso al visor de auditoría, salvo a un registro de "quién accedió a mis propios pacientes asignados" si tu implementación lo ofrece.

## 4. Restricción no negociable (HIPAA / UK GDPR)

El propio registro de auditoría **no puede contener PHI** (nombre del paciente en texto libre, diagnóstico, notas clínicas). Usa un identificador de paciente opaco (`patient_ref`) en cada entrada — nunca el nombre, historia clínica o cualquier dato identificable directamente en el log.

## 5. Detalle importante

Implementa detección de patrones de acceso inusuales como parte de este proyecto si tu tiempo lo permite: por ejemplo, un usuario que accede a un volumen de registros de pacientes muy por encima de su promedio histórico en un periodo corto. Esto es lo que Claire pediría ver primero ante cualquier sospecha.

## 6. Dato de seed necesario

Genera al menos 15 entradas de auditoría de ejemplo con pacientes completamente sintéticos, cubriendo al menos accesos de lectura, modificaciones y una exportación.
