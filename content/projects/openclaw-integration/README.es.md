# Mi Asistente 4Geeks — Enseñándole a OpenClaw a seguir tu progreso

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/openclaw-4geeks-assistant/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto.

<!-- endhide -->

---

## 🎯 Tu reto

Llevas ya tiempo en el curso y has llegado a una conclusión: OpenClaw es útil, pero es genérico. No sabe nada sobre tu curso, tus proyectos, tus fechas límite ni cómo estás progresando realmente. Cada vez que quieres revisar tu avance, sales del agente y lo buscas en otro lado — lo cual anula completamente el propósito de tener un asistente personal.

Has decidido cambiar eso. OpenClaw debería conocer tu estado en el curso de 4Geeks de la misma forma en que conoce cualquier otra cosa que le has enseñado: mediante una skill. Concretamente, debería poder conectarse a tu cuenta de 4Geeks usando tu token de estudiante y responder preguntas como _"¿Qué me falta por entregar?"_ o _"¿Qué tan avanzado estoy en el curso?"_ directamente desde la conversación.

La forma en que vas a construir esto es la misma con la que los profesionales abordan cualquier integración agente-API: mediante conversación. Le pedirás a OpenClaw que te ayude a diseñar y crear cada skill, una a la vez, describiendo lo que quieres en lenguaje natural y dejando que el agente guíe la implementación. Sin escribir skills de forma aislada — le enseñas a tu agente lo que necesita hacer, y él te ayuda a que eso ocurra.

> #### Cómo abordar la construcción
>
> - Inicia el proceso diciéndole a OpenClaw exactamente lo que quieres: _"Quiero darte la habilidad de conectarte a mi cuenta de 4Geeks usando mi token de estudiante, sin que tenga que desarrollar código de mi parte. ¿Qué debemos hacer?"_
> - Deja que esa conversación defina la primera skill a construir. Cada nueva pregunta que quieras que responda revela la siguiente skill.
> - Mantén cada skill enfocada en **una acción específica de la API** — nunca combines capacidades no relacionadas.

El resultado no será solo una integración funcional. Será un agente que realmente sabe dónde estás parado, y que se vuelve más útil con el tiempo a medida que le enseñas cosas nuevas.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no requiere hacer fork de un repositorio plantilla. Todo el trabajo ocurre dentro de la configuración de tu OpenClaw.

1. Asegúrate de que tu instancia de OpenClaw esté activa y accesible.
2. Abre una conversación con tu agente.
3. Obtén tu token de estudiante de 4Geeks:
  - Inicia sesión en [learn.4geeks.com](https://learn.4geeks.com).
  - Abre las herramientas de desarrollo de tu navegador y selecciona la pestaña **Application**.
  - En **Storage**, abre **Cookies** y luego selecciona `https://learn.4geeks.com`.
  - Filtra por `4g_tok` y copia su valor.
4. Documenta cada skill que crees y cada conversación que la originó en un archivo llamado `SKILL_LOG.md` — este es tu entregable.

> ⚠️ **IMPORTANTE:** Tu token de estudiante es una credencial. Almacénala usando el mecanismo de configuración segura de OpenClaw — nunca la pegues directamente en un archivo de skill ni la incluyas en un repositorio de código.

**API de estudiantes (BreatheCode)**  
Usa el mapa de endpoints mientras diseñas skills: [Llamadas API (español)](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/openclaw-integration/STUDENT_API_CALLS_REFERENCE.es.md) · [Student API calls (English)](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/openclaw-integration/STUDENT_API_CALLS_REFERENCE.md).

---

## 💻 Qué debes hacer

### Configuración inicial

- [ ] Confirma que tu instancia de OpenClaw está activa y puedes mantener una conversación con ella.
- [ ] Obtén tu token de estudiante de 4Geeks y almacénalo de forma segura en la configuración de OpenClaw (sin hardcodearlo en ninguna skill).

### Conversación de descubrimiento

- [ ] Inicia una conversación con OpenClaw pidiéndole que te ayude a conectarte a la API de 4Geeks usando tu token, sin que tengas que escribir código.
- [ ] Documenta la conversación: ¿qué sugirió OpenClaw? ¿Qué información te pidió? Guarda un resumen en `SKILL_LOG.md`.

### Skills principales (mínimo requerido)

Construye cada una de estas a través de conversación con OpenClaw. Para cada una, documenta: la solicitud en lenguaje natural que hiciste, la skill que OpenClaw te ayudó a crear, y una prueba que demuestre que funciona.

- [ ] **Skill 1 — Autenticar**: OpenClaw puede verificar que el token es válido y que la sesión está activa.
- [ ] **Skill 2 — Obtener mis proyectos**: OpenClaw puede recuperar la lista de proyectos asignados a ti con su estado actual (pendiente, entregado, calificado).
- [ ] **Skill 3 — Obtener trabajo pendiente**: OpenClaw puede decirte específicamente qué te falta completar.
- [ ] **Skill 4 — Obtener resumen de progreso**: OpenClaw puede darte una visión general de cuánto has avanzado en el curso.

### Skills extendidas (al menos 2 adicionales)

- [ ] Identifica al menos 2 cosas más que quisieras que tu agente sepa o haga desde tu cuenta de 4Geeks.
- [ ] Construye esas skills usando el mismo enfoque conversacional.
- [ ] Documéntalas en `SKILL_LOG.md` siguiendo el mismo formato.

### Registro de skills

- [ ] `SKILL_LOG.md` existe y documenta cada skill construida, incluyendo:
  - El prompt en lenguaje natural que usaste para iniciar la conversación
  - Una descripción breve de qué hace la skill y qué endpoint(s) de la API utiliza
  - Un resultado de prueba que demuestre que la skill funciona correctamente

> ⚠️ **IMPORTANTE:** Ninguna skill debe manejar más de una responsabilidad de API. Si una skill está haciendo dos cosas no relacionadas, divídela.

---

## ✅ Qué vamos a evaluar

- [ ] Al menos 4 skills principales están implementadas y funcionan (autenticar, obtener proyectos, obtener trabajo pendiente, obtener resumen de progreso).
- [ ] Al menos 2 skills adicionales construidas en base a necesidades identificadas por el propio estudiante.
- [ ] Cada skill mapea a una acción específica de la API o a un conjunto reducido muy relacionado — sin skills demasiado amplias.
- [ ] El token de estudiante está almacenado de forma segura y nunca hardcodeado en ningún archivo de skill ni en el repositorio.
- [ ] Las skills fueron construidas a través de interacción conversacional con OpenClaw, no diseñadas completamente fuera del agente.
- [ ] `SKILL_LOG.md` documenta cada skill con el prompt inicial, una descripción de lo que hace, y un resultado de prueba.
- [ ] Las skills funcionan correctamente — OpenClaw retorna información precisa desde la API de 4Geeks.

> Nota: La calidad de tu `SKILL_LOG.md` es tan importante como las propias skills. Demuestra tu capacidad para traducir una necesidad real en una capacidad del agente.

---

## 📦 Cómo entregar

Sube tu `SKILL_LOG.md` a tu repositorio personal de GitHub para este proyecto. Comparte la URL del repositorio con tu instructor siguiendo las instrucciones de entrega que te indique.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
