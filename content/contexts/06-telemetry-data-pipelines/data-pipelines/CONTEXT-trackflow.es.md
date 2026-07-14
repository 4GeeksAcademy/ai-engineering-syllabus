# CONTEXT — TrackFlow (Pipeline de Desempeño de Negocio)

## Proyectos de Data Pipeline (Diseño · Implementación · Subflows y Tests)

<!-- hide -->

_These instructions are [available in English](./CONTEXT-trackflow-pipeline.md)._

<!-- endhide -->

Este archivo es autocontenido: te da todo lo necesario para acotar, construir y probar el pipeline de desempeño de negocio de TrackFlow, sin tener que buscar en otros documentos. Se construye directamente sobre las métricas obligatorias ya definidas en tu `CONTEXT-trackflow.md` (telemetría) — léelo primero si no lo has hecho.

---

## 1. El entregable de negocio

Thomas (CEO) quiere un **reporte semanal** que pueda abrir sin llamar a Ana ni a Miguel, comparando cómo está funcionando cada almacén por cliente — lo mismo que sus directores hoy arman a mano cada domingo en la noche, consumiendo horas.

> **Entregable objetivo:** un consolidado semanal, por almacén y por cliente, de throughput, actividad de quiebre de stock y precisión de inventario — el "Reporte Semanal de Desempeño por Almacén y Cliente".

Este es el **único entregable concreto** para el que existe tu pipeline. Todo lo que escribas en tu `PIPELINE_DESIGN.md` debe poder rastrearse hasta aquí.

**Audiencia:** Thomas (CEO) y Ana (Head of Warehouse Operations) — stakeholders no técnicos que necesitan números, no eventos crudos.
**Frecuencia:** semanal (fresco la mañana del lunes, alineado con la expectativa que ya tiene el liderazgo de un "reporte ejecutivo semanal automático").

---

## 2. KPIs a medir

**Estos son los KPIs para los que existe este pipeline.** Todo lo demás en este documento — eventos de origen, lógica de agregación, esquema de tabla — es detalle de implementación al servicio de estos cuatro números. Si no tienes claro qué construir a continuación, vuelve a esta lista.

| KPI                          | Qué mide                                                                                             | Por qué le importa a TrackFlow                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Volumen de entrada**          | Cuántas unidades de mercancía de un cliente recibió un almacén durante la semana.                       | Muestra la carga entrante por almacén y cliente — la base para planificar capacidad (Ana).                  |
| **Throughput de salida**        | Cuántos pedidos preparó y despachó un almacén para un cliente durante la semana.                        | La señal de capacidad de procesamiento — cuánto es capaz de mover un almacén, no solo de recibir.           |
| **Frecuencia de quiebre de stock** | Cuántas veces durante la semana el SKU de un cliente en un almacén cayó por debajo del mínimo configurado. | Una alerta temprana antes de que ocurra un quiebre visible para el cliente — Miguel la necesita para gestionar expectativas. |
| **Tasa de discrepancia**        | La proporción de los pedidos de salida de la semana asociados a una discrepancia de inventario detectada. | La señal de precisión de inventario — indica qué combinaciones de almacén/cliente necesitan una auditoría.  |

Todo lo que sigue existe únicamente para calcular estos cuatro números de forma correcta, confiable y auditable.

---

## 3. Datos de origen

Tu fuente es `telemetry_events`, filtrada a las métricas obligatorias ya definidas en tu CONTEXT de telemetría:

| `event_type`                     | Alimenta qué KPI(s)                                  |
| ------------------------------------ | ---------------------------------------------------------- |
| `inbound_order_created`            | Volumen de entrada                                          |
| `outbound_order_created`           | Throughput de salida, Tasa de discrepancia (denominador)    |
| `stock_threshold_triggered`        | Frecuencia de quiebre de stock                               |
| `inventory_discrepancy_detected`   | Tasa de discrepancia (numerador)                             |

No necesitas ningún evento fuera de esta lista para la v1 — resiste la tentación de ampliar el alcance.

---

## 4. Agregación requerida

- **Grano:** una fila por `warehouse` por `client_id` por semana ISO (`week_start` = el lunes de esa semana, UTC).
- **Dimensiones:** `warehouse` (`los_angeles`/`zaragoza`), `client_id`, `week_start`.
- **Campos calculados por fila (cada uno mapea directamente a un KPI de la sección 2):**
  - `inbound_units_count` — Volumen de entrada: suma de las cantidades de `inbound_order_created` de la semana
  - `outbound_orders_count` — Throughput de salida: conteo de `outbound_order_created` de la semana
  - `stockout_events_count` — Frecuencia de quiebre de stock: conteo de `stock_threshold_triggered` de la semana
  - `discrepancy_events_count` — conteo de apoyo de `inventory_discrepancy_detected` de la semana
  - `discrepancy_rate` — Tasa de discrepancia: `discrepancy_events_count / outbound_orders_count` (0 si no hubo pedidos esa semana)

Aquí no hay dimensión de moneda — este entregable es operacional (volumen y precisión), no de costo.

---

## 5. Tabla de destino

Crea esta tabla bajo un esquema dedicado `reporting` — nunca escribas en `telemetry_events`:

```sql
create table reporting.weekly_warehouse_client_performance (
  id uuid primary key default gen_random_uuid(),
  warehouse text not null,
  client_id text not null,
  week_start date not null,
  inbound_units_count integer not null default 0,
  outbound_orders_count integer not null default 0,
  stockout_events_count integer not null default 0,
  discrepancy_events_count integer not null default 0,
  discrepancy_rate numeric not null default 0,
  computed_at timestamptz not null default now(),
  unique (warehouse, client_id, week_start)
);
```

El constraint `unique (warehouse, client_id, week_start)` es en el que debe apoyarse tu estrategia de idempotencia (upsert).

---

## 6. Nuevo endpoint de reporte

Expón el resultado de este pipeline a través de un módulo **nuevo**, `services/reporting/`, separado de `services/telemetry/`:

- `GET /reporting/weekly-warehouse-client-performance` — acepta un `week_start` opcional (por defecto, la semana calculada más reciente); devuelve todas las combinaciones almacén/cliente de esa semana:

```json
{
  "week_start": "2026-07-13",
  "entries": [
    {
      "warehouse": "los_angeles",
      "client_id": "fashion-co",
      "inbound_units_count": 4200,
      "outbound_orders_count": 980,
      "stockout_events_count": 3,
      "discrepancy_events_count": 2,
      "discrepancy_rate": 0.002
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — estado y metadata de la última corrida del pipeline (puedes reutilizar este mismo patrón para cualquier pipeline futuro).
- `POST /reporting/pipeline-runs` — dispara una corrida manual.

---

## 7. Restricciones de negocio

- Cada fila pertenece a un único cliente — nunca agregues entre clientes en la misma fila.
- Este pipeline lee `telemetry_events` en **modo solo lectura**. Nunca escribe de vuelta ahí.
- `services/telemetry/analysis.py` y `GET /telemetry/report` quedan fuera del alcance de este hito — no los modifiques.
