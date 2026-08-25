# CONTEXT — Brasaland: Gestor Centralizado de Incidencias

## 1. Panorama de la empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa con 14 locales propios en Colombia y Florida. Operaciones de Restaurante, a cargo de **Felipe Guerrero**, no tiene visibilidad centralizada de lo que falla en cada local día a día: fallos de equipo, riesgos de seguridad alimentaria, falta de personal y retrasos de proveedores se reportan hoy por WhatsApp o llamada telefónica y se pierden en hilos de chat individuales. Felipe se entera tarde de los problemas, y no hay forma de responder a "¿cuántas incidencias tuvo el local del centro de Medellín este mes?"

Estás construyendo la herramienta de backoffice que permite a cualquier local reportar una incidencia, la enruta al equipo correcto, y le da a Felipe y al resto de responsables de área una foto en vivo de qué está abierto, qué está retrasado y quién es responsable.

## 2. Catálogos

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Canales de entrada

| Valor | Descripción |
|---|---|
| `whatsapp` | Reportado por el grupo de WhatsApp del encargado de local |
| `phone_call` | Llamada directa a Operaciones |
| `pos_alert` | Marcado automáticamente por el terminal POS (p. ej. sin ventas registradas en 2+ horas) |
| `in_person` | Registrado por un supervisor en visita al local |
| `dashboard` | Introducido directamente en el backoffice por un encargado |

### 2.2 Tipos de incidencia

| Valor | Descripción |
|---|---|
| `food_safety` | Deterioro, riesgo de contaminación, fallo de control de temperatura |
| `equipment_failure` | Parrilla, refrigeración, terminal POS o equipo de cocina fuera de servicio |
| `staffing_gap` | Local con personal insuficiente para el turno |
| `supplier_delay` | Entrega de ingredientes retrasada o incompleta |
| `customer_complaint` | Queja escalada que requiere respuesta de dirección |
| `system_outage` | POS, app de pedidos o herramienta interna no disponible |

### 2.3 Niveles de severidad

| Valor | Significado | Ejemplo |
|---|---|---|
| `critical` | El local no puede operar o hay un riesgo activo de seguridad alimentaria | Fallo de refrigeración con producto en riesgo |
| `high` | Degradación significativa del servicio | Una de dos parrillas fuera de servicio en hora punta |
| `medium` | Impacto notable pero manejable | Escasez menor de un ingrediente, con alternativa disponible |
| `low` | Sin impacto operativo inmediato | Fallo cosmético del POS |

### 2.4 Áreas responsables

`restaurant_operations`, `procurement`, `marketing`, `people_and_culture`, `training_and_quality`, `technology`

## 3. Campos de la entidad

Un registro de incidencia debe incluir, como mínimo:

- `location_id` y `location_name` (uno de los 14 locales de Brasaland — siembra al menos 4, mezclando Colombia y Florida)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (ver §4)
- `assigned_to` (nombre o rol de un miembro del equipo)
- `created_at`, `updated_at`
- Neutral en moneda: Brasaland opera con locales en COP y en USD, pero la incidencia en sí no lleva ningún campo monetario — no inventes uno.

## 4. Ciclo de vida del estado

`open → assigned → in_progress → resolved → closed`

Una incidencia puede pasar también a `reopened` desde `resolved` si el mismo problema reaparece en un local antes del cierre — esto debe quedar visible en el historial de cambios, no sobrescribirlo.

## 5. Trazabilidad (no negociable)

Cada transición entre los estados del §4, y cada cambio de `assigned_to` o de `responsible_area`, debe capturarse como un registro discreto, con marca temporal y autor — no solo reflejarse en el valor actual del campo. Felipe necesita poder abrir una incidencia y ver su historial completo: quién la asignó, cuándo pasó a `in_progress`, quién la reasignó y por qué cambió el área responsable, si cambió.

## 6. Datos semilla

Siembra al menos 12 incidencias que cubran:

- Los cuatro niveles de severidad
- Al menos 4 locales distintos entre ambos países
- Al menos 4 canales de entrada distintos
- Al menos una incidencia `reopened` con historial visible de la recurrencia
- Al menos una incidencia todavía `open` sin asignar (para probar la vista de "sin asignar")

## 7. Restricciones de negocio

- Una incidencia `critical` no puede pasar a `closed` sin pasar antes por `resolved` — no existe transición directa.
- El `responsible_area` de una incidencia puede cambiar tras su creación (p. ej. un `system_outage` enrutado primero a `technology` puede resultar ser un problema de `procurement`), y cada reasignación debe ser trazable según el §5.
- Los dos idiomas son opcionales pero muy recomendables para la interfaz del backoffice (español/inglés), en línea con la operación multipaís de Brasaland — elige un idioma base y trata el segundo como una mejora.

## 8. Entregables esperados

- CRUD de incidencias limitado a los campos del §3, usando solo los valores de catálogo del §2.
- Una vista de incidencias abiertas agrupable o filtrable por `severity`, cubriendo el requisito del README de "volumen por severidad".
- Un historial de auditoría visible por incidencia que cumpla el §5 — esto es lo primero que revisa el sign-off de Felipe.
