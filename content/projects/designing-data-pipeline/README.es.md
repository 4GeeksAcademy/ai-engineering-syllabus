# Diseñando un Data Pipeline: del dato crudo a los reportes confiables

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeks.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto.

<!-- endhide -->

---

## 🎯 Tu reto

**Veridian Logistics** es una empresa de transporte de carga mediana que gestiona operaciones en cinco hubs regionales. Su equipo de operaciones exporta cada noche un reporte de actividad diaria desde su sistema de gestión de flota — despachos, confirmaciones de entrega, cambios de ruta y actualizaciones de estado de vehículos llegan todos en el mismo archivo CSV plano.

El problema: el archivo mezcla registros nuevos con actualizaciones de registros ya existentes. Cuando el estado de un paquete cambia (por ejemplo, de _en tránsito_ a _entregado_), el sistema genera una fila nueva en lugar de modificar la original. Con el tiempo, los archivos exportados empezaron a mostrar el mismo envío varias veces en distintas etapas del ciclo de vida — lo que significa que cualquier pipeline que cargue estos registros sin procesarlos termina acumulando duplicados y calculando métricas incorrectas.

La CTO te ha pedido que diseñes un pipeline de datos que maneje correctamente esta información antes de que llegue a cualquier tabla de reportes. No necesita una implementación todavía — necesita un **documento de diseño** que su equipo pueda revisar, cuestionar y luego entregar a un ingeniero para que lo construya. Tú eres el ingeniero de datos responsable de la arquitectura.

> Tu tech lead ha compartido el siguiente brief:
>
> #### Documento de diseño del pipeline — Veridian Logistics
>
> Produce un archivo `PIPELINE_DESIGN.md` que documente la arquitectura del pipeline ETL. El documento debe responder:
>
> - **Propósito**: ¿Qué problema de negocio resuelve este pipeline? ¿Cuáles son los datos de salida?
> - **Análisis del formato de datos**: El export actual es CSV. ¿Es el formato adecuado para este caso? ¿Habría algún formato más conveniente a escala?
> - **Diagrama de flujo de datos**: Un diagrama visual de cada etapa desde la fuente hasta el destino — extracción, transformación, carga y cualquier paso intermedio.
> - **Estrategia de deduplicación**: La fuente actualiza registros insertando nuevas filas. ¿Cómo detectará el pipeline duplicados y cómo los resolverá?
> - **Plan de idempotencia**: Si el pipeline falla a mitad de la fase de carga, ¿cómo se recupera la siguiente ejecución sin corromper ni cargar de nuevo los datos ya procesados?
> - **Especificación del log de ejecución**: ¿Qué campos mínimos debe registrar cada ejecución del pipeline para poder auditarlo en producción?
> - **Criterios de robustez**: ¿Qué diferencia a un pipeline que simplemente funciona de uno preparado para producción? Menciona al menos tres características concretas.

Este es un ejercicio de diseño previo a la implementación. No se escribe código. El entregable es un documento de planificación suficientemente riguroso para que otro ingeniero pueda implementarlo desde cero.

Piensa con cuidado en cada decisión — las elecciones de formato, almacenamiento y manejo de fallos tienen costos y beneficios. Tu documento debe demostrar que entiendes _por qué_ se toma cada decisión, no solo cuál es.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no requiere un repositorio de partida — la entrega es exclusivamente un documento de diseño.

1. Crea un nuevo repositorio en GitHub para este proyecto (por ejemplo, `veridian-pipeline-design`).
2. Clónalo en tu máquina local o ábrelo en un GitHub Codespace.
3. Crea el archivo `PIPELINE_DESIGN.md` en la raíz del repositorio y empieza tu diseño ahí.

Puedes usar [este editor de Mermaid](https://waficmikati.github.io/mermaid/) para construir e incrustar tu diagrama de flujo de datos.

---

## 💻 Qué debes hacer

### Fase 1 — Entender el escenario

- [ ] Lee el brief con atención e identifica las restricciones clave: registros mezclados (inserts + updates), export nocturno en CSV, operación multi-hub.
- [ ] Lista las preguntas que le harías al cliente antes de diseñar cualquier cosa (mínimo tres).

### Fase 2 — Diseñar la arquitectura del pipeline

- [ ] Crea `PIPELINE_DESIGN.md` en la raíz del proyecto.
- [ ] Escribe una sección de **Propósito** explicando qué problema resuelve el pipeline y cuáles son sus salidas.
- [ ] Escribe una sección de **Análisis del formato de datos**. Evalúa el formato CSV actual: ¿cuándo funciona bien, cuándo se queda corto? ¿Recomendarías una alternativa (p. ej. JSON, Parquet) en alguna etapa del pipeline? Justifica tu respuesta.
- [ ] Crea un **Diagrama de flujo de datos** que muestre cada etapa: fuente → extracción → transformación → carga → destino. Etiqueta cada etapa y anota las decisiones clave (p. ej. "la deduplicación ocurre aquí").
- [ ] Escribe una sección de **Estrategia de deduplicación**. Explica cómo el pipeline identifica y resuelve los registros duplicados de una fuente que actualiza insertando nuevas filas.
- [ ] Escribe una sección de **Plan de idempotencia**. Describe qué ocurre si el pipeline falla a mitad de la fase de carga y cómo se recupera la siguiente ejecución sin corromper los datos.
- [ ] Escribe una sección de **Especificación del log de ejecución**. Define los campos mínimos que debe registrar cada ejecución del pipeline (p. ej. ID de ejecución, hora de inicio, filas extraídas, filas cargadas, estado, errores).
- [ ] Escribe una sección de **Criterios de robustez**. Nombra al menos tres características concretas que diferencien a un pipeline production-ready de uno que "simplemente funciona".

### Fase 3 — Revisión y commit

- [ ] Relee el documento como si fueras otro ingeniero que nunca vio el escenario. ¿Están explicadas todas las decisiones?
- [ ] Haz commit de `PIPELINE_DESIGN.md` con el mensaje: `feat: add pipeline design document`.

⚠️ **IMPORTANTE:** Este proyecto **no requiere implementación de código**. No incluyas scripts de Python, migraciones de base de datos ni código ETL funcional. El entregable es exclusivamente el documento de diseño `PIPELINE_DESIGN.md`.

---

## ✅ Qué vamos a evaluar

- [ ] `PIPELINE_DESIGN.md` está presente, commiteado y completo.
- [ ] La sección de propósito define claramente el problema de negocio y los datos de salida esperados.
- [ ] El análisis de formato de datos incluye una recomendación justificada — no solo una descripción de los formatos.
- [ ] El diagrama de flujo de datos cubre todas las etapas del pipeline y es legible.
- [ ] La estrategia de deduplicación responde a la restricción específica del escenario (updates como inserts), no al caso genérico.
- [ ] El plan de idempotencia explica un mecanismo de recuperación concreto (p. ej. tablas de staging, lógica de upsert, checkpointing).
- [ ] La especificación del log incluye al menos cinco campos concretos con justificación para cada uno.
- [ ] Los criterios de robustez son específicos y accionables — no cualidades genéricas como "buen código".
- [ ] Las decisiones a lo largo del documento incluyen razonamiento de trade-offs, no solo conclusiones.

> Nota: La calidad del diagrama y la profundidad técnica de cada sección importan más que la extensión del documento. Un documento corto y preciso con razonamiento claro supera a uno largo con respuestas vagas.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace según las instrucciones de tu instructor. Asegúrate de que `PIPELINE_DESIGN.md` esté commiteado en la rama principal antes de entregar.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeks.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeks.com/es/comparar-programas) de [Ingeniería de IA](https://4geeks.com/es/programas-de-carrera/ingenieria-ia) y [Agentes y Automatizaciones con IA](https://4geeks.com/es/programas-de-carrera/agentes-y-automatizaciones-con-inteligencia-artificial).
