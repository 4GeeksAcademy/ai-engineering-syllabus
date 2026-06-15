# CONTEXT — Brasaland · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-brasaland.md)._

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la parrilla con 14 ubicaciones en Colombia y Florida. Formas parte de **Brasaland Digital**, el equipo interno de tecnología liderado por Nicolás Park (CTO). El sistema de gestión de inventario que construiste hace seguimiento del stock de ingredientes en todas las ubicaciones — productos, pedidos de suministro entrantes y pedidos de consumo salientes — aplicando la regla de que los niveles de stock nunca se editan directamente.

El equipo de operaciones (Felipe Guerrero, Operations Director) ha estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad Brasaland | Descripción                                                                  |
| ------------------------ | --------------------------- | ---------------------------------------------------------------------------- |
| `Product`                | `Ingredient`                | Un ingrediente rastreado (p. ej. corte de carne, salsa, material de empaque) |
| `InboundOrder`           | `SupplyOrder`               | Una entrega de proveedor que incrementa el stock de ingredientes             |
| `OutboundOrder`          | `ConsumptionOrder`          | Un registro de consumo de cocina que reduce el stock de ingredientes         |

Campos clave para referenciar en tus esquemas de eventos:

- `Ingredient`: `id`, `name`, `category` (`meat`, `produce`, `sauce`, `beverage`, `packaging`, `cleaning`), `unit`, `current_stock`, `min_stock_threshold`, `location_id`, `currency` (`COP` / `USD`)
- `SupplyOrder`: `id`, `ingredient_id`, `quantity`, `supplier_id`, `location_id`, `created_by` (UUID de usuario TinyDB), `created_at`
- `ConsumptionOrder`: `id`, `ingredient_id`, `quantity`, `reason` (`kitchen_use`, `waste`, `spoilage`, `theft`), `location_id`, `created_by`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que Felipe y Mariana (CEO) necesitan del sistema de inventario. Tu plan debe justificar cómo la telemetría alimenta cada una.

| #   | KPI                                                    | Definición                                                                                          | Decisión de negocio que habilita                                                                             |
| --- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1   | **Tasa de consumo diario por ingrediente y ubicación** | Unidades consumidas por ingrediente por ubicación por día (vía ConsumptionOrders)                   | Detectar ubicaciones que consumen por encima de lo esperado respecto a ventas; ajustar pedidos a proveedores |
| 2   | **Frecuencia de stock-out**                            | Número de veces que el stock de un ingrediente llegó a cero o activó el umbral mínimo en un período | Identificar ingredientes crónicamente infraabastecidos; renegociar contratos de suministro                   |
| 3   | **Ratio de desperdicio y pérdida**                     | Proporción de ConsumptionOrders con `reason = waste / spoilage / theft` frente al consumo total     | Marcar ubicaciones con patrones anómalos de desperdicio; activar investigación operativa                     |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato             | Disparador                                                                                    | ¿Stream o batch? (tú decides) |
| ---------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| `supply_order_created`       | Se registra exitosamente un SupplyOrder                                                       | ?                             |
| `consumption_order_created`  | Se registra exitosamente un ConsumptionOrder                                                  | ?                             |
| `stock_threshold_triggered`  | El stock de un ingrediente cae a o por debajo de `min_stock_threshold` tras un pedido         | ?                             |
| `direct_stock_edit_rejected` | Una solicitud de modificar el stock directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `consumption_order_failed`   | Un ConsumptionOrder es rechazado (p. ej. stock insuficiente, error de validación)             | ?                             |
| `supply_order_failed`        | Un SupplyOrder es rechazado (p. ej. proveedor desconocido, cantidad inválida)                 | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas de Brasaland.

| Evento candidato          | Disparador                                                                         | Sección       |
| ------------------------- | ---------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`    | Inicio de sesión exitoso por un gestor de ubicación u operario                     | Autenticación |
| `user_login_failed`       | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada)   | Autenticación |
| `session_expired`         | La sesión del usuario expiró y fue invalidada                                      | Autenticación |
| `ingredient_list_viewed`  | El usuario abre la lista de stock de ingredientes de una ubicación                 | Navegación    |
| `order_form_abandoned`    | El usuario inicia pero no completa un formulario de SupplyOrder o ConsumptionOrder | Navegación    |
| `location_filter_applied` | El usuario filtra la vista de stock por una ubicación específica                   | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble moneda:** los ingredientes en ubicaciones colombianas se valoran en COP; las de Florida en USD. Los eventos que incluyan campos de costo o valor deben llevar la propiedad `currency`.
- **Sensibilidad multi-ubicación:** todo evento originado en un restaurante específico debe incluir `location_id` para segmentar datos por país y ciudad.
- **Sin PII en telemetría:** los campos `created_by` deben incluirse como UUIDs opacos de TinyDB — nunca como nombres ni direcciones de correo.
- **Desperdicio y robo son sensibles:** los eventos de `ConsumptionOrder` con `reason = theft` deben marcarse en tu esquema como que requieren acceso restringido; documenta esto en tu sección de riesgos y exclusiones.

---

## Qué debe producir tu plan para Brasaland

- `telemetry-plan.md` referenciando `Ingredient`, `SupplyOrder` y `ConsumptionOrder` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`supply_order_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por la urgencia operativa de Brasaland — p. ej. un stock-out en una ubicación de alto volumen en Miami un viernes por la noche no tiene la misma urgencia que un resumen semanal de desperdicio.
- Una sección de riesgos y exclusiones que aborde las restricciones de doble moneda y multi-ubicación, y explique cualquier evento descartado.

---

_Brasaland Digital — Documento interno para 4Geeks Academy AI Engineering Track_
