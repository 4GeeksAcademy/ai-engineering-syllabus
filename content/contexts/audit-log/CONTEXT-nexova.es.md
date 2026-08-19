# CONTEXT — Registro de Auditoría · Nexova

## 1. Por qué le importa a Nexova

Nexova maneja datos de candidatos y clientes que son comercialmente sensibles. Si un cliente pregunta "¿quién vio el perfil de este candidato y cuándo?", Javier Almeida necesita poder responder con datos, no con suposiciones — especialmente si alguna vez hay una disputa sobre exclusividad de un candidato entre dos procesos de selección.

## 2. Acciones críticas a registrar

- Consulta o exportación del perfil completo de un candidato
- Cambios de estado de un candidato en un proceso de selección (shortlisted, rechazado, contratado)
- Creación o modificación de una vacante
- Cambios en el CRM de clientes (Ventas): actualización de estado de una cuenta o negociación
- Creación, modificación o desactivación de usuarios y sus roles/departamentos
- Reasignación de un candidato o ticket de soporte entre consultores

## 3. Quién puede consultar el registro

- **Admin** (Sergio, Laura): acceso al registro completo de todos los departamentos.
- **Supervisor**: acceso al registro de su propio departamento (por ejemplo, un Supervisor de Selección solo ve el registro de Selección, no el de Ventas).
- **Empleado**: sin acceso al visor de auditoría.

## 4. Detalle importante

Las consultas de perfiles de candidatos son especialmente sensibles: registra no solo modificaciones, sino también accesos de solo lectura a un perfil completo, porque en este dominio "quién vio qué" es tan relevante como "quién cambió qué".

## 5. Dato de seed necesario

Genera al menos 15 entradas de auditoría de ejemplo cubriendo al menos cuatro de las acciones críticas listadas, distribuidas entre al menos dos departamentos distintos (por ejemplo, Selección y Ventas).
