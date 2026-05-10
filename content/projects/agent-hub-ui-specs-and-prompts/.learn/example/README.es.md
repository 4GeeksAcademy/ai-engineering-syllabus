# Panel de Administración de Biblioteca — Ejemplo en Clase

> **Nota para el instructor:** Este es un ejemplo simplificado en clase para el proyecto "Agent Hub UI Specs and Prompts". Usa este escenario para introducir el flujo de trabajo spec-first y las interacciones de UI principales (sidebar, modales, dropdowns, modo oscuro) en 1–2 horas. El proyecto original cubre los mismos conceptos técnicos en un dominio más amplio y complejo.

---

## Escenario

Una pequeña biblioteca pública llamada **Biblioteca Comunitaria Bookshelf** necesita un panel de administración básico para gestionar su catálogo y la actividad de préstamos. Te han contratado para prototiparlo. Antes de tocar ningún HTML, debes escribir un documento de especificación (`SPECS.md`) que describa lo que vas a construir — con suficiente detalle como para que otro desarrollador (o un agente de IA) pueda implementarlo sin hacer preguntas.

La bibliotecaria ha compartido este brief:

> *"Necesito ver los libros que tenemos, quién los ha prestado y marcar los préstamos vencidos. Que sea sencillo. Uso un portátil, así que prioridad para escritorio."*

---

## Secciones a Construir

El panel debe tener **tres secciones** accesibles desde una barra lateral izquierda persistente:

### 1. Catálogo de Libros

Una tabla con todos los libros: título, autor, género y estado de disponibilidad (Disponible / En Préstamo / Vencido). Cada fila tiene un dropdown de acción `⋮` con dos opciones: **"Ver detalle"** (abre un modal con la información completa del libro) y **"Eliminar"**.

### 2. Préstamos Activos

Una tabla con los préstamos actuales: nombre del prestatario, título del libro, fecha de préstamo y fecha de devolución. Los préstamos vencidos se destacan con un badge de color. Cada fila tiene un dropdown `⋮` con **"Ver detalle"** y **"Marcar como devuelto"**.

### 3. Socios

Una lista de los socios registrados: nombre, correo electrónico y número de préstamos activos. Cada socio tiene un dropdown `⋮` con **"Ver detalle"** (abre un modal con el registro completo del socio).

---

## Lo que Debes Hacer

### Paso 1 — Escribe la especificación primero

- [ ] Crea `SPECS.md` en la raíz del proyecto **antes** de escribir ningún HTML.
- [ ] `SPECS.md` debe incluir:
  - [ ] Un párrafo de descripción del producto (qué es el panel, quién lo usa).
  - [ ] Stack tecnológico y restricciones: HTML, Tailwind CSS vía CDN, solo JS vanilla — sin frameworks, sin herramientas de build.
  - [ ] **Al menos 2 especificaciones por sección** — cada una nombrando un componente, describiendo su contenido y definiendo su comportamiento.
  - [ ] Un inventario de componentes con los elementos reutilizables: sidebar, fila de tabla, dropdown de acción, modal, badge de estado, toggle de modo oscuro.
  - [ ] Al menos 4 criterios de aceptación (uno por comportamiento interactivo).
- [ ] Haz commit de `SPECS.md` antes de escribir la primera línea de HTML.

> Una buena entrada de especificación tiene esta forma: *"Cada fila de la tabla de Libros tiene un botón `⋮`. Al hacer clic, se abre un menú desplegable con 'Ver detalle' y 'Eliminar'. El dropdown se cierra cuando el usuario hace clic fuera de él."*

### Paso 2 — Construye el prototipo

- [ ] Construye el panel como un único archivo `index.html`.
- [ ] Usa **Tailwind CSS vía CDN** — sin archivos CSS personalizados, sin atributos `style` en línea.
- [ ] Implementa una **sidebar** persistente con enlaces de navegación a las tres secciones.

#### Catálogo de Libros

- [ ] Tabla con al menos 5 libros hardcodeados (título, autor, género, badge de estado).
- [ ] Dropdown de acción `⋮` por fila: "Ver detalle" abre un modal; "Eliminar" puede ser sin acción.
- [ ] El modal muestra los detalles completos del libro y se cierra con el botón de cierre y al hacer clic en el backdrop.

#### Préstamos Activos

- [ ] Tabla con al menos 4 préstamos hardcodeados (prestatario, libro, fecha de préstamo, fecha de devolución).
- [ ] Los préstamos vencidos se distinguen visualmente con un badge rojo.
- [ ] Dropdown `⋮` por fila: "Ver detalle" y "Marcar como devuelto" (puede ser sin acción).

#### Socios

- [ ] Lista con al menos 3 socios hardcodeados (nombre, correo, número de préstamos activos).
- [ ] Dropdown `⋮` por fila: "Ver detalle" abre un modal con el registro completo del socio.

#### Interacciones globales

- [ ] **Toggle de modo oscuro/claro** en la barra superior que cambia todo el panel usando las utilidades `dark:` de Tailwind.
- [ ] Todos los dropdowns se cierran al hacer clic fuera.
- [ ] Todos los modales se cierran con el botón de cierre y al hacer clic en el backdrop.
- [ ] La sección activa queda resaltada en la sidebar.

> **Importante:** Toda la interactividad debe ser JavaScript vanilla — sin librerías ni frameworks.

---

## Criterios de Aceptación

| # | Criterio |
|---|----------|
| 1 | `SPECS.md` está commiteado antes que cualquier archivo HTML (verificable en el historial de Git) |
| 2 | Las tres secciones son accesibles desde la sidebar |
| 3 | "Ver detalle" abre un modal en al menos dos secciones |
| 4 | Todos los modales se cierran con el botón de cierre y al hacer clic en el backdrop |
| 5 | El toggle de modo oscuro/claro cambia todo el panel |
| 6 | Todos los dropdowns `⋮` se cierran al hacer clic fuera |

---

## Stack Tecnológico de Referencia

| Capa | Tecnología |
|------|------------|
| Marcado | HTML5 (etiquetas semánticas: `nav`, `main`, `section`, `table`) |
| Estilos | Tailwind CSS vía CDN |
| Interactividad | JavaScript vanilla |
| Datos | Hardcodeados en HTML |

---

## Preguntas para Debatir

1. ¿Por qué escribir la especificación antes del HTML es una ventaja cuando se trabaja con un agente de código IA? ¿Qué podría salir mal si se omite?
2. ¿Cuál es la relación entre el inventario de componentes en `SPECS.md` y la forma en que estructuras tu código JavaScript?
3. Si necesitaras añadir una cuarta sección (por ejemplo, "Multas por retraso"), ¿qué añadirías a `SPECS.md` antes de tocar el HTML? Escribe una entrada de especificación como ejemplo.
