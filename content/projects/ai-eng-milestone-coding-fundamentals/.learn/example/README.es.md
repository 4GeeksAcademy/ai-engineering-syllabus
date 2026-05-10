# Ejemplo de clase: Gestor de colección de películas (TypeScript)

> **Nota para el instructor:** Este es un ejemplo de clase para introducir los conceptos del proyecto *Hito 2 — Desarrollando scripts para automatizar tareas* usando un dominio más sencillo. Cubre las mismas habilidades de TypeScript (interfaces, filtrado, ordenamiento, búsqueda lineal, búsqueda binaria, agregaciones, validaciones de negocio, funciones puras) pero con una colección de películas como modelo de datos. Alcance: sesión en vivo de 1 a 2 horas. NO compartir este archivo con los estudiantes antes de que intenten el proyecto principal.

---

## El escenario

Una desarrolladora quiere construir un gestor de su colección personal de películas. Tiene una lista de películas almacenadas como objetos en TypeScript y necesita un conjunto de funciones utilitarias reutilizables para filtrar, buscar, ordenar y resumir la colección.

Aún no hay base de datos ni API — este hito trata exclusivamente de la capa lógica.

---

## Modelo de datos

Define las siguientes interfaces en `src/types/models.ts`:

```typescript
type Genre = "action" | "comedy" | "drama" | "horror" | "sci-fi" | "documentary" | "animation";
type WatchStatus = "watched" | "watchlist" | "dropped";

interface Director {
  id: number;
  name: string;
  nationality: string;
}

interface Movie {
  id: number;
  title: string;
  year: number;            // 1888–año actual
  genre: Genre;
  director: Director;
  rating: number;          // 0.0–10.0
  durationMinutes: number; // debe ser > 0
  status: WatchStatus;
}
```

### Datos de ejemplo

Usa este conjunto de datos inicial en `src/data/movies.ts`:

```typescript
export const movies: Movie[] = [
  { id: 1,  title: "Inception",              year: 2010, genre: "sci-fi",      director: { id: 1, name: "Christopher Nolan",    nationality: "Británico"      }, rating: 8.8, durationMinutes: 148, status: "watched"   },
  { id: 2,  title: "The Dark Knight",        year: 2008, genre: "action",      director: { id: 1, name: "Christopher Nolan",    nationality: "Británico"      }, rating: 9.0, durationMinutes: 152, status: "watched"   },
  { id: 3,  title: "Parásitos",              year: 2019, genre: "drama",       director: { id: 2, name: "Bong Joon-ho",         nationality: "Coreano"        }, rating: 8.6, durationMinutes: 132, status: "watched"   },
  { id: 4,  title: "El viaje de Chihiro",    year: 2001, genre: "animation",   director: { id: 3, name: "Hayao Miyazaki",       nationality: "Japonés"        }, rating: 8.6, durationMinutes: 125, status: "watched"   },
  { id: 5,  title: "Get Out",                year: 2017, genre: "horror",      director: { id: 4, name: "Jordan Peele",         nationality: "Estadounidense" }, rating: 7.7, durationMinutes: 104, status: "watched"   },
  { id: 6,  title: "Everything Everywhere",  year: 2022, genre: "sci-fi",      director: { id: 5, name: "Daniels",              nationality: "Estadounidense" }, rating: 7.8, durationMinutes: 139, status: "watchlist" },
  { id: 7,  title: "Knives Out",             year: 2019, genre: "comedy",      director: { id: 6, name: "Rian Johnson",         nationality: "Estadounidense" }, rating: 7.9, durationMinutes: 130, status: "watchlist" },
  { id: 8,  title: "Dune",                   year: 2021, genre: "sci-fi",      director: { id: 7, name: "Denis Villeneuve",     nationality: "Canadiense"     }, rating: 8.0, durationMinutes: 155, status: "watched"   },
  { id: 9,  title: "El poder del perro",     year: 2021, genre: "drama",       director: { id: 8, name: "Jane Campion",         nationality: "Neozelandesa"   }, rating: 6.9, durationMinutes: 126, status: "dropped"   },
  { id: 10, title: "Free Guy",               year: 2021, genre: "comedy",      director: { id: 9, name: "Shawn Levy",           nationality: "Canadiense"     }, rating: 7.1, durationMinutes: 115, status: "watchlist" },
];
```

---

## Estructura de archivos

```text
src/
├── types/
│   └── models.ts          # Interfaces y tipos
├── data/
│   └── movies.ts          # Conjunto de datos de ejemplo
├── utils/
│   ├── collections.ts     # funciones de filtrado y ordenamiento
│   ├── search.ts          # búsqueda lineal y binaria
│   ├── transformations.ts # agregaciones e informes
│   └── validations.ts     # validaciones de negocio
└── demo.ts                # Runner de pruebas manual
```

---

## Qué implementar

### `src/utils/collections.ts` — Filtrado y ordenamiento

- [ ] `filterByGenre(movies: Movie[], genre: Genre): Movie[]`
- [ ] `filterByStatus(movies: Movie[], status: WatchStatus): Movie[]`
- [ ] `filterByYearRange(movies: Movie[], from: number, to: number): Movie[]`
- [ ] `filterByMinRating(movies: Movie[], minRating: number): Movie[]`
- [ ] `sortByRating(movies: Movie[], order: "asc" | "desc"): Movie[]`
- [ ] `sortByYear(movies: Movie[], order: "asc" | "desc"): Movie[]`
- [ ] `sortByTitle(movies: Movie[]): Movie[]` — alfabético, ascendente

Todas las funciones deben ser **puras**: devuelven un nuevo array sin mutar el de entrada.

---

### `src/utils/search.ts` — Algoritmos de búsqueda

- [ ] `linearSearchByTitle(movies: Movie[], title: string): Movie | null`
  - Funciona con cualquier array independientemente del orden.
  - Devuelve la primera coincidencia exacta (sin distinción entre mayúsculas y minúsculas) o `null` si no se encuentra.

- [ ] `binarySearchById(sortedMovies: Movie[], id: number): Movie | null`
  - El array de entrada **debe** estar ordenado por `id` de forma ascendente.
  - Devuelve la película coincidente o `null` si no se encuentra.
  - Debe implementar el algoritmo de búsqueda binaria — no usar `.find()`.

Añade un comentario que explique por qué la búsqueda binaria requiere un array ordenado.

---

### `src/utils/transformations.ts` — Agregaciones

- [ ] `countByGenre(movies: Movie[]): Record<Genre, number>` — devuelve un recuento para cada género, incluidos los géneros con 0 películas
- [ ] `countByStatus(movies: Movie[]): Record<WatchStatus, number>`
- [ ] `averageRating(movies: Movie[]): number` — devuelve `0` para un array vacío
- [ ] `topRated(movies: Movie[], n: number): Movie[]` — devuelve las `n` películas mejor puntuadas (descendente)
- [ ] `totalDuration(movies: Movie[]): number` — suma de `durationMinutes` de todas las películas del array de entrada

---

### `src/utils/validations.ts` — Reglas de negocio

- [ ] `isValidMovie(movie: unknown): movie is Movie` — devuelve `true` solo si:
  - `title` es una cadena no vacía
  - `year` está entre 1888 y el año actual (inclusive)
  - `genre` es uno de los valores permitidos
  - `rating` está entre 0 y 10 (inclusive)
  - `durationMinutes` es mayor que 0
  - `status` es uno de los valores permitidos
  - `director.name` es una cadena no vacía

- [ ] `validateMovieOrThrow(movie: unknown): Movie` — llama a `isValidMovie`; lanza un `Error` descriptivo si es inválido; si no, devuelve la película tipada.

---

### `src/demo.ts` — Runner de pruebas manual

- [ ] Llama a cada utilidad con los datos de ejemplo e imprime los resultados por consola.
- [ ] Ejecútalo con: `npx tsx src/demo.ts`

Ejemplo de salida:

```
--- Filtro: películas de sci-fi ---
Inception, Dune, Everything Everywhere

--- Ordenar: por rating DESC ---
The Dark Knight (9.0), Inception (8.8), ...

--- Búsqueda lineal: "Dune" ---
Encontrada: Dune (2021)

--- Búsqueda binaria por id: 5 ---
Encontrada: Get Out

--- Recuento por género ---
action: 1, comedy: 2, drama: 2, horror: 1, sci-fi: 3, documentary: 0, animation: 1

--- Rating medio ---
8.04

--- Validación: película inválida ---
Error: "year" debe estar entre 1888 y 2026
```

---

## Reglas de calidad de código

- [ ] Todos los parámetros y valores de retorno tienen tipos explícitos de TypeScript (sin `any`)
- [ ] Usa `const` por defecto; `let` solo cuando el valor deba cambiar
- [ ] Gestiona casos límite: los arrays vacíos devuelven valores por defecto razonables (array vacío, `0`, `null`)
- [ ] Cada función hace exactamente una cosa (principio de responsabilidad única)
- [ ] Sin errores de compilación de TypeScript: verifica con `npx tsc --noEmit`

---

## Preguntas de discusión

1. `linearSearchByTitle` funciona con cualquier array, pero `binarySearchById` requiere que el array esté ordenado primero. Para una colección de 10 películas, ¿merece la pena el coste de ordenar para usar la búsqueda binaria? ¿A partir de qué tamaño de colección cambia la respuesta, y por qué?
2. `countByGenre` devuelve un recuento para cada género, incluyendo los géneros sin películas. ¿Por qué es mejor devolver `{ ..., "documentary": 0 }` en lugar de omitir la clave? ¿Cómo afecta esto al código que consume el resultado?
3. `isValidMovie` acepta `unknown` como tipo de entrada en lugar de `Movie`. ¿Por qué es más seguro esto que aceptar `Movie` directamente? ¿Puedes pensar en una situación donde recibirías datos de tipo desconocido que necesitan validarse antes de usarse?
