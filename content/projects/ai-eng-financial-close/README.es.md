# Agentic Engineering – Cierre Financiero Mensual

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee el **[BRIEFING de tu empresa](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/financial-close)** antes de escribir una sola línea de código. Ahí están las fuentes de datos del cierre, el presupuesto, los umbrales de desviación, el desglose que espera la dirección y quién revisa el informe antes de distribuirlo.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa, no en un repositorio nuevo.

La dirección general te escribe con una frustración que se repite cada mes. Los datos de cierre llegan tarde, montados a mano a partir de exportaciones de distintos sistemas y hojas de cálculo. Cuando por fin llegan, las cifras no siempre cuadran entre sí, y explicar por qué un área se ha desviado del presupuesto obliga a convocar una reunión.

> _"Quiero el cierre de cada mes en mi bandeja en los primeros días del mes siguiente, sin que nadie pase un fin de semana montándolo. Quiero ver cómo vamos frente al presupuesto, dónde nos hemos desviado y una explicación razonable de por qué. Pero no acepto una sola cifra que no se pueda rastrear hasta su origen. Si falta un dato, prefiero que el informe lo diga a que alguien lo rellene a ojo. Y antes de que el informe llegue al equipo directivo, una persona de confianza tiene que revisarlo."_
>
> — Dirección General

El brief deja implícitas cuatro exigencias que definen el proyecto:

1. **Cada cifra es trazable.** Cualquier número del informe debe poder rastrearse hasta el registro, el documento o la fila de la que sale.
2. **Los cálculos no los hace el modelo.** Sumas, porcentajes, desviaciones y conversiones de moneda se calculan con código determinista. El modelo decide qué calcular, interpreta los resultados y redacta, pero no hace la aritmética.
3. **Lo que falta se declara.** Un periodo con datos incompletos produce un informe que dice qué falta, no un informe que parece completo.
4. **Una persona aprueba antes de distribuir.** El agente prepara el informe; la distribución solo ocurre después de una revisión humana.

### Conocimiento complementario: qué hace el modelo y qué hace el código

Los modelos de lenguaje son buenos interpretando, resumiendo y redactando, pero no son fiables haciendo aritmética: pueden equivocarse en una suma de forma convincente, y en un informe financiero un error convincente es peor que un error evidente. El patrón correcto es un **agente con herramientas**: el código calcula de forma determinista y verificable, y el agente decide qué cálculos pedir, lee los resultados, identifica qué desviaciones importan y redacta la explicación. Así, el mismo periodo con los mismos datos produce siempre las mismas cifras, y cada cifra tiene una prueba detrás. Las explicaciones del agente, en cambio, son hipótesis basadas en los datos, y el informe debe presentarlas como tales.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee el briefing de tu empresa completo antes de tocar código.
3. Crea una rama nueva: `feature/financial-close`.
4. Revisa las fuentes de datos de prueba que indica el briefing y su estructura antes de diseñar la ingesta.
5. Diseña la estructura del informe de cierre antes de programar el agente: qué secciones tiene, qué desglose y qué indicadores.
6. Define la lista de herramientas de cálculo que necesitará el agente.

---

## 💻 Qué Debes Hacer

**Ingesta de datos**

- [ ] Implementa la ingesta de las fuentes de datos del cierre que indica el briefing
- [ ] Normaliza los datos a un formato común, conservando siempre la referencia a su origen
- [ ] Marca como dudoso cualquier registro incompleto o inconsistente, en lugar de darlo por válido

**Herramientas de cálculo deterministas**

- [ ] Implementa como herramientas de código los cálculos que necesita el cierre: totales, comparación real frente a presupuesto, desviación absoluta y porcentual, y conversión de moneda si el briefing lo requiere
- [ ] Cubre cada herramienta con pruebas automatizadas
- [ ] Asegura que ejecutar el cierre dos veces sobre el mismo periodo y los mismos datos produce exactamente las mismas cifras

**Agente de cierre**

- [ ] Implementa un único agente que use las herramientas de cálculo para analizar el periodo
- [ ] Identifica las desviaciones que superan el umbral definido en el briefing
- [ ] Redacta, para cada desviación relevante, una explicación basada en los datos, presentada como hipótesis y citando las cifras que la sostienen
- [ ] Genera el informe de cierre con la estructura y el desglose que define el briefing
- [ ] Declara explícitamente en el informe cualquier dato que falte o que se haya marcado como dudoso

**Trazabilidad**

- [ ] Enlaza cada cifra del informe con los registros de origen que la producen
- [ ] Permite que la persona revisora consulte, desde el informe, el origen de cualquier cifra

**Revisión y distribución**

- [ ] Ejecuta el cierre como tarea en segundo plano, programada para la fecha que define el briefing
- [ ] Envía el informe a la persona revisora definida en el briefing antes de cualquier distribución
- [ ] Permite aprobar el informe o rechazarlo con comentarios; un rechazo genera una nueva versión que tiene en cuenta esos comentarios
- [ ] Distribuye el informe solo tras su aprobación, y solo a los destinatarios que define el briefing

**Seguridad y registro**

- [ ] El agente opera con una identidad propia y acceso de solo lectura a los datos financieros
- [ ] Registra cada acción del agente, identificándola como acción de un proceso automatizado
- [ ] Identifica en el briefing qué datos son sensibles y demuestra que no aparecen en logs, prompts almacenados ni mensajes salientes

⚠️ **IMPORTANTE:** las fuentes de datos, los umbrales, la estructura del informe, la persona revisora y los destinatarios deben corresponder exactamente a lo especificado en el briefing de tu empresa. Una implementación genérica que ignore ese contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] Toda cifra del informe es rastreable hasta sus registros de origen
- [ ] Los cálculos se hacen con herramientas de código determinista, cubiertas por pruebas
- [ ] Ejecutar el cierre dos veces sobre los mismos datos produce exactamente las mismas cifras
- [ ] Las desviaciones por encima del umbral se detectan, y cada una tiene una explicación presentada como hipótesis y sostenida por datos
- [ ] Un periodo con datos incompletos produce un informe que declara lo que falta
- [ ] El informe no se distribuye sin aprobación de la persona revisora, y un rechazo con comentarios genera una nueva versión
- [ ] Las acciones del agente quedan registradas como acciones de proceso automatizado
- [ ] Los datos sensibles no aparecen en logs, prompts almacenados ni mensajes salientes

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/financial-close` hacia `main` en tu fork. En la descripción del PR incluye la estructura del informe, la lista de herramientas de cálculo, un informe de cierre de ejemplo con su trazabilidad y un ejemplo de informe generado con datos incompletos. Solicita el sign-off de la dirección antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
