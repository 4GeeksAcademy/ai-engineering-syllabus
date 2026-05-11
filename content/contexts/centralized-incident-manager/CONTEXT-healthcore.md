# CONTEXT — Gestor de Incidencias Centralizado · HealthCore

## Tu empresa

**HealthCore** es una empresa de servicios sanitarios ambulatorios con **12 clínicas** — 9 en EE.UU. (Texas, Florida y Georgia) y 3 en el Reino Unido (Londres y Mánchester). Emplea a unas 200 personas entre personal clínico, operaciones, administración y tecnología. Genera unos 28 millones de dólares de ingresos anuales.

Como parte del equipo de **HealthCore Digital**, llevas hitos construyendo la plataforma interna. Este proyecto integra en esa plataforma un gestor centralizado de incidencias. En HealthCore, una incidencia no es un concepto menor: puede afectar a la seguridad de un paciente, a la conformidad regulatoria (HIPAA en EE.UU., UK GDPR en el Reino Unido) o al ciclo de facturación. El registro estructurado de incidencias es también un requisito de auditoría.

> ⚠️ **Nota regulatoria:** Este gestor **no debe almacenar datos identificativos de pacientes** (nombre, fecha de nacimiento, número de historia clínica, datos de contacto). Si una incidencia implica a un paciente, se referenciará únicamente por un identificador interno opaco. Cualquier campo libre de texto debe incluir una advertencia visible al usuario sobre no introducir datos personales de pacientes.

---

## Quién lo usa y por qué

**James Osei (CTO)** necesita un registro trazable de fallos tecnológicos. Hoy no existe un sistema que registre qué falló, cuándo, en qué clínica y cuánto tardó en resolverse.

**Claire Whitfield (Chief Compliance Officer)** necesita poder auditar incidencias relacionadas con acceso a datos de pacientes o brechas de procedimiento. El sistema debe ser consultable por tipo y fecha para responder a auditorías regulatorias.

**Dr. Marcus Reid (Director de Operaciones Clínicas)** quiere saber si alguna clínica está acumulando incidencias de tipo clínico o de equipamiento que puedan afectar la atención a pacientes.

**Dr. Sandra Okonkwo (CEO)** quiere visibilidad ejecutiva: cuántas incidencias críticas hay abiertas en la red, con desglose por país.

---

## Clínicas de HealthCore

El campo `branch` debe contener exactamente uno de estos valores:

| Valor en base de datos | Nombre para mostrar       |
| ---------------------- | ------------------------- |
| `central`              | Central (Austin / London) |
| `austin_main`          | Austin — Main Clinic      |
| `austin_north`         | Austin — North            |
| `dallas_uptown`        | Dallas Uptown             |
| `houston_med_center`   | Houston Medical Center    |
| `san_antonio_west`     | San Antonio West          |
| `miami_brickell`       | Miami Brickell            |
| `miami_doral`          | Miami Doral               |
| `orlando_east`         | Orlando East              |
| `atlanta_midtown`      | Atlanta Midtown           |
| `london_city`          | London City               |
| `london_west`          | London West End           |
| `manchester_central`   | Manchester Central        |

Cuando el origen sea `internal` o `customer` y no corresponda a una clínica específica, se usará `central`.

---

## Categorías de incidencias

El campo `category` debe contener exactamente uno de estos valores:

| Valor                | Descripción                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| `clinical_equipment` | Fallo o problema con equipamiento clínico (sin datos de pacientes)                                     |
| `it_system`          | Fallo de sistema tecnológico: EHR, portal de pacientes, facturación, integraciones                     |
| `billing_error`      | Error en el proceso de facturación o codificación de reclamaciones                                     |
| `compliance_breach`  | Posible incumplimiento regulatorio (HIPAA / UK GDPR) — sin datos identificativos de pacientes          |
| `patient_experience` | Problema de experiencia del paciente: cita, comunicación, tiempo de espera (sin datos identificativos) |
| `staff_issue`        | Incidencia de personal: ausencia, conflicto, formación obligatoria pendiente                           |
| `facility_issue`     | Problema de instalaciones: agua, electricidad, climatización, limpieza                                 |
| `referral_issue`     | Problema en el proceso de derivación entre clínicas                                                    |
| `other`              | Cualquier incidencia que no encaje en las categorías anteriores                                        |

---

## Estados y ciclo de vida

| Valor         | Significado en HealthCore                                  |
| ------------- | ---------------------------------------------------------- |
| `open`        | Incidencia registrada, pendiente de asignar al responsable |
| `in_progress` | Responsable identificado y gestión en curso                |
| `resolved`    | Incidencia cerrada con acción correctiva documentada       |
| `discarded`   | Registrada por error, duplicada o fuera de alcance         |

Transiciones válidas: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. Los estados `resolved` y `discarded` son finales.

---

## Orígenes

| Valor      | Cuándo usarlo en HealthCore                                               |
| ---------- | ------------------------------------------------------------------------- |
| `customer` | Reportada por un paciente o su representante (sin datos identificativos)  |
| `branch`   | Reportada por personal clínico o administrativo de una clínica específica |
| `internal` | Detectada por tecnología, cumplimiento normativo o dirección corporativa  |

---

## Datos históricos — seed desde CSV

El fichero CSV del proyecto anterior contiene incidencias exportadas del sistema legacy de atención al paciente de HealthCore. Todas corresponden a incidencias comunicadas por pacientes o sus representantes (`origin: "customer"`). El CSV no contiene datos identificativos de pacientes — fue anonimizado antes de la extracción.

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

- **Advertencia de datos de pacientes:** el formulario debe mostrar un aviso visible antes del campo `description` recordando al usuario que no introduzca datos identificativos de pacientes. Este aviso no es opcional — es un requisito de cumplimiento normativo.
- Las incidencias de tipo `compliance_breach` son de máxima prioridad para Claire: aunque la alerta automática no es parte de este proyecto, diseña el modelo pensando en que ese filtro debe ser inmediato de implementar.
- HealthCore opera en EE.UU. y el Reino Unido. Las etiquetas de la interfaz deben estar en inglés para todas las clínicas. Si has implementado soporte multilingüe en hitos anteriores, el inglés es el idioma base obligatorio para este proyecto.
- El campo `description` es de texto libre y es donde más riesgo hay de que un usuario introduzca datos de pacientes accidentalmente. El aviso debe ser prominente, no un texto gris pequeño.
