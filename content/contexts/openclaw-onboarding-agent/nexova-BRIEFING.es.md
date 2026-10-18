# BRIEFING — Nexova
## Agente de Onboarding con Memoria · W6D16

---

## La empresa

Nexova es una consultora de RRHH y adquisición de talento con sede en Valencia y oficina en Miami. Incorpora perfiles muy distintos — consultores de selección, agentes de soporte, formadores y personal administrativo — con cadencias diferentes según la carga de proyectos. Patricia Solís (HR Manager) es la responsable de RRHH y quien interactúa con el agente.

---

## Personaje de RRHH

| Campo | Valor |
|---|---|
| Nombre | Patricia Solís |
| Cargo | HR Manager |
| Ubicación | Valencia |
| Estilo de comunicación | Directa y organizada. Envía mensajes precisos y espera respuestas igualmente precisas. |
| Handle de Telegram | `@patricia_nexova` |

---

## Template de email de bienvenida

> **Asunto:** Bienvenido/a a Nexova — completa tu proceso de incorporación
>
> Hola [nombre],
>
> Nos alegra que te incorpores al equipo Nexova. Para completar tu alta antes de tu primer día, necesitamos que realices algunos pasos a través de nuestro asistente de incorporación.
>
> Escríbele por Telegram en **[handle del bot]** para comenzar. El asistente te guiará paso a paso.
>
> Un saludo,
> **Equipo de Personas — Nexova**

---

## Instrucciones de onboarding

El agente entrega estas instrucciones en el paso 7, tras la verificación de identidad:

> ¡Hola! Soy el asistente de incorporación de Nexova. Para completar tu alta en el sistema necesito que me confirmes los siguientes datos, uno por uno:
>
> 1. ¿Cuál es tu nombre completo tal como aparece en tu DNI o pasaporte?
> 2. ¿Cuál es tu número de identificación fiscal (NIF, NIE o Tax ID)?
> 3. ¿En qué oficina trabajarás principalmente? (Valencia / Miami)
> 4. ¿Cuál es el nombre de usuario que quieres usar en los sistemas internos de Nexova? (sin espacios ni caracteres especiales)
> 5. Confirma que has leído y aceptado el Código de Conducta e indica la fecha en que lo hiciste.
> 6. Confirma que has tenido tu sesión de bienvenida con tu manager e indica su nombre.
>
> Cuando reciba todas tus respuestas, tu proceso de incorporación quedará completado y lo comunicaré a Patricia.

---

## Entregables requeridos y cómo el agente verifica cada uno

| # | Entregable | Qué espera el agente |
|---|---|---|
| 1 | Nombre completo | Texto libre (nombre y apellidos) |
| 2 | Número de identificación fiscal | NIF / NIE / Tax ID (texto libre) |
| 3 | Oficina principal | "Valencia" o "Miami" |
| 4 | Nombre de usuario elegido | Texto sin espacios ni caracteres especiales |
| 5 | Confirmación del Código de Conducta | Confirmación explícita + fecha (ej. "Aceptado el 8 de mayo") |
| 6 | Confirmación de sesión de bienvenida | Confirmación explícita + nombre del manager |

El proceso se marca como **terminado** cuando el agente ha recibido respuesta a los seis puntos.

---

## Esquema de memoria por empleado

```
empleado:
  nombre_completo: string
  correo: string
  identificacion_fiscal: string | null
  oficina: "Valencia" | "Miami" | null
  nombre_usuario: string | null
  codigo_conducta_confirmado: boolean
  codigo_conducta_fecha: string | null
  sesion_bienvenida_confirmada: boolean
  sesion_bienvenida_manager: string | null
  estado: "no_iniciado" | "activo" | "terminado"
  fecha_inicio: string
  fecha_cierre: string | null
```

---

## Reglas de negocio

- El nombre de usuario no puede contener espacios ni caracteres especiales. Si la respuesta no cumple el formato, el agente debe pedirla de nuevo antes de registrarla.
- El número de identificación fiscal puede ser un NIF o NIE (para empleados en España) o un Tax ID (para empleados en Miami). El agente acepta cualquier formato sin validar su estructura.
- El proceso no puede marcarse como terminado si faltan el número fiscal o la confirmación del Código de Conducta, ya que ambos tienen implicaciones legales.
- Patricia utiliza el resumen matutino principalmente para detectar personas con proceso no iniciado: empleados reportados que aún no han contactado al bot a uno o dos días de su fecha de incorporación.
