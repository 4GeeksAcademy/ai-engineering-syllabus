# Hito 5 — Backoffice: Interfaz de Gestión de Inventario

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/05-backend-development)** antes de escribir ningún componente — define los nombres de entidades, etiquetas de campos, restricciones de negocio y vocabulario de dominio que deben aparecer en la interfaz.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

El equipo de backend completó la API de inventario e hizo el **handoff** al equipo de producto: todos los endpoints `/inventory` están activos, autenticados y documentados. Ahora el responsable de operaciones ha enviado un **brief** a la unidad tecnológica: el personal que gestiona el stock a diario necesita una interfaz funcional dentro del backoffice. Mientras no la haya, la API existe pero nadie puede usarla sin un cliente REST.

Tu trabajo es construir la sección de inventario del backoffice: un conjunto de vistas que permitan al personal autenticado consultar el stock disponible, registrar entregas, registrar consumos o salidas y revisar el historial completo de órdenes — todo comunicándose con la API construida en el proyecto de backend.

Esta es una herramienta interna, no una página pública. Las personas que la utilizan son el personal de operaciones, no clientes. Eso condiciona cada decisión: la claridad y la velocidad importan más que el acabado visual de una campaña de marketing. Un responsable de operaciones registrando una entrega a las 7 de la mañana no tiene paciencia para un formulario roto ni para un mensaje de error críptico.

Dos requisitos del brief que es fácil pasar por alto: el formulario de orden de salida debe **mostrar el stock disponible actual** del producto seleccionado antes de que el usuario envíe el formulario, y cualquier respuesta `400` de la API debe mostrar al usuario un **mensaje de error legible** — no un objeto JSON en bruto ni un fallo silencioso.

### Brief del responsable de operaciones

> > **De:** Responsable de Operaciones
> > **Para:** Unidad Tecnológica
> >
> > El equipo de backend entregó la API de inventario el sprint pasado — buen trabajo. Ahora necesito la interfaz. Mi equipo no puede usar Postman para registrar entregas.
> >
> > Esto es lo que necesito en el backoffice:
> >
> > 1. Una página que muestre todos los productos con su stock actual. Usa código de color — quiero ver de un vistazo qué está bajo.
> > 2. Un formulario para registrar una orden de entrada (una entrega recibida).
> > 3. Un formulario para registrar una orden de salida (un consumo o salida). Debe mostrar cuánto stock hay disponible antes de que yo envíe, para no registrar más de lo que tenemos.
> > 4. Una página de sólo lectura con todas las órdenes — entradas y salidas — con el nombre del producto y quién creó cada una.
> >
> > Todas estas páginas requieren inicio de sesión. Si un usuario no está autenticado, redirígelo a la página de login.
> >
> > **Criterios de aceptación**: las cuatro vistas funcionales, autenticadas, consumiendo datos reales de la API, con gestión correcta de errores en fallos de la API.

---

## 🌱 Cómo Empezar el Proyecto

El frontend del backoffice ya existe en tu monorepo. Estás añadiendo la sección de inventario, no creando una nueva aplicación.

1. Abre tu repositorio existente (forkeado desde `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo`).
2. Navega a `uis/backoffice` — aquí vive tu Next.js backoffice.
3. Instala las dependencias si es necesario:
   ```bash
   npm install
   ```
4. Añade la URL base de la API de inventario a tu `.env.local`. Debe apuntar a tu backend en ejecución:
   ```
   NEXT_PUBLIC_INVENTORY_API_URL=http://localhost:8000
   ```
5. Lee tu **CONTEXT-company.md** — los nombres de entidades, etiquetas de campos y vocabulario de dominio deben coincidir con lo que existe en la API y en la interfaz.
6. Asegúrate de que el servicio de backend (`services/`) está ejecutándose localmente antes de probar el frontend.

---

## 💻 Qué Debes Hacer

### Capa de integración con la API

- [ ] Crea un módulo (p. ej., `lib/inventory.ts`) que centralice todas las llamadas a los endpoints `/inventory`. Ningún componente debe llamar a `fetch` directamente.
- [ ] Todas las peticiones a endpoints protegidos deben incluir la cabecera `Authorization: Bearer <token>`. Lee el token de donde tu sistema de auth existente lo almacena (localStorage, contexto, cookie).
- [ ] Gestiona los errores de la API de forma explícita: si el estado de la respuesta es `4xx` o `5xx`, extrae el mensaje de error del cuerpo de la respuesta y muéstraselo al usuario — nunca ignores los errores en silencio.

### Página de productos — `/backoffice/inventory/products`

- [ ] Obtén y muestra todos los productos desde `GET /inventory/products`.
- [ ] Muestra el valor de `current_stock` para cada producto junto con los campos específicos de entidad definidos en tu CONTEXT.md.
- [ ] Aplica indicadores visuales de nivel de stock: usa color o iconografía para distinguir el stock saludable del stock bajo. Define tus propios umbrales — documéntalos en un comentario.
- [ ] Incluye un enlace o botón claramente etiquetado en cada fila de producto para crear una orden de entrada o de salida para ese producto.

### Formulario de orden de entrada — `/backoffice/inventory/orders/inbound`

- [ ] Renderiza un formulario que envíe datos a `POST /inventory/orders/inbound`.
- [ ] El selector de producto debe listar todos los productos disponibles por nombre. No pidas al usuario que escriba un ID en bruto.
- [ ] Tras un envío exitoso, limpia el formulario y muestra un mensaje de confirmación. Ante un `400`/`500`, muestra el mensaje de error de la API en un elemento visible — no solo en la consola.
- [ ] El formulario debe estar protegido: redirige a los usuarios no autenticados a la página de login.

### Formulario de orden de salida — `/backoffice/inventory/orders/outbound`

- [ ] Renderiza un formulario que envíe datos a `POST /inventory/orders/outbound`.
- [ ] Cuando el usuario selecciona un producto, obtén y muestra su `current_stock` antes de que introduzca una cantidad. Esto debe actualizarse de forma reactiva cuando cambia la selección de producto.
- [ ] Si la cantidad introducida supera el stock mostrado, muestra una advertencia en el cliente antes de que el usuario envíe. Esto es una salvaguarda de UX — la API aplica la regla real.
- [ ] Gestiona el `HTTP 400` de la API (stock insuficiente) mostrando el mensaje de error inline junto al campo de cantidad.

### Página de historial de órdenes — `/backoffice/inventory/orders`

- [ ] Obtén y muestra todas las órdenes desde `GET /inventory/orders`.
- [ ] Cada fila debe mostrar: nombre del producto, cantidad, tipo de orden (entrada o salida), fecha de creación y el `user_uuid` que la creó.
- [ ] Muestra las órdenes de entrada y de salida con una distinción visual (p. ej., color, icono o etiqueta).
- [ ] Esta página es de sólo lectura. Sin acciones de borrado ni edición.

### Protección de rutas

- [ ] Las cuatro páginas de inventario deben redirigir a los usuarios no autenticados a la página de login. Usa el mismo patrón de comprobación de auth ya presente en el backoffice.

⚠️ **IMPORTANTE:** Los nombres de entidades, etiquetas de campos y el vocabulario de la interfaz deben coincidir con lo especificado en tu CONTEXT.md — usa el lenguaje de dominio de tu empresa, no los términos genéricos de este README.

---

## ✅ Qué Vamos a Evaluar

- [ ] Existe un módulo de integración con la API dedicado — no hay llamadas `fetch` directas dentro de los componentes.
- [ ] Todas las peticiones a endpoints protegidos incluyen la cabecera `Authorization` con el token del usuario actual.
- [ ] La página de productos carga datos reales de la API y muestra `current_stock` con indicadores visuales de nivel de stock.
- [ ] El formulario de orden de entrada envía correctamente y muestra una confirmación o un mensaje de error legible en cada resultado — sin fallos silenciosos.
- [ ] El formulario de orden de salida muestra el stock actual del producto seleccionado de forma reactiva, antes de que el usuario envíe.
- [ ] El formulario de orden de salida muestra una advertencia en el cliente cuando la cantidad introducida supera el stock disponible.
- [ ] Una respuesta `400` del endpoint de salida muestra el mensaje de error de la API de forma visible en la interfaz.
- [ ] La página de historial de órdenes muestra todas las órdenes con distinción entrada/salida, nombre de producto, cantidad, fecha y `user_uuid`.
- [ ] Las cuatro páginas redirigen a los usuarios no autenticados al login.
- [ ] Los nombres de entidades y etiquetas de campos en la interfaz coinciden con la especificación del CONTEXT.md.

---

## 📦 Cómo Entregar

1. Confirma y sube todos los cambios a tu fork.
2. Verifica que `.env.local` está en `.gitignore` — nunca subas URLs de API ni tokens.
3. Envía la URL de tu fork a través de la plataforma del estudiante.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
