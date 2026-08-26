# Construyendo contexto desde un proyecto existente - Dashboard financiero

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

<!-- endhide -->

---

## 🎯 Tu reto

Tu equipo hereda un repositorio que ya tiene frontend y backend. El handover es incompleto: casi no hay documentación de producto, no hay estándares de código explícitos y no hay memoria del proyecto para la siguiente persona (o el siguiente coding agent) que abra el repo.

**No** necesitas conocimiento previo del stack. En Ingeniería de IA a menudo te incorporas a codebases desconocidas. El coding agent es tu investigador principal. Tú lo diriges: pregunta qué hace la app, cómo se conectan las piezas, cómo levantarla y para qué sirven archivos desconocidos. Cada respuesta debe contrastarse con archivos reales — rechaza suposiciones y alucinaciones.

Tu misión no es reconstruir el producto. Tu misión es dejar el repo **listo para agentes**: comprensión validada, reglas accionables que el agent seguirá después, y un `memory-bank` anclado en evidencia.

### Cómo trabajas (en cada fase)

1. Pregunta primero al coding agent.
2. Exige evidencia con rutas/archivos para las afirmaciones importantes.
3. Rechaza puertos, frameworks o APIs inventados.
4. Haz commit de artefactos generados por el agent solo después de verificarlos.
5. Deja un rastro corto de verificación (afirmación incorrecta → corrección) en el mensaje de commit, notas del PR o un `verification.md` pequeño.

### Qué no hacer

- No inventes buenas prácticas de memoria o gusto — derívalas del codebase con el agent.
- No pegues solo este README como prompt y entregues lo que salga sin revisar.
- No centres la entrega en un ensayo largo del producto. Enfócala en contexto verificado, reglas que guían tareas reales y memoria mantenible.

> **Flujo requerido**
>
> 1. Haz fork de `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project` y ábrelo en tu coding agent.
> 2. Pregunta al agent cómo ejecutar el proyecto y qué servicios existen. Arranca solo lo que la evidencia del repo soporte (Docker Compose, scripts, READMEs, config). Confirma URLs y puertos con esa evidencia — no asumas puertos fijos de localhost.
> 3. Pide un resumen del proyecto. Marca cada afirmación importante: ✅ verificada en código / ❌ incorrecta / ❓ sin verificar. Corrige las incorrectas con el agent.
> 4. Un commit por fase mayor (sin un mega-commit para todo).
> 5. Pregunta al agent qué convenciones ya existen y qué riesgos dañarían futuras ediciones del agent. Convierte esos hallazgos en reglas propuestas — cada regla debe mapear al menos a un hecho concreto del repo.
> 6. Haz que el agent redacte archivos de reglas en `.agents/rules`. Pruébalas: dale al agent una tarea pequeña real y comprueba si las reglas dirigen el trabajo. Itera hasta que lo hagan.
> 7. Haz que el agent redacte un `memory-bank` con al menos descripción de producto, stack tecnológico y estado actual. Verifica antes de hacer commit.

La entrega debe leerse como stewardship profesional del repositorio impulsado por colaboración con el agent — no como notas genéricas sin inspección del código.

---

## 🌱 Cómo iniciar el proyecto

1. Haz fork de este repositorio en tu cuenta de GitHub:
   - `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project`
2. Clona tu fork en local (o ábrelo en GitHub Codespaces).
3. Abre el proyecto en tu coding agent y pregunta cómo levantar los servicios y cómo confirmar que están sanos. Sigue la evidencia del repo (compose, Dockerfiles, scripts de package, docs).

Si necesitas un recordatorio de setup y entregas, revisa [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project).

> **Tip:** Puedes encontrar errores de entorno (permisos, mounts, herramientas faltantes). Pega el error exacto en el agent y pide un arreglo paso a paso anclado a este repo.

---

## 💻 Qué debes hacer

### Fase 1 — Comprender el handover (con el agent)

- [ ] Haz fork y clona el repositorio del proyecto.
- [ ] Pide al agent mapear estructura, servicios y entry points — luego comprueba tú mismo rutas clave.
- [ ] Pide un resumen del proyecto (qué hace, cómo se conecta, cómo se ejecuta).
- [ ] Verifica el resumen contra el código real; marca ✅ / ❌ / ❓ y corrige desajustes con el agent.
- [ ] Deja un rastro corto de verificación (mensaje de commit, notas de PR o `verification.md`).
- [ ] Crea un commit dedicado para esta fase.

### Fase 2 — Derivar hallazgos de ingeniería (con el agent)

- [ ] Pide al agent que saque a la luz convenciones útiles y patrones arriesgados que afectarían a futuros contribuidores o agents.
- [ ] Quédate solo con hallazgos ligados a archivos, carpetas o comportamientos concretos — descarta frases vagas.
- [ ] Agrupa los hallazgos que sobrevivan por categoría (arquitectura, naming, testing, documentación, DX, etc.).
- [ ] Conviértelos en un set de reglas propuestas: cada regla cita al menos un hecho del repo.
- [ ] Crea un commit dedicado para esta fase (notas de análisis / reglas propuestas están bien aquí).

### Fase 3 — Implementar y probar reglas del repositorio

- [ ] Crea `.agents/rules` si no existe.
- [ ] Haz que el agent redacte archivos de reglas (nombre, alcance, justificación y guía específica del proyecto claros).
- [ ] Valida cada regla con una tarea pequeña real en este repo (cambio de docs, higiene de commits, ajuste de frontend, cambio de ruta de backend — lo que encaje). Refina con el agent hasta que la guía sea accionable.
- [ ] Crea un commit dedicado para esta fase.

### Fase 4 — Construir memoria del proyecto

- [ ] Crea una carpeta `memory-bank` en la raíz del repositorio (los nombres de archivo pueden seguir la convención del agent/repo).
- [ ] Asegura que cubra, como mínimo:
  - Overview del producto anclado en evidencia verificable
  - Stack tecnológico (lenguajes, frameworks, infra/tooling, dependencias clave)
  - Estado actual (qué funciona, gaps conocidos, siguientes prioridades)
- [ ] Rechaza claims de producto sin soporte o roadmaps inventados.
- [ ] Crea un commit dedicado para esta fase.

⚠️ **IMPORTANTE:** Cada fase listada debe tener su propio commit. Un único commit para varias fases = incompleto.

---

## ✅ Qué vamos a evaluar

- [ ] Repo forkeado y ejecutable usando el setup que el agent descubrió a partir de la evidencia del proyecto.
- [ ] Existe un resumen generado por IA y fue verificado/corregido contra el código real (hay rastro de verificación).
- [ ] El historial de commits muestra commits separados por fase.
- [ ] Los hallazgos de ingeniería citan evidencia concreta; las reglas propuestas mapean a esos hallazgos.
- [ ] `.agents/rules` contiene reglas accionables y específicas del proyecto (no eslóganes genéricos).
- [ ] La validación de reglas muestra que dirigen una tarea real en este repositorio.
- [ ] `memory-bank` cubre producto, stack y estado actual, ligado a la realidad del repositorio.
- [ ] Los artefactos se leen como stewardship asistido por agent que tú verificaste — no pegado sin revisar ni listas de preferencia personal.

> Nota: No se requiere rediseño visual, expansión de features ni refactors mayores, salvo que sean estrictamente necesarios para validar una regla.

---

## 📦 Cómo entregar este proyecto

Haz push de tu fork a GitHub y comparte:

1. URL del repositorio.
2. Historial de commits mostrando un commit por fase.
3. Archivos dentro de `.agents/rules`.
4. Carpeta `memory-bank`.
5. Rastro de verificación (en commits, notas de PR o `verification.md`).

Sigue cualquier instrucción adicional de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
