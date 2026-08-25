# CONTEXT — HealthCore: Gestor de Inventario

## 1. Panorama de la empresa

**HealthCore** opera 12 clínicas ambulatorias en EE. UU. y el Reino Unido. Los suministros clínicos — EPI, consumibles, medicación de venta libre y equipamiento — se controlan hoy de forma inconsistente entre ubicaciones, sin visibilidad compartida para el equipo de operaciones clínicas del **Dr. Marcus Reid** sobre qué hay disponible y dónde. Que una clínica se quede sin un consumible básico a mitad de turno es un problema de experiencia del paciente, no solo de logística.

Estás construyendo el gestor de inventario que le da a HealthCore una vista en tiempo real, por clínica, del stock de suministros, derivada estrictamente de los movimientos registrados, con una señal automática cuando una clínica está a punto de quedarse sin algo que necesita.

## 2. ⚠️ Restricción de datos no negociable

**No puede aparecer PHI, identificadores de pacientes, ni datos regulados por HIPAA o UK GDPR en ningún log, evento, tabla, respuesta de endpoint o salida del sistema.** Este gestor de inventario controla el stock de suministros, no el consumo clínico por paciente — un artículo y sus movimientos nunca deben referirse a un paciente concreto por nombre, número de historia clínica, fecha de nacimiento ni ningún otro identificador. El campo `reason` de un movimiento describe la causa operativa de un cambio de stock (recepción, uso en una categoría de procedimiento, daño, caducidad) y nunca el paciente en el que se usó. Si tu implementación no puede describir un movimiento sin detalle de paciente, el error está en la descripción, no en la restricción.

## 3. Catálogos del dominio

Usa exactamente estos valores. No inventes otros ni los renombres.

### 3.1 Unidades de medida

`unit`, `box`, `ml`, `tablet`

### 3.2 Categorías

| Valor | Ejemplos |
|---|---|
| `ppe` | Guantes, mascarillas, batas |
| `medical_consumables` | Jeringas, gasas, tiras reactivas |
| `otc_medication` | Medicación de venta libre disponible en el centro |
| `clinical_equipment` | Termómetros, tensiómetros, dispositivos reutilizables pequeños |

### 3.3 Ubicaciones

Cada artículo y cada movimiento pertenece a una de las 12 clínicas de HealthCore, y cada clínica tiene un `country` (`us` o `uk`). Siembra al menos 4 clínicas entre ambos países — el stock se controla por clínica, no a nivel de red.

## 4. Campos de la entidad

### 4.1 Artículo

- `clinic_location`, `country` (`us` o `uk`)
- `name`, `category` (§3.2), `unit_of_measure` (§3.1)
- `reorder_point` (numérico, en la unidad de medida del artículo)
- `created_at`, `updated_at`

### 4.2 Lote (obligatorio para `medical_consumables` y `otc_medication`; opcional para el resto de categorías)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 4.3 Movimiento

- `item_id`, `lot_id` (nulable — solo obligatorio para artículos con control de lote)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (obligatorio para `adjustment`; p. ej. `damaged`, `expired`, `count_correction` — nunca una referencia a un paciente; ver §2)
- `created_at`

## 5. El invariante

El stock disponible de un artículo en una clínica es la suma de sus movimientos `inbound` menos sus movimientos `outbound`, ajustado por las entradas de `adjustment` — calculado, nunca almacenado como campo editable. Es el mismo invariante que exige el README; este CONTEXT no lo relaja para ninguna categoría.

## 6. Punto de reorden

`reorder_point` se define por artículo y por clínica — una clínica de mayor volumen necesita un umbral más alto para un consumible de rotación rápida que una más pequeña. Cuando el stock de una clínica baja al nivel de `reorder_point` o por debajo, el backoffice debe señalarlo de forma visible.

## 7. Datos semilla

Siembra al menos 15 artículos entre al menos 4 clínicas de ambos países y las cuatro categorías, con:

- Al menos 4 artículos con control de lote, incluyendo un lote con `expiry_date` en el pasado
- Al menos 2 artículos actualmente en su `reorder_point` o por debajo
- Un historial de movimientos por artículo lo bastante profundo como para mostrar al menos un `inbound`, un `outbound` y un `adjustment`
- Cero artículos, movimientos o registros semilla en todo el conjunto que incumplan el §2 — esto se evalúa, no es orientativo

## 8. Restricciones de negocio

- Un movimiento `outbound` que dejaría el stock por debajo de cero debe rechazarse — este es el criterio de "comportamiento no deseado" que exige la fase de spec del README.
- Un `outbound` o `adjustment` que referencie un `item_id` o `lot_id` inexistente debe rechazarse.
- Un movimiento `outbound` no debe poder emitirse desde un lote con `expiry_date` ya pasada — los consumibles médicos y la medicación de venta libre caducados no pueden salir del inventario para su uso.
- Cada campo, línea de log y documento generado por esta funcionalidad debe verificarse contra el §2 antes de darse por completo — incluida la salida de consola, los scripts de semilla y cualquier texto de resumen generado por IA.

## 9. Entregables esperados

- Spec, plan y tareas que cubran el CRUD de artículos, el registro de movimientos y la señal de punto de reorden, limitados a los campos del §4 y usando solo los valores de catálogo del §3, respetando el §2 sin excepción.
- Una suite de tests que verifique el invariante de stock (§5) y los criterios de comportamiento no deseado (§8).
- La señal de punto de reorden funcionando por clínica, usando los valores de tus datos semilla.
