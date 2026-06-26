# Ejemplo en clase: Sincronización nocturna de informes — App de huerto comunitario

> **Para instructores:** Escenario paralelo en aula para `ai-eng-cronjobs`. Misma columna vertebral (script CLI independiente, máquina de estados `job_runs`, distributed lock, idempotencia, exportación CSV, disparo por subproceso, `TARGET_DATE`, logs estructurados), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_Estas instrucciones también están disponibles en [inglés](./README.md)._

---

## El reto

### Nota de alcance

Este ejemplo está acotado a una sesión en vivo. Conserva los mismos patrones que el proyecto oficial del estudiante pero usa una app preconstruida de **huerto comunitario**: turnos de voluntariado en lugar de telemetría empresarial. Requisitos secundarios (pipeline Prefect completo, cron Docker en producción) se simplifican — ver notas abajo.

Una colectiva local registra turnos de voluntarios en SQLite. Cada noche, un coordinador exportaba manualmente los registros del día anterior y ejecutaba un script de agregación. Tu trabajo es automatizarlo con un job en segundo plano que nunca bloquee el panel Flask.

> **Del ticket del tech lead:**
>
> - El script nocturno es un proceso autónomo — no forma parte del ciclo de peticiones Flask.
> - Si una ejecución ya está en `processing`, el siguiente disparo aborta en silencio.
> - Las ejecuciones fallidas deben terminar en `failed`, nunca atascadas en `processing`.
> - Ejecutar dos veces la misma fecha no debe duplicar el CSV ni relanzar el agregador.
> - Cada ejecución queda registrada en log con timestamp, nombre del job y estado.

---

## Vista del código

```text
admin/                 Panel Flask de solo lectura (no modificar handlers para el job)
db/
  shifts.db            SQLite: tabla volunteer_shift
scripts/
  nightly_sync.py      ← implementar
  aggregate_shifts.py  Preconstruido: lee CSV, imprime resumen (simula pipeline)
services/
  job_runner.py        ← implementar
data/raw/              Directorio de salida CSV
```

---

## Qué construir

### Modelo de datos

- [ ] Crear tabla `job_runs` (mismos campos que el proyecto del estudiante: `id`, `job_name`, `status`, `started_at`, `finished_at`, `error_message`, `created_at`).
- [ ] Añadir columna opcional `target_date` para comprobaciones de idempotencia.

### `services/job_runner.py`

- [ ] Funciones para crear, actualizar y consultar `job_runs`.
- [ ] `has_processing_lock('nightly_sync')` y `has_completed_for_date('nightly_sync', date)`.

### `scripts/nightly_sync.py`

- [ ] Leer env `TARGET_DATE` o usar ayer por defecto.
- [ ] Distributed lock: abortar en silencio si existe otra fila `processing`.
- [ ] Idempotencia: omitir si ya hay `completed` para `target_date`.
- [ ] Exportar filas de `volunteer_shift` de `target_date` a `data/raw/shifts_YYYY-MM-DD.csv` **solo si el archivo no existe**.
- [ ] Ejecutar `python scripts/aggregate_shifts.py data/raw/shifts_YYYY-MM-DD.csv` como subproceso.
- [ ] Actualizar `job_runs` con la máquina de estados completa; capturar excepciones → `failed`.

### Disparador (simplificación en clase)

- [ ] En clase: ejecutar manualmente y demostrar dos terminales lanzando el script a la vez.
- [ ] Extensión para casa: añadir línea crontab `0 2 * * *` en notas del PR (no obligatorio en vivo).

### Logging

- [ ] INFO para inicio, fin, omisión, cancelación; ERROR para fallos.
- [ ] Cada línea: timestamp, `nightly_sync`, estado resultante.

---

## Verificar juntos

- [ ] `python scripts/nightly_sync.py` funciona sin arrancar Flask.
- [ ] El CSV aparece en `data/raw/` con la fecha correcta en el nombre.
- [ ] Dos ejecuciones simultáneas: una completa, la otra registra cancelación.
- [ ] Segunda ejecución el mismo día: log de omisión, sin nueva llamada al subproceso.
- [ ] Romper el agregador (ruta incorrecta): `job_runs` muestra `failed`, no `processing`.
- [ ] `TARGET_DATE=2025-06-01 python scripts/nightly_sync.py` exporta esa fecha.

---

## Preguntas de discusión

1. ¿Por qué el script nocturno debe ser un proceso separado en lugar de un hilo en segundo plano de Flask arrancado en la primera petición?
2. El distributed lock usa una fila `processing` en base de datos. ¿Qué pasa si el servidor cae a mitad de ejecución antes de escribir `failed` o `completed`? ¿Cómo recuperarías en producción?
3. La idempotencia comprueba tanto la tabla `job_runs` como la existencia del CSV. ¿Por qué son útiles ambas capas en lugar de confiar solo en una?
