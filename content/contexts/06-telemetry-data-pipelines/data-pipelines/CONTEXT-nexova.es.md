# CONTEXT — Nexova (Pipeline de Desempeño de Negocio)

## Proyectos de Data Pipeline (Diseño · Implementación · Subflows y Tests)

<!-- hide -->

_These instructions are [available in English](./CONTEXT-nexova-pipeline.md)._

<!-- endhide -->

Este archivo es autocontenido: te da todo lo necesario para acotar, construir y probar el pipeline de desempeño de negocio de Nexova, sin tener que buscar en otros documentos. Se construye directamente sobre las métricas obligatorias ya definidas en tu `CONTEXT-nexova.md` (telemetría) — léelo primero si no lo has hecho.

---

## 1. El entregable de negocio

Laura (CEO) quiere un **reporte semanal** que pueda abrir sin llamar a Elena ni a Patricia, comparando cómo está cada oficina en inversión y entrega de material de formación — las dos cosas que L&D sigue mencionando pero que hoy nadie centraliza entre Valencia y Miami.

> **Entregable objetivo:** un consolidado semanal, por oficina y por programa, de costo de material, kits entregados y actividad de escasez de material — el "Reporte Semanal de Desempeño por Oficina y Programa".

Este es el **único entregable concreto** para el que existe tu pipeline. Todo lo que escribas en tu `PIPELINE_DESIGN.md` debe poder rastrearse hasta aquí.

**Audiencia:** Laura (CEO) y Elena (Gerente de L&D) — stakeholders no técnicos que necesitan números, no eventos crudos.
**Frecuencia:** semanal (fresco la mañana del lunes, alineado con la expectativa que ya tiene el liderazgo de un "reporte semanal automático").

---

## 2. KPIs a medir

**Estos son los KPIs para los que existe este pipeline.** Todo lo demás en este documento — eventos de origen, lógica de agregación, esquema de tabla — es detalle de implementación al servicio de estos cuatro números. Si no tienes claro qué construir a continuación, vuelve a esta lista.

| KPI                                      | Qué mide                                                                                                     | Por qué le importa a Nexova                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Costo de material por oficina/programa**   | Cuánto gastó una oficina adquiriendo material de formación o incorporación para un programa dado, durante la semana. | Muestra dónde se concentra la inversión de L&D, y si coincide con la demanda de matrículas.             |
| **Kits entregados**                          | Cuántos kits o certificados se entregaron realmente a clientes, candidatos, consultores o agentes durante la semana. | La señal de adopción — el gasto en material solo importa si llega a las personas que lo necesitan.     |
| **Frecuencia de escasez**                    | Cuántas veces durante la semana el stock de material de un programa cayó por debajo del mínimo configurado.  | Un indicador temprano de que Elena necesita reimprimir o reordenar antes de que afecte una ola grande de matrículas. |
| **Frecuencia de variación de costo**         | Cuántas veces durante la semana el costo de un proveedor de material subió de forma anómala respecto a su histórico. | Le indica a Elena y a Laura cuándo necesitan renegociar o buscar un proveedor alterno.                  |

Todo lo que sigue existe únicamente para calcular estos cuatro números de forma correcta, confiable y auditable.

---

## 3. Datos de origen

> **Un chequeo rápido de esquema primero:** este pipeline necesita un valor de costo en `inbound_order_created` (ej. un campo `unit_cost` o `total_cost` en `properties`) para calcular el costo de material. Si tu esquema de telemetría del hito anterior aún no lo tiene, agrégalo ahora — es una extensión natural de un evento obligatorio existente, no un tipo de evento nuevo.

Tu fuente es `telemetry_events`, filtrada a las métricas obligatorias ya definidas en tu CONTEXT de telemetría:

| `event_type`                  | Alimenta qué KPI(s)                             |
| -------------------------------- | ------------------------------------------------------ |
| `inbound_order_created`        | Costo de material por oficina/programa                 |
| `outbound_order_created`       | Kits entregados                                         |
| `stock_threshold_triggered`    | Frecuencia de escasez                                    |
| `kit_cost_variance_detected`   | Frecuencia de variación de costo                         |

No necesitas ningún evento fuera de esta lista para la v1 — resiste la tentación de ampliar el alcance.

---

## 4. Agregación requerida

- **Grano:** una fila por `office` por `programme_id` por semana ISO (`week_start` = el lunes de esa semana, UTC).
- **Dimensiones:** `office` (`valencia`/`miami`), `programme_id`, `week_start`.
- **Campos calculados por fila (cada uno mapea directamente a un KPI de la sección 2):**
  - `total_material_cost` — Costo de material por oficina/programa: suma de los costos de `inbound_order_created` de la semana, en la moneda local de la oficina
  - `kits_delivered_count` — Kits entregados: conteo de `outbound_order_created` de la semana
  - `shortage_events_count` — Frecuencia de escasez: conteo de `stock_threshold_triggered` de la semana
  - `cost_variance_events_count` — Frecuencia de variación de costo: conteo de `kit_cost_variance_detected` de la semana
  - `currency` — `EUR` o `USD`, según la oficina. **No conviertas monedas en este pipeline** — eso es un tema de v2, cuando exista una fuente de tipo de cambio.

---

## 5. Tabla de destino

Crea esta tabla bajo un esquema dedicado `reporting` — nunca escribas en `telemetry_events`:

```sql
create table reporting.weekly_office_program_performance (
  id uuid primary key default gen_random_uuid(),
  office text not null,
  programme_id text not null,
  week_start date not null,
  total_material_cost numeric not null default 0,
  kits_delivered_count integer not null default 0,
  shortage_events_count integer not null default 0,
  cost_variance_events_count integer not null default 0,
  currency text not null,
  computed_at timestamptz not null default now(),
  unique (office, programme_id, week_start)
);
```

El constraint `unique (office, programme_id, week_start)` es en el que debe apoyarse tu estrategia de idempotencia (upsert).

---

## 6. Nuevo endpoint de reporte

Expón el resultado de este pipeline a través de un módulo **nuevo**, `services/reporting/`, separado de `services/telemetry/`:

- `GET /reporting/weekly-office-program-performance` — acepta un `week_start` opcional (por defecto, la semana calculada más reciente); devuelve todas las combinaciones oficina/programa de esa semana:

```json
{
  "week_start": "2026-07-13",
  "entries": [
    {
      "office": "valencia",
      "programme_id": "b2b-sales",
      "total_material_cost": 1240.50,
      "kits_delivered_count": 18,
      "shortage_events_count": 1,
      "cost_variance_events_count": 0,
      "currency": "EUR"
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — estado y metadata de la última corrida del pipeline (puedes reutilizar este mismo patrón para cualquier pipeline futuro).
- `POST /reporting/pipeline-runs` — dispara una corrida manual.

---

## 7. Restricciones de negocio

- Nunca mezcles monedas en una sola fila agregada — `EUR` (Valencia) y `USD` (Miami) se reportan por separado, lado a lado, no sumados entre sí.
- Este pipeline lee `telemetry_events` en **modo solo lectura**. Nunca escribe de vuelta ahí.
- `services/telemetry/analysis.py` y `GET /telemetry/report` quedan fuera del alcance de este hito — no los modifiques.
