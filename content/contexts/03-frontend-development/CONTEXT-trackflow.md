# CONTEXT — TrackFlow · Hito 3: Talent Pipeline Tracker

> **Ruta en el repositorio:** `03-talent-pipeline-tracker/CONTEXT-trackflow.md`

---

## Tu empresa

Eres parte del equipo **TrackFlow Tech**, la unidad tecnológica interna de TrackFlow, una empresa de logística de última milla y gestión de almacenes con operaciones en Los Ángeles y Zaragoza. El equipo está en plena transformación digital y cada herramienta que construyes tiene impacto directo en las operaciones del día siguiente.

---

## El encargo

Ana Whitfield, Head of Warehouse Operations, ha enviado el siguiente correo con copia a Andrés Kim, CTO:

> **Para:** Andrés Kim (CTO)
> **CC:** Equipo TrackFlow Tech
> **Asunto:** URGENTE — Herramienta de gestión de candidaturas — necesaria ya
>
> Andrés,
>
> Te escribo con copia al equipo porque esto no puede esperar más. Estamos gestionando el proceso de selección del **Asistente de Dirección** para la sede de Zaragoza en una hoja de Excel que ya nadie controla. Tenemos más de cien candidaturas, tres personas tocando el archivo y esta mañana hemos descubierto que alguien sobreescribió las notas de dos entrevistas de la semana pasada.
>
> Javier me confirmó ayer que el backend está listo. Necesito que alguien del equipo monte el frontend esta semana. El proceso de selección no se puede parar.
>
> Lo que necesito:
> - Ver todas las candidaturas con nombre, puesto, estado y etapa de un vistazo.
> - Filtrar por estado y etapa, y buscar por nombre o email sin recargar la página.
> - Entrar al detalle de cada candidato y cambiarle el estado o la etapa desde ahí.
> - Añadir notas después de las llamadas y entrevistas, y eliminarlas cuando ya no hagan falta.
> - Dar de alta candidatos que llegan por otras vías y editar datos cuando vienen mal.
>
> Gracias,
> Ana

---

## Contexto del proceso de selección

| Campo | Valor |
|---|---|
| Puesto | Asistente de Dirección |
| Empresa | TrackFlow |
| Ubicación | Sede Zaragoza |
| Perfil buscado | Experiencia en asistencia ejecutiva, gestión de agenda y viajes, inglés profesional, manejo de herramientas ofimáticas |

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
