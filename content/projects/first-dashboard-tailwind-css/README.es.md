# Un dashboard sencillo en Tailwind CSS

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/first-dashboard-tailwind-css/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

🌐 _These guidelines are also [available in English](./README.md)_.

**Antes de empezar**:

> ¡Te necesitamos! Estos ejercicios se construyen y mantienen en colaboración con personas como tú. Si encuentras algún error 🐞 o falta de ortografía, por favor contribuye y/o repórtalos.

<!-- endhide -->

---

## 🎯 Tu reto

Una influencer que está empezando a relacionarse con marcas te contacta porque necesita medir el impacto de sus anuncios y su conversión. El problema es que tiene múltiples cuentas en redes sociales (Instagram, TikTok, YouTube, etc.) y necesita entender cómo puede consolidar toda la información en un tablero de reporte para responder preguntas básicas como:

- ¿Cuánto dinero estoy generando en comisiones?
- ¿Qué productos están generando más ingresos?
- ¿Qué tan bien convierten mis anuncios (conversiones / alcance)?
- ¿Qué plataformas están generando mejor retorno (ingresos/costes)?
- ¿Cuál es el _engagement rate_ por plataforma y por producto?

La influencer te contacta porque necesita un reporte claro (un dashboard) que le permita supervisar su negocio sin perderse en datos dispersos entre múltiples plataformas. Y tú, aunque estás empezando, quieres entregar una propuesta sólida y profesional, así que tu misión es diseñar un dashboard que consolide la información de todas sus redes sociales y le muestre lo más importante para tomar decisiones rápidas.

**Contexto del negocio:**

- Tiene 3 productos que promociona con tres precios distintos (Producto A: 50€, Producto B: 120 €, Producto C: 80 €)
- Por cada venta generada recibe una comisión del 15%

---

### ¿Qué hace que un dashboard sea “bueno”?

Organiza el dashboard en grandes bloques:

**1️⃣ Bloque superior:** Indicadores principales del resultado (KPI):

- **Volumen:** ventas, inscripciones, usuarios activos, impresiones
- **Ingresos:** revenue (comisiones, ventas), MRR (facturación mensual recurrente en suscripciones), precio medio de venta
- **Engagement:** tasa de _engagement_, interacciones totales, tasa de conversión
- **Retención:** churn (tasa de bajas), permanencia, tasa de compleción del proceso de venta o suscripción
- **Rendimiento:** conversiones totales, tasa de clics (CTR), tasa de conversión
- **Satisfacción:** puntuación de lealtad (NPS), puntuación de satisfacción (CSAT)
- **Eficiencia:** coste por resultado, margen, tiempos

**2️⃣ Bloque intermedio:** “Drivers” (factores que explican el resultado):

- **Conversión** por etapas (funnel de ventas)
- **Rendimiento por plataforma** (Instagram, TikTok, YouTube, etc.)
- **Calidad** (ratio de leads cualificados, _attendance rate_, _pass
  rate_)
- **Rendimiento por producto** (qué producto genera más comisiones y mejor conversión)
- **Actividad** (posts publicados, stories, reels, videos por plataforma)
- **Engagement** (me gusta, comentarios, compartidos, guardados por plataforma)

**3️⃣ Bloque inferior:** Detalles operacionales (tablas/listados, alertas):

- Tabla de productos: precio, comisiones generadas, conversiones, ROI por producto
- Tabla de plataformas: alcance, engagement, conversiones, mejor plataforma por métrica
- Tabla de campañas: fechas, productos promocionados, resultados, rendimiento
- Alertas: caídas fuertes en conversión, picos de conversión, anomalías en el rendimiento
- Listados con filtros: “top productos”, “top plataformas", "top campañas", "oportunidades de mejora”

> Ejemplo visual de dashboard administrativo:

![Ejemplo de dashboard](images/image1.png "Dashboard ejemplo")

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

Construye un dashboard que muestre al menos **tres KPIs**, **tres drivers** y **detalles operacionales** (tablas o listados) en los tres bloques descritos arriba. Debe verse y usarse bien en **móvil, tablet y escritorio** (al menos tres breakpoints; diseña **mobile-first**).

- [ ] **Planificar el layout:** Definir la estructura principal: navbar/cabecera o sidebar, y cómo se divide el contenido (bloque superior = KPIs, intermedio = drivers, inferior = tablas/listados). Pensar en **componentes reutilizables** (cards, cajas de widget, tablas) y estructura por secciones.
- [ ] **Diseño mobile-first:** Empezar por la pantalla más pequeña; luego adaptar con breakpoints de Tailwind (`sm:`, `md:`, `lg:`) para que los mismos componentes funcionen en tablet y escritorio. Evitar tamaños en píxeles; usar utilidades de espaciado y tamaño de Tailwind.
- [ ] **HTML semántico:** Usar etiquetas adecuadas (`<header>`, `<nav>`, `<main>`, `<section>`, `<table>`, etc.) para que el dashboard tenga un esquema de documento claro.
- [ ] **Solo Tailwind:** Aplicar estilos con clases utility de Tailwind (y Preflight si usas el build de Tailwind). No mezclar otros frameworks CSS ni CSS personalizado, salvo Chart CSS si lo usas para gráficos.
- [ ] **Gráficos (opcional):** Para KPIs o drivers puedes usar [Chart CSS](https://chartscss.org/) (solo CSS). Los datos pueden ser de ejemplo; importa la jerarquía visual y la legibilidad.
- [ ] **Consistencia:** Reutilizar los mismos patrones para elementos similares (p. ej. todas las cards de KPI comparten la misma estructura y estilo).

⚠️ **IMPORTANTE:** En este proyecto solo se usa **HTML y Tailwind CSS**. Indica a tu IA Copiloto que **no use otras tecnologías** (p. ej. React, Vue). Dilo desde el inicio.

---

## ✅ Qué vamos a evaluar

- [ ] **HTML semántico:** Uso correcto de etiquetas estructurales y landmarks; jerarquía clara y lógica.
- [ ] **Tailwind CSS:** Estilos aplicados con clases utility; sin CSS personalizado contradictorio o redundante; uso adecuado de breakpoints y utilidades de layout (flex/grid).
- [ ] **Layout y componentes:** Separación clara de los tres bloques (KPIs, drivers, operativo); agrupación y jerarquía visual coherentes; componentes con aspecto reutilizable (cards, secciones, tablas).
- [ ] **Diseño responsivo:** Uso correcto en al menos tres tamaños de dispositivo (p. ej. móvil, tablet, escritorio); enfoque mobile-first; sin scroll horizontal ni layout roto en pantallas pequeñas.

> Nota: No se valora si los KPIs o drivers elegidos son “correctos” para el negocio; se evalúa la estructura, el uso de Tailwind y la responsividad.

---

## 📦 Cómo entregar este proyecto

Debes entregar un repositorio que incluya el documento HTML con toda la estructura y el CSS con los estilos y las media queries necesarias para adaptar el dashboard a los distintos _breakpoints_.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) y [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack).
