# CONTEXT — HealthCore

## Modelo de pronóstico de series de tiempo para predicción de ventas

---

### 1. Por qué esto le importa a HealthCore

Sandra (CEO) necesita saber si es posible predecir los ingresos de los próximos meses antes de invertir en un dashboard ejecutivo de toda la red. Los ingresos de HealthCore están ligados a la demanda de consultas, que varía de forma predecible según la temporada — algo que Marcus (Operaciones Clínicas) y Tom (Revenue Cycle) observan cada año pero nunca han cuantificado con un modelo.

> **Nota regulatoria:** este dataset trabaja con **ingresos agregados mensuales**, no con datos de pacientes individuales. No incluyas ningún identificador de paciente, diagnóstico o dato clínico en el dataset de ventas — eso mantiene el proyecto fuera del alcance de HIPAA y UK GDPR para efectos de este ejercicio. Si en algún momento tu pipeline tocara datos a nivel de paciente, necesitarías un BAA (EE. UU.) o un DPA (Reino Unido) antes de procesarlos.

---

### 2. Estructura de datos

El dataset mensual de ingresos consolidados de HealthCore ya está incluido en tu monorepo, en `data/raw/healthcore_sales.csv`, con estas columnas exactas:

| Columna | Tipo | Descripción |
|---|---|---|
| `month` | fecha (`YYYY-MM-01`) | Primer día del mes reportado |
| `revenue_usd` | float | Ingresos totales del mes, consolidados en USD |
| `visits_count` | int | Número total de consultas atendidas en el mes (las 12 clínicas) |
| `avg_revenue_per_visit_usd` | float | Ingreso promedio por consulta del mes |
| `region` | string | `"us"`, `"uk"`, o `"consolidated"` — usa `"consolidated"` como fila principal para el modelo |

La variable objetivo (target) del modelo es `revenue_usd` de la fila `consolidated`.

---

### 3. KPIs y qué significa un buen modelo aquí

- Un **Gini** alto le importa a Sandra para distinguir con confianza entre un mes de temporada baja normal (por ejemplo, agosto) y una caída atípica que amerite atención — por ejemplo, un problema de capacidad clínica.
- El **PSI** ayuda a detectar si la mezcla de visitas entre EE. UU. y Reino Unido cambió de forma significativa entre entrenamiento y prueba — repórtalo si ocurre, ya que podría reflejar la apertura de una nueva clínica.
- El **MSE** repórtalo en USD² y también como porcentaje del ingreso mensual promedio, para que Tom (Revenue Cycle) y Sandra puedan interpretarlo sin traducción adicional.

---

### 4. Sobre el dataset provisto

El archivo `data/raw/healthcore_sales.csv` contiene **10 años** de datos mensuales (120 filas de `consolidated`), desde `2016-01` hasta `2025-12`. Ya refleja los siguientes patrones — no necesitas generarlos, pero sí entenderlos para interpretar los resultados de tu modelo:

**Patrón de crecimiento:** crecimiento anual base `X = 4%`, con variación `Y = 2%`. Cada año, el crecimiento real `d` alterna entre `X+Y` y `X-Y` (entre 2% y 6%), siempre positivo.

**Patrón de estacionalidad (presente cada año del dataset):**
- **Octubre–Diciembre:** alza de ingresos del 15–20% respecto al promedio, por la temporada de gripe y el aumento de consultas de fin de año.
- **Julio–Agosto:** caída de ingresos del 12–18% respecto al promedio, por la temporada vacacional de verano, que reduce las consultas no urgentes en ambos países.
- El resto de los meses fluctúa de forma moderada (±5%) alrededor de la tendencia de crecimiento anual.

El dataset se generó con una semilla aleatoria fija (`random_state=42`), por lo que es determinista. Al igual que el resto del dataset, contiene únicamente cifras agregadas mensuales — ningún dato a nivel de paciente individual.

---

### 5. Restricciones de negocio

- Todos los valores de `revenue_usd` deben ser positivos.
- No debe haber meses faltantes en el rango 2016-01 a 2025-12.
- El dataset provisto solo incluye la fila `consolidated` y no contiene ningún dato a nivel de paciente individual. Si separas por región como feature adicional, recuerda que EE. UU. concentra la mayor parte del volumen (9 de las 12 clínicas) — usa aproximadamente 75/25 como proporción de referencia entre EE. UU. y Reino Unido.

---

### 6. Entregables esperados

- Script de entrenamiento en `scripts/` que cargue `data/raw/healthcore_sales.csv`, separe los primeros 8 años como entrenamiento y los últimos 2 como prueba.
- Features causales de lag, estadísticas rodantes y calendario/estacionalidad construidos a partir de la serie (validados contra el patrón de crecimiento y estacionalidad descrito arriba), sin fuga de información desde filas futuras.
- Modelo entrenado (XGBoost o Random Forest) con las 4 métricas (MSE, PSI, Gini, K2 Score) calculadas sobre el conjunto de prueba.
- Visualización con la predicción y su rango de variabilidad frente a los datos reales de los 2 años de prueba.
- Prueba unitaria en `tests/pipelines/` que valide el split 8/2 años.
