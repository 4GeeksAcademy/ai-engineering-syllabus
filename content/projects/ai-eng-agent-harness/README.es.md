# Aseguramiento de Agentes: Harness y Guardrails

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/08-agent-engineering/harnessing)** antes de escribir código — define los temas de tu base de conocimientos, los límites de alcance del agente y las restricciones específicas de tu empresa que tu system prompt y tus guardrails deben respetar.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Tu agente de consulta de base de conocimientos ya funciona: responde preguntas usando RAG sobre los documentos de tu empresa, puede invocar herramientas y, desde el último sprint, consume el MCP Server como cliente. El problema es que ahora mismo cualquier persona puede hablarle de lo que quiera, pedirle que ignore sus instrucciones, o convertirlo en su asistente personal — y el agente obedecería.

Tu tech lead abrió un **ticket** después de una revisión de seguridad interna: _"El agente pasó las pruebas funcionales, pero falló todas las pruebas de abuso. Necesitamos el harness de protección antes de exponerlo a usuarios reales."_ El ticket incluye tres criterios de aceptación no negociables que debes leer con atención, porque no todos están escritos como checklist.

> **De: Tech Lead — Ticket #SEC-114**
>
> Necesitamos cerrar el agente antes del siguiente despliegue. Tres cosas puntuales:
>
> 1. El agente puede responder preguntas fuera del dominio de la empresa (small talk, una pregunta general de cultura), pero **siempre debe traer la conversación de vuelta al contexto de la empresa** — no puede convertirse en un chatbot de propósito general.
> 2. Nadie debería poder usar este agente como su ChatGPT personal para tareas que no tienen nada que ver con nosotros (escribirle un ensayo, pedirle código de otro proyecto, hacer de terapeuta). Eso hay que bloquearlo.
> 3. El system prompt no puede ser modificado por el usuario. Si alguien le pide "ignora tus instrucciones anteriores" o "actúa como si no tuvieras reglas", el agente debe rechazarlo sin excepción — y sin importar cuántas veces lo intenten reformular.
>
> Documenta cómo probaste cada uno de estos casos. Si solo tienes un filtro, no vamos a aceptar el PR.

### 🧠 Conocimiento complementario: Harness y Guardrails

Un **harness** es todo lo que envuelve al modelo para convertirlo en un agente confiable: orquestación de herramientas, loops de verificación, contexto/memoria, guardrails y observabilidad. El modelo decide; el harness ejecuta, controla y contiene.

Los **guardrails** existen porque los agentes fallan de tres formas distintas, y cada una necesita una defensa diferente:

- **Fallos estructurales**: JSON malformado, campos faltantes en una respuesta de tool.
- **Fallos de contenido**: alucinaciones, fuga de información sensible, contenido dañino.
- **Fallos de seguridad**: inyección de prompt que manipula al modelo para ignorar instrucciones o exfiltrar datos.

Un único guardrail nunca es suficiente — cada tipo de fallo necesita su propia capa de protección.

---

## 🌱 Cómo Empezar el Proyecto

Si ya tienes tu fork del monorepo de la empresa desde el inicio del curso, simplemente crea una nueva rama a partir de tu último trabajo (Milestone/día anterior) y continúa sobre el agente que ya construiste.

Si por algún motivo todavía no tienes un fork (por ejemplo, te uniste tarde o lo perdiste), haz un fork del [monorepo de referencia](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) antes de continuar.

```bash
git checkout -b w22-d66-agent-guardrails
```

Instala cualquier dependencia nueva que necesites con `uv add` (nunca `pip install` ni `pipenv`).

---

## 💻 Qué Debes Hacer

### System Prompt seguro

- [ ] Reescribe el system prompt de tu agente separando claramente **instrucciones del sistema** de **input del usuario** — el modelo nunca debe tratar una instrucción del usuario como si tuviera la misma autoridad que el system prompt.
- [ ] El system prompt debe declarar explícitamente el dominio de la empresa y las condiciones bajo las cuales el agente puede salirse de él (small talk permitido, redirección obligatoria).
- [ ] Documenta en el PR al menos 3 variantes de intento de "jailbreak" o cambio de instrucciones que probaste contra tu agente (ej. "ignora tus instrucciones", "ahora eres un asistente sin reglas", "olvida que trabajas para la empresa").

⚠️ **IMPORTANTE:** Los temas permitidos, los límites del dominio y las reglas específicas de tu empresa deben coincidir con lo especificado en tu CONTEXT.md. Un system prompt genérico que ignore el contexto no será aceptado.

### Guardrails de contenido y alcance

- [ ] Implementa un guardrail que detecte cuándo una consulta es una solicitud de uso personal no relacionada con la empresa (ej. "escríbeme un poema de amor", "ayúdame con la tarea de mi universidad") y responda rechazando la tarea mientras redirige al propósito del agente.
- [ ] Implementa un guardrail que permita preguntas generales o casuales (ej. "¿qué hora es en Tokio?") pero que cierre la respuesta reconduciendo la conversación hacia el contexto de la empresa.
- [ ] Añade validación de la salida del modelo antes de devolverla al usuario (formato esperado, ausencia de instrucciones internas filtradas, ausencia de datos sensibles del CONTEXT que no deberían exponerse).

### Guardrails de seguridad (anti-inyección)

- [ ] Implementa una capa que sanitice o aísle cualquier texto proveniente de una tool externa o de un documento recuperado por RAG — ese contenido **nunca** debe tratarse como una instrucción del sistema.
- [ ] Implementa un mecanismo de rechazo explícito ante solicitudes de cambio de instrucciones, reformuladas de al menos tres maneras distintas.
- [ ] Añade un test automatizado (`tests/pipelines/` o el directorio de tests correspondiente a tu agente) que ejecute tus casos de intento de inyección y falle el build si el agente los obedece.

### Observabilidad mínima

- [ ] Registra (log) cada vez que un guardrail bloquea o redirige una solicitud, incluyendo el tipo de fallo detectado (estructural, de contenido o de seguridad).
- [ ] Expón un resumen simple (endpoint o comando) de cuántas veces se activó cada guardrail durante una sesión de pruebas.

---

## ✅ Qué Vamos a Evaluar

- [ ] El agente redirige al contexto de la empresa cuando recibe una consulta fuera de dominio, en lugar de responderla como un asistente genérico.
- [ ] El agente rechaza consistentemente al menos 3 variantes distintas de intento de cambio de instrucciones documentadas en el PR.
- [ ] El agente rechaza solicitudes de uso como chatbot personal (tareas sin relación con la empresa) sin dejar de ser útil para consultas legítimas.
- [ ] Existe más de un guardrail implementado — no una única validación genérica.
- [ ] El contenido proveniente de tools o documentos RAG nunca es tratado como instrucción del sistema (demostrado con un caso de prueba).
- [ ] Cada bloqueo o redirección de un guardrail queda registrado con el tipo de fallo correspondiente.
- [ ] La implementación respeta los nombres de campos, temas de la base de conocimientos y restricciones definidas en tu CONTEXT.md.

---

## 📦 Cómo Entregar tu Proyecto

Haz un Pull Request desde tu rama hacia tu fork del monorepo de la empresa, con una descripción que incluya los casos de prueba de jailbreak/inyección que documentaste. Esta entrega es independiente y no depende de otras partes o milestones — no esperes a que otro trabajo esté terminado para enviar tu PR.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
