# CONTEXT — TrackFlow

## Proyectos de Telemetría (Plan · Captura · Almacenamiento · Reporte)

<!-- hide -->

_These instructions are [available in English](./CONTEXT-trackflow.md)._

<!-- endhide -->

---

## 1. Tu compañía

TrackFlow gestiona almacenes y última milla para marcas de moda, electrónica y cosmética, operando entre Los Ángeles y Zaragoza. El sistema de inventario es el corazón operativo de la compañía: el stock de cada SKU de cada cliente, en cada almacén.

Hoy Brasaland vende comida y Nexova vende formación; en TrackFlow el inventario **es literalmente el negocio**. Tu Plan de Telemetría, tu captura, tu almacenamiento y tu reporte técnico giran alrededor de ese sistema, y son la base sobre la que, más adelante, TrackFlow construirá el dashboard operativo de Ana y el dashboard ejecutivo global de Thomas.

---

## 2. Entidades del sistema de inventario en TrackFlow

| Entidad         | En TrackFlow significa...                                                                                 |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| `Product`      | Un SKU perteneciente a un cliente (marca): ej. `camiseta talla M — Cliente Fashion Co`, `auricular bluetooth — Cliente ElectroBrand`. Cada SKU tiene una categoría (moda, electrónica, cosmética) y pertenece a un cliente. |
| `InboundOrder`  | Una orden de entrada: recepción de mercancía de un cliente en un almacén (Los Ángeles o Zaragoza).           |
| `OutboundOrder` | Una orden de salida: preparación (picking) y despacho de un pedido hacia el transportista para entrega al consumidor final. |
| `warehouse`     | Los Ángeles o Zaragoza.                                                                                       |
| `client`        | La marca (cliente B2B) dueña del SKU.                                                                        |

---

## 3. Métricas obligatorias de telemetría

Estas son las métricas que TrackFlow necesita medir **desde ya**, sin importar qué más identifiques en tu propio catálogo. Van directamente al piso de tu Plan de Telemetría (Fase 1) y deben estar instrumentadas de punta a punta al final de la serie de proyectos.

> Estas métricas alimentarán, más adelante en el curso, el dashboard de operaciones de almacén de Ana y el dashboard ejecutivo global de Thomas (comparación de volumen y SLA entre Estados Unidos y España). Diséñalas pensando en que se agregarán por almacén, por cliente y por país.

| `event_type`                       | Se dispara cuando...                                                                        | Hipótesis de negocio                                                                                | Decisión que habilita                                                                       |
| ------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `inbound_order_created`              | Un almacén registra la recepción de mercancía de un cliente                                        | Necesitamos saber cuánto volumen entra, por cliente y por almacén                                          | Planificar capacidad de almacén y personal según el volumen entrante (Ana)                          |
| `outbound_order_created`             | Un almacén completa el picking y despacho de un pedido                                             | Necesitamos saber cuántos pedidos se procesan, por cliente y almacén, y a qué ritmo                        | Detectar cuellos de botella operativos antes de que afecten el SLA de entrega (Ana)                 |
| `stock_threshold_triggered`         | El stock de un SKU cae por debajo del mínimo configurado para ese cliente                          | Necesitamos saber con qué frecuencia un cliente se queda sin stock disponible de un SKU                    | Alertar al cliente y al equipo comercial antes de un quiebre de stock (Miguel)                       |
| `direct_stock_edit_rejected`        | Un usuario intenta modificar el stock directamente (fuera de una orden) y el sistema lo rechaza    | Necesitamos saber si el personal de almacén intenta saltarse el control de trazabilidad                    | Reforzar capacitación o permisos en el almacén donde esto ocurre con más frecuencia                  |
| `inventory_discrepancy_detected`    | Un conteo físico o una auditoría detecta una diferencia entre el stock del sistema y el stock real | Necesitamos saber en qué SKUs y almacenes ocurren más discrepancias                                        | Priorizar auditorías de inventario en los SKUs con mayor tasa de discrepancia (Ana)                  |

**Campos mínimos en `properties` para los eventos de inventario** (además del envelope estándar): `warehouse` (`los_angeles`/`zaragoza`), `client_id`, `product_id` (SKU), `product_category`, `quantity`.

⚠️ No incluyas datos personales del consumidor final (destinatario del paquete) en `properties` — estos eventos describen inventario de almacén, no envíos individuales a domicilio (eso corresponde al proyecto de tracking de última milla).

---

## 4. Cómo estas métricas conectan con el futuro

Estas métricas no son solo para el reporte técnico de hoy. A medida que avance el curso, estos mismos datos se van a reutilizar para automatizaciones y para reportes a nivel ejecutivo — con un nivel de agregación y de pulido bastante mayor al que estás construyendo ahora mismo. Diséñalas como si alguien más, más adelante, fuera a depender de ellas sin poder preguntarte cómo funcionan.

---

## 5. Datos semilla sugeridos

Genera al menos:

- 8–10 SKUs distintos, de al menos 2 clientes distintos y cubriendo las 3 categorías (moda, electrónica, cosmética)
- Los 2 almacenes (Los Ángeles y Zaragoza)
- 15–20 órdenes de entrada distribuidas entre ambos almacenes
- 15–20 órdenes de salida
- Al menos 2 casos que disparen `stock_threshold_triggered` y 1 caso de `inventory_discrepancy_detected`

---

## 6. Restricciones de negocio

- El stock nunca se modifica directamente: toda modificación pasa por `InboundOrder` u `OutboundOrder`, trazable a un usuario.
- Cada SKU pertenece a un único cliente — no mezcles inventario entre clientes en el mismo `product_id`.
- Los eventos de inventario no incluyen datos del transportista ni del destinatario final — eso pertenece al dominio de última milla, fuera del alcance de este sistema.
