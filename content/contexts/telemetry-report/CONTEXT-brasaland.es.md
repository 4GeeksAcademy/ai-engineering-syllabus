# CONTEXT — Brasaland · Telemetría Fase 4: Reporte desde los Datos

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa con 14 locales en Colombia y Florida. Formas parte de **Brasaland Digital**. La tabla `telemetry_events` está poblada con eventos reales del backoffice. Hoy construyes el pipeline que convierte esos eventos en las métricas que necesitan Felipe Guerrero (Director de Operaciones) y Mariana Restrepo (CEO).

---

## Tus dos métricas

Estos son los dos cálculos de KPI que debe implementar tu `analysis.py`. Cada uno corresponde directamente a los KPIs definidos en tu plan de la Fase 1.

### Métrica 1 — Consumo diario por local

**Pregunta de negocio:** ¿cuántos eventos de orden de consumo se registraron por día, segmentados por local?

**Responde el KPI:** Tasa de consumo diario por ingrediente y local.

```python
# Pseudocódigo — implementar solo con operaciones de Pandas
def consumption_by_location_per_day(start_date, end_date):
    # Cargar desde telemetry_events donde event_type = 'consumption_order_created'
    # y timestamp entre start_date y end_date
    # Convertir timestamp a datetime (utc=True)
    # Extraer fecha del timestamp
    # Extraer location_id del JSONB de tags
    # groupby(['date', 'location_id'])['id'].count()
    # Devolver como lista de dicts: [{ "date": "...", "location_id": "...", "count": N }]
```

**Dimensión de agrupamiento:** fecha + location_id (de `tags`).
**Agregación:** `.count()` sobre el `id` del evento.

---

### Métrica 2 — Tasa de fallos de órdenes por día

**Pregunta de negocio:** ¿qué proporción de intentos de orden (suministro + consumo) fallaron cada día?

**Responde el KPI:** Frecuencia de stock agotado (indirectamente — los fallos señalan estrés en la cadena de suministro).

```python
# Pseudocódigo — implementar solo con operaciones de Pandas
def order_failure_rate_per_day(start_date, end_date):
    # Cargar desde telemetry_events donde event_type IN (
    #   'consumption_order_created', 'supply_order_created',
    #   'consumption_order_failed', 'supply_order_failed'
    # ) y timestamp entre start_date y end_date
    # Convertir timestamp a datetime (utc=True)
    # Extraer fecha
    # Crear columna booleana: is_failure = event_type termina en '_failed'
    # groupby('date').agg(total=('id', 'count'), failures=('is_failure', 'sum'))
    # Calcular failure_rate = failures / total
    # Devolver como lista de dicts: [{ "date": "...", "total": N, "failures": M, "failure_rate": 0.12 }]
```

**Dimensión de agrupamiento:** fecha.
**Agregación:** `.agg()` con count y sum, luego ratio derivado.

---

## Ejemplo de JSON esperado

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "consumption_by_location_per_day": [
      { "date": "2025-01-13", "location_id": "medellin_centro", "count": 12 },
      { "date": "2025-01-13", "location_id": "miami_south", "count": 8 }
    ],
    "order_failure_rate_per_day": [
      { "date": "2025-01-13", "total": 20, "failures": 3, "failure_rate": 0.15 }
    ]
  }
}
```

---

## Actividad adicional — Tasa de fallos de autenticación

Si instrumentaste los eventos de autenticación en D47, implementa:

**Pregunta de negocio:** ¿qué porcentaje de intentos de login fallan cada día, por local?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'location_id de tags'])
# failure_rate = failed / (failed + succeeded)
```

---

## Restricciones de negocio para tu pipeline

- **`location_id` debe venir de `tags`**, no de una columna fija. Extráelo con Pandas: `df['location_id'] = df['tags'].apply(lambda x: x.get('location_id'))` — luego filtra las filas donde sea nulo antes de agrupar.
- **Colombia y Florida deben estar siempre segmentadas** en la métrica de consumo — Felipe necesita comparar ambos mercados. La convención de nomenclatura de `location_id` (`medellin_*`, `bogota_*` para Colombia; `miami_*` para Florida) es lo que permite esa segmentación.
- **El KPI de ratio de merma** (ConsumptionOrders con `reason = waste/spoilage/theft`) puede añadirse como tercera función si implementas la actividad adicional — carga con SQL (`event_type` + timestamp), extrae `reason` de `tags` en Pandas, luego `df[df['reason'].isin(['waste', 'spoilage', 'theft'])]` antes de agrupar.

---

_Brasaland Digital — Documento interno para el AI Engineering Track de 4Geeks Academy_
