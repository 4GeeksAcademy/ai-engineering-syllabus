# Campus Bike Share — Arranque del banco de memoria (ejemplo de clase)

> **Para instructores:** No es el proyecto del estudiante. Demo en vivo (~60–90 min) con la misma columna vertebral que `ai-eng-monorepo-kickoff-memory-bank`: conversación de descubrimiento → sintetizar vs conservar íntegro → política de stack vacío → huecos pendientes → índice `CONTEXT.md` → prueba en sesión limpia. El dominio es una pequeña cooperativa de bicicletas del campus, no el monorepo de empresa.

_These instructions are also available in [English](./README.md)._

---

## El reto

Una cooperativa de bicicletas del campus tiene un repo casi vacío: carpetas con nombre, un `CONTEXT.md` marcador de posición y un “BRIEFING” de una página más dos notas de departamento (Ops y Membership). Antes de cualquier feature, la clase debe dejar un banco de memoria listo para agentes: qué se construye, para quién y bajo qué reglas — sin inventar un stack.

### Nota de alcance

| Conservar (misma columna)                     | Reducir vs proyecto completo                     |
| --------------------------------------------- | ------------------------------------------------ |
| Q&A de descubrimiento antes de escribir       | BRIEFING corporativo + muchos departamentos      |
| Banco de memoria en ficheros por preocupación | Cinco historias de tres depts (usar **3**)       |
| Stack vacío + política + plantilla            | Mapa completo del monorepo (usar **3** carpetas) |
| Pendiente + evento que desbloquea             | PR largo (en clase basta oral)                   |
| Índice corto en `CONTEXT.md` + sesión limpia  | Varios docs íntegros en `docs/` (usar **1**)     |

Los estudiantes siguen el enunciado completo en el `README.md` raíz del proyecto.

---

## Qué construir

### Preparación (5 min)

Proporciona una carpeta de juguete (o un pegado) con:

```text
campus-bike-share/
├── CONTEXT.md          ← solo marcador de posición
├── apps/               ← vacía, “herramientas para ciclistas”
├── services/           ← vacía, “APIs de ops más adelante”
├── docs/               ← vacía
└── briefing/
    ├── BRIEFING.md     ← visión, usuarios, no-objetivos (1 página)
    ├── ops-notes.md    ← proceso de préstamo con excepciones (conservar íntegro)
    └── membership.md   ← corto; se puede sintetizar
```

### Conversación de descubrimiento

- [ ] En modo planificación/chat, pide al agente que lea las tres fuentes y liste ambigüedades antes de proponer ficheros
- [ ] Decide juntos: `ops-notes.md` → íntegro en `docs/`; `membership.md` + BRIEFING → sintetizar
- [ ] Conserva 1–2 preguntas del agente que cambien lo que escribas

### Banco de memoria (conjunto mínimo)

- [ ] Crea `memory-bank/` con ficheros separados: visión + aceptación (incl. **3** historias de Ops, Membership y otro rol), stack (vacío + política + plantilla), arquitectura (solo responsabilidades de carpetas), comandos (pendiente + desbloqueo), tabúes (al menos “no inventar stack”), estado actual
- [ ] Cita la fuente en cada fichero; enlaza `docs/ops-notes.md` indicando cuándo leerlo

### Punto de entrada del contexto

- [ ] Reemplaza `CONTEXT.md`: blurb de 3–4 líneas + índice de cada fichero de memory-bank y docs con cuándo leerlo + “actualizar este índice cuando cambien tech/docs/estado”

### Verificar juntos

- [ ] Chat nuevo, “empieza desde `CONTEXT.md`”: pregunta quiénes son los usuarios, qué queda fuera de alcance y si FastAPI es el stack → el agente debe decir que el stack no está decidido y citar la política
- [ ] Pídele que proponga una librería → debe exigir versión exacta + fuente oficial
- [ ] Corrige alucinaciones y repregunta una vez

---

## Preguntas de discusión

1. ¿Por qué volcar el BRIEFING en `CONTEXT.md` es peor que un índice corto con líneas de cuándo leer?
2. ¿Cuándo un proceso debe quedarse íntegro en `docs/` en lugar de resumirse en el banco de memoria?
3. ¿Cómo un documento de stack vacío con política de entrada evita que el agente invente tecnología?
