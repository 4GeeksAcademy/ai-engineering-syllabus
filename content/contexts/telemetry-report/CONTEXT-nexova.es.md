# CONTEXT — Nexova · Telemetría Fase 4: Reporte desde los Datos

## Tu empresa

**Nexova** es una consultora de recursos humanos y adquisición de talento con oficinas en Valencia (España) y Miami (Florida). Formas parte del equipo interno de Ingeniería de IA. La tabla `telemetry_events` está poblada con eventos reales del backoffice. Hoy construyes el pipeline que convierte esos eventos en las métricas que necesitan Patricia Solís (HR Manager) y Sergio Molina (CTO).

---

## Tus dos métricas

Estos son los dos cálculos de KPI que debe implementar tu `analysis.py`. Cada uno corresponde directamente a los KPIs definidos en tu plan de la Fase 1.

### Métrica 1 — Asignaciones diarias por oficina

**Pregunta de negocio:** ¿cuántos eventos de asignación de activos se registraron por día, segmentados por oficina?

**Responde el KPI:** Frecuencia de stock agotado por categoría de activo — las asignaciones por día revelan patrones de demanda que preceden a los desabastecimientos.

```python
# Pseudocódigo — implementar solo con operaciones de Pandas
def assignments_per_day_by_office(start_date, end_date):
    # Cargar desde telemetry_events donde event_type = 'assignment_order_created'
    # y timestamp entre start_date y end_date
    # Convertir timestamp a datetime (utc=True)
    # Extraer fecha del timestamp
    # Extraer office del JSONB de tags
    # groupby(['date', 'office'])['id'].count()
    # Devolver como lista de dicts: [{ "date": "...", "office": "...", "count": N }]
```

**Dimensión de agrupamiento:** fecha + office (de `tags`).
**Agregación:** `.count()` sobre el `id` del evento.

---

### Métrica 2 — Tasa de fallos de asignación por día

**Pregunta de negocio:** ¿qué proporción de intentos de asignación de activos fallaron cada día?

**Responde el KPI:** Tiempo de ciclo de aprovisionamiento (indirectamente — los fallos indican que los activos no se aprovisionaron a tiempo).

```python
# Pseudocódigo — implementar solo con operaciones de Pandas
def assignment_failure_rate_per_day(start_date, end_date):
    # Cargar desde telemetry_events donde event_type IN (
    #   'assignment_order_created', 'assignment_order_failed'
    # ) y timestamp entre start_date y end_date
    # Convertir timestamp a datetime (utc=True)
    # Extraer fecha
    # Crear columna booleana: is_failure = event_type == 'assignment_order_failed'
    # groupby('date').agg(total=('id', 'count'), failures=('is_failure', 'sum'))
    # Calcular failure_rate = failures / total
    # Devolver como lista de dicts: [{ "date": "...", "total": N, "failures": M, "failure_rate": 0.08 }]
```

**Dimensión de agrupamiento:** fecha.
**Agregación:** `.agg()` con count y sum, luego ratio derivado.

---

## Ejemplo de JSON esperado

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "assignments_per_day_by_office": [
      { "date": "2025-01-13", "office": "valencia", "count": 5 },
      { "date": "2025-01-13", "office": "miami", "count": 3 }
    ],
    "assignment_failure_rate_per_day": [
      { "date": "2025-01-13", "total": 8, "failures": 1, "failure_rate": 0.125 }
    ]
  }
}
```

---

## Actividad adicional — Tasa de fallos de autenticación

Si instrumentaste los eventos de autenticación en D47, implementa:

**Pregunta de negocio:** ¿qué porcentaje de intentos de login fallan cada día, por oficina?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'office de tags'])
# failure_rate = failed / (failed + succeeded)
```

---

## Restricciones de negocio para tu pipeline

- **`office` debe venir de `tags`**, no de una columna fija. Extráelo con Pandas: `df['office'] = df['tags'].apply(lambda x: x.get('office'))` — luego filtra las filas donde sea nulo antes de agrupar.
- **Valencia y Miami deben estar siempre segmentadas** en la métrica de asignaciones — Sergio necesita comparar ambas oficinas. Nunca agregues las dos oficinas en un único número sin dimensión de agrupamiento.
- **Las asignaciones de licencias de software** (`asset_category = software_licence` en `tags`) pueden aislarse en una tercera función si implementas la actividad adicional — carga eventos relevantes con SQL (`event_type` + timestamp), extrae `asset_category` en Pandas, luego `df[df['asset_category'] == 'software_licence']` antes de agrupar.

---

_Nexova AI Engineering Team — Documento interno para el AI Engineering Track de 4Geeks Academy_
