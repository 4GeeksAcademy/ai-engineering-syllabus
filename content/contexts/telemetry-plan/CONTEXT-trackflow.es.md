# CONTEXT — TrackFlow · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-trackflow.en.md)._

## Tu empresa

**TrackFlow** es una empresa de gestión de almacenes y entrega de última milla que opera en Los Ángeles (EE. UU.) y Zaragoza (España). Formas parte de **TrackFlow Tech**, el equipo interno de tecnología liderado por Andrés Kim (CTO). El sistema de gestión de inventario que construiste hace seguimiento del stock de SKU en almacén en ambas ubicaciones — SKUs, entradas de stock entrantes y salidas de stock salientes — aplicando la regla de que los niveles de stock nunca se editan directamente.

Ana Whitfield (Head of Warehouse Operations) y Thomas Harry (CEO) han estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad TrackFlow | Descripción                                                              |
| ------------------------ | --------------------------- | ------------------------------------------------------------------------ |
| `Product`                | `SKU`                       | Una unidad de stock rastreada almacenada en uno o ambos almacenes        |
| `InboundOrder`           | `StockEntry`                | Un envío de cliente que llega a un almacén e incrementa el stock del SKU |
| `OutboundOrder`          | `StockExit`                 | Un despacho a cliente o una pérdida confirmada que reduce el stock del SKU |

Campos clave para referenciar en tus esquemas de eventos:

- `SKU`: `id`, `sku`, `name`, `client_name`, `category` (`fashion`, `electronics`, `cosmetics`), `warehouse` (`"LA"` / `"ZGZ"`), `current_stock`
- `StockEntry`: `id`, `sku_id`, `quantity`, `reference`, `warehouse`, `user_uuid`, `created_at`
- `StockExit`: `id`, `sku_id`, `quantity`, `exit_type` (`dispatch` / `loss`), `tracking_number` (nullable), `warehouse`, `user_uuid`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que Ana y Thomas necesitan del sistema de inventario de almacén. Tu plan debe justificar cómo la telemetría alimenta cada una.

| #   | KPI                                      | Definición                                                                                           | Decisión de negocio que habilita                                                                                              |
| --- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Tasa de cumplimiento de pedidos**      | Proporción de despachos StockExit completados exitosamente frente a los rechazados por stock insuficiente | Detectar qué SKUs o almacenes tienen problemas crónicos de disponibilidad; marcar clientes en riesgo de incumplimiento de SLA |
| 2   | **Frecuencia de discrepancias de stock** | Número de intentos de edición directa de stock rechazados por la API por almacén por día             | Identificar almacenes donde los operarios intentan atajos manuales; activar auditoría de procesos                             |
| 3   | **Tiempo de ciclo recepción-despacho**   | Tiempo promedio entre un StockEntry y el primer StockExit que consume del mismo lote de SKU          | Medir velocidad de procesamiento por ubicación; identificar cuellos de botella antes de que impacten a los clientes           |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato             | Disparador                                                                                            | ¿Stream o batch? (tú decides) |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------- |
| `stock_entry_created`        | Se registra exitosamente un StockEntry                                                                | ?                             |
| `stock_exit_created`         | Se registra exitosamente un StockExit                                                                 | ?                             |
| `stock_threshold_triggered`  | El stock de un SKU cae a o por debajo de `min_stock_threshold` tras una salida                        | ?                             |
| `direct_stock_edit_rejected` | Una solicitud de modificar el stock del SKU directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `stock_exit_failed`          | Un StockExit es rechazado (p. ej. stock insuficiente, SKU desconocido)                                | ?                             |
| `stock_entry_failed`         | Un StockEntry es rechazado (p. ej. referencia inválida, cantidad inválida)                            | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas en TrackFlow.

| Evento candidato           | Disparador                                                                       | Sección       |
| -------------------------- | -------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`     | Inicio de sesión exitoso por un operario o coordinador de almacén                | Autenticación |
| `user_login_failed`        | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada) | Autenticación |
| `session_expired`          | La sesión del usuario expiró y fue invalidada                                    | Autenticación |
| `sku_list_viewed`          | El usuario abre la lista de stock de SKU de un almacén                           | Navegación    |
| `dispatch_form_abandoned`  | El usuario inicia pero no completa un formulario de StockExit                    | Navegación    |
| `warehouse_filter_applied` | El usuario cambia la vista entre Los Ángeles y Zaragoza                          | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble almacén:** todo evento originado en una operación de almacén debe incluir `warehouse` (`"LA"` / `"ZGZ"`) para que los datos puedan segmentarse por país. Thomas Harry no aceptará un dashboard que mezcle ambos almacenes sin una separación clara.
- **Aislamiento de datos de cliente:** TrackFlow gestiona inventario para múltiples marcas cliente. Los eventos deben usar `reference` e identificadores de SKU — nunca nombres de marca en campos de telemetría de texto libre — para evitar fugas accidentales de datos entre cuentas de cliente.
- **Sin PII en telemetría:** los campos `user_uuid` deben ser UUIDs opacos de TinyDB — nunca nombres ni direcciones de correo de operarios.
- **Sensibilidad SLA:** los fallos de StockExit con `exit_type = dispatch` en horas punta (Black Friday, Q4) tienen implicaciones contractuales de SLA. Marca los eventos `stock_exit_failed` en tu esquema como que requieren procesamiento inmediato en stream; documenta el fundamento en tu sección stream/batch.

---

## Qué debe producir tu plan para TrackFlow

- `telemetry-plan.md` referenciando `SKU`, `StockEntry` y `StockExit` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`stock_entry_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por la urgencia operativa de TrackFlow — p. ej. un stock-out para un cliente de moda de alto volumen en Los Ángeles es inmediato; un reporte semanal de ciclo de recepción no lo es.
- Una sección de riesgos y exclusiones que aborde la restricción de doble almacén, el aislamiento de datos de cliente y cualquier evento descartado.

---

_TrackFlow Tech — Documento interno para 4Geeks Academy AI Engineering Track_
