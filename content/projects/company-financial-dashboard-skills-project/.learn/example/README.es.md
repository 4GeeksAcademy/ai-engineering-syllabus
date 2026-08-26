# Ejemplo en Clase: Mejorando el Catálogo de Biblioteca con Agent Skills

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio continúa con la app de catálogo de biblioteca comunitaria del proyecto de contexto — mismo flujo agent-first de cargar, aplicar y crear skills sobre un codebase heredado, con un repo más pequeño que el dashboard financiero.

_These instructions are also available in [English](./README.md)._

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo flujo agent-first y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Continúas en el **repo heredado del catálogo de biblioteca** del proyecto de contexto. Tu `memory-bank/` y `.agents/rules` ya están en su sitio. La app funciona, pero tu tech lead quiere subir el nivel en dos frentes antes del merge: accesibilidad y buenas prácticas de despliegue. Compartieron dos agent skills para tu coding agent. Después de aplicarlas (agent al mando, tú verificas), explora el ecosistema de skills y escribe una **skill interna del proyecto** — commits, despliegue, testing, o algo específico del catálogo descubierto en el codebase.

---

## Conceptos Cubiertos

| Concepto                            | Dónde se aplica                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| Aplicación agent-first de skills    | El agent audita y propone; el estudiante verifica antes del commit                      |
| Skill `accessibility`               | Auditar y corregir aria labels, alt text, navegación por teclado                        |
| Skill `vercel-react-best-practices` | `next/image`, API de metadata, build sin advertencias                                   |
| `npx skills find`                   | Descubrir skills de la comunidad por tema                                               |
| Skill interna del proyecto          | Skill específica del repo (commits, despliegue, QA o reglas de dominio) con criterios de aceptación |
| Actualización del memory bank       | Reflejar cambios verificados en `memory-bank/status.md`                                  |

---

## Punto de Partida

Continúa desde el proyecto de ejemplo local usado en el proyecto de contexto. Confirma que existen `memory-bank/` y `.agents/rules`.

Crea una nueva rama antes de empezar:

```bash
git switch -c feature/agent-skills
```

Pide al agent cómo ejecutar la app y qué comando de build valida el frontend.

---

## Qué Hacer

### 1. Descubrir y revisar las skills proporcionadas

- [ ] Ejecuta `npx skills find accessibility` y lee en qué consiste la skill antes de cargarla
- [ ] Ejecuta `npx skills find vercel-react-best-practices` y léela también
- [ ] Carga ambas skills en tu coding agent y confirma que el agent entiende sus instrucciones

### 2. Aplicar la skill `accessibility` (agent al mando, tú verificas)

- [ ] Pide al agent (con la skill `accessibility` cargada) que audite el frontend del catálogo y proponga correcciones
- [ ] Revisa cada propuesta; acepta solo cambios ligados a un archivo e instrucción de la skill
- [ ] Verifica resultados: tarjetas de libros, búsqueda y navegación por teclado; `alt`; contraste básico
- [ ] Commit referenciando la skill `accessibility`

### 3. Aplicar la skill `vercel-react-best-practices` (agent al mando, tú verificas)

- [ ] Pide al agent que audite patrones orientados a despliegue y aplique correcciones que la skill señale
- [ ] Revisa propuestas — p. ej. `next/image` en portadas, metadata en catálogo y detalle
- [ ] Confirma que el comando de build del repo pasa sin advertencias nuevas injustificadas
- [ ] Commit referenciando la skill `vercel-react-best-practices`

### 4. Explorar el ecosistema

- [ ] Ejecuta `npx skills find <tema>` para al menos dos temas relevantes (sugerencias: `forms`, `seo`, `typescript`, `testing`)
- [ ] Aplica al menos una skill adicional — añade una justificación de una frase en `memory-bank/status.md`

### 5. Escribir una skill interna del proyecto

Con el agent, identifica un gap específico de este repo heredado que las skills comunitarias no cubren bien. Buenas opciones:

- Convenciones de commit o PR para este repo de equipo
- Cómo ejecutar smoke checks antes del merge (testing/QA)
- Cómo mostrar y ordenar resultados de búsqueda de libros
- Gestión de estados vacíos cuando la búsqueda no devuelve resultados

Escribe un archivo de skill en `.skills/library-catalog-<tema>.md` con:

| Sección                     | Qué incluir                                         |
| --------------------------- | --------------------------------------------------- |
| **Objetivo**                | Una frase: qué enforcea esta skill                  |
| **Inputs**                  | A qué archivos o componentes se aplica              |
| **Salida esperada**         | Cómo es una implementación que cumple los criterios |
| **Criterios de aceptación** | 2–3 condiciones verificables                        |

- [ ] Carga la skill en el agent y verifica que la orientación es específica y útil en una tarea real

### 6. Actualizar el memory bank

- [ ] Actualiza `memory-bank/status.md` para reflejar: skills aplicadas, cambios verificados, skill del ecosistema elegida y la skill interna que creaste

---

## Preguntas para Discusión

1. ¿Cuál es la diferencia entre una skill y una regla de proyecto (en `.agents/rules`)? ¿Cuándo usarías cada una?
2. Después de aplicar la skill `accessibility`, el agent sugirió añadir `aria-label` al botón de búsqueda. ¿Cómo verificarías que esto realmente ayuda a un usuario de lector de pantalla?
3. ¿Por qué escribir una skill interna para commits o testing si existen skills comunitarias?
4. Tu skill interna tiene pocas líneas. Un compañero dice que es "demasiado corta para ser útil". ¿Cómo defenderías que sea concisa?
