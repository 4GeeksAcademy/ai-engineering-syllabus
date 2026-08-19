# CONTEXT — Registro de Auditoría · Brasaland

## 1. Por qué le importa a Brasaland

Con 14 sedes operando en dos países y un equipo corporativo pequeño, cuando algo sale mal (una discrepancia de inventario, un cambio de precio no autorizado, una merma que no cuadra) hoy la única forma de investigar es preguntarle a la persona involucrada. Felipe Guerrero necesita poder reconstruir qué pasó sin depender de la memoria de nadie.

## 2. Acciones críticas a registrar

- Modificación de precios de menú o de ingredientes
- Aprobación o rechazo de pedidos de ingredientes a proveedores
- Registro de mermas (producto perdido por caducidad, error de cocina o posible robo)
- Cambios en la configuración de una sede (horarios, aforo, datos de contacto)
- Creación, modificación o desactivación de usuarios y sus roles/departamentos
- Acciones ejecutadas por el agente de informe ejecutivo semanal (si tu implementación ya lo tiene)

## 3. Quién puede consultar el registro

- **Admin** (Felipe, Nicolás, Mariana): acceso al registro completo de todas las sedes y departamentos.
- **Supervisor**: acceso únicamente al registro de su propia sede y departamento.
- **Empleado**: sin acceso al visor de auditoría.

## 4. Detalle importante

Brasaland opera con dos monedas (COP y USD). Cuando el evento auditado involucre un monto (por ejemplo, un cambio de precio), registra el monto junto con la moneda en la que se ejecutó, no lo conviertas — la conversión es responsabilidad del reporte, no del registro de auditoría.

## 5. Dato de seed necesario

Genera al menos 15 entradas de auditoría de ejemplo cubriendo al menos cuatro de las acciones críticas listadas, distribuidas entre al menos dos sedes distintas.
