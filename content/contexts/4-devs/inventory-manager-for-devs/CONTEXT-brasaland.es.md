# CONTEXT — Brasaland: Gestor de Inventario

## 1. Panorama de la empresa

**Brasaland** opera 14 restaurantes de comida a la brasa en Colombia y Florida. Hoy el pedido de ingredientes se hace por WhatsApp o llamada telefónica, y cada encargado de local pide lo que cree que necesita — el resultado es sobrestock en unos locales y roturas de stock en otros, sin visibilidad para **Felipe Guerrero** (Director de Operaciones) ni para **Lucía Fernández** (Gerente de Compras) sobre qué hay realmente disponible en la cadena.

Estás construyendo el gestor de inventario que le da a cada local una vista precisa y en tiempo real del stock, derivada estrictamente de los movimientos registrados, con una señal automática cuando un local está a punto de quedarse sin algo que necesita para el servicio.

## 2. Catálogos del dominio

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Unidades de medida

`kg`, `g`, `l`, `ml`, `unit`

### 2.2 Categorías

| Valor | Ejemplos |
|---|---|
| `meat` | Cortes de res, pollo, cerdo |
| `produce` | Verduras, hierbas |
| `sauces_condiments` | Salsas de la casa, marinados |
| `beverages` | Refrescos, jugos |
| `packaging` | Envases para llevar, servilletas |
| `cleaning_supplies` | Desinfectante, desengrasante |

### 2.3 Locales

Cada artículo y cada movimiento pertenece a uno de los 14 locales de Brasaland. Siembra al menos 4, mezclando Colombia y Florida — el local es una dimensión de primer nivel aquí, no un añadido: el stock se controla por local, no a nivel de cadena.

## 3. Campos de la entidad

### 3.1 Artículo

- `location_id`
- `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numérico, en la unidad de medida del artículo)
- `created_at`, `updated_at`

### 3.2 Lote (obligatorio para `meat` y `produce`; opcional para el resto de categorías)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movimiento

- `item_id`, `lot_id` (nulable — solo obligatorio para artículos con control de lote)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (obligatorio para `adjustment`; p. ej. `waste`, `theft`, `count_correction`)
- `created_at`

## 4. El invariante

El stock disponible de un artículo en un local es la suma de sus movimientos `inbound` menos sus movimientos `outbound`, ajustado por las entradas de `adjustment` — calculado, nunca almacenado como campo editable. Es el mismo invariante que exige el README; este CONTEXT no lo relaja para ninguna categoría, ni siquiera `cleaning_supplies`.

## 5. Punto de reorden

`reorder_point` se define por artículo y por local — el mismo ingrediente puede tener un umbral distinto en un local de alto volumen en Medellín que en uno más pequeño en Florida. Cuando el stock de un local baja al nivel de `reorder_point` o por debajo, el backoffice debe señalarlo de forma visible.

## 6. Datos semilla

Siembra al menos 15 artículos entre al menos 4 locales y las seis categorías, con:

- Al menos 3 artículos con control de lote, incluyendo un lote con `expiry_date` en el pasado (para probar el manejo de stock caducado)
- Al menos 2 artículos actualmente en su `reorder_point` o por debajo
- Un historial de movimientos por artículo lo bastante profundo como para mostrar al menos un `inbound`, un `outbound` y un `adjustment`

## 7. Restricciones de negocio

- Un movimiento `outbound` que dejaría el stock por debajo de cero debe rechazarse — este es el criterio de "comportamiento no deseado" que exige la fase de spec del README.
- Un `outbound` o `adjustment` que referencie un `item_id` o `lot_id` inexistente debe rechazarse.
- Los motivos de ajuste `waste` y `theft` deben ser distinguibles en cualquier informe de stock, ya que el equipo de Felipe los rastrea por separado.

## 8. Entregables esperados

- Spec, plan y tareas que cubran el CRUD de artículos, el registro de movimientos y la señal de punto de reorden, limitados a los campos del §3 y usando solo los valores de catálogo del §2.
- Una suite de tests que verifique el invariante de stock (§4) y los criterios de comportamiento no deseado (§7).
- La señal de punto de reorden funcionando por local, usando los valores de tus datos semilla.
