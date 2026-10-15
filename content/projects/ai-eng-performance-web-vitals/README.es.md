# Auditoría de Rendimiento Frontend

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/frontend-performance-audit/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de código.

<!-- endhide -->

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

El sitio corporativo y el backoffice de tu empresa están en producción. El equipo está satisfecho con las funcionalidades, pero el CTO acaba de dejar un mensaje en el canal de desarrollo: el equipo debería buscar mejoras de rendimiento — tanto para apoyar un mejor SEO en el sitio corporativo como para asegurar que el backoffice funcione bien para las personas que lo usan a diario. Antes del siguiente hito, necesitas auditar ambos frontends, identificar qué está arrastrando el rendimiento, aplicar las correcciones necesarias y documentar todo con el rigor que se espera en un codebase profesional.

Esto no se trata de hacer las cosas más bonitas. Se trata de hacerlas rápidas, medibles y mantenibles.

Una buena auditoría de rendimiento sigue un ciclo claro: **medir → analizar → corregir → volver a medir**. Ejecutarás Lighthouse antes de tocar una sola línea de código, luego revisarás el codebase para identificar qué puede mejorarse — incluyendo componentes o lógica que aparecen más de una vez y deberían extraerse en unidades reutilizables. Instalarás un conjunto de skills de agente diseñadas específicamente para guiar la corrección de problemas de web vitals, aplicarás las correcciones que recomienden, y cerrarás el ciclo con una segunda ejecución de Lighthouse para validar el trabajo realizado.

> Tu CTO ha dejado la siguiente nota en el gestor de tareas del equipo:
>
> #### Auditoría de rendimiento — ambos frontends
>
> - Ejecuta Lighthouse en el sitio corporativo y en el backoffice. Registra las puntuaciones iniciales (Performance, Accessibility, Best Practices, SEO).
> - Revisa el codebase. Identifica componentes o bloques de lógica que estén duplicados entre archivos y puedan refactorizarse en un componente compartido o un Custom Hook.
> - En caso de necesitarlo, puedes instalar alguna de las siguientes skills de agente para guiar el proceso de corrección:
>   - [core-web-vitals](https://www.skills.sh/addyosmani/web-quality-skills/core-web-vitals)
>   - [performance](https://www.skills.sh/addyosmani/web-quality-skills/performance)
>   - [web-perf (Cloudflare)](https://www.skills.sh/cloudflare/skills/web-perf)
> - Aplica las correcciones que las skills identifiquen como necesarias.
> - Entregables:
>   - Un archivo `AUDIT.md` con el análisis: puntuaciones iniciales, problemas identificados y causa raíz de cada uno.
>   - Un archivo `REPORT.md` con las mejoras aplicadas y su impacto medido sobre las puntuaciones originales.
>   - Capturas de pantalla de Lighthouse antes y después de los cambios, con commit en el repositorio.

El objetivo no es un 100 perfecto. El objetivo es un ciclo de mejora documentado y basado en evidencia — el mismo que repetirás a lo largo de toda tu carrera cada vez que pongas en producción un frontend.

---

### ¿Qué hace útil una auditoría de Lighthouse?

Lighthouse analiza **una página a la vez** — no recorre toda la aplicación. Una sola ejecución en la página de inicio no dice nada sobre el rendimiento de una vista de dashboard con carga intensiva de datos. Al auditar una aplicación con múltiples vistas, ejecuta Lighthouse en las páginas que más importan: aquellas con mayor complejidad visual, más componentes renderizados a la vez, o mayor tráfico de usuarios. En el sitio corporativo suelen ser la home y cualquier página con mucho contenido; en el backoffice, normalmente el dashboard principal o cualquier vista con tablas, gráficos o datos en tiempo real.

Lighthouse te entrega cuatro puntuaciones: **Performance**, **Accessibility**, **Best Practices** y **SEO**. Para un frontend en producción, los benchmarks que más importan son:

- **Performance ≥ 90** — Por debajo de 50 se considera deficiente y afecta a usuarios reales en redes móviles.
- **LCP (Largest Contentful Paint) < 2.5s** — Tiempo hasta que el contenido principal es visible.
- **CLS (Cumulative Layout Shift) < 0.1** — Movimiento inesperado del layout durante la carga.
- **FID / INP (Interaction to Next Paint) < 200ms** — Capacidad de respuesta a la interacción del usuario.
- **TTFB (Time to First Byte)** — Tiempo hasta que el servidor empieza a enviar la respuesta HTML.

Un informe completo de Lighthouse puede resultar abrumador las primeras veces — decenas de auditorías, oportunidades y diagnósticos en una sola pantalla. **No intentes corregir todo de golpe.** Una forma práctica de recorrerlo:

1. **Empieza por los indicadores principales** — las cuatro puntuaciones Core Web Vitals más las señales de servidor como **TTFB**, **LCP**, **CLS** e **INP**. Te dicen _dónde_ duele (red, render, layout, interactividad) antes de entrar en cada sub-auditoría.
2. **Apóyate en el agente de IA como tutor** — pega o describe una métrica cada vez y pregunta qué mide, qué se considera “bueno” y qué correcciones suelen moverla. Paso a paso: entiende el indicador y luego las acciones recomendadas para _tu_ stack (Next.js, imágenes, fuentes, hidratación, etc.).
3. **Resuelve un caso por commit** — elige el KPI de mayor impacto, aplica un cambio dirigido, haz commit con un mensaje claro, vuelve a ejecutar Lighthouse en la misma URL y anota la diferencia. Repite hasta que los KPI principales estén en rango saludable.
4. **Después aborda lo complementario** — avisos de accesibilidad, best practices, oportunidades de SEO y auditorías de menor prioridad importan, pero _después_ de las métricas que afectan de verdad a usuarios en dispositivos lentos.

Causas habituales que los estudiantes pasan por alto: imágenes sin optimizar, recursos que bloquean el render, layout shifts por atributos `width`/`height` ausentes en imágenes, fuentes cargadas sin `display: swap`, y problemas de hidratación en Next.js.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no utiliza una nueva plantilla de inicio. Trabajas dentro de tu monorepo de empresa existente.

1. Abre tu monorepo en Codespaces o clónalo localmente.
2. Compila y sirve **ambos** frontends en **modo producción** antes de cualquier ejecución de Lighthouse. En cada aplicación (o con los scripts del monorepo), ejecuta el build de producción y arranca el servidor de producción — normalmente `npm run build` y después `npm run start` (o el equivalente del monorepo). **No** audites con `npm run dev` / `next dev`: el modo desarrollo sesga las métricas (sin minify real, Strict Mode, HMR, etc.) y oculta mejoras reales. Next.js indica que los informes precisos requieren una compilación de producción.
3. Abre Chrome o Brave — Lighthouse está disponible de forma nativa en las DevTools (pestaña Lighthouse).
4. Toma tus primeras capturas de pantalla antes de modificar nada.

---

## 💻 Qué debes hacer

### Medición inicial

⚠️ **IMPORTANTE:** Todas las ejecuciones de Lighthouse (antes y después) deben hacerse contra el servidor de **producción** (`build` + `start`). Un informe tomado con `npm run dev` no es válido para este proyecto.

- [ ] Ejecuta Lighthouse en el sitio corporativo en modo **escritorio y móvil** — como mínimo en la página de inicio, más cualquier otra vista que consideres suficientemente compleja para auditar. Registra las cuatro puntuaciones por página y por modo.
- [ ] Ejecuta Lighthouse en el backoffice — como mínimo en el dashboard principal o la vista con más elementos. Registra las cuatro puntuaciones por página.
- [ ] Toma capturas de pantalla de ambos informes y realiza un commit en la carpeta `/audit/before/` del repositorio.

### Análisis del código

- [ ] Revisa ambos frontends e identifica al menos dos casos en los que un componente o bloque de lógica se repita y pueda extraerse en un componente compartido o un Custom Hook.
- [ ] Documenta cada caso en `AUDIT.md`: dónde aparece, por qué es candidato a refactorización y cómo quedaría la abstracción compartida.

### Instalación de skills de agente

- [ ] En caso de necesitarlo, instala una o más de las skills de agente indicadas por el CTO:
  - `https://www.skills.sh/addyosmani/web-quality-skills/core-web-vitals`
  - `https://www.skills.sh/addyosmani/web-quality-skills/performance`
  - `https://www.skills.sh/cloudflare/skills/web-perf`
- [ ] Ejecuta el agente sobre ambos frontends y registra las correcciones que identifica.

### Correcciones

- [ ] Prioriza los KPI principales (TTFB, LCP, CLS, INP, puntuación de Performance) antes que auditorías secundarias de Lighthouse; usa el agente para interpretar un indicador cada vez.
- [ ] Aplica correcciones de forma incremental — **un problema por commit**, y vuelve a ejecutar Lighthouse en la misma URL tras cada cambio para confirmar el impacto.
- [ ] Aplica las correcciones que las skills de agente clasifiquen como correcciones requeridas (no sugerencias).
- [ ] Aplica las refactorizaciones identificadas durante el análisis del código — extrae al menos un componente reutilizable o Custom Hook.

### Medición final

- [ ] Vuelve a ejecutar Lighthouse en ambos frontends tras las correcciones.
- [ ] Toma nuevas capturas de pantalla y realiza un commit en `/audit/after/`.

### Entregables

- [ ] Escribe `AUDIT.md` con: puntuaciones iniciales de Lighthouse, problemas identificados con explicación de causa raíz para cada uno, y el análisis de refactorización.
- [ ] Escribe `REPORT.md` con: descripción de cada corrección aplicada, comparativa de puntuaciones antes/después, y tu valoración de qué tuvo mayor impacto.
- [ ] Realiza un commit de ambos archivos markdown y todas las capturas de pantalla en el repositorio.

⚠️ **IMPORTANTE:** No reestructures la arquitectura de ninguno de los frontends para pasar esta auditoría. Aplica correcciones dirigidas. El objetivo es la mejora, no una reescritura.

---

## ✅ Qué vamos a evaluar

- [ ] Lighthouse se ejecutó en ambos frontends antes y después **en modo producción** (`build` + `start`, no `dev`), con capturas de pantalla con commit en el repositorio.
- [ ] `AUDIT.md` identifica problemas concretos con razonamiento sobre causa raíz — no solo una lista de lo que Lighthouse marcó.
- [ ] Al menos un componente reutilizable o Custom Hook fue extraído e integrado en el codebase.
- [ ] `REPORT.md` muestra una mejora medible en al menos una puntuación de Lighthouse por frontend.
- [ ] Si se instalaron skills de agente, hay evidencia de su uso en el proceso de corrección.
- [ ] Las correcciones aplicadas atacan causas reales (optimización de imágenes, layout shift, problemas de hidratación) y no cambios superficiales que inflan las puntuaciones sin resolver el problema subyacente.
- [ ] La calidad del código se mantiene tras la refactorización — sin funcionalidades rotas ni regresiones.

> Nota: Obtener una puntuación de 100 no es un criterio de evaluación. La mejora basada en evidencia y la calidad del análisis sí lo son.

---

## 📦 Cómo entregar

Sube tus cambios a tu monorepo de empresa en GitHub y comparte la URL del repositorio según las instrucciones de tu instructor. Asegúrate de que `AUDIT.md`, `REPORT.md` y la carpeta `/audit/` con todas las capturas de pantalla estén incluidos en el commit final.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/frontend-performance-audit/graphs/contributors). Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
