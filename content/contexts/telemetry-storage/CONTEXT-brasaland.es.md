# CONTEXT — Brasaland · Telemetría Fase 3: Almacenamiento en el Backend

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa con 14 locales en Colombia y Florida. Formas parte de **Brasaland Digital**. El `TelemetryService` del backoffice ya está enviando batches de eventos al stub. Hoy reemplazas ese stub por la capa de almacenamiento real.

---

## Qué va en `tags` por cada evento

La columna `tags` JSONB almacena las propiedades específicas del evento de tu allowlist. Esto es lo que Supabase recibirá y guardará para cada evento de Brasaland.

| `event_type` | Contenido de `tags` |
|---|---|
| `supply_order_created` | `{ "ingredient_id": "...", "quantity": 50, "location_id": "medellin_centro", "supplier_id": "..." }` |
| `consumption_order_created` | `{ "ingredient_id": "...", "quantity": 12, "reason": "kitchen_use", "location_id": "miami_south" }` |
| `consumption_order_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "ingredient_id": "...", "location_id": "medellin_centro" }` |
| `supply_order_failed` | `{ "error_code": "UNKNOWN_SUPPLIER", "location_id": "miami_south" }` |
| `ingredient_list_viewed` | `{ "location_id": "medellin_centro", "item_count": 34 }` |
| `user_login_succeeded` | `{ "location_id": "miami_south" }` |
| `user_login_failed` | `{ "reason": "invalid_credentials" }` |
| `session_expired` | `{}` |

Las columnas fijas (`event_type`, `timestamp`, `service`, `level`) se populan desde los campos del envelope. La columna `value` puede usarse para `quantity` en eventos de órdenes si quieres que sea consultable sin parsear JSONB — documenta tu decisión.

---

## Bulk insert — Notas específicas de Brasaland

Los 14 locales de Brasaland implican que varios gerentes pueden estar logados simultáneamente, cada uno generando eventos. Un servicio de tarde del viernes en Miami puede producir decenas de eventos `consumption_order_created` por minuto. Tu bulk insert debe manejar esto sin abrir una transacción por evento.

**Ejemplo de rechazo para Brasaland:** llega un batch de 5 eventos. El evento 3 no tiene `location_id` en `tags` — falla la validación de esquema. Los eventos 1, 2, 4 y 5 son válidos y se insertan. La respuesta es `{ "received": 5, "stored": 4, "rejected": 1 }`. Sin `location_id` ese evento sería inútil para la segmentación — rechazarlo es la decisión correcta.

---

## Checklist de verificación para Brasaland

Después de reemplazar el stub, verifica en el editor de tablas de Supabase:

- [ ] Las filas `supply_order_created` tienen `location_id` en `tags` — sin él Nicolás Park (CTO) no puede segmentar por país
- [ ] Las filas `consumption_order_created` tienen `reason` en `tags` — sin él el KPI de ratio de merma es incalculable
- [ ] Ninguna fila contiene direcciones de email, nombres de gerentes ni importes en COP/USD en ninguna parte de `tags`
- [ ] Las filas de locales colombianos (`medellin_*`, `bogota_*`) y de Florida (`miami_*`) son distinguibles por `location_id` dentro de `tags`

---

_Brasaland Digital — Documento interno para el AI Engineering Track de 4Geeks Academy_
