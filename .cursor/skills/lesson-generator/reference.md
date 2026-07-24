# Lesson format reference

Annotated template + a filled skeleton. The canonical format source is the 4Geeks/breatheco lesson:
<https://raw.githubusercontent.com/breatheco-de/content/refs/heads/master/src/content/lesson/performance-and-profiling-in-practice-for-react-native.md>

## Copy-paste template — English (`<slug>.md`)

```markdown
---
title: "Your lesson title in natural sentence case"
description: "One or two sentences describing what the reader will measure, build, or fix. Concrete and outcome-oriented."
author: "USER_PROVIDED"
tags: ["Primary Tech", "Concept", "Tool", "Language"]
---

# 🎯 Your lesson title in natural sentence case

<!-- hide -->

_Estas instrucciones también están disponibles en [español](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/<slug>/<slug>.es.md)._

<!-- endhide -->

A concrete, relatable problem the reader has hit before. Make the pain specific and observable, not abstract.

Reframe: what this lesson gives them and the principle behind it. Set the stakes — why doing this systematically beats guessing.

## 🎯 First core section

Short framing sentence for the section.

### A concrete subsection

Explanation, then a runnable example.

\`\`\`typescript
// realistic, self-contained snippet
export const example = (): boolean => true;
\`\`\`

How to read the result / what to look for.

## Second core section

Teach a fix by showing the problem version first, then the improved version.

\`\`\`python

# before: the problematic pattern

\`\`\`

\`\`\`python

# after: the corrected pattern and why it is better

\`\`\`

![descriptive alt text](PLACEHOLDER_OR_REAL_URL)

## Optional diagram

\`\`\`mermaid
flowchart LR
a[Step] --> b[Next] --> c[Result]
\`\`\`

## <Topic> Checklist

Concrete, verifiable items to run before shipping:

- Item with a measurable threshold (e.g. "no function > 10% of total time").
- Item with an observable signal.
- Item that must pass on a production build, not dev.

## Conclusion

Restate the systematic takeaway. Measure before optimizing; validate after. No new material.
```

## Copy-paste template — Spanish (`<slug>.es.md`)

Same structure. Translate prose + headings + frontmatter `title`/`description`. Keep `author`/`tags` identical. Cross-link points to the English file.

```markdown
---
title: "Tu título de lección en lenguaje natural"
description: "Una o dos frases sobre lo que el lector va a medir, construir o corregir. Concreto y orientado a resultados."
author: "USER_PROVIDED"
tags: ["Primary Tech", "Concept", "Tool", "Language"]
---

# 🎯 Tu título de lección en lenguaje natural

<!-- hide -->

_These instructions are also available in [English](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/<slug>/<slug>.md)._

<!-- endhide -->

Un problema concreto y cercano que el lector ya ha sufrido. Que el dolor sea específico y observable, no abstracto.

Reencuadre: qué le da esta lección y el principio detrás. Deja claro por qué hacerlo de forma sistemática gana a improvisar.

## Primera sección clave

... (misma estructura que el archivo en inglés)

## Checklist de <Tema>

- Ítem con umbral medible.
- Ítem con señal observable.

## Conclusión

Reafirma la idea sistemática. Medir antes de optimizar; validar después.
```

## Style anchors (concrete examples from the source lesson)

- Hook opens with a failure scenario ("works on my machine, lags in production").
- Sections named for the tool/technique, not generic ("Hermes: Your Code Microscope").
- Every technique ends with how to interpret the output / what number means what.
- Fixes shown as before/after code pairs.
- Checklist uses hard thresholds (FPS ≥ 55, request < 500ms p90, images ≤ 5× visual size).
- Conclusion is a principle recap, not a summary of steps.
