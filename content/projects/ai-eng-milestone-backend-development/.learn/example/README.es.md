# Ejemplo en Clase — Despensa del Carrito de Café del Campus (FastAPI + SQLModel + Doble BD)

> **Nota para el instructor:** Ejemplo en ritmo de aula, paralelo a `ai-eng-milestone-backend-development`. Mismo stack y patrones (auth TinyDB + inventario Supabase + ORM SQLModel + stock calculado), dominio distinto para que los estudiantes no lo confundan con el trabajo en el monorepo de su empresa. Objetivo: una sesión en vivo de 60–90 minutos.

_These instructions are also available in [English](./README.md)._

---

## El reto

Un carrito de café del campus lleva el control de suministros en una pizarra: granos, vasos, tapas. El equipo estudiantil necesita una API interna mínima para registrar **reposiciones** (entrega del proveedor) y **retiros de uso** (consumo al cierre del turno) sin editar cantidades a mano.

Regla no negociable del responsable del carrito:

> _"Nadie edita el stock directamente. La reposición suma unidades; el uso las resta. Cada movimiento debe registrar qué voluntario lo registró."_

Construye esto sobre el **mismo servicio FastAPI** que los estudiantes ya usan para autenticación — extiéndelo, no abras un repo nuevo.

### Nota de alcance

| Se mantiene (mismo eje que el proyecto evaluado)      | Simplificado para clase                                            |
| ----------------------------------------------------- | ------------------------------------------------------------------ |
| Conexión dual TinyDB + Supabase                       | Sin CONTEXT.md — `Product` genérico (`id`, `name`, `sku`)          |
| Modelos SQLModel + schemas Pydantic separados         | Sin campos específicos de empresa (`warehouse`, `exit_type`, etc.) |
| Router `/inventory` con los 6 endpoints               | Sin script de datos semilla obligatorio en clase                   |
| `current_stock` calculado desde órdenes               | Una sola ubicación — sin stock por almacén                         |
| Auth en endpoints de creación; `user_uuid` en órdenes | Reutilizar `get_current_user` del hito anterior                    |
| `400` antes de persistir si stock insuficiente        | —                                                                  |

Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

---

## Stack tecnológico

| Capa                  | Herramienta                    |
| --------------------- | ------------------------------ |
| API                   | FastAPI                        |
| Almacén de auth       | TinyDB (existente)             |
| Almacén de inventario | Supabase / PostgreSQL          |
| ORM                   | SQLModel                       |
| Sesión                | `Depends(get_db)` por petición |

---

## Estructura sugerida (`services/`)

```text
services/
├── main.py
├── database.py          # TinyDB + motor SQLModel + get_db
├── models.py            # Product, InboundOrder, OutboundOrder
├── schemas.py           # Request/response Pydantic (archivo separado)
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Modelo de datos (solo ejemplo de clase)

### `Product`

| Campo  | Tipo     | Notas                      |
| ------ | -------- | -------------------------- |
| `id`   | int (PK) | Auto-incremento            |
| `name` | str      | ej. `"Granos Arábica 1kg"` |
| `sku`  | str      | ej. `"BEAN-AR-1K"`         |

`current_stock` aparece **solo** en schemas de respuesta — nunca como columna en BD.

### `InboundOrder` (reposición)

| Campo        | Tipo               | Notas                                                    |
| ------------ | ------------------ | -------------------------------------------------------- |
| `id`         | int (PK)           |                                                          |
| `product_id` | int (FK → Product) |                                                          |
| `quantity`   | int                | Unidades recibidas                                       |
| `created_at` | datetime           | Auto-asignado                                            |
| `user_uuid`  | str                | Voluntario de TinyDB — sin tabla de usuarios en Supabase |

### `OutboundOrder` (uso)

Misma forma que inbound; representa unidades consumidas en un turno.

---

## Qué construir

### Configuración de bases de datos

- [ ] Añadir `DATABASE_URL` a `.env` con el URI de **Transaction pooler** de Supabase (**Connect → Direct** → Transaction pooler → URI). Mantener variables TinyDB existentes.
- [ ] En `database.py`, exponer cliente TinyDB y `engine` SQLModel.
- [ ] Implementar generador `get_db()`; inyectar con `Depends()` — sin sesión global.

### ORM + schemas

- [ ] `models.py`: `Product`, `InboundOrder`, `OutboundOrder` con `SQLModel, table=True` y FK en `product_id`.
- [ ] `schemas.py`: schemas create/read separados; `ProductRead` incluye `current_stock` calculado.
- [ ] Llamar `SQLModel.metadata.create_all(engine)` al arrancar.

### Router de inventario (`/inventory`)

| Método | Ruta                         | Auth | Acción                                                     |
| ------ | ---------------------------- | ---- | ---------------------------------------------------------- |
| `GET`  | `/inventory/products`        | —    | Listar productos + `current_stock`                         |
| `POST` | `/inventory/products`        | ✓    | Crear producto (empieza en stock 0)                        |
| `GET`  | `/inventory/products/{id}`   | —    | Un producto + stock                                        |
| `POST` | `/inventory/orders/inbound`  | ✓    | Registrar reposición                                       |
| `POST` | `/inventory/orders/outbound` | ✓    | Registrar uso                                              |
| `GET`  | `/inventory/orders`          | —    | Todos los movimientos con nombre de producto + `user_uuid` |

### Reglas de negocio (demostrar en vivo)

- [ ] `current_stock = SUMA(cant. inbound) − SUMA(cant. outbound)` por producto.
- [ ] Guardar UUID del usuario autenticado en `user_uuid` al crear órdenes.
- [ ] Rechazar outbound si el stock quedaría negativo → `HTTP 400` **antes** de `session.commit()`.
- [ ] Los endpoints devuelven schemas Pydantic, nunca instancias SQLModel crudas.

### Datos mínimos para demo en vivo (opcional)

| name                | sku        |
| ------------------- | ---------- |
| Granos Arábica 1kg  | BEAN-AR-1K |
| Vasos de Papel 12oz | CUP-12-P   |

Recorrido: crear producto → inbound 50 granos → outbound 12 → outbound 40 (debe devolver 400).

---

## Conceptos clave a trabajar en clase

| Concepto                  | Dónde aparece                                                 |
| ------------------------- | ------------------------------------------------------------- |
| Enrutado dual de BD       | TinyDB en dep de auth; SQLModel en rutas de inventario        |
| Separación ORM vs schema  | `models.py` vs `schemas.py`                                   |
| Estado derivado           | `current_stock` calculado, no almacenado                      |
| FK sin replicar usuarios  | `user_uuid` como string, sin tabla users en Supabase          |
| Guardia antes de escribir | Validación de stock en outbound                               |
| Conciencia N+1            | Mencionar al listar órdenes — cargar productos de forma eager |

---

## Verificar juntos

- [ ] `GET /inventory/products` muestra `current_stock: 0` en producto nuevo.
- [ ] Tras inbound 50, el stock muestra 50 sin columna de stock en BD.
- [ ] Outbound 60 devuelve `400`; en BD siguen 50 disponibles.
- [ ] `GET /inventory/orders` lista movimientos con `user_uuid` rellenado.
- [ ] `/docs` muestra todas las rutas bajo `/inventory`.

---

## Preguntas para debate

1. ¿Por qué mantener usuarios en TinyDB en lugar de copiar una tabla `users` en Supabase? ¿Qué se rompe si duplicamos filas de usuario?
2. ¿Dónde debe vivir el cálculo de stock — inline en la ruta, función de servicio, o agregado SQL? ¿Qué implica para las pruebas?
3. Si `GET /inventory/orders` carga 20 órdenes y obtiene cada producto en un bucle, ¿qué pasa con el rendimiento? ¿Cómo lo arreglarías en una sola consulta?
