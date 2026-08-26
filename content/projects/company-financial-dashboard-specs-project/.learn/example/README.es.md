# Ejemplo en Clase: Desarrollo Guiado por Especificaciones para el Catálogo de Biblioteca

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio continúa con la app de catálogo de biblioteca comunitaria del **proyecto de contexto** — mismo flujo agent-first guiado por especificaciones (explorar `/docs`, tipos TypeScript, specs de componentes, documentación del contrato de datos, casos límite), pero con dos funcionalidades en lugar de tres y una forma de API más sencilla.

_These instructions are also available in [English](./README.md)._

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo flujo agent-first y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Continúas en el **repo heredado del catálogo de biblioteca** del proyecto de contexto. Los bibliotecarios quieren dos funcionalidades nuevas. Antes de que nadie escriba un componente React, tu tech lead dice: **"Primero especificamos. Luego construimos."**

Tu coding agent explora `/docs`; tú verificas tipos y reglas contra evidencia de la API en vivo. Las specs deben ser lo bastante claras para que cualquier coding agent implemente sin preguntas de seguimiento.

---

## Conceptos Cubiertos

| Concepto                                   | Dónde se aplica                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------- |
| Exploración agent-first de la API          | Fase 1: mapear endpoints y formas desde `/docs` con el agent              |
| Interfaces TypeScript                      | `api-types.ts` — formas de respuesta verificadas contra OpenAPI           |
| Tipos de parámetros de consulta TypeScript | `param-types.ts` — parámetros de petición con JSDoc                       |
| Especificación de componentes              | `components.md` — nombres, props, renderizado condicional, estados vacíos |
| Documentación del contrato de datos        | `frontend/specs/README.md` — endpoints, tipos, casos límite               |
| Desarrollo guiado por especificaciones     | Especificar antes de construir para que la implementación sea inequívoca  |

---

## Punto de Partida

Continúa en el mismo proyecto local de ejemplo del proyecto de contexto. Confirma que existen `memory-bank/` y `.agents/rules`.

Crea una nueva rama:

```bash
git switch -c feature/frontend-specs
mkdir -p frontend/specs
```

Pide al agent que arranque el backend y explore `/docs` antes de escribir nada.

---

## Peticiones de Funcionalidades

> #### Funcionalidad 1 — Filtro de búsqueda por título
>
> Los bibliotecarios quieren filtrar la lista de libros por título parcial. Añade un input de texto en la parte superior de la página del catálogo que filtre los libros mostrados en tiempo real. La búsqueda no distingue mayúsculas de minúsculas. Cuando el input está vacío, se muestran todos los libros. Cuando no hay libros que coincidan, muestra un mensaje explícito "No se encontraron libros" — no una cuadrícula vacía.
>
> Endpoint relevante: `GET /api/books?title=<string>`
>
> ---
>
> #### Funcionalidad 2 — Panel de desglose por género
>
> Bajo la lista de libros, añade un panel que muestre los 3 principales géneros del catálogo con su número de libros y porcentaje del total de la colección. El panel tiene una tabla compacta: nombre del género, número de libros y porcentaje. Se actualiza automáticamente cuando el filtro de título de la Funcionalidad 1 está activo (es decir, muestra las estadísticas de géneros para el subconjunto filtrado, no para todo el catálogo). Si el resultado filtrado tiene menos de 3 géneros, muestra solo los disponibles con una nota explícita.
>
> Endpoint relevante: `GET /api/books/genres/summary`

---

## Qué Producir

### Fase 1 — Explorar `/docs` (con el agent)

- [ ] Mapear endpoints, formas de respuesta y parámetros de ambas funcionalidades
- [ ] Anotar desajustes entre el wording del PM y los campos reales de la API

### Fase 2 — Tipos TypeScript (el agent redacta, tú verificas)

**`frontend/specs/api-types.ts`**

- [ ] `BookEntry`, `BooksResponse`, `GenreEntry`, `GenresSummaryResponse`
- [ ] Sin `any`, sin `object`; JSDoc en cada propiedad; verificar contra `/docs`

**`frontend/specs/param-types.ts`**

- [ ] `BookSearchParams`, `GenresSummaryParams`

### Fase 3 — Specs de componentes (el agent redacta, tú verificas)

**`frontend/specs/components.md`** — por funcionalidad: nombres, props, layout, estados vacíos, interacción del filtro entre Funcionalidad 1 y 2.

### Fase 4 — Contrato de datos

**`frontend/specs/README.md`** — endpoints, tipos, restricciones de parámetros, ≥ 2 casos límite por funcionalidad con comportamiento de UI.

> ⚠️ **Importante:** No construyas componentes React ni hagas llamadas a la API. Entregables: archivos `.ts` de tipos, `components.md` y `frontend/specs/README.md`.

---

## Preguntas para Discusión

1. ¿Por qué verificar interfaces TypeScript contra `/docs` en lugar de inferir la forma desde las necesidades del componente?
2. El panel de géneros muestra estadísticas del subconjunto filtrado cuando hay filtro de título activo. ¿Qué caso límite crea?
3. Un compañero dice: "¿Para qué molestarse con `components.md`? Con los tipos basta." ¿Cuál es el contraargumento?
4. ¿Quién debe descubrir los nombres de campo de la API — el estudiante de memoria, o el estudiante+agent desde `/docs`?
