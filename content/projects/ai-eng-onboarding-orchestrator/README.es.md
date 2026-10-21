# Agentic Engineering – Agente de incorporaciones

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee el **[BRIEFING de tu empresa](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir una sola línea de código. Ahí están las etapas del onboarding corporativo, el contenido que debe conocer cada nueva incorporación, los documentos y accesos que se gestionan y quién aprueba cada etapa.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa, no en un repositorio nuevo.

El equipo de Personas te escribe con un problema que se repite con cada nueva incorporación al equipo corporativo. La persona llega, recibe un documento extenso, una lista de enlaces y un par de reuniones, y a partir de ahí se las arregla como puede. Nadie sabe con certeza si ya entiende cómo opera la empresa, qué se espera de su puesto o cuáles son los lineamientos internos, y los trámites (documentos, accesos, firmas) se pierden entre correos.

> _"Quiero que cada persona que se incorpora recorra el mismo camino, a su ritmo, sin que yo tenga que perseguirla. Que conozca la empresa, cómo operamos, qué se espera de su función y cómo trabajamos aquí, y que no pase a la siguiente etapa hasta demostrar que entendió la anterior. Si tiene dudas, que se las resuelvan con nuestra documentación oficial, no con respuestas inventadas. Y hay etapas que solo puede cerrar su responsable directo. Eso no lo decide la máquina."_
>
> — Responsable de Personas

El brief deja implícitas cuatro exigencias que definen la arquitectura:

1. **El proceso dura días o semanas, no minutos.** El agente tiene que guardar su estado y retomarlo exactamente donde lo dejó, aunque el servicio se reinicie entre una etapa y la siguiente.
2. **Avanzar requiere demostrar comprensión.** Cada etapa de contenido termina con una comprobación. Haber "abierto el documento" no equivale a haberlo entendido.
3. **Las respuestas salen del material oficial o no salen.** Si la duda no está cubierta por la documentación de la empresa, el agente lo dice y la deriva a una persona. Nunca la rellena con una suposición.
4. **Hay decisiones que no le corresponden al agente.** Las aprobaciones del responsable directo son puntos de parada reales del flujo: el agente se detiene, espera y continúa solo cuando una persona con el permiso adecuado decide.

### Conocimiento complementario: por qué un solo agente con estado, y no varios

Es tentador repartir el onboarding entre varios agentes especializados (uno para el contenido, otro para los trámites, otro para las dudas). Sin embargo, el onboarding es un proceso **secuencial, de larga duración y con un único hilo de responsabilidad**: en cada momento hay una sola cosa que hacer a continuación para esa persona, y lo difícil no es razonar en paralelo sino no perder el estado. Un único agente con un grafo de etapas explícito, un mecanismo de persistencia (checkpointer) y una herramienta de consulta sobre la documentación oficial resuelve eso de forma más simple, más fácil de depurar y más barata que una coordinación entre agentes. Elegir la arquitectura más simple que resuelve el problema es una decisión de ingeniería que debes poder defender.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee el briefing de tu empresa completo antes de tocar código.
3. Crea una rama nueva: `feature/onboarding-orchestrator`.
4. Dibuja el proceso como un grafo de estados antes de programar: etapas, condición de entrada y de salida de cada una, comprobaciones de comprensión, puntos de aprobación humana y plazos.
5. Reúne y organiza el material oficial de onboarding que indica el briefing. Será la única fuente de verdad del agente.
6. Decide qué herramientas necesita el agente y cuáles **no** debe tener. Empieza por la lista más corta posible.

---

## 💻 Qué Debes Hacer

**Diseño del flujo**

- [ ] Modela el onboarding corporativo de tu empresa como un grafo explícito de etapas, con condición de salida verificable en cada una
- [ ] Incluye como mínimo etapas de conocimiento de la empresa, de su operación, de las funciones del puesto, de la forma de trabajar y de los lineamientos internos
- [ ] Incluye las etapas administrativas que indique el briefing (documentos, accesos, firmas)
- [ ] Marca en el grafo los puntos que requieren aprobación humana y quién puede darla
- [ ] Define el plazo esperado de cada etapa según el briefing

**Contenido y comprobación de comprensión**

- [ ] Indexa el material oficial de onboarding para que el agente pueda consultarlo
- [ ] Presenta el contenido de cada etapa adaptado al puesto de la persona incorporada
- [ ] Cierra cada etapa de contenido con una comprobación de comprensión; si no se supera, el agente refuerza el contenido y repite la comprobación
- [ ] Responde las dudas de la persona usando solo el material oficial e indicando la fuente
- [ ] Cuando una duda no está cubierta por el material, el agente lo reconoce explícitamente y la deriva a una persona del equipo

**Agente y estado**

- [ ] Implementa el orquestador como un único agente con un framework de agentes (por ejemplo, LangGraph)
- [ ] Persiste el estado de cada incorporación con un checkpointer, de forma que el proceso sobreviva a un reinicio del servicio
- [ ] Permite que varias incorporaciones avancen en paralelo, cada una con su propio estado aislado
- [ ] Ejecuta el agente fuera del ciclo petición-respuesta, como tarea en segundo plano

**Aprobaciones humanas**

- [ ] Implementa los puntos de aprobación como interrupciones reales del flujo: el agente se detiene y no avanza hasta recibir la decisión
- [ ] Verifica que quien aprueba tiene el rol y el departamento adecuados para hacerlo
- [ ] Contempla el rechazo: el flujo debe saber qué hacer si una aprobación se deniega

**Seguimiento y escalado**

- [ ] Envía recordatorios a la persona incorporada cuando una etapa pendiente se acerca a su plazo
- [ ] Escala a su responsable directo cuando una etapa supera su plazo
- [ ] Implementa una vista para el equipo de Personas: qué incorporaciones están activas, en qué etapa está cada una y cuáles están bloqueadas
- [ ] Ofrece a la persona incorporada una vista de su propio progreso y de lo que le falta

**Seguridad y trazabilidad**

- [ ] El agente opera con una identidad propia y permisos más acotados que los de cualquier persona del equipo
- [ ] Registra cada acción del agente identificándola como acción de un proceso automatizado, no de una persona
- [ ] Identifica en el briefing qué datos de la persona incorporada son sensibles y demuestra que no aparecen en logs, prompts almacenados ni mensajes salientes

⚠️ **IMPORTANTE:** las etapas, el contenido, los documentos, los aprobadores y los plazos deben corresponder exactamente a lo especificado en el briefing de tu empresa. Un flujo genérico que ignore ese contexto no será aceptado.

---

## ✅ Qué Vamos a Evaluar

- [ ] El proceso está modelado como un grafo explícito que cubre empresa, operación, funciones, forma de trabajar, lineamientos y trámites administrativos
- [ ] Una prueba demuestra que, si el servicio se reinicia a mitad de una incorporación, el agente la retoma exactamente en la etapa en que estaba
- [ ] Ninguna etapa de contenido se da por superada sin pasar su comprobación de comprensión
- [ ] Las respuestas a dudas citan el material oficial, y una pregunta fuera de ese material se reconoce y se deriva en lugar de inventar una respuesta
- [ ] El agente no avanza más allá de un punto de aprobación sin una decisión humana, y solo acepta la de alguien con el permiso adecuado
- [ ] Una etapa vencida dispara el escalado al responsable directo
- [ ] Las acciones del agente quedan registradas como acciones de proceso automatizado
- [ ] Los datos sensibles de la persona incorporada no aparecen en logs, prompts almacenados ni mensajes salientes
- [ ] La elección de una arquitectura monoagente está justificada por escrito

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/onboarding-orchestrator` hacia `main` en tu fork. En la descripción del PR incluye el diagrama del grafo de etapas, la justificación de la arquitectura monoagente, evidencia de la prueba de reanudación tras reinicio y un ejemplo de pregunta fuera del material oficial correctamente derivada. Solicita el sign-off del equipo de Personas antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
