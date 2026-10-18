# Plataforma de Escuela de Cocina — Configuración de Monorepo con IA (Ejemplo en Clase)

> **Nota para el instructor:** Ejemplo simplificado en clase para el módulo "AI-Driven Engineering". Usa este escenario para introducir el patrón de memory bank, `AGENTS.md`, reglas de agente y skills en un monorepo pequeño — completable en 1–2 horas. El proyecto oficial del estudiante en la raíz del proyecto aplica los mismos patrones a plena escala con la empresa asignada en `BRIEFING.md`.

_These instructions are also available in [English](./README.md)._

---

## Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene los mismos patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Estás empezando la plataforma digital de **Masa & Fuego**, una escuela de cocina local. El repositorio es una plantilla en blanco — aún no hay código de aplicación. Antes de añadir funcionalidades, tu tech lead quiere que el repositorio esté **listo para IA**: el agente de código debe tener contexto persistente, un flujo de trabajo definido y al menos una skill reutilizable.

> _"Ahora mismo, si le doy este repositorio al agente, no tiene ni idea de qué estamos construyendo ni de cómo trabajamos. Vamos a solucionarlo antes de seguir avanzando."_  
> — Tech lead

---

## Conceptos Clave

| Concepto        | Qué es                                                                     | Dónde vive                         |
| --------------- | -------------------------------------------------------------------------- | ---------------------------------- |
| **Memory bank** | Archivos Markdown que el agente lee al inicio de cada sesión               | `memory-bank/`                     |
| **AGENTS.md**   | Reglas de flujo de trabajo que el agente debe seguir antes de hacer commit | Raíz del repositorio               |
| **Reglas**      | Instrucciones con alcance para situaciones específicas                     | `.agents/rules/`                   |
| **Skill**       | Una tarea reutilizable y estructurada con resultado verificable            | `.agents/skills/<nombre>/SKILL.md` |

---

## Lo que Debes Hacer

### Paso 1 — Crea el memory bank

Crea una carpeta `memory-bank/` en la raíz del repositorio con dos archivos:

- [ ] **`projectbrief.md`** — Responde: ¿Qué es Masa & Fuego? ¿Quién usa esta plataforma? ¿Qué problema resuelve? ¿Cuáles son las dos partes principales (sitio público + backoffice)?
- [ ] **`techContext.md`** — Responde: ¿Qué stack vas a usar? ¿Cuáles son las restricciones actuales (p. ej., sin base de datos todavía, proyecto greenfield)? ¿Qué carpetas existen en la plantilla del monorepo?

> El memory bank es **documentación viva** — debe actualizarse cada vez que se tome una decisión importante o se añada una nueva funcionalidad. Un memory bank desactualizado es peor que no tener ninguno.

### Paso 2 — Escribe `AGENTS.md`

Crea `AGENTS.md` en la raíz del repositorio. Debe definir:

- [ ] Qué archivos del memory bank lee el agente al inicio de cada sesión (enuméralos explícitamente).
- [ ] Un **flujo de trabajo pre-commit** obligatorio con al menos 4 pasos ordenados. Estructura de ejemplo:
  1. Leer los archivos del memory bank.
  2. Verificar que los archivos modificados siguen la convención de nombres.
  3. Ejecutar el comando de lint o validación del proyecto.
  4. Actualizar `memory-bank/progress.md` con el cambio realizado.
- [ ] Al menos una carpeta que el agente **no debe modificar** sin confirmación del desarrollador (p. ej., `memory-bank/techContext.md` — las decisiones arquitectónicas requieren aprobación humana).

### Paso 3 — Añade una regla

Crea `.agents/rules/no-hardcoded-copy.md` con:

- [ ] Alcance: aplica a archivos de UI/vistas en `uis/` (define los patrones de archivo que use tu stack).
- [ ] Regla: el copy de negocio (titulares, nombres de cursos, precios) debe vivir en un archivo de contenido dedicado o módulo de constantes — no disperso inline en el código de vistas.
- [ ] Justificación: explica en una frase por qué existe esta regla.

### Paso 4 — Crea una skill

Crea `.agents/skills/add-page-section/SKILL.md` para una tarea recurrente: añadir una nueva sección al sitio web público.

- [ ] **Objetivo:** Una sola frase — ¿qué hace esta skill?
- [ ] **Entradas:** ¿Qué necesita saber el agente antes de empezar? (p. ej., título de la sección, contenido, posición en la página)
- [ ] **Pasos:** Lista numerada de acciones que realiza el agente.
- [ ] **Criterios de aceptación:** Al menos 3 condiciones verificables (p. ej., _"La sección aparece en la posición correcta al ejecutar el comando de desarrollo del proyecto"_).

### Paso 5 — Aclara las carpetas del monorepo (no crees las apps)

Este paso es solo documentación — **no** scaffolds `uis/website` ni `uis/backoffice` aquí.

- [ ] En `techContext.md` (o una regla de agente), indica dónde va el código de producto cuando se cree:
  - `/uis` — frontends
  - `uis/website/` — sitio público de la escuela de cocina
  - `uis/backoffice/` — app interna del equipo
  - `/services` — APIs backend
- [ ] Confirma que no inventarás un árbol de apps paralelo fuera de ese mapa.

---

## Estructura Esperada del Repositorio

```
.
├── AGENTS.md
├── memory-bank/
│   ├── projectbrief.md
│   └── techContext.md
├── .agents/
│   ├── rules/
│   │   └── no-hardcoded-copy.md
│   └── skills/
│       └── add-page-section/
│           └── SKILL.md
```

(Mapa de carpetas para más adelante: `uis/website`, `uis/backoffice`, `services` — documentado, no arrancado en este ejemplo.)

---

## Lista de Verificación

- [ ] `memory-bank/projectbrief.md` describe tanto el contexto de negocio como el técnico (no solo uno).
- [ ] `AGENTS.md` especifica al menos 4 pasos pre-commit ordenados.
- [ ] `.agents/rules/no-hardcoded-copy.md` tiene un alcance explícito y una justificación.
- [ ] `.agents/skills/add-page-section/SKILL.md` tiene objetivo, entradas, pasos y criterios de aceptación.
- [ ] El mapa de carpetas para `uis/website`, `uis/backoffice` y `services` está documentado — no se requieren apps en esta sesión.

---

## Preguntas para Debatir

1. ¿Cuál es la diferencia entre `AGENTS.md` (una regla) y una skill? ¿Cuándo usarías una u otra?
2. ¿Por qué las decisiones arquitectónicas en `techContext.md` deberían requerir confirmación humana antes de que el agente las modifique?
3. Escribe un criterio de aceptación más para la skill `add-page-section` que verifique que el agente no rompió las secciones existentes.
