# Ejemplo en Clase: Mejorando el Catálogo de Biblioteca con Agent Skills

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio continúa con la app de catálogo de biblioteca comunitaria de la sesión de contexto anterior — mismo flujo de trabajo de cargar, aplicar y crear agent skills, con una base de código más accesible que el dashboard financiero.

## El Escenario

La app del catálogo de biblioteca está funcionando, pero tu tech lead ha señalado dos áreas antes de que la rama pueda fusionarse: accesibilidad y buenas prácticas de despliegue. Han compartido dos agent skills para guiar a tu asistente de IA. Después de aplicarlas, explorarás el ecosistema de skills y escribirás una skill personalizada específica para el catálogo.

---

## Conceptos Cubiertos

| Concepto | Dónde se aplica |
|---|---|
| Agent skills | Cargar conjuntos de instrucciones estructurados en un agente de código |
| Skill `accessibility` | Auditar y corregir aria labels, alt text, navegación por teclado |
| Skill `vercel-react-best-practices` | `next/image`, API de metadata, build sin advertencias |
| `npx skills find` | Descubrir skills de la comunidad por tema |
| Creación de skill personalizada | Escribir una skill específica del proyecto con objetivo claro y criterios de aceptación |
| Actualización del memory bank | Reflejar los cambios de la sesión en `memory-bank/status.md` |

---

## Punto de Partida

Continúa en el mismo repositorio de la sesión anterior (el fork del catálogo de biblioteca). Si no lo tienes:

```
https://github.com/4GeeksAcademy/ai-eng-library-catalog-context-example
```

Crea una nueva rama antes de empezar:

```bash
git checkout -b feature/agent-skills
```

---

## Qué Hacer

### 1. Descubrir y revisar las skills proporcionadas

- [ ] Ejecuta `npx skills find accessibility` y lee en qué consiste la skill antes de cargarla
- [ ] Ejecuta `npx skills find vercel-react-best-practices` y léela también
- [ ] Carga ambas skills en tu agente de código y confirma que el agente entiende sus instrucciones

### 2. Aplicar la skill `accessibility`

- [ ] Pide al agente (con la skill `accessibility` cargada) que audite el frontend del catálogo de biblioteca
- [ ] Corrige todos los problemas de `aria-label` y `role` detectados
- [ ] Verifica que las tarjetas de libros, el input de búsqueda y los enlaces de navegación son accesibles por teclado (`Tab` / `Enter`)
- [ ] Añade o corrige el atributo `alt` en las imágenes de portadas de libros o iconos
- [ ] Comprueba que el contraste del texto y los botones cumple los estándares básicos de legibilidad

### 3. Aplicar la skill `vercel-react-best-practices`

- [ ] Sustituye las etiquetas `<img>` que muestran portadas de libros por `next/image`
- [ ] Asegúrate de que la página del catálogo y la página de detalle del libro tienen `<title>` y `<meta description>` correctos mediante la API de metadata de Next.js
- [ ] Elimina los anti-patrones detectados por la skill
- [ ] Confirma que el build pasa: `npm run build`

### 4. Explorar el ecosistema

- [ ] Ejecuta `npx skills find <tema>` para al menos dos temas relevantes para la app de biblioteca (sugerencias: `forms`, `seo`, `typescript`)
- [ ] Aplica al menos una skill adicional que consideres valiosa — añade una justificación de una frase en `memory-bank/status.md`

### 5. Escribir una skill personalizada

Identifica algo específico de este catálogo de biblioteca que no esté cubierto por las skills existentes. Buenas opciones:

- Cómo deben mostrarse y ordenarse los resultados de búsqueda de libros
- La convención de nombres para los parámetros de rutas de la API (p. ej., `isbn` vs `bookId`)
- Cómo gestionar los estados vacíos cuando una búsqueda no devuelve resultados

Escribe un archivo de skill en `.skills/library-catalog-<tema>.md` con:

| Sección | Qué incluir |
|---|---|
| **Objetivo** | Una frase: qué enforcea esta skill |
| **Inputs** | A qué archivos o componentes se aplica |
| **Salida esperada** | Cómo es una implementación que cumple los criterios |
| **Criterios de aceptación** | 2–3 condiciones verificables |

- [ ] Carga la skill en el agente y verifica que la orientación es específica y útil

### 6. Actualizar el memory bank

- [ ] Actualiza `memory-bank/status.md` para reflejar: skills aplicadas, cambios realizados y la skill personalizada que creaste

---

## Preguntas para Discusión

1. ¿Cuál es la diferencia entre una skill y una regla de proyecto (en `.agents/rules`)? ¿Cuándo usarías cada una?
2. Después de aplicar la skill `accessibility`, el agente sugirió añadir `aria-label` al botón de búsqueda. ¿Cómo verificarías que esto realmente ayuda a un usuario de lector de pantalla?
3. Tu skill personalizada tiene pocas líneas. Un compañero dice que es "demasiado corta para ser útil". ¿Cómo defenderías que sea concisa?
