# CONTEXT — TrackFlow: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.

## 1. Introducción

En TrackFlow, las RFPs llegan al equipo de **Miguel Torres, Commercial Director**: marcas de e-commerce (moda, electrónica, cosmética) que quieren tercerizar su logística — almacenamiento, última milla, devoluciones, o una combinación — en Estados Unidos, España, o ambos. Hoy, cada account manager arma la propuesta a mano, coordinando por correo con Warehouse, Last Mile y Reverse Logistics; el proceso es lento y a veces una propuesta llega después de que el prospecto ya firmó con otro proveedor.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento:

| `department_id` | Departamento                | Responsable      | Qué aporta a la propuesta                                                  |
| ---------------- | ----------------------------- | ------------------ | -------------------------------------------------------------------------------- |
| `warehouse`         | Warehouse Operations           | Ana Whitfield        | Capacidad de almacenamiento, costo por pallet/SKU, tiempo de onboarding          |
| `lastmile`          | Last Mile and Carrier Management | Carlos Vega        | Costo por envío, transportistas disponibles según destino, SLA de entrega        |
| `reverse`           | Reverse Logistics              | Sofía Ramos          | Costo y tiempo de procesamiento de devoluciones (si el cliente lo solicita)       |

No toda RFP necesita a los tres departamentos: un cliente puede pedir solo almacenamiento y devoluciones, sin última milla (porque usa su propio transportista), por ejemplo. Tu clasificador/orquestador debe decidir qué departamentos aplican según el alcance solicitado.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF e incluyen normalmente: nombre y país de origen del cliente (EE. UU. o España — define la moneda), servicios solicitados (warehousing, last mile, reverse logistics), volumen estimado (pedidos/mes), fecha límite, y a veces un presupuesto de referencia.

### 2.3 Entidades sugeridas para tu estado

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analizando`, `esperando_aprobación`, `generando_borrador`, `en_evaluación`, `terminado`, `descartado`)
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects`, `draft_content`, `evaluation_results`, `approval_status`, `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `currency`, `generated_at`

## 3. Métricas de negocio y KPIs

- **Tiempo de armado de propuesta**: hoy varios días de coordinación manual → meta: menos de 2 días desde la carga de la RFP hasta el documento final.
- **Tasa de clasificación correcta** de RFPs vs. documentos que no lo son.
- **Iteraciones promedio por sección** en el ciclo generador-evaluador (ideal: menos de 2).
- **Tiempo de aprobación por departamento** desde que la sección está lista hasta la decisión del responsable.

## 4. Instrucciones de datos semilla

Crea al menos 3 documentos de prueba en `data/raw/`:

1. **RFP válida (completa):** *Luna Cosmetics*, marca DTC de Los Ángeles, solicita almacenamiento y última milla para el mercado de EE. UU., ~5.000 pedidos/mes. Fecha límite: 20 días. Activa `warehouse` y `lastmile`. Moneda: USD.
2. **RFP válida (parcial):** *Zaragoza ModaViva*, marca de moda española, solicita solo almacenamiento y gestión de devoluciones (usa su propio transportista para última milla). Fecha límite: 25 días. Activa `warehouse` y `reverse`, no `lastmile`. Moneda: EUR.
3. **Documento que NO es una RFP:** un correo de una empresa de transporte ofreciéndole a TrackFlow nuevas tarifas de envío. Es una oferta entrante de un proveedor, no una solicitud de un cliente. Tu clasificador debe descartarlo.

## 5. Restricciones de negocio (lineamientos para el evaluador de cumplimiento)

- El precio se cotiza en USD para operación en Estados Unidos y en EUR para operación en España — se determina a partir del campo `client_country`.
- Toda propuesta debe indicar el SLA de entrega a tiempo (%) que TrackFlow se compromete a cumplir.
- Ninguna propuesta puede prometer procesamiento de devoluciones en menos de 48 horas.
- Toda propuesta debe incluir una tabla de descuentos por volumen.
- Ninguna propuesta puede revelar tarifas negociadas con transportistas específicos — solo el costo final ofrecido al cliente.

## 6. Entregables esperados

- **Parte 1:** el ticket identifica correctamente si un documento es una RFP de TrackFlow, extrae metadatos (incluido el país del cliente) y reparte el análisis solo entre los departamentos que el alcance solicitado realmente requiere.
- **Parte 2:** cada departamento activo genera su sección y pasa por evaluación de legibilidad, pertinencia y cumplimiento de los lineamientos de la sección 5 (incluida la moneda correcta y el SLA).
- **Parte 3:** cada departamento aprueba su sección de forma independiente, sin bloquear a los demás, y el documento final se genera solo cuando todas las secciones activas están aprobadas.
