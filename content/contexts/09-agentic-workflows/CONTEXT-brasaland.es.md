# CONTEXT — Brasaland: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.

## 1. Introducción

Brasaland no tiene un departamento de "Ventas" tradicional: las RFPs corporativas (contratos de catering institucional, alianzas de co-marca, concesiones en eventos o resorts) le llegan al equipo de **Camila Ospina, Marketing, Brand and Digital Experience**, que además de campañas y CRM se encarga de recibir y coordinar este tipo de oportunidades B2B. En este hito, el equipo de Marketing es tu "Ventas": ellos abren el ticket y esperan el resultado del flujo agéntico.

Hoy, cuando llega una de estas solicitudes, Camila reenvía el PDF por WhatsApp a Felipe (Operaciones), Lucía (Procurement) y Jake (Training) y espera respuestas sueltas por correo. Armar una propuesta completa toma en promedio **9 días hábiles**, y varias veces se ha perdido una oportunidad porque un departamento no respondió a tiempo. Tu flujo agéntico reemplaza esa coordinación manual.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento en tu código y en el estado del grafo:

| `department_id` | Departamento                     | Responsable     | Qué aporta a la propuesta                                                                      |
| --------------- | -------------------------------- | --------------- | ---------------------------------------------------------------------------------------------- |
| `marketing`     | Marketing y Experiencia Digital  | Camila Ospina   | Términos de marca, exclusividad, co-branding, validez de la oferta. Dueña del ticket.          |
| `operaciones`   | Operaciones de Restaurante       | Felipe Guerrero | Viabilidad operativa: capacidad de cocina/personal, tiempos de montaje, costo operativo/evento |
| `procurement`   | Procurement y Proveedores        | Lucía Fernández | Costo estimado de insumos según volumen, tiempos de entrega de proveedores                     |
| `training`      | Training y Estándares de Calidad | Jake Morrison   | Si el pedido requiere receta o estándar nuevo, tiempo de desarrollo y certificación necesario  |

No toda RFP necesita a los cuatro departamentos: una solicitud de catering simple puede no requerir `training` (por ejemplo, si usa el menú estándar). Tu agente clasificador/orquestador debe decidir qué departamentos aplican según el contenido del documento — no asumas que siempre son los cuatro.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF y normalmente incluyen: nombre del cliente y ubicación, tipo de servicio solicitado (catering recurrente, concesión, co-branding), volumen o alcance (número de comensales, ubicaciones, duración del contrato), fecha límite para responder, y a veces un rango de presupuesto. No siempre están bien estructuradas — algunas son cartas de intención informales.

### 2.3 Entidades sugeridas para tu estado

Persiste **Ticket**, **metadatos RFP** y **DepartmentSection** (al menos `key_aspects` en la Parte 1; borradores/evals/aprobaciones en partes posteriores) en **PostgreSQL (Supabase)** vía tu capa SQLModel/DB existente. TinyDB o archivos JSON no son la fuente de verdad de estas entidades.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (opcional), `departments_needed`, métricas de legibilidad
- **DepartmentSection**: `department_id`, `key_aspects` (Parte 1), `draft_content` (Parte 2), `evaluation_results` (legibilidad, pertinencia, cumplimiento), `approval_status` (`pendiente`, `aprobado`, `rechazado`), `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `total_estimated_value`, `generated_at`

**Estado del ticket por parte** (mismo ticket en Partes 1–3):

| Estado                 | Parte | Cuándo                                              |
| ---------------------- | ----- | --------------------------------------------------- |
| `analizando`           | 1     | Subida aceptada; pipeline en curso                  |
| `descartado`           | 1     | El clasificador rechazó el documento                |
| `analisis_completo`    | 1     | Synthesizer listo; Ventas puede leer aspectos clave |
| `generando_borrador`   | 2     | Generadores escribiendo secciones                   |
| `en_evaluación`        | 2     | Evaluadores en paralelo / ciclo generador-evaluador |
| `needs_human_review`   | 2     | Límite de iteraciones agotado; último borrador + EvaluationResult pasan a Parte 3 |
| `esperando_aprobación` | 3     | Pausa humana por departamento (y CEO si aplica)     |
| `terminado`            | 3     | Documento final generado                            |

Los workers reciben **metadatos compartidos + extractos relevantes a su departamento**. Si falta una cifra (volumen, presupuesto, comensales, etc.) en la RFP, regístrala en `open_questions` / campos faltantes — **nunca inventes** números que no estén en el documento.

### 2.4 Layout del monorepo

- **HTTP**: extiende el **backend existente** bajo `services/` — sin un proceso API nuevo.
- **Pipeline / grafo**: `data/pipelines/rfp_intake/` (grafo dedicado; no lo mezcles con el grafo CX). Los routers importan y disparan; no poseen la lógica de agentes.
- **CLIs sueltos**: `scripts/` si hace falta.
- **PDFs subidos**: vía `uis/backoffice`; se guardan bajo `data/raw/` como artefacto runtime de la recepción.

## 3. Métricas de negocio y KPIs

- **Tiempo de ciclo de propuesta**: hoy ~9 días hábiles → meta con el flujo agéntico: menos de 2 días hábiles desde que se sube la RFP hasta que el documento final está listo.
- **Tasa de clasificación correcta**: % de documentos correctamente identificados como RFP vs. descartados.
- **Iteraciones promedio por sección**: cuántas veces, en promedio, una sección vuelve del evaluador al generador antes de pasar (ideal: menos de 2).
- **Tiempo de aprobación por departamento**: desde que la sección queda lista hasta que el responsable la aprueba o rechaza.

## 4. Instrucciones de datos semilla

Usa los PDF listos en [`rfp-requests/brasaland/`](./rfp-requests/brasaland/) como **subidas de prueba a través de la UI**. El proceso de recepción guarda cada PDF subido bajo `data/raw/` (no trates los PDF del currículo como inventario pre-sembrado en el repo). Las RFP formales e informales deben **aceptarse y procesarse**; el documento inválido debe **rechazarse**.

1. **`CONTEXT-brasaland-request-1.pdf` — RFP formal (aceptar):** _Sunset Bay Resorts_, concesión co-branded en 3 resorts de Florida, exclusividad + menú de autor, ~60–75k USD/año. Activa los cuatro departamentos, incluido `training`. **Nota:** supera 50.000 USD/año → aprobación extra de la CEO (Mariana Restrepo) en la Parte 3.
2. **`CONTEXT-brasaland-request-2.pdf` — RFP informal (aceptar):** correo de _Andes Tech Solutions_ pidiendo catering semanal para 220 empleados en Medellín, contrato 12 meses, menú estándar. Activa `marketing`, `operaciones` y `procurement` (no necesariamente `training`).
3. **`CONTEXT-brasaland-request-3.pdf` — inválido (rechazar):** consulta de franquicia sin alcance, presupuesto ni fecha límite. El clasificador debe descartarlo.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- Todo precio debe expresarse en COP y en USD.
- Toda propuesta debe mencionar, al menos una vez, los tres pilares de la marca: calidad consistente, experiencia cálida, velocidad de servicio.
- Ninguna sección puede prometer tiempos de montaje/entrega menores a 10 días hábiles.
- Ninguna propuesta puede mencionar nombres de competidores.
- Toda propuesta debe incluir un período de validez de la oferta (30 días desde su emisión).
- Contratos estimados por encima de 50.000 USD/año requieren aprobación adicional del CEO antes de generarse el documento final.

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de Brasaland, extrae metadatos y reparte el análisis entre `marketing`, `operaciones`, `procurement` y `training` (solo los que apliquen).
- **Parte 2:** cada departamento activo genera su sección de la propuesta y pasa por evaluación de legibilidad, pertinencia y cumplimiento de los lineamientos de esta sección 5.
- **Parte 3:** el responsable nombrado de cada departamento activo (§2.1) aprueba de forma independiente; si el valor anual estimado supera 50.000 USD/año, **Mariana Restrepo (CEO)** también debe aprobar antes de la síntesis. No inventes jerarquía extra más allá de esa regla del CONTEXT.

## 7. Parte 3 — Triggers de conflicto y árbitro fijo

El arbitraje debe ser un nodo dedicado del grafo disparado por **contradicciones detectables en estado estructurado**, no por agentes negociando entre ellos.

| Id del trigger        | Cuándo dispara                                                                                               | Árbitro fijo (no un LLM)                                                             | Regla de resolución                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| `cost-vs-feasibility` | El estimado de costo/`procurement` no soporta el precio por evento o por cubierto implícito en `operaciones` | Camila Ospina (Marketing; dueña del ticket)                                          | Subir precio o reducir alcance; forzar `request_changes` en la(s) sección(es) desalineada(s) |
| `setup-sla-breach`    | Cualquier sección promete montaje/entrega bajo 10 días hábiles (viola §5)                                    | Felipe Guerrero (`operaciones`) rechaza; Camila escala si otros depto aún lo embeben | Forzar `request_changes` hasta ≥10 días hábiles en todas partes                              |
| `ceo-threshold`       | Valor anual estimado supera 50.000 USD y la aprobación de la CEO sigue pendiente                             | Mariana Restrepo (CEO)                                                               | Bloquear ultimate synthesizer hasta `approve` de CEO; ruta de rechazo si la CEO rechaza      |

Conecta estos ids de trigger a tu nodo de arbitraje. Los agentes pueden **señalar** un conflicto; no deben **resolverlo** por consenso libre.
