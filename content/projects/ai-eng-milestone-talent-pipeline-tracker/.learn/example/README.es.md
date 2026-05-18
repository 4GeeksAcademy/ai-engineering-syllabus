# Ejemplo en Clase — Rastreador de Préstamos de Biblioteca Comunitaria

> **Nota para el instructor:** Este es un ejemplo diseñado para el ritmo del aula que introduce los mismos conceptos que el proyecto evaluado (Hito 3). Se utiliza un dominio diferente para que los estudiantes no lo confundan con su propio trabajo. El escenario es intencionalmente pequeño — el objetivo es una sesión de trabajo, no un producto terminado.

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una biblioteca de barrio lleva el seguimiento de los préstamos de libros con notas adhesivas y una pizarra. La bibliotecaria necesita una herramienta interna sencilla para ver quién tiene cada libro, cuándo hay que devolverlo, y añadir notas rápidas cuando un lector llama.

Ya existe una API REST documentada en `https://playground.4geeks.com/tracker/api/v1/docs` (se usa el mismo backend tracker). Los requisitos de la bibliotecaria:

> - Ver todos los préstamos activos en un listado (nombre del lector, título del libro, fecha de devolución, estado del préstamo).
> - Filtrar por estado (activo, devuelto, vencido). Buscar por nombre del lector.
> - Hacer clic en un préstamo para ver el detalle completo y actualizar su estado.
> - Añadir y eliminar notas breves en cualquier préstamo (ej. "el lector llamó, devuelve el viernes").
> - Registrar un préstamo nuevo y editar uno existente cuando algo cambia.

---

## Stack Tecnológico

| Capa | Herramienta |
|---|---|
| Framework | Next.js 14 (App Router) |
| Lenguaje | TypeScript |
| Estilos | Tailwind CSS |
| Datos | API REST via `fetch` + `async/await` |
| Estado | Solo hooks de React (sin librería externa) |

---

## Estructura del Proyecto (sugerida)

```
/app
  /page.tsx              ← listado de préstamos
  /loans/[id]/page.tsx   ← detalle del préstamo
/components
  LoanCard.tsx
  LoanForm.tsx
  NoteList.tsx
  StatusBadge.tsx
/types
  loan.ts
/lib
  api.ts                 ← todas las llamadas fetch en un solo lugar
```

---

## Qué Construir

### Página de listado de préstamos (`/`)

- [ ] Obtener todos los préstamos desde `GET /records` y mostrar: nombre del lector, título del libro, fecha de devolución, estado.
- [ ] Filtrar por estado usando `useSearchParams` (sin recarga completa).
- [ ] Buscar por nombre del lector (filtro en cliente, sin recarga).
- [ ] Mostrar un spinner mientras se cargan los datos; mostrar un mensaje de error si la petición falla.

### Página de detalle del préstamo (`/loans/[id]`)

- [ ] Obtener y mostrar todos los campos desde `GET /records/:id`: nombre del lector, email, teléfono, título del libro, ISBN, fecha de devolución, estado, notas.
- [ ] Actualizar el estado del préstamo via `PATCH /records/:id` — un desplegable o grupo de botones es suficiente.
- [ ] Listar notas desde `GET /records/:id/notes`. Añadir una nota (`POST`) y eliminar una nota (`DELETE`).
- [ ] Navegar de vuelta al listado sin recarga completa de página.

### Gestión de préstamos

- [ ] Formulario para crear un nuevo préstamo (`POST /records`) — validar campos requeridos antes de enviar.
- [ ] Formulario para editar un préstamo existente (`PUT /records/:id`) — rellenar previamente con los datos actuales.
- [ ] Mostrar un mensaje de éxito o error tras cada envío de formulario.

### Estados asíncronos (aplicar en todas partes)

- [ ] Cada operación con datos debe tener al menos tres estados de UI: **cargando**, **éxito**, **error**.
- [ ] Tras cualquier mutación (`POST`, `PATCH`, `PUT`, `DELETE`), actualizar la UI sin recarga completa.

### TypeScript

- [ ] Definir un tipo `Loan` y un tipo `Note` que coincidan con la forma de la respuesta de la API.
- [ ] Usar esos tipos en cada componente y función de servicio.

---

## Conceptos Clave a Trabajar en Clase

| Concepto | Dónde aparece |
|---|---|
| Rutas dinámicas | `/loans/[id]/page.tsx` |
| `useSearchParams` para filtros | Página de listado |
| Levantar estado vs. estado local | LoanForm dentro del listado vs. detalle |
| Async/await + estados de carga/error | Todas las llamadas `fetch` |
| Interfaces TypeScript para datos de la API | `/types/loan.ts` |
| Separación de responsabilidades | `/lib/api.ts` vs. componentes |

---

## Preguntas para Debate

1. ¿Por qué ponemos todas las llamadas fetch en `/lib/api.ts` en lugar de directamente dentro de los componentes? ¿Qué problema resuelve eso cuando cambia la URL de la API?
2. Cuando un usuario actualiza el estado del préstamo en la página de detalle, ¿debería actualizarse también la página de listado? ¿Cómo mantendrías ambas sincronizadas sin una recarga completa?
3. ¿Qué ocurre si la llamada `GET /records/:id` devuelve un `404`? ¿Cómo debería responder la UI y dónde en el código debería gestionarse eso?
