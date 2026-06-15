# Diseño del plan de telemetría de la compañía

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir una sola línea — define los KPIs, entidades y procesos clave de tu empresa, que son la base sobre la que construirás este plan.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Tu empresa ya tiene un sistema de gestión de inventario en producción: un backend FastAPI con autenticación, un modelo de datos relacional en Supabase y una regla de negocio no negociable — el stock no se modifica directamente, solo a través de órdenes de entrada y salida trazables a un usuario. El sistema funciona. Pero el equipo de operaciones no sabe qué está pasando dentro de él.

El equipo de dirección ha enviado una RFI al equipo de tecnología: quieren saber si el sistema de inventario puede generar información accionable sobre el negocio — tendencias de consumo, alertas tempranas de stock, patrones de error — o si necesitan herramientas externas para eso. Tu tech lead te ha asignado la tarea de responder esa RFI con un **Plan de Telemetría**: un documento técnico que identifica qué datos valen la pena capturar del sistema de inventario, por qué, y cómo estructurarlos antes de escribir una sola línea de instrumentación.

### 📚 Conocimiento complementario — Qué hace valioso un evento de telemetría

La telemetría no se genera por tener datos: se genera para responder preguntas de negocio que hoy no se pueden responder. La diferencia entre un sistema de telemetría útil y uno que nadie mantiene es si cada evento existe por una razón.

**La regla de oro:** si no puedes completar esta frase, el evento no existe — _"Captamos `[nombre_del_evento]` porque necesitamos saber `[hipótesis]`, lo que nos permite tomar la decisión `[decisión concreta]`."_

Dos conceptos que necesitarás aplicar hoy:

- **Batch vs. stream:** ¿Necesita la empresa ver este dato en segundos (stream) o es suficiente procesarlo en lotes periódicos (batch)? La respuesta determina el diseño técnico del pipeline que construirás en los siguientes días.
- **Event Envelope:** estructura estándar que todo evento debe respetar — identificador único (`eventId`), marca de tiempo en ISO 8601 (`timestamp`), identificadores de sesión/usuario (`sessionId`, `userId`), nombre del evento con taxonomía consistente (`entidad_acción`, ej: `order_submitted`), versión del esquema (`schemaVersion`), identificador de correlación (`requestId`/`traceId` para unir frontend–backend–logs), y las propiedades específicas del evento. Un sobre bien diseñado hoy previene duplicados, facilita el debug y hace el pipeline robusto.

---

> Tu tech lead te ha enviado este mensaje:
>
> > "Llevamos semanas con el sistema de inventario funcionando y el equipo de operaciones empieza a preguntar cosas que no sabemos responder: ¿cuántas órdenes de salida se registran por día? ¿Qué productos acumulan más errores de validación? ¿Hay usuarios que intentan modificar stock directamente y el sistema les rechaza? ¿Cuándo se activan más las alertas de stock mínimo?
> >
> > Y no es solo el inventario. El backoffice tiene otras secciones que hoy son cajas negras: ¿cuántos intentos de login fallidos hay por día? ¿Qué secciones visitan más los operadores? ¿Hay flujos que se abandonan a mitad? Cualquier parte de la aplicación que toque un usuario es una oportunidad de datos.
> >
> > Antes de instrumentar nada, necesito un documento de diseño. Parte del modelo que ya tenemos — `Product`, `InboundOrder`, `OutboundOrder`, el router `/inventory` — pero no te limites a él. Identifica los tres KPIs principales del negocio, traza los eventos que los alimentan, define su envelope completo y justifica si debe procesarse en stream o en batch. No escribas código todavía — escribe el plan que el equipo va a implementar mañana.
> >
> > El entregable es un **Plan de Telemetría** en Markdown más un fichero de esquemas JSON. Revisamos el viernes."

---

## 🌱 Cómo Empezar el Proyecto

1. Abre tu fork del monorepo de tu empresa asignada.
2. Lee tu `CONTEXT-company.md` completo y localiza los KPIs, las entidades del sistema de inventario (productos, órdenes) y las restricciones de negocio definidas para tu empresa.
3. Crea la carpeta `docs/telemetry/` dentro del monorepo.
4. Trabaja en los dos entregables dentro de esa carpeta: `telemetry-plan.md` y `event-schemas.json`.

No hay servidor nuevo que levantar hoy. El entregable es documentación de diseño — pero documentación que tiene que ser lo suficientemente precisa como para que otro desarrollador la instrumente en el sistema de inventario existente sin hacerte preguntas.

---

## 💻 Lo Que Debes Hacer

### Fase 1 — Análisis de KPIs y oportunidades de datos

- [ ] Identifica los **3 KPIs principales** de tu empresa a partir de tu `CONTEXT-company.md`. Para cada KPI, responde: ¿qué dato lo compone? ¿dónde se genera ese dato en el sistema?
- [ ] Mapea el **flujo de gestión de inventario** en tu aplicación: desde que un usuario autenticado accede al sistema hasta que completa una orden de entrada o salida. Identifica al menos **5 puntos de instrumentación** en ese flujo — incluyendo intentos de modificación directa de stock (que el sistema rechaza), validaciones fallidas, y activaciones de umbral mínimo.
- [ ] Explora otras secciones del backoffice que también pueden aportar datos valiosos: autenticación (intentos de login, sesiones expiradas, fallos de credenciales), navegación (qué secciones visitan los operadores y con qué frecuencia), y cualquier flujo que un usuario pueda abandonar antes de completarlo. Documenta al menos **2 oportunidades adicionales** fuera del módulo de inventario.
- [ ] Para cada punto de instrumentación, completa la frase: _"Captamos `[evento]` porque necesitamos saber `[hipótesis]`, lo que nos permite tomar la decisión `[decisión]`."_ Si no puedes completarla, descarta el punto.

⚠️ **IMPORTANTE:** Los KPIs, entidades e identificadores en tu plan deben corresponder exactamente a lo que define tu CONTEXT.md. Un plan genérico que ignore el contexto de tu empresa no será aceptado.

### Fase 2 — Diseño del Event Envelope

- [ ] Define el **Event Envelope estándar** que usará tu empresa: los campos obligatorios que todo evento debe incluir (`eventId`, `timestamp` en ISO 8601, `sessionId`, `userId`, nombre del evento, `schemaVersion`, `requestId`/`traceId` para correlación, y las propiedades específicas).
- [ ] Diseña el esquema completo de **al menos 5 eventos** derivados del flujo mapeado en la Fase 1. Cada evento debe tener nombre siguiendo la taxonomía `entidad_acción` con verbos consistentes (ej: `inbound_order_created`, `stock_threshold_triggered`, `direct_stock_edit_rejected`, `session_expired`).
- [ ] Para cada evento, define una **allowlist de propiedades**: lista explícita de las claves permitidas en ese evento. Nada fuera de la allowlist debe incluirse — esto previene fugas accidentales de datos.
- [ ] Para cada evento, especifica: nombre, descripción, propiedades (nombre, tipo, obligatorio/opcional, descripción), y si contiene datos sensibles o PII — en cuyo caso documenta cómo se anonimiza o sanitiza antes de emitir el evento.
- [ ] Exporta los esquemas al fichero `event-schemas.json` con estructura validable (puedes usar JSON Schema draft-07 o una estructura propia documentada).

### Fase 3 — Estrategia de envío

- [ ] Para cada evento diseñado, decide y justifica si debe procesarse en **stream** (tiempo real) o **batch** (lotes periódicos). La justificación debe basarse en la urgencia de la decisión de negocio que alimenta, no en preferencias técnicas.
- [ ] Documenta la estrategia de **throttle/debounce** para eventos de alta frecuencia (si los hay en tu diseño).
- [ ] Escribe una sección de **riesgos y exclusiones** en el plan: eventos que se descartaron y por qué, datos que no se capturarán por razones de privacidad o coste.

---

## ✅ Qué Evaluaremos

- [ ] Los 3 KPIs identificados son representativos del negocio de la empresa asignada y están justificados con datos de `CONTEXT-company.md`
- [ ] Cada evento tiene una hipótesis y una decisión de negocio que lo justifica — no hay eventos "por si acaso"
- [ ] El Event Envelope es consistente en todos los eventos y contiene al menos: `eventId`, `timestamp` (ISO 8601), `sessionId`, `userId`, nombre del evento en formato `entidad_acción`, `schemaVersion`, y `requestId`/`traceId`
- [ ] Cada evento tiene una **allowlist de propiedades** documentada — solo las claves explícitamente permitidas
- [ ] El fichero `event-schemas.json` es válido y los esquemas son coherentes con el plan en Markdown
- [ ] La decisión stream/batch está justificada por urgencia de negocio, no por preferencia técnica
- [ ] Los datos sensibles o PII están identificados y documentados con su estrategia de anonimización o sanitización
- [ ] La sección de riesgos y exclusiones demuestra pensamiento crítico: hay eventos que se descartaron con razón
- [ ] El plan es suficientemente preciso para que otro desarrollador lo instrumente sin necesitar aclaraciones

---

## 📦 Cómo Entregar

1. Asegúrate de que los ficheros `docs/telemetry/telemetry-plan.md` y `docs/telemetry/event-schemas.json` están en tu fork.
2. Crea un Pull Request contra la rama principal del monorepo con el título: `[W16D46] Telemetry Design Plan`.
3. En la descripción del PR, incluye:
   - Los 3 KPIs identificados (una línea cada uno)
   - El número de eventos diseñados
   - Una frase explicando la decisión de diseño más difícil que tomaste

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
