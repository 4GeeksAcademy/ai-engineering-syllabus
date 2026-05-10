# Ejemplo en Clase: Desarrollo Guiado por Especificaciones para el Catálogo de Biblioteca

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio continúa con la app de catálogo de biblioteca comunitaria — mismo flujo de trabajo guiado por especificaciones (tipos TypeScript, specs de componentes, documentación del contrato de datos, casos borde), pero con dos funcionalidades en lugar de tres y una forma de API más sencilla.

_These instructions are also available in [English](./README.md)._

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


El catálogo de biblioteca está en producción. Los bibliotecarios que lo usan quieren dos nuevas funcionalidades. Antes de que nadie escriba un componente React ni haga una llamada a la API, tu tech lead dice: **"Primero especificamos. Luego construimos."**

Tu trabajo es escribir especificaciones precisas para ambas funcionalidades. Consulta la documentación de la API en `http://localhost:8000/docs` para entender las formas reales de las respuestas antes de escribir ningún tipo. Tus specs deben ser lo suficientemente claras para que cualquier desarrollador — o agente de IA — pueda implementar la funcionalidad sin hacer preguntas.

---

## Conceptos Cubiertos

| Concepto | Dónde se aplica |
|---|---|
| Interfaces TypeScript | `api-types.ts` — formas de respuesta de endpoints reales de la API |
| Tipos de parámetros de consulta TypeScript | `param-types.ts` — parámetros de petición con JSDoc |
| Especificación de componentes | `components.md` — nombres, props, renderizado condicional, estados vacíos |
| Documentación del contrato de datos | `frontend/specs/README.md` — endpoints, tipos, casos borde |
| Desarrollo guiado por especificaciones | Escribir antes de construir para que la implementación sea inequívoca |

---

## Punto de Partida

Continúa en el mismo repositorio del catálogo de biblioteca. Crea una nueva rama:

```bash
git checkout -b feature/frontend-specs
mkdir -p frontend/specs
```

Arranca el backend y lee la documentación de la API en `http://localhost:8000/docs` antes de escribir nada.

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

### Tipos TypeScript (`frontend/specs/api-types.ts`)

- [ ] `BookEntry` — un registro de libro individual (id, título, autor, género, año, disponible)
- [ ] `BooksResponse` — lista de libros devuelta por el endpoint de búsqueda
- [ ] `GenreEntry` — una fila de género (nombre del género, número, porcentaje)
- [ ] `GenresSummaryResponse` — la respuesta completa del desglose de géneros

Reglas:
- Sin `any`, sin `object`
- Cada propiedad debe tener un comentario JSDoc que explique su significado y formato

### Tipos de Parámetros TypeScript (`frontend/specs/param-types.ts`)

- [ ] `BookSearchParams` — el parámetro de cadena de consulta `title` opcional
- [ ] `GenresSummaryParams` — acepta opcionalmente un filtro `title` para acotar las estadísticas de géneros

### Especificaciones de Componentes (`frontend/specs/components.md`)

Para cada funcionalidad, documenta:

**Funcionalidad 1 — Filtro de búsqueda por título**
- Nombre del componente y dónde se ubica en la página
- Props (si las hay) y sus tipos
- Qué se renderiza cuando el input está vacío vs. cuando no hay resultados

**Funcionalidad 2 — Panel de desglose por género**
- Nombre del componente, props y layout
- Qué se renderiza cuando hay menos de 3 géneros disponibles
- Cómo reacciona el panel cuando cambia el filtro de título

### Documentación del Contrato de Datos (`frontend/specs/README.md`)

Para cada funcionalidad, documenta:

- Qué endpoint(s) consume (verifica las rutas en `/docs`)
- Tipos TypeScript usados para la petición y la respuesta
- Valores válidos y restricciones para cada parámetro
- Al menos **2 casos borde** y qué debe mostrar la interfaz en cada uno

Ejemplos de casos borde a considerar:
- ¿Qué pasa si `title` contiene caracteres especiales como `&` o `/`?
- ¿Qué pasa si el endpoint de géneros devuelve un array vacío?
- ¿Qué pasa si la lista de libros tiene solo 1 género?

> ⚠️ **Importante:** No construyas componentes React ni hagas llamadas a la API. Tus entregables son los archivos `.ts` de tipos, `components.md` y `frontend/specs/README.md`.

---

## Preguntas para Discusión

1. ¿Por qué escribimos las interfaces TypeScript basándonos en la respuesta real de la API (desde `/docs`) en lugar de inferir la forma a partir de las necesidades del componente?
2. Se supone que el panel de géneros debe mostrar estadísticas para el "subconjunto filtrado" cuando hay un filtro de título activo. ¿Qué caso borde crea esto y cómo debe abordarlo la spec?
3. Un compañero dice: "¿Para qué molestarse con `components.md`? Con los tipos es suficiente." ¿Cuál es el argumento para escribir una especificación de componentes separada?
