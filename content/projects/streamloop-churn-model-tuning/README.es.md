# StreamLoop — Ajustando el Modelo de Cancelación

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/python-hello/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Trabajas como ingeniero/a de IA freelance para **StreamLoop**, una plataforma de streaming por suscripción de tamaño mediano. Hace unas semanas entregaste una primera versión de su clasificador de cancelación (churn) — lo entrenaste, revisaste el accuracy, y lo diste por terminado. El tech lead volvió con una observación:

> "El modelo funciona, pero no tengo forma de saber si es realmente bueno o simplemente lo primero que salió de `.fit()`. Antes de que esto se acerque a producción, quiero ver que de verdad buscaste la mejor configuración — no que la adivinaste. Y quiero entender _por qué_ elegiste la versión final, no solo que tuvo un buen puntaje."

Es un pedido justo. Un modelo entrenado con hiperparámetros por defecto rara vez es la mejor versión de sí mismo, y "tuvo un buen puntaje" no es una respuesta válida si no puedes explicar cómo llegaste ahí ni qué tan estable es realmente ese número.

Tu tarea en esta iteración: tomar un clasificador entrenado con los datos de clientes de StreamLoop y ajustarlo de forma sistemática — primero con una búsqueda amplia y económica, luego con una búsqueda precisa y focalizada — evitando los errores que vuelven inútil un proceso de tuning (filtrar el test set dentro de la búsqueda, evaluar con la métrica equivocada, o confiar en un solo número sin revisar cuánto varía entre folds).

#### El dataset

Los datos de clientes de StreamLoop están modelados sobre un conocido dataset público de cancelación de clientes de telecomunicaciones. Cárgalo directamente desde esta URL en tu notebook — no necesitas descargar nada manualmente:

```
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
```

La columna objetivo es `Churn` (`Yes` / `No`). El resto son atributos de cuenta, servicios y facturación de cada cliente.

#### Una nota sobre qué significa "bueno" aquí

StreamLoop pierde mucho más dinero por un cliente que cancela sin que nadie lo detecte, que por un cliente al que se le ofrece una retención que no necesitaba. Ten esto en cuenta al decidir qué optimizar — la métrica que se ve mejor en una tabla de resultados no es automáticamente la que mejor representa el problema de negocio.

---

## 🌱 Cómo Iniciar el Proyecto

1. Haz fork o clona el repositorio plantilla: [https://github.com/4GeeksAcademy/python-hello](https://github.com/4GeeksAcademy/python-hello)
2. Crea tu propio repositorio de GitHub a partir de la plantilla y actualiza el remote URL
3. Ábrelo en GitHub Codespaces, o clónalo localmente si prefieres trabajar en tu propia máquina
4. Instala las librerías necesarias (`scikit-learn`, `pandas`, como mínimo) y comienza un notebook

¿Necesitas un repaso? 📗 [Cómo iniciar un proyecto de programación](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion)

---

## 💻 Qué Debes Hacer

### Línea base

- [ ] Carga el dataset y haz la limpieza mínima necesaria para que sea usable (maneja las columnas que no son numéricas, maneja cualquier valor faltante o vacío)
- [ ] Divide en conjuntos de entrenamiento y test **antes** de hacer cualquier otra cosa con el modelo
- [ ] Construye un `Pipeline` que incluya tus pasos de preprocesamiento y un clasificador de tu elección — el preprocesamiento debe vivir dentro del pipeline, no aplicarse por separado antes
- [ ] Entrena ese pipeline con **hiperparámetros por defecto** y registra su desempeño en el test set — esta es tu línea base, y solo tocas el test set aquí y al final

### Búsqueda

- [ ] Define un espacio de búsqueda de hiperparámetros para tu clasificador elegido, basado en lo que ese modelo realmente soporta
- [ ] Corre un `RandomizedSearchCV` sobre ese espacio primero, usando validación cruzada y `n_jobs=-1`
- [ ] Usa los resultados de la búsqueda aleatoria para acotar el espacio, luego corre un `GridSearchCV` para refinar esa región
- [ ] Elige una métrica de `scoring` que refleje la prioridad de negocio descrita en el reto — no la métrica por defecto de sklearn
- [ ] Deja que `refit=True` (el valor por defecto) reentrene el mejor estimador por ti — no vuelvas a entrenar `best_estimator_` manualmente después

### Selección del modelo final

- [ ] Revisa `cv_results_` para tus mejores candidatos — no te quedes solo con el mejor promedio; observa cuánto varía entre folds
- [ ] Elige tu modelo final y justifica brevemente la elección: ¿es el de mayor promedio, o una opción ligeramente menor pero más estable? Cualquiera de las dos es válida si la explicas
- [ ] Evalúa el modelo final ajustado en el test set exactamente una vez, usando la(s) misma(s) métrica(s) que tu línea base
- [ ] Escribe un `tuning_report.md` breve comparando el desempeño de la línea base contra el modelo ajustado, indicando tus hiperparámetros finales, y explicando la elección de métrica y el trade-off de estabilidad que consideraste

⚠️ **IMPORTANTE:** Nunca ajustes `RandomizedSearchCV` ni `GridSearchCV` sobre el dataset completo — la búsqueda solo debe ver la partición de entrenamiento. El test set se toca exactamente dos veces: una para la línea base, otra para el modelo final ajustado.

---

## ✅ Qué Vamos a Evaluar

- [ ] El preprocesamiento está dentro de un `Pipeline`, no aplicado por separado antes de la división
- [ ] Se entrenó y registró una línea base con hiperparámetros por defecto antes de iniciar cualquier ajuste
- [ ] Se usó `RandomizedSearchCV` para explorar un espacio amplio antes de que `GridSearchCV` lo acotara
- [ ] La búsqueda se corrió con validación cruzada y nunca tocó el test set
- [ ] El parámetro `scoring` se definió de forma deliberada, con una razón indicada y conectada al problema de negocio — no se dejó el accuracy por defecto
- [ ] Se revisó `cv_results_` en busca de variación entre folds, no solo el mejor promedio
- [ ] La elección del modelo final está justificada en el reporte, incluyendo cualquier trade-off considerado
- [ ] Se reporta y compara el desempeño de la línea base y el modelo ajustado usando la(s) misma(s) métrica(s)

> Nota: la elección de arquitectura del modelo (qué clasificador usaste como punto de partida) no se evalúa — lo que importa aquí es el proceso de ajuste y cómo razonas sobre él.

---

## 📦 Cómo Entregar

Sube tu repositorio a GitHub, incluyendo tu notebook y `tuning_report.md`, y comparte el enlace siguiendo las instrucciones de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
