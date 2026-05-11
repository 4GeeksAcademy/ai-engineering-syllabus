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

El fichero CSV del proyecto anterior contiene incidencias exportadas del sistema legacy de atención al cliente. Todas son de origen cliente (`origin: "customer"`).

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

Una vez cargado el CSV correctamente, el endpoint `/api/incidents/summary` debe devolver valores coherentes con los del fichero CSV validado en el proyecto anterior. Contrasta los totales por categoría y por estado con los resultados que obtuviste en el script de análisis — deben coincidir (descontando los registros inválidos que el seed descarta).

---

## Notas de implementación

- El formulario lo usarán gerentes de local desde dispositivos táctiles: los campos deben ser suficientemente grandes y el desplegable de sede debe mostrar el nombre legible (`Medellín Centro`), no el valor interno (`medellin_centro`).
- Los mensajes de error deben estar en el idioma base elegido para la aplicación. Si has implementado soporte bilingüe en hitos anteriores, mantén esa lógica.
- Las incidencias de tipo `customer_complaint` con estado `open` durante más de 48 horas son prioritarias para Felipe — aunque la alerta automática no es parte de este proyecto, diseña el modelo de datos pensando en que ese filtro deberá ser fácil de implementar más adelante.
