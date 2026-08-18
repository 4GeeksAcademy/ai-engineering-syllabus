# Maple Street Library — Auditoría OWASP Top 10 (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-cybersecurity-vulnerabilities`. Misma columna vertebral (checklist de endurecimiento, matriz OWASP para backend / frontend / agente, corrección crítica + prueba antes/después). Dominio distinto a las auditorías con CONTEXT de compañía. Continúa la narrativa Maple Street Library de ejemplos previos. El alumnado sigue el brief completo del `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Maple Street Library** tiene una API de mostrador pequeña (`GET /faq`, `POST /chat`) y un agente con una tool: `waive_overdue_fine`. El stack se desplegó en una VM de aula con SSH root, puerto 8000 abierto al mundo y modo debug activado. Seguridad pide un **pase OWASP de una sesión** antes de la demo a la junta.

### Nota de alcance

| Proyecto evaluado (`ai-eng-cybersecurity-vulnerabilities`) | Este ejemplo de clase                       |
| ---------------------------------------------------------- | ------------------------------------------- |
| Monorepo de compañía + CONTEXT-empresa.md                  | Solo API de mostrador + agente Maple Street |
| Endurecimiento completo en VM prod                         | Pasos documentados en VM de aula            |
| 10 categorías OWASP × 3 carriles                           | Matriz corta + foco A01, A02, A05 en agente |
| PR al fork de compañía                                     | Checklist local + comandos demo             |

---

## Columna vertebral didáctica (debe verse en vivo)

1. Baseline: anotar SSH root, puertos abiertos, flag debug
2. Usuario no-root + `PermitRootLogin no` (o equivalente en aula)
3. Firewall: solo 22 (SSH) + 8000 (app) — cerrar el resto en papel
4. Matriz OWASP: backend (`/faq`, `/chat`), frontend (página estática si hay), agente (tool waive)
5. Corregir ≥2 issues críticos (debug off, ACL de tool, secretos en env)
6. Comando o test antes/después por cada corrección

---

## Vulnerabilidades semilla (indicativo)

```text
- API con DEBUG=true exponiendo stack traces (A05)
- waive_overdue_fine invocable sin control de rol (A01)
- OPENAI_API_KEY en archivo fuente (A02)
- Proceso del agente corre como root en la VM (A05)
```

Alcance: **API FAQ de mostrador + agente waive** — no el ERP completo de la biblioteca.

---

## Matriz OWASP mini (rellenar en clase)

| Categoría             | Backend          | Frontend | Agente                 | ¿Aplica?   |
| --------------------- | ---------------- | -------- | ---------------------- | ---------- |
| A01 Control de acceso | `/chat` abierto? | —        | waive sin rol?         | sí         |
| A02 Fallas cripto     | TLS? secretos?   | —        | almacenamiento API key | sí         |
| A05 Mala config       | DEBUG=true       | —        | corre como root        | sí         |
| A03 Inyección         | input chat       | —        | poison en FAQ          | discutir   |
| Otras                 | …                | …        | …                      | documentar |

---

## Qué construir (checklist)

- [ ] `docs/security/baseline.md` — puertos, usuario SSH, flags debug antes de fixes
- [ ] Notas de endurecimiento: usuario no-root, política SSH, reglas firewall (aunque simuladas)
- [ ] `docs/security/owasp-top10-report.md` — 10 filas con evidencia o N/A justificado
- [ ] Corregir DEBUG / secretos / ACL waive — dos como **críticos**
- [ ] `tests/security/test_access_control.py` o script curl mostrando antes/después
- [ ] Agente auditado por separado de las rutas API

---

## Verificar juntos

- [ ] SSH root bloqueado (o sustituto documentado en aula)
- [ ] Usuario deploy no-root en doc de endurecimiento
- [ ] Lista de puertos/firewall coherente con VM de aula
- [ ] 10 filas OWASP rellenadas
- [ ] Fila de agente no vacía
- [ ] Dos correcciones críticas demostradas en vivo

---

## Preguntas de discusión

1. ¿Por qué auditar el agente por separado si llama a la misma API?
2. ¿Qué categoría OWASP es DEBUG=true — y por qué el logging no basta?
3. ¿Cómo cambiaría la lista de puertos de Maple Street vs los puertos SSE/MCP de un CONTEXT de compañía?
