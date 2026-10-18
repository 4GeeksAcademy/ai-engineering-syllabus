# BRIEFING — TrackFlow
## Agente de Onboarding con Memoria · W6D16

---

## La empresa

TrackFlow gestiona almacenes y última milla en Los Ángeles y Zaragoza. Incorpora principalmente operarios de almacén, coordinadores logísticos y personal de atención al cliente, con flujos de contratación frecuentes en temporadas de mayor volumen. Las dos operaciones tienen legislaciones laborales distintas (California / España) y equipos de trabajo separados. El equipo de People está liderado por quien gestiona RRHH para ambas operaciones desde Zaragoza.

---

## Personaje de RRHH

| Campo | Valor |
|---|---|
| Nombre | Elena Morales |
| Cargo | People & Culture Manager |
| Ubicación | Zaragoza |
| Estilo de comunicación | Práctica y eficiente. Prefiere datos concretos y confirmaciones sin ambigüedad. |
| Handle de Telegram | `@elena_trackflow` |

---

## Template de email de bienvenida

> **Asunto:** Bienvenido/a a TrackFlow — comienza tu proceso de incorporación
>
> Hola [nombre],
>
> Estamos encantados de que te unas al equipo TrackFlow. Para que puedas empezar el primer día con todo listo, necesitamos completar algunos pasos antes.
>
> Escríbele a nuestro asistente de incorporación por Telegram en **[handle del bot]**. Él te guiará por cada paso.
>
> Hasta pronto,
> **Equipo de Personas — TrackFlow**

*Nota: si el empleado está asignado a Los Ángeles, el agente puede enviar el email en inglés. Si el estudiante ha implementado soporte bilingüe, el template en inglés está disponible como variante.*

---

## Instrucciones de onboarding

El agente entrega estas instrucciones en el paso 7, tras la verificación de identidad:

> ¡Bienvenido/a a TrackFlow! Para completar tu incorporación necesito que me confirmes los siguientes datos, uno por uno:
>
> 1. ¿Cuál es tu nombre completo tal como aparece en tu documento de identidad o pasaporte?
> 2. ¿En qué operación trabajarás? (Los Ángeles / Zaragoza)
> 3. ¿Cuál es tu turno asignado? (mañana / tarde / noche)
> 4. ¿Cuál es tu talla de equipo de protección? Indica talla de guantes (S / M / L / XL) y talla de chaleco (S / M / L / XL / XXL).
> 5. Confirma que has completado la formación de seguridad en almacén e indica la fecha en que la finalizaste.
> 6. Confirma que conoces a tu supervisor directo e indica su nombre.
>
> Cuando reciba todas tus respuestas, marcaré tu proceso como completado y lo comunicaré a Elena.

---

## Entregables requeridos y cómo el agente verifica cada uno

| # | Entregable | Qué espera el agente |
|---|---|---|
| 1 | Nombre completo | Texto libre (nombre y apellidos) |
| 2 | Operación asignada | "Los Ángeles" o "Zaragoza" |
| 3 | Turno asignado | "mañana", "tarde" o "noche" |
| 4 | Talla de EPI | Talla de guantes + talla de chaleco (ej. "guantes M, chaleco L") |
| 5 | Confirmación de formación de seguridad | Confirmación explícita + fecha (ej. "Completada el 3 de mayo") |
| 6 | Confirmación de supervisor | Confirmación explícita + nombre del supervisor |

El proceso se marca como **terminado** cuando el agente ha recibido respuesta a los seis puntos.

---

## Esquema de memoria por empleado

```
empleado:
  nombre_completo: string
  correo: string
  operacion: "Los Ángeles" | "Zaragoza" | null
  turno: "mañana" | "tarde" | "noche" | null
  talla_guantes: string | null
  talla_chaleco: string | null
  formacion_seguridad_completada: boolean
  formacion_seguridad_fecha: string | null
  supervisor_confirmado: boolean
  supervisor_nombre: string | null
  estado: "no_iniciado" | "activo" | "terminado"
  fecha_inicio: string
  fecha_cierre: string | null
```

---

## Reglas de negocio

- La operación asignada (campo `operacion`) determina el contexto laboral: Los Ángeles opera bajo legislación californiana, Zaragoza bajo legislación española. El agente no aplica ninguna lógica diferencial — solo registra el valor.
- La formación de seguridad es obligatoria para todos los roles de almacén. El proceso no puede marcarse como terminado si `formacion_seguridad_completada` es `false`.
- Para los turnos de noche, Elena necesita confirmación explícita del supervisor porque la asignación nocturna requiere validación adicional del responsable de operaciones. El agente registra el nombre sin validarlo.
- El resumen matutino es especialmente útil para Elena en períodos de contratación masiva: permite ver de un vistazo cuántos procesos hay abiertos simultáneamente y cuántos llevan más de 24 horas sin avanzar.
