# CONTEXT — Roles y Permisos · Brasaland

_These instructions are also available in [English](./CONTEXT-brasaland.en.md)._

> **Proyecto:** Plataforma – Roles y Permisos  
> **Ruta en el repositorio:** `content/contexts/roles-permissions/CONTEXT-brasaland.es.md`

---

## Tu empresa

Eres parte de **Brasaland Digital**. Brasaland es una cadena de restaurantes de comida a la brasa con **14 locales** en Colombia y Florida (~115 personas). El CTO **Nicolás Park** abrió este ticket después de que Legal señalara que cualquier usuario autenticado tiene hoy el mismo acceso.

Usa este archivo como fuente de verdad para **nombres de roles**, **departamentos**, **reglas de capacidad** y **usuarios semilla**. Un RBAC genérico que ignore estos valores no será aceptado.

---

## Roles (eje de capacidad)

El rol responde _"¿qué puede hacer esta persona?"_ — no qué datos ve. Persístelos como entidad propia. **No** lo reduzcas a `is_admin`.

| `code`       | Nombre visible | Rango | Capacidades                                                                                                                                                                                                                                 |
| ------------ | -------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `employee`   | Empleado       | 1     | Crear y leer registros de **su departamento**. No puede aprobar, eliminar ni administrar usuarios/roles/departamentos.                                                                                                                      |
| `supervisor` | Supervisor     | 2     | Todo lo de Empleado, más actualizar/aprobar registros de **su departamento**. No puede eliminar, no administra usuarios/roles/departamentos, no ve otros departamentos.                                                                     |
| `admin`      | Admin          | 3     | Todo lo de Supervisor, más eliminar registros, administrar usuarios y administrar roles y departamentos. **La visibilidad cruzada entre departamentos es una capacidad de Admin** — no significa que el Admin haya perdido su departamento. |

El rango es estrictamente jerárquico: `employee` < `supervisor` < `admin`. Cambiar el departamento de un usuario no debe cambiar este rango.

---

## Departamentos (eje de alcance de datos)

El departamento responde _"¿qué información le compete a esta persona?"_ **No** otorga acciones extra. Persístelos como entidad propia, independiente del rol.

| `code`                  | Nombre visible                    | Director / responsable | Datos que pertenecen a este departamento                                                              |
| ----------------------- | --------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `restaurant_operations` | Operaciones de restaurante        | Felipe Guerrero        | Incidentes de local, reportes de turno, notas operativas de cocina/sala                               |
| `procurement`           | Compras y proveedores             | Lucía Fernández        | Proveedores, tarifas, notas de compra                                                                 |
| `marketing`             | Marketing y experiencia digital   | Camila Ospina          | Campañas, loyalty, notas de cara al cliente                                                           |
| `people_culture`        | Personas y cultura                | Ashley Turner          | Notas de plantilla, turnos, onboarding                                                                |
| `training_quality`      | Formación y estándares de calidad | Jake Morrison          | Recetas, materiales de formación, notas de calidad                                                    |
| `technology`            | Tecnología                        | Nicolás Park           | Notas de configuración de plataforma (sigue siendo de alcance departamental para Empleado/Supervisor) |

Un Supervisor de Operaciones y un Supervisor de Compras tienen **las mismas capacidades de Supervisor**. No deben ver los registros departamentales del otro.

---

## Regla de independencia

- `User.role_id` y `User.department_id` son claves foráneas separadas (o equivalente). Ninguna se deriva de la otra.
- Un `PATCH` (o equivalente) que cambie solo el rol debe dejar el departamento intacto.
- Un `PATCH` que cambie solo el departamento debe dejar el rol intacto.
- Los usuarios Admin **siguen perteneciendo** a un departamento (`technology` en la semilla). La lectura/escritura cruzada es un privilegio de **rol**, no un departamento vacío.

---

## Matriz de acceso a recursos

Aplica **primero el rol**, después el **departamento**. Rol insuficiente → **403** con cuerpo explícito. Nunca devuelvas `200` con datos vacíos o silenciados para ocultar una capacidad que falta.

Un `GET` directo del registro de otro departamento por id → **403** (Empleado/Supervisor). Los listados de colecciones con alcance departamental pueden devolver solo el departamento del llamante — eso es alcance, no una denegación silenciosa.

| Recurso                                                       | Rol mínimo                                                                                                  | ¿Alcance departamental?                   | Notas                                                         |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------- |
| `GET /auth/me`                                                | autenticado                                                                                                 | no                                        | Devuelve rol **y** departamento                               |
| `GET/POST /users` (crear/listar)                              | `admin`                                                                                                     | no                                        | Administración de usuarios                                    |
| `PATCH /users/{id}/assignment`                                | `admin`                                                                                                     | no                                        | Cambiar `role_id` y/o `department_id` de forma independiente  |
| `GET/POST /roles`, `GET/PUT /roles/{id}`                      | `admin`                                                                                                     | no                                        | Administración de roles                                       |
| `GET/POST /departments`, `GET/PUT /departments/{id}`          | `admin`                                                                                                     | no                                        | Administración de departamentos                               |
| Endpoints de escritura existentes que mutan datos de negocio  | `supervisor` (actualizar/aprobar), `admin` (eliminar)                                                       | sí, cuando el registro tiene departamento | Mapea inventario/proveedores/incidentes actuales a esta regla |
| `GET/POST /internal-reports` (colección canónica con alcance) | `employee` (leer/crear su depto), `supervisor` (actualizar su depto), `admin` (todos los deptos + eliminar) | **sí**                                    | Obligatorio aunque otros módulos estén incompletos            |

### Colección canónica con alcance departamental: `internal-reports`

Si tu monorepo aún no tiene una entidad limpia con alcance departamental, implementa esta. Si ya tienes incidentes/inventario/proveedores, **también** etiquétalos con `department_id` y aplica la misma regla.

| Campo           | Tipo            | Reglas         |
| --------------- | --------------- | -------------- |
| `id`            | string/uuid     | clave primaria |
| `department_id` | FK → Department | requerido      |
| `title`         | string          | requerido      |
| `body`          | string          | requerido      |
| `created_by`    | FK → User       | requerido      |
| `created_at`    | datetime        | sistema        |

---

## Datos semilla

Siembra **exactamente** estos roles, departamentos y usuarios (más los extras que necesites para demo local). Las contraseñas pueden ser un hash de desarrollo compartido; los emails deben coincidir.

### Roles

```python
ROLES_SEED = [
    {"code": "employee", "name": "Employee", "rank": 1},
    {"code": "supervisor", "name": "Supervisor", "rank": 2},
    {"code": "admin", "name": "Admin", "rank": 3},
]
```

### Departamentos

```python
DEPARTMENTS_SEED = [
    {"code": "restaurant_operations", "name": "Restaurant Operations"},
    {"code": "procurement", "name": "Procurement and Suppliers"},
    {"code": "marketing", "name": "Marketing and Digital Experience"},
    {"code": "people_culture", "name": "People and Culture"},
    {"code": "training_quality", "name": "Training and Quality Standards"},
    {"code": "technology", "name": "Technology"},
]
```

### Usuarios (rol y departamento independientes)

```python
USERS_SEED = [
    {
        "email": "felipe.ops@brasaland.example",
        "role": "supervisor",
        "department": "restaurant_operations",
        "name": "Felipe Guerrero",
    },
    {
        "email": "lucia.procurement@brasaland.example",
        "role": "supervisor",
        "department": "procurement",
        "name": "Lucía Fernández",
    },
    {
        "email": "camila.marketing@brasaland.example",
        "role": "employee",
        "department": "marketing",
        "name": "Camila Ospina",
    },
    {
        "email": "jake.training@brasaland.example",
        "role": "employee",
        "department": "training_quality",
        "name": "Jake Morrison",
    },
    {
        "email": "nicolas.admin@brasaland.example",
        "role": "admin",
        "department": "technology",
        "name": "Nicolás Park",
    },
]
```

Felipe y Lucía son el par **mismo rol / distinto departamento** usado en la evaluación.

### Reportes internos (mínimo)

Siembra al menos un reporte en `restaurant_operations` y uno en `procurement` para poder probar el par anterior.

```python
INTERNAL_REPORTS_SEED = [
    {
        "department": "restaurant_operations",
        "title": "Medellín Centro — Friday stockout",
        "body": "Ribeye 86% depleted before close. Shift report attached.",
    },
    {
        "department": "procurement",
        "title": "Carnes del Valle rate change",
        "body": "Supplier proposed +8% on beef for Q4. Pending Lucía approval.",
    },
]
```

---

## Frontend / backoffice

- Oculta o deshabilita las acciones de crear/aprobar/eliminar que el rol actual no permite.
- Los listados de datos departamentales muestran **solo** el departamento del usuario autenticado (Admin ve todos).
- Vista solo Admin: listar/crear/editar **roles** y **departamentos**, y asignarlos a usuarios **de forma independiente**. Empleado y Supervisor que abran esa ruta (o llamen a la API) reciben **403**.

---

## Pruebas que pedirá Legal

1. Empleado llamando a un update solo de Supervisor → **403**.
2. Supervisor llamando a `GET /roles` o asignación de usuario solo Admin → **403**.
3. Felipe (`supervisor` + `restaurant_operations`) hace `GET` del reporte de compras de Lucía por id → **403**.
4. Cambiar el departamento de Lucía a `marketing` **no** cambia su rol; cambiar el rol de Felipe a `employee` **no** cambia su departamento.
5. La verificación de permisos vive en una dependencia/middleware — no copiada en el cuerpo de cada ruta.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
