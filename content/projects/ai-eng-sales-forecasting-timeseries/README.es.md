# Predicción de Ventas con Feature Engineering de Series de Tiempo

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/sales-forecasting)** antes de escribir cualquier línea de código — ahí se documenta el significado de cada columna y el patrón de estacionalidad del histórico de ventas de tu empresa, que ya viene incluido como CSV en `content/contexts/sales-forecasting/<empresa>/<empresa>_sales.csv` de este repositorio.

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya preparaste y dividiste los datos históricos de tu empresa en conjuntos de entrenamiento y prueba, y entrenaste un primer modelo de clasificación. Ahora tu tech lead necesita algo distinto: el equipo de Dirección quiere saber **cuánto va a vender la empresa en los próximos meses**, no solo clasificar un resultado en categorías. Tu primer intento metió las columnas crudas directo a un modelo — pero una serie de ventas no es solo una tabla de filas independientes, es una **secuencia en el tiempo**, y esconde información que un setup de regresión plano ignora: qué pasó el mes pasado, qué pasó este mismo mes el año anterior, y si la tendencia se está acelerando o aplanando.

Tu tech lead ha abierto un **ticket** a partir de una **RFI** que llegó del área de Finanzas: quieren saber si, con los datos históricos disponibles, es viable predecir el comportamiento futuro de las ventas con un margen de error aceptable antes de comprometerse a construir un dashboard ejecutivo completo alrededor de esto.

> **De:** Tu tech lead
> **Asunto:** Ticket — Modelo de pronóstico de ventas
>
> Finanzas quiere saber si podemos predecir las ventas de los próximos meses a partir del histórico. Antes de prometerles nada, necesito un modelo entrenado y evaluado con honestidad: nada de presumir un error bajo solo porque el modelo memorizó el pasado.
>
> Criterios no negociables:
>
> - Usa los **primeros 8 años** de datos para entrenar y los **2 años más recientes** como comprobación de la predicción — esos años recientes el modelo no los debe haber visto durante el entrenamiento.
> - No le metas las columnas crudas al modelo sin más — construye **features conscientes del tiempo** (lags, estadísticas rodantes, señales de calendario) para que aprenda el ritmo real de las ventas y no solo promedios.
> - Quiero una **visualización** que muestre la predicción junto con su rango de variabilidad (no un solo número optimista).
> - Justifica por qué elegiste XGBoost o Random Forest para este caso, no asumas que uno es "mejor" sin argumentarlo.
> - Reporta el error con una métrica que yo pueda explicarle a Finanzas sin que parezca una caja negra.

**Conocimiento complementario: leer una serie de tiempo antes de modelarla.** Antes de construir features, descompón la serie en tres componentes: **tendencia** (la dirección de largo plazo), **estacionalidad** (el patrón que se repite según el calendario, por ejemplo un pico en diciembre) y **residual** (lo que queda — ruido o eventos que las otras dos no explican). Una herramienta como `statsmodels.tsa.seasonal_decompose` grafica los tres componentes por separado para que puedas *ver* si la estacionalidad que vas a construir como feature realmente coincide con lo que hay en los datos, en lugar de adivinar. Esta descomposición es una lente de diagnóstico, no un modelo — el pronóstico lo sigues haciendo con un regresor, como se describe abajo.

Una vez que entiendes la forma de la serie, tradúcela en features que un regresor pueda consumir:

- **Features de lag**: `ventas(t-1)`, `ventas(t-12)` — qué pasó el mes pasado y en el mismo mes del año anterior.
- **Estadísticas rodantes (rolling)**: media/desviación estándar móvil sobre los últimos 3–12 meses — captura la tendencia reciente y la volatilidad.
- **Features de calendario**: mes, trimestre, o una codificación cíclica del mes (`sin`/`cos`) — captura la estacionalidad recurrente sin necesidad de codificarla a mano.

**Conocimiento complementario: Random Forest vs. XGBoost.** Random Forest entrena muchos árboles de decisión sobre subconjuntos distintos de datos y promedia sus resultados — es más simple de explicar y un buen punto de partida. XGBoost entrena árboles de forma secuencial, donde cada uno corrige los errores del anterior — suele predecir mejor pero es más difícil de explicar y requiere más ajuste. Elige según qué necesita realmente tu stakeholder: explicabilidad o máxima precisión.

---

## 🌱 Cómo Empezar el Proyecto

1. Si aún no tienes un _fork_ del [monorepo de tu empresa](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo), créalo en GitHub. Recomendamos abrir y trabajar ese fork en **GitHub Codespaces**; si prefieres trabajar en local, clónalo en tu máquina.
2. Desde `main` de tu fork, crea una rama nueva para este proyecto: `git switch -c feature/sales-forecast-model` (en Codespaces o en tu entorno local).
3. Valida que `uv` esté instalado con `uv --version`; si no lo tienes, instálalo con `curl -LsSf https://astral.sh/uv/install.sh | sh` y, en la raíz del proyecto, inicializa el entorno con `uv init` (solo si aún no existe `pyproject.toml`). Luego agrega las dependencias con `uv add` (por ejemplo `scikit-learn`, `xgboost`, `pandas`, `matplotlib`, `statsmodels`) — nunca uses `pip install` ni `pipenv`.
4. Usa el dataset de ventas históricas ya provisto para tu empresa: en el monorepo está en `data/raw/<empresa>_sales.csv` y en este repositorio de referencia en `content/contexts/sales-forecasting/<empresa>/<empresa>_sales.csv`; no lo generes ni lo simules.
5. Lee tu `CONTEXT-empresa.md` completo antes de escribir código: ahí están el significado de cada columna, el rango de fechas y el patrón de estacionalidad que el dataset ya refleja.

---

## 💻 Qué Debes Hacer

**Preparación de datos**

- [ ] Carga el dataset de ventas históricas de tu empresa desde la ruta correspondiente al entorno donde trabajas: `data/raw/<empresa>_sales.csv` en tu monorepo o `content/contexts/sales-forecasting/<empresa>/<empresa>_sales.csv` en este repositorio de referencia, y verifica que las columnas coincidan con las descritas en tu `CONTEXT-empresa.md`.
- [ ] Trata los valores nulos o vacíos antes de entrenar.
- [ ] Descompón la serie (tendencia / estacionalidad / residual) con `statsmodels.tsa.seasonal_decompose` (o equivalente) y anota brevemente, en un comentario o en tu reporte, si el patrón coincide con lo descrito en tu `CONTEXT-empresa.md`.
- [ ] Construye features conscientes del tiempo: al menos un feature de lag (por ejemplo `t-1`, `t-12`), una estadística rodante (media o desviación estándar sobre una ventana) y un feature de calendario/estacionalidad (mes, trimestre, o codificación cíclica).
- [ ] Calcula cada feature de lag y rolling de forma **causal** (solo con valores pasados, por ejemplo `shift(1)` antes de `rolling()`) — un feature que se asoma a la fila actual o futura invalida todo el pronóstico.
- [ ] Divide el dataset en **entrenamiento** (los primeros 8 años) y **comprobación/prueba** (los 2 años más recientes), de forma que el modelo nunca vea los años de prueba durante el entrenamiento.
- [ ] Escala las variables que lo requieran para evitar comparaciones erróneas entre magnitudes distintas.

**Entrenamiento del modelo**

- [ ] Entrena un modelo usando **XGBoost o Random Forest** (elige uno y documenta por qué) con `scikit-learn`, alimentado con los features conscientes del tiempo que construiste.
- [ ] Documenta en el código o en un comentario el criterio de elección del algoritmo (tamaño de datos, necesidad de explicabilidad, tiempo disponible para ajuste).

**Evaluación**

- [ ] Calcula y reporta al menos las siguientes métricas sobre el conjunto de prueba: **MSE**, **PSI**, **Gini** y **K2 Score**.
- [ ] Explica en el README de tu implementación (o en un comentario) qué mide cada métrica y por qué un MSE bajo no es suficiente por sí solo.

**Visualización**

- [ ] Genera una visualización que muestre la predicción del modelo junto con el área de variabilidad del resultado, comparada contra los datos reales de los 2 años de prueba.

⚠️ **IMPORTANTE:** Los nombres de columnas, el formato del dataset y los valores específicos de tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto de tu empresa no será aceptada.

**Pruebas**

- [ ] Agrega al menos una prueba unitaria en `tests/pipelines/` que valide que el split de entrenamiento/prueba respeta la regla de los 8 años / 2 años y que no hay fuga de datos (_data leakage_) entre ambos conjuntos.
- [ ] Agrega al menos una prueba unitaria en `tests/pipelines/` que valide que tus features de lag/rolling se calculan de forma causal (por ejemplo, que el feature de lag de la fila `t` sea igual al valor crudo en `t-1`, nunca en `t` o después).

---

## ✅ Qué Evaluaremos

- [ ] El split de entrenamiento y prueba respeta la regla 8 años / 2 años y no mezcla datos entre ambos conjuntos.
- [ ] Se construyó y usó al menos un feature de lag, una estadística rodante y un feature de calendario/estacionalidad para entrenar el modelo.
- [ ] Los features de lag y rolling se calculan de forma causal, sin fuga de información desde filas futuras.
- [ ] El modelo entrenado es XGBoost o Random Forest, con la elección justificada explícitamente.
- [ ] Las cuatro métricas (MSE, PSI, Gini, K2 Score) están calculadas y reportadas sobre el conjunto de prueba, no sobre el de entrenamiento.
- [ ] Existe una visualización que muestra la predicción junto con su rango de variabilidad, no solo una línea puntual.
- [ ] El dataset usado es el provisto en `data/raw/<empresa>_sales.csv`, sin alteraciones que rompan el patrón de estacionalidad y crecimiento descrito en el CONTEXT.md de la empresa.
- [ ] La semilla aleatoria (`random_state`/`seed`) está fijada para que el experimento sea reproducible.
- [ ] Ambas pruebas unitarias (regla del split y no fuga en los features) pasan correctamente.

---

## 📦 Cómo Entregar

1. Haz commit de tus cambios con mensajes claros y descriptivos.
2. Sube tu rama a tu fork del monorepo.
3. Abre un **Pull Request** hacia la rama `main` de tu propio fork, describiendo brevemente qué algoritmo elegiste y por qué.
4. Incluye en la descripción del PR las métricas obtenidas sobre el conjunto de prueba.
5. Espera el _review_ de tu tech lead antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Programas de Carrera](https://4geeksacademy.com/es/comparar-programas) de [4Geeks Academy](https://4geeksacademy.com). Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Encuentra más acerca de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/ciberseguridad) y [Desarrollador Full-Stack con IA](https://4geeksacademy.com/es/coding-bootcamps/full-stack-developer).
