# CONTEXT — HealthCore: Control de Agentes (Parte 2)

> Este documento asume que las entidades e identificadores de Agente, Flujo y Tarea de la Parte 1 (`compliance_assistant`, `rfp_pipeline`, `revenue`/`clinical`/`compliance`) ya están implementados. Solo agrega la semántica de control sobre ellos.
>
> ⚠️ **Restricción no negociable:** Ningún identificador de paciente ni PHI puede aparecer en ningún comando de control, evento o registro de auditoría generado por tu flujo — ni siquiera como ejemplo ilustrativo. Esto aplica a cada uno de los campos descritos abajo.

## 1. Introducción

El ticket de James Osei es un seguimiento directo de la Parte 1: saber que un agente necesita intervención solo sirve si alguien puede actuar sin reiniciar toda la plataforma — y en HealthCore, un agente atascado sin atender arriesga un retraso en una revisión de cumplimiento, no solo una respuesta lenta. Quiere que cualquier ingeniero del equipo pueda pausar, reanudar o cancelar la ejecución de un agente específico sin afectar a los demás.

## 2. Acciones de Control por Agente

| `agent_id` | Qué significa `pause` | Qué significa `resume` | Qué significa `cancel` |
|---|---|---|---|
| `compliance_assistant` | Detener la generación de la respuesta actual a mitad de stream; la sesión de chat queda abierta | El operador libera la retención, la generación continúa — sin necesidad de repetir un checkpoint | Termina la sesión de chat; el miembro del personal la ve como cerrada |
| `rfp_pipeline` | Persiste un checkpoint de LangGraph en el nodo actual; la ejecución del flujo se detiene | Reanuda la ejecución del grafo desde ese checkpoint exacto | El flujo pasa a un estado terminal `cancelled`; no se ejecuta ningún nodo más y no puede reanudarse |

`pause`/`resume` sobre `rfp_pipeline` deben reutilizar el mismo mecanismo de checkpointing que ya soporta la aprobación human-in-the-loop en ese pipeline — no estás construyendo un segundo sistema de checkpoints.

## 3. Quién Puede Ejecutar Acciones de Control

Cualquier usuario autenticado del backoffice con rol de ingeniería u operaciones puede ejecutar `pause`, `resume` y `cancel`. Esto es deliberadamente distinto de los permisos de aprobación propios de Compliance sobre el pipeline de RFP: un operador pausando un agente atascado no tiene la misma autoridad que Claire Whitfield aprobando que un documento es seguro de enviar desde el punto de vista regulatorio. No mezcles estos dos conjuntos de permisos, y no dejes que ejecutar una acción de control sustituya la aprobación obligatoria de Compliance en ninguna parte del flujo de RFP.

## 4. Esquema de Comandos WebSocket Sugerido

```json
{"command": "pause", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0710"}}
{"command": "cancel", "data": {"agent_id": "compliance_assistant", "flow_id": "chat_0812"}}
{"event": "control_applied", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0710", "action": "pause", "actor_id": "user_0033", "timestamp": "2026-03-13T11:07:29Z"}}
```

Ningún campo de ningún comando, evento o registro de auditoría puede contener jamás un nombre de paciente, diagnóstico u otro identificador de paciente — revisa cada payload antes de emitirlo o persistirlo, tal como en la Parte 1.

## 5. Restricciones

- Los nombres de campos, acciones y estados deben coincidir exactamente con este documento.
- Cancelar un `rfp_workflow` a mitad de ejecución debe marcar el flujo mismo como `cancelled`, y toda tarea de departamento aún `pending` bajo él debe marcarse en consecuencia — no dejes tareas huérfanas en un estado `running` obsoleto.
- No implementes ni alteres las acciones de aprobación por departamento que ya existen en el pipeline de RFP. En particular, la aprobación obligatoria de PHI/regulatoria de `compliance` debe permanecer intacta y no puede ser evadida por ninguna acción de control a nivel operador definida en esta parte.
