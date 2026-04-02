# CONTEXT — HealthCore · Hito 3: Talent Pipeline Tracker

> **Ruta en el repositorio:** `03-talent-pipeline-tracker/CONTEXT-healthcore.es.md`

---

## Tu empresa

Eres parte de **HealthCore Digital**, la unidad tecnológica interna de HealthCore, una empresa de servicios sanitarios ambulatorios con 12 clínicas en Estados Unidos y el Reino Unido. Todo lo que construyes da soporte a procesos operativos que afectan al personal clínico y, de forma indirecta, a la atención al paciente. Las herramientas que fallan en silencio no son aceptables.

---

## El encargo

Diane Foster, VP de People, ha enviado el siguiente correo con copia a James Osei, CTO:

> **Para:** James Osei (CTO)
> **CC:** Equipo HealthCore Digital
> **Asunto:** URGENTE — Necesitamos la herramienta de candidaturas esta semana
>
> James,
>
> Necesito escalar esto directamente. Estamos en medio de la selección de un **Asistente de Dirección** para la sede de Austin y el proceso ha superado con creces lo que podemos gestionar con nuestra configuración actual. Tenemos más de cien candidaturas y mi equipo lo está gestionando todo en una hoja de cálculo compartida. Esta mañana he encontrado que el estado de dos candidatos había sido sobreescrito por error y uno de ellos ya tenía una entrevista programada.
>
> Hablé con el equipo técnico la semana pasada y me confirmaron que el backend está listo. Necesito que alguien construya el frontend ahora. No puedo llevar un proceso de selección profesional para nuestra propia sede en una hoja de cálculo — especialmente cuando al mismo tiempo le pedimos a los equipos clínicos que confíen en nuestros sistemas.
>
> Lo que necesito que haga la herramienta:
> - Mostrar todas las candidaturas en un listado con nombre, puesto, estado y etapa visibles de inmediato.
> - Filtrar por estado y etapa, y buscar por nombre o email sin recargar la página.
> - Abrir el detalle completo de un candidato y actualizar su estado o etapa desde ahí.
> - Añadir notas internas después de cada llamada o entrevista, y eliminarlas cuando ya no sean relevantes.
> - Registrar candidatos que llegan por referencias y corregir datos cuando llegan incorrectos.
>
> Por favor, que sea la prioridad de tu equipo esta semana.
>
> Diane

---

## Contexto del proceso de selección

| Campo | Valor |
|---|---|
| Puesto | Asistente de Dirección |
| Empresa | HealthCore |
| Ubicación | Sede de Austin |
| Perfil buscado | Experiencia en asistencia ejecutiva, gestión de agenda y viajes, inglés profesional, discreción en el manejo de información sensible |

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
