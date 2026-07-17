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

| `department_id` | Departamento                     | Responsable         | Qué aporta a la propuesta                                                                 |
| ---------------- | ----------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------- |
| `revenue`           | Revenue Cycle                       | Tom Callahan            | Términos financieros, moneda, estructura de pago. Dueño del ticket.                              |
| `clinical`           | Clinical Operations                  | Dr. Marcus Reid          | Viabilidad clínica: qué clínicas y qué capacidad de personal pueden cubrir el contrato          |
| `compliance`         | Compliance and Data Governance        | Claire Whitfield         | Revisión regulatoria (HIPAA/UK GDPR), cláusulas de BAA o DPA según el país del cliente          |

`compliance` es **obligatorio en todas las RFPs, sin excepción** — no importa qué tan simple parezca el contrato, ninguna propuesta institucional puede cerrarse sin la aprobación de Compliance en la Parte 3.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF e incluyen normalmente: nombre y país del cliente institucional (EE. UU. o Reino Unido — define si aplica HIPAA o UK GDPR), tipo de programa solicitado (salud ocupacional, bienestar corporativo, red de referidos), volumen (número de empleados o estudiantes cubiertos), fecha límite, y a veces un presupuesto de referencia.

### 2.3 Entidades sugeridas para tu estado

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analizando`, `esperando_aprobación`, `generando_borrador`, `en_evaluación`, `terminado`, `descartado`)
- **RFP metadata**: `client_name`, `client_country` (US/UK), `program_type`, `covered_population`, `deadline`, `budget_range`, `departments_needed` — **nunca** un campo de datos de paciente individual
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results` (incluye una bandera `contains_phi: bool` que el evaluador de cumplimiento debe poder marcar), `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

## 3. Métricas de negocio y KPIs

- **Tiempo de armado de propuesta**: hoy ~3 semanas → meta: menos de 5 días hábiles desde la carga de la RFP hasta el documento final.
- **Tasa de clasificación correcta** de RFPs vs. documentos que no lo son.
- **Tasa de detección de PHI**: % de contenido con datos de paciente correctamente detectado y bloqueado antes de avanzar en el flujo (meta: 100%).
- **Tiempo de aprobación por departamento**, con seguimiento especial al tiempo de revisión de `compliance`.

## 4. Instrucciones de datos semilla

Crea al menos 4 documentos de prueba en `data/raw/`:

1. **RFP válida (EE. UU.):** *Meridian Manufacturing* (Austin, 800 empleados) solicita un programa de salud ocupacional y bienestar en sitio, contrato de 12 meses. Fecha límite: 20 días. Activa `revenue`, `clinical` y `compliance` (con cláusula de BAA, por ser EE. UU.). Moneda: USD.
2. **RFP válida (Reino Unido):** *Thames Valley University* solicita una alianza de red de referidos con una clínica satélite para sus estudiantes. Fecha límite: 25 días. Activa `revenue`, `clinical` y `compliance` (con cláusula de DPA y referencia a UK GDPR, por ser Reino Unido). Moneda: GBP.
3. **Documento que NO es una RFP:** un correo de un proveedor de software ofreciendo un nuevo sistema de historia clínica electrónica a HealthCore. No es una solicitud de un cliente institucional. Tu clasificador debe descartarlo.
4. **RFP con PHI indebida (caso crítico):** una "RFP" de un empleador que adjunta, como ejemplo de un caso previo con otro proveedor, un resumen de un caso clínico con nombre de paciente y diagnóstico. Tu flujo **nunca** debe dejar pasar ese contenido tal cual hacia agentes generadores, logs o la interfaz del ticket — debe detectarlo y bloquearlo (o redactarlo) antes de que avance, y marcarlo explícitamente para revisión humana de Compliance.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- **Ninguna sección generada puede contener nombres, diagnósticos o cualquier identificador de paciente, real o de ejemplo.** El evaluador de cumplimiento debe rechazar cualquier sección que los contenga, sin excepción.
- Toda propuesta para un cliente en Estados Unidos debe incluir una cláusula de Business Associate Agreement (BAA).
- Toda propuesta para un cliente en Reino Unido debe incluir una cláusula de Data Processing Agreement (DPA) referenciando UK GDPR.
- El precio se cotiza en USD para clientes de EE. UU. y en GBP para clientes del Reino Unido — se determina a partir del campo `client_country`.
- La aprobación de `compliance` es siempre obligatoria en la Parte 3, sin importar qué otros departamentos estén involucrados.

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de HealthCore, extrae metadatos sin incluir nunca datos de paciente, detecta y marca cualquier contenido con PHI, y reparte el análisis entre `revenue`, `clinical` y `compliance` (este último siempre activo).
- **Parte 2:** cada departamento genera su sección y pasa por evaluación de legibilidad, pertinencia y cumplimiento — incluyendo el chequeo de ausencia de PHI como criterio de evaluación obligatorio.
- **Parte 3:** cada departamento aprueba su sección de forma independiente sin bloquear a los demás; `compliance` debe aprobar siempre antes del cierre; el documento final se genera solo cuando todas las aprobaciones requeridas están completas y ninguna sección contiene PHI.
