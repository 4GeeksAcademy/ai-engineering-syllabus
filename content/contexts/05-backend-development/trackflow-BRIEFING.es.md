# BRIEFING — Hito 5: Gestión de Inventario Backend
## Empresa: TrackFlow

**Ruta:** `05-backend-inventory-orm/trackflow-BRIEFING.es.md`

---

## Tu Empresa

**TrackFlow** es una empresa de logística de último kilómetro y gestión de almacenes con operaciones en Los Ángeles (EE.UU.) y Zaragoza (España). Su negocio principal es gestionar el inventario de almacén en nombre de marcas de e-commerce — moda, electrónica y cosmética — que externalizan toda su operación logística.

Cada unidad de producto que pasa por los almacenes de TrackFlow debe registrarse con precisión: cuando llega de la marca cliente, y cuando sale hacia la entrega al cliente final. Una discrepancia en el stock es un problema contractual, no solo interno. Los clientes esperan exactitud en tiempo real.

Hasta ahora, cada almacén ha utilizado un sistema diferente (un WMS comercial y una hoja de cálculo avanzada) sin una capa de datos compartida. **Andrés Kim (CTO)** ha escalado esto a hito prioritario.

> **De Andrés (CTO) — Ticket Linear TRK-0341:**
> "Esta es la base de todo. Necesitamos una API de inventario unificada para SKUs en ambos almacenes. Una 'entrada de stock' es una recepción de mercancía de una marca cliente. Una 'salida de stock' es un despacho para un envío a cliente o una pérdida confirmada. El stock siempre se calcula — entradas menos salidas — nunca se establece directamente. Todas las rutas bajo `/inventory`. La especificación completa de entidades está a continuación. La autenticación se queda en TinyDB."

---

## Nombres de Entidades y Especificación de Campos

Usa estos nombres exactamente en tus modelos, schemas y respuestas de la API.

### `SKU` (equivale a `Product` del README)

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `name` | `str` | Descripción del producto, ej.: `"Zapatilla blanca clásica - Talla 42"` |
| `sku` | `str` | Código asignado por el cliente, ej.: `"CLT-SNK-W-42"` |
| `client_name` | `str` | La marca propietaria de este SKU, ej.: `"PureStep Footwear"` |
| `category` | `str` | `"fashion"`, `"electronics"` o `"cosmetics"` |
| `warehouse` | `str` | `"LA"` (Los Ángeles) o `"ZGZ"` (Zaragoza) |
| `current_stock` | `int` | **Campo calculado — no almacenado.** Derivado de los movimientos de stock. Incluir solo en el schema de respuesta. |

### `StockEntry` (equivale a `InboundOrder` del README)

Una recepción de mercancía: un envío de una marca cliente llega a un almacén de TrackFlow.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `sku_id` | `int` (FK → SKU) | |
| `quantity` | `int` | Unidades recibidas |
| `reference` | `str` | Referencia de despacho del cliente (p. ej., número de orden de compra) |
| `warehouse` | `str` | `"LA"` o `"ZGZ"` — almacén receptor |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del operario de almacén que confirmó la recepción (de TinyDB) |

### `StockExit` (equivale a `OutboundOrder` del README)

Un despacho: las unidades salen del almacén para una entrega a cliente o se dan de baja como pérdida.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `sku_id` | `int` (FK → SKU) | |
| `quantity` | `int` | Unidades despachadas o dadas de baja |
| `exit_type` | `str` | `"dispatch"` (envío a cliente) o `"loss"` (discrepancia o daño confirmado) |
| `tracking_number` | `str \| None` | Número de seguimiento del transportista si `exit_type = "dispatch"`. Nulo para pérdidas. |
| `warehouse` | `str` | `"LA"` o `"ZGZ"` |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del coordinador logístico que autorizó la salida (de TinyDB) |

---

## Router de la API

Todos los endpoints deben registrarse bajo el prefijo `/inventory`. El archivo del router se encuentra en `services/routers/inventory.py`.

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/inventory/products` | Lista todos los SKUs con `current_stock` |
| `POST` | `/inventory/products` | Registra un nuevo SKU |
| `GET` | `/inventory/products/{id}` | Obtiene un SKU con su stock actual |
| `POST` | `/inventory/orders/inbound` | Registra una recepción de mercancía (`StockEntry`) |
| `POST` | `/inventory/orders/outbound` | Registra un despacho o pérdida (`StockExit`) |
| `GET` | `/inventory/orders` | Lista todos los movimientos de stock con datos del SKU |

---

## Reglas de Negocio

1. **`current_stock` siempre se calcula**, nunca se almacena. Para cualquier SKU: `current_stock = SUMA(StockEntry.quantity) − SUMA(StockExit.quantity)`.
2. **No se puede registrar un `StockExit` si la cantidad llevaría el stock por debajo de cero.** Devuelve `HTTP 400` con el mensaje: `"Insufficient stock for SKU '{sku}'. Available: {available}, requested: {quantity}."`. Rechazar antes de escribir.
3. **`tracking_number` es obligatorio cuando `exit_type = "dispatch"` y debe ser nulo cuando `exit_type = "loss"`**. Validar en el schema o en la lógica de la ruta.
4. **Sin tabla de usuarios en Supabase.** Los campos `user_uuid` referencian usuarios de TinyDB. No crear un modelo User en SQLModel.
5. **Los almacenes de Los Ángeles y Zaragoza coexisten en las mismas tablas.** El campo `warehouse` (`"LA"` o `"ZGZ"`) debe estar presente tanto en los registros de SKU como en los de movimientos.
6. **El stock es por SKU y por almacén**, no agregado globalmente. Un SKU con 20 unidades en LA y 15 en ZGZ tiene dos cifras de stock separadas — no 35.

> ⚠️ La regla 6 cambia el cálculo de `current_stock`: filtra los movimientos por `warehouse` al calcular el stock para una ubicación concreta. Al listar todos los SKUs, puedes mostrar el stock total o el desglose por almacén — documenta tu elección.

---

## Datos Semilla

Crea los siguientes registros al configurar tu base de datos de desarrollo local.

### SKUs (mínimo 6)

| name | sku | client_name | category | warehouse |
|------|-----|-------------|----------|-----------|
| Zapatilla blanca clásica - Talla 42 | CLT-SNK-W-42 | PureStep Footwear | fashion | LA |
| Zapatilla blanca clásica - Talla 42 | CLT-SNK-W-42-Z | PureStep Footwear | fashion | ZGZ |
| Auriculares inalámbricos Pro | TEC-EAR-001 | SoundWave Electronics | electronics | LA |
| Sérum facial hidratante 30ml | CSM-SRM-030 | GlowLab Cosmetics | cosmetics | ZGZ |
| Chino slim fit - marino 32/32 | CLT-CHN-N-32 | UrbanThread | fashion | LA |
| Cargador rápido USB-C 65W | TEC-CHG-065 | SoundWave Electronics | electronics | ZGZ |

### StockEntries (mínimo 4)

Registra al menos 2 recepciones del mismo SKU con cantidades diferentes. Usa códigos de referencia realistas como `"PO-2024-0098"`, `"GR-LA-0234"`. Mezcla ambos almacenes.

### StockExits (mínimo 3)

Incluye al menos un `"dispatch"` (con un `tracking_number` como `"1Z999AA10123456784"`) y una `"loss"` (con `tracking_number` como nulo). Las cantidades no deben superar las entradas sembradas para el mismo almacén.

---

## Estructura de Archivos (dentro de `services/`)

```
services/
├── main.py
├── database.py          # Cliente TinyDB + motor SQLModel + dependencia get_db
├── models.py            # SKU, StockEntry, StockExit (SQLModel)
├── schemas.py           # Schemas Pydantic de request/response
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Notas de Evaluación para TrackFlow

- El evaluador registrará un `StockExit` que supere el stock del almacén y esperará `HTTP 400`.
- El evaluador intentará una salida de tipo `"dispatch"` sin `tracking_number` y esperará un error de validación.
- El evaluador verificará que las cifras de stock son por almacén, no agregadas.
- El campo `warehouse` debe estar presente en los modelos SKU, StockEntry y StockExit y en sus schemas de respuesta.

---

_Documento interno — 4Geeks Academy · Track de Ingeniería de IA_
_Hito 5 · Escenario TrackFlow_
