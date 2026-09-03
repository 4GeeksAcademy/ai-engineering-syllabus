# Signal Yard — Kill Switch del Operador (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-real-time-agent-control`. Misma columna vertebral (pause ≠ cancel, resume desde checkpoint/hold, comandos WebSocket, fan-out pub/sub, auditoría con `actor_id` del JWT). Se apoya en el tablero Signal Yard de la Parte 1. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

El tablero **Signal Yard** de la Parte 1 ya muestra `yard_desk` e `inbound_wave` con available-actions informativas. Esta noche: esos botones **funcionan**. Un operador pausa una ola atascada sin reiniciar todo el proceso del escritorio; resume continúa desde el último checkpoint stub; cancel es definitivo. Dos tableros abiertos deben actualizarse cuando cualquiera dispara un comando.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-real-time-agent-control`) | Este ejemplo de clase                  |
| -------------------------------------------------------------- | -------------------------------------- |
| Monorepo de empresa + panel de observabilidad Parte 1          | Solo Signal Yard                       |
| Reutilizar checkpointer real de LangGraph                      | Dict de checkpoint stub en memoria     |
| JWT de empresa + roles eng/ops                                 | Token demo → `actor_id` fijo           |
| Cascada CONTEXT de tareas de departamento pendientes           | Marcar hijas `cancelled` en store stub |
| PR de empresa + preguntas de diseño                            | Demo en vivo + 6 tests automatizados   |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Pause ≠ cancel** — estados y garantías distintos
2. **Resume desde hold/checkpoint** — no desde el paso 0
3. **Comandos WebSocket** — `pause` / `resume` / `cancel` con respuestas nombradas
4. **Pub/sub** — dos pestañas, un comando, ambas actualizan
5. **Auditoría** — el historial de Tarea muestra acción + `actor_id` + hora
6. **Transiciones inválidas rechazadas** — resume en `running` falla en alto
7. **Reconexión** — refetch del estado del agente, luego resubscribir

---

## Semilla (indicativo)

| `agent_id`     | Pause significa                           | Cancel significa                             |
| -------------- | ----------------------------------------- | -------------------------------------------- |
| `yard_desk`    | Sostener la generación del chat           | Cerrar la sesión                             |
| `inbound_wave` | Guardar checkpoint stub en el paso actual | Terminal; tareas hijas pendientes canceladas |

```json
{"command": "pause", "data": {"agent_id": "inbound_wave", "flow_id": "wave_07"}}
{"event": "control_applied", "data": {"agent_id": "inbound_wave", "flow_id": "wave_07", "action": "pause", "actor_id": "demo_op", "timestamp": "2026-03-12T09:41:17Z"}}
```

---

## Qué construir

### 1. API / WS de control

- [ ] Endpoint WebSocket que acepte comandos; rechazar transiciones inválidas
- [ ] Checkpoint stub al pausar `inbound_wave`; resume lo lee
- [ ] Cancel marca flujo + hijas pendientes; resume posterior rechazado
- [ ] Broadcast de `control_applied` a todos los suscriptores

### 2. Tablero UI

- [ ] Habilitar/deshabilitar pause / resume / cancel según estado
- [ ] Aplicar `control_applied` remoto sin recargar
- [ ] Mostrar filas de control en el historial de tareas

### 3. Tests

| #   | Escenario           | Esperado                                      |
| --- | ------------------- | --------------------------------------------- |
| 1   | Pausar ola          | Estado `paused`; clave de checkpoint presente |
| 2   | Resume              | Continúa después del paso del checkpoint      |
| 3   | Cancel luego resume | Resume rechazado                              |
| 4   | Transición inválida | Error, estado sin cambio                      |
| 5   | Dos clientes WS     | Ambos reciben `control_applied`               |
| 6   | Auditoría           | Historial tiene `actor_id`                    |

---

## Guion de demo (en vivo)

1. Arrancar un `rail_wave` con los stubs de la Parte 1
2. Abrir dos tableros → pausar desde pestaña A → pestaña B actualiza
3. Resume → la ola continúa
4. Cancelar otra ola → resume falla
5. Desconectar WS → reconectar → el estado coincide con el servidor

---

## Fuera de alcance del ejemplo

- LangGraph real / cableado HITL de RFP
- Empresas del CONTEXT
- WebSocket de chat con streaming de tokens (proyecto post-grad de communication)
