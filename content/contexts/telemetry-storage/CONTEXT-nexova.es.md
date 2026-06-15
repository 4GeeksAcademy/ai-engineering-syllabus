# CONTEXT — Nexova · Telemetría Fase 3: Almacenamiento en el Backend

## Tu empresa

**Nexova** es una consultora de recursos humanos y adquisición de talento con oficinas en Valencia (España) y Miami (Florida). Formas parte del equipo interno de Ingeniería de IA. El `TelemetryService` del backoffice ya está enviando batches de eventos al stub. Hoy reemplazas ese stub por la capa de almacenamiento real.

---

## Qué va en `tags` por cada evento

La columna `tags` JSONB almacena las propiedades específicas del evento de tu allowlist. Esto es lo que Supabase recibirá y guardará para cada evento de Nexova.

| `event_type` | Contenido de `tags` |
|---|---|
| `procurement_order_created` | `{ "asset_id": "...", "quantity": 5, "office": "valencia" }` |
| `assignment_order_created` | `{ "asset_id": "...", "quantity": 1, "office": "miami" }` |
| `assignment_order_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "asset_id": "...", "office": "valencia" }` |
| `procurement_order_failed` | `{ "error_code": "UNKNOWN_VENDOR", "office": "miami" }` |
| `asset_list_viewed` | `{ "office": "valencia", "item_count": 18 }` |
| `user_login_succeeded` | `{ "office": "miami" }` |
| `user_login_failed` | `{ "reason": "session_expired" }` |
| `session_expired` | `{}` |

Las columnas fijas (`event_type`, `timestamp`, `service`, `level`) se populan desde los campos del envelope. La columna `value` puede usarse para `quantity` en eventos de órdenes si quieres que sea consultable sin parsear JSONB — documenta tu decisión.

---

## Bulk insert — Notas específicas de Nexova

Las oficinas de Valencia y Miami operan en zonas horarias distintas. Los días de incorporación de nuevos empleados — cuando varios `assignment_order_created` se disparan en secuencia — son los momentos de mayor tráfico para el sistema de telemetría. Tu bulk insert debe manejar ráfagas de eventos de asignación sin degradar el tiempo de respuesta del backoffice.

**Ejemplo de rechazo para Nexova:** llega un batch de 4 eventos. El evento 2 es un `assignment_order_created` sin el campo `office` en `tags` — falla la validación. Los eventos 1, 3 y 4 son válidos y se insertan. La respuesta es `{ "received": 4, "stored": 3, "rejected": 1 }`. Sin `office`, Sergio Molina (CTO) no puede segmentar Valencia vs. Miami — el evento se descarta correctamente.

---

## Checklist de verificación para Nexova

Después de reemplazar el stub, verifica en el editor de tablas de Supabase:

- [ ] Las filas `procurement_order_created` y `assignment_order_created` tienen `office` en `tags` — sin él la segmentación entre oficinas es imposible
- [ ] Las filas `assignment_order_created` **no** contienen nombres ni emails de empleados en `tags` — solo UUIDs opacos si hay alguna referencia a empleado
- [ ] Las filas `assignment_order_failed` tienen tanto `error_code` como `asset_id` en `tags` — necesarios para identificar qué tipo de activo genera más fricciones
- [ ] Ninguna fila contiene claves de licencia de software ni valores de contratos con proveedores en ninguna parte de `tags`

---

_Nexova AI Engineering Team — Documento interno para el AI Engineering Track de 4Geeks Academy_
