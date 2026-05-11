# CONTEXT — Gestor de Incidencias Centralizado · TrackFlow

## Tu empresa

**TrackFlow** es una empresa de gestión de almacenes y última milla con **130 empleados**, operando en dos mercados: **Los Ángeles (EE.UU.)** y **Zaragoza (España)**. Sus servicios son gestión de almacén para marcas de e-commerce, entrega de última milla y logística inversa (devoluciones).

Como parte del equipo de **TrackFlow Tech**, llevas hitos construyendo la plataforma interna. Este proyecto integra en esa plataforma un gestor centralizado de incidencias. En TrackFlow, las incidencias son el pan de cada día: paquetes perdidos, fallos de carrier, discrepancias de inventario, devoluciones mal gestionadas. Hasta ahora todo llegaba por email o WhatsApp sin ningún registro estructurado.

---

## Quién lo usa y por qué

**Andrés Kim (CTO)** no tiene visibilidad de los fallos operativos hasta que alguien le escribe por WhatsApp. Con este gestor, cada incidencia queda registrada, categorizada y trazable.

**Thomas Harry (CEO)** quiere saber en tiempo real cuántas incidencias críticas hay abiertas en Los Ángeles vs. Zaragoza, y si alguna lleva más de 24 horas sin resolverse.

**Carlos Vega (Head of Carrier Operations)** y **Ana Whitfield (Head of Warehouse Operations)** son los principales usuarios del formulario: ellos y sus equipos reportarán incidencias operativas desde almacén o desde coordinación de carriers.

**Valentina Cruz (CX Manager)** registrará las quejas de clientes finales y empresas que lleguen por canales externos.

---

## Almacenes y oficinas de TrackFlow

El campo `branch` debe contener exactamente uno de estos valores:

| Valor en base de datos | Nombre para mostrar   |
| ---------------------- | --------------------- |
| `central`              | Central               |
| `la_warehouse`         | Los Ángeles — Almacén |
| `la_office`            | Los Ángeles — Oficina |
| `zaragoza_warehouse`   | Zaragoza — Almacén    |
| `zaragoza_office`      | Zaragoza — Oficina    |

Cuando el origen sea `internal` o `customer` y no corresponda a una instalación específica, se usará `central`.

---

## Categorías de incidencias

El campo `category` debe contener exactamente uno de estos valores:

| Valor                   | Descripción                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------- |
| `lost_parcel`           | Paquete extraviado en tránsito o en almacén                                            |
| `delivery_failure`      | Fallo de entrega: intento fallido, dirección incorrecta, cliente ausente no gestionado |
| `inventory_discrepancy` | Diferencia entre stock registrado y stock físico                                       |
| `carrier_issue`         | Problema imputable a un carrier: retraso, daño, incumplimiento de SLA                  |
| `returns_issue`         | Problema en el proceso de devolución o logística inversa                               |
| `warehouse_incident`    | Incidente en almacén: daño de mercancía, accidente, fallo de equipamiento              |
| `system_failure`        | Fallo en sistema tecnológico: WMS, integraciones, API de carrier                       |
| `client_complaint`      | Queja de una empresa cliente sobre el servicio prestado por TrackFlow                  |
| `other`                 | Cualquier incidencia que no encaje en las categorías anteriores                        |

---

## Estados y ciclo de vida

| Valor         | Significado en TrackFlow                                          |
| ------------- | ----------------------------------------------------------------- |
| `open`        | Incidencia registrada, pendiente de asignar al equipo responsable |
| `in_progress` | Coordinador o responsable de área está gestionándola activamente  |
| `resolved`    | Resuelta: paquete entregado, stock corregido, cliente informado   |
| `discarded`   | Registrada por error, duplicada o no accionable                   |

Transiciones válidas: `open → in_progress`, `open → discarded`, `in_progress → resolved`, `in_progress → discarded`. Los estados `resolved` y `discarded` son finales.

---

## Orígenes

| Valor      | Cuándo usarlo en TrackFlow                                           |
| ---------- | -------------------------------------------------------------------- |
| `customer` | Reportada por una empresa cliente o un consumidor final              |
| `branch`   | Detectada y reportada por personal de almacén u oficina de TrackFlow |
| `internal` | Detectada internamente por tecnología, dirección u operaciones       |

---

## Datos históricos — seed desde CSV

El fichero CSV del proyecto anterior contiene incidencias exportadas del sistema de atención al cliente de TrackFlow. Todas corresponden a incidencias comunicadas por clientes o consumidores finales (`origin: "customer"`).

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

- TrackFlow opera en dos idiomas: inglés en Los Ángeles y español en Zaragoza. Si has implementado soporte bilingüe en hitos anteriores, el formulario y los mensajes de error deben respetarlo. Las etiquetas del desplegable de sedes deben mostrarse en el idioma del usuario.
- Las incidencias de tipo `lost_parcel` y `carrier_issue` tienen impacto directo en el SLA con clientes: Thomas y Carlos necesitarán filtrarlas con facilidad. El modelo de datos debe facilitar ese filtro aunque la alerta automática no sea parte de este proyecto.
- El formulario lo usarán operarios de almacén desde terminales en el suelo del almacén: diseña los campos con tamaño suficiente para uso táctil y evita campos de texto libre innecesarios.
