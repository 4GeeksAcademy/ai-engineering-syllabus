# Agente de Soporte con LangGraph — Parte 2 de 2: Herramientas Fuera del RAG

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Esta es la **Parte 2 de 2** y depende directamente de la Parte 1: necesitas el grafo de LangGraph ya compilado, con tracing y evals funcionando, antes de continuar aquí.

Tu agente hoy solo sabe una cosa: buscar en la base de conocimiento del RAG. Pero soporte no vive solo de documentación — vive de datos que cambian todo el tiempo. El **brief** de tu tech lead es directo:

> **De:** Tech Lead
> **Para:** Equipo de Agentes
>
> El RAG que migraron en la Parte 1 responde bien preguntas sobre procedimientos y políticas, pero cuando un agente de soporte pregunta "¿en qué estado está el ticket 482?", el agente inventa una respuesta porque no tiene forma de consultar eso — esa información no vive en la base de conocimiento, vive en el **gestor de incidentes** que ya construimos.
>
> Necesito que le den al agente una tool para consultar el sistema de incidentes en tiempo real. Como extra, si les alcanza el tiempo, otra tool para consultar el **gestor de inventario** también resuelve preguntas frecuentes de soporte ("¿tenemos stock de X?").
>
> **Criterio de aceptación:** el agente debe decidir por sí mismo cuándo la pregunta requiere el RAG y cuándo requiere una tool externa — sin que el usuario tenga que especificarlo.

Dos requisitos quedan implícitos en ese brief y son fáciles de pasar por alto: (1) las tools deben leer de los servicios que **ya construiste** en proyectos anteriores (el gestor de incidentes y, si lo hiciste, el gestor de inventario) — no se simulan datos nuevos ni se inventa un dataset paralelo; y (2) si una tool falla o el servicio no responde, el grafo necesita una ruta explícita de recuperación, no un error que rompa toda la corrida.

### Conocimiento complementario: por qué esto no es "otro RAG"

Es tentador resolver esto indexando los tickets en el mismo vector store del RAG. No lo hagas: los tickets cambian de estado en tiempo real, y el RAG está pensado para conocimiento relativamente estable (políticas, procedimientos). Una **tool** que llama directamente al endpoint del gestor de incidentes siempre te da el dato actual; una copia indexada del ticket queda desactualizada en el momento en que alguien cambia su estado. Esta es la diferencia entre "conocimiento" (RAG) y "datos operativos en vivo" (tool call).

---

## 🌱 Cómo Empezar

1. Confirma que tu servicio del **gestor de incidentes** (`GET /api/incidents`, `GET /api/incidents/{id}`) está corriendo localmente — es el que construiste en un proyecto anterior del monorepo. Si construiste también el **gestor de inventario** (`GET /inventory/products`), tenlo disponible también para el extra.
2. Parte de la rama de la Parte 1 (grafo compilado, con tracing y evals).
3. No necesitas instalar dependencias nuevas más allá de las que ya usas para llamar HTTP desde tu backend.

---

## 💻 Qué Tienes Que Hacer

### Tool obligatoria: consulta de tickets de soporte

- [ ] Define un **contrato tipado** de entrada/salida para la tool (ej. entrada: `ticket_id` o filtros de búsqueda; salida: estado, categoría, origen, fechas — los mismos campos que expone tu API de incidentes).
- [ ] Implementa la tool para que llame a tu servicio existente del gestor de incidentes (`GET /api/incidents` o `GET /api/incidents/{id}`) — nunca datos simulados ni hardcodeados.
- [ ] Agrega al grafo un **nodo** para esta tool y una **arista condicional** que decida cuándo el agente debe usarla en lugar de (o además de) el RAG.
- [ ] Define un **timeout** explícito para la llamada — si el servicio de incidentes no responde a tiempo, el grafo no debe quedar colgado.
- [ ] Define una **ruta de fallback**: si la tool falla o el ticket no existe, el agente responde algo honesto ("no pude confirmar el estado de ese ticket ahora mismo"), nunca inventa un estado.

### Tool extra (opcional): consulta de inventario

- [ ] Si tu empresa tiene un gestor de inventario construido, define el mismo tipo de contrato tipado para consultar stock por producto (`GET /inventory/products`).
- [ ] Aplica las mismas reglas: timeout, fallback ante fallo, sin datos simulados.

### Enrutamiento del agente

- [ ] El agente debe decidir automáticamente, a partir de la pregunta del usuario, si necesita el RAG, una tool, o ambos — sin que el usuario indique explícitamente qué fuente usar.
- [ ] Ninguna tool hace más de una cosa: si te encuentras haciendo que una sola tool "busque tickets o inventario según el caso", sepáralas en dos tools distintas.

### Tracing y evaluación (extendidos desde la Parte 1)

- [ ] El trace de cada corrida debe mostrar con claridad si se usó el RAG, una tool, o ambos, y en qué orden.
- [ ] Agrega al menos 2 evals nuevos que verifiquen el enrutamiento: una pregunta que debe resolverse con una tool (no con el RAG) y una pregunta que debe resolverse con el RAG (no con una tool). Un tercer eval opcional puede verificar el comportamiento de fallback cuando el servicio de incidentes no está disponible.

⚠️ **IMPORTANTE:** Las tools deben leer de los servicios reales que ya construiste (incidentes, e inventario si aplica). Una implementación que simule esos datos en lugar de llamar a tu propio backend no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] La tool de tickets tiene un contrato de entrada/salida tipado y consulta el servicio real del gestor de incidentes.
- [ ] Existe un timeout explícito en la llamada a la tool.
- [ ] Existe una ruta de fallback verificable cuando la tool falla o el recurso no existe — sin respuestas inventadas.
- [ ] El agente enruta correctamente entre RAG y tool(s) según el contenido de la pregunta, sin instrucción explícita del usuario.
- [ ] Cada tool tiene una única responsabilidad (no hay una tool que combine tickets e inventario).
- [ ] El trace de cada corrida permite distinguir qué fuente(s) se usaron y en qué orden.
- [ ] Hay al menos 2 evals nuevos que verifican el enrutamiento correcto entre RAG y tool.
- [ ] (Extra) La tool de inventario, si se implementó, sigue las mismas reglas de contrato, timeout y fallback.

---

## 📦 Cómo Entregar Este Proyecto

Esta es la **Parte 2 de 2**. Se entrega mediante su propio Pull Request, separado del de la Parte 1 — puede partir de esa rama, pero se revisa de forma independiente.

```text
services/
  <agent-service>/               ← nodo(s) y tool(s) nuevas agregadas al grafo de la Parte 1

tests/
  pipelines/                     ← evals de enrutamiento y fallback
```

1. Sube tu rama con la estructura anterior y abre un Pull Request al repositorio original con la etiqueta `parte-2-tools-externas`.
2. Asegúrate de que el PR incluya:
   - El trace de una corrida donde el agente usó la tool de tickets.
   - El trace de una corrida donde el agente usó el RAG (para mostrar el enrutamiento correcto).
   - El resultado de correr los evals nuevos.

---

Este y otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
