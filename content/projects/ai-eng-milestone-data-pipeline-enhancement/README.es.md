# Hito 6 — Mejora del Pipeline de Desempeño de Negocio: Subflows y Tests (3/3)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuyentes](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Asegúrate de haber completado la **Parte 2 del Hito 6** — este proyecto se construye directamente sobre `data/pipelines/pipeline.py` implementado en la sesión anterior. Mantén abierto tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/data-pipelines)** — nombres de KPIs, esquema y audiencia de stakeholders vienen de ahí.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu propia copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la compañía seleccionada al inicio del curso — no en un repositorio nuevo.

Esta es la **Parte 3 del Hito 6 — Telemetría y Data Pipelines**. Tu pipeline de desempeño de negocio ya funciona: lee de `telemetry_events` y produce los KPIs que pidió el liderazgo — los nombrados en tu `CONTEXT-company.md` — sin tocar el sistema técnico de telemetría existente. Hoy lo llevas a nivel de producción: refactorizas el flow principal en subflows reutilizables, agregas tests unitarios que validan el comportamiento de las tasks de transformación, aseguras que el pipeline corra directamente desde la línea de comandos, y — la parte que realmente le importa al liderazgo — pones esos KPIs frente a un dashboard que alguien pueda leer.

> > **Ticket de Mejora — Pipeline a Producción**
> >
> > El pipeline básico está listo. Antes de la entrega final al equipo de operaciones, necesito cuatro cosas más:
> >
> > 1. El flow principal está creciendo — refactorízalo en subflows para que cada fase sea independiente, testeable, y reutilizable.
> > 2. Necesito tests unitarios para las tasks de transformación. Si un test falla, quiero saberlo antes de que el pipeline llegue a producción, no después.
> > 3. El pipeline debe poder correrse como script. Cuando ejecuto `python data/pipelines/pipeline.py`, el flujo ETL completo debe completarse sin errores.
> > 4. Necesito un dashboard. Nadie en el equipo de liderazgo va a consultar un endpoint — pon los KPIs en algún lugar donde realmente puedan mirarlos.
> >
> > Punto de partida: `data/pipelines/pipeline.py` de la sesión anterior.

### Por qué subflows

Un flow que crece sin estructura termina siendo tan difícil de mantener como el script que reemplazó. Los subflows aplican el principio DRY a nivel de orquestación: cada fase del pipeline (extracción, transformación, carga) se convierte en un flow independiente que puede ejecutarse, monitorearse, y reutilizarse por separado. El flow principal los coordina pero no contiene su lógica.

---

## 🌱 Cómo Empezar

1. Corre `git pull` en tu copia del monorepo.
2. Abre `data/pipelines/pipeline.py` — ese es tu punto de partida.
3. Ten a mano tu `CONTEXT-company.md`: los nombres de subflows, tasks, y tests deben reflejar los nombres de KPI de su sección "KPIs a medir" y el esquema que implementaste — no etiquetas genéricas.
4. Mantén la estructura de carpetas existente: `data/pipelines/` para flows y subflows, `data/process/` para lógica de transformación, `data/raw/` para datos de entrada, `data/eval/` para salidas de validación.
5. Los tests unitarios van en `tests/pipelines/` en la raíz del monorepo.
6. La página del dashboard va en `uis/backoffice/`, consumiendo el endpoint `services/reporting/` que ya construiste en la Parte 2.
7. Asegúrate de que Prefect 3 esté instalado desde la Parte 2: `uv add "prefect>=3"`.

---

## 💻 Qué Necesitas Hacer

### Fase 1 — Refactorización en subflows

- [ ] Divide el flow principal en al menos tres subflows (`@flow`) que correspondan a las etapas de tu diseño: uno para extracción (desde `telemetry_events` y cualquier otra tabla de dominio), uno para transformación, y uno para carga (en tu tabla `reporting.business_metrics`). El flow principal los invoca en secuencia.
- [ ] Cada subflow debe tener inputs y outputs explícitos — no dependas de variables globales entre subflows.
- [ ] Si tienes pasos opcionales (notificaciones, exportaciones secundarias), extráelos también como subflows e invócalos con `return_state=True` desde el flow principal.

### Fase 2 — Tests unitarios

- [ ] Crea el archivo `tests/pipelines/test_pipeline.py` con tests unitarios para al menos tres tasks de transformación — las que calculan los KPIs de tu `CONTEXT-company.md`.
- [ ] Cada test debe verificar el comportamiento de la task de forma aislada: no debe depender de una base de datos ni de APIs externas. Usa datos de prueba en memoria con la forma de tus eventos de telemetría (según tu `CONTEXT-company.md`).
- [ ] Incluye al menos un test que verifique el comportamiento defensivo de una task ante un input inválido o malformado (por ejemplo, un campo nulo donde no se espera ninguno, o un tipo incorrecto).
- [ ] Incluye al menos un test que confirme que el valor calculado de un KPI coincide con la definición de tu `CONTEXT-company.md` para un input conocido, calculado a mano.
- [ ] Los tests deben pasar con `python -m pytest tests/pipelines/test_pipeline.py` sin errores.

### Fase 3 — Ejecución basada en script

- [ ] Asegúrate de que `data/pipelines/pipeline.py` pueda ejecutarse directamente como script de CLI (por ejemplo, con un bloque `if __name__ == "__main__"` que invoque el flow principal).
- [ ] Verifica que el pipeline completo corre sin errores: `python data/pipelines/pipeline.py`.
- [ ] Documenta el comando de ejecución en un comentario o en `data/pipelines/PIPELINE_DESIGN.md`.

### Fase 4 — Dashboard de negocio (obligatorio)

Tu pipeline produce KPIs — pero una tabla que nadie mira no es un entregable. Esta fase no es opcional: el liderazgo necesita _ver_ los números de verdad, no consultar un endpoint con curl.

- [ ] Construye una página en `uis/backoffice/` (ej. `/reporting`) que consuma tu endpoint de `services/reporting/` y muestre cada KPI de la sección "KPIs a medir" de tu `CONTEXT-company.md` — un gráfico o una tabla por KPI es suficiente.
- [ ] Etiqueta cada KPI claramente con el mismo nombre que tiene en tu `CONTEXT-company.md`, y muestra el período (semana o mes, según tu frecuencia) que cubren los datos.
- [ ] Este dashboard es de cara al negocio, no una herramienta de desarrollador: debe ser legible para el stakeholder nombrado en tu `CONTEXT-company.md` (ej. el CEO o el gerente de departamento) sin que nada necesite traducción ni explicación.
- [ ] No necesitas pulirlo visualmente — el objetivo es una vista funcional y correctamente etiquetada de datos reales desde `reporting.business_metrics`.

⚠️ **IMPORTANTE:** Los nombres de subflows, tasks, y tests deben seguir el mismo vocabulario de dominio definido en `data/pipelines/PIPELINE_DESIGN.md` y tu `CONTEXT-company.md`. Un subflow llamado `extract_data` no es aceptable si tu compañía tiene entidades concretas y nombres de KPI — nómbralo según la métrica de negocio real que produce este pipeline.

### 🔵 Actividad adicional — Mejoras adicionales de tus preguntas de diseño

- [ ] Vuelve a la sección "Preguntas para Ayudarte a Diseñar el Pipeline" de la Parte 1. Si, al responderlas, identificaste mejoras de resiliencia u observabilidad más allá de lo que ya cubren las Fases 1–3 (por ejemplo, un heartbeat más alerta de silencio, un lock de concurrencia para corridas que se solapan, o un patrón `Idempotency-Key` para reintentos) y todavía no las implementaste, este es el lugar para hacerlo.
- [ ] Por cada mejora que agregues, anota en `data/pipelines/PIPELINE_DESIGN.md` qué pregunta responde y por qué la priorizaste.
- [ ] Esto es opcional — solo tómalo si tu propio documento de diseño realmente señaló algo que valía la pena construir. No inventes una mejora solo para marcar una casilla.

---

## ✅ Qué Vamos a Evaluar

- [ ] El flow principal en `data/pipelines/pipeline.py` invoca al menos tres subflows (`@flow`) en lugar de contener toda la lógica directamente.
- [ ] Cada subflow tiene inputs y outputs explícitos y puede ejecutarse de forma independiente.
- [ ] El archivo `tests/pipelines/test_pipeline.py` existe y contiene al menos tres tests unitarios para tasks de transformación.
- [ ] Al menos un test verifica el comportamiento defensivo de una task ante un input inválido.
- [ ] Al menos un test valida el valor calculado de un KPI contra su definición en `CONTEXT-company.md`.
- [ ] `python -m pytest tests/pipelines/test_pipeline.py` pasa sin errores.
- [ ] `python data/pipelines/pipeline.py` corre el flujo ETL completo sin errores.
- [ ] El comando de ejecución está documentado en `data/pipelines/PIPELINE_DESIGN.md` o en comentarios inline.
- [ ] Los nombres de subflows, tasks, y tests reflejan el vocabulario de dominio y los nombres de KPI de `CONTEXT-company.md`.
- [ ] `telemetry_events` y `services/telemetry/analysis.py` permanecen sin modificar durante toda la refactorización.
- [ ] Existe un dashboard en `uis/backoffice/` que muestra cada KPI de la sección "KPIs a medir" de `CONTEXT-company.md`, correctamente etiquetado, alimentado desde tu endpoint `services/reporting/`.
- [ ] El dashboard es legible para un stakeholder de negocio no técnico, no solo para otro ingeniero.

---

## 📦 Cómo Entregar

1. Asegúrate de que `data/pipelines/pipeline.py`, `tests/pipelines/test_pipeline.py`, y la página del dashboard en `uis/backoffice/` estén commiteados en tu copia del monorepo.
2. Haz commit con el mensaje: `feat: refactor business performance pipeline into subflows, add unit tests, and add reporting dashboard`.
3. Abre un Pull Request con estos cambios — puede construirse sobre el PR de la Parte 2 o ser uno nuevo. En la descripción del PR, menciona si implementaste alguna mejora adicional de las preguntas de diseño, y cuál. Comparte la URL con tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuyentes](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
