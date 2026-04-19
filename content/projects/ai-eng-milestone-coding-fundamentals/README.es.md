# Hito 2 — Desarrollando scripts para automatizar tareas

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) de [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Desafío

Ya tienes la web pública de tu empresa funcionando con formularios y validaciones básicas. Ahora tu equipo técnico necesita que construyas las primeras funcionalidades internas que harán que el negocio opere de forma más eficiente.

Tu gerente te ha asignado implementar un conjunto de utilidades de procesamiento de datos que el equipo necesita para el día a día. No se trata de una interfaz completa todavía — eso vendrá después — sino de las funciones base que permitirán gestionar, filtrar, ordenar y transformar la información crítica del negocio. Piensa en esto como la capa lógica que otros sistemas utilizarán más adelante.

Estas utilidades deben estar escritas en **TypeScript**, ser reutilizables, estar correctamente tipadas y poder ejecutarse tanto en el navegador como en entornos de desarrollo. El énfasis está en dominar la manipulación de datos estructurados: colecciones, objetos, búsquedas, ordenamientos y transformaciones.

### 📋 Lo que te piden construir

Tu tech lead te envía el siguiente brief por correo:

> **De:** Tech Lead  
> **Para:** Tú  
> **Asunto:** Funcionalidades base para procesamiento de datos
>
> Hola,
>
> Necesitamos que implementes un conjunto de funciones TypeScript que nos permitan manejar de forma eficiente los datos principales de la empresa. El objetivo es tener utilidades sólidas y bien tipadas que podamos reutilizar en múltiples contextos.
>
> **Lo que necesitamos:**
>
> 1. **Sistema de gestión de colecciones**: Funciones para filtrar, ordenar, buscar y agrupar elementos dentro de arrays. Debes implementar búsqueda lineal para arrays desordenados y búsqueda binaria para arrays ordenados. Asegúrate de manejar correctamente casos vacíos y elementos no encontrados.
> 2. **Modelado de datos con objetos e interfaces**: Define las interfaces TypeScript que representan las entidades principales del negocio. Cada interfaz debe tener tipos explícitos para todas sus propiedades y métodos auxiliares para trabajar con esos datos. Usa objetos literales para representar instancias concretas.
> 3. **Transformaciones y agregaciones**: Implementa funciones que tomen colecciones de objetos y generen reportes simples: contar elementos por categoría, sumar valores numéricos, encontrar máximos y mínimos, calcular promedios. Todo debe estar tipado.
> 4. **Validaciones de negocio**: Crea funciones que validen que los datos cumplan con las reglas específicas de tu empresa antes de ser procesados o almacenados. Por ejemplo, verificar que un elemento tenga todos los campos obligatorios, que los valores numéricos estén dentro de rangos permitidos, o que las fechas sean coherentes.
>
> El código debe ser limpio, con nombres descriptivos, y cada función debe tener una sola responsabilidad. Queremos que esto sea mantenible a largo plazo.
>
> Revisa el documento de contexto de tu empresa para conocer exactamente qué entidades modelar, qué validaciones aplicar y qué reportes generar.
>
> Saludos,  
> Tech Lead

---

### 💡 Qué debes saber antes de empezar

Este hito se enfoca exclusivamente en lógica de programación y manipulación de datos con TypeScript. No utilizarás IA generativa ni prompting para este desafío — el objetivo es que domines los fundamentos de la programación de forma autónoma.

**Conceptos clave que aplicarás:**

- **Arrays y matrices**: Cómo almacenar, recorrer, ordenar y buscar elementos en colecciones.
- **Búsqueda lineal vs búsqueda binaria**: Cuándo usar cada una y cómo implementarlas correctamente.
- **Interfaces y objetos literales**: Cómo modelar datos del mundo real en TypeScript con tipos explícitos.
- **Funciones puras**: Escribir funciones que solo trabajen con lo que reciben por parámetros, sin depender de variables globales.
- **Transformaciones funcionales**: Uso de `.map()`, `.filter()`, `.reduce()` y otros métodos de arrays para transformar datos sin bucles explícitos.
- **Validaciones**: Cómo escribir funciones que verifiquen que los datos cumplen reglas de negocio antes de procesarlos.

**Estructura de archivos esperada:**

Tu implementación debe organizarse en archivos TypeScript separados por responsabilidad:

```text
src/
├── types/
│   └── models.ts          Interfaces y tipos
├── utils/
│   ├── collections.ts     # Funciones para arrays
│   ├── search.ts          # Búsquedas lineal y binaria
│   ├── transformations.ts # Agregaciones y reportes
│   └── validations.ts     # Validaciones de negocio
└── index.html             # Página de prueba (opcional)
```

Puedes incluir una página HTML simple con Tailwind CSS para probar tus funciones manualmente si lo deseas, pero el foco principal está en la lógica TypeScript.
Como mínimo, tu proyecto debe incluir un comando claro para validar o ejecutar el código TypeScript durante el desarrollo, por ejemplo `npx tsc --noEmit`, `npm run typecheck` o `npx tsx src/demo.ts`.

---

## 🌱 Cómo Iniciar el Proyecto

1. Ve a tu repositorio del proyecto de compañía que ya tienes. Si no lo has creado aún, ve al [repositorio plantilla del proyecto transversal](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) y haz clic en el botón de la derecha "Usar esta plantilla" y selecciona "Crear un nuevo repositorio" o [haz clic aquí](https://github.com/new?template_name=ai-engineering-company-project-monorepo&template_owner=4GeeksAcademy).

2. Una vez tengas tu propio repositorio, ábrelo en un Codespace o clónalo localmente.

3. Lee completamente tu archivo **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir código. Allí encontrarás:
   - Las entidades específicas que debes modelar (productos, clientes, pedidos, etc.)
   - Los nombres exactos de los campos y sus tipos
   - Las reglas de validación específicas de tu empresa
   - Los reportes que debes generar

4. Crea una rama para este hito:

   ```bash
   git checkout -b hito-2-fundamentos-programacion
   ```

5. Organiza tu código en la estructura de carpetas propuesta y comienza a implementar las funciones.

6. Asegúrate de que el proyecto pueda validarse o ejecutarse con un comando claro de TypeScript durante el desarrollo. Ejemplo:

   ```bash
   npx tsc --noEmit
   ```

7. Comienza a implementar las funciones.

---

## 💻 Lo que Debes Hacer

Implementa las siguientes funcionalidades en TypeScript. Todos los nombres de entidades, campos y reglas deben coincidir exactamente con lo especificado en tu CONTEXT.md.

### Backend / Lógica

- [ ] Define las **interfaces TypeScript** para todas las entidades principales de tu empresa especificadas en tu CONTEXT.md
- [ ] Implementa funciones de **filtrado** que permitan buscar elementos por uno o más criterios (por ejemplo: filtrar por categoría, por rango de precio, por estado)
- [ ] Implementa funciones de **ordenamiento** que ordenen arrays según diferentes criterios (ascendente, descendente, por múltiples campos)
- [ ] Implementa **búsqueda lineal** para encontrar elementos en arrays desordenados
- [ ] Implementa **búsqueda binaria** para encontrar elementos en arrays previamente ordenados
- [ ] Crea funciones de **agregación** que generen reportes: contar elementos por categoría, calcular totales, promedios, máximos y mínimos
- [ ] Implementa **validaciones de negocio** que verifiquen que los objetos cumplen con las reglas de tu CONTEXT.md antes de ser procesados
- [ ] Todas las funciones deben tener **tipos explícitos** en parámetros y valores de retorno
- [ ] El código debe seguir el principio de **responsabilidad única**: cada función hace una sola cosa
- [ ] El proyecto incluye un comando claro para validar o ejecutar el código TypeScript durante el desarrollo

⚠️ **IMPORTANTE:** Los nombres de campos, tipos de entidades y reglas de validación en tu implementación deben coincidir exactamente con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

### Frontend / Pruebas (Opcional)

- [ ] Crea una página HTML simple con **Tailwind CSS** que te permita probar tus funciones manualmente
- [ ] Incluye botones o controles para ejecutar diferentes operaciones (filtrar, buscar, ordenar, generar reportes)
- [ ] Muestra los resultados de las operaciones en la interfaz de forma clara

Si agregas una página `index.html` para probar tus funciones manualmente, asegúrate de poder servirla en local o en Codespaces con un comando simple como:

```bash
npx http-server . -p 3000 -a 0.0.0.0
```

### Calidad de Código

- [ ] Usa **nombres descriptivos** para variables, funciones e interfaces (camelCase para variables y funciones, PascalCase para interfaces)
- [ ] Cada función debe ser **pura**: trabaja solo con lo que recibe por parámetros, sin modificar variables globales
- [ ] Escribe **comentarios** solo cuando sea necesario para explicar lógica compleja, no para describir código obvio
- [ ] Maneja correctamente **casos vacíos**: arrays vacíos, elementos no encontrados, valores nulos
- [ ] Usa **const** por defecto y **let** solo cuando el valor vaya a cambiar
- [ ] Mantén la **indentación** y el formato consistentes en todo el código

---

## ✅ Lo que Evaluaremos

### Corrección técnica

- [ ] Las interfaces TypeScript modelan correctamente las entidades especificadas en el CONTEXT.md con todos sus campos y tipos
- [ ] Las funciones de filtrado devuelven correctamente los elementos que cumplen los criterios especificados
- [ ] El ordenamiento funciona correctamente en orden ascendente y descendente
- [ ] La búsqueda lineal encuentra elementos en arrays desordenados sin errores
- [ ] La búsqueda binaria funciona correctamente en arrays ordenados y devuelve el índice correcto o -1 si no se encuentra
- [ ] Las agregaciones calculan correctamente totales, promedios, conteos y valores extremos
- [ ] Las validaciones rechazan datos que no cumplen con las reglas de negocio del CONTEXT.md
- [ ] No hay errores de compilación de TypeScript en ningún archivo
- [ ] Existe un comando documentado para validar o ejecutar TypeScript en local (`npx tsc --noEmit`, `npm run typecheck`, etc.)

### Estructura y organización

- [ ] El código está organizado en archivos separados por responsabilidad (types, utils, validations)
- [ ] Cada función tiene una única responsabilidad claramente identificable
- [ ] Los nombres de variables, funciones e interfaces son descriptivos y siguen las convenciones de TypeScript

### Adaptación al contexto

- [ ] Todos los nombres de entidades, campos y tipos coinciden exactamente con los especificados en el CONTEXT.md
- [ ] Las validaciones implementadas corresponden a las reglas de negocio definidas en el CONTEXT.md
- [ ] Los reportes generados responden a las necesidades específicas descritas en el CONTEXT.md

### Calidad de código

- [ ] Las funciones son puras: no dependen de variables externas ni modifican estado global
- [ ] Se manejan correctamente casos límite: arrays vacíos, elementos no encontrados, valores nulos
- [ ] El código sigue las mejores prácticas de TypeScript: tipos explícitos, uso de const/let apropiado, evita any

---

## 📦 Cómo Entregar

1. Asegúrate de que todos tus cambios están en la rama `hito-2-fundamentos-programacion`

2. Haz commit de tus cambios con mensajes descriptivos. Por ejmplo:

   ```bash
   git add .
   git commit -m "Implementa interfaces y funciones de colecciones para [tu empresa]"
   ```

3. Sube tu rama al repositorio remoto:

   ```bash
   git push origin hito-2-fundamentos-programacion
   ```

4. Abre un Pull Request desde tu rama hacia `main` en tu repositorio

5. En la descripción del PR incluye:
   - Qué funcionalidades implementaste
   - Qué desafíos encontraste y cómo los resolviste
   - Capturas de pantalla si implementaste la interfaz de prueba (opcional)

6. Entrega el enlace de tu Pull Request en la plataforma de 4Geeks

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack).
