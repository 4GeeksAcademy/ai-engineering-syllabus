# Wanderlust Explorer — App Interactiva con React y Next.js

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo iniciar un proyecto de código.

<!-- endhide -->

---

## 🎯 Tu reto

Wanderlust Labs es una startup de travel-tech que está construyendo una plataforma para descubrir y guardar experiencias únicas alrededor del mundo: desde tours gastronómicos en Bangkok hasta rutas de vela por el Adriático. Su diseñadora de producto ya ha preparado referencias visuales, y el equipo de ingeniería necesita un desarrollador frontend que dé vida al MVP del explorador.

Tu misión es construir el **explorador de experiencias**: una aplicación multipágina con React y Next.js donde los usuarios puedan explorar, buscar y filtrar experiencias sin recargar la página. Antes de escribir un solo componente, busca 2 o 3 interfaces reales que admires y que encajen con la estética esperada: una UI de descubrimiento limpia con tarjetas, una barra de búsqueda y un sistema de filtros. Úsalas como referencia de diseño y documéntalas en tu README bajo una sección "Design References".

Tu dataset será un array de 100 experiencias generadas con IA. La PM quiere que la búsqueda y los filtros vivan en la URL para que los usuarios puedan compartir enlaces como `/experiences?search=vela&category=adventure&destination=Croatia` y aterrizar directamente en una vista prefiltrada.

> Tu PM, Lea Moreau, te envió la siguiente spec por Slack:
>
> #### Páginas requeridas
>
> - **`/`** — Home: sección hero con un botón que navega a `/experiences`
> - **`/experiences`** — Explorador: listado completo de tarjetas con barra de búsqueda y al menos dos filtros (categoría y destino). La búsqueda y los filtros activos deben reflejarse en la URL como query parameters y deben prerrellenar los inputs al cargar la página
> - **`/experiences/[id]`** — Detalle: información completa de una experiencia, obtenida del dataset local por su ID
> - **`/favorites`** — Favoritos: lista de experiencias que el usuario ha marcado como favoritas (guardadas en estado de componente por ahora)
> - **`/profile`** — Perfil: página estática con un perfil de usuario simulado y un resumen con el número de favoritos guardados
>
> #### Comportamiento de la búsqueda
>
> La búsqueda debe filtrar las experiencias cuyo título coincida con el término buscado. Usa una regex case-insensitive para esto: algo como `/term/i`. El filtro por categoría y destino debe funcionar de forma independiente y combinarse con la búsqueda.
>
> #### Dataset
>
> Usa un asistente de código con IA para generar un array de 100 objetos de experiencia. Cada objeto debe tener como mínimo: `id`, `title`, `description`, `category` (una de: Adventure, Culture, Food, Wellness, Nature), `destination` (ciudad + país), `price`, `rating` e `imageUrl` (cualquier placeholder). Guárdalo como un fichero TypeScript local.
>
> #### Favoritos
>
> Un icono de corazón en cada tarjeta debe activar o desactivar la experiencia en la lista de favoritos del usuario. Los favoritos se guardan en un `useState` de nivel superior y se pasan hacia abajo como props donde sea necesario. No se requiere persistencia por ahora.

Este es el tipo de funcionalidad que aparece en sprints reales de producto: filtros compartibles por URL, estado manejado desde la URL y composición de componentes. Constrúyelo como algo que pondrías en tu portfolio — porque deberías.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto empieza **desde cero** — no hay ningún template que forkear. Tú crearás tu propia app de Next.js desde el principio.

1. Crea un nuevo proyecto con el CLI oficial de Next.js (con TypeScript y el App Router):

   ```bash
   npx create-next-app@latest nextjs-wanderlust-explorer --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
   ```

2. Crea un **repositorio público** en tu cuenta de GitHub con el nombre `nextjs-wanderlust-explorer`.

3. Conecta tu proyecto local a ese repositorio:

   ```bash
   git remote add origin https://github.com/TU_USUARIO/nextjs-wanderlust-explorer.git
   git push -u origin main
   ```

4. Abre el proyecto en GitHub Codespaces o en tu editor local y empieza a construir.

> 📗 ¿Necesitas repasar el flujo? [Cómo iniciar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project)

---

## 💻 Qué debes hacer

### 🗂️ Setup y dataset

- [ ] Inicializa el proyecto desde cero con `create-next-app` (TypeScript + Tailwind + App Router)
- [ ] Usa un asistente de código con IA para generar el array de 100 experiencias y guárdalo como `src/data/experiences.ts`
- [ ] Define una `interface Experience` en TypeScript con la forma de los datos y úsala en todo el proyecto
- [ ] Añade una sección `## Design References` en tu `README.md` con enlaces o capturas de 2-3 UIs reales que hayan inspirado tu diseño

### 🏠 Páginas y enrutamiento

- [ ] Crea la **Home** (`/`) con una sección hero y un botón que navega a `/experiences`
- [ ] Crea el **Explorador** (`/experiences`) con las 100 tarjetas de experiencias en una cuadrícula
- [ ] Crea la página de **Detalle** (`/experiences/[id]`) que lee el ID desde la URL y muestra el contenido completo de esa experiencia
- [ ] Crea la página de **Favoritos** (`/favorites`) que muestra solo las experiencias marcadas como favoritas
- [ ] Crea la página de **Perfil** (`/profile`) con un perfil de usuario simulado y el contador de favoritos guardados

### 🔍 Búsqueda y filtros

- [ ] Añade una **barra de búsqueda** en el Explorador que filtre experiencias por título
- [ ] Usa una **regex case-insensitive** para comparar el término con el título de cada experiencia (ej. `new RegExp(term, 'i').test(experience.title)`)
- [ ] Añade un **filtro de categoría** (dropdown o grupo de botones) con las cinco categorías disponibles
- [ ] Añade un **filtro de destino** (dropdown o búsqueda) que filtre por ciudad o país de destino
- [ ] Los filtros activos y el término de búsqueda deben almacenarse como **query parameters en la URL** usando `useSearchParams` y `usePathname` de Next.js
- [ ] Al cargar la página con query params existentes en la URL, los inputs de búsqueda y filtros deben **prerrellenarse** con esos valores

### ❤️ Favoritos

- [ ] Añade un icono de corazón (toggle) a cada tarjeta de experiencia
- [ ] Guarda la lista de IDs favoritos en un `useState` a nivel compartido y pásala hacia abajo como props
- [ ] El icono de corazón debe reflejar visualmente si la experiencia está en favoritos o no

### 🧩 Componentes y hooks

- [ ] Crea como mínimo los componentes: `ExperienceCard`, `SearchBar`, `FilterBar`, `Navbar`
- [ ] Usa `useEffect` en al menos un componente (ej. para sincronizar los resultados filtrados cuando cambien los query params, o para actualizar el título del documento en la página de detalle)
- [ ] Crea al menos un **custom hook** (ej. `useExperiences` o `useFilters`) que encapsule la lógica de filtrado

### 🎨 UI y calidad

- [ ] La app debe ser **responsiva** (móvil + escritorio)
- [ ] El explorador debe mostrar un mensaje **"No se encontraron resultados"** cuando los filtros no devuelvan ningún resultado
- [ ] La Navbar debe estar presente en todas las páginas y mostrar estilos de enlace activo usando `usePathname`

⚠️ **IMPORTANTE:** No uses ninguna librería externa de gestión de estado (Redux, Zustand, etc.). Todo el estado debe vivir en el `useState` nativo de React y pasarse mediante props o custom hooks.

---

## ✅ Qué vamos a evaluar

- [ ] La app tiene al menos 5 páginas distintas con navegación del lado del cliente (sin recargas completas de página entre rutas)
- [ ] La búsqueda filtra resultados por título usando una coincidencia con regex
- [ ] Los filtros de categoría y destino funcionan de forma independiente y se combinan correctamente con la búsqueda
- [ ] Los filtros activos y el término de búsqueda se reflejan en la URL como query params
- [ ] Al cargar la página con query params existentes, los inputs están prerrellenados y los resultados ya están filtrados
- [ ] `useEffect` se usa correctamente con arrays de dependencias adecuados (sin bucles infinitos ni dependencias faltantes)
- [ ] `useState` se usa para gestionar favoritos y se pasa correctamente como props
- [ ] Existe al menos un custom hook que encapsula lógica con significado
- [ ] Los componentes están divididos de forma lógica — ningún fichero contiene toda la app
- [ ] Los tipos e interfaces de TypeScript están definidos y se usan de forma consistente
- [ ] La app es responsiva y visualmente coherente entre páginas
- [ ] Las referencias de diseño están documentadas en el README

> **Nota:** La persistencia de favoritos entre recargas de página **no** se evalúa. El uso de `localStorage` está fuera del alcance de este proyecto.

---

## 📦 Cómo entregar

1. Asegúrate de que todo tu trabajo está commiteado y subido a tu repositorio de GitHub.
2. Comparte la URL del repositorio con tu instructor siguiendo sus instrucciones de entrega.
3. Si has desplegado la app (ej. en Vercel), incluye la URL en la descripción de tu repositorio — es un plus, no un requisito.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
