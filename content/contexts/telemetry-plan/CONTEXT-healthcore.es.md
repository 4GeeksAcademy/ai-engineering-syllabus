# CONTEXT — HealthCore · Fase 1 de Telemetría: Diseño del plan de telemetría de la compañía

_These instructions are also available in [English](./CONTEXT-healthcore.md)._

## Tu empresa

**HealthCore** es una empresa de servicios de salud ambulatorios con 12 clínicas en Estados Unidos (Texas, Florida, Georgia) y Reino Unido (Londres, Manchester). Formas parte de **HealthCore Digital**, el equipo interno de tecnología liderado por James Osei (CTO). El sistema de gestión de inventario que construiste hace seguimiento del stock de suministros médicos en las distintas clínicas — productos, pedidos de suministro entrantes y pedidos de dispensación salientes — aplicando la regla de que los niveles de stock nunca se editan directamente.

El Dr. Marcus Reid (Director de Operaciones Clínicas) y Claire Whitfield (Chief Compliance Officer) han estado haciendo preguntas que el sistema aún no puede responder. Tu plan de telemetría definirá exactamente qué datos capturar para responderlas.

---

## Entidades de tu sistema de inventario

Estos son los nombres canónicos de entidades que estableciste en el backend. Tu plan de telemetría debe referenciarlos exactamente.

| Nombre genérico (README) | Nombre de entidad HealthCore | Descripción                                                                            |
| ------------------------ | ---------------------------- | -------------------------------------------------------------------------------------- |
| `Product`                | `MedicalSupply`              | Un consumible o equipo rastreado (p. ej. guantes, jeringas, tensiómetros)              |
| `InboundOrder`           | `SupplyDelivery`             | Una entrega de proveedor que incrementa el stock de suministros médicos en una clínica |
| `OutboundOrder`          | `DispensingOrder`            | Un registro de uso clínico que reduce el stock de suministros                          |

Campos clave para referenciar en tus esquemas de eventos:

- `MedicalSupply`: `id`, `name`, `category` (`consumable`, `diagnostic_equipment`, `ppe`, `medication_adjacent`, `cleaning`), `unit`, `current_stock`, `min_stock_threshold`, `clinic_id`, `jurisdiction` (`us` / `uk`)
- `SupplyDelivery`: `id`, `supply_id`, `quantity`, `vendor`, `clinic_id`, `jurisdiction`, `created_by` (UUID de usuario TinyDB), `created_at`
- `DispensingOrder`: `id`, `supply_id`, `quantity`, `clinical_context` (`procedure`, `routine_care`, `emergency`, `waste_disposal`), `clinic_id`, `jurisdiction`, `created_by`, `created_at`

---

## Tus 3 KPIs

Estas son las métricas principales que el Dr. Reid y el Dr. Okonkwo (CEO) necesitan del sistema de suministros médicos. Tu plan debe justificar cómo la telemetría alimenta cada uno.

| #   | KPI                                                | Definición                                                                                                                           | Decisión de negocio que habilita                                                                                                    |
| --- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Tasa de disponibilidad de suministros críticos** | Porcentaje de tiempo en que EPI y consumibles de alta prioridad permanecen por encima de `min_stock_threshold` en todas las clínicas | Prevenir interrupciones en la atención clínica; activar compras de emergencia cuando la disponibilidad cae por debajo del 95%       |
| 2   | **Frecuencia de dispensación de emergencia**       | Número de DispensingOrders con `clinical_context = emergency` por clínica por semana                                                 | Identificar clínicas con necesidades recurrentes de suministros de emergencia; ajustar niveles de stock estándar de forma proactiva |
| 3   | **Tasa de incidentes de stock-out**                | Número de veces que el stock de cualquier suministro llegó a cero, segmentado por clínica y jurisdicción                             | Comparar fiabilidad de la cadena de suministro EE. UU. vs. Reino Unido; informar revisiones de rendimiento de proveedores           |

---

## Eventos candidatos — Módulo de inventario

Estos son puntos de partida sugeridos. Puedes refinarlos, dividirlos, fusionarlos o descartarlos — pero cada evento que mantengas debe superar la prueba de la regla de oro.

| Evento candidato               | Disparador                                                                                    | ¿Stream o batch? (tú decides) |
| ------------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------- |
| `supply_delivery_created`      | Se registra exitosamente un SupplyDelivery                                                    | ?                             |
| `dispensing_order_created`     | Se registra exitosamente un DispensingOrder                                                   | ?                             |
| `stock_threshold_triggered`    | El stock de un suministro cae a o por debajo de `min_stock_threshold` tras una dispensación   | ?                             |
| `direct_stock_edit_rejected`   | Una solicitud de modificar el stock directamente (fuera de un pedido) es bloqueada por la API | ?                             |
| `dispensing_order_failed`      | Un DispensingOrder es rechazado (p. ej. stock insuficiente, contexto clínico inválido)        | ?                             |
| `emergency_dispensing_flagged` | Se crea un DispensingOrder con `clinical_context = emergency`                                 | ?                             |

---

## Eventos candidatos — Backoffice (más allá del inventario)

Cubren otras secciones de la aplicación de backoffice. Elige los que produzcan datos relevantes para tus KPIs o para decisiones operativas en HealthCore.

| Evento candidato            | Disparador                                                                          | Sección       |
| --------------------------- | ----------------------------------------------------------------------------------- | ------------- |
| `user_login_succeeded`      | Inicio de sesión exitoso por un gestor de clínica o administrador                   | Autenticación |
| `user_login_failed`         | Intento de inicio de sesión fallido (credenciales incorrectas o sesión expirada)    | Autenticación |
| `session_expired`           | La sesión del usuario expiró y fue invalidada                                       | Autenticación |
| `supply_list_viewed`        | El usuario abre la lista de stock de suministros médicos de una clínica             | Navegación    |
| `dispensing_form_abandoned` | El usuario inicia pero no completa un formulario de DispensingOrder                 | Navegación    |
| `clinic_filter_applied`     | El usuario filtra la vista de suministros por una clínica o jurisdicción específica | Navegación    |

---

## Restricciones de negocio para tu plan

- **Doble jurisdicción — HIPAA y UK GDPR:** cualquier evento que pueda vincularse a un paciente — directa o indirectamente — queda bajo HIPAA (EE. UU.) o UK GDPR (Reino Unido). Los eventos de `DispensingOrder` vinculados a un procedimiento de paciente específico no deben incluir identificadores de paciente; usa solo `clinic_id` y `clinical_context`. Documenta esto explícitamente en tu sección de riesgos y exclusiones.
- **El campo `jurisdiction` es obligatorio:** todo evento originado en una operación de clínica debe incluir `jurisdiction` (`us` / `uk`) y `clinic_id`. Claire Whitfield requiere auditorías segmentadas por jurisdicción para informes de cumplimiento.
- **Sin PII en telemetría:** los campos `created_by` deben ser UUIDs opacos de TinyDB — nunca nombres ni direcciones de correo del personal.
- **Los eventos de emergencia requieren procesamiento en stream:** cualquier evento con `clinical_context = emergency` o un `stock_threshold_triggered` para EPI o consumibles críticos debe tratarse como evento de stream. Un stock-out de guantes quirúrgicos no es un problema de reporte batch. Documenta el fundamento clínico en tu justificación stream/batch.
- **Durabilidad de la auditoría:** a diferencia de otras empresas, los eventos de telemetría de HealthCore por movimientos de suministros pueden ser citados en una auditoría clínica. Tu esquema debe incluir `schemaVersion` y los eventos deben tratarse como inmutables una vez creados.

---

## Qué debe producir tu plan para HealthCore

- `telemetry-plan.md` referenciando `MedicalSupply`, `SupplyDelivery` y `DispensingOrder` por nombre, con eventos justificados frente a los tres KPIs anteriores.
- `event-schemas.json` con al menos 5 esquemas de eventos completos usando nomenclatura `entity_action` (`supply_delivery_created`, `stock_threshold_triggered`, etc.), cada uno con una **lista blanca de propiedades** documentada — solo las claves declaradas explícitamente están permitidas en ese evento.
- Una decisión stream/batch para cada evento justificada por urgencia clínica — los eventos de suministro de emergencia son stream no negociable; el reporte de reposición rutinaria es batch.
- Una sección de riesgos y exclusiones que aborde las restricciones HIPAA/UK GDPR, la prohibición de identificadores de paciente en telemetría y cualquier evento descartado.

---

_HealthCore Digital — Documento interno para 4Geeks Academy AI Engineering Track_
