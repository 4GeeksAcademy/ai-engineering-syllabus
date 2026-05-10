# Plataforma de Escuela de Cocina — Configuración de Monorepo con IA (Ejemplo en Clase)

> **Nota para el instructor:** Este es un ejemplo simplificado en clase para el hito "AI-Driven Engineering". Usa este escenario para introducir el patrón de memory bank, `AGENTS.md`, reglas de agente y skills en el contexto de un monorepo pequeño — completable en 1–2 horas. El proyecto original aplica los mismos conceptos a un monorepo multi-empresa más grande con más hitos de código acumulado.

---

## Escenario

Estás trabajando en la plataforma digital de **Masa & Fuego**, una escuela de cocina local. El repositorio ya tiene una página de inicio (HTML) y algo de lógica de precios (TypeScript). Antes de añadir más funcionalidades, tu tech lead quiere que el repositorio esté **listo para IA**: el agente de código debe tener contexto persistente, un flujo de trabajo definido y al menos una skill reutilizable.

> *"Ahora mismo, si le doy este repositorio al agente, no tiene ni idea de qué estamos construyendo ni de cómo trabajamos. Vamos a solucionarlo antes de seguir avanzando."*  
> — Tech lead

---

## Conceptos Clave

| Concepto | Qué es | Dónde vive |
|---------|---------|------------|
| **Memory bank** | Archivos Markdown que el agente lee al inicio de cada sesión | `memory-bank/` |
| **AGENTS.md** | Reglas de flujo de trabajo que el agente debe seguir antes de hacer commit | Raíz del repositorio |
| **Reglas** | Instrucciones con alcance para situaciones específicas | `.agents/rules/` |
| **Skill** | Una tarea reutilizable y estructurada con resultado verificable | `.agents/skills/<nombre>/SKILL.md` |

---

## Lo que Debes Hacer

### Paso 1 — Crea el memory bank

Crea una carpeta `memory-bank/` en la raíz del repositorio con dos archivos:

- [ ] **`projectbrief.md`** — Responde: ¿Qué es Masa & Fuego? ¿Quién usa esta plataforma? ¿Qué problema resuelve? ¿Cuáles son las dos partes principales (sitio público + backoffice)?
- [ ] **`techContext.md`** — Responde: ¿Cuál es el stack tecnológico? ¿Qué se ha construido hasta ahora? ¿Cuáles son las restricciones actuales (p. ej., sin base de datos todavía, solo TypeScript para la lógica de precios)?

> El memory bank es **documentación viva** — debe actualizarse cada vez que se tome una decisión importante o se añada una nueva funcionalidad. Un memory bank desactualizado es peor que no tener ninguno.

### Paso 2 — Escribe `AGENTS.md`

Crea `AGENTS.md` en la raíz del repositorio. Debe definir:

- [ ] Qué archivos del memory bank lee el agente al inicio de cada sesión (enuméralos explícitamente).
- [ ] Un **flujo de trabajo pre-commit** obligatorio con al menos 4 pasos ordenados. Estructura de ejemplo:
  1. Leer los archivos del memory bank.
  2. Verificar que los archivos modificados siguen la convención de nombres.
  3. Ejecutar linting o comprobaciones de tipos.
  4. Actualizar `memory-bank/progress.md` con el cambio realizado.
- [ ] Al menos una carpeta que el agente **no debe modificar** sin confirmación del desarrollador (p. ej., `memory-bank/techContext.md` — las decisiones arquitectónicas requieren aprobación humana).

### Paso 3 — Añade una regla

Crea `.agents/rules/no-inline-styles.md` con:

- [ ] Alcance: aplica a todos los archivos `.tsx` y `.html`.
- [ ] Regla: no se permiten atributos `style` en línea — todos los estilos deben usar clases de Tailwind o un módulo CSS.
- [ ] Justificación: explica en una frase por qué existe esta regla.

### Paso 4 — Crea una skill

Crea `.agents/skills/add-page-section/SKILL.md` para una tarea recurrente: añadir una nueva sección al sitio web público.

- [ ] **Objetivo:** Una sola frase — ¿qué hace esta skill?
- [ ] **Entradas:** ¿Qué necesita saber el agente antes de empezar? (p. ej., título de la sección, contenido, posición en la página)
- [ ] **Pasos:** Lista numerada de acciones que realiza el agente.
- [ ] **Criterios de aceptación:** Al menos 3 condiciones verificables (p. ej., *"La sección aparece en la posición correcta al ejecutar `npm run dev`"*).

### Paso 5 — Estructura las apps Next.js

- [ ] Crea `uis/website/` — una app Next.js + TypeScript para el sitio público de la escuela de cocina.
  - [ ] La ruta `/` renderiza una página de inicio simple (nombre de la escuela, eslogan, un placeholder de sección).
- [ ] Crea `uis/backoffice/` — una app Next.js + TypeScript para uso interno.
  - [ ] La ruta `/` renderiza una shell básica de dashboard (encabezado + contenido placeholder).
  - [ ] Importa y muestra en pantalla el resultado del módulo TypeScript de lógica de precios existente (no solo en la consola).

> Ambas apps deben arrancar sin errores con `npm run dev`.

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
│   │   └── no-inline-styles.md
│   └── skills/
│       └── add-page-section/
│           └── SKILL.md
└── uis/
    ├── website/        ← Sitio público Next.js
    └── backoffice/     ← App interna Next.js
```

---

## Lista de Verificación

- [ ] `memory-bank/projectbrief.md` describe tanto el contexto de negocio como el técnico (no solo uno).
- [ ] `AGENTS.md` especifica al menos 4 pasos pre-commit ordenados.
- [ ] `.agents/rules/no-inline-styles.md` tiene un alcance explícito y una justificación.
- [ ] `.agents/skills/add-page-section/SKILL.md` tiene objetivo, entradas, pasos y criterios de aceptación.
- [ ] `uis/website/` arranca sin errores y renderiza una página de inicio en `/`.
- [ ] `uis/backoffice/` arranca sin errores y muestra el resultado de la lógica de precios en pantalla.

---

## Preguntas para Debatir

1. ¿Cuál es la diferencia entre `AGENTS.md` (una regla) y una skill? ¿Cuándo usarías una u otra?
2. ¿Por qué las decisiones arquitectónicas en `techContext.md` deberían requerir confirmación humana antes de que el agente las modifique?
3. Escribe un criterio de aceptación más para la skill `add-page-section` que verifique que el agente no rompió las secciones existentes.
