# CONTEXT — TrackFlow: Gestor de Inventario

## 1. Panorama de la empresa

**TrackFlow** opera almacenes en Los Ángeles y Zaragoza para marcas medianas de moda, electrónica y cosmética que externalizan toda su operación logística. Cada almacén usa hoy un sistema distinto y desconectado, y **Ana Whitfield** (Directora de Operaciones de Almacén) no puede responder a "¿cuántas unidades de este SKU tenemos entre ambos países?" sin llamar a los dos sitios. Las discrepancias de inventario son frecuentes y se detectan tarde.

Estás construyendo el gestor de inventario que le da a TrackFlow una vista en tiempo real, por almacén, del stock de cada cliente, derivada estrictamente de los movimientos registrados, con una señal automática cuando un SKU está a punto de agotarse.

## 2. Catálogos del dominio

Usa exactamente estos valores. No inventes otros ni los renombres.

### 2.1 Unidades de medida

`unit`, `box`, `kg`

### 2.2 Categorías

| Valor | Ejemplos |
|---|---|
| `fashion` | Ropa, calzado, accesorios |
| `electronics` | Dispositivos pequeños, accesorios, componentes |
| `cosmetics` | Cuidado de la piel, maquillaje, cuidado personal |

### 2.3 Almacenes

Cada artículo y cada movimiento pertenece a uno de los dos almacenes de TrackFlow: `los_angeles`, `zaragoza`. El stock se controla por almacén — TrackFlow no traslada el stock de un cliente a través del Atlántico para cubrir un faltante, así que los dos nunca se compensan entre sí.

## 3. Campos de la entidad

### 3.1 Artículo

- `warehouse` (§2.3), `client_name` (la marca de e-commerce propietaria del SKU)
- `sku`, `name`, `category` (§2.2), `unit_of_measure` (§2.1)
- `reorder_point` (numérico, en la unidad de medida del artículo)
- `created_at`, `updated_at`

### 3.2 Lote (obligatorio para `cosmetics`; opcional para el resto de categorías)

- `item_id`, `lot_code`, `expiry_date`, `received_at`

### 3.3 Movimiento

- `item_id`, `lot_id` (nulable — solo obligatorio para artículos con control de lote)
- `movement_type` (`inbound`, `outbound`, `adjustment`)
- `quantity`, `reason` (obligatorio para `adjustment`; p. ej. `damaged`, `count_correction`, `return_restock`)
- `created_at`

## 4. El invariante

El stock disponible de un artículo en un almacén es la suma de sus movimientos `inbound` menos sus movimientos `outbound`, ajustado por las entradas de `adjustment` — calculado, nunca almacenado como campo editable. Es el mismo invariante que exige el README; este CONTEXT no lo relaja para ninguna categoría.

## 5. Punto de reorden

`reorder_point` se define por artículo y por almacén — el mismo SKU puede tener un umbral distinto en el almacén de Los Ángeles, de mayor volumen, que en el de Zaragoza. Cuando el stock de un almacén baja al nivel de `reorder_point` o por debajo, el backoffice debe señalarlo de forma visible, en línea con la alerta de stock bajo que usan el cliente y el equipo de compras.

## 6. Datos semilla

Siembra al menos 15 artículos entre ambos almacenes, al menos 3 clientes distintos y las tres categorías, con:

- Al menos 3 artículos de `cosmetics` con control de lote, incluyendo un lote con `expiry_date` en el pasado
- Al menos 2 artículos actualmente en su `reorder_point` o por debajo
- Un historial de movimientos por artículo lo bastante profundo como para mostrar al menos un `inbound`, un `outbound` y un `adjustment`, incluyendo al menos un ajuste `return_restock` ligado a un flujo de logística inversa

## 7. Restricciones de negocio

- Un movimiento `outbound` que dejaría el stock por debajo de cero debe rechazarse — este es el criterio de "comportamiento no deseado" que exige la fase de spec del README.
- Un `outbound` o `adjustment` que referencie un `item_id` o `lot_id` inexistente debe rechazarse.
- Dos artículos con el mismo `sku` pero distinto `client_name` son registros de inventario diferentes — los SKU no son únicos a nivel global entre clientes, solo dentro de un mismo cliente.

## 8. Entregables esperados

- Spec, plan y tareas que cubran el CRUD de artículos, el registro de movimientos y la señal de punto de reorden, limitados a los campos del §3 y usando solo los valores de catálogo del §2.
- Una suite de tests que verifique el invariante de stock (§4) y los criterios de comportamiento no deseado (§7).
- La señal de punto de reorden funcionando por almacén, usando los valores de tus datos semilla.
