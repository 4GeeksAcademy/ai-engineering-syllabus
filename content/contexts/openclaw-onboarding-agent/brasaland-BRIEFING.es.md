# BRIEFING — Brasaland
## Agente de Onboarding con Memoria · W6D16

---

## La empresa

Brasaland es una cadena de restaurantes de parrilla con 14 locales en Colombia y Florida. El equipo de operaciones y cocina rota con frecuencia, lo que hace que los procesos de incorporación sean constantes y a menudo simultáneos. Ashley Turner (People Manager, Miami) es la responsable de RRHH para toda la cadena y quien interactúa con el agente.

---

## Personaje de RRHH

| Campo | Valor |
|---|---|
| Nombre | Ashley Turner |
| Cargo | People Manager |
| Ubicación | Miami |
| Estilo de comunicación | Mensajes cortos y directos. Espera confirmaciones concretas, sin rodeos. |
| Handle de Telegram | `@ashley_brasaland` |

---

## Template de email de bienvenida

> **Asunto:** Welcome to Brasaland — next steps to complete your onboarding
>
> Hi [nombre],
>
> We're glad to have you joining the Brasaland team. Before your first day, we need to complete a few steps to get you set up.
>
> Please message our onboarding bot on Telegram to continue the process. You'll find it at **[handle del bot]**.
>
> Once you make contact, the bot will guide you through everything you need to do.
>
> See you soon,
> **Brasaland People Team**

*Nota: el email se envía en inglés porque Ashley opera desde Miami y la plantilla corporativa está en inglés. Si el estudiante ha implementado soporte bilingüe, puede enviar una versión en español para locales colombianos.*

---

## Instrucciones de onboarding

El agente entrega estas instrucciones a la nueva persona en el paso 7, tras la verificación de identidad:

> Bienvenido/a al equipo Brasaland. Para completar tu incorporación necesito que me confirmes los siguientes puntos, uno por uno:
>
> 1. ¿Cuál es tu nombre completo tal como aparece en tu documento de identidad?
> 2. ¿A qué local has sido asignado/a? (ciudad y nombre del local)
> 3. ¿Cuál es tu número de cuenta bancaria para el pago de nómina?
> 4. ¿Cuál es tu talla de uniforme? (XS / S / M / L / XL / XXL)
> 5. Confirma que has leído el Manual de Manipulación de Alimentos e indica la fecha en que lo completaste.
> 6. Confirma que has realizado el recorrido de cocina con tu supervisor e indica su nombre.
>
> Cuando haya recibido todas tus respuestas, marcaré tu proceso como completado y notificaré a RRHH.

---

## Entregables requeridos y cómo el agente verifica cada uno

| # | Entregable | Qué espera el agente |
|---|---|---|
| 1 | Nombre completo | Texto libre (nombre y apellidos) |
| 2 | Local asignado | Ciudad + nombre del local (ej. "Medellín, El Poblado") |
| 3 | Número de cuenta bancaria | Número de cuenta (texto libre) |
| 4 | Talla de uniforme | Una de las opciones: XS / S / M / L / XL / XXL |
| 5 | Confirmación del manual | Confirmación explícita + fecha (ej. "Leído el 12 de mayo") |
| 6 | Confirmación del recorrido | Confirmación explícita + nombre del supervisor |

El proceso se marca como **terminado** cuando el agente ha recibido respuesta a los seis puntos.

---

## Esquema de memoria por empleado

```
empleado:
  nombre_completo: string
  correo: string
  local_asignado: string | null
  talla_uniforme: string | null
  cuenta_bancaria: string | null
  manual_confirmado: boolean
  manual_fecha: string | null
  recorrido_confirmado: boolean
  recorrido_supervisor: string | null
  estado: "no_iniciado" | "activo" | "terminado"
  fecha_inicio: string
  fecha_cierre: string | null
```

---

## Reglas de negocio

- Un empleado puede ser asignado a cualquiera de los 14 locales. El agente no valida cuál — solo registra lo que se le indica.
- El número de cuenta puede ser colombiano (cuenta de ahorros o corriente) o estadounidense (routing + account number). El agente acepta cualquier formato.
- El proceso no tiene fecha límite forzada, pero el resumen matutino permite a Ashley detectar casos inactivos desde hace más de 48 horas.
