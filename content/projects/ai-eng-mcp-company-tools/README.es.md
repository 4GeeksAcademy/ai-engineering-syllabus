# Servidor MCP: Conectando tu Agente con las Herramientas de la Empresa

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[build by developers](https://4geeks.com)
[4Geeks Academy](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

**Sobre los MCP Servers**

Un MCP Server expone las capacidades de un sistema (herramientas, recursos, prompts) mediante un protocolo estándar que cualquier agente compatible puede descubrir y consumir, sin acoplarse al código interno de tu backend. A diferencia de las tools que ya conectaste directamente al grafo de tu agente, un MCP Server puede ser reutilizado por múltiples clientes — otros agentes, otros equipos, otras compañías del ecosistema — siempre que se autentiquen correctamente. Por eso la autenticación y el principio de mínimo privilegio no son un detalle: un servidor MCP sin auth es una vulnerabilidad real desde el primer día.

Tu agente ya sabe llamar herramientas directamente. Ahora tu tech lead ha abierto un **ticket** pidiendo que esas capacidades dejen de estar hardcodeadas dentro del grafo y se expongan como un servicio independiente, reutilizable y protegido por **OAuth** — y que el propio agente deje de llamar al Incidents Manager de forma directa para consumirlo a través del servidor MCP.

> **De:** Tu tech lead
> **Para:** Tu squad
> **Asunto:** RFP — Servidor MCP para herramientas de la compañía
>
> El agente que construimos ya consulta el Incidents Manager desde dentro del grafo, pero cualquier integración futura (otro agente, otro equipo, un partner externo) tendría que reimplementar esas mismas llamadas. Necesitamos exponerlas como un **MCP Server** independiente, autenticado con **OAuth**, para que cualquier cliente MCP autorizado pueda:
>
> - Gestionar tickets del Incidents Manager (crear, actualizar, consultar estado).
> - Consultar —**nunca editar**— los datos del inventario.
>
> El servidor no debe dar más permisos de los estrictamente necesarios para cada tool. Documenten bien el discovery: cualquier cliente debe poder entender qué puede hacer el servidor sin necesitar contexto humano adicional.
>
> Y no dejen la migración a medias: quiero que el propio agente reemplace su tool directa del Incidents Manager por una llamada al MCP Server como cliente. Si el agente sigue llamando al Incidents Manager por fuera del servidor, el ticket no está resuelto.
>
> Los criterios de aceptación están en el checklist. Avísenme cuando esté listo para probarlo desde un cliente MCP.

Como parte del reto, tu implementación debe resolver — sin que se te diga explícitamente en un checklist — las siguientes decisiones de diseño:

- Qué transporte usar (stdio vs. Streamable HTTP) según si el servidor se consume localmente o por múltiples clientes remotos, y qué implica esa elección para la autenticación.
- Cómo estructurar el sistema de permisos para que la tool de inventario sea, por diseño, de solo lectura — no basta con "no implementar" el endpoint de escritura, el servidor debe rechazar explícitamente cualquier intento.
- Qué información exponer en el discovery (nombres, descripciones y esquemas de las tools) para que un agente externo, sin contexto humano previo, entienda qué puede y qué no puede hacer.
- Cómo reemplazar, dentro del grafo del agente, el nodo que llamaba directamente al Incidents Manager por tools del MCP Server vía `langchain-mcp-adapters` — sin romper el enrutamiento entre RAG y tools que ya tenías funcionando.

---

## 🌱 Cómo Empezar el Proyecto

1. Ubícate en tu copia del [monorepo de la compañía](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) (si aún no tienes tu propio fork, créalo antes de continuar).
2. Trabaja sobre el backend del Incidents Manager y del módulo de inventario que ya construiste en hitos anteriores — el MCP Server se apoya en esos servicios, no los reemplaza.
3. Instala las dependencias necesarias con `uv add` (por ejemplo, `fastmcp`, `langchain-mcp-adapters`) — nunca uses `pip install` directamente en este monorepo.
4. Crea el servidor MCP dentro de `services/`, siguiendo la estructura del resto de servicios del backend.
5. Ubica el nodo del agente que hoy llama directamente al Incidents Manager — es el punto que vas a migrar para que consuma el nuevo MCP Server como cliente en lugar de llamar la API por fuera de él.

---

## 💻 Qué Debes Hacer

**Servidor MCP**

- [ ] Implementar el MCP Server en Python usando FastMCP (u otro SDK MCP equivalente).
- [ ] **Implementar autenticación OAuth** para asegurar el MCP Server — el acceso sin autenticar debe rechazarse.
- [ ] Exponer al menos una tool para gestionar tickets del Incidents Manager (crear, actualizar y consultar estado).
- [ ] Exponer al menos una tool de **solo consulta** sobre el inventario — cualquier intento de modificación debe ser rechazado explícitamente por el servidor, no simplemente omitido.
- [ ] Documentar cada tool con nombre, descripción y esquema de entrada/salida suficientes para que un agente externo la descubra sin contexto humano adicional (`--help`-equivalente vía discovery de MCP).

⚠️ **IMPORTANTE:** Los nombres de campos, IDs de entidad y valores de dominio en tu implementación deben coincidir con las APIs de incidencias e inventario que ya construiste. Una implementación genérica que ignore tus servicios existentes no será aceptada. Los cambios de estado deben pasar por el endpoint de ciclo de vida del Incidents Manager (`PATCH /api/incidents/{id}/status`), no por un `PATCH` genérico sobre el recurso de incidencia. Un MCP Server sin autenticación OAuth no será aceptado.

**Autenticación y seguridad**

- [ ] Proteger el servidor con autenticación **OAuth** — ningún cliente sin access token válido puede listar ni invocar tools. Esto es obligatorio: el MCP Server no debe exponer herramientas de la compañía sin auth.
- [ ] Aplicar el principio de mínimo privilegio: cada tool solo tiene acceso a los datos y operaciones que necesita para cumplir su función.
- [ ] Definir y documentar los códigos de error y de salida esperados ante fallos de autenticación, autorización o validación (no un genérico "error").
- [ ] Registrar en logs cada invocación de tool (qué tool, qué cliente, qué resultado) para trazabilidad.

**Validación (MCP Playground)**

- [ ] Primero, prueba tu servidor MCP en [MCP Playground](https://www.mcpplayground.tech/playground): introduce la URL del servidor, conéctate y ejecuta al menos un flujo completo por cada tool expuesta.
- [ ] Probar y documentar el comportamiento del servidor ante un intento de escritura sobre la tool de inventario (debe fallar de forma controlada y explicable).

**Migración del agente**

- [ ] Conectar el agente LangGraph que ya construiste al MCP Server usando [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters): reemplaza el nodo que llamaba directamente al Incidents Manager por tools cargadas desde el MCP Server.
- [ ] Eliminar (o dejar explícitamente deprecada y sin uso) la implementación anterior de la tool directa — el agente no debe tener dos caminos posibles hacia el Incidents Manager.
- [ ] Confirmar que el enrutamiento existente entre RAG y tools sigue funcionando igual que antes, ahora con el nuevo nodo cliente MCP en el lugar del anterior.

---

## ✅ Qué Vamos a Evaluar

- [ ] El servidor MCP levanta correctamente y expone sus tools mediante el mecanismo de discovery estándar de MCP.
- [ ] Un cliente sin access token OAuth válido no puede listar ni ejecutar ninguna tool.
- [ ] La tool de gestión de tickets crea, actualiza el estado vía `PATCH /api/incidents/{id}/status` y consulta contra el Incidents Manager real de la compañía.
- [ ] La tool de inventario responde correctamente a consultas y rechaza explícitamente cualquier operación de escritura.
- [ ] Cada tool tiene una descripción y un esquema claros, verificables desde el propio discovery del servidor sin leer el código fuente.
- [ ] Los errores de autenticación, autorización y validación devuelven códigos y mensajes distintos entre sí.
- [ ] Existe al menos un log por invocación de tool con cliente, tool y resultado.
- [ ] El agente ya no llama al Incidents Manager de forma directa: toda interacción pasa por el MCP Server como cliente.

---

## 📦 Cómo Entregar

Sigue el flujo estándar de entrega del monorepo: haz push de tu rama, abre un Pull Request hacia tu fork y describe en la descripción del PR qué transporte elegiste y por qué. Avisa a tu tech lead cuando el servidor esté listo para probarse desde un cliente MCP externo.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
