# Análisis de Sentimiento en Reseñas de Clientes — WeLoveReviews

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/repo-name/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de código.

<!-- endhide -->

---

## 🎯 Tu Reto

Trabajas como ingeniero/a de IA freelance para una pequeña consultora de datos. Tu último cliente, **WeLoveReviews**, ayuda a empresas a entender lo que realmente piensan sus clientes. Acaban de incorporar una nueva cuenta: un negocio con una puntuación promedio de **4.5 / 5**, pero la account manager tiene una duda que no la deja tranquila — _¿el sentimiento expresado en las reseñas escritas realmente coincide con esa puntuación?_ Antes de entregarle un reporte a su cliente, quieren una segunda opinión basada en datos, no en intuición.

No tienes tiempo (ni los datos) para entrenar un modelo desde cero — y no lo necesitas. Hay muchos modelos preentrenados en Hugging Face que ya saben leer sentimiento en texto. Tu trabajo es explorar los datos, integrar uno correctamente, validar su resultado contra la realidad, y convertir texto crudo en algo que la account manager pueda realmente usar.

> La account manager te compartió esto por correo:
>
> "Le vamos a entregar a este cliente 500 reseñas escritas la próxima semana. Necesito saber, en términos simples, cuántas de estas reseñas se leen como positivas, neutrales o negativas — y si esa distribución coincide con su promedio de 4.5 estrellas. Si hay una diferencia, quiero entender de dónde viene antes de ponerlo frente al cliente."

---

## 📓 Cómo se comunica este equipo

En este equipo, los líderes tratan los **notebooks de Jupyter como documentos de comunicación** para análisis y procesamiento de datos — no como borradores descartables. Tu entregable narrativo es **`src/explore.ipynb`**: un notebook ejecutado que guía al lector desde los objetivos hasta la exploración, los insights, las decisiones de modelado, los resultados y las conclusiones. Se espera markdown breve entre bloques de código importantes; el notebook debe sostenerse por sí solo sin un informe markdown aparte para el cliente.

> **Orden de trabajo:** Puedes ejecutar primero el prompt de EDA y luego anteponer los objetivos y continuar con el resto del proyecto en el **mismo** `src/explore.ipynb`, para que el archivo final siga el arco completo descrito abajo.

---

## 🤖 Nota sobre el modelo

**Modelo a utilizar:** [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) de Hugging Face.

> ⚠️ **Desajuste de dominio:** Este modelo fue fine-tuneado sobre **reseñas de productos** (p. ej. estilo Amazon). Tu dataset contiene **reseñas de servicios** — los clientes hablan del personal, tiempos de espera y ambiente. Ese desajuste puede producir **falsos negativos**: reseñas que a un humano leen como positivas (o tienen alta puntuación en estrellas) pero el modelo las clasifica con bajo sentimiento. Debes usar este modelo primero de todos modos — encontrar y explicar esos falsos negativos es parte del ejercicio.

Este modelo predice el sentimiento como una **puntuación de 1 a 5 estrellas** (no una etiqueta simple POSITIVO/NEGATIVO). Mapea la salida a bandas de sentimiento:

| Predicción del modelo | Banda de sentimiento |
| --------------------- | -------------------- |
| 1–2 estrellas         | Negativo             |
| 3 estrellas           | Neutral              |
| 4–5 estrellas         | Positivo             |

**Reglas de integración:**

- Carga el modelo con `pipeline()` o `from_pretrained()` — **no** descargues los pesos y los subas al repositorio.
- Carga el modelo **una sola vez** antes del loop de inferencia, no dentro de un loop por reseña.
- **Fija** (pin) el nombre/versión del modelo en tu código — no dependas silenciosamente de lo que sea que "latest" resuelva cuando otra persona clone tu repo.

---

## 🌱 Cómo Iniciar el Proyecto

1. Haz fork del repositorio [machine-learning-python-template](https://github.com/4GeeksAcademy/machine-learning-python-template) y, si tienes la opción, selecciona la cuenta de 4GeeksAcademy.
2. Ábrelo en GitHub Codespaces, o clónalo localmente si prefieres trabajar en tu propia máquina.
3. Descarga el archivo [reviews.csv](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/existing-model-sentiment-analysis-reviews/reviews.csv) desde la plataforma y colócalo en **`data/raw/reviews.csv`** en tu repositorio.
4. Extiende **`requirements.txt`** con `transformers` y `torch` (o el backend que elijas) — **fija las versiones**.
5. Lee las [instrucciones completas sobre cómo iniciar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project) si esto es nuevo para ti.

---

## 🧪 EDA con tu agente de código

Antes de modelar, explora el dataset con ayuda de tu agente de código:

1. Abre **[PROMPT.es.md](./PROMPT.es.md)** en la carpeta de este proyecto.
2. Copia todo lo que está debajo de la línea del encabezado en tu agente (Cursor, Copilot, Claude Code, etc.).
3. Deja que el agente trabaje en la **sección de EDA** de **`src/explore.ipynb`** — solo exploración, insights y propuesta de limpieza.

El prompt se detiene después de la EDA. Todo lo que sigue abajo es tu responsabilidad en el mismo notebook y en `src/app.py`.

---

## 💻 Qué Debes Hacer

Completa el arco completo del notebook en **`src/explore.ipynb`** (con **salidas ejecutadas**):

- [ ] **Objetivos** — enmarca la pregunta de negocio (sentimiento escrito vs promedio de 4.5 estrellas).
- [ ] **EDA / insights / limpieza** — usa la salida del prompt del agente; markdown breve entre pasos.
- [ ] **Plan de acción + justificación del modelo** — justifica los siguientes pasos a partir de tus insights; comprométete con el modelo `nlptown` fijo y el mapeo descrito arriba.
- [ ] **Inferencia sobre las 500 reseñas** — carga el modelo una sola vez; guarda estrellas predichas y bandas de sentimiento por reseña.
- [ ] **Desglose vs promedio de 4.5 estrellas** — calcula % positivo / neutral / negativo; compáralo con la puntuación del negocio; explica las diferencias.
- [ ] **Falsos negativos** — encuentra reseñas donde el modelo predice 1–2 estrellas pero la puntuación humana es 4–5 (o donde tú lees el texto como positivo/neutral pero el modelo no está de acuerdo); documenta ejemplos y patrones compartidos.
- [ ] **Muestra manual (15–20 reseñas)** — inspecciona predicciones a mano; anota casos donde la etiqueta parezca incorrecta.
- [ ] **Conclusiones** — takeaway en lenguaje claro que la account manager pueda usar.

**Entregables de producción:**

- [ ] Migra la lógica de inferencia limpia a **`src/app.py`** (patrón del template: notebook para la historia, script para producción).
- [ ] Escribe la salida enriquecida en **`data/processed/reviews_with_sentiment.csv`**.
- [ ] Fija las dependencias en **`requirements.txt`**.

---

## ✅ Qué Vamos a Evaluar

- [ ] **`src/explore.ipynb`** se entrega **con salidas ejecutadas** y un arco narrativo claro: objetivos → EDA → limpieza → plan/modelo → resultados/conclusiones.
- [ ] Aparece markdown transicional breve entre bloques de código importantes.
- [ ] El modelo está integrado mediante `pipeline()`/`from_pretrained()` — los pesos del modelo **no** están subidos al repositorio.
- [ ] Las 500 reseñas fueron procesadas y tienen una predicción de sentimiento asociada.
- [ ] La versión/nombre del modelo está fijada (pinned), no dependiendo de "latest".
- [ ] El modelo se carga una sola vez y se reutiliza, no se recarga en cada reseña.
- [ ] Se calcula la distribución de sentimiento y se compara explícitamente con el promedio de 4.5 estrellas.
- [ ] Hay evidencia de verificación manual — ejemplos específicos de predicciones revisadas a mano, con notas sobre si tenían sentido.
- [ ] Los falsos negativos están identificados y analizados — ejemplos documentados con una hipótesis sobre por qué el modelo de reseñas de productos clasificó mal texto de reseñas de servicios.
- [ ] **`src/app.py`** ejecuta la ruta de inferencia de producción y escribe **`data/processed/reviews_with_sentiment.csv`**.
- [ ] Las dependencias están fijadas en **`requirements.txt`**.

> **Nota:** No estamos evaluando arquitectura, entrenamiento ni fine-tuning del modelo — estás integrando un modelo existente, no construyendo uno. **No** buscamos un informe markdown aparte para el cliente; el notebook es tu artefacto de comunicación.

---

## 📦 Cómo Entregar

Sube tu código a tu propio repositorio de GitHub. Asegúrate de incluir **`src/explore.ipynb`** (con salidas), **`src/app.py`** y **`data/processed/reviews_with_sentiment.csv`** — no solo impresos en tu terminal y descartados. Entrega el link de tu repositorio siguiendo el proceso de entrega de tu instructor.

---

## 🔍 Extensión Opcional: Encuentra un Mejor Modelo

Una vez completado el análisis anterior, prueba esto por tu cuenta:

1. Ejecuta [`tabularisai/multilingual-sentiment-analysis`](https://huggingface.co/tabularisai/multilingual-sentiment-analysis) sobre las mismas 500 reseñas.
2. Compara: ¿baja la tasa de falsos negativos? ¿Qué reseñas siguen fallando?
3. Escribe un breve addendum **dentro del mismo `src/explore.ipynb`** recomendando si WeLoveReviews debería cambiar de modelo para este cliente — y por qué.

Este paso no se evalúa, pero es el tipo de trabajo que separa a quien integra modelos de un/a ingeniero/a de IA que entiende la **selección de modelos**.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
