# Northside Makerspace — Orquestador de Orientación de Seguridad (Ejemplo de clase)

> **Para instructores:** Brief de demo en vivo para `ai-eng-onboarding-orchestrator`. Misma columna vertebral (grafo explícito de etapas, un solo agente LangGraph, resume con checkpointer, gates de comprensión, lookup solo en docs oficiales sin alucinar, interrupt de aprobación humana, escalado por vencimiento, identidad de auditoría del agente). Dominio distinto: orientación de seguridad en makerspace, no onboarding corporativo de People. Alcance: ~60–90 minutos. El alumnado sigue el brief completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Northside Makerspace** solo deja usar herramientas eléctricas a miembros nuevos tras una orientación corta de seguridad. Hoy el mostrador entrega un PDF y espera lo mejor. Vas a demos un **único agente con estado** que lleva a un miembro nuevo por un grafo de etapas pequeño, se pausa para la aprobación de un mentor del taller, responde solo desde un handbook oficial mínimo y sobrevive a un reinicio del proceso a mitad del flujo.

### Nota de alcance

| Proyecto evaluado (`ai-eng-onboarding-orchestrator`)                 | Este ejemplo de clase                             |
| -------------------------------------------------------------------- | ------------------------------------------------- |
| Etapas del briefing de empresa (días/semanas, multi-país, contratos) | 4 etapas, plazos de juguete ~3 días laborables    |
| Índice RAG completo sobre corpus oficial de onboarding               | 1 markdown handbook + stub keyword/vector         |
| Vistas de producción People + nueva contratación                     | Dump de progreso print/JSON basta                 |
| Checkpointer durable en BD                                           | `MemorySaver` (o sqlite) basta                    |
| Productización completa de recordatorios/escalados                   | Una función de recordatorio + un stub de escalado |
| Documentos laborales sensibles                                       | Solo redactar `member_phone`                      |

---

## Qué construir

### 1. Grafo de etapas

| #   | Etapa                        | Condición de salida                        | Plazo | Aprueba             |
| --- | ---------------------------- | ------------------------------------------ | ----- | ------------------- |
| 1   | Bienvenida + waiver recibido | Staff marca waiver recibido                | Día 1 | Staff (flag manual) |
| 2   | Normas del taller            | Check de comprensión aprobado              | Día 2 | Automático          |
| 3   | Seguridad de herramientas    | Check aprobado **y** aprobación del mentor | Día 3 | Mentor del taller   |
| 4   | Cerrado                      | El agente marca la orientación completa    | Día 3 | Automático          |

- [ ] Modelar etapas como grafo explícito (nodos + aristas), no un script if/else enredado
- [ ] Las etapas de contenido no avanzan sin check aprobado

### 2. Un solo agente + checkpointer

- [ ] Un orquestador LangGraph compilado (o equivalente) — justificar “un agente” en voz alta
- [ ] Persistir estado con checkpointer keyed por `member_id` / `thread_id`
- [ ] Demo: matar el proceso a mitad de la etapa 2 → reiniciar → retomar en etapa 2

### 3. Lookup del handbook oficial

Corpus mínimo, p. ej.:

```text
# Northside Safety Handbook (excerpt)
- Eye protection required in the wood shop at all times.
- Never leave a running saw unattended.
- Report injuries to the desk before leaving the building.
```

- [ ] La tool responde solo desde este material y cita la línea/sección
- [ ] Pregunta fuera del handbook → “no está en el material oficial” + enrutar al desk (sin inventar normas)

### 4. Interrupt de aprobación humana

- [ ] La etapa 3 se pausa hasta que un usuario con rol `shop_mentor` envíe approve/reject
- [ ] Reject vuelve a la etapa 2 (re-check) — déjalo explícito en el grafo

### 5. Stub de vencimiento + auditoría

- [ ] Si la etapa 2 pasa el plazo → escalar a `shop_mentor` (log o print vale)
- [ ] Registrar acciones con `actor_type=agent`; nunca loguear `member_phone`

---

## Verificar juntos

- [ ] Fallar un check a propósito → reforzar contenido → no se puede saltar a la siguiente etapa
- [ ] Preguntar “¿Puedo traer mi propio láser?” → enrutado, no inventado
- [ ] Reiniciar a mitad de flujo → misma etapa
- [ ] Mentor sin rol `shop_mentor` no puede aprobar
- [ ] Mostrar una línea de auditoría con identidad de agente y sin teléfono

---

## Preguntas de discusión

1. ¿Por qué un orquestador largo y único encaja mejor aquí que tres agentes especializados (contenido, Q&A, aprobaciones)?
2. ¿Qué se rompe si “abrió el handbook” cuenta como etapa completa en vez de un check de comprensión?
3. ¿Dónde guardarías campos sensibles para que el checkpointer y los prompts del LLM nunca los vean?
