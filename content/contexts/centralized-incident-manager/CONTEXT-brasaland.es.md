# CONTEXT — Gestor de Incidencias Centralizado · Brasaland

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa con **14 locales** operando en Colombia y Florida (EE.UU.). Empleas a unas 115 personas entre personal de cocina y sala, supervisores de operaciones y el equipo corporativo de Medellín, con oficina comercial en Miami.

Como parte del equipo de **Brasaland Digital**, llevas hitos construyendo la plataforma interna de la empresa. Este proyecto integra en esa plataforma un gestor centralizado de incidencias, para que cualquier sede pueda reportar problemas operativos, de cliente o internos — y el equipo de operaciones pueda hacer seguimiento desde un único panel.

---

## Quién lo usa y por qué

**Felipe Guerrero (Director de Operaciones)** necesita saber qué está pasando en cada local sin tener que llamar a cada gerente. Hoy recibe reportes por WhatsApp o al final de la semana. Con este gestor, cualquier incidencia queda registrada al momento, categorizada y asignada a una sede.

**Mariana Restrepo (CEO)** quiere ver en el panel ejecutivo cuántas incidencias hay abiertas esta semana, de qué tipo y en qué locales. Hasta ahora eso no existe.

El formulario lo usarán **gerentes de local** (desde tablet en cocina o sala) y el **equipo de central** (desde escritorio en Medellín o Miami).

---

## Sedes de Brasaland

El campo `branch` debe contener exactamente uno de estos valores:

| Valor en base de datos  | Nombre para mostrar         |
| ----------------------- | --------------------------- |
| `central`               | Central (Medellín / Miami)  |
| `medellin_centro`       | Medellín Centro             |
| `medellin_laureles`     | Medellín Laureles           |
| `medellin_envigado`     | Medellín Envigado           |
| `medellin_bello`        | Medellín Bello              |
| `medellin_itagui`       | Medellín Itagüí             |
| `bogota_chapinero`      | Bogotá Chapinero            |
| `bogota_usaquen`        | Bogotá Usaquén              |
| `cali_granada`          | Cali Granada                |
| `barranquilla_norte`    | Barranquilla Norte          |
| `miami_doral`           | Miami Doral                 |
| `miami_hialeah`         | Miami Hialeah               |
| `miami_kendall`         | Miami Kendall               |
| `orlando_international` | Orlando International Drive |
| `fort_lauderdale`       | Fort Lauderdale             |

Cuando el origen sea `internal` o `customer` y no corresponda a un local específico, se usará `central`.

---

## Categorías de incidencias

El campo `category` debe contener exactamente uno de estos valores:

| Valor                | Descripción                                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| `equipment_failure`  | Fallo de equipamiento de cocina o sala (horno, freidora, cámara frigorífica, TPV) |
| `supply_issue`       | Problema con insumos: falta de producto, calidad deficiente, entrega incorrecta   |
| `customer_complaint` | Queja o reclamación de cliente: producto, servicio, tiempo de espera, experiencia |
| `staff_issue`        | Incidencia relacionada con personal: ausencia, conflicto, accidente laboral leve  |
| `facility_issue`     | Problema de instalaciones: agua, electricidad, climatización, limpieza            |
| `pos_system`         | Error en el sistema de caja o TPV                                                 |
| `delivery_issue`     | Problema con pedidos a domicilio o plataformas de delivery                        |
| `other`              | Cualquier incidencia que no encaje en las categorías anteriores                   |

---

## Estados y ciclo de vida

| Valor         | Significado en Brasaland                                           |
| ------------- | ------------------------------------------------------------------ |
| `open`        | Incidencia recién registrada, pendiente de asignar                 |
| `in_progress` | El equipo de operaciones o el gerente del local está gestionándola |
| `resolved`    | Incidencia cerrada con solución confirmada                         |
| `discarded`   | Registrada por error o duplicada — no requiere acción              |

Transiciones válidas: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. Los estados `resolved` y `discarded` son finales.

---

## Orígenes

| Valor      | Cuándo usarlo en Brasaland                                                  |
| ---------- | --------------------------------------------------------------------------- |
| `customer` | Queja o incidencia comunicada por un cliente (en local, por app, por email) |
| `branch`   | Reportada por el gerente o personal de un local específico                  |
| `internal` | Detectada por el equipo corporativo (operaciones, tecnología, RRHH)         |

---

## Datos históricos — seed desde CSV

El fichero CSV del proyecto **incidents-file-analyzer** (`incidents-<empresa>.csv` en `content/contexts/incidents-file-analysis/`) contiene incidencias exportadas del sistema legacy de atención al cliente. Todas son de origen cliente (`origin: "customer"`).

El esquema del CSV del analizador usa nombres de campo, estados y categorías distintos a los de este gestor. **No insertes filas del CSV directamente.** Reutiliza la lógica de validación compartida del analizador y aplica las transformaciones siguientes antes del insert.

**Campo identificador para idempotencia:** usa `incident_id` del CSV Brasaland. Si no existe, usa la combinación `title + created_at`.

### Mapeo directo de campos

| Campo CSV                   | Campo del modelo | Transformación                                                                 |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------ |
| `incident_id` / `ticket_id` | —                | Solo control de duplicados — no se almacena                                    |
| `description`               | `title`          | Primeros 120 caracteres de `description`, recortados. Descartar si queda vacío |
| `description`               | `description`    | Copiar literalmente                                                            |
| `date`                      | `created_at`     | Parsear `YYYY-MM-DD` como medianoche UTC. `updated_at` igual al insertar       |
| —                           | `origin`         | Siempre `"customer"` en todos los registros del seed                           |

### Mapeo de estados (todas las empresas)

| CSV `status` | Modelo `status` |
| ------------ | --------------- |
| `OPEN`       | `open`          |
| `CLOSED`     | `resolved`      |
| `DISCARDED`  | `discarded`     |

### Mapeo de categorías (Brasaland)

| CSV `category`       | Modelo `category`    |
| -------------------- | -------------------- |
| `CUSTOMER_COMPLAINT` | `customer_complaint` |
| `EQUIPMENT`          | `equipment_failure`  |
| `SUPPLY`             | `supply_issue`       |
| `FOOD_QUALITY`       | `customer_complaint` |
| `STAFF`              | `staff_issue`        |

### Mapeo de sede (Brasaland)

Mapea `location_id` del CSV a `branch` del modelo. Si falta o no hay mapeo, usa `central`.

| CSV `location_id` | Modelo `branch`         |
| ----------------- | ----------------------- |
| `COL-01`          | `medellin_centro`       |
| `COL-02`          | `medellin_laureles`     |
| `COL-03`          | `medellin_envigado`     |
| `COL-04`          | `medellin_bello`        |
| `COL-05`          | `medellin_itagui`       |
| `COL-06`          | `bogota_chapinero`      |
| `COL-07`          | `bogota_usaquen`        |
| `COL-08`          | `cali_granada`          |
| `COL-09`          | `barranquilla_norte`    |
| `COL-10`          | `central`               |
| `FLA-01`          | `miami_doral`           |
| `FLA-02`          | `miami_hialeah`         |
| `FLA-03`          | `miami_kendall`         |
| `FLA-04`          | `orlando_international` |

Los registros que fallen la validación o no se puedan mapear se descartan y se reportan en consola.

---

## Valores esperados tras el seed

Tras cargar el CSV, `/api/incidents/summary` debe devolver totales por `status` y `category` del **modelo** que coincidan con los siguientes conteos transformados. Corresponden a los **96 registros válidos** de `incidents-brasaland.csv` del proyecto analizador (excluidas filas inválidas).

**Por `status` del modelo:**

| Modelo `status` | Conteo |
| --------------- | ------ |
| `open`          | 32     |
| `resolved`      | 50     |
| `discarded`     | 14     |

**Por `category` del modelo:**

| Modelo `category`    | Conteo |
| -------------------- | ------ |
| `customer_complaint` | 48     |
| `equipment_failure`  | 17     |
| `supply_issue`       | 22     |
| `staff_issue`        | 9      |

Contrasta con la salida del script analizador: el CSV crudo usa `OPEN`/`CLOSED`/`DISCARDED` y códigos como `CUSTOMER_COMPLAINT`/`FOOD_QUALITY`. Los totales anteriores son los valores **post-transformación** que debe producir tu gestor.

---

## Notas de implementación

- El formulario lo usarán gerentes de local desde dispositivos táctiles: los campos deben ser suficientemente grandes y el desplegable de sede debe mostrar el nombre legible (`Medellín Centro`), no el valor interno (`medellin_centro`).
- Los mensajes de error deben estar en el idioma base elegido para la aplicación. Si has implementado soporte bilingüe en hitos anteriores, mantén esa lógica.
- Las incidencias de tipo `customer_complaint` con estado `open` durante más de 48 horas son prioritarias para Felipe — aunque la alerta automática no es parte de este proyecto, diseña el modelo de datos pensando en que ese filtro deberá ser fácil de implementar más adelante.
