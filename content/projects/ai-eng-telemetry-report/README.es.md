# Telemetría de la compañía – Reporte

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Necesitas la tabla `telemetry_events` en Supabase con al menos 20 filas de eventos reales generados desde el backoffice. Sin datos reales no hay nada que analizar — genera actividad en el módulo de inventario antes de continuar.

Relee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/telemetry-report)** junto con `docs/telemetry/telemetry-plan.md` — cada métrica debe responder a uno de los tres KPIs definidos ahí para tu empresa asignada, no a un dashboard genérico de inventario.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Los datos están ahí. La tabla `telemetry_events` tiene eventos reales con `timestamp`, `event_type` y `tags`. Pero los datos crudos no son la respuesta — son la materia prima. Hoy los transformas.

El entregable es un pipeline de análisis en Python y un endpoint que sirve el resultado: las métricas de los KPIs que definiste en la Fase 1, calculadas desde los eventos almacenados, servidas como JSON y listas para ser consumidas por cualquier dashboard o herramienta de reporte.

> Tu tech lead te ha enviado este mensaje:
>
> > "Tenemos datos. Ahora necesito respuestas.
> >
> > Escribe el pipeline de análisis. Para cada KPI del plan, una función Python que cargue los eventos relevantes, los transforme con Pandas y devuelva el resultado serializable. Luego un endpoint `GET /telemetry/report` que los sirva juntos.
> >
> > Dos reglas no negociables: primero, no calcules nada dentro del endpoint en cada request — el pipeline va separado y el endpoint lo llama, con caché. Segundo, convierte los timestamps a `datetime` antes de cualquier agrupamiento — si no lo haces obtendrás grupos incorrectos sin ningún error visible, y tardarás horas en encontrar el bug.
> >
> > Quiero ver métricas reales con dimensión temporal. Un número global sin contexto de agrupamiento no es una métrica — es un recuento."

---

### 📚 Conocimiento complementario — La fórmula de cualquier reporte

Los datos almacenados en `telemetry_events` responden la pregunta "¿qué ocurrió?". Las preguntas del negocio son distintas: "¿cuántas órdenes fallaron por día esta semana?" o "¿qué tipo de evento es más frecuente?". Responderlas requiere transformación — siempre en el mismo orden:

```
cargar (SQL) → refinar (Pandas) → convertir tipos → agrupar → agregar → servir
```

### Dónde va cada filtro

| Criterio                                               | Capa                     | Cómo                                                                                                                                               |
| ------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rango `timestamp` (`start_date` / `end_date`)          | **SQL**                  | `WHERE timestamp >= :start AND timestamp < :end` — límites **inicio inclusivo, fin exclusivo** en UTC                                              |
| `event_type` (uno o varios)                            | **SQL**                  | `WHERE event_type = '...'` o `WHERE event_type IN (...)` — métricas de ratio necesitan todos los tipos del denominador en una sola query           |
| Dimensiones en `tags` (`warehouse`, `office`, etc.)    | **Pandas**               | Extraer de `tags`, descartar filas con dimensión nula, luego `groupby` — segmentar **todos** los valores, no pre-filtrar a un solo almacén/clínica |
| Flags derivados (`is_failure`, tasas)                  | **Pandas**               | Crear columnas tras la carga, luego `.agg()`                                                                                                       |
| Predicados opcionales en `tags` (ej. `reason = waste`) | **Pandas** (por defecto) | Filtrar el DataFrame tras extraer el campo; push-down SQL con `tags->>'...'` es optimización opcional, no obligatoria                              |

**Cargar (SQL)** — traer solo las filas que la métrica necesita. Nunca cargar la tabla `telemetry_events` entera en memoria.

**Refinar (Pandas)** — tras la carga: extraer campos de `tags`, descartar filas con dimensiones nulas, aplicar filtros adicionales a nivel de fila. Esto **no** sustituye el filtrado SQL por `event_type` / `timestamp`.

**Propiedad de la ventana temporal** — el endpoint calcula el periodo por defecto (últimos 7 días si no hay query params) y pasa `start_date` / `end_date` a cada función de métrica. Las funciones aplican esa ventana **una sola vez en SQL**; no re-apliquen un filtro "últimos 7 días" en Pandas.

**Convertir tipos** — los timestamps llegan como strings. Hacer `groupby()` sobre strings que parecen fechas produce grupos incorrectos sin lanzar ningún error. Convierte siempre antes de agrupar:

```python
df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
df['date'] = df['timestamp'].dt.date
```

**Agrupar** con `groupby()` por la dimensión que responde la pregunta: por día, por `event_type`, por el valor de una propiedad dentro de `tags`.

**Agregar** con `.count()`, `.sum()` o `.mean()`. La fórmula mental es siempre:

```
MÉTRICA = AGREGACIÓN(columna) agrupada por DIMENSIÓN
```

`df.groupby('date')['id'].count()` — eventos por día. Sin dimensión de agrupamiento solo tienes un número global; con dimensión tienes contexto accionable.

**Servir** el resultado como lista de dicts con `.reset_index().to_dict(orient='records')` — serializable directamente a JSON.

**Lo que no se hace:** calcular el reporte dentro del endpoint en cada request. Si los datos no cambian en segundos, el cálculo va en una función separada llamada una vez, con el resultado en caché.

---

## 🌱 Cómo Empezar el Proyecto

1. Abre tu fork del monorepo y localiza `services/` (backend FastAPI).
2. Consulta `telemetry_events` en Supabase y confirma que tienes al menos 20 filas con variedad de `event_type` — si no, genera actividad en el backoffice primero.
3. Revisa tu `CONTEXT-company.md` y `docs/telemetry/telemetry-plan.md` — los KPIs del contexto de tu empresa son exactamente las métricas que calcularás hoy.
4. Sigue el orden: funciones de análisis → endpoint de reporte → caché.

---

## 💻 Lo Que Debes Hacer

### Fase 1 — Pipeline de análisis con Pandas

- [ ] Crea `services/telemetry/analysis.py` con al menos **dos funciones de métrica**, cada una encapsulando el cálculo de un KPI de tu plan. Cada función debe:
  - Recibir parámetros `start_date` y `end_date` (calculados por el endpoint — inicio inclusivo, fin exclusivo, UTC)
  - Cargar desde Supabase solo los eventos relevantes: filtrar `event_type` (valor único o `IN (...)` para métricas de ratio) y rango de `timestamp` **en la query SQL**, no en Python
  - Refinar en Pandas tras la carga: extraer dimensiones de `tags`, descartar filas con dimensión nula, aplicar filtros adicionales de la métrica
  - Cargar el resultado en un DataFrame de Pandas
  - Convertir `timestamp` a `datetime` con `pd.to_datetime(..., utc=True)` antes de cualquier operación de agrupamiento
  - Agrupar con `groupby()` por la dimensión temporal apropiada y agregar con `.count()`, `.sum()` o `.mean()`
  - Devolver el resultado como lista de dicts serializable a JSON con `.reset_index().to_dict(orient='records')`
- [ ] Cada función debe ser **independiente y sin efectos secundarios** — llamarla dos veces con los mismos parámetros debe producir el mismo resultado.
- [ ] No uses loops para calcular métricas — solo operaciones de Pandas (`.groupby()`, `.agg()`, `.count()`, `.sum()`, `.mean()`).

⚠️ **IMPORTANTE:** Los nombres de métricas y las preguntas de negocio deben mapear a KPIs basados en `CONTEXT-company.md` a través de tu plan de la Fase 1. Un recuento genérico de "eventos por día" sin las dimensiones de agrupamiento de tu empresa no será aceptado.

### Fase 2 — Endpoint de reporte

- [ ] Crea el endpoint `GET /telemetry/report` en FastAPI. Debe:
  - Aceptar parámetros opcionales de query `start_date` y `end_date` en formato ISO 8601; si no se proporcionan, usar los últimos 7 días por defecto (`start_date = now − 7d`, `end_date = now`, ambos UTC)
  - Resolver el periodo una vez y pasar `start_date` / `end_date` a cada función de métrica — las funciones no aplican su propia ventana por defecto
  - Llamar a las funciones de métrica del pipeline de análisis con esos parámetros
  - Devolver un JSON con la estructura:
    ```json
    {
      "period": { "from": "...", "to": "..." },
      "metrics": {
        "nombre_metrica_1": [...],
        "nombre_metrica_2": [...]
      }
    }
    ```
- [ ] El endpoint **no debe ejecutar el pipeline en cada request** — implementa una caché simple en memoria con TTL de 60 segundos. Si la misma combinación de `start_date`/`end_date` se solicita dentro del TTL, devuelve el resultado cacheado sin recalcular.

### 🔵 Actividad adicional — Métrica de autenticación

- [ ] Si instrumentaste el flujo de autenticación en D47, añade una tercera función de métrica que calcule la **tasa diaria de fallos de login**: `user_login_failed` dividido entre el total de intentos (`user_login_failed` + `user_login_succeeded`) por día. Carga ambos tipos con `event_type IN (...)` en SQL, luego calcula el ratio en Pandas. Inclúyela en el endpoint bajo la clave `auth_failure_rate`.

---

## ✅ Qué Evaluaremos

- [ ] El archivo `services/telemetry/analysis.py` existe y contiene al menos dos funciones de métrica independientes
- [ ] Cada función sigue la fórmula `cargar (SQL) → refinar (Pandas) → convertir tipos → agrupar → agregar` en ese orden
- [ ] Los timestamps se convierten a `datetime` con `utc=True` antes de cualquier `groupby()` temporal
- [ ] No hay loops para calcular métricas — solo operaciones de Pandas
- [ ] Cada función devuelve una lista de dicts serializable a JSON
- [ ] El endpoint `GET /telemetry/report` acepta `start_date` y `end_date` opcionales y usa 7 días por defecto
- [ ] El endpoint devuelve el JSON con la estructura `{ "period": {...}, "metrics": {...} }`
- [ ] El endpoint tiene caché en memoria con TTL de 60 segundos — no recalcula en cada request
- [ ] Cada métrica responde a un KPI del `telemetry-plan.md` del estudiante, justificado con datos de `CONTEXT-company.md`
- [ ] Las métricas devueltas tienen dimensión de agrupamiento — no son números globales sin contexto

---

## 📦 Cómo Entregar

1. Asegúrate de que los cambios están en tu fork: `analysis.py` en `services/telemetry/` y endpoint `GET /telemetry/report` en `services/`.
2. Crea un Pull Request contra la rama principal del monorepo con el título: `[W17D49] Telemetry Report`.
3. En la descripción del PR, incluye:
   - El nombre de las dos métricas implementadas y la pregunta de negocio que responde cada una
   - Una muestra del JSON que devuelve `GET /telemetry/report` con datos reales
   - Si implementaste la métrica de autenticación, indícalo

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
