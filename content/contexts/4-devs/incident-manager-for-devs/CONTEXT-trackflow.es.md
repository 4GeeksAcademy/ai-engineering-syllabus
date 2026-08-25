# CONTEXT — TrackFlow: Gestor Centralizado de Incidencias

## 1. Panorama de la empresa

**TrackFlow** gestiona almacenes y entrega de última milla en dos mercados — Los Ángeles y Zaragoza — para marcas de e-commerce medianas. Hoy las incidencias están dispersas entre portales de transportistas, correos de clientes y llamadas al equipo de almacén de **Ana Whitfield** o al equipo de operaciones de transportistas de **Carlos Vega**. Cuando algo falla en Los Ángeles, el equipo de Zaragoza se entera por WhatsApp, si es que se entera. No existe un lugar único para ver qué está roto, quién lo está atendiendo y si está a punto de incumplir el SLA de entrega de un cliente.

Estás construyendo la herramienta de backoffice que le da a TrackFlow Tech un único lugar para registrar, enrutar y hacer seguimiento de cada incidencia operativa en ambos almacenes y en todas las relaciones con transportistas.

## 2. Catálogos

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Canales de entrada

| Valor | Descripción |
|---|---|
| `carrier_portal_alert` | Marcado automáticamente desde el sistema de seguimiento de un transportista |
| `client_email` | Reportado por correo de un cliente de TrackFlow (marca de e-commerce) |
| `wms_alert` | Marcado automáticamente por el sistema de gestión de almacén |
| `warehouse_call` | Llamada directa del personal de almacén |
| `dashboard` | Introducido directamente en el backoffice |

### 2.2 Tipos de incidencia

| Valor | Descripción |
|---|---|
| `lost_parcel` | Un envío está perdido o sin seguimiento más allá de la entrega esperada |
| `inventory_discrepancy` | El stock registrado no coincide con el stock físico en un almacén |
| `carrier_failure` | Un transportista falló una recogida, retrasó una ruta o entregó mercancía dañada |
| `system_outage` | WMS, seguimiento o herramienta interna no disponible |
| `return_dispute` | Un cliente o consumidor final disputa la aprobación o valoración de una devolución |
| `sla_breach` | Se incumplió el SLA contratado de entrega o cumplimiento de un cliente |

### 2.3 Niveles de severidad

| Valor | Significado | Ejemplo |
|---|---|---|
| `critical` | SLA de cara al cliente incumplido o un almacén no operativo | WMS caído en un almacén completo durante hora punta |
| `high` | Riesgo significativo para el volumen de envío o el plazo de un cliente | Un transportista no recogió el volumen saliente de todo un día |
| `medium` | Impacto notable pero contenido | Discrepancia de inventario en un único SKU |
| `low` | Sin impacto operativo inmediato | Problema cosmético de visualización en el portal de seguimiento |

### 2.4 Áreas responsables

`warehouse_operations`, `last_mile_carrier`, `reverse_logistics`, `customer_experience`, `commercial`, `technology`

## 3. Campos de la entidad

Un registro de incidencia debe incluir, como mínimo:

- `warehouse_location` (`los_angeles` o `zaragoza`, nulable si la incidencia no es específica de un almacén — p. ej. un problema puramente de transportista)
- `client_name` (la marca de e-commerce afectada, nulable para incidencias solo internas)
- `channel` (§2.1), `type` (§2.2), `severity` (§2.3), `responsible_area` (§2.4)
- `title`, `description`
- `status` (ver §4)
- `assigned_to`
- `created_at`, `updated_at`

## 4. Ciclo de vida del estado

`open → assigned → in_progress → resolved → closed`

Una incidencia puede pasar a `reopened` desde `resolved` si el mismo problema reaparece para el mismo cliente o almacén antes del cierre — esto debe quedar visible en el historial de cambios, no sobrescribirlo.

## 5. Trazabilidad (no negociable)

Cada transición entre los estados del §4, y cada cambio de `assigned_to` o de `responsible_area`, debe capturarse como un registro discreto, con marca temporal y autor. En las incidencias `sla_breach` y `carrier_failure`, este registro es lo que Comercial usa para justificar una compensación de servicio o disputar la factura de un transportista — tiene que ser fiable.

## 6. Datos semilla

Siembra al menos 12 incidencias que cubran:

- Los cuatro niveles de severidad
- Ambas ubicaciones de almacén
- Al menos 4 canales de entrada distintos
- Al menos una incidencia `reopened` con historial visible de la recurrencia
- Al menos una incidencia sin `client_name` (puramente interna, p. ej. un fallo de sistema interno)

## 7. Restricciones de negocio

- Una incidencia `critical` no puede pasar a `closed` sin pasar antes por `resolved`.
- El `responsible_area` de una incidencia puede cambiar tras su creación (p. ej. un `lost_parcel` enrutado primero a `last_mile_carrier` puede resultar ser un error de picking de `warehouse_operations`), y cada reasignación debe ser trazable según el §5.
- Los dos idiomas son opcionales pero muy recomendables para la interfaz del backoffice (español/inglés), en línea con la operación de TrackFlow entre Los Ángeles y Zaragoza — elige un idioma base y trata el segundo como una mejora.

## 8. Entregables esperados

- CRUD de incidencias limitado a los campos del §3, usando solo los valores de catálogo del §2.
- Una vista de incidencias abiertas agrupable o filtrable por `severity`, cubriendo el requisito del README de "volumen por severidad", con ambos almacenes representados.
- Un historial de auditoría visible por incidencia que cumpla el §5.
