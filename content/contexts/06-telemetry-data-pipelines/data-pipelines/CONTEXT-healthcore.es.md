# CONTEXT — HealthCore (Pipeline de Desempeño de Negocio)

## Proyectos de Data Pipeline (Diseño · Implementación · Subflows y Tests)

<!-- hide -->

_These instructions are [available in English](./CONTEXT-healthcore-pipeline.md)._

<!-- endhide -->

Este archivo es autocontenido: te da todo lo necesario para acotar, construir y probar el pipeline de desempeño de negocio de HealthCore, sin tener que buscar en otros documentos. Se construye directamente sobre las métricas obligatorias ya definidas en tu `CONTEXT-healthcore.md` (telemetría) — léelo primero si no lo has hecho.

> ⚠️ **Nota regulatoria (HIPAA / UK GDPR):** este pipeline agrega únicamente datos de la cadena de suministro. Igual que en el sistema de telemetría, ningún resultado de este pipeline puede contener identificadores de paciente, diagnósticos, ni ningún dato real o simulado de PHI — todo aquí se agrega por `clinic` y `department`, nunca por paciente.

---

## 1. El entregable de negocio

La Dra. Okonkwo (CEO) quiere un **paquete mensual listo para la junta directiva** que pueda revisar sin que su equipo pase dos días consolidando hojas de cálculo — comparando costo de insumos y riesgo de quiebre de stock entre las 12 clínicas de la red, en EE.UU. y Reino Unido.

> **Entregable objetivo:** un consolidado mensual, por clínica y por país, de costo de insumos, actividad de quiebre de stock y riesgo de vencimiento — el "Reporte Mensual de Desempeño de Insumos por Clínica".

Este es el **único entregable concreto** para el que existe tu pipeline. Todo lo que escribas en tu `PIPELINE_DESIGN.md` debe poder rastrearse hasta aquí.

**Audiencia:** la Dra. Okonkwo (CEO) y Claire (Chief Compliance Officer) — stakeholders no técnicos que necesitan números, no eventos crudos.
**Frecuencia:** mensual (listo el primer día hábil del mes, alineado con la expectativa que ya tiene el liderazgo de un "paquete de reporte para la junta automático").

---

## 2. KPIs a medir

**Estos son los KPIs para los que existe este pipeline.** Todo lo demás en este documento — eventos de origen, lógica de agregación, esquema de tabla — es detalle de implementación al servicio de estos cuatro números. Si no tienes claro qué construir a continuación, vuelve a esta lista.

| KPI                                  | Qué mide                                                                                              | Por qué le importa a HealthCore                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------|
| **Costo de insumos por clínica**       | Cuánto gastó una clínica comprando insumos médicos durante el mes.                                       | Muestra dónde se concentra el gasto en toda la red y alimenta las decisiones de compra entre clínicas.          |
| **Volumen de consumo de insumos**      | Cuántos eventos de consumo de insumos registró una clínica durante el mes, por departamento.              | La señal de actividad operativa — ayuda a distinguir una clínica genuinamente ocupada de un hueco de captura de datos. |
| **Frecuencia de quiebre crítico**      | Cuántas veces durante el mes una clínica cayó por debajo del umbral mínimo de un insumo.                  | Una señal de riesgo de seguridad del paciente y de cumplimiento sobre la que Marcus y Claire necesitan actuar rápido. |
| **Conteo de riesgo de vencimiento**    | Cuántos lotes de insumo en una clínica fueron marcados por acercarse a su fecha de vencimiento durante el mes. | Una señal de riesgo de merma y de cumplimiento — indica qué insumo hay que usar o dar de baja antes de que venza. |

Todo lo que sigue existe únicamente para calcular estos cuatro números de forma correcta, confiable y auditable.

---

## 3. Datos de origen

> **Un chequeo rápido de esquema primero:** este pipeline necesita un valor de costo en `inbound_order_created` (ej. un campo `unit_cost` o `total_cost` en `properties`) para calcular el costo de insumos. Si tu esquema de telemetría del hito anterior aún no lo tiene, agrégalo ahora — es una extensión natural de un evento obligatorio existente, no un tipo de evento nuevo. Como siempre, este campo describe un costo de insumo, nunca a un paciente.

Tu fuente es `telemetry_events`, filtrada a las métricas obligatorias ya definidas en tu CONTEXT de telemetría:

| `event_type`                | Alimenta qué KPI(s)                          |
| -------------------------------- | ---------------------------------------------------- |
| `inbound_order_created`        | Costo de insumos por clínica                          |
| `outbound_order_created`       | Volumen de consumo de insumos                          |
| `stock_threshold_triggered`    | Frecuencia de quiebre crítico                          |
| `supply_expiry_flagged`        | Conteo de riesgo de vencimiento                        |

No necesitas ningún evento fuera de esta lista para la v1 — resiste la tentación de ampliar el alcance. En particular, no hagas join contra ninguna tabla a nivel de paciente.

---

## 4. Agregación requerida

- **Grano:** una fila por `clinic_id` por mes calendario (`month_start` = el primer día del mes, UTC).
- **Dimensiones:** `clinic_id`, `country` (`US`/`UK`), `month_start`.
- **Campos calculados por fila (cada uno mapea directamente a un KPI de la sección 2):**
  - `total_supply_cost` — Costo de insumos por clínica: suma de los costos de `inbound_order_created` del mes
  - `supply_consumption_count` — Volumen de consumo de insumos: conteo de `outbound_order_created` del mes
  - `critical_stockout_count` — Frecuencia de quiebre crítico: conteo de `stock_threshold_triggered` del mes
  - `expiry_risk_count` — Conteo de riesgo de vencimiento: conteo de `supply_expiry_flagged` del mes
  - `currency` — `USD` o `GBP`, según el país de la clínica. **No conviertas monedas en este pipeline** — eso es un tema de v2, cuando exista una fuente de tipo de cambio.

---

## 5. Tabla de destino

Crea esta tabla bajo un esquema dedicado `reporting` — nunca escribas en `telemetry_events`:

```sql
create table reporting.monthly_clinic_supply_performance (
  id uuid primary key default gen_random_uuid(),
  clinic_id text not null,
  country text not null,
  month_start date not null,
  total_supply_cost numeric not null default 0,
  supply_consumption_count integer not null default 0,
  critical_stockout_count integer not null default 0,
  expiry_risk_count integer not null default 0,
  currency text not null,
  computed_at timestamptz not null default now(),
  unique (clinic_id, month_start)
);
```

El constraint `unique (clinic_id, month_start)` es en el que debe apoyarse tu estrategia de idempotencia (upsert).

---

## 6. Nuevo endpoint de reporte

Expón el resultado de este pipeline a través de un módulo **nuevo**, `services/reporting/`, separado de `services/telemetry/`:

- `GET /reporting/monthly-clinic-supply-performance` — acepta un `month_start` opcional (por defecto, el mes calculado más reciente); devuelve todas las clínicas de ese mes:

```json
{
  "month_start": "2026-07-01",
  "clinics": [
    {
      "clinic_id": "austin-north",
      "country": "US",
      "total_supply_cost": 18420.50,
      "supply_consumption_count": 340,
      "critical_stockout_count": 1,
      "expiry_risk_count": 4,
      "currency": "USD"
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — estado y metadata de la última corrida del pipeline (puedes reutilizar este mismo patrón para cualquier pipeline futuro).
- `POST /reporting/pipeline-runs` — dispara una corrida manual.

---

## 7. Restricciones de negocio

- Ningún campo del resultado de este pipeline — tabla, respuesta del endpoint, o log — puede contener jamás un identificador de paciente, un diagnóstico, ni ningún dato real o simulado de PHI. La agregación se queda a nivel de `clinic`/`department`.
- Nunca mezcles monedas en una sola fila agregada — `USD` (clínicas en EE.UU.) y `GBP` (clínicas en Reino Unido) se reportan por separado, lado a lado, no sumados entre sí.
- Este pipeline lee `telemetry_events` en **modo solo lectura**. Nunca escribe de vuelta ahí.
- `services/telemetry/analysis.py` y `GET /telemetry/report` quedan fuera del alcance de este hito — no los modifiques.
