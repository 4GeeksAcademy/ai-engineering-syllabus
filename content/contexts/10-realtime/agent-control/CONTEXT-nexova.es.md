# CONTEXT — Nexova: Control de Agentes (Parte 2)

> Este documento asume que las entidades e identificadores de Agente, Flujo y Tarea de la Parte 1 (`first_line_support`, `rfp_pipeline`, `seleccion`/`capacitacion`/`soporte`) ya están implementados. Solo agrega la semántica de control sobre ellos.

## 1. Introducción

El ticket de Sergio Molina es un seguimiento directo de la Parte 1: saber que un agente necesita intervención solo sirve si alguien puede actuar sin reiniciar todo el servicio. Quiere que cualquier ingeniero del equipo pueda pausar, reanudar o cancelar la ejecución de un agente específico sin tocar a los demás.

## 2. Acciones de Control por Agente

| `agent_id` | Qué significa `pause` | Qué significa `resume` | Qué significa `cancel` |
|---|---|---|---|
| `first_line_support` | Detener la generación de la respuesta actual a mitad de stream; la sesión de chat queda abierta | El operador libera la retención, la generación continúa — sin necesidad de repetir un checkpoint | Termina la sesión de chat; el cliente la ve como cerrada |
| `rfp_pipeline` | Persiste un checkpoint de LangGraph en el nodo actual; la ejecución del flujo se detiene | Reanuda la ejecución del grafo desde ese checkpoint exacto | El flujo pasa a un estado terminal `cancelled`; no se ejecuta ningún nodo más y no puede reanudarse |

`pause`/`resume` sobre `rfp_pipeline` deben reutilizar el mismo mecanismo de checkpointing que ya soporta la aprobación human-in-the-loop en ese pipeline — no estás construyendo un segundo sistema de checkpoints.

## 3. Quién Puede Ejecutar Acciones de Control

Cualquier usuario autenticado del backoffice con rol de ingeniería u operaciones puede ejecutar `pause`, `resume` y `cancel`. Esto es deliberadamente más amplio que los permisos de aprobación por departamento del pipeline de RFP — el acceso de control y el acceso de aprobación de negocio son dos conjuntos de permisos distintos, no los mezcles.

## 4. Esquema de Comandos WebSocket Sugerido

```json
{"command": "pause", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318"}}
{"command": "resume", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318"}}
{"event": "control_applied", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318", "action": "resume", "actor_id": "user_0154", "timestamp": "2026-03-12T09:41:17Z"}}
```

## 5. Restricciones

- Los nombres de campos, acciones y estados deben coincidir exactamente con este documento.
- Cancelar un `rfp_workflow` a mitad de ejecución debe marcar el flujo mismo como `cancelled`, y toda tarea de departamento aún `pending` bajo él debe marcarse en consecuencia — no dejes tareas huérfanas en un estado `running` obsoleto.
- No implementes ni alteres las acciones de aprobación por departamento que ya existen en el pipeline de RFP — esas siguen siendo un asunto de negocio separado del `pause`/`resume`/`cancel` a nivel operador de este milestone.
