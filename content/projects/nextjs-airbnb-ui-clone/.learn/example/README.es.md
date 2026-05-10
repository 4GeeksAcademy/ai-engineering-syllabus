> **Ejemplo para usar en clase (solo instructores).** Usa este escenario para introducir el App Router de Next.js, hooks de React, Tailwind mobile-first y prompts de visión en una sesión de ~1-2 horas. Este archivo es un recurso pedagógico con un *dominio diferente* al del proyecto asignado. No lo compartas con los estudiantes como su brief de proyecto.

# Interfaz de Alquiler de Coches — Ejemplo en Clase con Next.js y React

## Escenario

Una agencia de alquiler de coches quiere una interfaz moderna y mobile-first donde los usuarios puedan explorar los vehículos disponibles, ver los resultados de búsqueda y consultar el detalle de un coche concreto. El tech lead ha definido tres páginas y un conjunto de componentes a implementar.

> #### Brief del producto
>
> Construye tres vistas de una experiencia de alquiler de coches en Next.js usando componentes de React:
> - **Home (`/`)** — barra de búsqueda + chips de tipo de vehículo + cuadrícula de tarjetas
> - **Flota (`/fleet`)** — lista ordenada de coches disponibles + placeholder de mapa
> - **Detalle del coche (`/cars/[id]`)** — galería de fotos, especificaciones, widget de reserva
>
> La implementación debe ser **mobile-first** (375px primero, escritorio a partir de 768px). Sin librerías de componentes prefabricadas — solo clases de Tailwind.

---

## Páginas y componentes

### Página de inicio (`/`)

| Componente | Qué hace | Hook usado |
|------------|----------|------------|
| `Navbar` | Logo + campo de búsqueda + icono de usuario | — |
| `SearchBar` | Input de texto controlado que filtra tarjetas en tiempo real | `useState` |
| `CategoryFilter` | Fila horizontal de chips: Económico, SUV, Eléctrico, Lujo | `useState` (categoría activa) |
| `CarCard` | Placeholder de foto, modelo, precio/día, valoración con estrellas | — |
| `CarGrid` | Cuadrícula responsiva de `CarCard` (1 col → varias col) | `useEffect` (simular carga de datos) |

### Página de flota (`/fleet`)

| Componente | Qué hace | Hook usado |
|------------|----------|------------|
| `ResultsHeader` | "X coches disponibles" + toggle de orden (Asc/Desc por precio) | `useState` |
| `CarCard` | Reutilizado de la Home | — |
| `MapPlaceholder` | Caja gris con texto "Mapa" (a la derecha en escritorio, abajo en móvil) | — |

### Página de detalle del coche (`/cars/[id]`)

| Componente | Qué hace | Hook usado |
|------------|----------|------------|
| `PhotoGallery` | Array de placeholders de fotos + botones Anterior/Siguiente | `useState` (índice de foto) |
| `CarHeader` | Modelo, año, valoración, número de reseñas | — |
| `SpecsGrid` | Plazas, transmisión, combustible, puertas | — |
| `BookingCard` | Precio/día + contador de días (mín 1, máx 30) + botón CTA | `useState` (días) |

---

## Lista de verificación

### 0 — Antes de escribir código

- [ ] Crear `context.md` en la raíz del proyecto describiendo cada página, sus componentes principales y el usuario objetivo

### 1 — Configuración del proyecto

- [ ] Crear el proyecto con `npx create-next-app` (TypeScript + Tailwind + App Router)
- [ ] Estructura de carpetas: `/app` para rutas, `/components` para UI reutilizable, `/types` para interfaces TypeScript

### 2 — Flujo de trabajo con prompts de visión

- [ ] Hacer una captura de pantalla de cualquier web real de alquiler de coches (p. ej. Hertz, Enterprise) a 375px de viewport
- [ ] Adjuntar la captura al agente de código con IA y pedirle que genere una especificación de componentes
- [ ] Documentar la especificación generada en `context.md` antes de codificar esa vista

### 3 — Implementación

- [ ] Home: `SearchBar` filtra tarjetas en tiempo real con `useState`; `CategoryFilter` resalta el chip activo; `CarGrid` carga datos con `useEffect` + estado de carga
- [ ] Flota: `ResultsHeader` con toggle de orden (Asc/Desc precio) con `useState`; reutilizar `CarCard`; `MapPlaceholder`
- [ ] Detalle: `PhotoGallery` con índice en `useState`; `BookingCard` con contador de días en `useState`; datos cargados con `useEffect`

### 4 — Navegación y calidad

- [ ] Hacer clic en un `CarCard` navega a `/cars/[id]` usando `<Link>` de Next.js
- [ ] El detalle del coche tiene un botón de volver que regresa a `/fleet`
- [ ] Sin etiquetas `<a href="...">` para navegación interna
- [ ] Todos los componentes son `const` (componentes funcionales) — sin componentes de clase
- [ ] Interfaces TypeScript definidas para la estructura de datos `Car`

⚠️ **IMPORTANTE:** Sin librerías de componentes prefabricadas (ni shadcn, MUI, Chakra). Solo clases de Tailwind.

---

## Preguntas de debate

1. El `SearchBar` filtra tarjetas usando `useState`. ¿Qué habría que cambiar si el término de búsqueda tuviera que sobrevivir a una recarga de página (p. ej. para compartir por URL)? ¿Qué API de Next.js usarías?
2. ¿Por qué recomienda Next.js usar `<Link>` en lugar de `<a href>` para la navegación interna? ¿Qué ocurre internamente cuando usas `<Link>`?
3. El `useEffect` en `CarGrid` simula una petición de datos con `setTimeout`. ¿Qué cambiarías para reemplazarlo por una llamada a una API real, y qué casos límite (carga, error, estado vacío) habría que gestionar?
