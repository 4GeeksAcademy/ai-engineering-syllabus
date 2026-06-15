# CONTEXT — TrackFlow · Telemetría Fase 3: Almacenamiento en el Backend

## Tu empresa

**TrackFlow** es una empresa de gestión de almacenes y entrega de última milla con operaciones en Los Ángeles (EE. UU.) y Zaragoza (España). Formas parte de **TrackFlow Tech**. El `TelemetryService` del backoffice ya está enviando batches de eventos al stub. Hoy reemplazas ese stub por la capa de almacenamiento real.

---

## Qué va en `tags` por cada evento

La columna `tags` JSONB almacena las propiedades específicas del evento de tu allowlist. Esto es lo que Supabase recibirá y guardará para cada evento de TrackFlow.

| `event_type` | Contenido de `tags` |
|---|---|
| `receiving_order_created` | `{ "sku_id": "...", "quantity": 200, "warehouse": "los_angeles", "client_id": "client_uuid_..." }` |
| `dispatch_order_created` | `{ "sku_id": "...", "quantity": 15, "warehouse": "zaragoza", "destination_country": "ES" }` |
| `dispatch_order_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "sku_id": "...", "warehouse": "los_angeles", "destination_country": "US" }` |
| `receiving_order_failed` | `{ "error_code": "UNKNOWN_CLIENT", "warehouse": "zaragoza" }` |
| `sku_list_viewed` | `{ "warehouse": "los_angeles", "item_count": 142 }` |
| `user_login_succeeded` | `{ "warehouse": "zaragoza" }` |
| `user_login_failed` | `{ "reason": "invalid_credentials" }` |
| `session_expired` | `{}` |

Las columnas fijas (`event_type`, `timestamp`, `service`, `level`) se populan desde los campos del envelope. La columna `value` puede usarse para `quantity` en eventos de órdenes si quieres que sea consultable sin parsear JSONB — documenta tu decisión.

---

## Bulk insert — Notas específicas de TrackFlow

Los picos de tráfico de TrackFlow coinciden con las ventanas de despacho de e-commerce: Black Friday, temporada de Navidad, ventas flash de clientes de moda. Durante estos períodos, los operarios de Los Ángeles pueden generar cientos de eventos `dispatch_order_created` y `dispatch_order_failed` en poco tiempo. Tu bulk insert debe absorber estas ráfagas sin acumular transacciones.

**Ejemplo de rechazo para TrackFlow:** llega un batch de 6 eventos. El evento 4 es un `dispatch_order_failed` sin `warehouse` en `tags` — falla la validación. Los eventos 1, 2, 3, 5 y 6 son válidos y se insertan. La respuesta es `{ "received": 6, "stored": 5, "rejected": 1 }`. Un `dispatch_order_failed` sin `warehouse` es operativamente inútil — Andrés Kim (CTO) no puede atribuir el fallo a ninguno de los dos almacenes.

---

## Checklist de verificación para TrackFlow

Después de reemplazar el stub, verifica en el editor de tablas de Supabase:

- [ ] Todos los eventos de órdenes tienen `warehouse` en `tags` (`los_angeles` o `zaragoza`) — Thomas Harry (CEO) exige segmentación por almacén en cada vista
- [ ] Las filas `dispatch_order_created` tienen `destination_country` en `tags` — necesario para el análisis de SLA EE. UU. vs. España
- [ ] Los valores de `client_id` en `tags` son UUIDs opacos — nunca nombres de marcas ni razones sociales
- [ ] Ninguna fila contiene nombres de destinatarios, direcciones de entrega ni números de teléfono en ninguna parte de `tags`
- [ ] Las filas `dispatch_order_failed` siempre tienen `warehouse` y `destination_country` aunque falten otras propiedades

---

_TrackFlow Tech — Documento interno para el AI Engineering Track de 4Geeks Academy_
