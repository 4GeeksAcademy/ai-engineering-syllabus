# Ejemplo en Clase: Dashboard de un Gimnasio

> **Nota para el instructor:** Este es un ejemplo en vivo para clase que enseña los conceptos del proyecto `simple-dashboard-tailwind-css`. Usa este escenario para guiar a los estudiantes en la construcción de un dashboard responsivo con Tailwind CSS y HTML semántico usando un enfoque mobile-first. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Un pequeño gimnasio de barrio quiere un dashboard web sencillo para ver el estado de su negocio de un vistazo. El dueño lo consulta cada mañana desde el móvil y en el monitor de escritorio de la recepción. Necesita saber:

- ¿Cuántos socios activos tiene este mes?
- ¿Cuántos ingresos generaron las membresías?
- ¿Qué clases se están llenando y cuáles están vacías?
- ¿Los socios están renovando o cancelando?

Tu tarea: construir una página única en **HTML + Tailwind CSS v4** (sin frameworks, sin lógica JavaScript) que presente estos datos de forma clara en pantallas de móvil, tablet y escritorio.

---

## Configuración

Añade el CDN de Tailwind CSS v4 en tu `<head>`:

```html
<head>
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
```

> ⚠️ Indica a tu asistente de IA que use **Tailwind CSS v4** y que evite `cdn.tailwindcss.com` o cualquier CDN de Tailwind v3.

---

## Datos de Ejemplo (usa estos en el dashboard)

**Tipos de membresía:**

| Tipo | Precio mensual | Socios activos |
|---|---|---|
| Básica | 29 € | 85 |
| Estándar | 49 € | 120 |
| Premium | 79 € | 40 |

**Clases de esta semana:**

| Clase | Aforo | Inscritos | Día |
|---|---|---|---|
| Yoga Matinal | 15 | 14 | Lun / Mié / Vie |
| HIIT | 20 | 20 | Mar / Jue |
| Spinning | 18 | 9 | Lun / Mié |
| Pilates | 12 | 12 | Mar / Vie |

**Resumen mensual:**
- Nuevos socios este mes: **18**
- Bajas este mes: **5**
- Crecimiento neto: **+13**
- Ingresos totales: **12.745 €**

---

## Estructura del Dashboard

Construye el dashboard en **tres bloques verticales**:

### Bloque 1 — KPIs (superior)

Muestra al menos **3 tarjetas de KPI**, por ejemplo:

- Total de socios activos: **245**
- Ingresos mensuales: **12.745 €**
- Tasa media de ocupación de clases: **87%**

### Bloque 2 — Drivers (intermedio)

Muestra al menos **3 visualizaciones de drivers**, por ejemplo:

- Desglose de ingresos por tipo de membresía (usa una barra CSS sencilla o Chart CSS si está disponible)
- Retención de socios este mes: altas vs. bajas
- Las 3 clases con mayor tasa de ocupación

### Bloque 3 — Detalles Operacionales (inferior)

- Tabla completa de horario de clases (nombre, aforo, inscritos, % ocupación, días)
- Tabla de tipos de membresía (tipo, precio, socios activos, ingresos)

---

## Requisitos

- [ ] Usa **HTML semántico**: `<header>`, `<main>`, `<section>`, `<table>`, `<nav>` donde corresponda
- [ ] Aplica estilos usando **solo clases utility de Tailwind** — sin CSS personalizado, sin otros frameworks
- [ ] Diseña **mobile-first**: empieza con un layout de una sola columna y luego expande con los breakpoints `sm:`, `md:`, `lg:`
- [ ] Las tarjetas de KPI deben ser visualmente consistentes (misma estructura, mismo padding, misma jerarquía de texto)
- [ ] El layout no debe romperse ni requerir scroll horizontal en pantallas pequeñas

---

## Preguntas de Discusión

1. ¿Por qué separamos el dashboard en bloques de KPI / Driver / Operacional? ¿Qué tipo de decisión apoya cada bloque para el dueño del gimnasio?
2. Usaste los breakpoints `sm:`, `md:` y `lg:`. ¿Qué ocurre en una pantalla más pequeña que `sm:`? ¿Por qué el enfoque mobile-first importa en la práctica?
3. Los datos de este dashboard están escritos directamente en el HTML. ¿Cómo se vería diferente este dashboard si estuviera conectado a una base de datos en tiempo real? ¿Qué habría que cambiar en el código?
