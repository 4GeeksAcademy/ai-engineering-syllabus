# BRIEFING — HealthCore
## Agente de Onboarding con Memoria · W6D16

---

## La empresa

HealthCore opera 12 clínicas ambulatorias en Estados Unidos (Texas, Florida, Georgia) y Reino Unido (Londres y Manchester). La incorporación de personal clínico está sujeta a requisitos de compliance regulatorio: ningún miembro del staff puede acceder a sistemas con datos de pacientes hasta haber completado la formación obligatoria en HIPAA (US) o UK GDPR (UK). Diane Foster (VP of People, Austin) es la responsable de RRHH y quien interactúa con el agente.

---

## Personaje de RRHH

| Campo | Valor |
|---|---|
| Nombre | Diane Foster |
| Cargo | VP of People |
| Ubicación | Austin, TX |
| Estilo de comunicación | Estructurada y metódica. Sus mensajes son claros y esperan confirmaciones precisas. |
| Handle de Telegram | `@diane_healthcore` |

---

## Template de email de bienvenida

> **Subject:** Welcome to HealthCore — complete your onboarding to get started
>
> Hi [name],
>
> Welcome to the HealthCore team. To ensure you're set up correctly and in compliance with our regulatory requirements, please complete your onboarding before your first day.
>
> Message our onboarding bot on Telegram at **[bot handle]** to begin. The bot will guide you through each step.
>
> Important: access to clinical systems will only be granted once all onboarding steps are confirmed.
>
> Best regards,
> **HealthCore People Team**

---

## Instrucciones de onboarding

El agente entrega estas instrucciones en el paso 7, tras la verificación de identidad:

> Welcome to HealthCore. To complete your onboarding, please provide the following information one step at a time:
>
> 1. What is your full legal name as it appears on your professional licence or ID?
> 2. Which clinic and country have you been assigned to? (e.g. "Austin Clinic 2, US" or "London North, UK")
> 3. What is your professional licence number? (If you are in an administrative role, reply "N/A".)
> 4. What is the expiry date of your professional licence? (If N/A, skip this step.)
> 5. Confirm that you have completed the mandatory compliance training module (HIPAA for US staff, UK GDPR for UK staff) and provide the date of completion.
> 6. Confirm that you have received your system login credentials from IT and provide the date you received them.
>
> Once I have received all your responses, I will mark your onboarding as complete and notify the People team.

---

## Entregables requeridos y cómo el agente verifica cada uno

| # | Entregable | Qué espera el agente |
|---|---|---|
| 1 | Nombre legal completo | Texto libre (nombre y apellidos) |
| 2 | Clínica y país asignados | Nombre de clínica + país (ej. "Austin Clinic 2, US") |
| 3 | Número de licencia profesional | Número o "N/A" para roles administrativos |
| 4 | Fecha de vencimiento de licencia | Fecha o saltado si paso 3 fue N/A |
| 5 | Confirmación de formación de compliance | Confirmación explícita + fecha (ej. "Completed 10 May") |
| 6 | Confirmación de credenciales IT | Confirmación explícita + fecha de recepción |

El proceso se marca como **terminado** cuando el agente ha recibido respuesta a todos los pasos aplicables según el rol.

---

## Esquema de memoria por empleado

```
empleado:
  nombre_legal: string
  correo: string
  clinica_asignada: string | null
  pais: "US" | "UK" | null
  numero_licencia: string | null
  licencia_vencimiento: string | null
  compliance_completado: boolean
  compliance_fecha: string | null
  credenciales_it_recibidas: boolean
  credenciales_it_fecha: string | null
  estado: "no_iniciado" | "activo" | "terminado"
  fecha_inicio: string
  fecha_cierre: string | null
```

---

## Reglas de negocio

- El campo `numero_licencia` es obligatorio para roles clínicos (physician, nurse practitioner, nurse). Para roles administrativos se acepta "N/A" y los pasos 3 y 4 quedan marcados automáticamente como completados.
- El paso de compliance es bloqueante: el proceso no puede marcarse como terminado si `compliance_completado` es `false`, independientemente de que el resto de pasos estén completados.
- El país determina qué módulo de compliance aplica: HIPAA para US, UK GDPR para UK. El agente no valida el contenido del módulo, solo la confirmación y la fecha.
- El resumen matutino es especialmente relevante aquí: Diane necesita visibilidad sobre quién no ha completado el compliance antes de su primer día.
