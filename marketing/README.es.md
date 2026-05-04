# AI Native Full Stack — Módulos del programa

_This content is also available in [English](./README.md)._

---

## Núcleo IA y Agentes

### Personal Assistants with OpenClaw

`IA` `Agentes` `OpenClaw` `Despliegue`

Aprenderás a desplegar y configurar un asistente de IA de código abierto y autoalojado — tuyo, controlado por ti, sin depender de proveedores externos. La base práctica sobre la que se construyen los módulos de agentes más avanzados del programa.

**Habilidades desarrolladas:**

- Configurar un agente de IA open source como asistente personal
- Asignar tareas e integrar aplicaciones externas al agente

---

### Advanced Personal Assistants with OpenClaw

`Skills de Agente` `Memoria` `Tool Calling` `Configuración avanzada`

Llevarás tu agente de asistente básico a herramienta productiva. Aprenderás a enseñarle nuevas habilidades (skills), a elegir el tipo de memoria adecuado para cada caso y a configurarlo para operar con autonomía real en contextos empresariales.

**Habilidades desarrolladas:**

- Identificar escenarios donde un agente resuelve problemas reales del negocio
- Desarrollar skills personalizadas para OpenClaw
- Implementar memoria contextual (episódica, semántica, procedimental)
- Configuración avanzada y extensión del agente

---

### Working with AI Coding Agents

`Coding Agents` `Context Engineering` `Agent Rules` `Memory Banks` `Skills`

El salto de "usar IA" a "trabajar profesionalmente con IA". Aprenderás a construir bancos de memoria y reglas de contexto que convierten a un coding agent en un colaborador que entiende tu codebase. Dominarás la técnica de escribir especificaciones que un agente puede ejecutar con precisión.

**Habilidades desarrolladas:**

- Construir memory banks y context rules desde un código base existente
- Escribir especificaciones ejecutables para agentes (agent specs)
- Sintetizar habilidades reutilizables para que los agentes actúen con precisión

---

### LLMs, Training & RAG

`RAG` `Vector DBs` `Chunking` `Fine-tuning` `Embeddings` `Model Evaluation`

Comprenderás cómo funcionan los modelos que potencian los agentes — y cómo hacerlos más inteligentes para casos de uso específicos. Implementarás RAG para que tu agente responda con conocimiento propio y actualizado, y aprenderás cuándo y cómo entrenar o ajustar un modelo.

**Habilidades desarrolladas:**

- Preparar datos y seleccionar modelos para entrenamiento
- Implementar técnicas de RAG sobre bases de conocimiento propias
- Trabajar con bases de datos vectoriales
- Evaluar, depurar e integrar modelos en producción

---

### Agentic Engineering

`Tool Calling` `CLIs` `MCPs` `Guardrails` `Agent Memory`

El corazón técnico del programa. Construirás agentes capaces de llamar herramientas, acceder a sistemas externos mediante MCPs y CLIs, operar con memoria persistente y comportarse de forma segura bajo guardrails. El conocimiento que separa a un AI Engineer de alguien que solo usa chatbots.

**Habilidades desarrolladas:**

- Construir agentes con tool calling (llamadas a funciones reales)
- Implementar Guardrails como mecanismo de seguridad y control
- Proveer herramientas al agente mediante CLIs optimizados para IA
- Extender capacidades del agente mediante Model Context Protocol (MCP)
- Dotar de memoria persistente a un agente

---

### Agentic Workflows

`Multi-Agent Systems` `Routing` `Serverless` `Cronjobs`

Cuando un agente no es suficiente. Aprenderás a diseñar sistemas donde múltiples agentes colaboran, se distribuyen tareas y comparten memoria. Implementarás pipelines agentic con funciones serverless y cronjobs que operan de forma autónoma, continua y escalable.

**Habilidades desarrolladas:**

- Diseñar sistemas multi-agente con routing y arbitraje
- Implementar memoria compartida entre agentes
- Desplegar workflows agentic con funciones serverless y durable

---

## Infraestructura para IA

### Backend Development with Coding Agents

`Python` `FastAPI` `Agent Loops` `APIs` `Document DBs`

El backend que da vida a los agentes. Construirás APIs robustas con FastAPI, implementarás agent loops en Python y aprenderás a diseñar arquitecturas de backend orientadas a casos de uso de IA — desde el procesamiento de datos hasta la integración con LLMs.

**Habilidades desarrolladas:**

- Diseñar arquitecturas de backend para soluciones con IA
- Crear agent loops integrando LLMs con APIs
- Implementar almacenamiento ligero y procesamiento de datos CSV
- Construir y exponer APIs REST para consumo desde frontends y agentes

---

### Workflow Automations

`n8n` `LLM Nodes` `Webhooks` `Automation`

Automatización de negocio con IA integrada. Aprenderás a representar procesos empresariales como flujos ejecutables, a implementarlos en n8n y a conectar LLMs y aplicaciones de terceros en esos flujos. El resultado: procesos que operan de forma autónoma sin intervención manual.

**Habilidades desarrolladas:**

- Modelar lógica de negocio con diagramas de flujo de trabajo
- Implementar flujos básicos y avanzados en n8n
- Integrar LLMs y apps externas en automatizaciones
- Desplegar workflows mantenibles con gestión de errores

---

### Data Pipelines

`Pandas` `ETL` `Data Pipelines`

Los datos son el combustible de cualquier solución de IA. Aprenderás a construir pipelines que toman datos crudos de una aplicación, los transforman y los dejan listos para alimentar modelos, reportes o agentes — el eslabón que determina la calidad de los resultados.

**Habilidades desarrolladas:**

- Manipular y preparar conjuntos de datos con Python
- Construir pipelines de datos desde la aplicación hacia sistemas de análisis

---

### Telemetry

`Observability` `Reporting` `Data Collection` `Analysis`

No puedes mejorar lo que no mides. Aprenderás a instrumentar aplicaciones para recolectar datos de comportamiento, construir reportes sobre esos datos y tomar decisiones de negocio basadas en evidencia real — no en intuición.

**Habilidades desarrolladas:**

- Optimizar almacenamiento para reportes e integridad de datos
- Identificar oportunidades de recolección de datos en escenarios reales
- Recolectar telemetría y contexto del usuario desde la aplicación
- Construir reportes desde datos de telemetría

---

### Asynchronous Processing and Offloading

`Queues` `Background jobs` `Workers` `Redis`

Tareas que no pueden bloquear al usuario van a la cola. Aprenderás a implementar procesamiento en segundo plano y sistemas de colas que permiten a agentes y aplicaciones delegar trabajo pesado sin sacrificar tiempo de respuesta — un patrón esencial en arquitecturas de IA productivas.

**Habilidades desarrolladas:**

- Implementar background processing para tareas costosas
- Gestionar colas de procesos con workers
- Usar colas para delegar trabajo entre agentes y servicios

---

### Real-Time

`WebSockets` `Streaming` `Pub/Sub` `Event Architecture`

La capa que hace que la IA se sienta viva. Implementarás comunicación en tiempo real entre usuarios y modelos de lenguaje usando streaming, websockets y arquitecturas orientadas a eventos — la misma tecnología detrás de las interfaces conversacionales modernas.

**Habilidades desarrolladas:**

- Construir chats de soporte con LLMs en tiempo real
- Implementar streaming de respuestas con generadores (yield)
- Integrar webhooks y pub/sub en aplicaciones con IA

---

### Web Application Authentication

`JWT` `FastAPI` `Auth flows` `Security`

Toda aplicación productiva necesita saber quién es quién. Aprenderás a implementar autenticación segura en FastAPI y a construir flujos de login completos que definen qué puede hacer cada usuario — y qué pueden invocar los agentes en su nombre.

**Habilidades desarrolladas:**

- Implementar autenticación y restricción de rutas en FastAPI
- Construir flujos de autenticación completos (login, tokens, sesiones)

---

### Error Handling, Debugging and Testing

`Error Handling` `Testing` `Debugging` `TDD`

El código que los agentes generan necesita ser verificado. Aprenderás a gestionar errores de forma controlada, a escribir baterías de pruebas que validan el comportamiento esperado y a depurar aplicaciones con criterio — los estándares de calidad que distinguen software profesional del prototipo.

**Habilidades desarrolladas:**

- Comprender y gestionar errores de ejecución con control de flujo
- Desarrollar baterías de pruebas para aplicaciones robustas

---

### Cybersecurity in AI Applications

`OWASP` `AI Security` `LLM Auditing` `Guardrails`

La IA introduce vectores de ataque que la seguridad tradicional no cubre. Aprenderás a identificar las vulnerabilidades más críticas en aplicaciones con IA, a implementar prácticas seguras en la integración de modelos y a usar los propios LLMs para auditar un sistema.

**Habilidades desarrolladas:**

- Identificar y corregir vulnerabilidades OWASP Top 10 en aplicaciones web
- Implementar prácticas de seguridad específicas para integraciones de IA
- Usar LLMs como herramienta de auditoría de ciberseguridad

---

## Otros conocimientos complementarios

### Fundamentos y conocimientos de soporte técnico

`Algorithms` `Data Structures` `Docker` `TypeScript` `React` `Next.js` `Tailwind` `SQL` `Git` `Command Line`

Estos módulos aportan los fundamentos esenciales para colaborar de manera eficaz con agentes de software y revisar su trabajo:

- **Herramientas de colaboración:** Dominio de la línea de comandos, Git y GitHub para flujos de trabajo colaborativos y seguros.
- **Contenerización:** Empaquetado y despliegue de aplicaciones completas con Docker para entornos productivos y reproducibles.
- **Programación:** Lógica, algoritmos, estructuras de datos y POO con TypeScript y Python para entender y mejorar el código generado por IA.
- **Frontend moderno:** Construcción y revisión de interfaces con React, Next.js y especificaciones visuales; estilos accesibles y optimizados con HTML, CSS y Tailwind.
- **Bases de datos:** Uso de SQL, PostgreSQL y ORMs para manejo robusto de datos y consultas relacionales.
- **Optimización:** Estrategias de rendimiento en frontend y backend: caching, serializers, lazy loading, buenas prácticas para alta demanda.

Este conocimiento complementa y potencia el ciclo completo de desarrollo de sistemas impulsados por IA y agentes.

---

## Capstone

### Empresa transformada con IA

`Final Project` `AI-First Company`

El cierre del programa es un entregable real: la transformación completa de una empresa mediante IA. Integrarás todo lo aprendido — frontend generado por agentes, APIs con autenticación, telemetría, workflows automatizados, capa RAG de conocimiento y agentes con tool calling — en un sistema funcional y desplegado. No un ejercicio académico: una demostración de capacidad profesional.

**Componentes del entregable:**

- Frontend generado por IA
- API con autenticación completa
- Telemetría y pipeline de reporting
- Workflows automatizados generados por agentes
- Capa de conocimiento RAG
- Agentes con tool calling
- Comunicación en tiempo real
