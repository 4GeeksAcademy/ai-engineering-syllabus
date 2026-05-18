# Ejemplo de clase: Rastreador de bugs del portfolio

> **Nota para el instructor:** Este es un ejemplo de clase para introducir los conceptos del proyecto *Gestor de Incidencias Centralizado* usando un dominio más sencillo. Cubre el mismo stack y los mismos patrones (modelo de datos con ciclo de vida, seed, API REST, formulario/listado/resumen en frontend, validación compartida), pero está pensado para una sesión en vivo de 1 a 2 horas. NO compartir este archivo con los estudiantes antes de que intenten el proyecto principal.

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una desarrolladora mantiene su portfolio personal con varias páginas (Inicio, Sobre mí, Proyectos, Contacto). Los visitantes a veces encuentran bugs: enlaces rotos, imágenes que no cargan, problemas de layout o erratas. Quiere una pequeña herramienta interna para registrar esos reportes, asignarles prioridad, moverlos por un ciclo de vida de resolución y ver un resumen rápido de lo que está pendiente.

El equipo ya tiene un CSV con 10 bugs históricos que deben importarse como seed data en el primer arranque.

---

## Modelo de datos

Define una entidad `BugReport` con los siguientes campos:

| Campo | Tipo | Notas |
|---|---|---|
| `id` | entero | Generado automáticamente |
| `title` | texto | Obligatorio |
| `description` | texto | Obligatorio |
| `page` | enum | `home`, `about`, `projects`, `contact` |
| `priority` | enum | `low`, `medium`, `high` |
| `status` | enum | `open`, `in_progress`, `resolved`, `discarded` |
| `created_at` | datetime | Generado automáticamente |
| `updated_at` | datetime | Actualizado automáticamente |

**Transiciones del ciclo de vida:**

```
open → in_progress → resolved
open → discarded
in_progress → discarded
resolved y discarded son estados finales (no se permiten transiciones desde ellos)
```

---

## Datos de seed (`/scripts`)

El siguiente CSV representa el fichero de importación histórica. Guárdalo como `bug-reports.csv`:

```csv
title,description,page,priority,status
Broken contact form,Submit button does nothing on mobile,contact,high,open
Missing profile photo,Image returns 404,about,medium,open
Typo in hero text,"Recieve" should be "Receive",home,low,resolved
Dead project link,Link to GitHub project 404s,projects,high,open
Wrong font on mobile,Body text uses serif on iOS,home,low,open
Footer overlaps content,Footer covers last section on small screens,about,medium,in_progress
Slow image load,Hero image takes 8s to load,home,medium,open
Missing alt text,All project images have empty alt,projects,low,open
Form validation missing,Email field accepts any text,contact,high,open
Dark mode flicker,Screen flashes white on load in dark mode,home,low,discarded
```

- [ ] Crea `seed.py` que lea `bug-reports.csv` e inserte cada fila en la base de datos.
- [ ] Omite las filas con campos obligatorios vacíos e imprímelas por consola al final.
- [ ] Haz el script idempotente: comprueba por `title` antes de insertar para evitar duplicados.

---

## Backend (FastAPI)

- [ ] `POST /api/bugs` — crea un nuevo reporte. Devuelve `400` con un mensaje de error a nivel de campo para cualquier campo ausente o con valor inválido.
- [ ] `GET /api/bugs` — lista todos los reportes. Acepta filtros opcionales: `status`, `priority`, `page`.
- [ ] `GET /api/bugs/{id}` — devuelve un reporte individual. Devuelve `404` si no existe.
- [ ] `PATCH /api/bugs/{id}/status` — actualiza el estado. Rechaza transiciones de ciclo de vida inválidas con `400`.
- [ ] `GET /api/bugs/summary` — devuelve totales agrupados por `status`, `priority` y `page`. Debe devolver ceros si la base de datos está vacía (sin errores).

**Reglas de manejo de errores:**
- Las excepciones no controladas devuelven `500` con un mensaje genérico — nunca un traceback de Python.
- Los errores de validación identifican el campo problemático en el cuerpo JSON de la respuesta.

---

## Frontend (Next.js)

**Formulario de reporte:**

- [ ] Una página con un formulario que incluye todos los campos del modelo.
- [ ] Muestra un spinner de carga mientras la petición está en curso; deshabilita el botón de envío.
- [ ] Si la API devuelve un error a nivel de campo, muestra el mensaje junto al input correspondiente.
- [ ] En caso de éxito, limpia el formulario y muestra un mensaje de confirmación.
- [ ] Nunca muestres el texto de error técnico del servidor al usuario.

**Panel de listado:**

- [ ] Una página con todos los reportes, con filtros por `status`, `priority` y `page`.
- [ ] Gestiona tres estados: cargando (spinner), vacío (mensaje informativo), con datos (tabla/tarjetas).
- [ ] Permite actualizar el estado de cada reporte de forma inline. Si la actualización falla, revierte el estado visual y notifica al usuario.

**Panel de resumen:**

- [ ] Muestra los totales del endpoint `/api/bugs/summary`.
- [ ] Si la petición falla, muestra un estado de error sin romper el resto de la página.

---

## Validación compartida

- [ ] Extrae la lógica de validación (campos obligatorios, valores de enum, transiciones de ciclo de vida) a un módulo compartido que reutilicen tanto el script de seed como la API. Sin duplicación.

---

## Preguntas de discusión

1. ¿Por qué es importante que el script de seed sea idempotente? ¿Qué podría salir mal si lo ejecutas dos veces en una base de datos de producción sin esa comprobación?
2. El ciclo de vida del estado impide pasar directamente de `open` a `resolved`. ¿Puedes pensar en un motivo del mundo real por el que estas restricciones importan, y cómo comunicarías una transición rechazada al usuario de forma amigable?
3. El endpoint de resumen debe devolver ceros aunque la base de datos esté vacía. ¿Por qué devolver `{ "open": 0, ... }` en lugar de un objeto vacío `{}`? ¿Cómo afecta esto al código del frontend?
