# Ejemplo de clase: Tablero de incidencias de cafetería

> **Nota para el instructor:** Ejemplo de aula para _Backoffice de Operaciones – Gestor Centralizado de Incidencias_. Mismas ideas centrales (reconocimiento → reglas → memory-bank → ciclo de vida + historial) en un dominio pequeño de cafetería. Pensado para una sesión en vivo de 1–2 horas. NO compartir con estudiantes antes de que intenten el proyecto principal.

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Solo para sesión en vivo. Mismos patrones que el proyecto oficial; catálogos CONTEXT y profundidad del monorepo reducidos. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Una cadena pequeña de cafeterías tiene tres locales. Los turnos reportan fallos de equipo y huecos de personal por WhatsApp o teléfono; nada está centralizado. La responsable de ops quiere un tablero mínimo: registrar, asignar área, mover estado y ver quién cambió qué.

El repo es un monorepo stub con carpetas y nombrado ya decididos pero sin documentar.

---

## Fase 1 — Reconocimiento (15 min)

- [ ] Pide al agente un resumen del proyecto.
- [ ] Abre el árbol real y corrige al menos **dos** afirmaciones erróneas de ese resumen.
- [ ] Anota ≥2 convenciones ya visibles en el código (p. ej. gestor de paquetes, layout de carpetas).
- [ ] Registra una idea de mejora **sin** aplicarla.

---

## Fase 2 — Una regla + memory bank mínimo (20 min)

Crea `.agents/rules/no-new-package-manager.md`:

```markdown
---
description: Do not introduce a second package manager
globs: ["**/package.json", "**/pnpm-lock.yaml", "**/package-lock.json"]
alwaysApply: false
---

# No second package manager

- Use the lockfile and manager already present in the repo.
- Do not add npm/yarn/pnpm if another is already the source of truth.
- If a change seems to require a different manager, stop and ask.
```

Crea `memory-bank/` con:

- `product.md` — ops de cafetería, quién usa el tablero, qué significa aquí una incidencia `critical`
- `stack.md` — lo que el stub ya usa
- `status.md` — tablero vacío → primera feature de incidencias en curso

---

## Fase 3 — Tablero mínimo de incidencias (40–50 min)

### Modelo

| Campo                  | Notas                                                         |
| ---------------------- | ------------------------------------------------------------- |
| `id`                   | Auto                                                          |
| `title`, `description` | Obligatorios                                                  |
| `channel`              | `whatsapp` \| `phone_call` \| `dashboard`                     |
| `type`                 | `equipment_failure` \| `staffing_gap` \| `customer_complaint` |
| `severity`             | `critical` \| `high` \| `medium` \| `low`                     |
| `responsible_area`     | `operations` \| `people` \| `technology`                      |
| `status`               | `open` → `assigned` → `in_progress` → `resolved` → `closed`   |
| `assigned_to`          | String opcional                                               |
| historial              | Cambios de estado y asignado con `author` + marca temporal    |

### Debe demo

- [ ] Crear + listar + filtrar por `status` y `severity`
- [ ] Asignar `responsible_area` / `assigned_to`
- [ ] Recorrido completo de estados hasta `closed`
- [ ] Ficha con historial de cambios
- [ ] Conteos simples de abiertas por severidad

---

## Preguntas de discusión

1. ¿Por qué registrar discrepancias del resumen del agente en lugar de solo corregirlo en silencio?
2. ¿Cuándo conviene una regla frente a un párrafo del memory-bank?
3. ¿Por qué no basta con que cambie `updated_at` para rendición de cuentas en ops?

---

## Checklist del instructor

- [ ] Estudiantes corrigieron el resumen del agente con evidencia
- [ ] La regla declara ámbito / modo de aplicación
- [ ] El memory bank menciona el significado de producto de la severidad, no solo el stack
- [ ] El historial muestra autor + hora en al menos un cambio de estado
