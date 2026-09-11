# CONTEXT — Brasaland

## Modelo de pronóstico de series de tiempo para predicción de ventas

---

### 1. Por qué esto le importa a Brasaland

Mariana (CEO) quiere saber si, antes de invertir en un dashboard ejecutivo completo, es posible predecir con un margen razonable cuánto va a vender la cadena en los próximos meses. Felipe (Operaciones) necesita anticipar compras de insumos según la tendencia esperada, y Lucía (Procurement) quiere anticipar variaciones de precio de la carne según el volumen proyectado. Un modelo de pronóstico de series de tiempo sobre las ventas históricas — que aprenda de lags, tendencias rodantes y patrones estacionales, no solo de las columnas crudas — es el primer paso concreto hacia ese dashboard.

---

### 2. Estructura de datos

El dataset mensual de ventas consolidadas de las 14 ubicaciones ya está incluido en tu monorepo, en `data/raw/brasaland_sales.csv`, con estas columnas exactas:

| Columna | Tipo | Descripción |
|---|---|---|
| `month` | fecha (`YYYY-MM-01`) | Primer día del mes reportado |
| `revenue_usd` | float | Ventas totales del mes, consolidadas en USD (usa una tasa fija de conversión COP→USD para simplificar, por ejemplo 1 USD = 4.000 COP) |
| `covers_served` | int | Número total de comensales atendidos en el mes, en las 14 ubicaciones |
| `avg_ticket_usd` | float | Ticket promedio del mes en USD |
| `market` | string | `"colombia"`, `"florida"`, o `"consolidated"` — usa `"consolidated"` como la fila principal para el modelo; las filas por mercado son opcionales como features adicionales |

La variable objetivo (target) del modelo es `revenue_usd` de la fila `consolidated`.

---

### 3. KPIs y qué significa un buen modelo aquí

- Un **Gini** bajo indica que el modelo no distingue bien entre meses "buenos" y "malos" — para Mariana esto es tan importante como el error absoluto, porque necesita identificar los meses de bajo desempeño con anticipación.
- Un **PSI** alto entre el conjunto de entrenamiento y el de prueba sería señal de que el comportamiento de ventas cambió estructuralmente (por ejemplo, apertura de nuevas ubicaciones, cambio de mercado) y el modelo necesitaría reentrenarse — menciónalo explícitamente si lo detectas.
- El **MSE** repórtalo en USD² pero tradúcelo también a un error porcentual promedio, porque así es como Felipe y Mariana entienden el número.

---

### 4. Sobre el dataset provisto

El archivo `data/raw/brasaland_sales.csv` contiene **10 años** de datos mensuales (120 filas de `consolidated`), desde `2016-01` hasta `2025-12`. Ya refleja los siguientes patrones — no necesitas generarlos, pero sí entenderlos para interpretar los resultados de tu modelo:

**Patrón de crecimiento:** el crecimiento anual base es `X = 5%`, con una variación `Y = 2%`. Cada año, el crecimiento real `d` alterna entre `X+Y` y `X-Y` (es decir, entre 3% y 7%), nunca fuera de ese rango, y siempre positivo.

**Patrón de estacionalidad (presente cada año del dataset):**
- **Enero:** caída de ventas del 12–18% respecto al promedio del año anterior, explicable por el período de "vacaciones colectivas" y el bajón post-diciembre típico en Colombia.
- **Diciembre:** alza de ventas del 20–30% respecto al promedio, por la temporada de fiestas en ambos mercados.
- El resto de los meses fluctúa de forma moderada (±5%) alrededor de la tendencia de crecimiento anual, sin patrones abruptos.

El dataset se generó con una semilla aleatoria fija (`random_state=42`), por lo que es determinista: si lo regeneraras con el mismo script y semilla, obtendrías exactamente los mismos valores.

---

### 5. Restricciones de negocio

- Todos los valores de `revenue_usd` deben ser positivos.
- No debe haber meses faltantes en el rango 2016-01 a 2025-12.
- El dataset provisto solo incluye la fila `consolidated`; si quieres analizar Colombia y Florida por separado como feature adicional, ten en cuenta que Florida es un mercado más pequeño (aproximadamente 25% del total) — no asumas magnitudes similares entre ambos.

---

### 6. Entregables esperados

- Script de entrenamiento en `scripts/` que cargue `data/raw/brasaland_sales.csv`, separe los primeros 8 años como entrenamiento y los últimos 2 como prueba.
- Features causales de lag, estadísticas rodantes y calendario/estacionalidad construidos a partir de la serie (validados contra el patrón de crecimiento y estacionalidad descrito arriba), sin fuga de información desde filas futuras.
- Modelo entrenado (XGBoost o Random Forest) con las 4 métricas (MSE, PSI, Gini, K2 Score) calculadas sobre el conjunto de prueba.
- Visualización con la predicción y su rango de variabilidad frente a los datos reales de los 2 años de prueba.
- Prueba unitaria en `tests/pipelines/` que valide el split 8/2 años.
