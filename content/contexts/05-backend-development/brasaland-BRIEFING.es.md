# BRIEFING — Hito 5: Gestión de Inventario Backend
## Empresa: Brasaland

**Ruta:** `05-backend-inventory-orm/brasaland-BRIEFING.es.md`

---

## Tu Empresa

**Brasaland** es una cadena de restaurantes de cocina a la brasa con 14 locales repartidos entre Colombia y Florida. La empresa procesa cientos de órdenes de ingredientes cada semana: carne, verduras, salsas, bebidas, envases y productos de limpieza llegan de unos 20 proveedores en ambos países, y esos mismos ingredientes salen de cada cocina cada día durante la preparación y — inevitablemente — en forma de merma.

Hasta ahora, el stock de ingredientes en cada local lo ha gestionado el encargado local por WhatsApp y hojas de cálculo. **Nicolás Park (CTO)** ha asignado a tu equipo la construcción de la capa centralizada de gestión de inventario de la plataforma Brasaland Digital. Es la primera vez que Brasaland tendrá una única fuente de verdad sobre qué hay en stock en toda la cadena.

> **De Nicolás (CTO) — Ticket Notion #BRD-0512:**
> "El equipo de operaciones está ciego con los ingredientes. Los supervisores de Felipe no saben cuánta carne hay disponible en Miami hasta que llaman a la cocina. Construid la API de inventario. Las entradas de ingredientes vienen de entregas de proveedores; las salidas vienen de registros de consumo e informes de merma. El stock debe ser de solo lectura — siempre es el neto de lo que llegó menos lo que se usó. Todos los endpoints bajo `/inventory`. Consultad la especificación de entidades a continuación."

---

## Nombres de Entidades y Especificación de Campos

Usa estos nombres exactamente en tus modelos, schemas y respuestas de la API.

### `Ingredient` (equivale a `Product` del README)

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `name` | `str` | Ej.: `"Falda de ternera"`, `"Salsa de la casa"`, `"Caja para llevar (M)"` |
| `sku` | `str` | Código interno único, ej.: `"BRS-BEEF-001"` |
| `unit` | `str` | Unidad de medida: `"kg"`, `"litro"`, `"unidad"` |
| `category` | `str` | `"meat"`, `"produce"`, `"sauce"`, `"beverage"`, `"packaging"`, `"cleaning"` |
| `country` | `str` | `"CO"` (Colombia) o `"US"` (Estados Unidos) |
| `current_stock` | `float` | **Campo calculado — no almacenado.** Siempre se deriva de las órdenes. Incluir solo en el schema de respuesta. |

### `IngredientEntry` (equivale a `InboundOrder` del README)

Una entrega de ingredientes recibida de un proveedor.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `ingredient_id` | `int` (FK → Ingredient) | |
| `quantity` | `float` | Cantidad recibida en la unidad del ingrediente |
| `supplier_name` | `str` | Nombre del proveedor de esta entrega |
| `location_id` | `int` | Local receptor (1–14). No es FK — los datos de locales se gestionan por separado. |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del supervisor de operaciones que registró la entrega (de TinyDB) |

### `IngredientExit` (equivale a `OutboundOrder` del README)

Un registro de consumo de ingredientes o informe de merma.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `ingredient_id` | `int` (FK → Ingredient) | |
| `quantity` | `float` | Cantidad consumida o mermada |
| `reason` | `str` | `"consumption"` (consumo) o `"waste"` (merma) |
| `location_id` | `int` | Local donde ocurrió la salida |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del miembro del personal que registró la salida (de TinyDB) |

---

## Router de la API

Todos los endpoints deben registrarse bajo el prefijo `/inventory`. El archivo del router se encuentra en `services/routers/inventory.py`.

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/inventory/products` | Lista todos los ingredientes con `current_stock` |
| `POST` | `/inventory/products` | Crea un nuevo ingrediente |
| `GET` | `/inventory/products/{id}` | Obtiene un ingrediente con su stock actual |
| `POST` | `/inventory/orders/inbound` | Registra una entrega de proveedor (`IngredientEntry`) |
| `POST` | `/inventory/orders/outbound` | Registra un consumo o merma (`IngredientExit`) |
| `GET` | `/inventory/orders` | Lista todas las entradas y salidas con datos del ingrediente |

---

## Reglas de Negocio

1. **`current_stock` siempre se calcula**, nunca se almacena. Para cualquier ingrediente: `current_stock = SUMA(IngredientEntry.quantity) − SUMA(IngredientExit.quantity)`.
2. **No se puede registrar una salida si resultaría en stock negativo.** Devuelve `HTTP 400` con el mensaje: `"Insufficient stock for ingredient '{name}'. Available: {available}, requested: {requested}."`. Rechazar antes de escribir.
3. **Los ingredientes de Colombia y EE.UU. coexisten en la misma tabla.** Usa el campo `country` para filtrar por mercado cuando sea necesario.
4. **Sin tabla de usuarios en Supabase.** Los campos `user_uuid` referencian usuarios de TinyDB. No crear un modelo User en SQLModel.
5. **Los IDs de locales van del 1 al 14.** No son claves foráneas en este hito — almacenar solo el entero.

---

## Datos Semilla

Crea los siguientes registros al configurar tu base de datos de desarrollo local. Deben estar presentes antes de tu demo.

### Ingredients (mínimo 6)

| name | sku | unit | category | country |
|------|-----|------|----------|---------|
| Falda de ternera | BRS-BEEF-001 | kg | meat | CO |
| Costilla de cerdo | BRS-PORK-001 | kg | meat | US |
| Chimichurri | BRS-SAUCE-001 | litro | sauce | CO |
| Salsa BBQ de la casa | BRS-SAUCE-002 | litro | sauce | US |
| Yuca | BRS-PROD-001 | kg | produce | CO |
| Caja para llevar (M) | BRS-PKG-001 | unidad | packaging | CO |

### IngredientEntries (mínimo 4)

Registra al menos 2 entregas para `BRS-BEEF-001` (p. ej., 50 kg y 30 kg) y 1 entrega para cada uno de otros dos ingredientes. Usa nombres de proveedor realistas: `"Carnes del Valle S.A."`, `"MiamiMeat Co."`, `"Salsas Artesanales Ltda."`.

### IngredientExits (mínimo 3)

Registra salidas de consumo que reduzcan el stock sin llegar a cero. Incluye al menos una salida de tipo `"waste"`. Usa valores de `user_uuid` que correspondan a usuarios existentes en tu instancia TinyDB.

---

## Estructura de Archivos (dentro de `services/`)

```
services/
├── main.py
├── database.py          # Cliente TinyDB + motor SQLModel + dependencia get_db
├── models.py            # Ingredient, IngredientEntry, IngredientExit (SQLModel)
├── schemas.py           # Schemas Pydantic de request/response
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Notas de Evaluación para Brasaland

- El evaluador creará un `IngredientExit` que supere el stock disponible y esperará `HTTP 400`.
- El evaluador llamará a `GET /inventory/products` y verificará que `current_stock` refleja el neto de las entradas y salidas sembradas.
- El campo `country` debe aparecer tanto en el modelo como en el schema de respuesta.
- El campo `reason` en `IngredientExit` solo debe aceptar `"consumption"` o `"waste"`.

---

_Documento interno — 4Geeks Academy · Track de Ingeniería de IA_
_Hito 5 · Escenario Brasaland_
