# AI Native Full Stack — Módulos del programa

_This content is also available in [English](./README.md)._

---

## IA y Agentes (Core)

### Asistentes Personales con OpenClaw

`AI` `Agents` `OpenClaw` `Deployment`
Aprenderás a desplegar y configurar un asistente de IA open-source, auto-alojado — tuyo, bajo tu control, sin depender de proveedores externos. La base práctica para los módulos más avanzados de agentes del programa.

**Habilidades desarrolladas:**

- Configurar un agente de IA open-source como asistente personal
- Asignar tareas e integrar aplicaciones externas con el agente

---

### Asistentes Personales Avanzados con OpenClaw

`Agent Skills` `Memory` `Tool Calling` `Advanced configuration`
Llevarás tu agente asistente básico a una herramienta productiva. Aprenderás a enseñarle nuevas habilidades, elegir el tipo de memoria adecuado para cada caso y configurarlo para operar con autonomía real en contextos de negocio.

**Habilidades desarrolladas:**

- Identificar escenarios donde un agente resuelve problemas reales de negocio
- Desarrollar habilidades personalizadas para OpenClaw
- Implementar memoria contextual (episódica, semántica, procedimental)
- Configuración avanzada y extensión del agente

---

### Trabajo con Agentes de Código

`Coding Agents` `Context Engineering` `Agent Rules` `Memory Banks` `Skills`
El salto de "usar IA" a "trabajar profesionalmente con IA." Aprenderás a construir bancos de memoria y reglas de contexto que convierten a un agente de código en un colaborador que entiende tu codebase. Dominarás la escritura de especificaciones que un agente puede ejecutar con precisión.

**Habilidades desarrolladas:**

- Construir bancos de memoria y reglas de contexto a partir de un codebase existente
- Escribir especificaciones ejecutables para agentes (agent specs)
- Sintetizar habilidades reutilizables para que los agentes actúen con precisión

---

### LLMs, Entrenamiento y RAG

`RAG` `Vector DBs` `Chunking` `Fine-tuning` `Embeddings` `Model Evaluation`
Entenderás cómo funcionan los modelos que impulsan a los agentes — y cómo hacerlos más inteligentes para casos de uso específicos. Implementarás RAG para que tu agente responda con conocimiento propietario y actualizado, y aprenderás cuándo y cómo entrenar o hacer fine-tuning de un modelo.

**Habilidades desarrolladas:**

- Preparar datos y seleccionar modelos para entrenamiento
- Implementar técnicas de RAG sobre bases de conocimiento propietarias
- Trabajar con bases de datos vectoriales
- Evaluar, depurar e integrar modelos en producción

---

### Ingeniería Agéntica

`Tool Calling` `CLIs` `MCPs` `Guardrails` `Agent Memory`
El corazón técnico del programa. Construirás agentes que pueden llamar herramientas, acceder a sistemas externos vía MCPs y CLIs, operar con memoria persistente y comportarse de forma segura bajo guardrails. El conocimiento que separa a un ingeniero de IA de alguien que solo usa chatbots.

**Habilidades desarrolladas:**

- Construir agentes con tool calling (llamadas a funciones reales)
- Implementar guardrails como mecanismo de seguridad y control
- Proveer herramientas al agente mediante CLIs optimizados para IA
- Extender las capacidades del agente con el Model Context Protocol (MCP)
- Dotar al agente de memoria persistente

---

### Workflows Agénticos y Orquestación

`Multi-Agent Systems` `LangGraph` `State Graphs` `Routing` `Human-in-the-Loop` `Checkpointing`
Cuando un solo agente no es suficiente. Aprenderás a diseñar y orquestar sistemas multi-agente con LangGraph, dominando el modelo de grafos de estado que hace posible la colaboración compleja entre agentes. Definirás esquemas de estado, implementarás enrutamiento condicional y ciclos con condiciones de terminación, construirás checkpoints human-in-the-loop para aprobación y escalamiento, y compondrás subgrafos modulares reutilizables entre proyectos. También aprenderás a rastrear, evaluar y depurar flujos multi-agente — entendiendo qué agente hizo qué, por qué el enrutamiento tomó un camino específico y cuánto costó cada decisión.

**Habilidades desarrolladas:**

- Diseñar sistemas multi-agente con el modelo de grafos de estado de LangGraph
- Definir esquemas de estado e implementar aristas condicionales y ciclos
- Implementar patrones human-in-the-loop (puertas de aprobación, checkpoints de revisión, enrutamiento de escalamiento)
- Usar persistencia de estado y checkpointing para workflows de larga duración
- Manejar errores y recuperación en nodos individuales sin colapsar el grafo
- Construir subgrafos modulares y componerlos en sistemas más grandes
- Implementar memoria y contexto compartido entre agentes
- Rastrear, evaluar y observar la ejecución multi-agente (decisiones de enrutamiento, costo de tokens por camino)

---

## Infraestructura para IA

### Desarrollo Backend con Agentes de Código

`Python` `FastAPI` `Agent Loops` `APIs` `Document DBs`
El backend que da vida a los agentes. Construirás APIs robustas con FastAPI, implementarás agent loops en Python y aprenderás a diseñar arquitecturas backend orientadas a casos de uso de IA — desde procesamiento de datos hasta integración con LLMs.

**Habilidades desarrolladas:**

- Diseñar arquitecturas backend para soluciones potenciadas por IA
- Crear agent loops integrando LLMs con APIs
- Implementar almacenamiento ligero y procesamiento de datos CSV
- Construir y exponer APIs REST para frontends y agentes

---

### Automatización de Workflows

`n8n` `LLM Nodes` `Webhooks` `Automation`
Automatización de negocio con IA integrada. Aprenderás a representar procesos de negocio como flujos ejecutables, implementarlos en n8n y conectar LLMs y aplicaciones de terceros en esos flujos. El resultado: procesos que corren de forma autónoma sin intervención manual.

**Habilidades desarrolladas:**

- Modelar lógica de negocio con diagramas de workflow
- Implementar flujos básicos y avanzados en n8n
- Integrar LLMs y aplicaciones externas en automatizaciones
- Desplegar workflows mantenibles con manejo de errores

---

### Pipelines de Datos

`Pandas` `ETL` `Data Pipelines`
Los datos son el combustible de cualquier solución de IA. Aprenderás a construir pipelines que toman datos crudos de una aplicación, los transforman y los dejan listos para alimentar modelos, reportes o agentes — el eslabón que determina la calidad del output.

**Habilidades desarrolladas:**

- Manipular y preparar datasets con Python
- Construir pipelines de datos desde la aplicación hasta sistemas de análisis

---

### Telemetría

`Observability` `Reporting` `Data Collection` `Analysis`
No puedes mejorar lo que no mides. Aprenderás a instrumentar aplicaciones para recolectar datos de comportamiento, construir reportes a partir de esos datos y tomar decisiones de negocio basadas en evidencia real — no en intuición.

**Habilidades desarrolladas:**

- Optimizar almacenamiento para reportes e integridad de datos
- Identificar oportunidades de recolección de datos en escenarios reales
- Recolectar telemetría y contexto de usuario desde la aplicación
- Construir reportes a partir de datos de telemetría

---

### Procesamiento Asíncrono y Despliegue Agéntico

`Queues` `Background Jobs` `Workers` `Redis` `Serverless` `Durable Execution` `Cronjobs`
Las tareas que no deben bloquear al usuario van a la cola — y los workflows agénticos que deben correr de forma confiable también van aquí. Aprenderás a implementar procesamiento en background y sistemas de colas que permiten a agentes y aplicaciones delegar trabajo pesado sin sacrificar tiempo de respuesta. Luego irás más allá: desplegando workflows agénticos en producción con funciones serverless, patrones de ejecución durable y pipelines disparados por cron. Implementarás retry y reanudación desde checkpoints, dispararás pipelines de LangGraph vía webhooks y construirás la infraestructura que mantiene a los sistemas multi-agente corriendo de forma autónoma, continua y a escala.

**Habilidades desarrolladas:**

- Implementar procesamiento en background para tareas costosas
- Gestionar colas de procesos con workers
- Usar colas para delegar trabajo entre agentes y servicios
- Desplegar workflows agénticos con funciones serverless y ejecución durable
- Disparar pipelines de agentes vía webhooks y cron jobs
- Implementar patrones de retry y reanudación desde checkpoints de workflows

---

### Real-Time

`WebSockets` `Streaming` `Pub/Sub` `Event Architecture`
La capa que hace que la IA se sienta viva. Implementarás comunicación en tiempo real entre usuarios y modelos de lenguaje usando streaming, WebSockets y arquitecturas orientadas a eventos — la misma tecnología detrás de las interfaces conversacionales modernas.

**Habilidades desarrolladas:**

- Construir chats de soporte con LLMs en tiempo real
- Implementar streaming de respuestas con generadores (yield)
- Integrar webhooks y pub/sub en aplicaciones de IA

---

### Autenticación en Aplicaciones Web

`JWT` `FastAPI` `Auth flows` `Security`
Toda aplicación productiva necesita saber quién es quién. Aprenderás a implementar autenticación segura en FastAPI y construir flujos completos de login que definen qué puede hacer cada usuario — y qué pueden invocar los agentes en su nombre.

**Habilidades desarrolladas:**

- Implementar autenticación y restricciones de rutas en FastAPI
- Construir flujos completos de autenticación (login, tokens, sesiones)

---

### Manejo de Errores, Debugging y Testing

`Error Handling` `Testing` `Debugging` `TDD`
El código que generan los agentes debe ser verificado. Aprenderás a manejar errores de forma controlada, escribir suites de tests que validen el comportamiento esperado y depurar aplicaciones con criterio — los estándares de calidad que separan el software profesional de los prototipos.

**Habilidades desarrolladas:**

- Entender y gestionar errores en tiempo de ejecución con control de flujo
- Desarrollar suites de tests para aplicaciones robustas

---

### Ciberseguridad en Aplicaciones de IA

`OWASP` `AI Security` `LLM Auditing` `Guardrails`
La IA introduce vectores de ataque que la seguridad tradicional no cubre. Aprenderás a identificar las vulnerabilidades más críticas en aplicaciones de IA, implementar prácticas seguras en la integración de modelos y usar los propios LLMs como herramienta de auditoría de un sistema.

**Habilidades desarrolladas:**

- Identificar y corregir vulnerabilidades OWASP Top 10 en aplicaciones web
- Implementar prácticas de seguridad específicas para integraciones de IA
- Usar LLMs como herramienta de auditoría de ciberseguridad

---

## Otros conocimientos complementarios

### Fundamentos y habilidades técnicas de soporte

`Algorithms` `Data Structures` `Docker` `TypeScript` `React` `Next.js` `Tailwind` `SQL` `Git` `Command Line`
Estos módulos proveen las bases esenciales para colaborar efectivamente con agentes de software y revisar su trabajo:

- **Herramientas de colaboración:** Línea de comandos, Git y GitHub para flujos de trabajo colaborativos y seguros.
- **Contenedorización:** Empaquetar y desplegar aplicaciones completas con Docker para entornos productivos y reproducibles.
- **Programación:** Lógica, algoritmos, estructuras de datos y POO con TypeScript y Python para entender y mejorar código generado por IA.
- **Frontend moderno:** Construir y revisar interfaces con React, Next.js y specs visuales; estilos accesibles y optimizados con HTML, CSS y Tailwind.
- **Bases de datos:** SQL, PostgreSQL y ORMs para manejo robusto de datos y consultas relacionales.
- **Optimización:** Estrategias de rendimiento en frontend y backend: caching, serializers, lazy loading y prácticas para alta carga.
  Este conocimiento complementa y fortalece el ciclo completo de desarrollo de sistemas impulsados por IA y agentes.

---

## Capstone

### Empresa transformada por IA

`Final Project` `AI-First Company`
El programa cierra con un entregable real: la transformación completa de una empresa a través de IA. Integrarás todo lo aprendido — frontend generado por agentes, APIs autenticadas, telemetría, workflows automatizados, una capa de conocimiento RAG y agentes con tool calling — en un sistema funcional y desplegado. No es un ejercicio académico: es una demostración de capacidad profesional.

**Componentes del entregable:**

- Frontend generado por IA
- API con autenticación completa
- Pipeline de telemetría y reportes
- Workflows automatizados generados por agentes
- Capa de conocimiento RAG
- Agentes con tool calling
- Comunicación en tiempo real
