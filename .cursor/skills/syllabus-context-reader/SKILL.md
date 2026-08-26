---
name: syllabus-context-reader
description: >
  Official syllabus source: planning CSV(s) under a `syllabus/` directory
  (e.g. ai-engineering-syllabus/docs/syllabus/*.csv). NOT syllabus.md — that
  file is a derived export and may be out of date. Discovers CSVs automatically;
  if more than one and none specified, asks the user which to use. Extracts full
  pedagogical context for a course day: skill, content, how-to-think, best
  practices, patterns, anti-patterns, limitations, and prior_skills.

  Use this skill whenever a request involves creating, reviewing, or adapting
  course content (lessons, exercises, projects, assessments, quizzes, README
  files, rubrics, slides, or any educational material) for the AI Engineer or
  AI Native Full Stack programs. Trigger on phrases like "para el día N",
  "semana X día Y", "hito N", "basado en el syllabus", "en el contexto del
  curso", "qué saben los estudiantes hasta el día X", or any request that
  implies alignment with a specific point in the course timeline.
---

# Syllabus Context Reader

Extrae el contexto pedagógico completo de un día del curso desde el CSV de
planificación del programa **AI Engineer** (o **AI Native Full Stack**).

---

## 0. Fuente oficial del syllabus

| Archivo / ubicación                                                      | Rol                                                                           |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **`**/syllabus/**/\*.csv`** (p. ej. `docs/syllabus/…Planificación….csv`) | **Fuente oficial** — semana, día, skill, teoría, proyecto, thinking framework |
| **`syllabus.md`**                                                        | Export derivado — **no usar como fuente**                                     |
| **GitHub raw URL de `syllabus.md`**                                      | Igual — evitar                                                                |

Si `syllabus.md` y el CSV **no coinciden**, gana el **CSV** (vía `parse_syllabus.py`).

**Ubicación canónica (este monorepo):**

`ai-engineering-syllabus/docs/syllabus/`

El parser busca ahí (y cualquier otro directorio llamado `syllabus/`) — no hardcodear rutas de CSV en skills consumidores.

---

## 1. Cuándo usar esta skill

- Crear o revisar **contenido de clase** (teoría, ejercicios, proyectos).
- Generar **READMEs** de proyectos o hitos.
- Diseñar **rúbricas** o **criterios de evaluación**.
- Producir **quizzes**, **checklists** o **material de apoyo**.
- Verificar que el contenido sea coherente con **lo que el estudiante ya sabe**.
- Consumida por `module-guidelines-generator` para crear lineamientos alineados al día.

> Regla de oro: nunca referenciar contenido de días futuros. El parser
> entrega `prior_skills` para evitar este error.

---

## 2. Prerequisito: resolver el CSV (`syllabus/`)

**No asumir un único archivo.** Flujo obligatorio:

```text
1. python3 …/parse_syllabus.py --list-csvs
   (opcional: --search-root <repo o workspace>)
2. count == 0 → error: falta CSV en syllabus/; avisar al usuario
3. count == 1 → OK; omitir --csv en comandos siguientes
4. count > 1 y el usuario NO nombró programa/archivo
   → STOP. Preguntar cuál CSV usar. Listar `candidates` (nombre + ruta).
5. Usuario elige → pasar --csv "<ruta>" o --csv "<substring único>"
   (ej. --csv "AI Engineer" vs --csv "Full Stack")
```

| Señal del usuario                 | Acción                                        |
| --------------------------------- | --------------------------------------------- |
| Ninguna / ambiguo + varios CSV    | **Preguntar** — no adivinar                   |
| “AI Engineer” / nombre de archivo | `--csv` con substring o path                  |
| Path explícito                    | `--csv <path>` (incluso fuera de `syllabus/`) |

Ruta tipica del script:

`course-outline-generator/skills/syllabus-context-reader/scripts/parse_syllabus.py`

---

## 3. Script de extracción

Ruta: `scripts/parse_syllabus.py`

### Comandos disponibles

**Listar CSVs descubiertos** (siempre primero si hay duda de programa):

```bash
python3 scripts/parse_syllabus.py --list-csvs
# o acotar el árbol:
python3 scripts/parse_syllabus.py --list-csvs --search-root ai-engineering-syllabus
```

**Listar todas las lecciones:**

```bash
python3 scripts/parse_syllabus.py --list
# con varios CSV:
python3 scripts/parse_syllabus.py --csv "AI Engineer" --list
```

**Extraer contexto de un día:**

```bash
python3 scripts/parse_syllabus.py --week <semana> --day <día>
# o:
python3 scripts/parse_syllabus.py --csv <ruta_o_nombre> --week <semana> --day <día>
```

Ejemplos de valores válidos:

- `--week 1 --day 2`
- `--week 0 --day -1`
- `--week 0 --day "-4 y -3"`
- `--week "HITO 01" --day "En Syllabus"` ← comillas si hay espacios

**Incluir skills previas** (modo _smart_ por defecto):

```bash
python3 scripts/parse_syllabus.py \
  --week <semana> \
  --day <día> \
  --include-prior
```

| Flag                      | Efecto                                                         |
| ------------------------- | -------------------------------------------------------------- |
| `--include-prior`         | Modo **smart**: hitos previos + últimas 15 lecciones regulares |
| `--prior-window N`        | Cambia N en modo smart (default `15`)                          |
| `--prior-full`            | Todas las lecciones anteriores                                 |
| `--prior-milestones-only` | Solo hitos previos                                             |

**Buscar por palabra clave:**

```bash
python3 scripts/parse_syllabus.py --search "tailwind"
```

Devuelve `matches` con `week`, `day`, `skill`. Después:

```bash
python3 scripts/parse_syllabus.py --week <w> --day <d> --include-prior
```

**Errores de resolución CSV** (exit code `2`):

```jsonc
{
  "error": "multiple_syllabus_csvs",
  "candidates": ["…/docs/syllabus/A.csv", "…/docs/syllabus/B.csv"],
  "hint": "Ask the user which one…",
}
```

→ **Preguntar al usuario**; no elegir en silencio.

**Salida compacta** (default): JSON en una línea. Para depurar: `--pretty`.
El campo `csv` en el JSON indica qué archivo se usó.

---

## 4. Estructura del output JSON

```jsonc
{
  "csv": "/…/docs/syllabus/New Syllabus AI Engineer - Planificación del programa.csv",
  "current": {
    "week": "1",
    "day": "2",
    "is_milestone": false,
    "skill": "Descripción de la skill a desarrollar",
    "content": "...",
    "how_to_think": "...",
    "best_practices": "...",
    "patterns": "...",
    "anti_patterns": "...",
    "limitaciones": "...",
    "statuses": "En Syllabus | Pendiente evaluación | ...",
  },

  // Solo con --include-prior
  "prior_skills": [
    { "week": "0", "day": "-6", "skill": "...", "is_milestone": false },
  ],
  "prior_skills_meta": {
    "mode": "smart",
    "window": 15,
    "total_prior": 29,
    "returned": 18,
  },
}
```

**Búsqueda** (`--search`):

```jsonc
{
  "csv": "…",
  "query": "tailwind",
  "count": 2,
  "matches": [
    { "week": "3", "day": "12", "skill": "...", "is_milestone": false },
  ],
  "next": "Run --week and --day on a match for full lesson context.",
}
```

Cualquier campo puede ser `null` si el CSV no tiene información para esa celda.

---

## 5. Flujo de trabajo recomendado

```text
1. --list-csvs → si >1 y no especificado: PREGUNTAR al usuario
2. Si semana/día desconocidos: --search "tema" → elegir match → --week/--day
   (o --list)
3. Ejecutar --week X --day Y --include-prior
4. Leer JSON (compacto; no pegarlo entero al usuario):
   a. current.skill / content / how_to_think / practices / patterns /
      anti_patterns / limitaciones
   b. prior_skills → techo de conocimiento (NO adelantar)
5. Generar el contenido solicitado
```

---

## 6. Convenciones del CSV

| Columna | Contenido                                 |
| ------- | ----------------------------------------- |
| 0       | Semana (número) o `HITO XX`               |
| 1       | Día (número, rango, o estado)             |
| 2       | Skill (filas de día) o contenido/proyecto |
| 3       | How to think                              |
| 4       | Best practices                            |
| 5       | Patterns                                  |
| 6       | Anti-patterns                             |
| 7       | Limitaciones                              |

- Varias filas de contenido por día → unidas con `---`.
- Estados comunes: `En Syllabus`, `Pendiente evaluación`, …
- Prework: `week: "0"`, días negativos (`-6` a `-1`).
- Filas `--- SECCIÓN ---` → flush de lección (p. ej. antes de `--- INICIO DEL CURSO ---`).

---

## 7. Casos especiales

**Hitos**

```bash
python3 scripts/parse_syllabus.py --week "HITO 01" --day "En Syllabus"
```

**Días con rango** — `--day` exacto al CSV; usar `--list` si hay duda.

**Varios programas en `syllabus/`** — nunca default silencioso a AI Engineer si hay otro CSV. Preguntar.

---

## 8. Notas para la generación de contenido

1. **Nivel de abstracción** acorde a `how_to_think`.
2. **`limitaciones`** son pedagógicas — respetarlas en ejemplos/ejercicios.
3. **Anti-patrones** — anticiparlos en el material.
4. **`prior_skills`** = techo; no asumir filas posteriores.
5. Estado `Pendiente evaluación` → advertir posible cambio.
