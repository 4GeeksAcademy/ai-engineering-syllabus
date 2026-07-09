# Hito 6 — Implementación de un Data Pipeline Resiliente (2/3)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

El documento de diseño del pipeline está aprobado. Ahora toca construirlo. Pero hay una diferencia fundamental entre un script que funciona en tu máquina y un pipeline que puede ejecutarse en producción de forma desatendida: la resiliencia.

Tu CTO ha cerrado el ticket de diseño y ha abierto el de implementación:

> > **Ticket de implementación — Pipeline de datos resiliente**
> >
> > El diseño está aprobado. El equipo de operaciones quiere ver el pipeline corriendo, no solo documentado. Requisitos no negociables antes del handoff a producción:
> >
> > — El pipeline debe tolerar fallos parciales sin interrumpir toda la ejecución.  
> > — Las tareas con datos externos deben tener reintentos configurados.  
> > — El pipeline debe poder ejecutarse como script desde la línea de comandos.  
> > — Si una tarea ya fue ejecutada con éxito en la última hora, no debe repetirse innecesariamente.
> >
> > Punto de partida: tu `data/pipelines/PIPELINE_DESIGN.md` del día anterior. Implementa lo que diseñaste.

### ¿Qué hace resiliente a un pipeline?

Un pipeline resiliente no es el que nunca falla — es el que falla bien. Eso significa tres cosas concretas en Prefect:

- **Tolerancia a fallos parciales**: una tarea que falla no tumba el flow completo. Prefect distingue entre tareas críticas (cuyo fallo debe detener todo) y tareas opcionales (cuyo fallo debe registrarse y continuar).
- **Reintentos inteligentes**: las tareas que interactúan con servicios externos (bases de datos, APIs) se configuran con `retries` y `retry_delay_seconds` para absorber fallos transitorios sin intervención humana.
- **Caché de resultados**: si una tarea ya produjo un resultado válido recientemente, Prefect puede reutilizarlo en lugar de repetir el cómputo. Esto es especialmente útil en transformaciones costosas.

---

## 🌱 Cómo Empezar

1. Haz un `git pull` en tu fork del monorepo.
2. Abre tu `data/pipelines/PIPELINE_DESIGN.md` — ese documento es tu especificación. Implementa lo que diseñaste.
3. Escribe el código del pipeline en `data/pipelines/`. El entry point principal debe llamarse `data/pipelines/pipeline.py`. Usa `data/raw/` para datos de entrada y archivos intermedios, `data/process/` para scripts de transformación reutilizables, y `data/eval/` para los resultados de validación del pipeline.
4. Cualquier endpoint que exponga o dispare el pipeline (por ejemplo, para consultar el estado de la última ejecución o lanzar una ejecución manualmente) debe implementarse en `services/`, importando las funciones y flows desde `data/pipelines/` según sea necesario.
5. Instala Prefect 3 en tu entorno: `uv add "prefect>=3"`.

---

## 💻 Qué Debes Hacer

### Fase 1 — Flows y tasks

- [ ] Implementa el pipeline como uno o más **flows** de Prefect (`@flow`) siguiendo la estructura de etapas de tu diseño: extracción, transformación y carga como mínimo.
- [ ] Cada etapa debe ser una **task** (`@task`) independiente con entradas y salidas explícitas.
- [ ] Si tu pipeline tiene pasos opcionales (por ejemplo, notificaciones o exportaciones secundarias), invócalos con `return_state=True` para que un fallo en ellos no interrumpa la ejecución principal.

### Fase 2 — Resiliencia

- [ ] Añade `retries` y `retry_delay_seconds` a todas las tasks que interactúan con servicios externos (base de datos, APIs). Justifica en un comentario el número de reintentos elegido.
- [ ] Maneja al menos un fallo de task de forma explícita en el flow usando `return_state=True` en lugar de dejarlo propagar automáticamente.
- [ ] Añade caché (`cache_key_fn`, `cache_expiration`) a al menos una task de transformación costosa. Explica en un comentario qué define la clave de caché y durante cuánto tiempo es válida.

### Fase 3 — Idempotencia

- [ ] La fase de carga debe ser idempotente: si el pipeline se ejecuta dos veces sobre el mismo rango de datos, el resultado en base de datos debe ser idéntico tras ambas ejecuciones. Implementa la estrategia que documentaste en tu diseño (upsert, tabla de control, marca de tiempo, u otra).
- [ ] Registra en base de datos o en un archivo de log los metadatos mínimos de cada ejecución: inicio, fin, registros procesados, estado final y cualquier error capturado.

### Fase 4 — Ejecución mediante script

- [ ] Asegúrate de que `data/pipelines/pipeline.py` puede ejecutarse directamente como script CLI (por ejemplo, con un bloque `if __name__ == "__main__"` que invoque el flow principal).
- [ ] Verifica que el pipeline completo se ejecuta sin errores: `python data/pipelines/pipeline.py`.
- [ ] Documenta el schedule previsto para el ciclo de datos de tu empresa en `data/pipelines/PIPELINE_DESIGN.md` y el comando de ejecución en un comentario o en el mismo documento de diseño.

### Fase 5 — Endpoints en el backend

- [ ] En `services/`, implementa al menos dos endpoints relacionados con el pipeline: uno para consultar el estado y los metadatos de la última ejecución, y otro para lanzar una ejecución manual del flow.
- [ ] Los endpoints deben importar los flows o funciones desde `data/pipelines/` — no dupliques la lógica del pipeline en `services/`.
- [ ] Los endpoints siguen las mismas convenciones de autenticación y estructura de respuesta que el resto de tu API.

⚠️ **IMPORTANTE:** Los nombres de flows, tasks, tablas y campos deben coincidir con los definidos en `data/pipelines/PIPELINE_DESIGN.md` y el esquema de telemetría ya existente en tu monorepo. Una implementación genérica que ignore el modelo de datos de tu empresa no será aceptada.

---

## ✅ Qué Evaluaremos

- [ ] El archivo `data/pipelines/pipeline.py` existe y define al menos un flow con tres o más tasks.
- [ ] Al menos una task tiene `retries` configurado con un valor mayor que cero y un comentario que justifica el número elegido.
- [ ] Al menos una task opcional se invoca con `return_state=True` y el flow continúa su ejecución cuando esa task falla.
- [ ] Al menos una task de transformación tiene caché configurado con `cache_key_fn` y `cache_expiration`.
- [ ] La fase de carga es idempotente: ejecutar el pipeline dos veces sobre los mismos datos no produce duplicados en base de datos.
- [ ] Cada ejecución del pipeline registra al menos cinco metadatos (inicio, fin, registros procesados, estado, errores) en base de datos o en un archivo de log estructurado.
- [ ] `python data/pipelines/pipeline.py` ejecuta el flow ETL completo sin errores.
- [ ] El comando de ejecución está documentado en `data/pipelines/PIPELINE_DESIGN.md` o en comentarios inline.
- [ ] Existe al menos un endpoint en `services/` que devuelve los metadatos de la última ejecución del pipeline (estado, inicio, fin, registros procesados).
- [ ] Existe al menos un endpoint en `services/` que dispara una ejecución manual del flow, importando la función desde `data/pipelines/` sin duplicar la lógica.
- [ ] El diseño implementado es coherente con `data/pipelines/PIPELINE_DESIGN.md` — las etapas, entidades y estrategias de resiliencia descritas allí están reflejadas en el código.

---

## 📦 Cómo Entregar

1. Asegúrate de que `data/pipelines/pipeline.py`, los endpoints en `services/` y cualquier archivo de soporte están en tu fork del monorepo.
2. Haz commit con el mensaje: `feat: implement resilient prefect pipeline`.
3. Sube los cambios a tu repositorio en GitHub y comparte la URL con tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
