# Agentic Engineering – Gestión de Proveedores y Contratos

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee el **[BRIEFING de tu empresa](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir una sola línea de código. Ahí están los proveedores, los contratos y los datos de precios con los que trabajarás, los umbrales de alerta y quién aprueba cada decisión.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa, no en un repositorio nuevo.

La dirección de Operaciones te escribe con un problema que le cuesta dinero cada trimestre. Las subidas de precio de los proveedores se descubren cuando llega la factura. Los contratos están repartidos entre carpetas y correos, y nadie sabe con certeza cuándo vence cada uno, cuánto preaviso exige o si una subida concreta está permitida. Cuando hay que renegociar, alguien dedica días a reunir el histórico de precios, revisar el contrato y comparar con otros proveedores.

> _"Necesito enterarme de una subida antes de pagarla, no después. Y cuando me entere, quiero saber en el momento si el contrato la permite, cuánto nos cuesta, qué alternativas tenemos y qué margen nos da el contrato para negociar o salir. Hoy eso lo hacen dos personas que no se hablan: una mira precios y otra mira contratos. Quiero que el sistema cruce las dos cosas. Pero nadie habla con un proveedor en nombre de la empresa sin que yo lo apruebe."_
>
> — Dirección de Operaciones

El brief deja implícitas cuatro exigencias que definen el proyecto:

1. **Son dos especialidades que se necesitan mutuamente.** Analizar precios y analizar contratos requieren fuentes, herramientas y criterios distintos. Pero las preguntas importantes ("¿esta subida está permitida?", "¿conviene renegociar?") necesitan las dos a la vez, así que alguien tiene que coordinarlas.
2. **Cada cifra y cada cláusula son trazables.** Todo precio tiene que rastrearse hasta su registro de origen, y toda afirmación sobre un contrato hasta la cláusula y la página de las que sale. Si el dato no existe, el sistema lo dice; no lo estima.
3. **Los cálculos no los hace el modelo.** Variaciones de precio, impacto económico y comparativas se calculan con código determinista. El modelo interpreta, redacta y decide qué calcular, pero no hace la aritmética.
4. **El sistema prepara; las personas deciden.** Ninguna comunicación con un proveedor ni ninguna decisión con impacto económico se ejecuta sin aprobación humana.

### Conocimiento complementario: cuándo sí tiene sentido una arquitectura multiagente

Un único agente con todas las herramientas de análisis de precios y de contratos acumula instrucciones que compiten entre sí y un contexto lleno de información irrelevante para cada tarea concreta, lo que degrada la calidad de sus decisiones. Una arquitectura **supervisor + especialistas** resuelve el problema: cada especialista tiene un alcance estrecho, sus propias herramientas y su propio contexto, y el supervisor decide a quién consultar y combina las respuestas. El coste es mayor complejidad: hay que definir un contrato claro de lo que cada especialista recibe y devuelve, y controlar que el supervisor no entre en bucles de consultas. La arquitectura multiagente se justifica cuando las especialidades son realmente distintas y las preguntas importantes las cruzan, como aquí. En un proceso lineal, un solo agente basta.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee el briefing de tu empresa completo antes de tocar código.
3. Crea una rama nueva: `feature/supplier-contracts`.
4. Revisa los datos de prueba que indica el briefing (proveedores, histórico de precios y contratos) y su estructura antes de diseñar la ingesta.
5. Dibuja la arquitectura antes de programar: qué hace el supervisor, qué hace cada especialista, qué herramientas tiene cada uno y qué datos se pasan entre ellos.
6. Define por escrito el contrato de entrada y salida de cada especialista.

---

## 💻 Qué Debes Hacer

**Ingesta de datos y documentos**

- [ ] Implementa la ingesta del registro de proveedores y de su histórico de precios, conservando siempre la referencia a su origen
- [ ] Implementa la ingesta de los contratos en PDF y extrae sus términos clave: fecha de vencimiento, preaviso de renovación o cancelación, condiciones de revisión de precio, cláusulas de salida y penalizaciones
- [ ] Conserva para cada término extraído la cláusula y la página de origen
- [ ] Marca como dudosa cualquier extracción con baja confianza, en lugar de darla por válida

**Especialista de precios**

- [ ] Mantiene el histórico de precios por proveedor y por producto o servicio
- [ ] Detecta subidas de precio que superan el umbral definido en el briefing
- [ ] Calcula el impacto económico de una subida a partir del volumen de compra
- [ ] Compara el precio de un proveedor con el de otros proveedores de la misma categoría

**Especialista de contratos**

- [ ] Responde qué permite o impide un contrato ante una situación concreta, citando la cláusula
- [ ] Determina si una subida de precio está dentro de lo que permite la cláusula de revisión de precios
- [ ] Genera alertas con la antelación que define el briefing antes de cada vencimiento o fecha límite de preaviso

**Supervisor**

- [ ] Recibe la petición, decide qué especialistas consultar y combina sus respuestas en una respuesta única
- [ ] Ante una subida detectada, determina automáticamente si el contrato la permite y cuál es su impacto
- [ ] Genera, a petición, un brief de renegociación que combina histórico de precios, comparativa con otros proveedores, impacto económico y margen contractual (preaviso, cláusulas de salida, penalizaciones)
- [ ] Limita el número de consultas por petición para evitar bucles

**Cálculo y trazabilidad**

- [ ] Implementa variaciones de precio, impacto económico, comparativas y conversiones de moneda, si el briefing las requiere, como herramientas de código determinista cubiertas por pruebas
- [ ] Asegura que toda cifra y toda referencia contractual de una respuesta o un brief se puede rastrear hasta su origen
- [ ] Cuando falta un dato o una cláusula, el sistema lo declara explícitamente en lugar de suponerlo

**Aprobación humana y seguridad**

- [ ] El sistema puede redactar comunicaciones a proveedores, pero ninguna se envía sin aprobación humana
- [ ] Aplica los umbrales de aprobación y los aprobadores que define el briefing
- [ ] Cada agente opera con su propia identidad y solo con las herramientas de su especialidad
- [ ] Registra cada acción de cada agente, identificando qué agente la realizó
- [ ] Identifica en el briefing qué datos son sensibles y demuestra que no aparecen en logs, prompts almacenados ni mensajes salientes

⚠️ **IMPORTANTE:** los proveedores, los contratos, los umbrales, los plazos de alerta y los aprobadores deben corresponder exactamente a lo especificado en el briefing de tu empresa. Una implementación genérica que ignore ese contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] La arquitectura separa supervisor y especialistas, con herramientas y contratos de entrada y salida definidos para cada uno
- [ ] Una subida por encima del umbral se detecta y se evalúa contra la cláusula de revisión de precios del contrato correspondiente
- [ ] El brief de renegociación combina datos de los dos especialistas en una recomendación coherente
- [ ] Toda cifra es rastreable hasta su registro de origen, y toda afirmación contractual hasta su cláusula y página
- [ ] Los cálculos se hacen con código determinista, verificable con pruebas
- [ ] Las alertas de vencimiento y preaviso se disparan con la antelación definida
- [ ] Ninguna comunicación con un proveedor se envía sin aprobación humana del aprobador correcto
- [ ] Cuando un dato o una cláusula no existen, el sistema lo declara en lugar de inventarlo
- [ ] Los datos sensibles no aparecen en logs, prompts almacenados ni mensajes salientes
- [ ] La elección de una arquitectura multiagente está justificada por escrito

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/supplier-contracts` hacia `main` en tu fork. En la descripción del PR incluye el diagrama de la arquitectura, los contratos de entrada y salida de cada especialista, la justificación de la arquitectura multiagente, un ejemplo de subida detectada y evaluada contra su contrato, y un brief de renegociación con su trazabilidad. Solicita el sign-off de la dirección de Operaciones antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
