# Vestuario del club — Vincular Google cuando ya tienes carnet (ejemplo de clase)

> **Para instructores:** No es el proyecto del estudiante. Demo en vivo de la misma columna vertebral que `ai-eng-federated-authentication`: el login federado **no crea cuentas**; la vinculación solo desde un perfil autenticado; OAuth `state` + `redirect_uri`; la desvinculación no puede dejar cero métodos de acceso; auditar logins rechazados. El dominio es un club deportivo de barrio para que el alumnado no copie la historia del IdP de la empresa.

_These instructions are also available in [English](./README.md)._

---

## El reto

El club ya tiene números de socio y contraseñas. Los socios quieren "Iniciar sesión con Google". La regla de la junta: Google solo puede abrir un **carnet que ya existe y que el socio vinculó desde Mi cuenta**. Aparecer con un login de Google nunca debe fabricar una membresía nueva.

### Nota de alcance

Una sesión. Un proveedor (`google`), dos flujos (vincular vs login), callback OAuth mockeado (no hace falta un proyecto real de Google Cloud). Se omite multi-proveedor, Apple/Microsoft/LinkedIn y una UI pulida — basta `/docs` más una página de perfil mínima. El alumnado sigue el brief completo en el `README.md` de la raíz del proyecto.

---

## Qué construir

### Modelo

- [ ] `IdentityLink`: `user_id`, `provider="google"`, `provider_user_id`, `linked_at`
- [ ] Único `(provider, provider_user_id)`
- [ ] Sin tokens de Google en texto plano

### Dos caminos OAuth

- [ ] `GET /auth/google/link` — requiere sesión; guarda `state` con `intent=link`
- [ ] `GET /auth/google/login` — público; `intent=login`
- [ ] Callback: validar `state` + `redirect_uri` en lista blanca
- [ ] Miss en login → rechazar, **no** hacer `INSERT` de usuario; auditar `federated_login_rejected`
- [ ] Link que ya pertenece a otro usuario → 409

### Desvincular

- [ ] `DELETE` del vínculo desde el perfil
- [ ] Si no hay contraseña ni otro vínculo → advertir + 409

---

## Verificar juntos

- [ ] Sembrar socio A con Google `sub=club-001`; socio B solo con contraseña
- [ ] Callback con `sub=club-unknown` → rechazo; el recuento de usuarios no cambia
- [ ] `GET /auth/google/link` anónimo → 401
- [ ] Desvincular el Google de A mientras tiene contraseña → OK; desvincular el último método → 409

---

## Preguntas de discusión

1. ¿Por qué "crear usuario en el primer login de Google" es cómodo y aun así está mal en un sistema de membresías?
2. ¿Dónde debe vivir `intent=link|login` para que un `code` robado no vincule la cuenta de otra persona?
3. ¿Es el email una clave de unión segura frente a `provider_user_id` (`sub`)? ¿Qué pasa cuando cambia el correo de Google?
