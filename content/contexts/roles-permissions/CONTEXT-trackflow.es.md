# CONTEXT — Roles y Permisos · TrackFlow

_These instructions are also available in [English](./CONTEXT-trackflow.en.md)._

> **Proyecto:** Plataforma – Roles y Permisos  
> **Ruta en el repositorio:** `content/contexts/roles-permissions/CONTEXT-trackflow.es.md`

---

## Tu empresa

Eres parte de **TrackFlow Tech**. TrackFlow es una empresa de last-mile y almacén (~130 personas) con sedes en Los Ángeles y Zaragoza. El CTO **Andrés Kim** abrió este ticket después de que Legal señalara que cualquier usuario autenticado tiene hoy el mismo acceso — las notas de almacén no deben filtrarse a cuentas comerciales.

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

| `code`                 | Nombre visible                    | Director / responsable | Datos que pertenecen a este departamento                                                              |
| ---------------------- | --------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `warehouse_operations` | Operaciones de almacén            | Ana Whitfield          | Notas de discrepancias de inventario, reportes de inbound/picking                                     |
| `last_mile`            | Last mile y gestión de carriers   | Carlos Vega            | Notas de desempeño de carriers, reportes de entregas fallidas                                         |
| `reverse_logistics`    | Logística inversa                 | Sofía Ramos            | Notas de aprobación de devoluciones, reportes de inspección                                           |
| `customer_experience`  | Experiencia de cliente            | Valentina Cruz         | Notas de volumen de consultas, reportes de ops de agentes                                             |
| `commercial`           | Comercial y relación con clientes | Miguel Torres          | Notas de salud de cuenta, reportes de renovación                                                      |
| `technology`           | Tecnología                        | Andrés Kim             | Notas de configuración de plataforma (sigue siendo de alcance departamental para Empleado/Supervisor) |

Un Supervisor de Almacén y un Supervisor Comercial tienen **las mismas capacidades de Supervisor**. No deben ver los registros departamentales del otro.

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
    {"code": "warehouse_operations", "name": "Warehouse Operations"},
    {"code": "last_mile", "name": "Last Mile and Carrier Management"},
    {"code": "reverse_logistics", "name": "Reverse Logistics"},
    {"code": "customer_experience", "name": "Customer Experience"},
    {"code": "commercial", "name": "Commercial and Client Relations"},
    {"code": "technology", "name": "Technology"},
]
```

### Usuarios (rol y departamento independientes)

```python
USERS_SEED = [
    {
        "email": "ana.warehouse@trackflow.example",
        "role": "supervisor",
        "department": "warehouse_operations",
        "name": "Ana Whitfield",
    },
    {
        "email": "miguel.commercial@trackflow.example",
        "role": "supervisor",
        "department": "commercial",
        "name": "Miguel Torres",
    },
    {
        "email": "carlos.carriers@trackflow.example",
        "role": "employee",
        "department": "last_mile",
        "name": "Carlos Vega",
    },
    {
        "email": "sofia.returns@trackflow.example",
        "role": "employee",
        "department": "reverse_logistics",
        "name": "Sofía Ramos",
    },
    {
        "email": "andres.admin@trackflow.example",
        "role": "admin",
        "department": "technology",
        "name": "Andrés Kim",
    },
]
```

Ana y Miguel son el par **mismo rol / distinto departamento** usado en la evaluación.

### Reportes internos (mínimo)

Siembra al menos un reporte en `warehouse_operations` y uno en `commercial` para poder probar el par anterior.

```python
INTERNAL_REPORTS_SEED = [
    {
        "department": "warehouse_operations",
        "title": "Zaragoza — cycle count variance",
        "body": "SKU TF-1044 variance of 37 units after Friday count. Client not notified yet.",
    },
    {
        "department": "commercial",
        "title": "Account Northwind — renewal risk",
        "body": "On-time delivery below contracted 96%. QBR scheduled. No warehouse internals in this note.",
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
3. Ana (`supervisor` + `warehouse_operations`) hace `GET` del reporte comercial de Miguel por id → **403**.
4. Cambiar el departamento de Miguel a `customer_experience` **no** cambia su rol; cambiar el rol de Ana a `employee` **no** cambia su departamento.
5. La verificación de permisos vive en una dependencia/middleware — no copiada en el cuerpo de cada ruta.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
