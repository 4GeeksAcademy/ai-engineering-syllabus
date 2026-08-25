# CONTEXT — Nexova: Gestor Centralizado de Incidencias

## 1. Panorama de la empresa

**Nexova** es una consultora de recursos humanos que opera tres líneas de negocio — selección de directivos, soporte al cliente externalizado (30 agentes que atienden a los propios clientes de Nexova) y formación corporativa — desde Valencia y Miami. Hoy las incidencias quedan donde caen: un DM de Slack al equipo de soporte de **Roberto Díaz**, un correo al Gerente de Operaciones **Javier Almeida**, o una llamada que nadie anotó. No hay una vista compartida de qué está abierto en las tres líneas de negocio, y los incumplimientos de SLA en los contratos de soporte externalizado pasan desapercibidos hasta que un cliente se queja.

Estás construyendo la herramienta de backoffice que centraliza la entrada de incidencias en todas las líneas de negocio de Nexova y hace visible el riesgo de SLA antes de que se convierta en una escalada de cliente.

## 2. Catálogos

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Canales de entrada

| Valor | Descripción |
|---|---|
| `email` | Reportado por correo a un responsable de área |
| `slack` | Reportado en un canal interno de Slack |
| `helpdesk_ticket` | Levantado a través del helpdesk de soporte externalizado |
| `client_call` | Llamada directa de un cliente de Nexova |
| `dashboard` | Introducido directamente en el backoffice |

### 2.2 Tipos de incidencia

| Valor | Descripción |
|---|---|
| `sla_breach` | Un compromiso de SLA de soporte externalizado se incumplió o está en riesgo |
| `client_escalation` | Un cliente ha escalado su insatisfacción más allá del consultor/agente asignado |
| `system_outage` | ATS, CRM o herramienta de helpdesk no disponible |
| `data_issue` | Datos de candidato o cliente introducidos incorrectamente, duplicados o perdidos |
| `staffing_gap` | Equipo de soporte externalizado con personal insuficiente para la cobertura contratada |
| `compliance_flag` | Una posible preocupación de cumplimiento de RRHH o legal-laboral señalada internamente |

### 2.3 Niveles de severidad

| Valor | Significado | Ejemplo |
|---|---|---|
| `critical` | SLA contractual incumplido o cliente amenazando con cancelar | SLA de 24h incumplido por más de 20 horas en una cuenta clave |
| `high` | Riesgo significativo para una relación de cliente o un entregable | Proceso de selección detenido con plazo de cliente en 48h |
| `medium` | Impacto notable pero contenido | Un único registro de candidato necesita corrección |
| `low` | Sin impacto inmediato en el negocio | Fallo menor de la herramienta de helpdesk |

### 2.4 Áreas responsables

`marketing`, `sales`, `hr_internal`, `talent_selection`, `corporate_training`, `customer_support`, `technology`

## 3. Campos de la entidad

Un registro de incidencia debe incluir, como mínimo:

- `client_name` (nulable — no toda incidencia está ligada a un cliente externo; las incidencias internas de RRHH o de herramientas pueden no tenerlo)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (ver §4)
- `assigned_to`
- `sla_deadline` (nulable — solo se rellena cuando `type` es `sla_breach` o la incidencia está ligada a un SLA contratado)
- `created_at`, `updated_at`

## 4. Ciclo de vida del estado

`open → assigned → in_progress → resolved → closed`

Una incidencia puede pasar a `reopened` desde `resolved` si el mismo problema reaparece en la misma cuenta o sistema antes del cierre — esto debe quedar visible en el historial de cambios, no sobrescribirlo.

## 5. Trazabilidad (no negociable)

Cada transición entre los estados del §4, y cada cambio de `assigned_to` o de `responsible_area`, debe capturarse como un registro discreto, con marca temporal y autor. Esto importa sobre todo en las incidencias `sla_breach`: si un cliente disputa cuándo Nexova tuvo constancia de un problema, el historial de auditoría es la evidencia.

## 6. Datos semilla

Siembra al menos 12 incidencias que cubran:

- Los cuatro niveles de severidad
- Al menos 3 valores distintos de `responsible_area`, incluyendo `customer_support`
- Al menos una incidencia `sla_breach` con un `sla_deadline` ya vencido
- Al menos una incidencia `reopened` con historial visible de la recurrencia
- Al menos una incidencia sin `client_name` (solo interna)

## 7. Restricciones de negocio

- Las incidencias con `type = sla_breach` deben tener `sla_deadline` no nulo; las de cualquier otro tipo no deben rellenarlo.
- Una incidencia `critical` no puede pasar a `closed` sin pasar antes por `resolved`.
- Los dos idiomas son opcionales pero muy recomendables para la interfaz del backoffice (español/inglés), en línea con la operación de Nexova entre Valencia y Miami — elige un idioma base y trata el segundo como una mejora.

## 8. Entregables esperados

- CRUD de incidencias limitado a los campos del §3, usando solo los valores de catálogo del §2.
- Una vista de incidencias abiertas agrupable o filtrable por `severity`, cubriendo el requisito del README de "volumen por severidad", con las incidencias de incumplimiento de SLA distinguibles de un vistazo.
- Un historial de auditoría visible por incidencia que cumpla el §5.
