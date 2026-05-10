# Ejemplo en Clase: Entendiendo una App de Catálogo de Biblioteca

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio es una app de catálogo de biblioteca comunitaria en lugar de un dashboard financiero — mismo flujo de trabajo de comprensión de código con IA, reglas de ingeniería y documentación del memory bank, pero con una base de código más pequeña y familiar.

## El Escenario

Acabas de unirte a un pequeño equipo que mantiene una app de catálogo de biblioteca comunitaria. Hay un frontend en React y un backend en FastAPI, pero la entrega fue precipitada: no hay docs, no hay estándares de código escritos y no hay notas sobre qué está terminado o roto. Tu trabajo es usar tu asistente de IA para entender lo que existe, definir reglas para que sea mantenible y dejar un memory bank en el que cualquier colaborador futuro pueda apoyarse.

---

## Conceptos Cubiertos

| Concepto | Dónde se aplica |
|---|---|
| Exploración de código con IA | Fase 1: generar y validar un resumen del proyecto |
| Análisis de prácticas de ingeniería | Fase 2: identificar patrones buenos y malos |
| Reglas de repositorio (`.agents/rules`) | Fase 3: escribir archivos de gobernanza accionables |
| Documentación del memory bank | Fase 4: descripción del producto, stack tecnológico, estado actual |
| Disciplina de commits | Un commit por fase, sin mega-commits agrupados |

---

## Repositorio de Partida

Usa este repositorio como punto de partida (tu instructor compartirá el enlace real):

```
https://github.com/4GeeksAcademy/ai-eng-library-catalog-context-example
```

Estructura esperada tras clonar:

```
library-catalog/
├── frontend/         ← React (Vite)
├── backend/          ← FastAPI + SQLite
├── docker-compose.yml
└── README.md         ← mínimo, poco útil
```

---

## Qué Hacer

### Fase 1 — Entender la entrega

- [ ] Haz fork y clona el repositorio
- [ ] Ejecuta `docker compose up` y verifica que la app carga en `http://localhost:5173` y la documentación de la API en `http://localhost:8000/docs`
- [ ] Pregunta a tu asistente de IA: *"Resume este proyecto: ¿qué hace, cómo está estructurado y cuál es el stack tecnológico?"*
- [ ] Lee el resumen generado y compruébalo contra lo que realmente ves en el código — corrige cualquier inexactitud
- [ ] Commit: `"Fase 1: resumen del proyecto con IA y validación"`

### Fase 2 — Analizar las prácticas de ingeniería

- [ ] Revisa el código del frontend y backend e identifica:
  - Al menos **3 buenas prácticas** (p. ej., separación clara de componentes, nomenclatura consistente)
  - Al menos **3 prácticas arriesgadas o malas** (p. ej., falta de gestión de errores, valores hardcodeados, sin tests)
- [ ] Agrupa los hallazgos por categoría:

| Categoría | Hallazgo | Buena / Mala |
|---|---|---|
| Gestión de errores | Sin try/catch en las llamadas fetch | Mala |
| Nomenclatura | Los componentes usan PascalCase de forma consistente | Buena |
| ... | ... | ... |

- [ ] Commit: `"Fase 2: análisis de prácticas de ingeniería"`

### Fase 3 — Escribir reglas del repositorio

- [ ] Crea el directorio `.agents/rules/`
- [ ] Escribe al menos **2 archivos de reglas** — uno para el frontend, uno para el backend. Cada archivo debe incluir:
  - **Objetivo:** qué enforcea la regla
  - **Justificación:** por qué es importante para este proyecto
  - **Ejemplos:** un patrón correcto y uno incorrecto del código real
- [ ] Prueba cada regla: pide a tu asistente de IA que la aplique y verifica que la orientación tiene sentido
- [ ] Commit: `"Fase 3: reglas del repositorio en .agents/rules"`

### Fase 4 — Construir el memory bank

- [ ] Crea una carpeta `memory-bank/` en la raíz del repositorio
- [ ] Añade tres documentos:
  - `product.md` — qué hace la app, quién la usa, características clave
  - `tech-stack.md` — framework frontend, framework backend, base de datos, dependencias clave y sus versiones
  - `status.md` — qué funciona, qué está incompleto o roto, próximas prioridades sugeridas
- [ ] Commit: `"Fase 4: memory bank — producto, stack tecnológico y estado"`

---

## Preguntas para Discusión

1. Cuando le pediste a la IA que resumiera el proyecto, ¿se equivocó en algo? ¿Qué te dice eso sobre confiar en la documentación generada por IA sin verificarla?
2. ¿Cuál es la diferencia entre una "regla" demasiado genérica (p. ej., "escribe código limpio") y una que sea accionable para este proyecto específico?
3. ¿Por qué es importante hacer un commit por cada fase en lugar de un gran commit al final?
