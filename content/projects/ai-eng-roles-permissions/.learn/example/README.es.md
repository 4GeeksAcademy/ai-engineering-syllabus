# Taller de makerspace — Roles vs departamentos (ejemplo de clase)

> **Para instructores:** No es el proyecto del estudiante. Demo en vivo de la misma columna vertebral que `ai-eng-roles-permissions`: dos ejes independientes (rol = capacidad, departamento = alcance de datos), una dependencia de permisos en FastAPI, **403** explícito, vista Admin solo para Admin. El dominio es un makerspace de campus para que el alumnado no copie la historia de la empresa.

_These instructions are also available in [English](./README.md)._

---

## El reto

La API de un makerspace de campus trata igual a cualquier miembro autenticado. Legal (el asesor de facultad) pide **dos mecanismos**, no una sola tabla: **rol** (qué puedes hacer) y **taller** (qué herramientas/notas ves). Un Lab Lead de carpintería y un Lab Lead de electrónica tienen los mismos poderes de lead — no deben ver las notas de incidentes del otro.

### Nota de alcance

Una sesión. Tres roles, dos talleres, una colección con alcance (`shop-notes`), `require_role` + `require_shop_scope` centralizados. Se omite el mapeo completo del monorepo, la semilla de 5+ usuarios de empresa y una UI Admin pulida — basta una página Admin o `/docs`. El alumnado sigue el brief completo en el `README.md` de la raíz del proyecto.

---

## Qué construir

### Modelo

- [ ] `Role`: `maker` (rango 1), `lab_lead` (rango 2), `admin` (rango 3)
- [ ] `Shop` (eje departamento): `woodshop`, `electronics` — independiente del rol
- [ ] `User.role_id` y `User.shop_id` como FKs separadas
- [ ] `ShopNote`: `id`, `shop_id`, `title`, `body`

### Checks centralizados

- [ ] Dependencia `require_role(*codes_or_min_rank)` — rol insuficiente → **403**
- [ ] `require_shop_scope` — `GET` de la nota de otro taller por id → **403** (no un 200 vacío)
- [ ] Las rutas declaran dependencias; no copiar `if user.role == ...` en los handlers

### API (mínimo)

| Método   | Ruta                     | Quién                                                  |
| -------- | ------------------------ | ------------------------------------------------------ |
| `GET`    | `/shop-notes`            | maker+: su taller (admin: todos)                       |
| `GET`    | `/shop-notes/{id}`       | su taller o admin; si no, 403                          |
| `PUT`    | `/shop-notes/{id}`       | lab_lead+ su taller; admin cualquiera                  |
| `DELETE` | `/shop-notes/{id}`       | admin                                                  |
| `GET`    | `/roles`                 | solo admin → 403 en caso contrario                     |
| `PATCH`  | `/users/{id}/assignment` | admin; cambiar rol **o** taller de forma independiente |

### UI (delgada)

- [ ] Ocultar delete si no es admin
- [ ] El listado muestra solo las notas del propio taller
- [ ] Admin puede abrir la asignación de roles/talleres (los demás 403)

---

## Verificar juntos

- [ ] Maker hace `PUT` de una nota → **403**
- [ ] Lab lead de carpintería hace `GET` de una nota de electrónica por id → **403**
- [ ] `PATCH` solo de `shop_id` → el rol no cambia
- [ ] `GET /roles` como lab lead → **403**

---

## Preguntas de discusión

1. ¿Por qué devolver `200 []` ante una acción prohibida es peor que un **403** cuando Legal audita la API?
2. Si Admin puede ver todos los talleres, ¿mezclamos los dos ejes — o la visibilidad cruzada es una capacidad de **rol**?
3. ¿Dónde debe vivir la comparación de rango para que un cuarto rol no bifurque cada endpoint?
