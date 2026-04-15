# Construyendo contexto desde un proyecto existente - Dashboard financiero

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

<!-- endhide -->

---

## 🎯 Tu reto

Tu equipo recibe un repositorio que ya tiene una implementación de frontend y backend, pero el handover es incompleto: hay muy poca documentación de producto, casi no existen estándares de código explícitos y no hay un artefacto de memoria del proyecto útil para futuros contribuidores.

En lugar de reconstruir la aplicación, tu misión es usar IA como colaborador técnico para comprender el repositorio, definir reglas de ingeniería y documentar memoria operativa para que el proyecto pueda mantenerse de forma segura. Debes trabajar con evidencia real encontrada en el código, no con suposiciones sobre el comportamiento del producto.

El tech lead definió una secuencia de entrega que debes seguir exactamente:

> **Flujo requerido**
>
> 1. Haz fork del repositorio `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project` y prepara tu entorno local.
> 2. Pídele a tu asistente de IA un resumen del proyecto y valida ese resumen contra la estructura y el código reales.
> 3. Lee el contenido generado por la IA y verifica que esté alineado con tu propia comprensión del repositorio.
> 4. Haz un commit separado por cada paso importante (sin un mega-commit para todo).
> 5. Identifica buenas y malas prácticas de ingeniería en el código y conviértelas en reglas explícitas del proyecto.
> 6. Documenta esas reglas dentro de `.agents/rules` e itera hasta que sean aplicables al flujo real del proyecto.
> 7. Genera una carpeta `memory-bank` con al menos: descripción del producto, stack tecnológico y estado actual del proyecto.

Tu entrega debe leerse como trabajo profesional de mantenimiento de repositorios, no como notas genéricas sin inspección real del código.

---

## 🌱 Cómo iniciar el proyecto

1. Haz fork de este repositorio en tu cuenta de GitHub:
   - `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project`
2. Clona tu fork en local (o ábrelo en GitHub Codespaces).
3. Valida los servicios disponibles:
   - Frontend: `http://localhost:5173`
   - Backend: `http://localhost:8000`
   - Documentación API: `http://localhost:8000/docs`

Si necesitas un recordatorio de setup y entregas, revisa [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### Fase 1 — Comprender el handover

- [ ] Haz fork y clona el repositorio del proyecto.
- [ ] Inspecciona la estructura del repo e identifica carpetas, servicios y entry points clave.
- [ ] Pídele a tu asistente de IA un resumen del proyecto.
- [ ] Lee el resumen generado y verifica que coincida con lo que comprendiste del código real.
- [ ] Valida y corrige el resumen de IA con evidencia directa del código.
- [ ] Crea un commit dedicado para esta fase.

### Fase 2 — Analizar prácticas de ingeniería

- [ ] Revisa el código e identifica al menos 5 buenas prácticas y 5 malas prácticas o riesgos.
- [ ] Agrupa hallazgos por categoría (arquitectura, naming, testing, documentación, DX, etc.).
- [ ] Define un set de reglas propuestas que mitigue riesgos y preserve patrones útiles.
- [ ] Crea un commit dedicado para esta fase.

### Fase 3 — Implementar reglas del repositorio

- [ ] Crea el directorio `.agents/rules` si no existe.
- [ ] Agrega archivos de reglas que reflejen tus estándares propuestos (nombre, alcance y razón claros).
- [ ] Valida cada regla comprobando si realmente puede guiar tareas en este repositorio.
- [ ] Refina reglas ambiguas, demasiado genéricas o desconectadas del flujo real del proyecto.
- [ ] Crea un commit dedicado para esta fase.

### Fase 4 — Construir memoria del proyecto

- [ ] Crea una carpeta `memory-bank` en la raíz del repositorio.
- [ ] Agrega un documento de overview del producto basado en evidencia verificable del repositorio.
- [ ] Agrega un documento de stack tecnológico (frontend, backend, infraestructura/tooling y dependencias clave).
- [ ] Agrega un documento de estado actual (features implementadas, gaps conocidos y siguientes prioridades).
- [ ] Crea un commit dedicado para esta fase.

⚠️ **IMPORTANTE:** No centres tu entrega en explicar la aplicación en profundidad. Enfócala en calidad de comprensión del repositorio, reglas de gobernanza prácticas y artefactos de mantenibilidad.

⚠️ **IMPORTANTE:** Cada fase debe tener su propio commit. Si tu historial tiene un único commit para varias fases, el proyecto está incompleto.

---

## ✅ Qué vamos a evaluar

- [ ] El repositorio fue forkeado correctamente y corrió en local con Docker.
- [ ] El resumen generado por IA existe y fue validado/corregido con evidencia real del código.
- [ ] El historial de commits refleja commits separados por fase.
- [ ] Se identificaron buenas y malas prácticas con ejemplos concretos.
- [ ] Las reglas propuestas están documentadas en `.agents/rules` y son accionables.
- [ ] La validación de reglas demuestra aplicabilidad real al flujo de este proyecto.
- [ ] `memory-bank` existe e incluye descripción del producto, stack y estado actual.
- [ ] La calidad de la documentación es específica, estructurada y conectada con la realidad del repositorio.

> Nota: No se requiere rediseño visual, expansión de features ni refactors mayores, salvo que sean estrictamente necesarios para validar una regla.

---

## 📦 Cómo entregar este proyecto

Haz push de tu fork a GitHub y comparte:

1. URL del repositorio.
2. Historial de commits mostrando un commit por fase.
3. Archivos dentro de `.agents/rules`.
4. Carpeta `memory-bank`.

Sigue cualquier instrucción adicional de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
