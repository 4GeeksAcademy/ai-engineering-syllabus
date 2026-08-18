# CONTEXT — Autenticación Federada · HealthCore

_These instructions are also available in [English](./CONTEXT-healthcore.md)._

> **Proyecto:** Plataforma – Autenticación Federada  
> **Ruta en el repositorio:** `content/contexts/federated-authentication/CONTEXT-healthcore.es.md`

---

## 1. Por qué le importa a HealthCore

HealthCore es un entorno regulado: cualquier mecanismo de acceso a una cuenta con datos de pacientes debe ser tan defendible ante un auditor HIPAA o UK GDPR como el resto del sistema. James Osei (CTO) quiere ofrecer login federado al personal clínico y administrativo — que ya usa Microsoft 365 para el correo corporativo — pero solo si el mecanismo no debilita el control de acceso existente.

## 2. Proveedor de identidad elegido

**Microsoft** — es el proveedor de identidad ya desplegado para el correo corporativo de HealthCore en EE. UU. y Reino Unido, y permite reutilizar la gestión de cuentas que IT ya audita.

| Código `provider` | ¿Obligatorio? | Notas                                                                      |
| ----------------- | ------------- | -------------------------------------------------------------------------- |
| `microsoft`       | **sí**        | Microsoft identity platform (OAuth 2.0 / OIDC). Único proveedor permitido. |

**No** añadas Google, Apple ni LinkedIn en este CONTEXT. Mezclar IdPs de consumidor con acceso de staff a sistemas clínicos rompe la historia de auditoría.

## 3. Dónde aplica

Este proyecto aplica **solo al personal interno de HealthCore** (clínico, administrativo, billing, compliance) — nunca a pacientes. El portal de pacientes tiene sus propias reglas de identidad y no debe mezclarse con este flujo.

## 4. Regla de vinculación (recordatorio del README, reforzado aquí)

La vinculación solo ocurre desde el perfil de un empleado con sesión ya iniciada por el método tradicional, y **solo después de que IT haya aprovisionado a esa persona en el sistema**. El login federado nunca debe ser la forma de dar de alta a un empleado nuevo — equivaldría a dejar que cualquiera con una cuenta Microsoft llegue a datos de pacientes sin pasar por el aprovisionamiento de acceso.

La desvinculación vive en la misma pantalla de perfil. Si Microsoft es el **único** método de acceso que queda, la UI debe advertir y la API debe rechazar la desvinculación hasta que exista contraseña (u otro método aprobado).

Una identidad Microsoft (`provider` + `provider_user_id`) no puede vincularse a dos usuarios de staff de HealthCore a la vez.

## 5. Modelo de datos y OAuth

Guarda el vínculo, no la sesión de Microsoft.

| Campo                | Tipo      | Reglas                                                 |
| -------------------- | --------- | ------------------------------------------------------ |
| `user_id`            | FK → User | requerido; solo usuario staff                          |
| `provider`           | string    | `microsoft`                                            |
| `provider_user_id`   | string    | `oid` / `sub` de Microsoft. Único junto con `provider` |
| `email_at_link_time` | string    | snapshot                                               |
| `linked_at`          | datetime  | sistema                                                |
| `provisioned_by_it`  | bool      | debe ser `true` antes de permitir vincular             |

**No** persistas access/refresh tokens de Microsoft en texto plano. Este proyecto no exige guardar tokens.

OAuth debe validar `state` y un `redirect_uri` en lista blanca.

```bash
MICROSOFT_CLIENT_ID=...
MICROSOFT_CLIENT_SECRET=...
MICROSOFT_TENANT_ID=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/microsoft
```

Usa configuración **single-tenant** (o tenant explícito) — no "cualquier cuenta Microsoft". Un callback con `redirect_uri` distinto se rechaza.

## 6. Dato de seed necesario

Crea al menos un usuario de prueba (staff clínico o administrativo) con Microsoft vinculado y otro sin vincular, ambos con datos totalmente sintéticos.

```python
USERS_SEED = [
    {
        "email": "marcus.clinical@healthcore.example",
        "name": "Dr. Marcus Reid",
        "audience": "staff",
        "has_password": True,
        "provisioned_by_it": True,
        "linked_providers": [
            {"provider": "microsoft", "provider_user_id": "ms-oid-marcus-001"}
        ],
    },
    {
        "email": "priya.access@healthcore.example",
        "name": "Priya Nair",
        "audience": "staff",
        "has_password": True,
        "provisioned_by_it": True,
        "linked_providers": [],
    },
]
```

Una identidad Microsoft **que no** esté en `linked_providers` (p. ej. `ms-oid-unknown-999`) es el fixture de login rechazado. No siembres identidades reales de pacientes.

## 7. Eventos de auditoría (obligatorios)

Registra estos con timestamp, `user_id` (nullable en rechazo), `provider` y `provider_user_id`. Un login Microsoft de staff rechazado es un **evento de seguridad**, no un fallo de UX.

| `event`                    | Cuándo                                                                    |
| -------------------------- | ------------------------------------------------------------------------- |
| `federated_link`           | Proveedor vinculado desde perfil staff autenticado                        |
| `federated_unlink`         | Proveedor desvinculado                                                    |
| `federated_login_success`  | Sign-in con cuenta Microsoft ya vinculada                                 |
| `federated_login_rejected` | Sign-in con cuenta Microsoft no vinculada — **sin crear fila de usuario** |

## 8. Criterio de aceptación específico

Un intento de "Iniciar sesión con Microsoft" desde una cuenta corporativa válida no vinculada a ningún usuario HealthCore existente debe rechazarse de forma explícita y quedar en la traza de auditoría — porque en este contexto ese intento puede ser un riesgo de seguridad, no solo un error de usuario.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
