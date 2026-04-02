# CONTEXT — Brasaland · Hito 3: Talent Pipeline Tracker

> **Ruta en el repositorio:** `03-talent-pipeline-tracker/CONTEXT-brasaland.md`

---

## Tu empresa

Eres parte del equipo **Brasaland Digital**, la unidad tecnológica interna de Brasaland, una cadena de restaurantes de parrilla con 14 locales en Colombia y Florida. Tu trabajo es construir las herramientas que los equipos operativos usarán en el día a día.

---

## El encargo

Ashley Turner, People Manager, ha enviado el siguiente correo con copia a Nicolás Park, CTO:

> **Para:** Nicolás Park (CTO)
> **CC:** Equipo Brasaland Digital
> **Asunto:** URGENTE — Necesitamos la herramienta de selección esta semana
>
> Nicolás,
>
> Te escribo porque ya no podemos seguir gestionando el proceso de selección del **Asistente de Dirección** en una hoja de Google Sheets. Llevamos más de cien candidaturas y tres personas editando el mismo archivo a la vez. Esta mañana hemos perdido los datos de dos candidatos por un error al guardar.
>
> Entiendo que el backend ya está listo. Necesito que alguien del equipo monte el frontend esta semana, no puede esperar más.
>
> Lo que necesito que haga la herramienta:
> - Ver todas las candidaturas de un vistazo: nombre, puesto, estado y etapa.
> - Filtrar por estado y etapa, y buscar por nombre o email sin recargar la página.
> - Entrar al detalle de cada candidato y poder cambiarle el estado o la etapa desde ahí.
> - Apuntar notas internas después de cada llamada o entrevista, y borrarlas si ya no sirven.
> - Registrar candidatos que llegan por otras vías y corregir datos cuando vienen mal.
>
> Gracias por escalarlo.
>
> Ashley

---

## Contexto del proceso de selección

| Campo | Valor |
|---|---|
| Puesto | Asistente de Dirección |
| Empresa | Brasaland |
| Ubicación | Sede corporativa, Medellín |
| Perfil buscado | Experiencia en asistencia ejecutiva, manejo de agenda y viajes corporativos, inglés profesional |

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
