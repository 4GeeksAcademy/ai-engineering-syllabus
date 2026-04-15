# Clonando la interfaz de Airbnb con Next.js y React

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/nextjs-airbnb-clone/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo iniciar un proyecto de código.

<!-- endhide -->

---

## 🎯 Tu reto

Un estudio de diseño de producto acaba de ganar un contrato para reconstruir el frontend de una plataforma de alquiler vacacional. Antes de crear su propio sistema de diseño, quieren validar la arquitectura de componentes clonando una interfaz de producción bien conocida: Airbnb. De esta forma, el equipo aprende qué componentes son necesarios, qué datos necesita cada uno y cómo se conectan entre las distintas vistas.

Te han incorporado como desarrollador frontend junior. Tu misión es implementar **tres vistas** de la experiencia de Airbnb en Next.js usando componentes de React: la **página de inicio (Home)**, la **página de catálogo (resultados de búsqueda)** y la **vista de detalle de una habitación**. Usarás prompts de visión para convertir capturas de pantalla en especificaciones de componentes, y luego implementarás esas especificaciones.

El tech lead del estudio te ha enviado un brief rápido:

> #### Brief del producto
>
> - La implementación debe ser **mobile-first**. Diseña primero para un viewport de 375px; adapta al escritorio a partir de 768px.
> - Antes de escribir código, crea un archivo `context.md` en la raíz del repositorio. Este archivo debe describir con tus propias palabras la interfaz que vas a construir: qué contiene cada página, cuáles son los componentes principales, quién es el usuario y qué intenta hacer. Piénsalo como el mini-brief que escribirías antes de empezar un proyecto real.
> - Usa prompts de visión: adjunta una captura de pantalla de la interfaz original de Airbnb a tu agente de código con IA para generar una especificación de componentes y úsala como guía durante la implementación.
> - Mantén los componentes pequeños y enfocados. Una responsabilidad por componente.
> - La navegación entre las tres páginas debe funcionar sin recargar el navegador.

Este es exactamente el tipo de tarea que recibirás en tu primer trabajo: una interfaz real que replicar, un framework real que usar y la responsabilidad de decidir cómo estructurarlo. Parte de lo que ves, razona sobre lo que hace cada pieza y constrúyelo componente a componente.

---

## 🌱 Cómo iniciar el proyecto

No hay plantilla de inicio para este proyecto. Tu primera tarea es pedirle a tu agente de código con IA que configure el proyecto por ti.

Usa un prompt similar a este:

> "Configura un nuevo proyecto de Next.js 16 con TypeScript, Tailwind CSS y el App Router. Usa `npx create-next-app` con las opciones adecuadas. Llama al proyecto `airbnb-clone`. Organiza la estructura de carpetas con una carpeta `/components` para las piezas de UI reutilizables."

Una vez que el agente genere los comandos, revísalos, ejecútalos en tu terminal y asegúrate de que el servidor de desarrollo arranque correctamente antes de escribir ningún componente.

Después:

1. Crea tu propio repositorio en GitHub.
2. Inicializa git dentro de la carpeta del proyecto y sube tu primer commit.
3. ¿Necesitas un repaso sobre el inicio de proyectos? [Lee esta guía](https://4geeks.com/lesson/como-comenzar-un-proyecto-de-codificacion).

---

## 💻 Qué debes hacer

### 0 — Antes de escribir código

- [ ] Crea un archivo `context.md` en la raíz del proyecto. Debe incluir:
  - [ ] Una descripción de las tres páginas que vas a construir y qué muestra cada una.
  - [ ] Un listado de los componentes principales que identificas en cada vista (usa Airbnb.com como referencia).
  - [ ] Un párrafo corto que describa al usuario y qué intenta conseguir en esta plataforma.

### 1 — Configuración del proyecto

- [ ] Pídele a tu agente de código con IA que configure un proyecto de Next.js 16 con TypeScript, Tailwind CSS y el App Router usando `create-next-app`.
- [ ] Revisa los comandos generados antes de ejecutarlos y confirma que el servidor de desarrollo arranca correctamente.
- [ ] Organiza tus carpetas: `/app` para las rutas, `/components` para las piezas de UI reutilizables, `/types` para las interfaces de TypeScript.
- [ ] Usa Tailwind CSS para todos los estilos.

### 2 — Flujo de trabajo con prompts de visión

- [ ] Haz una captura de pantalla de cada una de las tres páginas de Airbnb en un **viewport móvil (375px)**.
- [ ] Adjunta cada captura a tu agente de código con IA y pídele que genere una especificación de componentes. Tu prompt debe pedir al modelo que identifique: nombre de cada componente, sus props y su relación de layout dentro de la página.
- [ ] Documenta cada especificación generada como comentario en el código o en tu `context.md` antes de empezar a implementar esa vista.

⚠️ **IMPORTANTE:** No uses ninguna librería de componentes preconstruida (ni shadcn, ni MUI, ni Ant Design, ni Chakra). Usa solo clases de utilidad de Tailwind y tus propios componentes.

### 3 — Página de inicio (`/`)

- [ ] Implementa la barra de navegación superior: logo, campo de búsqueda e iconos del menú de usuario.
- [ ] El campo de búsqueda debe usar `useState` para guardar el texto escrito y filtrar las tarjetas visibles en tiempo real mientras el usuario escribe. La lista de tarjetas es tu estado local — actualízala en cada pulsación.
- [ ] Implementa la fila horizontal de filtros por categoría debajo de la navbar (icono + etiqueta: Playa, Mansiones, Tendencias, etc.). Usa `useState` para guardar la categoría activa y resaltarla visualmente.
- [ ] Implementa una cuadrícula responsiva de tarjetas de alojamiento. Cada tarjeta debe mostrar: placeholder de foto, título, precio por noche y valoración con estrellas.
- [ ] Usa `useEffect` para simular la carga de los datos cuando la página se monta: empieza con una lista vacía, pon un estado de carga a `true` y, tras un breve `setTimeout` (p. ej. 1 segundo), asigna los datos y marca la carga como `false`. Muestra un indicador de carga mientras los datos no estén disponibles.
- [ ] La cuadrícula debe mostrarse en una sola columna en móvil y expandirse a varias columnas en escritorio.

### 4 — Página de catálogo (`/catalog`)

- [ ] Implementa la cabecera de resultados: número de resultados y un control de ordenación (Ascendente / Descendente por precio). Usa `useState` para guardar el orden seleccionado y reordenar las tarjetas mostradas en consecuencia.
- [ ] Reutiliza el componente de tarjeta de alojamiento de la página de inicio.
- [ ] Añade un área de mapa a la derecha de la lista de tarjetas (escritorio) o debajo de las tarjetas (móvil). Por defecto, muestra un placeholder con estilo — un recuadro gris con el texto "Mapa" es suficiente.
- [ ] **Reto opcional (solo si has completado todos los demás requisitos):** Sustituye el placeholder por un mapa interactivo real usando una librería como `react-leaflet` o la API de Google Maps. Muestra cada alojamiento como un pin en el mapa usando sus coordenadas.

### 5 — Página de detalle de habitación (`/rooms/[id]`)

- [ ] Usa `useEffect` para cargar los datos de la habitación cuando el componente se monta, usando el `id` de la URL. Simula la carga con un `setTimeout` y muestra un estado de carga mientras los datos no estén disponibles.
- [ ] Implementa la galería de fotos en la parte superior. Usa `useState` para guardar el índice de la foto actualmente visible y añade botones Anterior / Siguiente para navegar por un array de placeholders de fotos.
- [ ] Implementa la cabecera del alojamiento: título, valoración con estrellas, número de reseñas y ubicación.
- [ ] Implementa la fila de información del anfitrión: placeholder de avatar, nombre del anfitrión y años como anfitrión.
- [ ] Implementa la sección de servicios (amenities) como una cuadrícula de pares icono + etiqueta.
- [ ] Implementa la tarjeta de reserva: precio por noche, un contador de huéspedes (usa `useState` para aumentar o reducir el número de huéspedes dentro de un rango mín/máx) y un botón CTA.
- [ ] **Reto opcional (solo si has completado todos los demás requisitos):** Añade campos funcionales de fecha de entrada / salida con una librería de date picker y calcula el precio total en función del número de noches seleccionadas.

### 6 — Navegación

- [ ] Al hacer clic en una tarjeta de alojamiento en la Home o en el Catálogo, debe navegar a la página de detalle.
- [ ] Usa el componente `<Link>` de Next.js para toda la navegación entre páginas.
- [ ] Incluye un botón de volver o un breadcrumb en la página de detalle que regrese al Catálogo.

⚠️ **IMPORTANTE:** Nunca uses una etiqueta `<a href="...">` plana para la navegación interna en una aplicación Next.js.

### 7 — Calidad de código

- [ ] Cada componente vive en su propio archivo dentro de `/components`.
- [ ] Ningún componente supera las ~80 líneas de JSX + lógica. Si lo hace, divídelo.
- [ ] Todos los componentes están definidos como `const` (componentes funcionales). Sin componentes de clase.

---

## ✅ Qué vamos a evaluar

- [ ] Existe un archivo `context.md` en la raíz con una descripción clara de la interfaz, sus componentes y su usuario.
- [ ] El proyecto fue configurado con Next.js 16, TypeScript, Tailwind CSS y el App Router (sin usar plantilla de inicio).
- [ ] Tres rutas están implementadas y son navegables: `/`, `/catalog` y `/rooms/[id]`.
- [ ] Toda la navegación interna usa `<Link>` — sin recargas completas de página entre vistas.
- [ ] El diseño es mobile-first: el viewport de 375px está correcto antes de aplicar ningún breakpoint de escritorio.
- [ ] El componente de tarjeta de alojamiento se reutiliza en la Home y en el Catálogo.
- [ ] `useState` se usa en al menos tres casos distintos: filtrado por búsqueda, categoría activa, orden de resultados, contador de huéspedes o índice de la galería de fotos.
- [ ] `useEffect` se usa para simular la carga de datos al montar el componente en al menos dos páginas, con un estado de carga visible mientras los datos no están disponibles.
- [ ] La página de detalle incluye las cinco secciones: galería con navegación, cabecera del alojamiento, info del anfitrión, amenities y tarjeta de reserva.
- [ ] Los componentes están divididos en archivos individuales, cada uno con una única responsabilidad.
- [ ] Sin componentes de clase — todos los componentes son funcionales y usan `const`.
- [ ] Se definen tipos o interfaces de TypeScript para las estructuras de datos principales (alojamiento, habitación).
- [ ] Las clases de utilidad de Tailwind se usan para todos los estilos — sin objetos `style={{}}` en línea.
- [ ] El flujo de visión a especificación es visible: las especificaciones derivadas de las capturas están documentadas en `context.md` o en comentarios del código.

> **Nota:** Los retos opcionales (mapa real, date picker funcional) no forman parte de la evaluación base. Están pensados para quienes terminen antes y quieran ir más lejos.

---

## 📦 Cómo entregar

Sube tu trabajo a tu repositorio de GitHub y comparte el enlace con tu instructor siguiendo sus instrucciones. Asegúrate de que el repositorio es público y de que el archivo `context.md` está en la raíz.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
