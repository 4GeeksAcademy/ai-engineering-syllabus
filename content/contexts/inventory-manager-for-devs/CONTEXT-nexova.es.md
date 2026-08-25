# CONTEXT — Nexova: Gestor de Inventario

## 1. Panorama de la empresa

**Nexova** gestiona su operación de consultoría, selección y soporte externalizado desde dos oficinas — Valencia y Miami. No es un negocio de almacén, pero sí mantiene stock físico que hace funcionar la operación: portátiles y auriculares para los 30 agentes de soporte externalizado, kits de bienvenida de marca para nuevas incorporaciones, y materiales de formación — incluyendo bonos de examen de certificación — para la línea de formación corporativa de **Elena Vargas**. Ahora mismo ese stock vive en una hoja de cálculo en la que nadie confía: cuando entra un nuevo agente de soporte, alguien descubre que no quedan auriculares justo el primer día.

Estás construyendo el gestor de inventario que controla los activos operativos y de formación de Nexova en ambas oficinas, derivados estrictamente de los movimientos registrados, con una señal automática cuando una oficina está a punto de quedarse sin algo que necesita.

## 2. Catálogos del dominio

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Unidades de medida

`unit`, `box`

### 2.2 Categorías

| Valor | Ejemplos |
|---|---|
| `it_equipment` | Portátiles, auriculares, monitores |
| `office_supplies` | Cuadernos, credenciales, papelería |
| `training_materials` | Kits de curso impresos, bonos de examen de certificación |
| `branded_merchandise` | Kits de bienvenida, packs de onboarding |

### 2.3 Oficinas

Cada artículo y cada movimiento pertenece a una de las dos oficinas de Nexova: `valencia`, `miami`. El stock se controla por oficina, no a nivel de empresa — una rotura de stock en Miami no se cubre silenciosamente con el sobrante de Valencia.

## 3. Campos de la entidad

### 3.1 Artículo

- `office` (§2.3)
- `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numérico, en la unidad de medida del artículo)
- `created_at`, `updated_at`

### 3.2 Lote (obligatorio para `training_materials` con caducidad, como los bonos de certificación; opcional para el resto de categorías)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movimiento

- `item_id`, `lot_id` (nulable — solo obligatorio para artículos con control de lote)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (obligatorio para `adjustment`; p. ej. `damaged`, `lost`, `count_correction`)
- `created_at`

## 4. El invariante

El stock disponible de un artículo en una oficina es la suma de sus movimientos `inbound` menos sus movimientos `outbound`, ajustado por las entradas de `adjustment` — calculado, nunca almacenado como campo editable. Es el mismo invariante que exige el README; este CONTEXT no lo relaja para ninguna categoría.

## 5. Punto de reorden

`reorder_point` se define por artículo y por oficina — el stock de auriculares en Miami (30 agentes de soporte) necesita un umbral más alto que en Valencia. Cuando el stock de una oficina baja al nivel de `reorder_point` o por debajo, el backoffice debe señalarlo de forma visible.

## 6. Datos semilla

Siembra al menos 12 artículos entre ambas oficinas y las cuatro categorías, con:

- Al menos 2 artículos con control de lote (bonos de certificación), incluyendo un lote con `expiry_date` en el pasado
- Al menos 2 artículos actualmente en su `reorder_point` o por debajo
- Un historial de movimientos por artículo lo bastante profundo como para mostrar al menos un `inbound`, un `outbound` y un `adjustment`

## 7. Restricciones de negocio

- Un movimiento `outbound` que dejaría el stock por debajo de cero debe rechazarse — este es el criterio de "comportamiento no deseado" que exige la fase de spec del README.
- Un `outbound` o `adjustment` que referencie un `item_id` o `lot_id` inexistente debe rechazarse.
- Un artículo de `training_materials` con control de lote no debe poder emitirse (`outbound`) desde un lote con `expiry_date` ya pasada — un bono de certificación caducado no puede asignarse a un alumno.

## 8. Entregables esperados

- Spec, plan y tareas que cubran el CRUD de artículos, el registro de movimientos y la señal de punto de reorden, limitados a los campos del §3 y usando solo los valores de catálogo del §2.
- Una suite de tests que verifique el invariante de stock (§4) y los criterios de comportamiento no deseado (§7).
- La señal de punto de reorden funcionando por oficina, usando los valores de tus datos semilla.
