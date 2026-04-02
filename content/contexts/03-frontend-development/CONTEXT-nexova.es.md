# CONTEXT — Nexova · Hito 3: Talent Pipeline Tracker

> **Ruta en el repositorio:** `03-talent-pipeline-tracker/CONTEXT-nexova.es.md`

---

## Tu empresa

Eres parte del equipo de Ingeniería de IA de **Nexova**, una consultora de recursos humanos y adquisición de talento con oficinas en Valencia y Miami. El negocio principal de Nexova es exactamente lo que esta herramienta soporta: encontrar a las personas adecuadas. Construir este frontend no es solo un proyecto interno — es una demostración directa de las propias capacidades de Nexova.

---

## El encargo

Elena Vargas, L&D Manager, ha enviado el siguiente correo con copia a Sergio Molina, CTO:

> **Para:** Sergio Molina (CTO)
> **CC:** Equipo de Ingeniería de IA
> **Asunto:** URGENTE — Necesitamos la herramienta de gestión de candidaturas esta semana
>
> Sergio,
>
> Te escribo directamente porque la situación con el proceso de selección del **Asistente de Dirección** se ha vuelto inmanejable. Hemos recibido más de cien candidaturas y mi equipo sigue trabajando desde una hoja de cálculo compartida. Ayer encontramos entradas duplicadas y al menos un candidato cuyo estado no se había actualizado en dos semanas.
>
> Sé que el backend está listo — hablé con Javier y me lo confirmó. Necesito que alguien de tu equipo monte el frontend ahora. No podemos seguir llevando un proceso de selección para nuestra propia empresa en una hoja de cálculo. Es un problema de imagen y nos está costando candidatos.
>
> Lo que necesito que haga la herramienta:
> - Mostrar todas las candidaturas en un listado con nombre, puesto, estado y etapa de un vistazo.
> - Filtrar por estado y etapa, y buscar por nombre o email sin recargar la página.
> - Abrir el detalle de un candidato y actualizar su estado o etapa desde ahí.
> - Añadir notas internas después de cada llamada o entrevista, y eliminarlas cuando ya no sean necesarias.
> - Registrar candidatos que llegan por otras vías y corregir datos cuando vienen mal.
>
> Por favor, ponlo como prioridad.
>
> Elena

---

## Contexto del proceso de selección

| Campo | Valor |
|---|---|
| Puesto | Asistente de Dirección |
| Empresa | Nexova |
| Ubicación | Sede de Valencia |
| Perfil buscado | Experiencia en asistencia ejecutiva, gestión de agenda y viajes, inglés y español profesionales |

---

## API y datos

La API mock está desplegada de forma centralizada y es compartida por todos los contextos del curso. Los campos, valores y estructura son los definidos en la especificación técnica del backend. No es necesario adaptarlos.

### Valores de `status`

| Valor API | Etiqueta en la UI |
|---|---|
| `received` | Recibida |
| `in_progress` | En proceso |
| `selected` | Seleccionada |
| `discarded` | Descartada |

### Valores de `stage`

| Valor API | Etiqueta en la UI |
|---|---|
| `pending` | Pendiente de revisión |
| `review` | En revisión |
| `personal_interview` | Entrevista personal |
| `technical_interview` | Entrevista técnica |
| `offer_presented` | Oferta presentada |

> Los valores crudos de la API (`in_progress`, `personal_interview`, etc.) no deben aparecer nunca en la interfaz. Usa siempre las etiquetas de esta tabla.

---

## Criterios de aceptación específicos

- Los estados y etapas muestran etiquetas legibles, nunca valores de API.
- Las notas internas son visibles únicamente en el detalle del candidato.
- El formulario de registro incluye todos los campos requeridos por la API.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_Contexto de uso exclusivo en la generación de proyectos del programa_
