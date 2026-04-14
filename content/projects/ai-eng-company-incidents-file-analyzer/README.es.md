# Script procesador de Reportes de Incidentes

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de comenzar:** Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir cualquier línea de código; allí se definen los nombres exactos de campos CSV, categorías válidas, estados permitidos y los valores esperados que tu script debe producir.

---

## 🎯 El reto

Llega un tipo de solicitud diferente: no hay interfaz que construir ni API que levantar. Lo que necesitas entregar es una **herramienta de análisis de datos** que resuelva un problema real y urgente.

El departamento de soporte postventa de tu empresa gestiona incidentes de clientes: reclamos, solicitudes, fallos operativos. Acaban de preparar un archivo CSV con **100 registros** extraídos de su sistema: la primera muestra de un volumen real de datos que podría llegar al millón de filas.

El problema es que **este archivo no se puede enviar a una herramienta de IA**. Contiene información sensible de clientes: identificadores personales, direcciones de correo y datos de contacto. El equipo necesita analizar los datos internamente.

Tu trabajo es escribir un **script en Python** que cargue el archivo, lo valide, extraiga métricas clave y entregue un resumen estructurado. Si el script funciona correctamente con la muestra de 1.000 registros, luego se ejecutará sobre el archivo completo de producción.

> **Nota de tu tech lead:** _"Necesitamos un script que cualquiera del equipo pueda ejecutar con_ `python analyze.py incidents.csv`_. La salida en consola tiene que ser legible y profesional. Dales también una opción para exportar resultados a JSON o CSV; no todo el mundo trabaja desde la terminal. Asegúrate de detectar registros corruptos o incompletos; si no validamos datos antes de procesarlos, el análisis del archivo grande será basura. Los valores esperados para el CSV de prueba están en tu CONTEXT."_

### ¿Qué se considera un registro incompleto o corrupto?

Los datos del mundo real siempre tienen problemas. Para este proyecto, un registro se considera **inválido** si le falta al menos uno de los campos requeridos definidos en tu CONTEXT, o si contiene un valor en un campo que no está dentro del conjunto permitido (estados y categorías). Tu script debe detectarlos, contarlos y excluirlos del análisis principal, pero nunca ignorarlos silenciosamente.

---

## 🌱 Cómo empezar el proyecto

1. Haz fork del repositorio del curso:
   ```text
   https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo
   ```
2. Clona tu fork en local.
3. Lee tu archivo **CONTEXT-company.md** antes de escribir una sola línea de código. Ahí se define la estructura CSV, campos requeridos, valores válidos y resultados esperados que tu script debe cumplir.
4. Trabaja dentro del directorio correspondiente a este proyecto en el monorepo.

No hay código inicial. El script empieza desde cero.

---

## 💻 Lo que debes hacer

### Script principal de análisis

- [ ] Crea el script principal (`analyze.py`) que acepte la ruta al CSV como argumento de línea de comandos: `python analyze.py incidents.csv`.
- [ ] El script debe cargar y leer el archivo fila por fila (o con pandas, tú eliges).
- [ ] Detectar y contar registros inválidos. Detalla cuántos hay y por qué (campo faltante, valor fuera de rango, etc.).
- [ ] Calcula las siguientes métricas sobre **registros válidos**:
  - [ ] Número total de elementos procesados (válidos e inválidos por separado).
  - [ ] Desglose por categoría de incidente.
  - [ ] Desglose por estado (`open`, `closed`, `discarded`, o sus equivalentes en tu CONTEXT).
  - [ ] Índice promedio de satisfacción para casos cerrados que tengan una puntuación registrada.
- [ ] Imprime el resumen en consola con formato legible: usa separadores, etiquetas claras y alineación. No es un `print` crudo de un diccionario.

### Exportación de resultados

- [ ] Al final de la ejecución, el script debe preguntar al usuario (entrada interactiva): `Export results to CSV? [y / n]`
- [ ] Si el usuario elige `y`, guarda los resultados en `results.csv` (una fila por métrica).
- [ ] Si el usuario elige `n`, el script termina sin exportar.

### Validación contra valores esperados

- [ ] Compara los resultados de tu script con los valores esperados indicados en tu CONTEXT. Los totales deben coincidir exactamente.

⚠️ **IMPORTANTE:** Los nombres de campos, categorías, estados y valores esperados en tu implementación deben coincidir exactamente con lo especificado en tu CONTEXT.md. No se aceptará un script genérico que ignore la estructura de datos de tu empresa.

---

## ✅ Qué vamos a evaluar

- [ ] El script acepta la ruta del CSV como argumento de línea de comandos y funciona sin modificar el código.
- [ ] Los registros corruptos o inválidos se detectan, clasifican y se muestran en el resumen junto a su tipo de problema.
- [ ] Las cinco métricas requeridas (total procesado, por categoría, por estado, registros corruptos, índice de satisfacción) aparecen en la salida de consola.
- [ ] El formato en consola es legible: no es un volcado de datos crudo. Incluye separadores, etiquetas y alineación.
- [ ] La exportación a CSV funciona correctamente y genera un archivo bien estructurado.
- [ ] Los resultados del script coinciden con los valores esperados en el CONTEXT.
- [ ] El código está organizado en funciones con responsabilidades claras (carga, validación, análisis, salida, exportación).

---

## 📦 Cómo entregar

1. Asegúrate de que tu repositorio contenga:
   - `analyze.py`: el script de análisis.
   - `COMPANY-incidents.csv`: se envía como archivo adjunto (ver `COMPANY-incidents.csv` en los archivos del proyecto).
   - Un `README` breve en el directorio del proyecto que explique cómo ejecutar el script.
2. Haz push de tu rama y abre un Pull Request al repositorio original.
3. Asegúrate de que el PR incluya una captura de la salida de consola usando el CSV de 100 filas.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) en 4Geeks Academy. Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Descubre más sobre [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) e [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
