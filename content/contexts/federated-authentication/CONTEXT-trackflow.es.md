# CONTEXT — Autenticación Federada · TrackFlow

_These instructions are also available in [English](./CONTEXT-trackflow.md)._

> **Proyecto:** Plataforma – Autenticación Federada  
> **Ruta en el repositorio:** `content/contexts/federated-authentication/CONTEXT-trackflow.es.md`

---

## 1. Por qué le importa a TrackFlow

Los clientes B2B de TrackFlow (las marcas que externalizan su logística) ya gestionan su identidad corporativa con Microsoft 365, igual que la mayor parte del equipo de TrackFlow en Los Ángeles y Zaragoza. Miguel Torres (Comercial) ha recibido más de una queja de account managers de marca pidiendo no tener que gestionar otra contraseña más para el portal de cliente.

## 2. Proveedor de identidad elegido

**Microsoft** — es el proveedor de identidad corporativa dominante tanto en el equipo interno de TrackFlow como en sus clientes de marca, en ambos países.

| Código `provider` | ¿Obligatorio? | Notas                                                                       |
| ----------------- | ------------- | --------------------------------------------------------------------------- |
| `microsoft`       | **sí**        | Microsoft identity platform (OAuth 2.0 / OIDC). Proveedor mínimo (y único). |

## 3. Dónde aplica

- **Portal de cliente (marcas B2B):** un account manager ya registrado de una marca cliente puede vincular la cuenta Microsoft de su empresa desde su perfil.
- **Backoffice interno:** el staff de TrackFlow Tech y operaciones puede vincular su cuenta Microsoft corporativa desde su perfil.

El primer acceso de un cliente B2B **no** es autoservicio vía login federado. Comercial inicia el onboarding; la cuenta ya existe antes de poder vincular Microsoft.

## 4. Regla de vinculación (recordatorio del README)

La vinculación solo ocurre desde el perfil de un usuario con sesión ya iniciada. Un usuario que llega con "Iniciar sesión con Microsoft" y no tiene cuenta previa en TrackFlow debe ser rechazado y dirigido a registrarse primero por el canal adecuado (el onboarding de un cliente B2B lo inicia normalmente el equipo Comercial, no el propio cliente).

La desvinculación vive en la misma pantalla de perfil. Si Microsoft es el **único** método de acceso que queda, la UI debe advertir y la API debe rechazar la desvinculación hasta que exista contraseña (u otro método aprobado).

Una identidad Microsoft (`provider` + `provider_user_id`) no puede vincularse a dos usuarios de TrackFlow a la vez.

## 5. Modelo de datos y OAuth

Guarda el vínculo, no la sesión de Microsoft.

| Campo                | Tipo      | Reglas                                                 |
| -------------------- | --------- | ------------------------------------------------------ |
| `user_id`            | FK → User | requerido                                              |
| `provider`           | string    | `microsoft`                                            |
| `provider_user_id`   | string    | `oid` / `sub` de Microsoft. Único junto con `provider` |
| `email_at_link_time` | string    | snapshot                                               |
| `linked_at`          | datetime  | sistema                                                |
| `audience`           | string    | `internal` o `b2b_client` — no se deriva del IdP       |

**No** persistas access/refresh tokens de Microsoft en texto plano. Este proyecto no exige guardar tokens.

OAuth debe validar `state` y un `redirect_uri` en lista blanca.

```bash
MICROSOFT_CLIENT_ID=...
MICROSOFT_CLIENT_SECRET=...
MICROSOFT_TENANT_ID=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/microsoft
```

Un callback con `redirect_uri` distinto se rechaza. Multi-tenant es aceptable para clientes B2B **solo si** la fila de usuario TrackFlow ya existe; el tenant nunca debe crear esa fila.

## 6. Dato de seed necesario

Crea al menos un usuario de prueba (interno o cliente B2B) con Microsoft vinculado y otro sin vincular.

```python
USERS_SEED = [
    {
        "email": "miguel.commercial@trackflow.example",
        "name": "Miguel Torres",
        "audience": "internal",
        "has_password": True,
        "linked_providers": [
            {"provider": "microsoft", "provider_user_id": "ms-oid-miguel-001"}
        ],
    },
    {
        "email": "brand.am@northwind.example",
        "name": "Northwind Account Manager",
        "audience": "b2b_client",
        "has_password": True,
        "linked_providers": [],
    },
]
```

Una identidad Microsoft **que no** esté en `linked_providers` (p. ej. `ms-oid-unknown-999`) es el fixture de login rechazado.

## 7. Eventos de auditoría (obligatorios)

Registra estos con timestamp, `user_id` (nullable en rechazo), `provider` y `provider_user_id`:

| `event`                    | Cuándo                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| `federated_link`           | Microsoft vinculado desde perfil autenticado                                               |
| `federated_unlink`         | Microsoft desvinculado                                                                     |
| `federated_login_success`  | Sign-in con cuenta Microsoft ya vinculada                                                  |
| `federated_login_rejected` | Sign-in con cuenta Microsoft no vinculada — **sin crear usuario ni asociación de cliente** |

## 8. Criterio de aceptación específico

Un intento de "Iniciar sesión con Microsoft" desde una cuenta no vinculada a ningún usuario TrackFlow existente debe rechazarse de forma explícita, sin crear automáticamente una cuenta ni una asociación de cliente.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
