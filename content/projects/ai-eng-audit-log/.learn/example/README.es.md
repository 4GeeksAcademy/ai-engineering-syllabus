# Bodega de barrio — Rastro de Auditoría (Ejemplo de clase)

> **Para instructores:** No es proyecto del estudiante. Demo en vivo de misma columna vertebral que `ai-eng-audit-log`: registros append-only, hash chaining como evidencia de alteración, actor humano vs proceso, y acceso de visor por alcance. Dominio cambiado a bodega de barrio para evitar copiar historia de empresa.

_These instructions are also available in [English](./README.md)._

---

## El reto

Una bodega pequeña registra movimientos de stock en una app web. Tras un incidente, manager hace pregunta simple: "¿Quién cambió cantidad del SKU W-42 anoche?" El equipo tiene logs normales, pero se pueden sobreescribir. Hace falta rastro de auditoría que responda **quién / qué / cuándo** y detecte manipulación.

### Nota de alcance

Una sesión de 60–120 minutos. Mantén un recurso auditado (`stock_adjustments`) más eventos de auth. No hace falta integración completa de monorepo. El alumnado sigue el brief completo en el `README.md` raíz.

---

## Qué construir

### Modelo de auditoría

- [ ] Tabla/colección `audit_log` append-only
- [ ] Campos: `actor_type`, `actor_id`, `action`, `resource`, `resource_id`, `origin`, `created_at`, `prev_hash`, `entry_hash`
- [ ] `entry_hash = sha256(canonical_payload + prev_hash)`

### Captura

- [ ] Registrar ajuste manual de inventario create/update/delete-attempt
- [ ] Registrar acción de proceso (`nightly_reconciliation_bot`)
- [ ] Registrar auth success/fail

### Visor

- [ ] Filtro por actor, acción, recurso, rango de fechas
- [ ] Admin ve todo; Supervisor ve su departamento; Employee no ve
- [ ] Añadir paginación (`limit/offset`)

### Guard rails

- [ ] API sin ruta `UPDATE`/`DELETE` para `audit_log`
- [ ] Test de manipulación manual rompe validación de cadena hash

---

## Verificar juntos

- [ ] Crear 5+ entradas desde acciones de usuario + 1 acción de bot
- [ ] Intentar editar fila guardada en fixture DB; correr validación de cadena; verificar `invalid_from_index`
- [ ] Consultar visor como Supervisor de otro departamento; verificar denegación o respuesta recortada

---

## Preguntas de discusión

1. ¿Por qué append-only en capa app sigue débil sin restricciones DB?
2. Si actor es proceso, ¿qué identidad conviene persistir para mantener trazabilidad?
3. Cuando volumen llegue a millones, ¿dónde vivir paginación y política de retención?
