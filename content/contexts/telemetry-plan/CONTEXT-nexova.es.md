# CONTEXT — Nexova · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-nexova.md)._

## Tu empresa

**Nexova** es una consultora de RRHH y adquisición de talento con oficinas en Valencia, España y Miami, Florida. Formas parte del equipo interno de AI Engineering que reporta a Sergio Molina (CTO). El sistema de gestión de inventario que construiste hace seguimiento de activos de oficina y equipos IT asignados a empleados — productos, pedidos de compra entrantes y pedidos de asignación salientes — aplicando la regla de que la disponibilidad de activos nunca se edita directamente.

Patricia Solís (HR Manager) y Sergio han estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad Nexova | Descripción                                                                          |
| ------------------------ | ------------------------ | ------------------------------------------------------------------------------------ |
| `Product`                | `Asset`                  | Un ítem rastreado (p. ej. portátil, monitor, silla ergonómica, licencia de software) |
| `InboundOrder`           | `ProcurementOrder`       | Una compra o entrega que incrementa el stock disponible de activos                   |
| `OutboundOrder`          | `AssignmentOrder`        | Una asignación a un empleado que reduce el stock disponible                          |

Campos clave para referenciar en tus esquemas de eventos:

- `Asset`: `id`, `name`, `category` (`hardware`, `software_licence`, `furniture`, `peripheral`, `consumable`), `unit`, `current_stock`, `min_stock_threshold`, `office` (`valencia` / `miami`), `assigned_to` (UUID de usuario TinyDB nullable — solo poblado cuando `current_stock = 0` para activos de unidad única)
- `ProcurementOrder`: `id`, `asset_id`, `quantity`, `vendor`, `office`, `created_by` (UUID de usuario TinyDB), `created_at`
- `AssignmentOrder`: `id`, `asset_id`, `quantity`, `assigned_to` (UUID de empleado TinyDB), `office`, `created_by`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que Patricia y Laura Mendoza (CEO) necesitan del sistema de gestión de activos. Tu plan debe justificar cómo la telemetría alimenta cada una.

| #   | KPI                                                 | Definición                                                                                                                  | Decisión de negocio que habilita                                                                                            |
| --- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Tiempo de entrega de asignación de activos**      | Tiempo transcurrido entre el primer acceso registrado del empleado al flujo de asignación y la creación del AssignmentOrder | Detectar fricción en el proceso de entrega de activos en onboarding; identificar oficinas con flujos de asignación lentos   |
| 2   | **Frecuencia de stock-out por categoría de activo** | Número de veces que una categoría de activo llegó a cero unidades disponibles en un período, segmentado por oficina         | Asegurar que el hardware crítico (portátiles, licencias) nunca esté indisponible en onboarding; ajustar cadencia de compras |
| 3   | **Tiempo de ciclo de compras**                      | Días promedio entre ProcurementOrders consecutivos para el mismo activo                                                     | Identificar activos comprados de forma reactiva (demasiado tarde) vs. proactiva; optimizar puntos de reorden                |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato             | Disparador                                                                                               | ¿Stream o batch? (tú decides) |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `procurement_order_created`  | Se registra exitosamente un ProcurementOrder                                                             | ?                             |
| `assignment_order_created`   | Se registra exitosamente un AssignmentOrder                                                              | ?                             |
| `stock_threshold_triggered`  | El stock de un activo cae a o por debajo de `min_stock_threshold` tras una asignación                    | ?                             |
| `direct_stock_edit_rejected` | Una solicitud de modificar el stock del activo directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `assignment_order_failed`    | Un AssignmentOrder es rechazado (p. ej. stock insuficiente, `assigned_to` faltante)                      | ?                             |
| `procurement_order_failed`   | Un ProcurementOrder es rechazado (p. ej. proveedor desconocido, cantidad inválida)                       | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas en Nexova.

| Evento candidato            | Disparador                                                                       | Sección       |
| --------------------------- | -------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`      | Inicio de sesión exitoso por un operador de RRHH o consultor                     | Autenticación |
| `user_login_failed`         | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada) | Autenticación |
| `session_expired`           | La sesión del usuario expiró y fue invalidada                                    | Autenticación |
| `asset_list_viewed`         | El usuario abre la lista de stock de activos                                     | Navegación    |
| `assignment_form_abandoned` | El usuario inicia pero no completa un formulario de AssignmentOrder              | Navegación    |
| `office_filter_applied`     | El usuario filtra la vista de activos por Valencia o Miami                       | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble oficina:** los activos se gestionan de forma independiente por oficina (`valencia` / `miami`). Los eventos deben incluir `office` para segmentar datos por ubicación.
- **Sensibilidad de activos de unidad única:** para activos donde `current_stock` representa una unidad física única (portátiles, teléfonos), un `AssignmentOrder` efectivamente lo retira del stock disponible y lo vincula a un empleado. Tu esquema de evento para `assignment_order_created` debe incluir tanto `asset_id` como `assigned_to`.
- **Sin PII en telemetría:** los campos `assigned_to` y `created_by` deben ser UUIDs opacos de TinyDB — nunca nombres ni direcciones de correo de empleados.
- **Riesgo de cumplimiento de licencias de software:** los eventos de `AssignmentOrder` para `category = software_licence` están sujetos a auditoría de proveedor. Márcalos en tu esquema como que requieren una auditoría completa y duradera; documenta esto en tu sección de riesgos y exclusiones.

---

## Qué debe producir tu plan para Nexova

- `telemetry-plan.md` referenciando `Asset`, `ProcurementOrder` y `AssignmentOrder` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`procurement_order_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por la urgencia operativa de Nexova — p. ej. un stock-out de portátil el día de onboarding de un nuevo consultor es urgencia inmediata; el reporte de ciclo de compras es semanal.
- Una sección de riesgos y exclusiones que aborde la restricción de doble oficina, el requisito de auditoría de licencias de software y cualquier evento descartado.

---

_Nexova AI Engineering Team — Documento interno para 4Geeks Academy AI Engineering Track_
