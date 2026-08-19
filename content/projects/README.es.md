# Proyectos de Ingeniería de IA

Repositorio de proyectos prácticos del programa de **Ingeniería de IA** de 4Geeks Academy. Cada carpeta es un proyecto independiente con su propio README, criterios de evaluación y, cuando aplica, `learn.json` para la plataforma.

Los proyectos siguen un orden pedagógico: desde fundamentos web (HTML, CSS, SEO, accesibilidad) y Tailwind, pasando por hitos de empresa y colaboración, **configuración e integraciones de agentes OpenClaw**, luego TypeScript y diseño de sistemas, React/Next.js y entrega asistida por IA, APIs, autenticación, agentes, rendimiento, telemetría, pipelines de datos, jobs en segundo plano, colas de mensajes, bases de conocimiento RAG, flujos agénticos de RFPs, sistemas en tiempo real y un **pitch final de 5 minutos**.

---

## Proyectos (orden sugerido)

0. **[¿Es Saludable Este Snack? — Una Automatización que Verifica Nutrición](./n8n-snackcheck-nutrition)**  
   Proyecto final en n8n: webhook de código de barras → Open Food Facts → reglas de semáforo + Nutri-Score → veredicto Groq con tono adaptable, con diagrama, README, pruebas y CHANGELOG.

1. **[Hito de empresa: Elige tu compañía](./ai-eng-milestone-choose-company)**  
   `Hito 0` — Elige tu empresa ficticia, captúrala en `CONTEXT.md` y prepara la narrativa y los datos que reutilizarás en hitos posteriores.

2. **[Landing de artista: HTML, CSS, SEO y accesibilidad](./html-css-artist-landing-seo-access)**  
   Landing accesible y optimizada para SEO de un artista usando HTML semántico y CSS.

3. **[Dashboard simple con Tailwind CSS](./simple-dashboard-tailwind-css)**  
   Dashboard responsive con HTML y Tailwind mostrando KPIs, drivers y detalles operativos (sin React).

4. **[Hito de empresa: Fundamentos web](./ai-eng-milestone-web-fundamentals)**  
   `Hito 1` — Sitio público de tu empresa: landing más formulario de registro con HTML5 semántico, Tailwind, Schema.org y validación JavaScript. Sigue `CONTEXT.md` para datos y campos del formulario.

5. **[Proyecto colaborativo: tienda online con HTML y Tailwind](./collaborative-project-html-tailwind-online-store)**  
   Prototipo e-commerce colaborativo (mín. 5 páginas: Home, Catálogo, Producto, Carrito, Checkout) con HTML y Tailwind, trabajo en equipo con ramas y pull requests.

6. **[Configura tu agente de IA personal con OpenClaw](./openclaw-setup)**  
   Despliega y configura OpenClaw en un VPS con LiteLLM, valida el chat local y documenta un paquete de entrega seguro (config saneada + captura de prueba).

7. **[Conecta tu agente: Telegram, Google Drive y Calendar](./openclaw-connection)**  
   Proyecto solo de configuración: canal Telegram, Zapier MCP, acciones de Google Drive y Calendar, y flujo end-to-end confirmado con capturas (después de tener OpenClaw en marcha).

8. **[Mi agente, a mi manera: enseña nuevas skills a tu asistente](./openclaw-skills)**  
   Continúa en tu entorno OpenClaw y repo de tareas previas: completa los cinco archivos de briefing `.openclaw`, commitea `SKILLS_DESIGN.md` e implementa al menos dos skills OpenClaw usando solo integraciones Composio que ya tengas (Google apps, GitHub, Telegram).

9. **[Mi asistente 4Geeks — OpenClaw sigue tu progreso](./openclaw-integration)**  
   Conecta OpenClaw a la API de 4Geeks con tu token para que el agente reporte proyectos pendientes, progreso del curso y datos LearnPack relacionados.

10. **[Dale memoria a tu agente](./openclaw-memory)**  
    Configura tipos de memoria OpenClaw (episódica, semántica, procedimental), reestructura archivos del workspace y valida que el contexto persiste entre sesiones.

11. **[Agente de onboarding con memoria](./openclaw-onboarding-agent)**  
    Construye un flujo de onboarding empresarial: agente OpenClaw con memoria que lee plantillas HR y envía email de bienvenida personalizado desde tu `CONTEXT-empresa.md`.

12. **[Gestor de asientos de cine (TypeScript)](./seats-management-typescript)**  
    Sistema de reserva de asientos en terminal con array 2D: reservar, contar y buscar asientos adyacentes.

13. **[Reproductor de playlist — Modelado de objetos](./data-modeling-and-class-diagrams-music-player)**  
    Diagrama de clases UML para un reproductor de playlist en diagram.4geeks.com: entidades, tipos de datos y relaciones.

14. **[Billetera digital — Modelado de objetos](./data-modeling-and-class-diagrams-digital-wallet)**  
    Diagrama de clases UML para una billetera digital con historial de transacciones en diagram.4geeks.com.

15. **[Hito de empresa: Fundamentos de programación (TypeScript)](./ai-eng-milestone-coding-fundamentals)**  
    `Hito 2` — Fundamentos con TypeScript: módulos pequeños y testeables (control de flujo, arrays, objetos, funciones, casos límite) con buenas prácticas.

16. **[Plataforma de alquiler de agentes IA: prototipo de panel admin](./agent-hub-ui-specs-and-prompts)**  
    Frontend spec-driven: escribe `SPECS.md` primero, luego dashboard y vistas de gestión con HTML, Tailwind y JavaScript vanilla.

17. **[Habla con la máquina: interfaz de chat con API de IA real](./chat-interface-real-ai-api)**  
    Interfaz de chat en el navegador que llama a la API Groq con `fetch`, envía historial completo y rastrea tokens y métricas de respuesta.

18. **[Wanderlust Explorer con React y Next.js](./nextjs-wanderlust-explorer)**  
    App Next.js App Router desde cero: listado de experiencias con búsqueda y filtros en URL, páginas de detalle, favoritos en estado y dataset TypeScript local.

19. **[Clon UI de Airbnb con Next.js y React](./nextjs-airbnb-ui-clone)**  
    Clon UI Next.js 16 + TypeScript + Tailwind desde brief de producto: layout, componentes reutilizables y datos tipados.

20. **[Hito de empresa: Talent Pipeline Tracker](./ai-eng-milestone-frontend-development)**  
    `Hito 3` — Frontend Next.js App Router para la API de reclutamiento: listado y detalle de candidatos, filtros, CRUD de notas, formularios y estados async alineados con `CONTEXT-empresa.md`.

21. **[Proyecto de contexto — dashboard financiero empresarial](./company-financial-dashboard-context-project)**  
    Stewardship del repo: fork de repo full-stack, valida comprensión generada por IA, define reglas en `.agents/rules` y genera `memory-bank` con producto, stack y estado actual.

22. **[Proyecto de specs — dashboard financiero empresarial](./company-financial-dashboard-specs-project)**  
    Asignación spec-first: tipos TypeScript alineados con `/docs`, `components.md` y README de contrato de datos — sin implementación React.

23. **[Proyecto de skills — dashboard financiero empresarial](./company-financial-dashboard-skills-project)**  
    Continúa en el mismo repo: aplica skills de agente (`accessibility`, `vercel-react-best-practices`), explora `skills.sh`, autoría skill custom bajo `.skills/` y actualiza memory bank.

24. **[Hito 4 — Ingeniería impulsada por IA](./ai-eng-milestone-ai-driven-engineering)**  
    `Hito 4` — Layout monorepo: sitio Next.js público, backoffice interno, services/APIs e integración de hitos previos con flujo de entrega asistido por IA.

25. **[Propuesta de arquitectura backend](./ai-eng-architectural-proposal)**  
    Documento de arquitectura y diagramas para extender el sistema de la empresa (servicios, datos, riesgos y trade-offs).

26. **[Lista de tareas por voz con API de IA](./voice-to-do-list-api)**  
    Flujo to-do por voz: captura input del usuario, integra API de IA y transforma peticiones habladas en gestión de tareas.

27. **[Analizador de incidentes — Script y panel de control](./ai-eng-company-incidents-file-analyzer)**  
    Script Python para validar y resumir CSVs de incidentes, luego FastAPI + UI web para subir archivos, ver resúmenes y exportar resultados.

28. **[Agent loop básico de inventario con IA](./ai-basic-inventory-agent-loop)**  
    API FastAPI de inventario más agent loop Python que usa endpoints como tools, registra interacciones en CSV y soporta operaciones de stock en lenguaje natural.

29. **[Directorio de proveedores — API de almacenamiento ligero](./ai-eng-supplier-directory)**  
    API FastAPI + TinyDB + Pydantic: datos sembrados desde `CONTEXT`, validación, CRUD y filtros por país y categoría.

30. **[Asegurando la API: autenticación y restricción de rutas en FastAPI](./ai-eng-user-authentication-api)**  
    Auth JWT en la API de proveedores: registro, login, rutas protegidas, hash de contraseñas y checks de ownership.

31. **[Conectando el candado: flujos de autenticación en el frontend](./ai-eng-user-authentication-flows)**  
    Flujos frontend contra la API asegurada: login, registro, manejo de sesión y vistas protegidas.

32. **[La pieza que faltaba: flujo de restablecimiento de contraseña](./ai-eng-user-authentication-restore)**  
    Reset de contraseña end-to-end: tokens seguros, email o stub de desarrollo, y alineación UI/API.

33. **[Construyendo aplicaciones a prueba de balas](./ai-eng-building-bullet-proof-applications)**  
    Suite de tests unitarios en la API de autenticación: lógica de tokens, casos límite de validación y comportamiento de endpoints.

34. **[Gestor centralizado de incidentes](./ai-eng-centralized-incident-manager)**  
    Integra gestor de incidentes en tiempo real en el monorepo: registrar, consultar y rastrear incidentes desde el navegador con `CONTEXT-empresa.md`.

35. **[Manejo de errores](./ai-eng-error-handling)**  
    Audita y corrige manejo de errores en el monorepo: fallos de API, estados de carga, mensajes al usuario y salida de scripts antes del siguiente hito.

36. **[Auditoría de datos EduTrack](./edutrack-data-audit-sql)**  
    Auditoría SQL en dataset de inscripciones de una tabla: checks de calidad, agregaciones e informe escrito para operaciones.

37. **[Auditoría EduTrack — Tablas relacionadas](./edutrack-data-audit-sql-related-tables)**  
    SQL multi-tabla en esquema EduTrack normalizado: JOINs, métricas cruzadas y respuestas que relacionan estudiantes, cursos e inscripciones.

38. **[Hito de empresa: Backend — Gestión de inventario](./ai-eng-milestone-backend-development)**  
    `Hito 5` (backend) — API FastAPI + SQLModel de inventario en Supabase: dual-database, órdenes entrantes/salientes y reglas de negocio desde `CONTEXT-empresa.md`.

39. **[Hito de empresa: Backoffice — Gestión de inventario](./ai-eng-inventory-management-backoffice)**  
    `Hito 5` (frontend) — UI backoffice para operaciones de inventario conectada a la API del Hito 5.

40. **[Listo para lanzar: MVP containerizado desde cero](./launch-ready-containerized-mvp)**  
    Módulo standalone: Dockeriza un MVP pequeño generado con IA usando Dockerfile, Compose y ejecución local reproducible.

41. **[Containerización del monorepo de la empresa](./ai-eng-container-project)**  
    Containeriza el monorepo: `docker-compose.yml` multi-servicio, configuración de entorno y orquestación local lista para producción.

42. **[Auditoría de rendimiento frontend](./ai-eng-performance-web-vitals)**  
    Auditoría Lighthouse del sitio corporativo y backoffice, refactor de componentes/hooks reutilizables e informe antes/después con Core Web Vitals.

43. **[Auditoría de serialización backend](./ai-eng-performance-serialization)**  
    Auditoría endpoint por endpoint de serialización en la API del monorepo: DTOs, shaping de payloads y fixes de seguridad antes de escalar.

44. **[Optimización de rendimiento: caché](./ai-eng-performance-caching)**  
    Perfila hot paths frontend y API, implementa caché justificada (TTL, `useMemo`, caché FastAPI) y documenta trade-offs en informe técnico.

45. **[Diseño del plan de telemetría de tu compañía](./ai-eng-telemetry-plan)**  
    Diseña `telemetry-plan.md` y `event-schemas.json` desde métricas obligatorias del CONTEXT más un catálogo amplio de oportunidades antes de instrumentar código.

46. **[Telemetría de tu compañía – Captura en el frontend](./ai-eng-telemetry-capture)**  
    Stub `POST /telemetry/events` + `TelemetryService` (cola, batch/debounce, `sendBeacon`, reintentos) instrumentando métricas obligatorias del CONTEXT y un piso técnico vía `track()` única.

47. **[Telemetría de tu compañía – Almacenamiento](./ai-eng-telemetry-storage)**  
    Sustituye stub por Supabase `telemetry_events`: validación por evento, bulk insert, `{ received, stored, rejected }`, frontend intacto.

48. **[Telemetría de tu compañía – Reporte técnico](./ai-eng-telemetry-report)**  
    Pipeline Pandas técnico/operacional más `GET /telemetry/report` (≥3 métricas, caché 60s) — no es un dashboard de negocio.

49. **[Diseñando un Data Pipeline: del dato crudo a los reportes confiables](./designing-data-pipeline)**  
    Ejercicio standalone de diseño ETL para Veridian Logistics: analiza exportaciones CSV nocturnas con updates-as-inserts, documenta deduplicación e idempotencia y produce `PIPELINE_DESIGN.md` — sin código de orquestación.

50. **[Hito 6 — Diseño del pipeline de datos de la compañía (1/3)](./ai-eng-milestone-data-pipeline-design)**  
    `Hito 6` (diseño) — Documenta un pipeline de telemetría listo para producción en el monorepo: estado actual, diagrama ETL, idempotencia, log de ejecución y mapeo Prefect antes de escribir código.

51. **[Hito 6 — Implementación de un Data Pipeline Resiliente (2/3)](./ai-eng-milestone-data-pipeline-build)**  
    `Hito 6` (build) — Implementa flows Prefect extract-transform-load en el monorepo con reintentos, cargas idempotentes, ejecución por script y endpoints de estado/disparo del pipeline.

52. **[Hito 6 — Mejora del pipeline de datos: Subflows y tests (3/3)](./ai-eng-milestone-data-pipeline-enhancement)**  
    `Hito 6` (mejora) — Refactoriza el pipeline en subflows reutilizables, añade tests unitarios aislados para tasks de transformación y garantiza la ejecución por script con `python data/pipelines/pipeline.py`.

53. **[Procesos en segundo plano](./ai-eng-cronjobs)**  
    Cronjob nocturno de exportación de telemetría en el monorepo: script CLI independiente, máquina de estados `job_runs`, distributed lock, exportación CSV idempotente, disparo del pipeline por subproceso y override `TARGET_DATE` para pruebas.

54. **[Branch Queue — Cola de servicio etiquetada](./branch-queue)**  
    Gestor de cola en terminal Python para sucursal bancaria: una `deque` por tipo de servicio, contador global de tickets, menú CLI y notas de diseño — solo stdlib.

55. **[Triage Queue — Gestor de cola de prioridad](./triage-queue)**  
    Cola de prioridad en terminal Python para urgencias: niveles de triaje 1–3 con FIFO dentro del nivel, cinco operaciones núcleo, menú CLI y notas de estructura de datos — solo stdlib.

56. **[Colas de mensajes y tareas asíncronas](./ai-eng-message-queue)**  
    Desacopla trabajo pesado de la API con Redis y Celery en el monorepo: `202` + `task_id`, `GET /tasks/{task_id}`, reintentos con backoff, Dead Letter Queue, worker como proceso separado y monitoreo con Flower.

57. **[Análisis de Sentimiento en Reseñas de Clientes — WeLoveReviews](./existing-model-sentiment-analysis-reviews)**  
    Integra `nlptown/bert-base-multilingual-uncased-sentiment` de Hugging Face para clasificar 500 reseñas de servicios, encuentra falsos negativos por desajuste de dominio de reseñas de productos, valida predicciones manualmente y entrega un reporte listo para el cliente.

58. **[StreamLoop — Ajuste del modelo de churn](./streamloop-churn-model-tuning)**  
    Ajusta un clasificador de churn en el dataset estilo telecom de StreamLoop: Pipeline sklearn con preprocesado interno, baseline por defecto, RandomizedSearchCV → GridSearchCV solo en train, métrica alineada al negocio, revisión de estabilidad en `cv_results_` y `tuning_report.md`.

59. **[Hito 7 — RAG y Base de Conocimiento](./ai-eng-milestone-rag-knowledge-base)**  
    `Hito 7` — RAG modular en el monorepo: fragmenta e indexa documentos del CONTEXT en Qdrant (`setup`, `embed`), recupera con umbral de similitud, genera respuestas con voz comercial (`query`), expone `POST /knowledge/query` vía FastAPI, UI mínima de consulta y tests unitarios — sin LangChain; nunca devolver hits vectoriales crudos.

60. **[Agente de Soporte con LangGraph — Parte 1: Migración y Flujo del Agente](./ai-eng-langgraph-agent-base)**  
    `Parte 1 de 2` — Envuelve el RAG del Hito 7 en un LangGraph compilado con estado mínimo, nodos de responsabilidad única, aristas condicionales, checkpointing, traces consultables, evals en `tests/pipelines/` y `POST /agent/query` — reutiliza `data/pipelines/` sin duplicar.

61. **[Agente de Soporte con LangGraph — Parte 2: Herramientas Fuera del RAG](./ai-eng-langgraph-agent-tools)**  
    `Parte 2 de 2` — Extiende el grafo de la Parte 1 con tools externas tipadas: consulta de tickets contra tu API real del gestor de incidentes (timeout + fallback honesto), consulta opcional de inventario, enrutamiento automático RAG vs tool, traces extendidos y ≥2 evals nuevos de enrutamiento en `tests/pipelines/` — sin datos operativos simulados.

62. **[Servidor MCP: Conectando tu Agente con las Herramientas de la Empresa](./ai-eng-mcp-company-tools)**  
    Expón el Incidents Manager y el inventario de solo lectura como un servidor FastMCP autenticado (API Key, mínimo privilegio, esquemas de discovery, logs de invocación), valídalo con un cliente MCP y migra el agente LangGraph para consumir incidentes vía MCP en lugar de tools HTTP directas.

63. **[Hito 8 — Memoria y Auto-mejora de Agentes (Parte 1 de 2)](./ai-eng-milestone-agentic-engineering)**  
    `Hito 8` Parte 1 — Extiende el agente LangGraph de la empresa (RAG + MCP) con memoria persistente: interfaz explícita de lectura/escritura, `memory_proposal` estructurado, proponer en conversación → confirmar clasificado → auditar → consolidar — solo hechos permitidos por CONTEXT, nunca escrituras silenciosas. Misma identidad de agente que la Parte 2.

64. **[Hito 8 — Aseguramiento de Agentes: Harness y Guardrails (Parte 2 de 2)](./ai-eng-agent-harness)**  
    `Hito 8` Parte 2 — Cierra el **mismo** agente de la empresa después de memoria: system prompt seguro alineado al CONTEXT, guardrails de contenido/alcance (bloqueo de uso personal + redirección casual), aislamiento anti-inyección de texto RAG/MCP, validación de salida, observabilidad de guardrails y tests **deterministas** del harness — defensas en capas, no un único filtro ni solo un LLM vivo.

65. **[Hito — Flujo Agéntico de RFPs: Recepción y Enrutamiento (Parte 1 de 3)](./ai-eng-milestone-agentic-workflows-orchestrate)**  
    `Hito 9` Parte 1 — Ingesta agéntica de RFPs: router de triage, filtro de RFP, descomposición orchestrator-worker en workstreams paralelos y synthesizer hacia la estructura definida en el CONTEXT.

66. **[Hito — Flujo Agéntico de RFPs: Generación de Respuestas (Parte 2 de 3)](./ai-eng-milestone-agentic-workflows-evaluate)**  
    `Hito 9` Parte 2 — Mapea workstreams a departamentos, genera y autoevalúa cada sección y produce tickets de asignación — misma fila de ticket que la Parte 1.

67. **[Hito — Flujo Agéntico de RFPs: Aprobación y Cierre (Parte 3 de 3)](./ai-eng-milestone-agentic-workflows-produce)**  
    `Hito 9` Parte 3 — Interrupt/resume human-in-the-loop por departamento, ramas en paralelo bajo interrupt, árbitro de conflicto del CONTEXT, síntesis automática del documento final y continuidad E2E desde las Partes 1–2.

68. **[Hito 10 — Sistemas en Tiempo Real (Parte 1 de 2): Notificaciones SSE](./ai-eng-milestone-real-time-notification)**  
    `Hito 10` Parte 1 — Empuja notificaciones de tickets RFP al dashboard por SSE: evento nombrado + payload del CONTEXT, keep-alive, `fetch` + `ReadableStream`, reconexión con backoff sin duplicados — solo capa de comunicación (sin modelo/agente).

69. **[Hito 10 — Sistemas en Tiempo Real (Parte 2 de 2): Streaming de Chat por WebSocket](./ai-eng-milestone-real-time-communication)**  
    `Hito 10` Parte 2 — WebSocket bidireccional para el agente de soporte existente: streaming de tokens, interrupt a mitad de respuesta + checkpointing, pub/sub por sesión, UI de escritura en vivo, reconexión con backoff — reutiliza el naming de eventos de la Parte 1; no reescribas la lógica del agente.

70. **[Entrega final — Vídeo del proyecto final: pitch de IA en 5 minutos](./ai-eng-capstone-project)**  
    Capstone — Graba un pitch horizontal de ~5 minutos del sistema de IA de la empresa: gancho, problema, demo en vivo, trade-offs de ingeniería y Q&A de 4Geeks listo para cortar. Entrega una carpeta de Google Drive (o similar) con `FirstnameLastname-ProjectName.mp4`, una descripción de 1–2 frases y la cesión de imagen firmada.

## Otros proyectos

No forman parte de la secuencia del temario. Se mantienen aquí como referencia o uso opcional.

- **[Plataforma – Roles y Permisos](./ai-eng-roles-permissions)**  
  Ejes independientes de rol y departamento en la plataforma de la empresa: 403 centralizado, datos con alcance departamental y vista Admin solo para roles/departamentos.

- **[Plataforma – Autenticación Federada](./ai-eng-federated-authentication)**  
  Vincular Google / Microsoft / LinkedIn solo desde un perfil existente: el login federado nunca crea cuentas; OAuth `state` + `redirect_uri`; auditar intentos rechazados.

- **[Plataforma – Registro de Auditoría](./ai-eng-audit-log)**  
  Rastro de eventos auditable append-only con evidencia de alteración, atribución proceso-vs-humano y consulta con alcance por rol/departamento.

- **[Plataforma – Procesamiento Asíncrono](./ai-eng-async-processing)**  
  Saca una operación con proveedor externo del ciclo request: cola + worker, backoff exponencial, DLQ, claves de idempotencia y estado consultable.

- **[Plataforma – Endurecimiento de Seguridad](./ai-eng-security-hardening)**  
  Auditoría OWASP guiada sobre tu app del monorepo: ≥3 hallazgos reales con prueba antes/después, rate limits en endpoints sensibles y documentación de rotación de secretos.

---

Cada proyecto tiene instrucciones detalladas en su carpeta (`README.md` y, si existe, `README.es.md`). Para empezar, abre la carpeta del proyecto y sigue el README.
