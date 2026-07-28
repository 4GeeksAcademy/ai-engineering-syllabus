# Prácticas Seguras en la Integración de IA en Sistemas

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/cybersecurity-analysis)** antes de escribir código — define el marco regulatorio, los datos de la compañía y las restricciones específicas de tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya construiste agentes que clasifican, responden y escalan solicitudes; les diste memoria; los conectaste a herramientas externas mediante MCP; y expusiste actualizaciones en tiempo real al dashboard. Todo eso funciona — pero nadie ha verificado todavía si es seguro correrlo en producción. Tu líder de compliance ha abierto un **ticket** pidiendo una auditoría formal antes de que el sistema siga creciendo.

El **brief** es directo: no se trata solo de "que funcione", sino de demostrar que cada componente que toca un modelo de lenguaje — endpoints, agentes, integraciones con terceros — sigue principios de seguridad por diseño y puede sostenerse frente a un marco de referencia reconocido. Tu tech lead fue igual de específico en el **handoff**: la entrega no es únicamente un informe, es también la corrección de al menos las brechas más críticas que ese informe identifique.

> **De:** Responsable de Compliance
> **Para:** Equipo de Ingeniería de IA
>
> **Contexto:** Nuestros sistemas de IA han crecido rápido — agentes, RAG, MCP, workflows con aprobación humana — pero nunca hicimos una revisión de seguridad formal de conjunto. Antes de seguir escalando, necesitamos saber dónde estamos parados.
>
> **Qué necesito:** Un inventario de todos los sistemas de IA de la compañía, un informe estructurado según el checklist de NIST (Govern, Identify, Protect, Detect, Respond, Recover) con una ruta de mejoras priorizada, y la implementación de las protecciones más urgentes — especialmente frente a prompt injection y manejo de secretos.
>
> **Acceptance criteria:** El informe cubre las seis funciones de NIST con al menos una acción concreta por función; el inventario de sistemas de IA está completo y con responsable asignado por componente; las protecciones implementadas se pueden demostrar con un caso de prueba reproducible.

### 📎 Conocimiento complementario: el framework NIST

NIST organiza la gestión de ciberseguridad en seis funciones: **Govern** (política y responsabilidades), **Identify** (inventario y evaluación de riesgo), **Protect** (controles preventivos), **Detect** (monitoreo y alertas), **Respond** (plan de incidentes) y **Recover** (restauración de servicio). No necesitas implementar las seis a nivel enterprise — necesitas mapear tu sistema actual contra cada función y priorizar lo que falta. Es la misma lógica de un checklist de calidad, aplicada a seguridad.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz un `git pull` de tu fork del monorepo y crea una rama nueva para este trabajo.
2. Lee tu `CONTEXT-empresa.md` para identificar el marco regulatorio aplicable a tu compañía y los sistemas de IA que ya construiste en milestones anteriores.
3. Revisa `.env.example` y confirma cómo se gestionan actualmente tus credenciales y API keys.
4. Antes de tocar código, dibuja o lista (en el README de tu propio informe) todos los puntos donde un modelo de lenguaje recibe input externo — de un usuario, de un documento en tu base de conocimiento semántica, o de una herramienta MCP.

---

## 💻 Qué Necesitas Hacer

**Inventario y gobierno**

- [ ] Documenta un inventario completo de los sistemas de IA de la compañía construidos hasta ahora (agentes, RAG, MCP, workflows), con responsable asignado por componente.
- [ ] Identifica, para cada componente, quién es responsable del control cuando el modelo o la herramienta la provee un tercero.

⚠️ **IMPORTANTE:** El marco regulatorio aplicable (qué normativa rige, qué plazos de notificación aplican, qué datos están restringidos) depende de tu CONTEXT.md. Un informe genérico que ignore el contexto de tu compañía no será aceptado.

**Seguridad por diseño (backend y agentes)**

- [ ] Verifica y corrige el manejo de credenciales: ninguna API key o secreto debe estar hardcodeado en el código; todo debe venir de variables de entorno o un vault.
- [ ] Implementa validación y sanitización explícita de cualquier input de usuario antes de que llegue al modelo.
- [ ] Separa claramente las instrucciones de sistema del contenido del usuario en tus prompts, de forma que el contenido de usuario nunca pueda sobrescribir las instrucciones.
- [ ] Si algún agente lee contenido externo (documentos de tu base de conocimiento, resultados de herramientas MCP), documenta y mitiga el riesgo de prompt injection indirecta.
- [ ] Si algún componente genera código, SQL o llamadas a herramientas, agrega una capa de validación de ese output antes de ejecutarlo.
- [ ] Implementa rate limiting sobre al menos un endpoint que dispare llamadas a un modelo, para evitar loops de costo descontrolado.
- [ ] Agrega logging y trazabilidad de qué acción tomó cada agente y por qué, para al menos un flujo agentic existente.
- [ ] Confirma que las acciones irreversibles (borrar datos, enviar comunicaciones, aprobar procesos) requieran confirmación humana explícita.

⚠️ **IMPORTANTE:** Los valores específicos de tu compañía — qué se considera una acción irreversible, qué datos son sensibles, qué SLA de respuesta aplica ante un incidente — están definidos en tu CONTEXT.md.

**Informe NIST**

- [ ] Redacta el informe cubriendo las seis funciones de NIST (Govern, Identify, Protect, Detect, Respond, Recover), con al menos una acción concreta y priorizada por función.
- [ ] Para cada brecha identificada que no llegaste a corregir en este ciclo, documenta el riesgo y la mitigación propuesta.

---

## ✅ Qué Vamos a Evaluar

- [ ] El inventario de sistemas de IA lista cada componente construido hasta ahora, con responsable asignado.
- [ ] No hay API keys ni credenciales hardcodeadas en el código; todas provienen de variables de entorno o vault.
- [ ] Existe al menos un caso de prueba reproducible que demuestra un intento de prompt injection siendo bloqueado o neutralizado.
- [ ] Al menos un endpoint que invoca un modelo tiene rate limiting implementado y verificable.
- [ ] Existe logging verificable de las decisiones y acciones de al menos un agente.
- [ ] Las acciones irreversibles identificadas requieren confirmación humana antes de ejecutarse.
- [ ] El informe NIST cubre las seis funciones con al menos una acción concreta por función.
- [ ] El informe hace referencia explícita al marco regulatorio de tu CONTEXT.md, no a normativa genérica.

---

## 📦 Cómo Entregar

1. Haz commit y push de tu rama.
2. Abre un Pull Request hacia tu propio fork del monorepo, incluyendo el informe NIST como archivo markdown dentro de tu carpeta de entrega.
3. En la descripción del PR, enlaza el caso de prueba de prompt injection y explica brevemente qué brechas quedaron pendientes y por qué.
4. Solicita revisión a tu tech lead antes del sign-off final.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
