# Evaluación de un Modelo de Regresión

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/sales-forecasting)** — necesitas los datos de ventas de tu empresa para poder interpretar el costo real de los errores de tu modelo.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya entrenaste un modelo de regresión para predecir las ventas de tu empresa y ajustaste sus hiperparámetros. Pero un modelo entrenado no es lo mismo que un modelo confiable: tu tech lead ha abierto un **ticket** pidiendo una **evaluación técnica formal** antes de aprobar su paso a staging. Nadie va a promover un modelo a producción solo porque "el error final se ve bien".

El ticket es específico y trae tres preguntas que tu reporte debe responder sin ambigüedad:

1. ¿El modelo tiene **underfitting**, **overfitting**, o está razonablemente bien ajustado?
2. ¿Qué tan **estable** es su desempeño si cambias qué porción de los datos usas para entrenar?
3. Si hay un problema, ¿cuál es la **acción correctiva específica** — no genérica — que se debería tomar?

Responder "el modelo funciona bien" sin evidencia no es una evaluación técnica, es una opinión. Tu reporte debe estar respaldado por curvas de aprendizaje, validación cruzada y métricas justificadas.

### 📚 Conocimiento complementario: sesgo, varianza y curvas de aprendizaje

Un modelo con **underfitting** falla incluso con los datos de entrenamiento: no capturó el patrón. Un modelo con **overfitting** memoriza el ruido de entrenamiento y falla al generalizar. La forma más confiable de diagnosticar cuál de los dos está pasando (o si no está pasando ninguno) es una **curva de aprendizaje**: graficar el error de entrenamiento y el error de validación a medida que aumenta el tamaño del set de entrenamiento.

- Si ambas curvas convergen en un error **alto** → underfitting. La solución típica es aumentar la complejidad del modelo o revisar la calidad de las features — nunca agregar más datos como primera respuesta.
- Si hay una **brecha amplia y persistente** entre entrenamiento (bajo) y validación (alto) → overfitting. La solución típica es regularización, reducir complejidad, o más datos — nunca aumentar la complejidad como primera respuesta.
- Si ambas curvas convergen en un error **bajo y cercano** entre sí → el modelo está razonablemente bien ajustado.

No existe una curva "correcta" universal — lo que importa es el patrón relativo entre las dos líneas.

---

## 🌱 Cómo Empezar el Proyecto

1. Continúa en tu copia existente del [monorepo de la empresa](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) que te fue asignada al inicio del curso (si aún no tienes una, haz fork del repositorio).
2. Clona tu fork y crea una rama para este trabajo.
3. Confirma que el modelo entrenado y el split temporal (8 años entrenamiento / 2 años prueba) de tu proyecto anterior siguen disponibles y son reproducibles.
4. Instala cualquier dependencia adicional con `uv add` — nunca uses `pip install` ni `pipenv`.
5. Lee tu `CONTEXT-empresa.md` para entender qué error es más costoso para tu negocio: sobreestimar ventas o subestimarlas.

---

## 💻 Qué Debes Hacer

**Validación cruzada respetando el tiempo:**

- [ ] Implementa una estrategia de validación cruzada temporal (por ejemplo `TimeSeriesSplit`) con al menos 5 folds sobre el set de entrenamiento.
- [ ] Verifica explícitamente que ningún fold mezcla o baraja los datos — el orden cronológico debe preservarse en cada fold.
- [ ] Reporta la métrica elegida como **media ± desviación estándar** a través de los folds, no solo un número agregado.

**Curva de aprendizaje:**

- [ ] Genera una curva de aprendizaje que grafique el error de entrenamiento y el error de validación a medida que crece el tamaño del set de entrenamiento.
- [ ] Guarda la imagen resultante en `data/eval/`.

**Selección y cálculo de métricas:**

- [ ] Calcula **MAE** y **RMSE** para entrenamiento y validación.
- [ ] Justifica por escrito cuál de las dos refleja mejor el costo de negocio de tus errores, según lo que indica tu `CONTEXT-empresa.md`.

⚠️ **IMPORTANTE:** Los nombres de campos, IDs de entidades y valores específicos de dominio en tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

**Diagnóstico y reporte técnico:**

- [ ] Redacta un reporte técnico (`data/eval/evaluation_report.md`) que clasifique explícitamente el modelo como **bien ajustado**, **underfitting** u **overfitting**, respaldado por la curva de aprendizaje y los resultados de validación cruzada.
- [ ] Propón una acción correctiva concreta y coherente con el diagnóstico — no una respuesta genérica como "agregar más datos" o "aumentar la complejidad" sin justificar por qué esa es la causa raíz.

**Pruebas:**

- [ ] Escribe un test unitario en `tests/pipelines/` que valide que la estrategia de validación cruzada temporal preserva el orden cronológico de los datos en cada fold (ningún índice de un fold posterior aparece antes que uno de un fold anterior).

---

## ✅ Qué Evaluaremos

- [ ] La curva de aprendizaje está generada correctamente y su patrón (underfitting / overfitting / buen ajuste) está interpretado de forma explícita en el reporte.
- [ ] La validación cruzada temporal no baraja los datos y reporta media ± desviación estándar.
- [ ] Se calculan y comparan al menos dos métricas de regresión, con una justificación de negocio para la elegida como principal.
- [ ] El reporte da un diagnóstico explícito (bien ajustado / underfitting / overfitting) respaldado por evidencia, no solo una afirmación.
- [ ] La acción correctiva propuesta es específica y coherente con el diagnóstico dado — no una recomendación genérica.
- [ ] El test unitario sobre el orden cronológico de los folds pasa correctamente.

---

## 📦 Cómo Entregar

1. Haz commit y push de tus cambios a tu fork.
2. Abre un Pull Request hacia la rama principal de tu copia del monorepo.
3. En la descripción del PR, resume tu diagnóstico en una o dos frases (por ejemplo: "El modelo muestra overfitting moderado; recomiendo regularización antes de aumentar el dataset").
4. Verifica que el test unitario pase en CI antes de solicitar revisión.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Programas de Carrera](https://4geeksacademy.com/es/comparar-programas) de [4Geeks Academy](https://4geeksacademy.com). Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Encuentra más acerca de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/ciberseguridad) y [Desarrollador Full-Stack con IA](https://4geeksacademy.com/es/coding-bootcamps/full-stack-developer).
