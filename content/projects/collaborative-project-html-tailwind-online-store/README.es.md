# Mi primer proyecto profesional colaborativo

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/collaborative-project-html-tailwind-online-store/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

🌐 _These guidelines are also [available in English](./README.md)_.

**Antes de empezar**:

> ¡Te necesitamos! Estos ejercicios se construyen y mantienen en colaboración con personas como tú. Si encuentras algún error 🐞 o falta de ortografía, por favor contribuye y/o repórtalos.

<!-- endhide -->

---

## 🎯 Tu reto

Estás trabajando en un pequeño equipo de desarrollo dentro de una consultora y acaba de llegar un nuevo proyecto: **una reconocida marca de ropa con sede en Francia** quiere un **prototipo visual y funcional** para su próxima tienda online.

El cliente ha sido claro con los requisitos:

- **SEO bien trabajado** (estructura semántica, contenido indexable, buenas prácticas).
- **Diseño moderno** y consistente.
- **Responsive completo**: móvil, tablet y escritorio.

Antes de avanzar a desarrollo completo, necesitan ver un prototipo que incluya **al menos 5 vistas principales**:

1. **Home**
2. **Catálogo**
3. **Vista de producto**
4. **Carrito**
5. **Formulario de pago (checkout)**

Ha llegado el momento de brillar. La consultora armó un equipo para el proyecto y te asignó a ti y a otra persona para sacarlo adelante.

### Especificaciones por vista

Tu _project manager_ te ha compartido un documento con la estructura mínima de cada vista para evitar olvidos y asegurar que el prototipo cubra lo que el cliente espera.

> #### 1) Página de inicio (Home)
>
> - **Barra superior (navbar)** con:
>   - Logo
>   - Barra de búsqueda
>   - Menú de cuenta de usuario
> - **Sección Hero** destacando productos especiales o campañas de la marca.
> - Dos secciones con listados horizontales (_cards_ de producto):
>   - **Nuevos lanzamientos**
>   - **Más vendidos**
> - **Footer** con secciones:
>   - **Categorías:** calzado, camisas, pantalones, accesorios
>   - **Legal:** términos y condiciones, política de privacidad, sobre la marca
>   - **Contacto**
> - **La navbar y el footer se reutilizan** en todas las demás vistas.
>
> #### 2) Catálogo
>
> - Mantiene **navbar y footer**.
> - Incluye una **barra de filtros** antes del listado:
>   - Filtro por **categoría**
>   - Filtro por **talla**
> - Listado de productos en **rejilla (grid) 4×5** (20 productos visibles como referencia).
>
> #### 3) Vista de producto
>
> - Diseño en dos columnas:
>   - **Izquierda:** foto del producto ocupando aproximadamente **la mitad del ancho**.
>   - **Derecha:** información principal del producto:
>     - Nombre
>     - Código o referencia
>     - Talla
>     - Precio
>     - Selector de cantidad
>     - Botón **"Agregar al carrito"**
> - Debajo, una sección de **descripción detallada**:
>   - Materiales
>   - Uso recomendado / escenarios donde se puede usar la prenda
>
> #### 4) Carrito
>
> - Vista completa del carrito (no un panel lateral).
> - Listado de productos añadidos con:
>   - Miniatura
>   - Precio unitario
>   - Cantidad
>   - Total por producto
> - Cuadro de totalización con:
>   - Subtotal
>   - Impuestos
>   - Total
>   - Botón **"Comprar"**
> - Añadir **3 productos de ejemplo** para mostrar el comportamiento visual.
>
> #### 5) Formulario de pago (Checkout)
>
> Flujo en **3 pasos**:
>
> 1. **Datos personales**
> 2. **Dirección de entrega**
> 3. **Pago con tarjeta** (datos de tarjeta)

Ahora sí: toca construir un prototipo claro, consistente y responsive que demuestre el potencial de la tienda y facilite la aprobación del cliente. **¡Manos a la obra!** 😁

> **⚠️ IMPORTANTE:** En este proyecto solo usaremos **HTML y Tailwind CSS**. Asegúrate de que tu IA Copiloto **no incluya tecnologías más avanzadas** (por ejemplo, React). Indícalo desde el inicio del trabajo.

---

## 🌱 Cómo iniciar el proyecto

Abre el repositorio de plantilla usando una herramienta de aprovisionamiento como [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recomendado) o clónalo en local:

```text
https://github.com/4GeeksAcademy/html-hello
```

Sigue los pasos en [cómo comenzar un proyecto de codificación](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion).

💡 **Importante:** Crea un nuevo repositorio en GitHub para tu código, actualiza el remoto (`git remote set-url origin <tu-nueva-url>`) y sube los cambios con `add`, `commit` y `push`.

---

## 💻 Qué debes hacer

Desarrollar el prototipo de e-commerce **en equipo**, aplicando lo visto hasta ahora: **HTML semántico**, **Tailwind**, **Schema.org**, diseño responsivo y **Git** (ramas, commits, pull requests). Usar la IA de forma ordenada y mantener el alcance en HTML + Tailwind únicamente.

**Vistas a implementar (y enlazar entre sí):**

- [ ] **Home** — navbar, Hero, listados “Nuevos lanzamientos” y “Más vendidos”, footer (navbar y footer reutilizados en todas las páginas).
- [ ] **Catálogo** — navbar, barra de filtros (categoría, talla), rejilla de productos (p. ej. 4×5), footer.
- [ ] **Vista de producto** — dos columnas (imagen + datos: nombre, código, talla, precio, cantidad, “Añadir al carrito”), sección de descripción; navbar y footer.
- [ ] **Carrito** — vista completa: listado de productos (miniatura, precio unitario, cantidad, total por línea), resumen (subtotal, impuestos, total), botón “Comprar”; p. ej. 3 productos de ejemplo para ver el comportamiento; navbar y footer.
- [ ] **Formulario de pago (checkout)** — 3 pasos: (1) Datos personales, (2) Dirección de entrega, (3) Pago con tarjeta; navbar y footer.

**Git y trabajo en equipo (Skill 5):**

- [ ] Usar **una rama por vista o funcionalidad** (p. ej. `feature/home`, `feature/catalogo`). No trabajar directamente en `main`.
- [ ] **Abrir una pull request (PR)** por cada rama antes de integrarla en `main`. Describir qué incluye la PR.
- [ ] **Actualizar tu rama** con `main` (p. ej. `git pull origin main`) antes de enviar la PR para reducir conflictos.
- [ ] **Resolver conflictos** en equipo; no hacer force-push ni sobrescribir el trabajo del otro sin consenso.
- [ ] **Hacer commits frecuentes** con mensajes claros (p. ej. “Añadir navbar y hero al home”, “Añadir rejilla y filtros al catálogo”). Mejor un cambio lógico por commit.

---

## ✅ Qué vamos a evaluar

- [ ] **HTML semántico:** Estructura y landmarks correctos; etiquetas con sentido (`<header>`, `<nav>`, `<main>`, `<section>`, `<form>`, etc.) en todas las vistas.
- [ ] **Tailwind CSS:** Uso coherente de clases utility; breakpoints responsivos (móvil, tablet, escritorio); sin frameworks ajenos al enunciado.
- [ ] **Layout y componentes:** Diagramación clara; navbar y footer reutilizados; contenido acorde a las especificaciones por vista.
- [ ] **Diseño responsivo:** Las cinco vistas usables en distintos tamaños de pantalla; sin layout roto ni scroll horizontal en móvil.
- [ ] **Schema.org:** Datos estructurados (p. ej. Product, Organization) donde aplique (p. ej. producto o home).
- [ ] **Flujo con Git:** Uso de ramas por vista/funcionalidad; al menos una PR por parte importante; commits con mensajes descriptivos; no trabajo prolongado directo en `main`.

Entregable: **al menos 5 archivos HTML** (uno por vista), enlazados entre sí, más estilos compartidos (Tailwind y CSS adicional si aplica).

---

## 📦 Cómo entregar este proyecto

Sigue los pasos habituales de entrega para subir tu repositorio a GitHub y compártelo según las indicaciones de tu instructor.

---

## Contribuidores

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/collaborative-project-html-tailwind-online-store/graphs/contributors). Descubre más sobre [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
