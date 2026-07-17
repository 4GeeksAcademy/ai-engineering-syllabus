# Hito 9 — Generación de Flujos de Trabajo Agénticos (Parte 2 de 3): Generación de Respuestas a RFPs

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** antes de escribir cualquier línea de código — allí están los lineamientos concretos contra los que deben validar tus agentes evaluadores.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

En la Parte 1 ya tienes un flujo que clasifica cada RFP y abre un ticket por cada una, dejándole claro a Ventas qué le toca a cada departamento. Ahora Ventas quiere ir un paso más allá: que ese análisis se convierta directamente en un primer borrador de la propuesta económica, revisado automáticamente antes de que un humano lo vea.

> **Ticket — Generación y evaluación de respuestas a RFP**
>
> > **Contexto:** La Parte 1 nos dice qué hay que responder en cada RFP, pero armar el borrador de la propuesta económica sigue siendo manual y lento. Necesito que el sistema genere un primer borrador por departamento y que ese borrador se autoevalúe antes de llegar a un humano.
> >
> > **Qué necesito que construyas:**
> >
> > - Un agente generador por departamento que reciba los metadatos y el resumen producidos en la Parte 1, y redacte la sección correspondiente de la propuesta económica.
> > - Varios agentes evaluadores corriendo en paralelo sobre cada sección generada: legibilidad (de nuevo, `py-readability-metrics` te sirve para esto), pertinencia respecto a lo que pide la RFP, y cumplimiento de nuestros lineamientos de empresa.
> > - Si una sección falla la evaluación, que vuelva al generador correspondiente con feedback concreto sobre qué corregir — no que se quede atascada ni que se descarte el ticket completo.
> > - Un límite de iteraciones para ese ciclo generador-evaluador, para que no se repita indefinidamente si un generador no logra pasar la evaluación.
> > - _Opcional:_ si ya tienes montada la base de conocimiento semántica de la empresa, dale acceso al generador — que redacte con nuestras políticas y tono reales en lugar de improvisarlos ayuda mucho a que pase la evaluación de cumplimiento a la primera. No es indispensable para esta parte, pero si la tienes disponible, úsala.
> >
> > **Acceptance criteria:** El _handoff_ hacia la Parte 3 debe incluir, por cada departamento, tanto el contenido generado como el resultado de su evaluación.
> >
> > — Tu tech lead

### 📚 Conocimiento complementario: cumplimiento de lineamientos

Cuando el ticket pide que un evaluador revise "cumplimiento de lineamientos de la empresa", no se refiere a un juicio de estilo libre: tu `CONTEXT-company.md` incluye una lista concreta de reglas (tono, datos que no pueden faltar, cifras que deben aparecer) contra la cual el evaluador debe verificar el contenido generado — no una opinión subjetiva del agente. Si tu empresa ya tiene una base de conocimiento semántica, es un buen lugar para que el generador busque políticas, precios de referencia o lenguaje de marca reales antes de redactar — reduce las veces que el evaluador rebota la sección por inventar algo que no coincide con lo que la empresa realmente dice. Esto es una mejora sugerida, no un requisito de esta parte.

### 🗺️ Referencia visual: mapeo departamental y finalización del entregable

Este tramo del flujo toma la **estructura de workstreams definida** en la Parte 1, mapea tareas a departamentos vía un **assignment orchestrator**, ejecuta generación por departamento en paralelo, y un **synthesizer** consolida las salidas en tickets de asignación por departamento listos para evaluación / aprobación:

![Mapeo departamental y finalización del entregable: el assignment orchestrator mapea workstreams a Sales, Legal & Compliance y Operations & Delivery; el synthesizer produce tickets de asignación por departamento](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-evaluate/.learn/departmental-mapping-deliverable-finalization.jpg)

---

## 🌱 Cómo Empezar el Proyecto

Continúa sobre la misma rama de trabajo del Hito 9 en tu fork del monorepo (o crea `feature/hito-9-parte-2-generacion-respuestas` a partir de la rama donde entregaste la Parte 1). Si aún no tienes tu fork, créalo desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Parte del flujo de clasificación y enrutamiento que construiste en la Parte 1 — no lo reescribas desde cero.
2. Instala cualquier dependencia nueva con `uv add`.
3. Revisa nuevamente tu `CONTEXT-company.md`: allí están los lineamientos concretos contra los que deben validar tus agentes evaluadores.

---

## 💻 Lo Que Debes Hacer

**Generación por departamento**

- [ ] Implementa un agente generador por departamento que reciba el resumen relevante producido en la Parte 1
- [ ] El agente generador debe producir contenido específico para la sección de propuesta económica de su departamento

> 💡 _Opcional:_ si tu empresa ya tiene una base de conocimiento semántica, puedes darle acceso al generador para que redacte con políticas y lenguaje de marca reales. No es un requisito de esta parte ni se evalúa como tal — es una mejora que puede reducir cuántas veces una sección rebota en la evaluación.

**Evaluación en paralelo**

- [ ] Implementa múltiples agentes evaluadores que corran en paralelo sobre cada sección generada
- [ ] Al menos un evaluador debe revisar legibilidad (se sugiere `py-readability-metrics`)
- [ ] Al menos un evaluador debe revisar pertinencia (que el contenido responda lo que pide la RFP)
- [ ] Al menos un evaluador debe revisar cumplimiento de los lineamientos definidos en tu `CONTEXT-company.md`

**Ciclo generador-evaluador**

- [ ] Si una sección falla la evaluación, el flujo debe devolverla al agente generador correspondiente junto con las razones del fallo
- [ ] Define y aplica un límite de iteraciones para evitar que el ciclo generador-evaluador se repita indefinidamente

**Estado del ticket**

- [ ] Actualiza el ticket creado en la Parte 1 para reflejar el progreso de la generación y evaluación (por ejemplo: `generando_borrador`, `en_evaluación`)

⚠️ **IMPORTANTE:** Los lineamientos de la empresa contra los que evalúas el contenido generado, y el formato esperado de cada sección, deben coincidir con lo especificado en tu `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

**Pruebas**

- [ ] Incluye pruebas unitarias en `tests/pipelines/` para al menos un agente generador y un agente evaluador, incluyendo el caso donde la evaluación falla

---

## 🧭 Preguntas de Diseño

- ¿Qué información del estado necesita realmente cada agente evaluador? ¿Le estás pasando solo la sección que debe revisar o el documento completo?
- ¿Cómo evitas que dos evaluadores en paralelo entren en conflicto al escribir su resultado en el estado compartido?
- ¿Qué pasa si un agente generador alcanza el límite de iteraciones sin pasar la evaluación? ¿Qué le muestra el ticket a Ventas en ese caso?
- ¿El feedback que recibe el generador tras un fallo es lo suficientemente específico como para corregir el problema real, o es genérico?

---

## ✅ Lo Que Evaluaremos

- [ ] Cada departamento tiene su propio agente generador, claramente separado de los demás
- [ ] Los evaluadores corren en paralelo y no bloquean la ejecución de otros departamentos entre sí
- [ ] El sistema aplica correctamente el ciclo generador-evaluador, incluyendo el límite de iteraciones
- [ ] El ticket refleja con precisión el progreso de generación y evaluación en tiempo real
- [ ] Los criterios de evaluación (legibilidad, pertinencia, lineamientos) están implementados de forma verificable, no como texto libre sin estructura
- [ ] Existen pruebas unitarias que cubren tanto el caso de éxito como el de fallo en la evaluación
- [ ] La implementación usa los lineamientos y formatos definidos en el `CONTEXT-company.md` de tu empresa

---

## 📦 Cómo Entregar

Esta es la Parte 2 de 3 del Hito 9. Entrégala con su propio Pull Request — no esperes a tener la Parte 3 lista.

1. Haz commit y push de tu rama `feature/hito-9-parte-2-generacion-respuestas`
2. Abre un Pull Request describiendo qué implementaste y cómo probarlo
3. Incluye en la descripción del PR un ejemplo de sección generada: uno que pase evaluación y uno que falle
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
