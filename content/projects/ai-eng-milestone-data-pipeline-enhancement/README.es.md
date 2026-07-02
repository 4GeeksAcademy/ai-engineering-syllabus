# Hito 6 — Mejora del pipeline de datos de la compañía: Subflows y tests (3/3)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de comenzar**: Asegúrate de haber completado la **[Parte 2 del Hito 6](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/ai-eng-milestone-data-pipeline-build)** — este proyecto parte directamente de `data/pipelines/pipeline.py` implementado en la sesión anterior.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Esta es la **Parte 3 del Hito 6 — Telemetría y Data Pipelines**. El pipeline base ya funciona. Hoy lo llevas al nivel de producción: refactorizas el flow principal en subflows reutilizables, añades tests unitarios que validan el comportamiento de las tasks de transformación, y completas el deployment en Docker con schedule.

Tu CTO ha actualizado el ticket:

> > **Ticket de mejoras — Pipeline en producción**
> >
> > El pipeline básico está listo. Antes del handoff definitivo al equipo de operaciones, necesito tres cosas más:
> >
> > 1. El flow principal está creciendo — refactorízalo en subflows para que cada fase sea independiente, testeable y reutilizable.
> > 2. Necesito tests unitarios para las tasks de transformación. Si un test falla, quiero saberlo antes de que el pipeline llegue a producción, no después.
> > 3. El pipeline debe tener un deployment funcional en Docker con su schedule. Cuando yo ejecute `prefect deployment run`, quiero ver el resultado en Prefect Cloud.
> >
> > Punto de partida: `data/pipelines/pipeline.py` de la sesión anterior.

### Por qué subflows

Un flow que crece sin estructura acaba siendo tan difícil de mantener como el script que reemplazó. Los subflows aplican el principio DRY al nivel de la orquestación: cada fase del pipeline (extracción, transformación, carga) se convierte en un flow independiente que puede ejecutarse, monitorizarse y reutilizarse por separado. El flow principal los coordina, pero no contiene su lógica.

---

## 🌱 Cómo Empezar

1. Haz un `git pull` en tu fork del monorepo.
2. Abre `data/pipelines/pipeline.py` — es tu punto de partida.
3. Mantén la estructura de carpetas existente: `data/pipelines/` para flows y subflows, `data/process/` para lógica de transformación, `data/raw/` para datos de entrada, `data/eval/` para outputs de validación.
4. Los tests unitarios van en `tests/pipelines/` en la raíz del monorepo.

---

## 💻 Qué Debes Hacer

### Fase 1 — Refactorización en subflows

- [ ] Divide el flow principal en al menos tres subflows (`@flow`) que se correspondan con las etapas de tu diseño: uno para extracción, uno para transformación y uno para carga. El flow principal los invoca en secuencia.
- [ ] Cada subflow debe tener entradas y salidas explícitas — no dependas de variables globales entre subflows.
- [ ] Si tienes pasos opcionales (notificaciones, exportaciones secundarias), extráelos también como subflows con `allow_failure=True` en la invocación desde el flow principal.

### Fase 2 — Tests unitarios

- [ ] Crea el archivo `tests/pipelines/test_pipeline.py` con tests unitarios para al menos tres tasks de transformación.
- [ ] Cada test debe verificar el comportamiento de la task de forma aislada: no debe depender de base de datos ni de APIs externas. Usa datos de prueba en memoria.
- [ ] Incluye al menos un test que verifique el comportamiento defensivo de una task ante entrada inválida o malformada (por ejemplo, un campo nulo donde no se espera, un tipo incorrecto).
- [ ] Los tests deben poder ejecutarse con `python -m pytest tests/pipelines/test_pipeline.py` sin errores.

### Fase 3 — Scheduling y deployment en Docker

- [ ] Revisa el schedule definido en la sesión anterior y confirma que sigue siendo el más adecuado para el ciclo de datos de tu empresa. Si lo cambias, justifícalo en un comentario.
- [ ] Genera o actualiza el deployment de Prefect con infraestructura Docker como work pool. El deployment debe incluir nombre, schedule, work pool y las variables de entorno necesarias.
- [ ] Verifica el deployment desde la CLI: `prefect deployment run <nombre-del-flow>/<nombre-del-deployment>` debe arrancar el flow sin errores.
- [ ] Documenta en un comentario o en el propio `data/pipelines/PIPELINE_DESIGN.md` cómo pausar y reanudar el schedule: `prefect deployment pause-schedule` / `prefect deployment resume-schedule`.

⚠️ **IMPORTANTE:** Los nombres de subflows, tasks y tests deben seguir el mismo vocabulario de dominio definido en `data/pipelines/PIPELINE_DESIGN.md`. Un subflow llamado `extract_data` no es aceptable si tu empresa tiene entidades concretas — llámalo `extract_sales_events` o el nombre que corresponda.

---

## ✅ Qué Evaluaremos

- [ ] El flow principal en `data/pipelines/pipeline.py` invoca al menos tres subflows (`@flow`) en lugar de contener toda la lógica directamente.
- [ ] Cada subflow tiene entradas y salidas explícitas y puede ejecutarse de forma independiente.
- [ ] El archivo `tests/pipelines/test_pipeline.py` existe y contiene al menos tres tests unitarios para tasks de transformación.
- [ ] Al menos un test verifica el comportamiento defensivo de una task ante entrada inválida.
- [ ] `python -m pytest tests/pipelines/test_pipeline.py` pasa sin errores.
- [ ] El deployment de Prefect tiene infraestructura Docker configurada como work pool y un schedule definido.
- [ ] `prefect deployment run <nombre-del-flow>/<nombre-del-deployment>` arranca el flow sin errores.
- [ ] Los nombres de subflows, tasks y tests reflejan el vocabulario de dominio de `data/pipelines/PIPELINE_DESIGN.md`.

---

## 📦 Cómo Entregar

1. Asegúrate de que `data/pipelines/pipeline.py` y `tests/pipelines/test_pipeline.py` están en tu fork del monorepo.
2. Haz commit con el mensaje: `feat: refactor pipeline into subflows and add unit tests`.
3. Abre un Pull Request con estos cambios — puede ir sobre el PR de la Parte 2 o ser uno nuevo. Comparte la URL con tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
