# CONTEXT — TrackFlow: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.

## 1. Introducción

En TrackFlow, las RFPs llegan al equipo de **Miguel Torres, Commercial Director**: marcas de e-commerce (moda, electrónica, cosmética) que quieren tercerizar su logística — almacenamiento, última milla, devoluciones, o una combinación — en Estados Unidos, España, o ambos. Hoy, cada account manager arma la propuesta a mano, coordinando por correo con Warehouse, Last Mile y Reverse Logistics; el proceso es lento y a veces una propuesta llega después de que el prospecto ya firmó con otro proveedor.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento:

| `department_id` | Departamento                     | Responsable   | Qué aporta a la propuesta                                                   |
| --------------- | -------------------------------- | ------------- | --------------------------------------------------------------------------- |
| `warehouse`     | Warehouse Operations             | Ana Whitfield | Capacidad de almacenamiento, costo por pallet/SKU, tiempo de onboarding     |
| `lastmile`      | Last Mile and Carrier Management | Carlos Vega   | Costo por envío, transportistas disponibles según destino, SLA de entrega   |
| `reverse`       | Reverse Logistics                | Sofía Ramos   | Costo y tiempo de procesamiento de devoluciones (si el cliente lo solicita) |

No toda RFP necesita a los tres departamentos: un cliente puede pedir solo almacenamiento y devoluciones, sin última milla (porque usa su propio transportista), por ejemplo. Tu clasificador/orquestador debe decidir qué departamentos aplican según el alcance solicitado.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF e incluyen normalmente: nombre y país de origen del cliente (EE. UU. o España — define la moneda), servicios solicitados (warehousing, last mile, reverse logistics), volumen estimado (pedidos/mes), fecha límite, y a veces un presupuesto de referencia.

### 2.3 Entidades sugeridas para tu estado

Persiste **Ticket**, **metadatos RFP** y **DepartmentSection** (al menos `key_aspects` en la Parte 1; borradores/evals/aprobaciones en partes posteriores) en **PostgreSQL (Supabase)** vía tu capa SQLModel/DB existente. TinyDB o archivos JSON no son la fuente de verdad de estas entidades.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`, métricas de legibilidad
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

**Estado del ticket por parte** (mismo ticket en Partes 1–3):

| Estado                 | Parte | Cuándo                                              |
| ---------------------- | ----- | --------------------------------------------------- |
| `analizando`           | 1     | Subida aceptada; pipeline en curso                  |
| `descartado`           | 1     | El clasificador rechazó el documento                |
| `analisis_completo`    | 1     | Synthesizer listo; Ventas puede leer aspectos clave |
| `generando_borrador`   | 2     | Generadores escribiendo secciones                   |
| `en_evaluación`        | 2     | Evaluadores en paralelo / ciclo generador-evaluador |
| `needs_human_review`   | 2     | Límite de iteraciones agotado; último borrador + EvaluationResult pasan a Parte 3 |
| `esperando_aprobación` | 3     | Pausa humana por departamento                       |
| `terminado`            | 3     | Documento final generado                            |

Los workers reciben **metadatos compartidos + extractos relevantes a su departamento**. Ejemplo: `warehouse` recibe slices/metadatos de warehousing — si falta el volumen mensual, registra una pregunta abierta; **nunca inventes** pallets/SKU/pedidos que no estén en la RFP.

### 2.4 Layout del monorepo

- **HTTP**: extiende el **backend existente** bajo `services/` — sin un proceso API nuevo.
- **Pipeline / grafo**: `data/pipelines/rfp_intake/` (grafo dedicado; no lo mezcles con el grafo CX). Los routers importan y disparan; no poseen la lógica de agentes.
- **CLIs sueltos**: `scripts/` si hace falta.
- **PDFs subidos**: vía `uis/backoffice`; se guardan bajo `data/raw/` como artefacto runtime de la recepción.

## 3. Métricas de negocio y KPIs

- **Tiempo de armado de propuesta**: hoy varios días de coordinación manual → meta: menos de 2 días desde la carga de la RFP hasta el documento final.
- **Tasa de clasificación correcta** de RFPs vs. documentos que no lo son.
- **Iteraciones promedio por sección** en el ciclo generador-evaluador (ideal: menos de 2).
- **Tiempo de aprobación por departamento** desde que la sección está lista hasta la decisión del responsable.

## 4. Instrucciones de datos semilla

Usa los PDF listos en [`rfp-requests/trackflow/`](./rfp-requests/trackflow/) como **subidas de prueba a través de la UI**. El proceso de recepción guarda cada PDF subido bajo `data/raw/` (no trates los PDF del currículo como inventario pre-sembrado en el repo). Las RFP formales e informales deben **aceptarse y procesarse**; el documento inválido debe **rechazarse**.

1. **`CONTEXT-trackflow-request-1.pdf` — RFP formal (aceptar):** _ModaViva_ (España), solo almacenamiento + devoluciones (transportista propio para última milla). Activa `warehouse` y `reverse`, no `lastmile`. Moneda: EUR.
2. **`CONTEXT-trackflow-request-2.pdf` — RFP informal (aceptar):** correo de _Luna Cosmetics_ (LA) pidiendo almacenamiento + última milla EE. UU., ~5.000 pedidos/mes. Activa `warehouse` y `lastmile`. Moneda: USD.
3. **`CONTEXT-trackflow-request-3.pdf` — inválido (rechazar):** pitch entrante de tarifas de transportista — no es RFP de cliente. El clasificador debe descartarlo.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- El precio se cotiza en USD para operación en Estados Unidos y en EUR para operación en España — se determina a partir del campo `client_country`.
- Toda propuesta debe indicar el SLA de entrega a tiempo (%) que TrackFlow se compromete a cumplir.
- Ninguna propuesta puede prometer procesamiento de devoluciones en menos de 48 horas.
- Toda propuesta debe incluir una tabla de descuentos por volumen.
- Ninguna propuesta puede revelar tarifas negociadas con transportistas específicos — solo el costo final ofrecido al cliente.

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de TrackFlow, extrae metadatos (incluido el país del cliente) y reparte el análisis solo entre los departamentos que el alcance solicitado realmente requiere.
- **Parte 2:** cada departamento activo genera su sección y pasa por evaluación de legibilidad, pertinencia y cumplimiento de los lineamientos de la sección 5 (incluida la moneda correcta y el SLA).
- **Parte 3:** el responsable nombrado de cada departamento activo (§2.1) aprueba su sección de forma independiente, sin bloquear a los demás, y el documento final se genera solo cuando todas las secciones activas están aprobadas. **No** inventes una escalera jerárquica multi-nivel — TrackFlow solo tiene responsables pares por departamento.

## 7. Parte 3 — Triggers de conflicto y árbitro fijo

El arbitraje debe ser un nodo dedicado del grafo disparado por **contradicciones detectables en estado estructurado**, no por agentes negociando entre ellos.

| Id del trigger       | Cuándo dispara                                                                                                                         | Árbitro fijo (no un LLM)                                                            | Regla de resolución                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `volume-vs-capacity` | La capacidad comprometida de `warehouse` (pallets/SKU o throughput de onboarding) no soporta el volumen mensual asumido por `lastmile` | Miguel Torres (Director Comercial)                                                  | Limitar el volumen de la propuesta a la capacidad de warehouse; `lastmile` debe revisar volumen/costo a la baja   |
| `returns-sla-breach` | `reverse` (u otra sección) promete turnaround de devoluciones bajo 48 horas (viola §5)                                                 | Sofía Ramos rechaza su sección; si otro depto aún embebe esa promesa, Miguel Torres | Forzar `request_changes` en toda sección que diga devoluciones en menos de 48h; sin documento final hasta cumplir |
| `currency-mismatch`  | Dos secciones activas cotizan monedas distintas, o la moneda ≠ mapeo de `client_country` (US→USD, Spain→EUR)                           | Miguel Torres                                                                       | Reescribir las secciones ofensoras a la moneda del país; rechazar si no se resuelve tras el límite de iteraciones |

Conecta estos ids de trigger a tu nodo de arbitraje. Los agentes pueden **señalar** un conflicto; no deben **resolverlo** por consenso libre.
