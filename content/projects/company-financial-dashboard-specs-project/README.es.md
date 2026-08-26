# Aplicando desarrollo guiado por especificaciones - Dashboard financiero

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Continúas en el **mismo dashboard financiero heredado** del proyecto de contexto. El equipo de finanzas del cliente pide tres capacidades nuevas. Antes de que nadie construya un componente, tu tech lead para al equipo:

> **"Primero la especificación. Luego construimos."**

Una especificación bien escrita define qué ve el usuario, qué datos necesita cada componente y qué reglas rigen cada campo. Si la spec es clara, cualquier desarrollador — o coding agent — puede implementarla sin hacerte preguntas.

**Stack-agnostic se refiere a tu conocimiento previo, no al stack del proyecto.** Este repo tiene frontend y backend predefinidos. **No** necesitas dominar ya interfaces TypeScript, OpenAPI ni cada nombre de campo de la API. Tu coding agent explora `/docs` y los patrones frontend existentes; tú lo diriges, verificas cada tipo y regla contra evidencia de la API en vivo y rechazas suposiciones.

### Cómo trabajas (en cada fase)

1. Pide al agent que explore `/docs` y el código frontend relevante antes de redactar specs.
2. Por funcionalidad, pasa el outcome del PM como prompt — deja que el agent proponga tipos, componentes y casos límite.
3. Marca afirmaciones de API ✅ verificadas en `/docs` / ❌ incorrectas / ❓ sin verificar; corrige con el agent.
4. Haz commit de artefactos de spec solo después de verificar — commits separados para tipos, componentes y contrato de datos son ideales.
5. **No** implementes componentes React ni llamadas a la API en este proyecto.

> Tu product manager compartió las siguientes solicitudes de funcionalidad:
>
> ---
>
> #### Funcionalidad 1 — Filtro de rango de fechas en el dashboard principal
>
> El equipo de finanzas quiere centrarse en períodos concretos sin ver todos los datos históricos a la vez. Añade dos inputs de fecha en la parte superior del dashboard — una fecha de inicio y una fecha de fin — que filtren todos los datos que se muestran actualmente en la página. Las fechas se envían a la API en formato `YYYY-MM-DD`. Ambos inputs son opcionales; cuando están vacíos, el dashboard muestra todos los datos disponibles. El rango de fechas disponible (la fecha más antigua y la más reciente del dataset) debe mostrarse cerca de los inputs como referencia para que el usuario sepa qué rango es válido.
>
> Endpoint relevante: `GET /api/metrics/facets` (para obtener el rango de fechas disponible) y la extensión de filtros sobre el endpoint de métricas existente.
>
> ---
>
> #### Funcionalidad 2 — Tabla de alertas de anomalías en el dashboard principal
>
> Bajo los gráficos existentes, añade una tabla que destaque los períodos en los que el gasto subió de forma inesperada. La tabla tiene cuatro columnas: período, outcome registrado, media móvil de los 3 períodos anteriores e incremento porcentual. El umbral de alerta es configurable por el usuario mediante un input numérico (un ratio entre `0.01` y `1.0`, por defecto `0.3`). Si no se detectan anomalías para el umbral actual, la tabla debe mostrar un mensaje explícito de estado vacío — no simplemente desaparecer. La tabla también debe respetar el rango de fechas establecido en la Funcionalidad 1 si está activo.
>
> Endpoint relevante: `GET /api/metrics/alerts?threshold=<ratio>`
>
> ---
>
> #### Funcionalidad 3 — Vista comparativa B2B vs B2C
>
> Crea una nueva página en el dashboard para comparar el rendimiento de ingresos entre las dos líneas de negocio: B2B y B2C. La vista tiene dos secciones en paralelo. Cada sección muestra una tabla con las 5 categorías de ingreso principales de esa línea de negocio, mostrando nombre de categoría, total de ingresos y porcentaje sobre el total del grupo. Bajo ambas secciones, un único gráfico compara visualmente el total de ingresos de B2B frente a B2C. El usuario puede filtrar la comparativa por un rango de fechas (mismo formato `YYYY-MM-DD`). Las categorías disponibles para cada grupo deben obtenerse del endpoint de facetas.
>
> Endpoints relevantes: `GET /api/metrics/categories/top?operation_type=income&limit=5` y `GET /api/metrics/facets`

Tus especificaciones deben ser lo bastante precisas para que un coding agent construya cada funcionalidad solo con ellas — porque cada nombre de campo, parámetro y caso límite fue verificado contra `/docs`, no inventado.

---

## 🌱 Cómo iniciar el proyecto

Continúa en el **mismo repositorio** del proyecto de contexto. No hagas fork de un repo nuevo.

1. Abre tu fork del dashboard financiero ([**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) en tu coding agent.
2. Confirma que `memory-bank/` y `.agents/rules` del trabajo previo están commiteados y actualizados.
3. Crea una rama: `git switch -c feature/frontend-specs`.
4. Crea `frontend/specs/` — aquí irán todos los archivos de especificación.
5. Pide al agent que arranque el backend y abra `/docs`; explora endpoints de las tres funcionalidades antes de escribir ninguna spec.

Si necesitas repasar el trabajo con ramas: [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### Fase 1 — Explorar la API (con el agent)

- [ ] Con el backend en marcha, pide al agent mapear endpoints, formas de respuesta y parámetros de query de las tres funcionalidades usando `/docs`.
- [ ] Contrasta con patrones de fetch existentes en el frontend del repo cuando ayude.
- [ ] Anota desajustes entre el wording del PM y los campos reales de la API — resuélvelos en la spec, no en la implementación.
- [ ] Opcional: rastro corto de verificación en mensajes de commit o `verification.md`.

### Fase 2 — Tipos TypeScript (el agent redacta, tú verificas)

- [ ] Haz que el agent redacte `frontend/specs/api-types.ts` con interfaces para respuestas usadas por las tres funcionalidades:
  - `FacetsResponse` — referencia de rango de fechas y vista B2B vs B2C
  - `AlertEntry`, `AlertsResponse` — tabla de anomalías
  - `CategoryEntry`, `TopCategoriesResponse` — tabla comparativa B2B vs B2C
- [ ] Haz que el agent redacte `frontend/specs/param-types.ts` con tipos de parámetros de query:
  - `DateRangeFilter` — fechas opcionales de inicio/fin como `string` en formato `YYYY-MM-DD`
  - `AlertsParams` — threshold más filtro de fechas
  - `TopCategoriesParams` — tipo de operación, limit y filtro de fechas
- [ ] Verifica cada nombre y tipo de propiedad contra `/docs`; TypeScript estricto — sin `any`, sin `object`.
- [ ] Cada propiedad necesita JSDoc: significado, valores válidos, formato cuando aplique.
- [ ] Commit: tipos verificados contra OpenAPI.

### Fase 3 — Especificación de componentes (el agent redacta, tú verificas)

- [ ] Haz que el agent redacte `frontend/specs/components.md` por funcionalidad:

  **Funcionalidad 1 — Filtro de rango de fechas**
  - Nombre(s) de componente, props, layout
  - Comportamiento cuando solo un input de fecha está relleno
  - Cómo se muestra la pista del rango disponible (desde `FacetsResponse`)

  **Funcionalidad 2 — Tabla de alertas de anomalías**
  - Nombre(s) de componente y props
  - Cuatro columnas y sus tipos de dato
  - Estado vacío cuando el array de alertas está vacío
  - Comportamiento cuando el threshold está fuera de rango

  **Funcionalidad 3 — Vista comparativa B2B vs B2C**
  - Componentes del layout de dos paneles, tabla top-5, gráfico comparativo
  - Props de cada componente
  - Qué renderiza cada panel cuando la lista top-5 está vacía
  - Qué muestra el gráfico comparativo y qué representan sus dos puntos de datos

- [ ] Alinea props de componentes con tipos de la Fase 2; resuelve ambigüedades que el brief del PM dejó abiertas.
- [ ] Commit: specs de componentes.

### Fase 4 — Documentación del contrato de datos

- [ ] Haz que el agent redacte `frontend/specs/README.md` cubriendo las tres funcionalidades:
  - Endpoint(s) que consume cada una (rutas verificadas en `/docs`)
  - Tipos TypeScript de cada petición y respuesta
  - Valores válidos y restricciones de cada parámetro
  - Al menos 2 casos límite por funcionalidad y qué debe mostrar la UI
- [ ] Léelo como si se lo entregaras a una sesión nueva del agent — corrige lo que provocaría preguntas de seguimiento.
- [ ] Ejecuta `npx tsc --noEmit` y corrige errores de tipos.
- [ ] Commit: README de contrato de datos.

> ⚠️ **IMPORTANTE:** Estás especificando la capa frontend, no implementándola. No construyas componentes React ni conectes llamadas a la API. Entregables: tipos TypeScript, `components.md` y `frontend/specs/README.md`.

---

## ✅ Qué vamos a evaluar

- [ ] Evidencia de exploración de API: tipos y endpoints trazables a `/docs`, no nombres de campo inventados.
- [ ] Todas las interfaces de respuesta coinciden con OpenAPI en vivo, sin `any`.
- [ ] `DateRangeFilter` define ambos campos opcionales, tipados como `string` con JSDoc `YYYY-MM-DD`.
- [ ] `AlertsParams` y `TopCategoriesParams` extienden o incluyen `DateRangeFilter`.
- [ ] `components.md` nombra cada componente, lista props con tipos y especifica renderizado condicional por funcionalidad.
- [ ] Estado vacío de la tabla de anomalías especificado explícitamente.
- [ ] Comportamiento con un solo input de fecha especificado explícitamente.
- [ ] Ambos paneles B2B vs B2C especifican renderizado vacío de top-5.
- [ ] `frontend/specs/README.md` cubre las tres funcionalidades con endpoints, tipos, parámetros y ≥ 2 casos límite cada una.
- [ ] TypeScript compila (`npx tsc --noEmit`).
- [ ] Trabajo en `feature/frontend-specs` con commits significativos; specs se leen como trabajo asistido por agent que verificaste.
- [ ] Sin componentes React, llamadas fetch ni cambios de backend.

> Nota: La implementación queda fuera de alcance. La barra es una spec lo bastante buena para que un coding agent construya sin preguntas.

---

## 📦 Cómo entregar

Sube tu rama `feature/frontend-specs` a GitHub y comparte la URL del repositorio con tu instructor. Asegúrate de que `frontend/specs/` esté presente y la rama sea visible.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
