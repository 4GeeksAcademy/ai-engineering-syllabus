# Plataforma de Alquiler de Agentes IA — Prototipo de Panel de Administración

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeks.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/how-to-start-a-coding-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una startup llamada **AgentHub** está construyendo una plataforma SaaS donde las empresas pueden alquilar agentes de IA — asistentes inteligentes preconfigurados que pueden equiparse con distintas skills (habilidades como navegar por la web, leer documentos o gestionar calendarios) y desplegarse para tareas de negocio específicas.

El equipo fundador tiene un backend funcional y una idea aproximada de cómo debería ser su panel de administración interno, pero nadie tiene tiempo para construirlo. Te han contratado como desarrollador frontend freelance. Tu primer entregable es un **prototipo HTML completamente diseñado** del panel de administración — algo que el equipo pueda revisar, validar y entregar a los desarrolladores de backend más adelante.

Antes de escribir una sola línea de HTML, tendrás que producir un **documento de especificación** — una descripción estructurada de lo que vas a construir, escrita con suficiente detalle como para que un agente de código IA (u otro desarrollador) pueda implementarlo desde cero sin hacer preguntas. Esto sigue un enfoque de **Vision to spec**: defines el qué y las reglas antes de empezar a construir. La spec no es un trámite — es tu contrato con el código.

El equipo de producto ha compartido el siguiente briefing:

> #### Requisitos del Panel de Administración — AgentHub
>
> El panel debe incluir las siguientes seis secciones, accesibles desde una navegación lateral persistente. Un toggle en la barra superior debe permitir cambiar toda la interfaz entre modo claro y modo oscuro usando las utilidades `dark:` de Tailwind.
>
> **1. Dashboard**
> De un vistazo, el administrador debe poder ver: ingresos totales generados (este mes), pérdida total por descuentos y cupones, número de agentes activos en todos los clientes, y número de agentes actualmente marcados como fallando. Cada uno de estos debe ser una tarjeta de métrica visible. Debajo de las tarjetas, incluye un área de marcador de posición para un gráfico de actividad semanal.
>
> **2. Gestión de usuarios**
> Una tabla que lista todos los usuarios registrados (nombre, email, plan, estado). Cada fila debe tener un dropdown de acciones — un pequeño menú activado con un botón `⋮` — con al menos dos opciones: "Ver detalle" y "Eliminar". Al elegir "Ver detalle" se abre un modal overlay con el registro completo del usuario. El modal debe cerrarse mediante un botón y haciendo clic en el backdrop.
>
> **3. Gestión de agentes**
> Un listado de todos los agentes registrados en la plataforma, mostrando nombre del agente, propietario, estado actual (activo / inactivo / fallando) y una lista de skills colapsada. Las skills asociadas a cada agente están ocultas por defecto; hacer clic en un control expandible las revela con una transición suave. Cada agente también tiene un dropdown de acciones con las opciones "Configurar" — que abre un modal con el prompt de sistema del agente — y "Eliminar".
>
> **4. Skills**
> Una sección dedicada al catálogo de skills disponibles — las capacidades que se pueden adjuntar a los agentes. Cada skill tiene un nombre, una descripción breve, y un indicador de cuántos agentes la tienen habilitada actualmente. Incluye una breve explicación dentro del panel sobre qué significa una "skill" en el contexto de AgentHub. Las skills también tienen un dropdown de acciones con "Ver detalle" y "Eliminar".
>
> **5. Contrataciones de agentes**
> Una tabla que muestra todos los contratos de alquiler activos y pasados. Cada fila debe mostrar el cliente, el agente alquilado, las skills contratadas, las fechas del contrato y el importe total pagado. Cada fila tiene un dropdown de acciones. Al elegir "Ver detalle" se abre un modal con el desglose completo del contrato, incluyendo la lista desglosada de skills contratadas y sus precios individuales.
>
> **6. Log de errores**
> Un registro de errores de ejecución de los agentes — mostrando timestamp, nombre del agente, tipo de error y una descripción breve. Los errores deben categorizarse visualmente por tipo o gravedad usando badges con código de color. Cada entrada tiene un dropdown de acciones con "Ver detalle" (abre un modal con la traza completa del error) y "Marcar como resuelto".

El panel debe sentirse profesional e inmediatamente utilizable como referencia para el desarrollo futuro. Todos los datos deben estar hardcodeados — el equipo no espera conexiones a API ni backend en esta etapa.

**Tu trabajo es escribir la especificación primero, commitearla al repositorio, y luego construir el prototipo contra ella.**

---

## 🌱 Cómo iniciar el proyecto

1. Haz fork del repositorio plantilla: [https://github.com/4GeeksAcademy/html-hello](https://github.com/4GeeksAcademy/html-hello)
2. Crea tu propio repositorio en GitHub y actualiza la URL del remote para que apunte a él.
3. Abre el proyecto en GitHub Codespaces o clónalo localmente.
4. Lee el briefing completo con atención antes de escribir la especificación.
5. Cuando tengas un primer borrador de `SPECS.md`, usa esas specs como prompt en [Google Stitch](https://stitch.withgoogle.com/) para obtener una propuesta visual inicial del panel.
6. Toma esa propuesta visual como referencia y adáptala manualmente para cumplir todos los requisitos del proyecto.
7. ¿Necesitas ayuda para empezar? [Sigue estas instrucciones](https://4geeks.com/es/lesson/how-to-start-a-coding-project).

---

## 💻 Qué debes hacer

### Escribe la especificación primero

- [ ] Crea un archivo llamado `SPECS.md` en la raíz del repositorio.
- [ ] En `SPECS.md`, escribe una especificación estructurada que incluya:
  - [ ] Una breve descripción del producto (qué es AgentHub y quién es el usuario administrador).
  - [ ] El stack tecnológico y las restricciones (HTML, Tailwind vía CDN, solo JS vanilla, sin frameworks, sin backend).
  - [ ] **Al menos 3 especificaciones por sección** — cada una describiendo un requisito visual o interactivo concreto para esa vista. Una buena entrada de spec nombra un componente, describe su contenido y define su comportamiento. Por ejemplo, para el Dashboard: _(1) cuatro tarjetas de métricas en una cuadrícula responsive 2×2, cada una con un icono, una etiqueta y un valor hardcodeado; (2) las tarjetas usan colores de acento distintos por tipo de métrica e incluyen una sombra sutil; (3) debajo de las tarjetas, un div de ancho completo con borde discontinuo y una etiqueta centrada representa el gráfico de actividad semanal._ Aplica este nivel de detalle a las seis secciones.
  - [ ] Un inventario de componentes: una lista de los componentes de UI reutilizables que aparecen en varias secciones (sidebar, tarjeta de métrica, dropdown de acciones, modal, badge, lista de skills colapsable, toggle de modo oscuro).
  - [ ] Criterios de aceptación: una lista numerada de condiciones verificables que deben cumplirse para que el prototipo se considere completo — incluye al menos un criterio por comportamiento interactivo (dropdown, modal, colapsable, modo oscuro).
- [ ] Commitea `SPECS.md` al repositorio **antes** de comenzar cualquier trabajo en HTML.
- [ ] Usa el contenido de `SPECS.md` para generar una propuesta visual en [Google Stitch](https://stitch.withgoogle.com/) y úsala como guía de diseño (no como entrega final).

> ⚠️ **IMPORTANTE:** La especificación debe estar commiteada antes del primer archivo HTML. Usa un commit separado para la spec — se revisará el historial de Git. Un agente de código IA debería poder leer tu `SPECS.md` y construir el panel desde él sin hacer ninguna pregunta. Ese es tu estándar de calidad.
>
> ⚠️ **IMPORTANTE:** La propuesta visual de Stitch es solo un punto de partida. Debes adaptar estructura, componentes e interacciones para que coincidan exactamente con los requisitos de este proyecto.

### Construye el prototipo

- [ ] Construye el panel de administración como un único archivo `index.html` (o varios archivos HTML enlazados, uno por sección).
- [ ] Usa **Tailwind CSS vía CDN** para todos los estilos — sin archivos CSS personalizados, sin atributos `style` en línea.
- [ ] Implementa una **barra lateral (sidebar)** persistente con enlaces de navegación a las seis secciones y un indicador de sección activa.

#### Dashboard

- [ ] Cuatro tarjetas de métricas (ingresos totales, pérdidas por descuentos, agentes activos, agentes fallando), cada una con un icono, una etiqueta y un valor hardcodeado.
- [ ] Un área de ancho completo debajo de las tarjetas que representa un gráfico de actividad semanal.

#### Gestión de usuarios

- [ ] Una tabla con al menos 5 filas de usuarios hardcodeados mostrando nombre, email, plan y badge de estado.
- [ ] Cada fila tiene un dropdown `⋮` con "Ver detalle" y "Eliminar".
- [ ] "Ver detalle" abre un modal con el registro completo del usuario. El modal se cierra con el botón de cierre y haciendo clic en el backdrop.

#### Gestión de agentes

- [ ] Un listado con al menos 4 agentes, cada uno mostrando nombre, propietario, badge de estado y una lista de skills colapsada.
- [ ] Hacer clic en el control expandible revela las skills del agente con una transición suave; volver a hacer clic las colapsa.
- [ ] Cada agente tiene un dropdown `⋮` con "Configurar" y "Eliminar". "Configurar" abre un modal con el prompt de sistema del agente en un `<textarea>` editable.

#### Skills

- [ ] Un catálogo de al menos 4 skills, cada una mostrando nombre, descripción y el número de agentes que la tienen habilitada.
- [ ] Una breve explicación dentro del panel sobre qué es una "skill" en el contexto de AgentHub.
- [ ] Cada skill tiene un dropdown `⋮` con "Ver detalle" y "Eliminar".

#### Contrataciones de agentes

- [ ] Una tabla con al menos 4 contratos mostrando cliente, agente, skills contratadas, fechas de inicio/fin e importe pagado.
- [ ] Cada fila tiene un dropdown `⋮`. "Ver detalle" abre un modal con el desglose completo del contrato, incluyendo skills desglosadas y sus precios individuales.

#### Log de errores

- [ ] Al menos 6 entradas de error hardcodeadas mostrando timestamp, nombre del agente, badge de tipo de error con código de color, y descripción breve.
- [ ] Cada entrada tiene un dropdown `⋮` con "Ver detalle" y "Marcar como resuelto".

#### Interacciones globales

- [ ] Un toggle de modo oscuro/claro en la barra superior cambia todo el panel entre esquemas de color usando las utilidades `dark:` de Tailwind. El modo elegido se conserva al navegar entre secciones.
- [ ] Todos los dropdowns de acciones se cierran al hacer clic fuera de su área.
- [ ] Todos los modales se cierran al hacer clic en el backdrop.

> ⚠️ **IMPORTANTE:** Toda la interactividad debe implementarse con **JavaScript vanilla** únicamente — sin frameworks (React, Vue, etc.), sin jQuery, sin herramientas de build. Tailwind debe cargarse solo vía CDN.

---

## ✅ Qué vamos a evaluar

- [ ] `SPECS.md` fue commiteado antes de cualquier archivo HTML (verificado mediante el historial de Git).
- [ ] La spec contiene al menos 3 especificaciones concretas por sección, un inventario de componentes y una lista numerada de criterios de aceptación.
- [ ] Las seis secciones del panel están presentes y son accesibles desde la barra lateral.
- [ ] Las clases utilitarias de Tailwind se usan de forma consistente en todo el proyecto — sin estilos en línea, sin archivos CSS externos.
- [ ] Todas las filas de los listados tienen un dropdown `⋮` funcional que se abre, se cierra al hacer clic y se cierra al hacer clic fuera.
- [ ] "Ver detalle" abre un modal en al menos cuatro secciones diferentes.
- [ ] Los modales se cierran con el botón de cierre y con clic en el backdrop.
- [ ] Las listas de skills de los agentes están colapsadas por defecto y se expanden/colapsan al hacer clic con una transición visible.
- [ ] El toggle de modo oscuro/claro cambia todo el panel y el estado se mantiene entre secciones.
- [ ] Los datos hardcodeados son consistentes entre secciones (el mismo nombre de agente aparece en Gestión de agentes, Contrataciones y Log de errores).
- [ ] El HTML usa etiquetas semánticas correctamente — `section`, `table`, `nav`, `header`, `main` y similares.
- [ ] El layout es usable en viewports de escritorio y tablet.

> Nota: El envío de formularios, la búsqueda en vivo y la navegación real entre páginas no se evalúan. Los comportamientos interactivos descritos arriba — dropdowns, modales, colapsables, modo oscuro — son obligatorios y se comprobarán manualmente.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace según las instrucciones de tu instructor. Asegúrate de que el repositorio sea público y de que tanto `SPECS.md` como los archivos HTML estén commiteados y visibles.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeks.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeks.com/es/comparar-programas) de [Ingeniería de IA](https://4geeks.com/es/programas-de-carrera/ingenieria-ia) y [Agentes y Automatizaciones con IA](https://4geeks.com/es/programas-de-carrera/agentes-y-automatizaciones-con-inteligencia-artificial).
