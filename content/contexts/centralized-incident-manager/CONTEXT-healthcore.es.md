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

| Valor en base de datos | Nombre para mostrar          |
| ---------------------- | ---------------------------- |
| `central`              | Central — Austin Main Clinic |
| `austin_north`         | Austin — North               |
| `dallas_uptown`        | Dallas Uptown                |
| `houston_med_center`   | Houston Medical Center       |
| `san_antonio_west`     | San Antonio West             |
| `miami_brickell`       | Miami Brickell               |
| `miami_doral`          | Miami Doral                  |
| `orlando_east`         | Orlando East                 |
| `tampa_bay`            | Tampa Bay                    |
| `atlanta_midtown`      | Atlanta Midtown              |
| `savannah`             | Savannah                     |
| `london_city`          | London City                  |
| `london_west`          | London West End              |
| `manchester_central`   | Manchester Central           |

Usa `central` cuando la incidencia no corresponda a una clínica concreta — por ejemplo, reportes `internal` de dirección corporativa o quejas `customer` que no se puedan asociar a una clínica. `central` es la sede central de HealthCore en Austin (Main Clinic); también es la sede del código de clínica `US-TX-01`.

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

El fichero CSV del proyecto **incidents-file-analyzer** (`incidents-<empresa>.csv` en `content/contexts/incidents-file-analysis/`) contiene incidencias exportadas del sistema legacy de atención al paciente de HealthCore. Todas corresponden a incidencias comunicadas por pacientes o sus representantes (`origin: "customer"`). El CSV no contiene datos identificativos de pacientes — fue anonimizado antes de la extracción.

El esquema del CSV del analizador usa nombres de campo, estados y categorías distintos a los de este gestor. **No insertes filas del CSV directamente.** Reutiliza la lógica de validación compartida del analizador y aplica las transformaciones siguientes antes del insert.

**Campo identificador para idempotencia:** usa `incident_id` del CSV. Si no existe, usa la combinación `title + created_at`.

### Mapeo directo de campos

| Campo CSV     | Campo del modelo | Transformación                                                                 |
| ------------- | ---------------- | ------------------------------------------------------------------------------ |
| `incident_id` | —                | Solo control de duplicados — no se almacena                                    |
| `description` | `title`          | Primeros 120 caracteres de `description`, recortados. Descartar si queda vacío |
| `description` | `description`    | Copiar literalmente                                                            |
| `date`        | `created_at`     | Parsear `YYYY-MM-DD` como medianoche UTC. `updated_at` igual al insertar       |
| —             | `origin`         | Siempre `"customer"` en todos los registros del seed                           |

### Mapeo de estados

| CSV `status` | Modelo `status` |
| ------------ | --------------- |
| `OPEN`       | `open`          |
| `CLOSED`     | `resolved`      |
| `DISCARDED`  | `discarded`     |

### Mapeo de categorías (HealthCore)

| CSV `category`   | Modelo `category`    |
| ---------------- | -------------------- |
| `APPOINTMENT`    | `patient_experience` |
| `BILLING`        | `billing_error`      |
| `CLINICAL_CARE`  | `patient_experience` |
| `ACCESSIBILITY`  | `patient_experience` |
| `ADMINISTRATIVE` | `other`              |

### Mapeo de sede (HealthCore)

Mapea `clinic_id` del CSV a `branch` del modelo. Si falta o no hay mapeo, usa `central`.

| CSV `clinic_id` | Modelo `branch`      |
| --------------- | -------------------- |
| `US-TX-01`      | `central`            |
| `US-TX-02`      | `austin_north`       |
| `US-TX-03`      | `houston_med_center` |
| `US-FL-01`      | `miami_brickell`     |
| `US-FL-02`      | `orlando_east`       |
| `US-FL-03`      | `tampa_bay`          |
| `US-GA-01`      | `atlanta_midtown`    |
| `US-GA-02`      | `atlanta_midtown`    |
| `US-GA-03`      | `savannah`           |
| `UK-LON-01`     | `london_city`        |
| `UK-LON-02`     | `london_west`        |
| `UK-MAN-01`     | `manchester_central` |

Los registros que fallen la validación o no se puedan mapear se descartan y se reportan en consola.

---

## Valores esperados tras el seed

Tras cargar el CSV, `/api/incidents/summary` debe devolver totales por `status` y `category` del **modelo** que coincidan con los siguientes conteos transformados. Corresponden a los **94 registros válidos** de `incidents-healthcore.csv` del proyecto analizador (excluidas filas inválidas).

**Por `status` del modelo:**

| Modelo `status` | Conteo |
| --------------- | ------ |
| `open`          | 28     |
| `resolved`      | 52     |
| `discarded`     | 14     |

**Por `category` del modelo:**

| Modelo `category`    | Conteo |
| -------------------- | ------ |
| `patient_experience` | 61     |
| `billing_error`      | 20     |
| `other`              | 13     |

**Por `branch` del modelo:**

| Modelo `branch`      | Conteo |
| -------------------- | ------ |
| `manchester_central` | 15     |
| `atlanta_midtown`    | 12     |
| `savannah`           | 10     |
| `austin_north`       | 9      |
| `london_west`        | 9      |
| `london_city`        | 9      |
| `miami_brickell`     | 8      |
| `tampa_bay`          | 7      |
| `central`            | 7      |
| `houston_med_center` | 4      |
| `orlando_east`       | 4      |

Contrasta con la salida del script analizador: el CSV crudo usa `OPEN`/`CLOSED`/`DISCARDED` y códigos como `APPOINTMENT`/`BILLING`. Los totales anteriores son los valores **post-transformación** que debe producir tu gestor.

---

## Notas de implementación

- **Advertencia de datos de pacientes:** el formulario debe mostrar un aviso visible antes del campo `description` recordando al usuario que no introduzca datos identificativos de pacientes. Este aviso no es opcional — es un requisito de cumplimiento normativo.
- Las incidencias de tipo `compliance_breach` son de máxima prioridad para Claire: aunque la alerta automática no es parte de este proyecto, diseña el modelo pensando en que ese filtro debe ser inmediato de implementar.
- HealthCore opera en EE.UU. y el Reino Unido. Las etiquetas de la interfaz deben estar en inglés para todas las clínicas. Si has implementado soporte multilingüe en hitos anteriores, el inglés es el idioma base obligatorio para este proyecto.
- El campo `description` es de texto libre y es donde más riesgo hay de que un usuario introduzca datos de pacientes accidentalmente. El aviso debe ser prominente, no un texto gris pequeño.
