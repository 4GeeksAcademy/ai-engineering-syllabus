# Hito 9 — Generación de Flujos de Trabajo Agénticos (Parte 1 de 3): Recepción y Enrutamiento de RFPs

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** antes de escribir cualquier línea de código — allí se definen los departamentos, el formato de las RFPs y los lineamientos específicos de tu empresa para esta parte del hito.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya construiste un agente capaz de usar herramientas, recordar contexto entre interacciones y orquestarse de forma segura a través de un servidor MCP. Ahora tu empresa necesita que varios agentes trabajen juntos para resolver un problema real de negocio.

El equipo de Ventas recibe cada semana decenas de RFPs (_Request for Proposal_) en PDF de clientes que piden una propuesta económica, y le está costando cumplir los plazos porque cada solicitud requiere involucrar a varios departamentos distintos — y nadie tiene claro, al leer el documento, a quién hay que pedirle qué. Tu tech lead te asigna el siguiente ticket: construir el primer tramo de un flujo agéntico que reciba estas RFPs, determine si realmente lo son, y reparta el trabajo entre los agentes correctos.

> **Ticket — Flujo agéntico de recepción y enrutamiento de RFPs**
>
> > **Contexto:** Ventas está perdiendo plazos porque nadie sabe, al recibir una RFP, qué departamentos debe involucrar ni qué necesita cada uno. Necesitamos automatizar ese primer análisis antes de tocar la generación de la propuesta en sí (eso viene en la siguiente parte).
> >
> > **Qué necesito que construyas:**
> >
> > - Una interfaz en modo ticket donde el equipo suba la RFP (llega siempre en PDF) y vea su estado en tiempo real: analizando, esperando aprobación, terminado...
> > - Las RFPs en PDF pesan mucho y nos van a salir caras en tokens si se las pasamos así a los agentes tal cual. Te sugiero convertirlas a Markdown apenas entran — algo como **MarkItDown** de Microsoft hace bien ese trabajo — antes de que cualquier agente las procese.
> > - Un primer agente clasificador que decida si el documento es una RFP legítima; si no lo es, que el flujo se detenga ahí, sin pasar al resto del pipeline.
> > - Para cada RFP válida, extrae metadatos y métricas de legibilidad que nos anticipen cuánto va a tardar el procesamiento (`py-readability-metrics` te puede servir para esto).
> > - El resto del flujo debe repartir el análisis por departamento con el patrón orchestrator-worker-synthesizer que vimos en clase — no quiero un solo agente tratando de hacerlo todo.
> >
> > **Acceptance criteria:** Ventas debe poder mirar el resultado de una RFP procesada y saber, sin leer el documento original, qué le toca a cada departamento y a quién pedírselo.
> >
> > — Tu tech lead

### 📚 Conocimiento complementario: PDFs, legibilidad y "modo ticket"

Las RFPs reales llegan como PDF, un formato denso en marcado y ruido visual que consume muchos más tokens de los necesarios cuando se pasa directo a un LLM. Convertirlas a Markdown con una herramienta como **MarkItDown** antes de procesarlas reduce ese costo y le da a tus agentes un texto más limpio para trabajar. Ya con el texto en Markdown, `py-readability-metrics` calcula índices como Flesch-Kincaid o Gunning Fog; úsalo para estimar cuánto le costará procesar cada RFP, no como una nota de calidad literaria. El "modo ticket" simplemente significa que cada RFP subida se convierte en una entidad con un ciclo de vida — estados como `analizando`, `esperando_aprobación` o `terminado` — que el frontend puede consultar y refrescar, igual que un ticket de soporte.

### 🗺️ Referencia visual: análisis inicial y aislamiento de workstreams

Esta parte del flujo empieza con un triage rápido (¿es una RFP / lo bastante compleja?), luego un **orquestador** descompone el documento principal en workstreams paralelos (secciones / departamentos), los workers los procesan de forma independiente, y un **synthesizer** consolida todo en una estructura de workstreams definida con meta-información:

![Análisis inicial y aislamiento de workstreams: router de triage, filtro RFP, descomposición orchestrator-worker en secciones paralelas, luego synthesizer hacia la estructura de workstreams definida](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-orchestrate/.learn/rfp-intake-workstream-isolation.jpg)

---

## 🌱 Cómo Empezar el Proyecto

Sigue trabajando sobre la copia (fork) del monorepo de tu empresa que vienes usando desde el Hito 1. Si por algún motivo todavía no tienes tu fork, créalo ahora desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Crea una rama nueva a partir de tu rama principal: `feature/hito-9-parte-1-revision-rfps`.
2. Instala las dependencias nuevas que necesites con `uv add` (por ejemplo, `uv add markitdown` y `uv add py-readability-metrics`) — nunca con `pip install` ni `pipenv`.
3. Si necesitas construir o extender una interfaz, hazlo sobre `uis/backoffice` — no crees una aplicación nueva.
4. Ubica la lógica de tus agentes en `services/` siguiendo el mismo patrón que usaste en el Hito 8.
5. Lee tu `CONTEXT-company.md` antes de definir los departamentos o el formato de las RFPs de ejemplo.

---

## 💻 Lo Que Debes Hacer

**Interfaz de recepción (modo ticket)**

- [ ] Implementa en `uis/backoffice` una interfaz donde se puedan subir documentos RFP en PDF y se cree un ticket por cada uno
- [ ] El ticket debe mostrar su estado actual (por ejemplo: `analizando`, `esperando_aprobación`, `terminado`) y actualizarse a medida que el flujo avanza

**Ingesta y conversión del documento**

- [ ] Convierte cada RFP de PDF a Markdown antes de pasarla a los agentes (se sugiere `MarkItDown` de Microsoft) para reducir el consumo de tokens
- [ ] Extrae metadatos del documento ya convertido (por ejemplo: cliente, fecha, departamentos mencionados)
- [ ] Calcula métricas de legibilidad que permitan anticipar el tiempo de procesamiento (se sugiere `py-readability-metrics`)

**Agente clasificador**

- [ ] Implementa un primer agente que lea el documento (ya convertido) y determine si es una RFP válida
- [ ] Si el documento no es una RFP, el flujo debe detenerse y dejar el ticket en un estado explícito de descarte (no fallar en silencio)

**Orquestación por departamento**

- [ ] Implementa el patrón orchestrator-worker-synthesizer: el orquestador descompone la RFP en subtareas por departamento
- [ ] Cada agente worker extrae los aspectos clave que le corresponden a su departamento
- [ ] Un agente synthesizer consolida los resultados en un resumen que le indique a Ventas qué debe pedir a cada departamento

**Enrutamiento**

- [ ] Implementa el enrutamiento (_routing_) del documento clasificado hacia el resto del flujo agéntico

⚠️ **IMPORTANTE:** Los nombres de los departamentos, el formato de las RFPs y los criterios de clasificación deben coincidir con lo que se especifica en tu `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

**Pruebas**

- [ ] Incluye pruebas unitarias en `tests/pipelines/` para el agente clasificador y para al menos un agente worker

---

## 🧭 Preguntas de Diseño

- ¿Qué pasa si una RFP menciona un departamento que no existe en tu `CONTEXT-company.md`? ¿Cómo lo maneja tu agente clasificador?
- ¿Qué información necesita realmente cada agente worker del estado compartido? ¿Le estás pasando todo el documento o solo lo relevante para su departamento?
- ¿Cómo decides que un documento "no es una RFP"? ¿Qué criterio usas, y qué pasa si el agente se equivoca?
- ¿Qué pasa si dos agentes worker devuelven información contradictoria sobre la misma sección de la RFP?

---

## ✅ Lo Que Evaluaremos

- [ ] El ticket refleja el estado real del flujo en cada momento (analizando, esperando aprobación, terminado, descartado)
- [ ] El agente clasificador rechaza correctamente documentos que no son RFPs, sin detener el resto del sistema
- [ ] Los metadatos y las métricas de legibilidad se calculan y se almacenan por cada documento procesado
- [ ] El patrón orchestrator-worker-synthesizer está implementado con agentes claramente separados (no un solo agente monolítico)
- [ ] El resultado final identifica, por departamento, los aspectos clave y a quién dirigirse — verificable comparando contra un caso de prueba real
- [ ] Existen pruebas unitarias para el agente clasificador y al menos un agente worker
- [ ] La implementación usa los departamentos y el formato de RFP definidos en el `CONTEXT-company.md` de tu empresa

---

## 📦 Cómo Entregar

Esta es la Parte 1 de 3 del Hito 9. Entrégala con su propio Pull Request contra tu rama principal — no esperes a tener las partes 2 y 3 listas.

1. Haz commit y push de tu rama `feature/hito-9-parte-1-revision-rfps`
2. Abre un Pull Request describiendo qué implementaste y cómo probarlo
3. Incluye en la descripción del PR un ejemplo de RFP de prueba y el resultado que produce tu flujo
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
