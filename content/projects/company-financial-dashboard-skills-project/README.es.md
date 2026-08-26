# Mejorando el desarrollo con skills de agentes - Dashboard financiero

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo iniciar un proyecto de código.

<!-- endhide -->

---

## 🎯 Tu reto

Continúas en el **mismo dashboard financiero heredado** del proyecto de contexto. Ya lo dejaste listo para agentes: un `memory-bank` verificado, reglas en `.agents/rules` y un setup local que descubriste con tu coding agent.

La app funciona. Los datos cargan, los gráficos se renderizan. Tu tech lead revisó tu trabajo de stewardship y dejó un comentario:

> _"Buena base. Antes de hacer merge de los próximos cambios, sube el nivel en dos frentes: accesibilidad y buenas prácticas de despliegue. Te comparto dos skills que puedes cargar directamente en tu coding agent — guiarán la auditoría y las correcciones sin que memorices cada regla. Una vez aplicadas, explora el ecosistema de skills y mira qué encaja en este repo. Luego captura una skill interna que el equipo reutilizará aquí — commits, despliegue, testing, o algo específico de este dashboard. Documenta lo que aprendiste."_

Los equipos profesionales escalan calidad así: paquetes de instrucciones reutilizables cargados en agentes, aplicados de forma consistente sobre codebases heredadas — no checklists copiados de memoria.

**Stack-agnostic se refiere a tu conocimiento previo, no al stack del proyecto.** Este dashboard tiene un stack predefinido — lo documentaste en el `memory-bank` del proyecto de contexto. Las skills asignadas (`accessibility`, `vercel-react-best-practices`) encajan con ese stack. **No** necesitas conocer ya Next.js, patrones de despliegue en Vercel ni APIs de accesibilidad. Carga la skill, deja que el agent la aplique y verifica resultados en la app en ejecución y en el build.

El agent aplica la skill; tú diriges, verificas resultados contra la evidencia del repo y rechazas cambios que no encajen con lo que la skill y el codebase soportan.

### ¿Qué es una skill para un agente?

Una skill para un agente es un conjunto de instrucciones estructuradas y autocontenidas que le dice al coding agent _cómo_ realizar una tarea específica — qué buscar, qué patrones aplicar, qué evitar y cómo verificar el resultado. Las skills son componibles: combina varias skills pequeñas y enfocadas para una mejora compuesta sin un prompt masivo.

El ecosistema en [skills.sh](https://skills.sh) aloja skills mantenidas por la comunidad listas para cargar. **Una skill solo es tan buena como la claridad con la que define objetivo, inputs, outputs y criterios de aceptación.** Hoy lo experimentarás — también cuando escribas la tuya.

### Cómo trabajas (en cada fase)

1. Carga la skill, luego deja que el agent audite y proponga cambios — no corrijas a mano solo siguiendo este README.
2. Pide al agent que cite archivos y explique cada cambio antes de aceptarlo.
3. Verifica resultados en la app en ejecución y con el comando de build/test que documente tu `memory-bank` o los scripts del repo.
4. Mantén los cambios trazables a una skill (mensaje de commit o notas del PR).
5. Actualiza el `memory-bank` cuando cambie la línea base de calidad o el flujo de trabajo del repo.

> Tu tech lead ha compartido las siguientes instrucciones:
>
> #### Accesibilidad (`accessibility`)
>
> Aplica la skill `accessibility` al dashboard. Objetivo: personas que usan tecnologías de asistencia — lectores de pantalla, navegación por teclado, modos de alto contraste — puedan usar el producto sin fricción. La skill guía al agent para auditar y corregir problemas comunes: atributos `aria-label` faltantes, gestión deficiente del foco, texto `alt` ausente y elementos interactivos con bajo contraste.
>
> #### Vercel + React Best Practices (`vercel-react-best-practices`)
>
> Aplica la skill `vercel-react-best-practices`. Cubre patrones listos para despliegue: uso correcto de `next/image`, `next/font`, evitar layout shift, metadatos correctos por página y anti-patrones que afectan los scores de Lighthouse en despliegues de Vercel.
>
> #### Explorar el ecosistema
>
> Para descubrir qué más está disponible sin adivinar nombres, ejecuta:
>
> ```bash
> npx skills find <tema>
> ```
>
> Por ejemplo: `npx skills find forms`, `npx skills find performance`, `npx skills find seo`. Revisa lo que aparece y decide si alguna skill vale la pena aplicar a este proyecto.

Terminarás con un codebase mejorado, al menos una skill comunitaria adicional aplicada y **una skill interna del proyecto** que el equipo pueda recargar en este repo.

---

## 🌱 Cómo iniciar el proyecto

Continúa en el **mismo repositorio** del proyecto de contexto. No hagas fork de un nuevo repo.

1. Abre tu fork del dashboard financiero ([**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) en tu coding agent.
2. Confirma que `memory-bank/` y `.agents/rules` del proyecto de contexto están commiteados y actualizados.
3. Pide al agent que confirme cómo ejecutar la app y qué comando de build valida el frontend — usa evidencia del repo, no suposiciones.
4. Haz pull de los últimos cambios si trabajas en equipo: `git pull origin main`.
5. Crea una rama: `git switch -c feature/agent-skills`.

Si necesitas repasar la configuración: [cómo iniciar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### 1. Descubrir y cargar las skills proporcionadas

- [ ] Ejecuta `npx skills find accessibility` y revisa qué cubre la skill antes de aplicarla.
- [ ] Ejecuta `npx skills find vercel-react-best-practices` y revísala.
- [ ] Carga ambas skills en tu coding agent y lee qué instrucciones le dan al agent.

### 2. Aplicar la skill `accessibility` (agent al mando, tú verificas)

- [ ] Con la skill cargada, pide al agent que audite el dashboard y proponga correcciones.
- [ ] Revisa cada propuesta; acepta solo cambios que puedas ligar a un archivo real e instrucción de la skill.
- [ ] Verifica resultados: accesibilidad por teclado en elementos interactivos, `aria-*` / `role` correctos donde haga falta, `alt` en imágenes/iconos, contraste básico en textos y controles.
- [ ] Commit con mensaje que referencie la skill `accessibility`.

### 3. Aplicar la skill `vercel-react-best-practices` (agent al mando, tú verificas)

- [ ] Con la skill cargada, pide al agent que audite patrones frontend orientados a despliegue y aplique correcciones.
- [ ] Revisa propuestas contra la skill — p. ej. `next/image` donde corresponda, metadata de página, anti-patrones de layout shift y fuentes que la skill señale.
- [ ] Ejecuta el comando de build del frontend documentado en este repo; confirma que pasa sin advertencias nuevas injustificadas.
- [ ] Commit con mensaje que referencie la skill `vercel-react-best-practices`.

### 4. Explorar el ecosistema

- [ ] Ejecuta `npx skills find <tema>` sobre al menos dos temas relevantes (p. ej. `performance`, `seo`, `forms`, `typescript`, `testing`).
- [ ] Aplica al menos una skill adicional que consideres valiosa. Justifica la elección en el memory bank o notas del PR.

### 5. Escribir una skill interna del proyecto

- [ ] Con el agent, identifica un gap **específico de este repo heredado** que las skills comunitarias no cubren bien — p. ej. convenciones de commits, pasos de despliegue de este dashboard, checks de testing/QA antes del merge, reglas de formateo de datos, patrones de uso de API o convenciones UI del dashboard descubiertas en el codebase.
- [ ] Haz que el agent redacte el archivo de skill; tú lo refinas a la estructura de clase: objetivo claro, inputs definidos, output esperado, criterios de aceptación.
- [ ] Guárdalo en `.skills/` y cárgalo en el agent para verificar que produce guía accionable en una tarea real de este repo.

### 6. Actualizar el memory bank

- [ ] Actualiza `memory-bank/progress.md` (o equivalente) con: skills aplicadas, cambios verificados, skill del ecosistema elegida (y por qué) y la skill interna que creaste.

⚠️ **IMPORTANTE:** No reescribas el dashboard desde cero. Mejora dirigida vía skills — cada cambio trazable a una instrucción de skill. Tú verificas; el agent implementa.

---

## ✅ Qué vamos a evaluar

- [ ] Las skills `accessibility` y `vercel-react-best-practices` fueron cargadas y aplicadas — mejoras visibles y trazables a las instrucciones de cada skill.
- [ ] Resultados de accesibilidad verificados: navegación por teclado funciona, atributos `aria-*` correctos donde haga falta, `alt` presente, contraste pasa comprobaciones básicas.
- [ ] El build del frontend pasa usando el comando documentado en este repo, sin advertencias nuevas injustificadas.
- [ ] Al menos una skill adicional descubierta con `npx skills find` y aplicada con justificación escrita.
- [ ] Existe una skill interna en `.skills/`, bien estructurada (objetivo, inputs, outputs, criterios de aceptación), con guía **específica del proyecto** — commits, despliegue, testing/QA u otro tema derivado del repo; no relleno genérico.
- [ ] El memory bank refleja con precisión el trabajo de la sesión.
- [ ] Cambios en `feature/agent-skills` con commits claros — lo ideal es un commit por skill aplicada.
- [ ] El trabajo se lee como mejora impulsada por agent sobre un codebase heredado que tú verificaste — no ediciones masivas sin revisar.

> **Nota:** La calidad de la skill interna se evalúa por claridad y especificidad, no por longitud. Una skill corta y precisa vale más que una larga y vaga.

---

## 📦 Cómo entregar

Sube tu rama de feature a GitHub y abre un pull request contra `main`. Comparte la URL del pull request con tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
