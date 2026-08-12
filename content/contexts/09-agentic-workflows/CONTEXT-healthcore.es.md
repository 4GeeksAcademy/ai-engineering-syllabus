# CONTEXT — HealthCore: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.
>
> ⚠️ **Restricción no negociable:** HealthCore opera bajo HIPAA (EE. UU.) y UK GDPR (Reino Unido). Ningún identificador de paciente ni PHI (Protected Health Information) puede aparecer en ningún evento, tabla, endpoint, log, ticket o documento generado por tu flujo — ni siquiera como ejemplo ilustrativo. Esto aplica en las tres partes de este hito.

## 1. Introducción

HealthCore no tiene un departamento de "Ventas" tradicional: las RFPs institucionales (contratos de salud ocupacional con empleadores, programas de bienestar corporativo, alianzas de referidos con universidades) le llegan al equipo de **Tom Callahan, Revenue Cycle Director**, que además de facturación y cobros evalúa nuevas oportunidades de contrato B2B. En este hito, Revenue Cycle es tu "Ventas": ellos abren el ticket y esperan el resultado del flujo agéntico.

Hoy, armar una propuesta institucional toma en promedio **3 semanas**, coordinando por correo entre Revenue Cycle, Clinical Operations y, obligatoriamente, Compliance — porque cualquier contrato que involucre datos de pacientes debe pasar revisión regulatoria antes de salir.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento:

| `department_id` | Departamento                   | Responsable      | Qué aporta a la propuesta                                                              |
| --------------- | ------------------------------ | ---------------- | -------------------------------------------------------------------------------------- |
| `revenue`       | Revenue Cycle                  | Tom Callahan     | Términos financieros, moneda, estructura de pago. Dueño del ticket.                    |
| `clinical`      | Clinical Operations            | Dr. Marcus Reid  | Viabilidad clínica: qué clínicas y qué capacidad de personal pueden cubrir el contrato |
| `compliance`    | Compliance and Data Governance | Claire Whitfield | Revisión regulatoria (HIPAA/UK GDPR), cláusulas de BAA o DPA según el país del cliente |

`compliance` es **obligatorio en todas las RFPs, sin excepción** — no importa qué tan simple parezca el contrato, ninguna propuesta institucional puede cerrarse sin la aprobación de Compliance en la Parte 3.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF e incluyen normalmente: nombre y país del cliente institucional (EE. UU. o Reino Unido — define si aplica HIPAA o UK GDPR), tipo de programa solicitado (salud ocupacional, bienestar corporativo, red de referidos), volumen (número de empleados o estudiantes cubiertos), fecha límite, y a veces un presupuesto de referencia.

### 2.3 Entidades sugeridas para tu estado

Persiste **Ticket**, **metadatos RFP** y **DepartmentSection** (al menos `key_aspects` en la Parte 1; borradores/evals/aprobaciones en partes posteriores) en **PostgreSQL (Supabase)** vía tu capa SQLModel/DB existente. TinyDB o archivos JSON no son la fuente de verdad. **Nunca** guardes identificadores de paciente ni PHI en estas tablas.

- **Ticket**: `ticket_id`, `rfp_id`, `status`, `raw_pdf_path`, `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `client_country` (US/UK), `program_type`, `covered_population`, `deadline`, `budget_range`, `departments_needed`, métricas de legibilidad — **nunca** un campo de datos de paciente individual
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results` (incluye una bandera `contains_phi: bool` que el evaluador de cumplimiento debe poder marcar), `approval_status`, `approver`, `approved_at`
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

Los workers reciben **metadatos compartidos + extractos relevantes a su departamento**. Si faltan cifras de población cubierta / volumen, registra preguntas abiertas — **nunca inventes** headcount ni PHI.

### 2.4 Layout del monorepo

- **HTTP**: extiende el **backend existente** bajo `services/` — sin un proceso API nuevo.
- **Pipeline / grafo**: `data/pipelines/rfp_intake/` (grafo dedicado; no lo mezcles con el grafo CX). Los routers importan y disparan; no poseen la lógica de agentes.
- **CLIs sueltos**: `scripts/` si hace falta.
- **PDFs subidos**: vía `uis/backoffice`; se guardan bajo `data/raw/` como artefacto runtime de la recepción (sigue sin PHI en paths, logs ni columnas DB).

## 3. Métricas de negocio y KPIs

- **Tiempo de armado de propuesta**: hoy ~3 semanas → meta: menos de 5 días hábiles desde la carga de la RFP hasta el documento final.
- **Tasa de clasificación correcta** de RFPs vs. documentos que no lo son.
- **Tasa de detección de PHI**: % de contenido con datos de paciente correctamente detectado y bloqueado antes de avanzar en el flujo (meta: 100%).
- **Tiempo de aprobación por departamento**, con seguimiento especial al tiempo de revisión de `compliance`.

## 4. Instrucciones de datos semilla

Usa los PDF listos en [`rfp-requests/healthcore/`](./rfp-requests/healthcore/) como **subidas de prueba a través de la UI**. El proceso de recepción guarda cada PDF subido bajo `data/raw/` (no trates los PDF del currículo como inventario pre-sembrado en el repo). Las RFP formales e informales deben **aceptarse y procesarse**; el documento inválido debe **rechazarse**.

1. **`CONTEXT-healthcore-request-1.pdf` — RFP formal (aceptar):** _Meridian Manufacturing_ (Austin, 800 empleados), salud ocupacional y bienestar en sitio, contrato 12 meses. Activa `revenue`, `clinical` y `compliance` (BAA). Moneda: USD.
2. **`CONTEXT-healthcore-request-2.pdf` — RFP informal (aceptar):** correo de _Thames Valley University_ pidiendo alianza de red de referidos con clínica satélite. Activa `revenue`, `clinical` y `compliance` (DPA / UK GDPR). Moneda: GBP.
3. **`CONTEXT-healthcore-request-3.pdf` — inválido (rechazar):** pitch de proveedor de EHR — no es RFP de cliente. El clasificador debe descartarlo.
4. **RFP con PHI indebida (caso crítico — créalo tú):** una "RFP" que adjunta resumen clínico con nombre de paciente y diagnóstico. El flujo **nunca** debe pasar ese contenido tal cual a generadores, logs o UI del ticket — detectar, bloquear/redactar y marcar para revisión humana de Compliance.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- **Ninguna sección generada puede contener nombres, diagnósticos o cualquier identificador de paciente, real o de ejemplo.** El evaluador de cumplimiento debe rechazar cualquier sección que los contenga, sin excepción.
- Toda propuesta para un cliente en Estados Unidos debe incluir una cláusula de Business Associate Agreement (BAA).
- Toda propuesta para un cliente en Reino Unido debe incluir una cláusula de Data Processing Agreement (DPA) referenciando UK GDPR.
- El precio se cotiza en USD para clientes de EE. UU. y en GBP para clientes del Reino Unido — se determina a partir del campo `client_country`.
- La aprobación de `compliance` es siempre obligatoria en la Parte 3, sin importar qué otros departamentos estén involucrados.

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de HealthCore, extrae metadatos sin incluir nunca datos de paciente, detecta y marca cualquier contenido con PHI, y reparte el análisis entre `revenue`, `clinical` y `compliance` (este último siempre activo).
- **Parte 2:** cada departamento genera su sección y pasa por evaluación de legibilidad, pertinencia y cumplimiento — incluyendo el chequeo de ausencia de PHI como criterio de evaluación obligatorio.
- **Parte 3:** el responsable nombrado de cada departamento (§2.1) aprueba de forma independiente sin bloquear a los demás; `compliance` debe aprobar siempre antes del cierre. **No** inventes jerarquía extra más allá de Compliance obligatorio. El documento final solo cuando todas las aprobaciones requeridas están completas y ninguna sección contiene PHI.

## 7. Parte 3 — Triggers de conflicto y árbitro fijo

El arbitraje debe ser un nodo dedicado del grafo disparado por **contradicciones detectables en estado estructurado**, no por agentes negociando entre ellos.

| Id del trigger           | Cuándo dispara                                                                                 | Árbitro fijo (no un LLM)                                                          | Regla de resolución                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `phi-detected`           | Cualquier sección o artefacto tiene `contains_phi: true` o incluye identificadores de paciente | Claire Whitfield (`compliance`)                                                   | Parada dura: redactar/bloquear, `request_changes` o descarte; el synthesizer no debe correr                              |
| `baa-dpa-mismatch`       | Cliente US sin cláusula BAA, o UK sin DPA/UK GDPR, o instrumento incorrecto para el país       | Claire Whitfield                                                                  | Forzar `request_changes` en `compliance` (y secciones que embeban la cláusula incorrecta) hasta que sea correcto al país |
| `capacity-vs-population` | La capacidad clínica/staff de `clinical` no cubre la población/`revenue` del contrato          | Tom Callahan (Revenue; dueño del ticket) tras confirmar Compliance que no hay PHI | Reducir población cubierta o añadir sedes; forzar revisión en `revenue` y/o `clinical`                                   |

Conecta estos ids de trigger a tu nodo de arbitraje. Los agentes pueden **señalar** un conflicto; no deben **resolverlo** por consenso libre. Compliance siempre gana en triggers de PHI / regulatorios.
