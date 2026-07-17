# Biblioteca Maple Street — Servidor MCP (Ejemplo de Clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-mcp-company-tools`. Misma columna vertebral (servidor FastMCP, auth OAuth, esquemas de discovery, tool de lectura-escritura + tool de solo lectura, rechazo explícito de escritura, logs de invocación, validación en MCP Playground), distinto alcance que el monorepo de la compañía. Continúa la narrativa de Biblioteca Maple Street de ejemplos previos. Los estudiantes siguen el enunciado completo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

El personal de mostrador de **Biblioteca Maple Street** ya consulta préstamos y catálogo desde un agente pequeño. Cualquier otra integración tendría que reimplementar esas mismas llamadas HTTP.

Tu objetivo en vivo: exponer gestión de préstamos y consulta de catálogo **solo lectura** como un **Servidor MCP** independiente (protegido con OAuth) y validarlo — sin tocar el monorepo completo de la compañía.

### Nota de alcance

| Proyecto evaluable (`ai-eng-mcp-company-tools`) | Este ejemplo de clase                                |
| ----------------------------------------------- | ---------------------------------------------------- |
| Monorepo + Incidents Manager real               | Mini `library-api` con préstamos en memoria o TinyDB |
| Módulo de inventario del Hito 5                 | `catalog.json` pre-cargado (solo lectura)            |
| Migración del agente LangGraph                  | Solo discusión verbal; stretch opcional              |
| Debate stdio vs Streamable HTTP en el PR        | Solo transporte **stdio**                            |
| Cliente MCP en TypeScript                       | Script Python pequeño                                |
| Rúbrica completa                                | Demo local + test de rechazo de escritura            |

---

## Prerrequisitos

- [ ] Python 3.11+ con `uv` (o venv)
- [ ] `fastmcp` instalado: `uv add fastmcp`
- [ ] Opcional: `library-api` de Maple Street de sesiones anteriores — o usa los datos stub de abajo

### Datos semilla (indicativos)

**Préstamos** (almacén mutable):

```json
[
  {
    "loan_id": 1,
    "patron_id": "P-042",
    "book_isbn": "978-0143127550",
    "status": "active"
  }
]
```

**Catálogo** (archivo de solo lectura `data/catalog.json`):

```json
[
  {
    "isbn": "978-0143127550",
    "title": "The Night Circus",
    "copies_available": 2
  }
]
```

---

## Qué construir

### 1. Servidor MCP (`mcp_server/server.py`)

- [ ] App FastMCP con transporte **stdio**
- [ ] Access token OAuth desde env / header Authorization — rechazar listado + invocación sin token válido

### 2. Tool: `manage_book_loan`

- [ ] Acciones: `create`, `update`, `get_status`
- [ ] Esquema de entrada: `loan_id`, `action`, opcional `patron_id`, `book_isbn`, `status`
- [ ] Descripción + esquema de salida claros solo con discovery MCP

| Acción       | Comportamiento                             |
| ------------ | ------------------------------------------ |
| `create`     | Insertar nuevo préstamo                    |
| `update`     | Cambiar `status` (p. ej. `returned`)       |
| `get_status` | Devolver campos del préstamo o `not_found` |

### 3. Tool: `query_catalog` (solo lectura)

- [ ] Búsqueda por `isbn` o listar títulos
- [ ] Si el cliente envía `action: "update"` o cualquier campo de escritura → rechazar explícitamente:

```json
{
  "error_code": "CATALOG_WRITE_FORBIDDEN",
  "message": "Catalog tool is read-only.",
  "tool": "query_catalog"
}
```

### 4. Errores de auth (códigos distintos)

| Escenario                        | Código                    |
| -------------------------------- | ------------------------- |
| Token ausente                    | `AUTH_MISSING_TOKEN`      |
| Token inválido / expirado        | `AUTH_INVALID_TOKEN`      |
| Intento de escritura en catálogo | `CATALOG_WRITE_FORBIDDEN` |
| Input inválido                   | `VALIDATION_ERROR`        |

### 5. Logs de invocación

- [ ] Una línea estructurada por llamada: `client_id`, `tool`, `result`, `duration_ms`

### 6. Cliente MCP (`scripts/mcp_client_demo.py`)

- [ ] Conectar con access token OAuth válido
- [ ] Listar tools — comprobar nombres + descripciones
- [ ] Ejecutar: crear préstamo → consultar estado → consulta catálogo → intento de escritura en catálogo (esperar `CATALOG_WRITE_FORBIDDEN`)

---

## Verificar juntos

- [ ] Servidor arranca; cliente lista dos tools vía discovery
- [ ] Cliente sin token no puede listar tools
- [ ] `manage_book_loan` create + `get_status` devuelve campos esperados
- [ ] `query_catalog` devuelve `copies_available` para ISBN conocido
- [ ] Intento de escritura en catálogo falla con `CATALOG_WRITE_FORBIDDEN` (no error genérico)
- [ ] Terminal muestra al menos un log por tool invocada

---

## Preguntas de discusión

1. ¿Por qué **stdio** basta para un agente local pero no cuando varios equipos remotos necesitan el mismo servidor?
2. ¿Qué diferencia hay entre **omitir** un endpoint de escritura y **rechazar explícitamente** intentos de escritura en la tool de catálogo?
3. Si migraras el agente LangGraph de Maple Street después, ¿qué nodo reemplazarías — y cómo evitarías dos caminos hacia los mismos datos de préstamo?
