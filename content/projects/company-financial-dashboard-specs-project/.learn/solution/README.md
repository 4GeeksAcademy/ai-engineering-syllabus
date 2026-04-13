# Company financial dashboard specs project — Solución de referencia

Este README describe qué debe incluir una entrega sólida y ofrece **ejemplos de especificaciones en lenguaje humano** (el tipo de instrucciones que se le darían a una IA o a otro desarrollador), alineadas con el [README principal del proyecto](../README.md).

El objetivo **no** es implementar React ni llamadas HTTP. El objetivo es producir artefactos de especificación que coincidan con la API real (`/docs`) y que permitan implementar sin preguntas pendientes.

> **Nota:** Los nombres de campos en los fragmentos TypeScript siguen el backend de referencia del dashboard financiero (p. ej. `outcome_total`, `baseline_average`, `increase_ratio`). El alumno debe **confirmar cada propiedad en `/docs`** de su propio entorno antes de entregar.

---

## Entregables esperados

En la rama `feature/frontend-specs`, bajo `frontend/specs/`:

| Archivo          | Contenido                                                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `api-types.ts`   | Interfaces estrictas: `FacetsResponse`, `AlertEntry`, `AlertsResponse`, `CategoryEntry`, `TopCategoriesResponse` (alineadas con OpenAPI). |
| `param-types.ts` | `DateRangeFilter`, `AlertsParams`, `TopCategoriesParams` (fechas opcionales `YYYY-MM-DD` con JSDoc).                                      |
| `components.md`  | Componentes nombrados, props tipadas, layout y renderizado condicional.                                                                   |
| `README.md`      | Contrato por funcionalidad: endpoints, tipos, parámetros y **≥ 2 casos límite** con comportamiento de UI.                                 |

---

## Ejemplos de especificaciones humanas para la IA

Estos bloques son **plantillas del tipo de texto** que el alumno puede escribir (en comentarios, en un chat con la IA o como criterio de aceptación) **antes** de congelar los archivos en `frontend/specs/`. Deben reflejar el README principal: mismas tres funcionalidades, mismas reglas de negocio.

### 1) Funcionalidad — Filtro de rango de fechas (dashboard principal)

**Instrucción tipo prompt para la IA:**

> En la parte superior del dashboard principal, añade dos controles de fecha (inicio y fin), opcionales, que envíen a la API `start_date` y `end_date` como strings `YYYY-MM-DD` en todos los endpoints de métricas que ya consume la página (incluido el resumen agregado). Si ambos están vacíos, no envíes esos query params y muestra todos los datos. Si solo uno está rellenado, [la spec del alumno debe fijar el comportamiento: p. ej. ignorar el filtro hasta que ambos sean válidos, o tratar el vacío como “sin límite” — debe ser explícito].  
> Carga una sola vez `GET /api/metrics/facets` y muestra cerca de los inputs un texto de ayuda con el rango disponible usando `min_date` y `max_date` de la respuesta (formateado legible para el usuario).  
> No implementes todavía: solo documenta tipos, props y reglas en los archivos de spec.

**Ejemplo mínimo en `api-types.ts` (facetas):**

```typescript
/**
 * Respuesta de GET /api/metrics/facets.
 * Las fechas vienen como ISO date (YYYY-MM-DD) en JSON.
 */
export interface FacetsResponse {
  /** Valores posibles de operation_type en el dataset */
  operation_types: ("income" | "outcome")[];
  /** Líneas de negocio presentes (p. ej. B2B, B2C) */
  business_types: string[];
  /** Categorías presentes en los movimientos */
  categories: string[];
  /** Fecha mínima con datos (YYYY-MM-DD) */
  min_date: string;
  /** Fecha máxima con datos (YYYY-MM-DD) */
  max_date: string;
}
```

**Ejemplo mínimo en `param-types.ts`:**

```typescript
/**
 * Filtro de rango opcional compartido por varias vistas.
 * Solo incluir en la query las claves que el usuario haya definido.
 */
export interface DateRangeFilter {
  /** Inicio inclusive; formato YYYY-MM-DD */
  start_date?: string;
  /** Fin inclusive; formato YYYY-MM-DD */
  end_date?: string;
}
```

---

### 2) Funcionalidad — Tabla de alertas de anomalías

**Instrucción tipo prompt para la IA:**

> Debajo de los gráficos del home, añade una tabla alimentada por `GET /api/metrics/alerts`. El usuario configura `threshold` con un número entre 0.01 y 1.0 (por defecto 0.3); si escribe un valor fuera de rango, [la spec debe decir: clamp, mensaje de error, deshabilitar envío, etc.].  
> Columnas: período; gasto (outcome) del período; media móvil de los tres períodos anteriores; incremento porcentual o ratio según defina el contrato con los campos reales de la API.  
> Si la respuesta es un array vacío, muestra un **estado vacío explícito** (título + texto), no una tabla sin filas sin explicación.  
> Reutiliza el mismo `DateRangeFilter` que en la funcionalidad 1: si hay rango activo, pásalo como `start_date` / `end_date` a alerts.

**Ejemplo mínimo en `api-types.ts` (alertas):**

```typescript
/** Una fila devuelta por GET /api/metrics/alerts */
export interface AlertEntry {
  /** Etiqueta del período (p. ej. mes o semana según group_by) */
  period: string;
  /** Total de outcome en ese período */
  outcome_total: number;
  /** Media de outcome de los 3 períodos anteriores */
  baseline_average: number;
  /** Ratio de aumento respecto a la baseline (según /docs) */
  increase_ratio: number;
}

/** La API devuelve un array de alertas (puede ser []) */
export type AlertsResponse = AlertEntry[];
```

**Ejemplo mínimo en `param-types.ts` (mismo archivo que `DateRangeFilter`):**

```typescript
export interface AlertsParams extends DateRangeFilter {
  /** Ratio de umbral; rango permitido en UI 0.01–1.0 (validar contra /docs) */
  threshold: number;
}
```

---

### 3) Funcionalidad — Vista comparativa B2B vs B2C

**Instrucción tipo prompt para la IA:**

> Crea una ruta nueva del dashboard con dos columnas. En cada columna, una tabla “top 5” de categorías de **ingresos** para esa línea de negocio: llama a `GET /api/metrics/categories/top` con `operation_type=income`, `limit=5` y `business_type=B2B` o `B2C`, más el mismo filtro de fechas opcional que en el home.  
> Columnas de cada tabla: nombre de categoría, total de ingresos, y **porcentaje sobre el total de ingresos de ese panel** (si la API no lo devuelve, la spec debe indicar que el front calcula `total_amount / sum(totals) * 100`).  
> Debajo, un único gráfico que compare el total de ingresos agregado B2B vs B2C en el rango seleccionado (la spec debe definir si es suma de `total_amount` de cada top-5 o agregación distinta — debe ser una sola regla clara).  
> Usa `GET /api/metrics/facets` para textos de ayuda o validaciones si el enunciado lo pide (categorías / líneas disponibles).

**Ejemplo mínimo en `api-types.ts` (categorías top):**

```typescript
/** Elemento de GET /api/metrics/categories/top */
export interface CategoryEntry {
  category: string;
  operation_type: "income" | "outcome";
  total_amount: number;
}

export type TopCategoriesResponse = CategoryEntry[];
```

**Ejemplo mínimo en `param-types.ts`:**

```typescript
export interface TopCategoriesParams extends DateRangeFilter {
  operation_type: "income" | "outcome";
  /** Entre 1 y el máximo que permita /docs (p. ej. 20) */
  limit: number;
  /** Filtra movimientos de la línea de negocio antes de agregar */
  business_type: "B2B" | "B2C";
}
```

---

## Ejemplo de fragmento para `components.md`

El alumno debe nombrar componentes reales de su diseño; aquí va un patrón **válido** de nivel de detalle:

```markdown
## Feature 1 — DateRangeFilterBar

- **Componente:** `DateRangeFilterBar`
- **Props:**
  - `value: DateRangeFilter` — estado controlado
  - `onChange: (next: DateRangeFilter) => void`
  - `facets: FacetsResponse | null` — para el hint; null mientras carga
- **Layout:** fila en la parte superior: [Inicio] [Fin] [texto de rango disponible]
- **Solo `start_date` relleno:** [describir: p. ej. no aplicar filtro hasta que ambas fechas sean válidas, mostrar mensaje inline]
- **Hint:** `Datos disponibles desde {facets.min_date} hasta {facets.max_date}`

## Feature 2 — OutcomeAlertsTable

- **Componente:** `OutcomeAlertsTable`
- **Props:** `alerts: AlertEntry[]`, `threshold: number`, `onThresholdChange`, `dateFilter: DateRangeFilter`, …
- **Empty state:** si `alerts.length === 0`, renderizar `EmptyState` con título "No hay anomalías" y texto que mencione el umbral actual.
- **Threshold inválido:** [describir comportamiento exacto]
```

---

## Ejemplo de fragmento para `frontend/specs/README.md` (contrato + edge cases)

```markdown
## Feature 2 — Anomalías

**Endpoints:** `GET /api/metrics/alerts`  
**Query:** `threshold`, opcionalmente `start_date`, `end_date` (y otros que figuren en /docs).  
**Response:** `AlertsResponse` (`AlertEntry[]`).

### Parámetros

- `threshold`: número; en UI restringido a [0.01, 1.0]; default 0.3.

### Edge cases

1. **Array vacío:** la UI muestra componente de estado vacío con copy fijo; no ocultar la sección.
2. **Rango de fechas sin datos:** la tabla muestra el mismo estado vacío o mensaje "Sin datos en este período" (la spec debe elegir una y ser consistente).
```

---

## Lista de comprobación (revisores)

- [ ] `npx tsc --noEmit` pasa en estricto (sin `any`, sin `object` genérico para payloads).
- [ ] Cada propiedad relevante tiene JSDoc (significado, formato, valores válidos).
- [ ] Los ejemplos anteriores se entienden como **referencia pedagógica**; la entrega del alumno debe **cuadrar con su `/docs`**.
- [ ] Commits en `feature/frontend-specs` con mensajes claros (tipos → componentes → contrato).

## Notas para revisores

- No evaluar componentes React, `fetch` ni cambios de backend en este proyecto.
- Priorizar coherencia con OpenAPI y completitud de casos límite descritos en el README principal.
