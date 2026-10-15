# Frontends de Refugio de Mascotas — Mini auditoría Lighthouse (Ejemplo en clase)

> **Para instructores:** Escenario paralelo para `ai-eng-frontend-performance-audit`. Mismo ciclo (medir → analizar → corregir → volver a medir) y mismo patrón de documentación, dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` de la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Paws & Co. Rescue** mantiene un monorepo Next.js pequeño: web pública de adopciones (`adopt-site`) y app de ingreso para el personal (`intake-app`). Crece el tráfico de adopciones; el personal dice que el panel va lento. En una sesión, demuestra el ciclo de auditoría en **una página por app** — no el alcance completo corporativo/backoffice del proyecto evaluable.

### Nota de alcance

| Proyecto evaluable                       | Este ejemplo en clase                            |
| ---------------------------------------- | ------------------------------------------------ |
| Sitio corporativo + backoffice empresa   | Web de adopciones + panel de ingreso             |
| Escritorio + móvil en web pública        | Solo escritorio (ahorra tiempo)                  |
| ≥2 candidatos a refactor documentados    | 1 patrón duplicado → 1 hook compartido           |
| Checklist CTO + skills de agente         | Lighthouse + 1 corrección concreta + docs breves |
| `audit/before` + `audit/after` completos | 2 capturas por fase (4 en total)                 |

---

## Qué construir

### 1. Lighthouse inicial

- [ ] Ejecutar Lighthouse (DevTools de Chrome) en la home de `adopt-site` (`/`) — **escritorio**.
- [ ] Ejecutar Lighthouse en la vista principal de listado de `intake-app` (p. ej. `/animals`) — **escritorio**.
- [ ] Guardar PNG en `audit/before/adopt-home.png` y `audit/before/intake-list.png`.

Anotar las cuatro puntuaciones por ejecución: Performance, Accessibility, Best Practices, SEO (en intake puede no aplicar SEO — indícalo).

### 2. Revisión rápida del código

- [ ] Encontrar **un** patrón duplicado (p. ej. mismo `useEffect` de fetch + UI de carga en dos componentes).
- [ ] Anotar en un `AUDIT.md` breve: rutas de archivos, por qué perjudica el mantenimiento, nombre propuesto del hook.

### 3. Una corrección + un refactor

- [ ] Aplicar **una** corrección motivada por Lighthouse (p. ej. `next/image` en la imagen LCP, o `font-display: swap`).
- [ ] Extraer **un** hook `useAsyncList(url)` (o similar) usado en al menos un componente.

### 4. Segunda medición

- [ ] Volver a ejecutar Lighthouse en las mismas dos URLs.
- [ ] Guardar en `audit/after/` con los mismos nombres de archivo.
- [ ] Escribir `REPORT.md` (media página): qué cambió, tabla antes/después solo de Performance.

---

## Verificar juntos

- [ ] Existen ambas carpetas `audit/` en el repo con imágenes commiteadas.
- [ ] `AUDIT.md` incluye una frase de causa raíz para la corrección elegida (no solo etiquetas de Lighthouse).
- [ ] El hook compartido se importa en código real (no código muerto).
- [ ] Las apps siguen sirviendo en modo producción (`npm run build` + `npm run start`, o el comando del monorepo); las capturas de Lighthouse deben salir de ese servidor, no de `npm run dev`.

---

## Preguntas para debatir

1. ¿Por qué auditar solo la home es insuficiente en una app con varias rutas? ¿Cuándo añadirías una segunda URL?
2. ¿Qué diferencia hay entre una **oportunidad** de Lighthouse y una corrección que ataca la **causa raíz**?
3. ¿Cómo adaptarías este ciclo a CI más adelante (presupuestos, Lighthouse CI, comprobaciones sintéticas)?
