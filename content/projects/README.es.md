# Proyectos de Ingeniería de IA

Repositorio de proyectos prácticos del programa de **Ingeniería de IA** de 4Geeks Academy. Cada carpeta es un proyecto independiente con su propio README, criterios de evaluación y, cuando aplica, `learn.json` para la plataforma.

Los proyectos siguen un orden pedagógico: desde fundamentos web (HTML, CSS, SEO, accesibilidad) y Tailwind, pasando por hitos de empresa y colaboración, **configuración e integraciones de agentes OpenClaw**, luego TypeScript y diseño de sistemas, React/Next.js y entrega asistida por IA, APIs, autenticación, agentes, rendimiento, telemetría, pipelines de datos, jobs en segundo plano y colas de mensajes.

---

## Proyectos (orden sugerido)

0. **[Hito de empresa: Elige tu compañía](./ai-eng-milestone-choose-company)**  
   `Hito 0` — Elige tu empresa ficticia, captúrala en `CONTEXT.md` y prepara la narrativa y los datos que reutilizarás en hitos posteriores.

1. **[Landing de artista: HTML, CSS, SEO y accesibilidad](./html-css-artist-landing-seo-access)**  
   Landing accesible y optimizada para SEO de un artista usando HTML semántico y CSS.

2. **[Dashboard simple con Tailwind CSS](./simple-dashboard-tailwind-css)**  
   Dashboard responsive con HTML y Tailwind mostrando KPIs, drivers y detalles operativos (sin React).

3. **[Hito de empresa: Fundamentos web](./ai-eng-milestone-web-fundamentals)**  
   `Hito 1` — Sitio público de tu empresa: landing más formulario de registro con HTML5 semántico, Tailwind, Schema.org y validación JavaScript. Sigue `CONTEXT.md` para datos y campos del formulario.

4. **[Proyecto colaborativo: tienda online con HTML y Tailwind](./collaborative-project-html-tailwind-online-store)**  
   Prototipo e-commerce colaborativo (mín. 5 páginas: Home, Catálogo, Producto, Carrito, Checkout) con HTML y Tailwind, trabajo en equipo con ramas y pull requests.

5. **[Configura tu agente de IA personal con OpenClaw](./openclaw-setup)**  
   Despliega y configura OpenClaw en un VPS con LiteLLM, valida el chat local y documenta un paquete de entrega seguro (config saneada + captura de prueba).

6. **[Conecta tu agente: Telegram, Google Drive y Calendar](./openclaw-connection)**  
   Proyecto solo de configuración: canal Telegram, Zapier MCP, acciones de Google Drive y Calendar, y flujo end-to-end confirmado con capturas (después de tener OpenClaw en marcha).

7. **[Mi agente, a mi manera: enseña nuevas skills a tu asistente](./openclaw-skills)**  
   Continúa en tu entorno OpenClaw y repo de tareas previas: completa los cinco archivos de briefing `.openclaw`, commitea `SKILLS_DESIGN.md` e implementa al menos dos skills OpenClaw usando solo integraciones Composio que ya tengas (Google apps, GitHub, Telegram).

8. **[Mi asistente 4Geeks — OpenClaw sigue tu progreso](./openclaw-integration)**  
   Conecta OpenClaw a la API de 4Geeks con tu token para que el agente reporte proyectos pendientes, progreso del curso y datos LearnPack relacionados.

9. **[Dale memoria a tu agente](./openclaw-memory)**  
   Configura tipos de memoria OpenClaw (episódica, semántica, procedimental), reestructura archivos del workspace y valida que el contexto persiste entre sesiones.

10. **[Agente de onboarding con memoria](./openclaw-onboarding-agent)**  
    Construye un flujo de onboarding empresarial: agente OpenClaw con memoria que lee plantillas HR y envía email de bienvenida personalizado desde tu `CONTEXT-empresa.md`.

11. **[Gestor de asientos de cine (TypeScript)](./seats-management-typescript)**  
    Sistema de reserva de asientos en terminal con array 2D: reservar, contar y buscar asientos adyacentes.

12. **[Reproductor de playlist — Modelado de objetos](./data-modeling-and-class-diagrams-music-player)**  
    Diagrama de clases UML para un reproductor de playlist en diagram.4geeks.com: entidades, tipos de datos y relaciones.

13. **[Billetera digital — Modelado de objetos](./data-modeling-and-class-diagrams-digital-wallet)**  
    Diagrama de clases UML para una billetera digital con historial de transacciones en diagram.4geeks.com.

14. **[Hito de empresa: Fundamentos de programación (TypeScript)](./ai-eng-milestone-coding-fundamentals)**  
    `Hito 2` — Fundamentos con TypeScript: módulos pequeños y testeables (control de flujo, arrays, objetos, funciones, casos límite) con buenas prácticas.

15. **[Plataforma de alquiler de agentes IA: prototipo de panel admin](./agent-hub-ui-specs-and-prompts)**  
    Frontend spec-driven: escribe `SPECS.md` primero, luego dashboard y vistas de gestión con HTML, Tailwind y JavaScript vanilla.

16. **[Habla con la máquina: interfaz de chat con API de IA real](./chat-interface-real-ai-api)**  
    Interfaz de chat en el navegador que llama a la API Groq con `fetch`, envía historial completo y rastrea tokens y métricas de respuesta.

17. **[Wanderlust Explorer con React y Next.js](./nextjs-wanderlust-explorer)**  
    App Next.js App Router desde cero: listado de experiencias con búsqueda y filtros en URL, páginas de detalle, favoritos en estado y dataset TypeScript local.

18. **[Clon UI de Airbnb con Next.js y React](./nextjs-airbnb-ui-clone)**  
    Clon UI Next.js 16 + TypeScript + Tailwind desde brief de producto: layout, componentes reutilizables y datos tipados.

19. **[Hito de empresa: Talent Pipeline Tracker](./ai-eng-milestone-frontend-development)**  
    `Hito 3` — Frontend Next.js App Router para la API de reclutamiento: listado y detalle de candidatos, filtros, CRUD de notas, formularios y estados async alineados con `CONTEXT-empresa.md`.

20. **[Proyecto de contexto — dashboard financiero empresarial](./company-financial-dashboard-context-project)**  
    Stewardship del repo: fork de repo full-stack, valida comprensión generada por IA, define reglas en `.agents/rules` y genera `memory-bank` con producto, stack y estado actual.

21. **[Proyecto de specs — dashboard financiero empresarial](./company-financial-dashboard-specs-project)**  
    Asignación spec-first: tipos TypeScript alineados con `/docs`, `components.md` y README de contrato de datos — sin implementación React.

22. **[Proyecto de skills — dashboard financiero empresarial](./company-financial-dashboard-skills-project)**  
    Continúa en el mismo repo: aplica skills de agente (`accessibility`, `vercel-react-best-practices`), explora `skills.sh`, autoría skill custom bajo `.skills/` y actualiza memory bank.

23. **[Hito 4 — Ingeniería impulsada por IA](./ai-eng-milestone-ai-driven-engineering)**  
    `Hito 4` — Layout monorepo: sitio Next.js público, backoffice interno, services/APIs e integración de hitos previos con flujo de entrega asistido por IA.

24. **[Propuesta de arquitectura backend](./ai-eng-architectural-proposal)**  
    Documento de arquitectura y diagramas para extender el sistema de la empresa (servicios, datos, riesgos y trade-offs).

25. **[Lista de tareas por voz con API de IA](./voice-to-do-list-api)**  
    Flujo to-do por voz: captura input del usuario, integra API de IA y transforma peticiones habladas en gestión de tareas.

26. **[Analizador de incidentes — Script y panel de control](./ai-eng-company-incidents-file-analyzer)**  
    Script Python para validar y resumir CSVs de incidentes, luego FastAPI + UI web para subir archivos, ver resúmenes y exportar resultados.

27. **[Agent loop básico de inventario con IA](./ai-basic-inventory-agent-loop)**  
    API FastAPI de inventario más agent loop Python que usa endpoints como tools, registra interacciones en CSV y soporta operaciones de stock en lenguaje natural.

28. **[Directorio de proveedores — API de almacenamiento ligero](./ai-eng-supplier-directory)**  
    API FastAPI + TinyDB + Pydantic: datos sembrados desde `CONTEXT`, validación, CRUD y filtros por país y categoría.

29. **[Asegurando la API: autenticación y restricción de rutas en FastAPI](./ai-eng-user-authentication-api)**  
    Auth JWT en la API de proveedores: registro, login, rutas protegidas, hash de contraseñas y checks de ownership.

30. **[Conectando el candado: flujos de autenticación en el frontend](./ai-eng-user-authentication-flows)**  
    Flujos frontend contra la API asegurada: login, registro, manejo de sesión y vistas protegidas.

31. **[La pieza que faltaba: flujo de restablecimiento de contraseña](./ai-eng-user-authentication-restore)**  
    Reset de contraseña end-to-end: tokens seguros, email o stub de desarrollo, y alineación UI/API.

32. **[Construyendo aplicaciones a prueba de balas](./ai-eng-building-bullet-proof-applications)**  
    Suite de tests unitarios en la API de autenticación: lógica de tokens, casos límite de validación y comportamiento de endpoints.

33. **[Gestor centralizado de incidentes](./ai-eng-centralized-incident-manager)**  
    Integra gestor de incidentes en tiempo real en el monorepo: registrar, consultar y rastrear incidentes desde el navegador con `CONTEXT-empresa.md`.

34. **[Manejo de errores](./ai-eng-error-handling)**  
    Audita y corrige manejo de errores en el monorepo: fallos de API, estados de carga, mensajes al usuario y salida de scripts antes del siguiente hito.

35. **[Auditoría de datos EduTrack](./edutrack-data-audit-sql)**  
    Auditoría SQL en dataset de inscripciones de una tabla: checks de calidad, agregaciones e informe escrito para operaciones.

36. **[Auditoría EduTrack — Tablas relacionadas](./edutrack-data-audit-sql-related-tables)**  
    SQL multi-tabla en esquema EduTrack normalizado: JOINs, métricas cruzadas y respuestas que relacionan estudiantes, cursos e inscripciones.

37. **[Hito de empresa: Backend — Gestión de inventario](./ai-eng-milestone-backend-development)**  
    `Hito 5` (backend) — API FastAPI + SQLModel de inventario en Supabase: dual-database, órdenes entrantes/salientes y reglas de negocio desde `CONTEXT-empresa.md`.

38. **[Hito de empresa: Backoffice — Gestión de inventario](./ai-eng-inventory-management-backoffice)**  
    `Hito 5` (frontend) — UI backoffice para operaciones de inventario conectada a la API del Hito 5.

39. **[Listo para lanzar: MVP containerizado desde cero](./launch-ready-containerized-mvp)**  
    Módulo standalone: Dockeriza un MVP pequeño generado con IA usando Dockerfile, Compose y ejecución local reproducible.

40. **[Containerización del monorepo de la empresa](./ai-eng-container-project)**  
    Containeriza el monorepo: `docker-compose.yml` multi-servicio, configuración de entorno y orquestación local lista para producción.

41. **[Auditoría de rendimiento frontend](./ai-eng-performance-web-vitals)**  
    Auditoría Lighthouse del sitio corporativo y backoffice, refactor de componentes/hooks reutilizables e informe antes/después con Core Web Vitals.

42. **[Auditoría de serialización backend](./ai-eng-performance-serialization)**  
    Auditoría endpoint por endpoint de serialización en la API del monorepo: DTOs, shaping de payloads y fixes de seguridad antes de escalar.

43. **[Optimización de rendimiento: caché](./ai-eng-performance-caching)**  
    Perfila hot paths frontend y API, implementa caché justificada (TTL, `useMemo`, caché FastAPI) y documenta trade-offs en informe técnico.

44. **[Diseño del plan de telemetría de la empresa](./ai-eng-telemetry-plan)**  
    Diseña `telemetry-plan.md` y `event-schemas.json` desde KPIs de inventario en `CONTEXT-empresa.md` antes de instrumentar código.

45. **[Telemetría de la empresa — Captura frontend](./ai-eng-telemetry-capture)**  
    `TelemetryService` en Next.js: cola, batch/debounce, `sendBeacon`, reintentos y API `track()` única hacia `POST /telemetry/events`.

46. **[Telemetría de la empresa — Almacenamiento](./ai-eng-telemetry-storage)**  
    Persiste telemetría por lotes en Supabase/PostgreSQL con validación por evento, aceptación parcial de lotes y contrato frontend sin cambios.

47. **[Telemetría de la empresa — Informe](./ai-eng-telemetry-report)**  
    Pipeline Pandas más `GET /telemetry/report` con métricas agrupadas, caché de respuesta 60s e informes accionables de inventario/uso.

48. **[Diseñando un Data Pipeline: del dato crudo a los reportes confiables](./designing-data-pipeline)**  
    Ejercicio standalone de diseño ETL para Veridian Logistics: analiza exportaciones CSV nocturnas con updates-as-inserts, documenta deduplicación e idempotencia y produce `PIPELINE_DESIGN.md` — sin código de orquestación.

49. **[Hito 6 — Diseño del pipeline de datos de la compañía (1/3)](./ai-eng-milestone-data-pipeline-design)**  
    `Hito 6` (diseño) — Documenta un pipeline de telemetría listo para producción en el monorepo: estado actual, diagrama ETL, idempotencia, log de ejecución y mapeo Prefect antes de escribir código.

50. **[Hito 6 — Implementación de un Data Pipeline Resiliente (2/3)](./ai-eng-milestone-data-pipeline-build)**  
    `Hito 6` (build) — Implementa flows Prefect extract-transform-load en el monorepo con reintentos, cargas idempotentes, deployment Docker programado y endpoints de estado/disparo del pipeline.

51. **[Hito 6 — Mejora del pipeline de datos: Subflows y tests (3/3)](./ai-eng-milestone-data-pipeline-enhancement)**  
    `Hito 6` (mejora) — Refactoriza el pipeline en subflows reutilizables, añade tests unitarios aislados para tasks de transformación y completa el deployment Docker de producción con verificación en Prefect Cloud.

52. **[Procesos en segundo plano](./ai-eng-cronjobs)**  
    Cronjob nocturno de exportación de telemetría en el monorepo: script CLI independiente, máquina de estados `job_runs`, distributed lock, exportación CSV idempotente, disparo del pipeline por subproceso y override `TARGET_DATE` para pruebas.

53. **[Branch Queue — Cola de servicio etiquetada](./branch-queue)**  
    Gestor de cola en terminal Python para sucursal bancaria: una `deque` por tipo de servicio, contador global de tickets, menú CLI y notas de diseño — solo stdlib.

54. **[Triage Queue — Gestor de cola de prioridad](./triage-queue)**  
    Cola de prioridad en terminal Python para urgencias: niveles de triaje 1–3 con FIFO dentro del nivel, cinco operaciones núcleo, menú CLI y notas de estructura de datos — solo stdlib.

55. **[Colas de mensajes y tareas asíncronas](./ai-eng-message-queue)**  
    Desacopla trabajo pesado de la API con Redis y Celery en el monorepo: `202` + `task_id`, `GET /tasks/{task_id}`, reintentos con backoff, Dead Letter Queue, worker como proceso separado y monitoreo con Flower.

56. **[Análisis de Sentimiento en Reseñas de Clientes — WeLoveReviews](./ai-eng-sentiment-analysis-reviews)**  
    Integra `prajjwal1/bert-mini` de Hugging Face para clasificar 500 reseñas, compara la distribución de sentimiento con un promedio de 4.5 estrellas, valida predicciones manualmente y entrega un reporte listo para el cliente.

---

Cada proyecto tiene instrucciones detalladas en su carpeta (`README.md` y, si existe, `README.es.md`). Para empezar, abre la carpeta del proyecto y sigue el README.
