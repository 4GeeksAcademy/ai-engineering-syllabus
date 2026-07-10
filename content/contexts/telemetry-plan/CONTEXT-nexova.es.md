# CONTEXT — Nexova · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-nexova.en.md)._

## Tu empresa

**Nexova** es una consultora de RRHH y adquisición de talento con oficinas en Valencia, España y Miami, Florida. Formas parte del equipo interno de AI Engineering que reporta a Sergio Molina (CTO). El sistema de gestión de inventario que construiste hace seguimiento de activos de oficina y equipos IT — activos, entradas entrantes y salidas salientes — aplicando la regla de que la disponibilidad de activos nunca se edita directamente.

Patricia Solís (HR Manager) y Sergio han estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad Nexova | Descripción                                                                          |
| ------------------------ | ------------------------ | ------------------------------------------------------------------------------------ |
| `Product`                | `Asset`                  | Un ítem rastreado (p. ej. portátil, monitor, silla ergonómica, material de oficina) |
| `InboundOrder`           | `AssetEntry`             | Una compra o entrega que incrementa el stock disponible de activos                   |
| `OutboundOrder`          | `AssetExit`              | Una asignación a un empleado o un evento de consumo que reduce el stock              |

Campos clave para referenciar en tus esquemas de eventos:

- `Asset`: `id`, `name`, `sku`, `category` (`hardware`, `peripherals`, `office_supplies`, `training_materials`), `office` (`"Valencia"` / `"Miami"`), `current_stock`
- `AssetEntry`: `id`, `asset_id`, `quantity`, `supplier`, `office`, `user_uuid`, `created_at`
- `AssetExit`: `id`, `asset_id`, `quantity`, `exit_type` (`allocation` / `consumption`), `assigned_to` (nullable), `office`, `user_uuid`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que Patricia y Laura Mendoza (CEO) necesitan del sistema de gestión de activos. Tu plan debe justificar cómo la telemetría alimenta cada una.

| #   | KPI                                                 | Definición                                                                                                                  | Decisión de negocio que habilita                                                                                            |
| --- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Tiempo de entrega de asignación de activos**      | Tiempo transcurrido entre el primer acceso registrado del empleado al flujo de salida y la creación del AssetExit           | Detectar fricción en el proceso de entrega de activos en onboarding; identificar oficinas con flujos de asignación lentos   |
| 2   | **Frecuencia de stock-out por categoría de activo** | Número de veces que una categoría de activo llegó a cero unidades disponibles en un período, segmentado por oficina         | Asegurar que el hardware crítico (portátiles, periféricos) nunca esté indisponible en onboarding; ajustar cadencia de compras |
| 3   | **Tiempo de ciclo de compras**                      | Días promedio entre eventos AssetEntry consecutivos para el mismo activo                                                    | Identificar activos comprados de forma reactiva (demasiado tarde) vs. proactiva; optimizar puntos de reorden                |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato             | Disparador                                                                                               | ¿Stream o batch? (tú decides) |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `asset_entry_created`        | Se registra exitosamente un AssetEntry                                                                     | ?                             |
| `asset_exit_created`         | Se registra exitosamente un AssetExit                                                                      | ?                             |
| `stock_threshold_triggered`  | El stock de un activo cae a o por debajo de `min_stock_threshold` tras una salida                          | ?                             |
| `direct_stock_edit_rejected` | Una solicitud de modificar el stock del activo directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `asset_exit_failed`          | Un AssetExit es rechazado (p. ej. stock insuficiente, error de validación)                                 | ?                             |
| `asset_entry_failed`         | Un AssetEntry es rechazado (p. ej. proveedor desconocido, cantidad inválida)                               | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas en Nexova.

| Evento candidato            | Disparador                                                                       | Sección       |
| --------------------------- | -------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`      | Inicio de sesión exitoso por un operador de RRHH o consultor                     | Autenticación |
| `user_login_failed`         | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada) | Autenticación |
| `session_expired`           | La sesión del usuario expiró y fue invalidada                                    | Autenticación |
| `asset_list_viewed`         | El usuario abre la lista de stock de activos                                     | Navegación    |
| `assignment_form_abandoned` | El usuario inicia pero no completa un formulario de AssetExit                    | Navegación    |
| `office_filter_applied`     | El usuario filtra la vista de activos por Valencia o Miami                       | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble oficina:** los activos se gestionan de forma independiente por oficina (`"Valencia"` / `"Miami"`). Los eventos deben incluir `office` para segmentar datos por ubicación.
- **Sensibilidad del tipo de salida:** los eventos AssetExit con `exit_type = allocation` vinculan stock a un empleado en los datos de negocio — la telemetría registra la acción solo con `exit_type`, nunca con nombres de empleados.
- **Sin PII en telemetría:** los campos `user_uuid` deben ser UUIDs opacos de TinyDB — nunca nombres ni direcciones de correo de empleados.
- **Riesgo de auditoría de hardware:** los eventos AssetExit para `category = hardware` pueden estar sujetos a auditoría de proveedor. Márcalos en tu esquema como que requieren una auditoría completa; documenta esto en tu sección de riesgos y exclusiones.

---

## Qué debe producir tu plan para Nexova

- `telemetry-plan.md` referenciando `Asset`, `AssetEntry` y `AssetExit` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`asset_entry_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por la urgencia operativa de Nexova — p. ej. un stock-out de portátil el día de onboarding de un nuevo consultor es urgencia inmediata; el reporte de ciclo de compras es semanal.
- Una sección de riesgos y exclusiones que aborde la restricción de doble oficina, los requisitos de auditoría de hardware y cualquier evento descartado.

---

_Nexova AI Engineering Team — Documento interno para 4Geeks Academy AI Engineering Track_
