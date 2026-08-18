# Dale memoria a tu agente

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/openclaw-memory/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Llevas varias semanas trabajando con Openclaw: le has creado skills y has conectado integraciones. Es útil, pero tiene un problema: cada vez que inicias una nueva sesión, olvida todo. No sabe tu nombre, no conoce tus proyectos en curso, no recuerda tus preferencias ni lo que estabas haciendo ayer.

Eso hay que arreglarlo.

Tu tarea es identificar una **necesidad personal real** — algo que genuinamente quieras que tu agente recuerde o rastree entre sesiones — e implementar el tipo de memoria adecuado para esa necesidad. No todo requiere la misma solución: guardar tu estilo de código preferido es diferente a llevar un diario de trabajo diario, que a su vez es diferente a hacer que el agente recuerde hechos sobre tus proyectos en curso.

Antes de escribir una sola línea de configuración, deberías poder responder: *¿Qué necesita recordar mi agente y por qué este tipo de memoria es la opción correcta para este caso concreto?*

> La arquitectura de memoria de tu agente debe satisfacer los siguientes requisitos:
>
> #### Contexto persistente
>
> - Un archivo `Memory.md` que defina quién eres: tu nombre, rol, preferencias de trabajo y cualquier regla que el agente deba seguir siempre.
>
> #### Notas episódicas
>
> - Al menos una entrada dentro de la carpeta `/memory` — una nota diaria o registro estructurado que capture algo que ocurrió en tu sesión de trabajo (una tarea completada, una decisión tomada, un recurso encontrado).
>
> #### Recuperación más inteligente
>
> - QMD configurado como método de búsqueda en memoria, reemplazando el `memory_search` por defecto. Tu configuración debe incluir búsqueda por keyword, similitud semántica y reranking activados.
>
> #### Decisión de arquitectura justificada
>
> - Una nota breve (dentro de `Memory.md` o como `MEMORY_DESIGN.md` separado) que explique por qué elegiste esta arquitectura para tu caso de uso personal, y qué te daría una alternativa más avanzada como `mem0` que esta configuración no ofrece.

Elige un escenario que sea genuinamente tuyo. No inventes un caso de uso falso — piensa en lo que realmente haces. Aquí tienes algunos ejemplos para inspirarte:

- **Seguimiento del progreso del curso:** El agente sabe en qué módulo estás, cuántos proyectos tienes pendientes y cuáles ya completaste — y puede abrir cada sesión diciéndote si vas bien encaminado o si te has retrasado.
- **Registro de decisiones diarias:** El agente recuerda las decisiones técnicas que tomaste esta semana (por qué elegiste una librería sobre otra, qué probaste que no funcionó) para que no repitas la misma investigación dos veces.
- **Gestor de referencias:** El agente recuerda los enlaces, documentos y recursos que le has compartido, y puede recuperar los relevantes cuando preguntas sobre un tema.
- **Contexto de proyecto paralelo:** El agente mantiene el estado actual de un proyecto personal — qué está construido, qué está roto, cuál es el siguiente paso — sin que tengas que re-explicarlo en cada sesión.

Una necesidad real produce una implementación mejor.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto se construye sobre tu configuración de Openclaw existente de lecciones anteriores. No necesitas hacer fork de un nuevo repositorio — trabaja directamente en tu directorio de configuración de Openclaw.

1. Abre tu workspace de Openclaw en tu entorno local o en Codespace.
2. Si necesitas un punto de partida limpio o quieres revisar la configuración base, consulta el repositorio que creaste en la Semana 2 Día 6.
3. Crea una nueva rama para este proyecto: `git switch -c feature/memory-setup`
4. ¿Necesitas un recordatorio sobre cómo estructurar un proyecto? [Lee la guía](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### Diseño de memoria

- [ ] Escribe un archivo `MEMORY_DESIGN.md` (o una sección dedicada al inicio de `Memory.md`) que:
  - [ ] Describa tu caso de uso personal en un párrafo (qué quieres que el agente recuerde y por qué)
  - [ ] Justifique el o los tipos de memoria elegidos
  - [ ] Explique brevemente qué ofrece `mem0` y por qué decidiste usarlo o no para este caso

### Memory.md — contexto persistente

- [ ] Crea o actualiza `Memory.md` con al menos:
  - [ ] Tu nombre y una breve descripción de tu contexto de trabajo (rol, proyectos actuales)
  - [ ] Al menos 3 reglas de comportamiento para el agente (p. ej., idioma preferido, estilo de respuesta, cosas que siempre o nunca debe hacer)
  - [ ] Una sección de contexto específico del proyecto relevante para tu caso de uso

### Carpeta /memory — notas episódicas

- [ ] Crea al menos 2 entradas en la carpeta `/memory` siguiendo una convención de nombres consistente (p. ej., `YYYY-MM-DD-tema.md`)
- [ ] Cada entrada debe tener un formato estructurado: fecha, contexto, hechos o decisiones clave, y acciones pendientes

### Configuración de QMD

- [ ] Instala y configura QMD como método de búsqueda de memoria en Openclaw
- [ ] Verifica que los tres modos de recuperación estén activos: búsqueda por keyword, similitud semántica y reranking
- [ ] Ejecuta al menos una consulta manual sobre tu carpeta `/memory` y documenta el resultado en tu `MEMORY_DESIGN.md`

### Verificación

- [ ] Inicia una nueva sesión de Openclaw y confirma que el agente recuerda correctamente al menos dos datos de `Memory.md`
- [ ] Hazle al agente una pregunta que deba activar una búsqueda en la carpeta `/memory` y verifica que la recuperación funciona

⚠️ **IMPORTANTE:** No uses `mem0` como solución principal de memoria en este proyecto a menos que puedas justificar claramente por qué la arquitectura más sencilla es insuficiente para tu caso de uso. El objetivo es hacer coincidir la herramienta correcta con el problema, no usar la opción más compleja disponible.

---

## ✅ Qué vamos a evaluar

- [ ] `Memory.md` existe y contiene contexto personal estructurado y significativo (sin texto de placeholder)
- [ ] Existen al menos 2 entradas episódicas en `/memory` con formato consistente y contenido real
- [ ] QMD está correctamente configurado y reemplaza la búsqueda de memoria por defecto
- [ ] Una prueba de recuperación manual está documentada con la consulta utilizada y el resultado obtenido
- [ ] `MEMORY_DESIGN.md` (o sección equivalente) explica el caso de uso y justifica la elección de arquitectura con razonamiento claro
- [ ] El agente recuerda correctamente el contexto de `Memory.md` en una sesión nueva (demostrado con captura de pantalla o log)
- [ ] El nombre de la rama sigue la convención `feature/memory-setup`

> Nota: No se evalúa la calidad de la integración de `mem0`. Lo que importa es la justificación sobre si usarlo o no.

---

## 📦 Cómo entregar

Sube tu rama `feature/memory-setup` a tu repositorio de GitHub y comparte el enlace siguiendo las instrucciones de tu instructor. Incluye una captura de pantalla o un log de terminal que muestre al agente recordando información en una sesión recién iniciada.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
