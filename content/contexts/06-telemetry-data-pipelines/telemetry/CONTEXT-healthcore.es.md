# CONTEXT — HealthCore

## Proyectos de Telemetría (Plan · Captura · Almacenamiento · Reporte)

<!-- hide -->

_These instructions are [available in English](./CONTEXT-healthcore.md)._

<!-- endhide -->

---

## 1. Tu compañía

HealthCore opera 12 clínicas ambulatorias entre Estados Unidos (Texas, Florida, Georgia) y el Reino Unido (Londres, Manchester). El sistema de inventario controla los **insumos clínicos**: medicamentos de uso común, material de curación, EPP (equipo de protección personal), y consumibles de consultorio en cada clínica.

Tu Plan de Telemetría, tu captura, tu almacenamiento y tu reporte técnico giran alrededor de ese sistema. Más adelante, esta misma telemetría alimentará el dashboard operativo de la red y el reporte ejecutivo mensual de la Dra. Okonkwo.

> ⚠️ **Nota regulatoria (HIPAA / UK GDPR):** los eventos de este sistema describen **insumos y existencias**, nunca pacientes. Ningún campo de `properties` debe contener nombres de pacientes, identificadores de historia clínica, diagnósticos, ni ningún dato real o simulado que pudiera interpretarse como información de salud protegida (PHI). Si necesitas asociar un consumo de insumo a un contexto clínico, usa únicamente el `department` o el tipo de servicio (ej. `general_consultation`, `chronic_care`), nunca un identificador de paciente.

---

## 2. Entidades del sistema de inventario en HealthCore

| Entidad         | En HealthCore significa...                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| `Product`      | Un insumo clínico o de consultorio: ej. `guantes de nitrilo (caja)`, `jeringas 5ml`, `vacuna antigripal`, `mascarilla quirúrgica`. Cada producto tiene una categoría (`medication`, `ppe`, `consumable`, `equipment`) y, cuando aplica, una fecha de vencimiento. |
| `InboundOrder`  | Una orden de entrada: recepción de insumos de un proveedor en una clínica.                               |
| `OutboundOrder` | Una orden de salida: consumo de un insumo en la atención clínica (registrado por departamento, no por paciente). |
| `clinic`        | Una de las 12 clínicas, identificada por país (`US`/`UK`) y estado/región.                                |
| `department`    | Atención primaria, especialidades, manejo de enfermedades crónicas, etc.                                  |

---

## 3. Métricas obligatorias de telemetría

Estas son las métricas que HealthCore necesita medir **desde ya**, sin importar qué más identifiques en tu propio catálogo. Van directamente al piso de tu Plan de Telemetría (Fase 1) y deben estar instrumentadas de punta a punta al final de la serie de proyectos.

> Estas métricas alimentarán, más adelante en el curso, el dashboard operativo de red de la Dra. Okonkwo y las alertas de cumplimiento de Claire. Diséñalas pensando en que se agregarán por clínica y por país (US/UK), respetando siempre HIPAA y UK GDPR.

| `event_type`                       | Se dispara cuando...                                                                          | Hipótesis de negocio                                                                                     | Decisión que habilita                                                                              |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `inbound_order_created`              | Una clínica registra la recepción de insumos de un proveedor                                        | Necesitamos saber cuánto y qué insumo se compra, por clínica y proveedor                                        | Consolidar compras entre clínicas y negociar mejores condiciones con proveedores                            |
| `outbound_order_created`             | Una clínica registra el consumo de un insumo en la atención de un departamento                      | Necesitamos saber qué insumos se consumen más, y a qué ritmo, por clínica y departamento                       | Ajustar la reposición automática de insumos críticos por clínica                                            |
| `stock_threshold_triggered`          | El stock de un insumo cae por debajo del mínimo configurado para esa clínica                        | Necesitamos saber con qué frecuencia una clínica se queda corta de un insumo crítico (ej. EPP, medicamento)     | Priorizar el reabastecimiento urgente y escalar a Marcus (Operaciones Clínicas)                             |
| `direct_stock_edit_rejected`         | Un usuario intenta modificar el stock directamente (fuera de una orden) y el sistema lo rechaza      | Necesitamos saber si el personal intenta saltarse el control de trazabilidad de insumos                          | Reforzar capacitación o permisos en la clínica donde esto ocurre con más frecuencia                          |
| `supply_expiry_flagged`             | Un lote de insumo (medicamento o material) se acerca a su fecha de vencimiento (ej. 30 días)         | Necesitamos saber qué insumos están por vencer antes de que se conviertan en pérdida o riesgo de cumplimiento   | Priorizar el uso o la baja controlada de ese lote antes del vencimiento                                     |

**Campos mínimos en `properties` para los eventos de inventario** (además del envelope estándar): `clinic_id`, `country` (`US`/`UK`), `product_id`, `product_category` (`medication`/`ppe`/`consumable`/`equipment`), `quantity`, `department` (solo cuando aplique, nunca un identificador de paciente).

⚠️ **Recordatorio crítico:** ningún evento de este catálogo debe contener PHI. `department` describe el área clínica, no a una persona atendida.

---

## 4. Cómo estas métricas conectan con el futuro

Estas métricas no son solo para el reporte técnico de hoy. A medida que avance el curso, estos mismos datos se van a reutilizar para automatizaciones y para reportes a nivel ejecutivo — con un nivel de agregación y de pulido bastante mayor al que estás construyendo ahora mismo. Diséñalas como si alguien más, más adelante, fuera a depender de ellas sin poder preguntarte cómo funcionan.

---

## 5. Datos semilla sugeridos

Genera al menos:

- 8–10 insumos distintos, cubriendo las 4 categorías (`medication`, `ppe`, `consumable`, `equipment`)
- 3 clínicas (al menos una en EE.UU. y una en el Reino Unido)
- 15–20 órdenes de entrada distribuidas entre esas clínicas
- 15–20 órdenes de salida, asociadas únicamente a `department`, nunca a un paciente
- Al menos 2 casos que disparen `stock_threshold_triggered` y 1 caso de `supply_expiry_flagged`

---

## 6. Restricciones de negocio

- El stock nunca se modifica directamente: toda modificación pasa por `InboundOrder` u `OutboundOrder`, trazable a un usuario del staff (nunca a un paciente).
- Ningún dato real o simulado de paciente (nombre, identificador de historia clínica, diagnóstico) puede aparecer en ningún campo de estos eventos, ni siquiera como dato de prueba.
- Los insumos con fecha de vencimiento deben registrar esa fecha en el modelo de `Product`, no solo en la orden — es lo que permite calcular `supply_expiry_flagged` de forma consistente entre clínicas.
