# CONTEXT — HealthCore: Gestor Centralizado de Incidencias

## 1. Panorama de la empresa

**HealthCore** opera 12 clínicas ambulatorias en EE. UU. y el Reino Unido. Las incidencias operativas — una caída del EHR, un fallo del sistema de facturación, una preocupación de cumplimiento, una falta de personal — se reportan hoy por teléfono, correo informal o de palabra entre el equipo clínico del **Dr. Marcus Reid**, el equipo de ciclo de ingresos de **Tom Callahan** y el equipo de cumplimiento de **Claire Whitfield**, sin ningún registro compartido. Nadie puede responder a "¿cuántas incidencias de sistema tuvimos en las clínicas del Reino Unido este trimestre?", y Claire no tiene forma fiable de demostrar los tiempos de respuesta a incidencias durante una revisión regulatoria.

Estás construyendo la herramienta de backoffice que le da a HealthCore Digital un lugar único y auditable para registrar y hacer seguimiento de cada incidencia operativa — operaciones clínicas, facturación, cumplimiento, personal y tecnología — en las 12 ubicaciones de ambos países.

## 2. ⚠️ Restricción de datos no negociable

**No puede aparecer PHI, identificadores de pacientes, ni datos regulados por HIPAA o UK GDPR en ningún log, evento, tabla, respuesta de endpoint o salida del sistema.** Este gestor de incidencias registra incidencias operativas y de sistema — no es un registro clínico y nunca debe referirse a un paciente concreto por nombre, número de historia clínica, fecha de nacimiento ni ningún otro identificador. Si una incidencia realmente involucra a un paciente específico (p. ej. un error de documentación que afecta al registro de un paciente), referénciala únicamente mediante un token opaco `patient_ref` sin ningún significado clínico por sí mismo — nunca un nombre o número de historia. Si tu implementación no puede describir una incidencia sin detalle de paciente, el error está en la descripción, no en la restricción.

## 3. Catálogos

Usa exactamente estos valores. No inventes otros ni los renombres.

### 3.1 Canales de entrada

| Valor | Descripción |
|---|---|
| `internal_ticket` | Levantado a través del sistema interno de tickets de HealthCore |
| `phone` | Llamada directa al departamento correspondiente |
| `monitoring_alert` | Marcado automáticamente por un monitor de salud del sistema |
| `compliance_escalation` | Escalado por correo desde el equipo de Cumplimiento |
| `dashboard` | Introducido directamente en el backoffice |

### 3.2 Tipos de incidencia

| Valor | Descripción |
|---|---|
| `system_outage` | EHR, plataforma de facturación o sistema de citas no disponible |
| `billing_issue` | Fallo en el procesamiento de reclamaciones, pico de denegaciones o patrón de error de codificación |
| `compliance_concern` | Una posible cuestión de cumplimiento de HIPAA o UK GDPR (anomalía de acceso, vacío de política, vencimiento de acuerdo con proveedor) |
| `staffing_gap` | Una clínica con personal insuficiente para el volumen de pacientes programado |
| `data_integrity` | Un problema de integración de sistemas o sincronización de datos no ligado a un registro de paciente concreto |
| `vendor_sla_breach` | Un proveedor de tecnología o servicio incumplió un SLA contratado |

### 3.3 Niveles de severidad

| Valor | Significado | Marco regulatorio |
|---|---|---|
| `critical` | Exposición de cumplimiento activa o una clínica no puede operar | Cualquier caso con un plazo de notificación de brecha plausible en marcha (60 días bajo HIPAA, 72 horas al ICO bajo UK GDPR) es `critical` por defecto |
| `high` | Riesgo clínico o financiero significativo, contenido por ahora | EHR degradado pero funcional; un pico de denegaciones que afecta a un pagador |
| `medium` | Impacto notable pero contenido | Una única clínica con falta de personal para un turno |
| `low` | Sin impacto operativo inmediato | Problema cosmético de visualización en el dashboard |

### 3.4 Áreas responsables

`clinical_operations`, `patient_experience`, `revenue_cycle`, `compliance`, `people_and_workforce`, `technology`

## 4. Campos de la entidad

Un registro de incidencia debe incluir, como mínimo:

- `clinic_location` (una de las 12 clínicas de HealthCore; nulable si la incidencia es a nivel de toda la red, p. ej. una caída de sistema central) y `country` (`us` o `uk`)
- `channel` (§3.1), `type` (§3.2), `severity` (§3.3), `responsible_area` (§3.4)
- `title`, `description` — debe cumplir el §2
- `status` (ver §5)
- `assigned_to`
- `patient_ref` (nulable, solo token opaco — ver §2; nunca un nombre, número de historia o fecha de nacimiento)
- `created_at`, `updated_at`

## 5. Ciclo de vida del estado

`open → assigned → in_progress → resolved → closed`

Una incidencia puede pasar a `reopened` desde `resolved` si el mismo problema reaparece en la misma clínica o sistema antes del cierre — esto debe quedar visible en el historial de cambios, no sobrescribirlo.

## 6. Trazabilidad (no negociable)

Cada transición entre los estados del §5, y cada cambio de `assigned_to` o de `responsible_area`, debe capturarse como un registro discreto, con marca temporal y autor. Aquí esto no es higiene documental opcional — es lo que el equipo de Claire extrae durante una revisión regulatoria para demostrar tiempos de respuesta, y es el hábito de log de auditoría de accesos que este hito busca construir antes de cualquier pipeline que más adelante toque datos reales de pacientes.

## 7. Datos semilla

Siembra al menos 12 incidencias que cubran:

- Los cuatro niveles de severidad
- Ambos países (`us` y `uk`)
- Al menos una incidencia `compliance_concern` con severidad `critical`
- Al menos una incidencia `reopened` con historial visible de la recurrencia
- Al menos una incidencia que use un token `patient_ref`, para confirmar que ningún dato real de paciente se filtra al campo
- Cero incidencias en todo el conjunto semilla que incumplan el §2 — esto se evalúa, no es orientativo

## 8. Restricciones de negocio

- Una incidencia `critical` no puede pasar a `closed` sin pasar antes por `resolved`.
- Cada campo, línea de log y documento generado por esta funcionalidad debe verificarse contra el §2 antes de darse por completo — incluida la salida de consola, los scripts de semilla y cualquier texto de resumen generado por IA.
- El idioma base de la interfaz del backoffice es inglés; el español es opcional y no se requiere en este hito (el compromiso multilingüe de HealthCore aplica a las herramientas de cara al paciente, no a esta herramienta interna).

## 9. Entregables esperados

- CRUD de incidencias limitado a los campos del §4, usando solo los valores de catálogo del §3, y respetando el §2 sin excepción.
- Una vista de incidencias abiertas agrupable o filtrable por `severity`, cubriendo el requisito del README de "volumen por severidad".
- Un historial de auditoría visible por incidencia que cumpla el §6.
