# CONTEXT — Brasaland: Hito 9, Flujos de Trabajo Agénticos (Partes 1, 2 y 3)

> Este documento es válido para las tres partes del Hito 9. Léelo completo antes de empezar la Parte 1 — las Partes 2 y 3 reutilizan los mismos departamentos, formato de RFP y lineamientos definidos aquí.

## 1. Introducción

Brasaland no tiene un departamento de "Ventas" tradicional: las RFPs corporativas (contratos de catering institucional, alianzas de co-marca, concesiones en eventos o resorts) le llegan al equipo de **Camila Ospina, Marketing, Brand and Digital Experience**, que además de campañas y CRM se encarga de recibir y coordinar este tipo de oportunidades B2B. En este hito, el equipo de Marketing es tu "Ventas": ellos abren el ticket y esperan el resultado del flujo agéntico.

Hoy, cuando llega una de estas solicitudes, Camila reenvía el PDF por WhatsApp a Felipe (Operaciones), Lucía (Procurement) y Jake (Training) y espera respuestas sueltas por correo. Armar una propuesta completa toma en promedio **9 días hábiles**, y varias veces se ha perdido una oportunidad porque un departamento no respondió a tiempo. Tu flujo agéntico reemplaza esa coordinación manual.

## 2. Departamentos y estructuras de datos

### 2.1 Departamentos que participan en la propuesta

Usa exactamente estos identificadores de departamento en tu código y en el estado del grafo:

| `department_id` | Departamento              | Responsable      | Qué aporta a la propuesta                                                                 |
| ---------------- | -------------------------- | ----------------- | -------------------------------------------------------------------------------------------- |
| `marketing`       | Marketing y Experiencia Digital | Camila Ospina      | Términos de marca, exclusividad, co-branding, validez de la oferta. Dueña del ticket.        |
| `operaciones`      | Operaciones de Restaurante | Felipe Guerrero    | Viabilidad operativa: capacidad de cocina/personal, tiempos de montaje, costo operativo/evento |
| `procurement`      | Procurement y Proveedores  | Lucía Fernández    | Costo estimado de insumos según volumen, tiempos de entrega de proveedores                    |
| `training`         | Training y Estándares de Calidad | Jake Morrison | Si el pedido requiere receta o estándar nuevo, tiempo de desarrollo y certificación necesario |

No toda RFP necesita a los cuatro departamentos: una solicitud de catering simple puede no requerir `training` (por ejemplo, si usa el menú estándar). Tu agente clasificador/orquestador debe decidir qué departamentos aplican según el contenido del documento — no asumas que siempre son los cuatro.

### 2.2 Formato de una RFP real

Las RFPs llegan como PDF y normalmente incluyen: nombre del cliente y ubicación, tipo de servicio solicitado (catering recurrente, concesión, co-branding), volumen o alcance (número de comensales, ubicaciones, duración del contrato), fecha límite para responder, y a veces un rango de presupuesto. No siempre están bien estructuradas — algunas son cartas de intención informales.

### 2.3 Entidades sugeridas para tu estado

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analizando`, `esperando_aprobación`, `generando_borrador`, `en_evaluación`, `terminado`, `descartado`), `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (opcional), `departments_needed`
- **DepartmentSection**: `department_id`, `key_aspects` (Parte 1), `draft_content` (Parte 2), `evaluation_results` (legibilidad, pertinencia, cumplimiento), `approval_status` (`pendiente`, `aprobado`, `rechazado`), `approver`, `approved_at`
- **FinalDocument**: `ticket_id`, `sections`, `total_estimated_value`, `generated_at`

## 3. Métricas de negocio y KPIs

- **Tiempo de ciclo de propuesta**: hoy ~9 días hábiles → meta con el flujo agéntico: menos de 2 días hábiles desde que se sube la RFP hasta que el documento final está listo.
- **Tasa de clasificación correcta**: % de documentos correctamente identificados como RFP vs. descartados.
- **Iteraciones promedio por sección**: cuántas veces, en promedio, una sección vuelve del evaluador al generador antes de pasar (ideal: menos de 2).
- **Tiempo de aprobación por departamento**: desde que la sección queda lista hasta que el responsable la aprueba o rechaza.

## 4. Instrucciones de datos semilla

Crea al menos 3 documentos de prueba en `data/raw/`:

1. **RFP válida (rutina):** *Andes Tech Solutions*, empresa tecnológica de Bogotá, solicita catering semanal para 220 empleados en su oficina de Medellín, contrato de 12 meses, fecha límite en 15 días. Debe activar `marketing`, `operaciones` y `procurement` (no necesariamente `training`, ya que usa el menú estándar).
2. **RFP válida (compleja, alto valor):** *Sunset Bay Resorts*, cadena hotelera de Florida, solicita un concesión de marca compartida en 3 de sus resorts, con cláusula de exclusividad y un nuevo menú de autor. Contrato estimado sobre 60.000 USD/año, fecha límite en 30 días. Debe activar los cuatro departamentos, incluido `training` por el menú nuevo. **Nota:** por superar los 50.000 USD/año, esta propuesta requiere una aprobación adicional de Mariana Restrepo (CEO) antes del cierre — impleméntalo como un paso de aprobación extra en tu Parte 3.
3. **Documento que NO es una RFP:** un correo de un cliente preguntando de forma informal sobre oportunidades de franquicia, sin alcance, presupuesto ni fecha límite. Tu agente clasificador debe descartarlo.

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
- **Parte 3:** cada departamento (y, si aplica, la CEO por el umbral de 50.000 USD/año) aprueba su sección de forma independiente, sin bloquear a los demás, y el documento final se genera solo cuando todas las aprobaciones requeridas están completas.
