# API de parcelas comunitarias — Pase de seguridad (ejemplo de clase)

> **Para instructores:** No es proyecto del estudiante. Misma columna vertebral que `ai-eng-security-hardening`: revisión OWASP guiada, 3 hallazgos reales con prueba antes/después, rate limits, auditoría de secretos, doc de rotación. Dominio = API de reservas de huertos comunitarios.

_These instructions are also available in [English](./README.md)._

---

## El reto

FastAPI pequeña gestiona reservas de parcelas en huerto comunitario. CTO bloquea demo pública hasta que alguien demuestre que la app no es trivialmente explotable. Una sesión: encontrar bugs reales, corregir uno crítico, documentar el resto.

### Nota de alcance

Máx 3 endpoints (`POST /auth/login`, `GET /plots`, `POST /plots/{id}/reserve`). Sin SSH/firewall de servidor. Alumnado sigue brief completo en `README.md` raíz.

---

## Qué construir

### Doc de auditoría

- [ ] Mini matriz OWASP (10 filas, aplica/N/A)
- [ ] 3 hallazgos con pasos de reproducción + impacto (p. ej. reservar sin auth, IDOR en parcela, stack trace en debug)

### Rate limit

- [ ] `POST /auth/login` → 429 tras 5/min/IP

### Secretos

- [ ] Quitar `SECRET_KEY = "dev123"` hardcodeado → env
- [ ] `SECRET_ROTATION.md` procedimiento de una página

### Corrección + prueba

- [ ] Corregir al menos 1 hallazgo crítico
- [ ] Salida curl antes + test/captura después por corrección

---

## Verificar juntos

- [ ] Demostrar vuln #1 en vivo (antes del parche)
- [ ] Mismos pasos fallan después del parche
- [ ] 6º login → 429
- [ ] `grep -r "dev123" .` limpio

---

## Preguntas de discusión

1. ¿Por qué checklist OWASP sin pasos de explotación falla aceptación del CTO?
2. Rate limit por IP — ¿qué rompe detrás de NAT en un colegio?
3. ¿Cuándo es seguro rotar JWT secret sin echar a todos los usuarios?
