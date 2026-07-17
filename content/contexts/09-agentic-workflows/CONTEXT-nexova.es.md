# CONTEXT — Nexova: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.

## 1. Introducción

En Nexova, las RFPs llegan directo al equipo de **Marcos Ibáñez, Sales Director**: clientes potenciales (empresas de tecnología, retail o finanzas) que piden una propuesta para outsourcing de selección, soporte al cliente o capacitación corporativa. El ciclo de venta actual dura entre 3 y 8 semanas, y buena parte de ese tiempo se va en ida y vuelta por correo con Selección, Capacitación o Soporte para armar el alcance y el precio.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento:

| `department_id` | Departamento                          | Responsable      | Qué aporta a la propuesta                                                        |
| ---------------- | -------------------------------------- | ------------------ | ------------------------------------------------------------------------------------ |
| `seleccion`        | Talent Selection Operations            | Javier Almeida      | Roles a cubrir, tiempo estimado de cierre, horas de consultoría necesarias           |
| `capacitacion`      | Corporate Training                     | Elena Vargas        | Programas de formación aplicables, duración, modalidad                              |
| `soporte`           | Customer Support (outsourcing)          | Roberto Díaz        | Dotación de agentes, turnos, SLA de respuesta comprometido                          |

No toda RFP necesita a los tres departamentos: depende de qué servicio(s) pide el cliente (headhunting, training, soporte outsourced, o una combinación). Tu clasificador/orquestador debe identificar qué departamentos aplican leyendo el documento — nunca actives los tres por defecto.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF e incluyen normalmente: nombre y sede del cliente (España o Miami — esto define la moneda de la propuesta), servicio(s) solicitados, volumen (número de roles, número de agentes, número de participantes en training), fecha límite, y a veces un presupuesto de referencia.

### 2.3 Entidades sugeridas para tu estado

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analizando`, `esperando_aprobación`, `generando_borrador`, `en_evaluación`, `terminado`, `descartado`)
- **RFP metadata**: `client_name`, `client_hq` (España/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

## 3. Métricas de negocio y KPIs

- **Tiempo de armado de propuesta**: hoy consume aproximadamente 1 semana del ciclo de venta total → meta: menos de 2 días desde la carga de la RFP hasta el documento final.
- **Tasa de clasificación correcta** de RFPs vs. documentos que no lo son.
- **Iteraciones promedio por sección** en el ciclo generador-evaluador (ideal: menos de 2).
- **Tiempo de aprobación por departamento** desde que la sección está lista hasta que el responsable decide.

## 4. Instrucciones de datos semilla

Crea al menos 3 documentos de prueba en `data/raw/`:

1. **RFP válida (headhunting + training):** *Vantex Retail Group* (Madrid) solicita búsqueda ejecutiva para 5 posiciones de mandos medios más un programa trimestral de liderazgo. Fecha límite: 15 días. Activa `seleccion` y `capacitacion`. Moneda: EUR.
2. **RFP válida (soporte outsourced):** *NubeSoft* (startup SaaS con sede en Miami) solicita un equipo de soporte al cliente 24/7 de 12 agentes. Fecha límite: 20 días. Activa `soporte` (y posiblemente `seleccion` para el reclutamiento de los agentes). Moneda: USD.
3. **Documento que NO es una RFP:** un correo de un proveedor de software ofreciendo un nuevo ATS a Nexova. No tiene cliente, alcance ni fecha límite de respuesta esperada de Nexova hacia un tercero — es una oferta entrante, no una solicitud de propuesta. Tu clasificador debe descartarlo.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- Toda propuesta debe incluir la garantía de satisfacción estándar de Nexova a 90 días.
- El precio se cotiza en EUR si el cliente tiene sede en España, y en USD si tiene sede en Miami/EE. UU. — se determina a partir del campo `client_hq` en los metadatos de la RFP.
- Ninguna propuesta de búsqueda ejecutiva puede comprometer un tiempo de cierre menor a 15 días hábiles.
- Toda propuesta de soporte outsourced debe mencionar explícitamente el SLA de respuesta de 24 horas.
- Ninguna propuesta puede incluir nombres de clientes actuales como referencia sin anonimizar (usar "cliente del sector retail", no el nombre real).

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de Nexova, extrae metadatos (incluida la sede del cliente) y reparte el análisis solo entre los departamentos que el servicio solicitado realmente requiere.
- **Parte 2:** cada departamento activo genera su sección y pasa por evaluación de legibilidad, pertinencia y cumplimiento de los lineamientos de la sección 5 (incluida la moneda correcta).
- **Parte 3:** cada departamento aprueba su sección de forma independiente, sin bloquear a los demás, y el documento final se genera solo cuando todas las secciones activas están aprobadas.
