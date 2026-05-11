# CONTEXT — Gestor de Incidencias Centralizado · Nexova

## Tu empresa

**Nexova** es una consultora de recursos humanos y adquisición de talento con **120 empleados**, con sede en Valencia (España) y oficina en Miami (EE.UU.). Opera en tres líneas de negocio: headhunting, externalización de equipos de soporte al cliente para empresas tecnológicas, y formación corporativa.

Como parte del equipo de **AI Engineering de Nexova**, llevas hitos construyendo la plataforma interna. Este proyecto integra en esa plataforma un gestor centralizado de incidencias. En Nexova, las incidencias no son solo fallos de infraestructura: también incluyen quejas de clientes corporativos, errores en procesos de selección y problemas del equipo de soporte externalizado.

---

## Quién lo usa y por qué

**Sergio Molina (CTO)** necesita visibilidad centralizada de todos los problemas técnicos y operativos que hoy llegan por email, Slack o de viva voz. Sin un registro estructurado, no puede medir ni mejorar los tiempos de resolución.

**Roberto Díaz (Customer Support Lead)** gestiona 30 agentes que atienden incidencias de los clientes de Nexova. Hoy trabajan con un helpdesk legacy y sin base de conocimiento centralizada. Este gestor será el primer paso hacia un sistema estructurado.

**Laura Mendoza (CEO)** quiere saber cuántas incidencias críticas hay abiertas en este momento, desde qué oficina vienen y cuánto tiempo llevan sin resolver.

---

## Oficinas de Nexova

El campo `branch` debe contener exactamente uno de estos valores:

| Valor en base de datos  | Nombre para mostrar             |
| ----------------------- | ------------------------------- |
| `central`               | Central (Valencia / Miami)      |
| `valencia_headquarters` | Valencia — Sede Central         |
| `valencia_operations`   | Valencia — Operaciones          |
| `miami_office`          | Miami Office                    |
| `remote`                | Remoto (empleado sin sede fija) |

Cuando el origen sea `internal` o `customer` y no corresponda a una oficina específica, se usará `central`.

---

## Categorías de incidencias

El campo `category` debe contener exactamente uno de estos valores:

| Valor               | Descripción                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| `technical_failure` | Fallo de sistema o herramienta tecnológica (ATS, HubSpot, Zendesk, infraestructura) |
| `process_error`     | Error en un proceso operativo: selección, incorporación, formación, facturación     |
| `client_complaint`  | Queja o reclamación de un cliente corporativo sobre el servicio prestado            |
| `candidate_issue`   | Problema reportado por o relacionado con un candidato en proceso de selección       |
| `staff_issue`       | Incidencia interna de RRHH: ausencia, conflicto, accidente, baja                    |
| `sla_breach`        | Incumplimiento de SLA comprometido con un cliente                                   |
| `data_quality`      | Error o inconsistencia en datos de candidatos, clientes o reportes                  |
| `other`             | Cualquier incidencia que no encaje en las categorías anteriores                     |

---

## Estados y ciclo de vida

| Valor         | Significado en Nexova                                           |
| ------------- | --------------------------------------------------------------- |
| `open`        | Incidencia registrada, sin responsable asignado aún             |
| `in_progress` | Asignada a un equipo o persona, en gestión activa               |
| `resolved`    | Resuelta y confirmada por quien la reportó o por el responsable |
| `discarded`   | Registrada por error, duplicada o fuera de alcance              |

Transiciones válidas: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. Los estados `resolved` y `discarded` son finales.

---

## Orígenes

| Valor      | Cuándo usarlo en Nexova                                                         |
| ---------- | ------------------------------------------------------------------------------- |
| `customer` | Reportada por un cliente corporativo (empresa que contrata servicios de Nexova) |
| `branch`   | Reportada por personal de una de las oficinas de Nexova                         |
| `internal` | Detectada internamente por tecnología, operaciones o dirección                  |

---

## Datos históricos — seed desde CSV

El fichero CSV del proyecto anterior contiene incidencias exportadas del helpdesk de soporte al cliente. Todas corresponden a quejas o problemas reportados por clientes corporativos (`origin: "customer"`).

**Campo identificador para idempotencia:** usa el campo `incident_id` del CSV para evitar duplicados. Si ese campo no existe en tu CSV, usa la combinación `title + created_at`.

**Mapeo de campos CSV → modelo:**

| Campo CSV     | Campo del modelo | Notas                                                  |
| ------------- | ---------------- | ------------------------------------------------------ |
| `incident_id` | —                | Solo para control de duplicados, no se almacena        |
| `title`       | `title`          |                                                        |
| `description` | `description`    |                                                        |
| `category`    | `category`       | Verificar que el valor esté en la lista permitida      |
| `status`      | `status`         | Verificar que el valor esté en la lista permitida      |
| `created_at`  | `created_at`     | Respetar la fecha original                             |
| —             | `origin`         | Siempre `"customer"` para todos los registros del seed |
| —             | `branch`         | Siempre `"central"` para todos los registros del seed  |

Los registros con `category` o `status` fuera de los valores permitidos se descartan y se reportan en consola.

---

## Valores esperados tras el seed

Una vez cargado el CSV correctamente, el endpoint `/api/incidents/summary` debe devolver valores coherentes con los del fichero CSV validado en el proyecto anterior. Contrasta los totales por categoría y por estado con los resultados obtenidos en el script de análisis — deben coincidir (descontando los registros inválidos descartados por el seed).

---

## Notas de implementación

- Nexova opera en dos idiomas: los empleados de Valencia trabajan en español y los de Miami en inglés. Si has implementado soporte bilingüe en hitos anteriores, el formulario y los mensajes de error deben respetarlo.
- Las incidencias de tipo `sla_breach` son críticas para Roberto y para Laura: aunque la alerta automática no es parte de este proyecto, diseña el modelo pensando en que ese filtro debe ser trivial de añadir.
- El campo `remote` en `branch` es frecuente en Nexova: muchos empleados trabajan sin sede fija. Asegúrate de que aparece visible en el desplegable y que no genera ambigüedad con `central`.
