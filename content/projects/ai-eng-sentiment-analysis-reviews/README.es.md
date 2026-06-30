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

No tienes tiempo (ni los datos) para entrenar un modelo desde cero — y no lo necesitas. Hay muchos modelos preentrenados en Hugging Face que ya saben leer sentimiento en texto. Tu trabajo es elegir el correcto, integrarlo bien, y convertir texto crudo en algo que la account manager pueda realmente usar.

> La account manager te compartió esto por correo:
>
> "Le vamos a entregar a este cliente 500 reseñas escritas la próxima semana. Necesito saber, en términos simples, cuántas de estas reseñas se leen como positivas, neutrales o negativas — y si esa distribución coincide con su promedio de 4.5 estrellas. Si hay una diferencia, quiero entender de dónde viene antes de ponerlo frente al cliente."

**Modelo a utilizar:** [`prajjwal1/bert-mini`](https://huggingface.co/prajjwal1/bert-mini) de Hugging Face.

#### Una nota sobre cómo integrar el modelo

No descargues los pesos del modelo y los subas a tu repositorio — eso lo va a inflar innecesariamente y no es así como se trabaja en un equipo real. En vez de eso, carga el modelo en tiempo de ejecución usando `pipeline()` o `from_pretrained()`. La primera vez que lo ejecutes, se descarga y se cachea localmente (`~/.cache/huggingface`); cada ejecución posterior reutiliza ese caché. Mantén tu repo limpio — debe contener tu código y tus datos, no binarios de modelos.

⚠️ **IMPORTANTE:** Fija (pin) el nombre/versión del modelo que cargas — no dependas silenciosamente de lo que sea que "latest" resuelva cuando otra persona clone tu repo.

Antes de confiar en cualquier resultado, toma una muestra de reseñas y léelas tú mismo/a. ¿La etiqueta del modelo coincide con tu propia lectura del texto? Un modelo solo es útil una vez que lo has verificado contra la realidad.

---

## 🌱 Cómo Iniciar el Proyecto

> Haz fork o clona el siguiente repositorio antes de comenzar: [github.com/4GeeksAcademy/python-hello](https://github.com/4GeeksAcademy/python-hello)

1. Crea tu propio repositorio a partir de la plantilla (no hagas fork directo — usa "Use this template" o clona y sube a un repo nuevo en tu propia cuenta).
2. Ábrelo en GitHub Codespaces, o clónalo localmente si prefieres trabajar en tu propia máquina.
3. Descarga el archivo [reviews.csv](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/ai-eng-sentiment-analysis-reviews/reviews.csv) desde la plataforma y colócalo en una carpeta `data/` dentro de tu repositorio.
4. Lee las [instrucciones completas sobre cómo iniciar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project) si esto es nuevo para ti.

---

## 💻 Qué Debes Hacer

- [ ] Configura tu entorno e instala las librerías necesarias (por ejemplo, `transformers` y un backend como `torch`) — fija las versiones en tu archivo de dependencias.
- [ ] Carga las 500 reseñas del dataset proporcionado.
- [ ] Carga `prajjwal1/bert-mini` con `pipeline()` o `from_pretrained()` — cárgalo una sola vez, no dentro de un loop que lo re-descargue o re-instancie por cada reseña.
- [ ] Ejecuta la inferencia de sentimiento sobre cada reseña y guarda la etiqueta predicha junto a cada reseña.
- [ ] Calcula la distribución general de sentimiento (por ejemplo, % positivo / neutral / negativo).
- [ ] Compara esa distribución con el promedio de 4.5 estrellas del negocio. ¿Coincide? ¿Dónde no coincide?
- [ ] Inspecciona manualmente una muestra de predicciones (al menos 15–20 reseñas) y anota los casos donde la etiqueta del modelo te parezca incorrecta. No te saltees esto — así es como detectas un modelo que está fallando silenciosamente.
- [ ] Escribe un reporte breve en un archivo markdown que la account manager pueda realmente entregarle a un cliente: total de reseñas analizadas, distribución de sentimiento, comparación con la puntuación en estrellas, y cualquier discrepancia encontrada junto con tu hipótesis de por qué ocurre.

---

## ✅ Qué Vamos a Evaluar

- [ ] El modelo está integrado mediante `pipeline()`/`from_pretrained()` — los pesos del modelo **no** están subidos al repositorio.
- [ ] Las 500 reseñas fueron procesadas y tienen una predicción de sentimiento asociada.
- [ ] La versión/nombre del modelo está fijada (pinned), no dependiendo de "latest".
- [ ] El modelo se carga una sola vez y se reutiliza, no se recarga en cada reseña.
- [ ] Se calcula la distribución de sentimiento y se compara explícitamente con el promedio de 4.5 estrellas.
- [ ] Hay evidencia de verificación manual — ejemplos específicos de predicciones revisadas a mano, con notas sobre si tenían sentido.
- [ ] El reporte final es lo suficientemente claro como para que una account manager no técnica pueda entender la conclusión y el razonamiento detrás de ella.

> **Nota:** No estamos evaluando arquitectura, entrenamiento ni fine-tuning del modelo — estás integrando un modelo existente, no construyendo uno.

---

## 📦 Cómo Entregar

Sube tu código a tu propio repositorio de GitHub, asegúrate de que tu reporte de sentimiento esté incluido en el repo (no solo impreso en tu terminal y descartado), y entrega el link de tu repositorio siguiendo el proceso de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
