# Aplicando desarrollo guiado por especificaciones - Dashboard financiero

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

El dashboard financiero que construiste recientemente ya está en manos del equipo de finanzas del cliente, y tienen feedback. Quieren más control sobre los datos que ven, una forma de detectar gastos inusuales sin revisar filas una a una, y una vista dedicada para comparar ingresos entre sus dos líneas de negocio.

Antes de que alguien construya un solo componente, tu tech lead ha parado al equipo: **"Primero la especificación. Luego construimos."**

Una especificación bien escrita define qué ve el usuario, qué datos necesita cada componente y qué reglas rigen cada campo. Si la especificación es clara, cualquier desarrollador — o agente de IA — puede implementarla correctamente sin hacerte preguntas. Tu trabajo es producir esa especificación para tres funcionalidades concretas.

Empieza abriendo `/docs` en tu navegador con el backend en marcha. Lee las formas de respuesta y las reglas de parámetros de los endpoints relevantes antes de escribir ningún tipo ni descripción de componente. Tus especificaciones deben coincidir con lo que la API realmente devuelve.

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
> #### Funcionalidad 3 — Vista de comparativa B2B vs B2C
>
> Crea una nueva página en el dashboard para comparar el rendimiento de ingresos entre las dos líneas de negocio: B2B y B2C. La vista tiene dos secciones en paralelo. Cada sección muestra una tabla con las 5 categorías de ingreso principales de esa línea de negocio, mostrando nombre de categoría, total de ingresos y porcentaje sobre el total del grupo. Bajo ambas secciones, un único gráfico compara visualmente el total de ingresos de B2B frente a B2C. El usuario puede filtrar la comparativa por un rango de fechas (mismo formato `YYYY-MM-DD`). Las categorías disponibles para cada grupo deben obtenerse del endpoint de facetas.
>
> Endpoints relevantes: `GET /api/metrics/categories/top?operation_type=income&limit=5` y `GET /api/metrics/facets`

Tus especificaciones deben ser lo suficientemente precisas para que cualquier desarrollador — o agente de IA — pueda construir cada funcionalidad a partir de ellas, sin necesidad de hacerte ninguna pregunta.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto continúa en el mismo repositorio que usaste para el dashboard financiero. No hagas fork de un repo nuevo.

1. Abre tu repositorio existente del dashboard financiero (tu fork de [**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) en GitHub Codespaces o clónalo localmente.
2. Crea una nueva rama llamada `feature/frontend-specs` desde tu `main` actual.
3. Crea una carpeta llamada `frontend/specs/` — aquí irán todos tus archivos de especificación.
4. Arranca el backend y visita `/docs` para explorar los endpoints antes de escribir ninguna especificación.

Si necesitas repasar el trabajo con ramas: [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### Tipos TypeScript

- [ ] Crea `frontend/specs/api-types.ts` con interfaces TypeScript para las respuestas de la API usadas por las tres funcionalidades:
  - `FacetsResponse` — usada por la referencia de rango de fechas y por la vista B2B vs B2C
  - `AlertEntry`, `AlertsResponse` — usada por la tabla de anomalías
  - `CategoryEntry`, `TopCategoriesResponse` — usada por la tabla comparativa B2B vs B2C
- [ ] Crea `frontend/specs/param-types.ts` con tipos TypeScript para los parámetros de consulta enviados por cada funcionalidad:
  - `DateRangeFilter` — los parámetros opcionales de fecha de inicio y fin compartidos entre funcionalidades (fechas como `string` en formato `YYYY-MM-DD`)
  - `AlertsParams` — threshold más el filtro de rango de fechas
  - `TopCategoriesParams` — tipo de operación, limit y el filtro de rango de fechas
- [ ] Todos los tipos deben usar TypeScript estricto — sin `any`, sin `object`
- [ ] Documenta cada propiedad con un comentario JSDoc explicando su significado, valores válidos y formato cuando corresponda

### Especificación de componentes

- [ ] Crea `frontend/specs/components.md` con el desglose de componentes para cada funcionalidad:

  **Funcionalidad 1 — Filtro de rango de fechas**
  - Nombra el/los componente/s, lista sus props y describe el layout
  - Especifica qué ocurre cuando solo uno de los dos inputs de fecha está relleno
  - Especifica cómo se muestra la pista del rango de fechas disponible (procedente de `FacetsResponse`)

  **Funcionalidad 2 — Tabla de alertas de anomalías**
  - Nombra el/los componente/s y lista sus props
  - Especifica las cuatro columnas y sus tipos de dato
  - Especifica el estado vacío: qué se renderiza cuando el array de alertas está vacío
  - Especifica qué ocurre cuando el input del umbral recibe un valor fuera de rango

  **Funcionalidad 3 — Vista comparativa B2B vs B2C**
  - Nombra los componentes para el layout de dos paneles, la tabla top-5 y el gráfico comparativo
  - Lista las props de cada componente
  - Especifica qué renderiza cada panel cuando su lista top-5 está vacía
  - Describe qué muestra el gráfico comparativo y qué representan sus dos puntos de datos

### Documentación del contrato de datos

- [ ] Crea `frontend/specs/README.md` documentando las tres funcionalidades:
  - Qué endpoint/s consume cada funcionalidad (verifica las rutas contra `/docs`)
  - Los tipos TypeScript usados para cada petición y respuesta
  - Valores válidos y restricciones para cada parámetro
  - Al menos 2 casos edge por funcionalidad y qué debe mostrar la UI en cada caso

> ⚠️ **IMPORTANTE:** Estás especificando la capa frontend, no implementándola. No construyas componentes React ni hagas llamadas a la API. Tus entregables son los tipos TypeScript, `components.md` y `frontend/specs/README.md`.

---

## ✅ Qué vamos a evaluar

- [ ] Todas las interfaces de respuesta coinciden con las formas que devuelve la API (verificable en `/docs`), sin usar `any`
- [ ] `DateRangeFilter` define ambos campos como opcionales y tipados como `string` con una anotación JSDoc `YYYY-MM-DD`
- [ ] `AlertsParams` y `TopCategoriesParams` extienden o incluyen `DateRangeFilter`
- [ ] `components.md` nombra cada componente, lista sus props con tipos y especifica el renderizado condicional de cada funcionalidad
- [ ] El estado vacío de la tabla de alertas está especificado explícitamente
- [ ] El comportamiento cuando solo un input de fecha está relleno está especificado explícitamente
- [ ] Ambos paneles de la vista B2B vs B2C especifican qué se renderiza cuando su lista top-5 está vacía
- [ ] `frontend/specs/README.md` cubre las tres funcionalidades con endpoints, tipos, parámetros válidos y al menos 2 casos edge cada una
- [ ] TypeScript compila sin errores (`npx tsc --noEmit`)
- [ ] El código está commiteado en una rama llamada `feature/frontend-specs` con mensajes de commit significativos

> Nota: Los componentes React, las llamadas a la API y la implementación del backend no se evalúan en este proyecto.

---

## 📦 Cómo entregar

Sube tu rama `feature/frontend-specs` a GitHub y comparte la URL del repositorio con tu instructor según lo indicado en clase. Asegúrate de que la carpeta `frontend/specs/` esté presente y de que tu rama sea visible.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
