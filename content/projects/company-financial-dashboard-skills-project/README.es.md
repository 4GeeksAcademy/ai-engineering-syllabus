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

El dashboard financiero que entregaste recientemente está funcionando. Los datos cargan, los gráficos se renderizan, el layout aguanta. Tu tech lead revisó el pull request y dejó un comentario:

> _"Buen trabajo. Antes de hacer merge, quiero que subas el nivel en dos frentes: accesibilidad y buenas prácticas de despliegue. Te comparto dos skills que puedes cargar directamente en tu agente de código — te guiarán para hacer las mejoras correctas sin que tengas que memorizar cada regla desde cero. Una vez aplicadas, explora el ecosistema de skills y mira qué más vale la pena añadir. Luego documenta lo que aprendiste."_

Así es como los equipos profesionales escalan la calidad: no memorizando cada checklist, sino construyendo conocimiento reutilizable que se puede cargar en cualquier agente y aplicar de forma consistente en cualquier codebase.

### ¿Qué es una skill para un agente?

Una skill para un agente es un conjunto de instrucciones estructuradas y autocontenidas que le dice al agente de código _cómo_ realizar una tarea específica — qué buscar, qué patrones aplicar, qué evitar y cómo verificar el resultado. Las skills son componibles: puedes combinar varias skills pequeñas y enfocadas para obtener una mejora compuesta sin necesidad de escribir un prompt masivo.

El ecosistema en [skills.sh](https://skills.sh) aloja skills mantenidas por la comunidad listas para cargar. Pero el punto clave es este: **una skill solo es tan buena como la claridad con la que define su objetivo, sus inputs, sus outputs y sus criterios de aceptación.** Hoy lo vas a experimentar en primera persona.

> Tu tech lead ha compartido las siguientes instrucciones:
>
> #### Accesibilidad (`accessibility`)
>
> Aplica la skill `accessibility` al dashboard. El objetivo es garantizar que las personas que utilizan tecnologías de asistencia — lectores de pantalla, navegación por teclado, modos de alto contraste — puedan usar el producto sin fricción. La skill guiará al agente para auditar y corregir los problemas más comunes: atributos `aria-label` faltantes, gestión deficiente del foco, texto `alt` ausente y elementos interactivos con bajo contraste.
>
> #### Vercel + React Best Practices (`vercel-react-best-practices`)
>
> Aplica la skill `vercel-react-best-practices`. Cubre patrones listos para despliegue: uso correcto de `next/image`, `next/font`, evitar layout shift, metadatos correctos por página y evitar anti-patrones que afectan los scores de Lighthouse en despliegues de Vercel.
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

Al terminar esta sesión tendrás un codebase mejorado _y_ una skill documentada propia — un artefacto transferible que puedes llevar a cualquier proyecto futuro.

---

## 🌱 Cómo iniciar el proyecto

Continuarás trabajando en el **mismo repositorio** que utilizaste en la sesión anterior. No hagas fork de un nuevo repo.

1. Abre tu repositorio `company-financial-dashboard-context-project` en GitHub Codespaces o clónalo localmente.
2. Asegúrate de que tu memory bank (`memory-bank/`) y las reglas de contexto (`.cursor/rules/` o equivalente) de la sesión anterior están commiteadas y actualizadas.
3. Haz pull de los últimos cambios si trabajas en equipo: `git pull origin main`.
4. Crea una rama nueva para el trabajo de hoy: `git checkout -b feature/agent-skills`.

Si necesitas repasar la configuración del proyecto: [cómo iniciar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué debes hacer

### 1. Descubrir y cargar las skills proporcionadas

- [ ] Ejecuta `npx skills find accessibility` y revisa qué cubre la skill antes de aplicarla.
- [ ] Ejecuta `npx skills find vercel-react-best-practices` y revísala.
- [ ] Carga ambas skills en tu agente de código y lee qué instrucciones le dan al agente.

### 2. Aplicar la skill `accessibility`

- [ ] Usa el agente con la skill `accessibility` cargada para auditar el dashboard.
- [ ] Corrige todos los problemas de `aria-label` y `role` identificados por el agente.
- [ ] Asegúrate de que todos los elementos interactivos (botones, enlaces, inputs) sean alcanzables por teclado (`Tab` / `Enter` / `Space`).
- [ ] Añade o corrige el texto `alt` en todas las imágenes e iconos.
- [ ] Verifica que no existan problemas de contraste de color en textos y elementos interactivos.

### 3. Aplicar la skill `vercel-react-best-practices`

- [ ] Reemplaza las etiquetas `<img>` estándar por `next/image` donde corresponda.
- [ ] Asegúrate de que todas las páginas tienen `<title>` y `<meta description>` correctos mediante la API de metadata de Next.js.
- [ ] Elimina los anti-patrones identificados por la skill (p. ej. estilos que causan layout shift, importaciones de fuentes no optimizadas).
- [ ] Verifica que el build pase en local: `npm run build`.

### 4. Explorar el ecosistema

- [ ] Ejecuta `npx skills find <tema>` sobre al menos dos temas relevantes para este proyecto (p. ej. `performance`, `seo`, `forms`, `typescript`).
- [ ] Aplica al menos una skill adicional que consideres valiosa para el dashboard. Justifica tu elección en un comentario o en el memory bank.

### 5. Escribe tu propia skill

- [ ] Identifica algo específico de este dashboard financiero que no esté cubierto por las skills existentes — un patrón, una restricción, una convención de nombrado, una regla de formateo de datos.
- [ ] Escribe un fichero de skill para ello siguiendo la estructura vista en clase: objetivo claro, inputs definidos, output esperado, criterios de aceptación.
- [ ] Guárdalo en la carpeta `.skills/` del proyecto y cárgalo en el agente para verificar que produce la guía esperada.

### 6. Actualizar el memory bank

- [ ] Actualiza `memory-bank/progress.md` (o equivalente) para reflejar las skills aplicadas, los cambios realizados y la skill que has creado.

⚠️ **IMPORTANTE:** No reescribas el dashboard desde cero. El objetivo es una _mejora dirigida_ usando skills — no una reconstrucción total. Cada cambio debe ser trazable a una instrucción específica de una skill.

---

## ✅ Qué vamos a evaluar

- [ ] Las skills `accessibility` y `vercel-react-best-practices` fueron cargadas y aplicadas correctamente — las mejoras son visibles y trazables a las instrucciones de cada skill.
- [ ] Los problemas de accesibilidad están resueltos: la navegación por teclado funciona, los atributos `aria-*` son correctos, el texto `alt` está presente, el contraste supera comprobaciones básicas.
- [ ] El build pasa (`npm run build`) sin nuevas advertencias introducidas.
- [ ] Al menos una skill adicional fue descubierta con `npx skills find` y aplicada con una justificación escrita.
- [ ] Existe un fichero de skill propia en `.skills/`, está bien estructurado (objetivo, inputs, outputs, criterios de aceptación) y contiene guía específica y significativa del proyecto — no relleno genérico.
- [ ] El memory bank refleja con precisión el trabajo de la sesión.
- [ ] Los cambios están commiteados en una rama de feature con mensajes claros y descriptivos — lo ideal es un commit por skill aplicada.

> **Nota:** La calidad de la skill propia se evaluará por su claridad y especificidad, no por su longitud. Una skill corta y precisa vale más que una larga y vaga.

---

## 📦 Cómo entregar

Sube tu rama de feature a GitHub y abre un pull request contra `main`. Comparte la URL del pull request con tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
