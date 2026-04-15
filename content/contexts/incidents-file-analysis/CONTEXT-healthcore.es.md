# CONTEXT — Utilidad de Análisis de Datos: Procesador de Reportes de Incidentes

## Empresa: HealthCore

---

## Tu empresa

**HealthCore** es una empresa de atención ambulatoria que opera 12 clínicas entre Estados Unidos (Texas, Florida y Georgia) y Reino Unido (Londres y Manchester). Formas parte del equipo interno **HealthCore Digital**, bajo la dirección de **James Osei (CTO)**.

Tu contacto para este proyecto es **Priya Nair (Head of Patient Experience)**. Su equipo de coordinación de pacientes registra todos los incidentes reportados por pacientes en la red: problemas de citas, disputas de facturación, preocupaciones sobre atención clínica, barreras de accesibilidad y asuntos administrativos.

Hasta ahora, los reportes se recopilan en distintos formatos según la clínica y luego se cargan manualmente en una hoja de cálculo compartida. Esa hoja se exportó a CSV y tu archivo de prueba tiene **1,000 filas** que cubren un mes de historial en las 12 sedes.

Estos datos **no pueden enviarse a ninguna herramienta de IA externa.** Contienen identificadores de pacientes protegidos por **HIPAA** (clínicas de EE. UU.) y **UK GDPR** (clínicas del Reino Unido). Cualquier script que procese este archivo debe manejar datos de pacientes con cero exposición: no debe aparecer ningún identificador ni dato personal en salidas, logs o exportaciones.

El objetivo de tu script es darle a Priya un resumen confiable y preciso de los incidentes. Si funciona correctamente con la muestra de 1,000 registros, se ejecutará sobre el histórico completo antes de integrarlo al dashboard de experiencia de pacientes.

---

## Estructura del CSV

**Nombre de archivo:** `incidents.csv`  
**Codificación:** UTF-8  
**Separador:** coma (`,`)  
**Fila de encabezado:** sí (fila 1)

| Campo                | Tipo    | Requerido | Valores permitidos / formato                             |
| -------------------- | ------- | --------- | -------------------------------------------------------- |
| `incident_id`        | string  | ✅        | ID único, formato `HC-XXXXXX` (ej.: `HC-000001`)         |
| `date`               | string  | ✅        | `YYYY-MM-DD`                                             |
| `clinic_id`          | string  | ✅        | Uno de los 12 códigos de clínica válidos (ver abajo)     |
| `country`            | string  | ✅        | `US` o `UK` — debe coincidir con el país de la clínica   |
| `category`           | string  | ✅        | Ver categorías abajo                                     |
| `description`        | string  | ✅        | Texto libre, mínimo 5 caracteres                         |
| `status`             | string  | ✅        | `OPEN`, `CLOSED`, `DISCARDED`                            |
| `patient_id`         | string  | ✅        | Formato `PAT-XXXXXX` — **protegido por HIPAA / UK GDPR** |
| `satisfaction_score` | integer | ❌\*      | Entero 1–5. **Requerido si** `status = CLOSED`           |

\*`satisfaction_score` es opcional en la estructura, pero un registro `CLOSED` sin este valor se considera **incompleto**.

> ⚠️ El campo `patient_id` es información de salud protegida (PHI) bajo HIPAA en EE. UU. y dato personal bajo UK GDPR en Reino Unido. **Tu script nunca debe imprimir, registrar ni exportar ningún valor de `patient_id`** — ni siquiera en mensajes de error. Si un registro tiene `patient_id` inválido, reporta solo la regla (por ejemplo: "Missing patient_id: 7 records"), nunca el valor.

### Códigos de clínica válidos

| Código      | País | Ubicación              |
| ----------- | ---- | ---------------------- |
| `US-TX-01`  | US   | Austin, TX — Main      |
| `US-TX-02`  | US   | Austin, TX — North     |
| `US-TX-03`  | US   | Houston, TX            |
| `US-FL-01`  | US   | Miami, FL              |
| `US-FL-02`  | US   | Orlando, FL            |
| `US-FL-03`  | US   | Tampa, FL              |
| `US-GA-01`  | US   | Atlanta, GA — Midtown  |
| `US-GA-02`  | US   | Atlanta, GA — Buckhead |
| `US-GA-03`  | US   | Savannah, GA           |
| `UK-LON-01` | UK   | London — Canary Wharf  |
| `UK-LON-02` | UK   | London — Kensington    |
| `UK-MAN-01` | UK   | Manchester             |

Un registro es **inválido** si el campo `country` no coincide con el país del `clinic_id` declarado.

### Categorías válidas

| Código           | Descripción                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `APPOINTMENT`    | Problema de agenda, espera excesiva, cancelación o manejo de no-show           |
| `BILLING`        | Disputa de facturación, confusión con seguros o cargo inesperado               |
| `CLINICAL_CARE`  | Preocupación del paciente sobre calidad asistencial, diagnóstico o tratamiento |
| `ACCESSIBILITY`  | Barrera de idioma, acceso físico o dificultad de comunicación                  |
| `ADMINISTRATIVE` | Solicitud de historial, retraso en derivación o error documental               |

---

## Reglas de registros inválidos

Un registro debe marcarse como **inválido** si ocurre cualquiera de estos casos:

| Regla                                        | Descripción                                                 |
| -------------------------------------------- | ----------------------------------------------------------- |
| `clinic_id` faltante o inválido              | Vacío o fuera de los 12 códigos válidos                     |
| Incompatibilidad país/clínica                | `country` no coincide con el país del `clinic_id` declarado |
| `category` faltante o inválida               | Vacía o fuera de las 5 categorías válidas                   |
| `description` vacía                          | Vacía o con menos de 5 caracteres                           |
| Falta `patient_id`                           | Vacío o no cumple formato `PAT-XXXXXX`                      |
| `status = CLOSED` y sin `satisfaction_score` | Incidente cerrado sin puntaje                               |
| `satisfaction_score` fuera de rango          | Hay valor, pero no está entre 1 y 5 (inclusive)             |

Tu script debe reportar cuántos registros caen en cada tipo de regla, **sin exponer datos de pacientes**.

---

## Distribución de datos (archivo de prueba provisto)

El archivo `incidents-healthcore.csv` se envió como adjunto (ver ficheros `incidents-healthcore.csv`). Los siguientes valores describen su contenido y son los que tu script debe producir exactamente.

**Total de filas:** 100

**Registros válidos: 94**
| Categoría | Cantidad |
|---|---|
| `APPOINTMENT` | 30 |
| `BILLING` | 20 |
| `CLINICAL_CARE` | 14 |
| `ACCESSIBILITY` | 17 |
| `ADMINISTRATIVE` | 13 |

| Estado      | Cantidad |
| ----------- | -------- |
| `OPEN`      | 28       |
| `CLOSED`    | 52       |
| `DISCARDED` | 14       |

| País | Cantidad |
| ---- | -------- |
| `US` | 61       |
| `UK` | 33       |

**Registros inválidos: 6**
| Regla activada | Cantidad |
|---|---|
| `clinic_id` faltante o inválido | 1 |
| Incompatibilidad país/clínica | 1 |
| `category` faltante o inválida | 1 |
| `description` vacía o demasiado corta | 1 |
| Falta `patient_id` | 1 |
| `status = CLOSED` sin `satisfaction_score` | 1 |

**Puntajes de satisfacción (52 registros cerrados)**
| Puntaje | Cantidad |
|---|---|
| 1 | 3 |
| 2 | 5 |
| 3 | 12 |
| 4 | 23 |
| 5 | 9 |
Promedio: **3.58**

---

## Salida esperada

Cuando el estudiante ejecute `python analyze.py incidents-healthcore.csv` con el archivo provisto, la salida en consola debe mostrar los siguientes valores:

```
============================================================
  HEALTHCORE — PATIENT INCIDENT REPORT ANALYSIS
  Source file: incidents-healthcore.csv
============================================================

TOTAL RECORDS IN FILE .......... 100
  ├─ Valid records ................ 94
  └─ Invalid / incomplete .......... 6

INVALID RECORDS BREAKDOWN
  ├─ Invalid or missing clinic_id .. 1
  ├─ Country/clinic mismatch ....... 1
  ├─ Invalid or missing category ... 1
  ├─ Empty description ............. 1
  ├─ Missing patient_id ............ 1
  └─ Closed case, no score ......... 1

BREAKDOWN BY CATEGORY (valid records)
  ├─ APPOINTMENT .................. 30  (31.9%)
  ├─ BILLING ...................... 20  (21.3%)
  ├─ CLINICAL_CARE ................ 14  (14.9%)
  ├─ ACCESSIBILITY ................ 17  (18.1%)
  └─ ADMINISTRATIVE ............... 13  (13.8%)

BREAKDOWN BY STATUS (valid records)
  ├─ OPEN ......................... 28  (29.8%)
  ├─ CLOSED ....................... 52  (55.3%)
  └─ DISCARDED .................... 14  (14.9%)

BREAKDOWN BY COUNTRY (valid records)
  ├─ US ........................... 61  (64.9%)
  └─ UK ........................... 33  (35.1%)

SATISFACTION INDEX (closed cases)
  Scored cases: 52 of 52
  Average score: 3.58 / 5.00
  ├─ Score 1 (Very dissatisfied) ... 3
  ├─ Score 2 (Dissatisfied) ........ 5
  ├─ Score 3 (Neutral) ............ 12
  ├─ Score 4 (Satisfied) .......... 23
  └─ Score 5 (Very satisfied) ...... 9

============================================================
Export results to CSV? [y / n]:
```

> **Nota:** Se aceptan diferencias menores de formato (espaciado, caracteres de caja), pero todos los valores numéricos deben coincidir exactamente. El desglose por país es específico de HealthCore; inclúyelo aunque no sea obligatorio en el README genérico.

---

## Nota de stakeholders

> **De Priya Nair (Head of Patient Experience):**
> _"La categoría ACCESSIBILITY es especialmente importante para mí. Si esos números son altos en las clínicas de Florida, necesito escalarlo con Sandra hoy, no la semana que viene. Asegúrense de que el desglose por país sea visible en la consola. Y quiero dejarlo explícito: ningún identificador de paciente puede aparecer en ninguna salida. James ya lo revisó con Claire: es un requisito de cumplimiento, no una preferencia. Si el script imprime un_ `patient_id` _por cualquier motivo, la salida no se puede usar."_

> **De James Osei (CTO):**
> _"La exportación CSV debe ser consistente y simple: una fila por métrica, con columnas_ `metric`, `value` _y opcionalmente_ `percentage`_. El equipo de facturación de Tom la usará directamente en su hoja de reporte. Añadan una sección_ `by_country` _en la salida de consola específica para HealthCore."_

---

## Ruta en el repositorio

```
incidents-analysis/CONTEXT-healthcore.md
```

---

_Documento interno — 4Geeks Academy · AI Engineering Track_  
_Para uso exclusivo en la generación de proyectos del programa_
