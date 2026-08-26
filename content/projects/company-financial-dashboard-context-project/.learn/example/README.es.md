# Ejemplo en Clase: Entendiendo una App de Catálogo de Biblioteca

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio es una app de catálogo de biblioteca comunitaria en lugar de un dashboard financiero — mismo flujo de investigación con coding agent, comprensión verificada, reglas de ingeniería y documentación del memory bank, pero con una base de código más pequeña y familiar.

_These instructions are also available in [English](./README.md)._

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo flujo agent-first que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Acabas de unirte a un pequeño equipo que mantiene una app de catálogo de biblioteca comunitaria. Hay frontend y backend, pero la entrega fue precipitada: pocas docs, sin estándares de código escritos y sin notas sobre qué está terminado o roto. **No** necesitas conocimiento previo del stack. Tu trabajo es dirigir un coding agent para entender lo que existe, derivar reglas desde evidencia del repo y dejar un memory bank en el que cualquier colaborador (o agent) futuro pueda apoyarse.

---

## Conceptos Cubiertos

| Concepto                                | Dónde se aplica                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| Exploración agent-first del código      | Fase 1: pedir, verificar y corregir el resumen del proyecto                  |
| Hallazgos de ingeniería basados en evidencia | Fase 2: convenciones y riesgos del repo (no checklists personales)      |
| Reglas de repositorio (`.agents/rules`) | Fase 3: el agent redacta reglas; el estudiante las prueba en una tarea real  |
| Documentación del memory bank           | Fase 4: producto, stack, estado — el agent redacta, el estudiante verifica   |
| Disciplina de commits                   | Un commit por fase, sin mega-commits agrupados                               |

---

## Punto de Partida

Usa una carpeta local de proyecto de ejemplo con esta estructura mínima:

```
library-catalog/
├── frontend/
├── backend/
├── docker-compose.yml
└── README.md         ← mínimo, poco útil
```

**No** digas a los estudiantes puertos o frameworks fijos de antemano. Pide al agent descubrir cómo ejecutar la app a partir de la evidencia del repo.

---

## Qué Hacer

### Fase 1 — Entender la entrega (con el agent)

- [ ] Pregunta al agent cómo levantar los servicios y cómo confirmar que están sanos; sigue la evidencia del repo
- [ ] Pregunta: _"Resume este proyecto: ¿qué hace, cómo está estructurado, cómo lo ejecuto y cuál es el stack? Cita rutas."_
- [ ] Marca afirmaciones importantes ✅ / ❌ / ❓ contra archivos reales; corrige inexactitudes con el agent
- [ ] Deja un rastro corto de verificación (mensaje de commit o `verification.md`)
- [ ] Commit: `"Fase 1: resumen del proyecto con IA y validación"`

### Fase 2 — Derivar hallazgos de ingeniería (con el agent)

- [ ] Pide al agent convenciones útiles y patrones arriesgados que dañarían futuras ediciones del agent
- [ ] Quédate solo con hallazgos ligados a archivos/comportamientos concretos; agrupa por categoría
- [ ] Conviértelos en reglas propuestas — cada regla cita al menos un hecho del repo
- [ ] Commit: `"Fase 2: hallazgos de ingeniería y reglas propuestas"`

### Fase 3 — Escribir y probar reglas del repositorio

- [ ] Crea el directorio `.agents/rules/`
- [ ] Haz que el agent redacte al menos **2** archivos de reglas (p. ej. alcance frontend y backend). Cada uno debe incluir:
  - **Objetivo:** qué enforcea la regla
  - **Justificación:** por qué es importante para este proyecto
  - **Ejemplos:** un patrón correcto y uno incorrecto del código real
- [ ] Prueba cada regla: dale al agent una tarea pequeña real y comprueba si las reglas dirigen el trabajo; refina si no
- [ ] Commit: `"Fase 3: reglas del repositorio en .agents/rules"`

### Fase 4 — Construir el memory bank

- [ ] Crea una carpeta `memory-bank/` en la raíz del repositorio
- [ ] Haz que el agent redacte documentos que cubran al menos:
  - Overview del producto — qué hace la app, quién la usa, características clave
  - Stack tecnológico — lenguajes, frameworks, base de datos, dependencias clave
  - Estado actual — qué funciona, qué está incompleto, próximas prioridades sugeridas
- [ ] Verifica las afirmaciones contra el repo antes de hacer commit
- [ ] Commit: `"Fase 4: memory bank — producto, stack tecnológico y estado"`

---

## Preguntas para Discusión

1. Cuando le pediste al agent que resumiera el proyecto, ¿se equivocó en algo? ¿Qué te dice eso sobre confiar en la documentación generada por IA sin verificarla?
2. ¿Cuál es la diferencia entre una "regla" demasiado genérica (p. ej., "escribe código limpio") y una que sea accionable para este proyecto específico?
3. ¿Por qué es importante hacer un commit por cada fase en lugar de un gran commit al final?
4. ¿Quién debe inventar las buenas prácticas aquí — el estudiante de memoria, o el estudiante+agent desde la evidencia del codebase?
