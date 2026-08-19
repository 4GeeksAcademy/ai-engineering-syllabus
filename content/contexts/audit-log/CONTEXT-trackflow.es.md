# CONTEXT — Registro de Auditoría · TrackFlow

## 1. Por qué le importa a TrackFlow

TrackFlow gestiona inventario y envíos de terceros (las marcas cliente). Una discrepancia de inventario o una aprobación de devolución incorrecta puede costarle dinero directamente a un cliente — y Andrés Kim necesita poder demostrarle a esa marca, con datos, qué pasó y quién lo autorizó.

## 2. Acciones críticas a registrar

- Ajustes manuales de inventario (correcciones fuera del flujo normal de entrada/salida)
- Aprobación o rechazo de una devolución
- Cambios en la asignación de carrier para un envío
- Modificación de contratos o condiciones comerciales de un cliente
- Creación, modificación o desactivación de usuarios y sus roles/departamentos
- Acciones ejecutadas por el motor automático de aprobación de devoluciones (si tu implementación ya lo tiene)

## 3. Quién puede consultar el registro

- **Admin** (Andrés, Thomas): acceso al registro completo de ambos países y todos los departamentos.
- **Supervisor**: acceso al registro de su propio departamento (por ejemplo, Ana solo ve el registro de Almacén).
- **Empleado**: sin acceso al visor de auditoría.

## 4. Detalle importante

Cuando el evento auditado ocurra en un almacén específico, registra el país y el identificador del almacén junto con el evento — esto le permite a Dirección Ejecutiva más adelante comparar patrones entre Los Ángeles y Zaragoza, aunque ese análisis no es parte de este proyecto.

## 5. Dato de seed necesario

Genera al menos 15 entradas de auditoría de ejemplo cubriendo al menos cuatro de las acciones críticas listadas, distribuidas entre al menos dos departamentos distintos.
