# CONTEXT — TrackFlow · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-trackflow.md)._

## Tu empresa

**TrackFlow** es una empresa de gestión de almacenes y entrega de última milla que opera en Los Ángeles (EE. UU.) y Zaragoza (España). Formas parte de **TrackFlow Tech**, el equipo interno de tecnología liderado por Andrés Kim (CTO). El sistema de gestión de inventario que construiste hace seguimiento del stock de SKU en almacén en ambas ubicaciones — productos, pedidos de recepción entrantes y pedidos de despacho salientes — aplicando la regla de que los niveles de stock nunca se editan directamente.

Ana Whitfield (Head of Warehouse Operations) y Thomas Harry (CEO) han estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad TrackFlow | Descripción                                                              |
| ------------------------ | --------------------------- | ------------------------------------------------------------------------ |
| `Product`                | `SKU`                       | Una unidad de stock rastreada almacenada en uno o ambos almacenes        |
| `InboundOrder`           | `ReceivingOrder`            | Un envío de cliente que llega a un almacén e incrementa el stock del SKU |
| `OutboundOrder`          | `DispatchOrder`             | Una entrega a cliente recogida del stock que reduce el stock del SKU     |

Campos clave para referenciar en tus esquemas de eventos:

- `SKU`: `id`, `sku_code`, `name`, `category` (`fashion`, `electronics`, `cosmetics`, `home`, `other`), `unit`, `current_stock`, `min_stock_threshold`, `warehouse` (`los_angeles` / `zaragoza`), `client_id`
- `ReceivingOrder`: `id`, `sku_id`, `quantity`, `client_id`, `warehouse`, `carrier`, `created_by` (UUID de usuario TinyDB), `created_at`
- `DispatchOrder`: `id`, `sku_id`, `quantity`, `client_id`, `destination_country`, `carrier`, `warehouse`, `created_by`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que Ana y Thomas necesitan del sistema de inventario de almacén. Tu plan debe justificar cómo la telemetría alimenta cada una.

| #   | KPI                                      | Definición                                                                                           | Decisión de negocio que habilita                                                                                              |
| --- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Tasa de cumplimiento de pedidos**      | Proporción de DispatchOrders completados exitosamente frente a los rechazados por stock insuficiente | Detectar qué SKUs o almacenes tienen problemas crónicos de disponibilidad; marcar clientes en riesgo de incumplimiento de SLA |
| 2   | **Frecuencia de discrepancias de stock** | Número de intentos de edición directa de stock rechazados por la API por almacén por día             | Identificar almacenes donde los operarios intentan atajos manuales; activar auditoría de procesos                             |
| 3   | **Tiempo de ciclo recepción-despacho**   | Tiempo promedio entre un ReceivingOrder y el primer DispatchOrder que consume del mismo lote de SKU  | Medir velocidad de procesamiento por ubicación; identificar cuellos de botella antes de que impacten a los clientes           |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato             | Disparador                                                                                            | ¿Stream o batch? (tú decides) |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------- |
| `receiving_order_created`    | Se registra exitosamente un ReceivingOrder                                                            | ?                             |
| `dispatch_order_created`     | Se registra exitosamente un DispatchOrder                                                             | ?                             |
| `stock_threshold_triggered`  | El stock de un SKU cae a o por debajo de `min_stock_threshold` tras un despacho                       | ?                             |
| `direct_stock_edit_rejected` | Una solicitud de modificar el stock del SKU directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `dispatch_order_failed`      | Un DispatchOrder es rechazado (p. ej. stock insuficiente, SKU desconocido)                            | ?                             |
| `receiving_order_failed`     | Un ReceivingOrder es rechazado (p. ej. cliente desconocido, cantidad inválida)                        | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas en TrackFlow.

| Evento candidato           | Disparador                                                                       | Sección       |
| -------------------------- | -------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`     | Inicio de sesión exitoso por un operario o coordinador de almacén                | Autenticación |
| `user_login_failed`        | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada) | Autenticación |
| `session_expired`          | La sesión del usuario expiró y fue invalidada                                    | Autenticación |
| `sku_list_viewed`          | El usuario abre la lista de stock de SKU de un almacén                           | Navegación    |
| `dispatch_form_abandoned`  | El usuario inicia pero no completa un formulario de DispatchOrder                | Navegación    |
| `warehouse_filter_applied` | El usuario cambia la vista entre Los Ángeles y Zaragoza                          | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble almacén:** todo evento originado en una operación de almacén debe incluir `warehouse` (`los_angeles` / `zaragoza`) para que los datos puedan segmentarse por país. Thomas Harry no aceptará un dashboard que mezcle ambos almacenes sin una separación clara.
- **Aislamiento de datos de cliente:** TrackFlow gestiona inventario para múltiples marcas cliente. Los eventos que incluyan `client_id` deben usar identificadores opacos — nunca nombres de marca — para evitar fugas accidentales de datos entre cuentas de cliente.
- **Sin PII en telemetría:** los campos `created_by` deben ser UUIDs opacos de TinyDB — nunca nombres ni direcciones de correo de operarios.
- **Sensibilidad SLA:** los fallos de DispatchOrder con `destination_country = US` en horas punta (Black Friday, Q4) tienen implicaciones contractuales de SLA. Marca los eventos `dispatch_order_failed` en tu esquema como que requieren procesamiento inmediato en stream; documenta el fundamento en tu sección stream/batch.

---

## Qué debe producir tu plan para TrackFlow

- `telemetry-plan.md` referenciando `SKU`, `ReceivingOrder` y `DispatchOrder` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`receiving_order_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por la urgencia operativa de TrackFlow — p. ej. un stock-out para un cliente de moda de alto volumen en Los Ángeles es inmediato; un reporte semanal de ciclo de recepción no lo es.
- Una sección de riesgos y exclusiones que aborde la restricción de doble almacén, el aislamiento de datos de cliente y cualquier evento descartado.

---

_TrackFlow Tech — Documento interno para 4Geeks Academy AI Engineering Track_
