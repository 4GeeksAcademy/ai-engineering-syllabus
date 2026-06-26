# Procesos en Segundo Plano

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Tu empresa tiene un pipeline de datos y una API con telemetría instrumentada. El problema es que alguien tiene que ejecutar el pipeline cada noche. Tu tech lead ha registrado el siguiente ticket:

> > **Ticket #DEV-53 — Script nocturno de telemetría**
> >
> > Necesitamos un script que se ejecute cada noche de forma automática, sin intervención manual. El script debe exportar los datos de telemetría del día anterior a CSV (si aún no se ha hecho), lanzar el pipeline de datos, y dejar constancia en base de datos de qué pasó y cuándo.
> >
> > **Criterios de aceptación:**
> >
> > - El script es un proceso completamente independiente de la API — no puede bloquear ningún endpoint ni ejecutarse en el mismo hilo de FastAPI.
> > - Si el script ya está corriendo cuando el siguiente ciclo lo dispara, la segunda instancia debe abortar silenciosamente. No dos ejecuciones en paralelo.
> > - Si el script falla, el estado de ese registro en base de datos debe quedar en `failed`, no en `processing`. Ningún registro puede quedarse zombi.
> > - El script debe ser idempotente: si se ejecuta dos veces sobre el mismo día, el resultado debe ser el mismo que si se hubiera ejecutado una sola vez.
> > - Cada ejecución queda registrada con timestamp, estado (`pending` → `processing` → `completed` | `failed`) y, en caso de error, el mensaje de la excepción.
> >
> > Pon el script en `scripts/` y la lógica de estado en `services/`. El disparador queda en crontab o en el scheduler del framework — la decisión es tuya, justifícala en el PR.

### 📚 Conocimiento complementario — Ciclo de vida de una tarea en segundo plano

Antes de escribir una línea de código, hay un concepto arquitectónico que debes interiorizar: **en procesamiento en segundo plano, un dato no existe solo como "dato" — existe como un estado.**

La máquina de estados canónica para este tipo de tarea es:

```
pending → processing → completed
                    ↘ failed
```

Cada transición importa:

- **`pending`** — la tarea está esperando ser ejecutada. Se crea el registro antes de empezar.
- **`processing`** — se actualiza al inicio de la ejecución, antes de hacer ningún trabajo. Esto es lo que impide que otro proceso tome la misma tarea.
- **`completed`** — se actualiza solo si todo terminó bien.
- **`failed`** — se actualiza si se captura cualquier excepción. Nunca debe quedarse en `processing`.

El patrón **Distributed Lock** complementa a la máquina de estados: al iniciar, el script escribe un "candado" en base de datos. Si la siguiente ejecución detecta el candado, aborta silenciosamente. Al terminar —bien o mal— el candado se libera.

Un script que implementa estos dos patrones puede fallar, reiniciarse, o ejecutarse fuera de horario y siempre dejará el sistema en un estado conocido y recuperable.

---

## 🌱 Cómo Empezar el Proyecto

1. Revisa tu monorepo: identifica las tablas de telemetría existentes y las convenciones de nomenclatura que ya has usado para rutas y campos.
2. Crea la tabla de control de ejecuciones en base de datos (puedes añadirla al schema existente o crear una migración nueva).
3. Implementa el script en `scripts/nightly_export.py` y el servicio de control de estado en `services/`.
4. Configura el disparador en crontab o en el scheduler de tu framework y documenta la expresión cron en el PR.

---

## 💻 Qué Debes Hacer

### Modelo de datos

- [ ] Crear una tabla `job_runs` con al menos los campos: `id`, `job_name`, `status` (`pending` | `processing` | `completed` | `failed`), `started_at`, `finished_at`, `error_message`, `created_at`.
- [ ] Añadir la migración o instrucción SQL necesaria para crear la tabla en el esquema del monorepo.

### Script principal (`scripts/nightly_export.py`)

- [ ] El script exporta los registros de telemetría del día anterior a un archivo CSV en `data/raw/`, con nombre que incluya la fecha (p. ej. `telemetry_2025-01-15.csv`), **si ese archivo no existe todavía**.
- [ ] El script lanza el pipeline de datos como subproceso una vez completada la exportación.
- [ ] El script escribe en `job_runs` el resultado de la ejecución (estado final + timestamp + error si lo hay).
- [ ] El script es ejecutable directamente desde línea de comandos: `python scripts/nightly_export.py`.

### Idempotencia y bloqueo

- [ ] Implementar un **Distributed Lock**: si ya existe un registro `job_runs` con `status = 'processing'` para el job `nightly_export`, el script aborta silenciosamente y registra la cancelación en el log.
- [ ] Implementar **idempotencia**: si ya existe un registro `completed` para la fecha de ayer, el script no vuelve a exportar el CSV ni relanza el pipeline. Registra en el log que la ejecución fue omitida por ser duplicada.

### Control de estado (`services/`)

- [ ] Implementar un módulo `job_runner` en `services/` con funciones para crear, actualizar y consultar registros de `job_runs`.
- [ ] Cualquier excepción no controlada debe capturarse, actualizar el estado a `failed` con el mensaje de error, liberar el lock y propagar el error al log.
- [ ] Ningún registro puede quedar en estado `processing` tras una ejecución fallida.

### Disparador

- [ ] Configurar el cronjob mediante `crontab` del sistema operativo **o** mediante el scheduler de tu framework (p. ej. `fastapi-utils`, `APScheduler`).
- [ ] Documentar la expresión cron y la decisión de implementación en el cuerpo del PR.
- [ ] Añadir una variable de entorno `TARGET_DATE` opcional para sobrescribir la fecha objetivo y poder probar el script en cualquier momento sin modificar el código.

### Observabilidad

- [ ] Generar logs de ejecución con nivel `INFO` para los eventos normales (inicio, fin, omisión por duplicado) y `ERROR` para excepciones.
- [ ] Cada línea de log incluye timestamp, nombre del job y estado resultante.

---

## ✅ Qué Evaluaremos

- [ ] El script es un proceso independiente: no importa ni ejecuta código de FastAPI en el hilo principal de la aplicación.
- [ ] La máquina de estados `pending → processing → completed | failed` está implementada y los registros en `job_runs` reflejan el estado real de cada ejecución.
- [ ] El Distributed Lock impide ejecuciones paralelas: demostrable lanzando dos instancias del script al mismo tiempo.
- [ ] El script es idempotente: ejecutarlo dos veces sobre el mismo día produce el mismo resultado que ejecutarlo una vez, sin duplicar registros CSV ni ejecuciones del pipeline.
- [ ] Ningún registro queda en estado `processing` tras un fallo: el bloque `try/except/finally` garantiza la transición a `failed` y la liberación del lock.
- [ ] El CSV de salida existe en `data/raw/` con nombre correcto y contiene los datos de telemetría del día anterior.
- [ ] Los logs incluyen timestamp, nombre del job y estado en cada evento relevante.
- [ ] El disparador está configurado y la expresión cron documentada en el PR.
- [ ] `TARGET_DATE` permite ejecutar el script sobre fechas arbitrarias sin modificar el código.

---

## 📦 Cómo Entregar

1. Asegúrate de que todos los ítems del checklist estén completados.
2. Haz push de tu rama al repositorio.
3. Abre un **Pull Request** desde tu rama hacia `main`.
4. En el cuerpo del PR incluye:
   - La expresión cron configurada y el método elegido (crontab vs. scheduler de framework), con una breve justificación.
   - Un ejemplo del log de una ejecución exitosa y uno de una ejecución fallida o bloqueada.
   - Captura o fragmento del CSV generado (primeras filas).
5. Añade la etiqueta `cronjob` al PR antes de enviarlo a revisión.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
