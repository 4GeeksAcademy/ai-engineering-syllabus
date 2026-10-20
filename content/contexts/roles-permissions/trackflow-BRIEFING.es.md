# CONTEXT — Roles y Permisos · TrackFlow

## 1. Por qué le importa a TrackFlow

TrackFlow gestiona almacenes y última milla en Los Ángeles y Zaragoza para marcas de e-commerce que confían en la empresa su operación logística completa. Un operativo de almacén, un coordinador de carriers y un account manager tienen hoy el mismo nivel de acceso al sistema — lo que significa que cualquiera podría, en teoría, ver el contrato comercial de un cliente, modificar el inventario de otro país o consultar los datos laborales de un compañero sin que nadie lo note.

## 2. Roles de TrackFlow

Usa exactamente estos tres roles como mínimo:

| Rol del sistema | Quién lo ocupa en TrackFlow | Capacidades típicas |
|---|---|---|
| **Empleado** | Operativos de almacén, coordinadores de carrier, agentes de CX, personal corporativo | Registrar picking, actualizar estado de incidencias, consultar el estado de envíos de su cola de trabajo, consultar sus propios datos laborales |
| **Supervisor** | Ana Whitfield (Almacén), Carlos Vega (Carriers), Valentina Cruz (CX), Sofía Ramos (Devoluciones), Rafael Sanz (Personas) | Todo lo del Empleado + ver el dashboard operativo de su área, aprobar excepciones, reasignar trabajo dentro de su equipo |
| **Admin** | Andrés Kim (CTO), Thomas Harry (CEO) | Todo lo anterior + gestionar usuarios, ver datos de ambos países y todos los departamentos, configurar roles y departamentos |

## 3. Departamentos de TrackFlow

- **Operaciones de Almacén**
- **Última Milla y Gestión de Carriers**
- **Logística Inversa (Devoluciones)**
- **Experiencia del Cliente (CX)**
- **Comercial y Relación con Clientes**
- **Personas**
- **Tecnología**
- **Dirección Ejecutiva**

## 4. Reglas de qué información compete a cada departamento

- Un **Supervisor de Almacén** ve inventario, discrepancias y pedidos entrantes, pero no ve los contratos comerciales de los clientes (eso es de Comercial).
- Un **Supervisor de Comercial** ve el estado de cuenta y renovación de cada cliente, pero no ve el detalle operativo de inventario por almacén.
- Un usuario de **CX** ve tickets y su SLA, pero no ve el desempeño financiero por carrier (eso es de Última Milla/Comercial combinado con Dirección).
- Un usuario de **Personas** ve los datos laborales del personal de TrackFlow (contratos, ausencias, vacaciones, progreso de incorporación), pero no ve datos de clientes, inventario ni envíos.
- Ningún Supervisor de otro departamento ve los datos laborales de las personas de su equipo más allá de lo operativo (horarios y asignaciones). Contratos, ausencias justificadas y datos personales son exclusivos de Personas.
- Cualquier **Empleado** puede consultar sus propios datos laborales, nunca los de otra persona.
- Solo **Dirección Ejecutiva** ve el consolidado de Estados Unidos y España a la vez.

## 5. Detalle importante

TrackFlow opera en dos países con marcas cliente distintas, pero **esto no es multi-tenancy** — es scoping por departamento y, opcionalmente, por país. No modeles aislamiento de datos por cliente final en este proyecto; eso pertenece a otro proyecto de la plataforma. Aquí el eje relevante es rol × departamento.

Personas trabaja con dos marcos laborales distintos (Estados Unidos y España). Puedes modelar el país como atributo adicional del registro laboral, pero no es necesario aislar los datos de Personas por país en este proyecto.

## 6. Datos semilla mínimos

Crea al menos:
- 3 usuarios Empleado (de departamentos distintos: Almacén, Carriers y uno más)
- 2 usuarios Supervisor (uno de ellos de Personas)
- 1 usuario Admin
- Los 8 departamentos listados arriba

## 7. Criterios de aceptación específicos

- Un Supervisor de Almacén que intenta consultar el estado de renovación de contrato de un cliente (departamento Comercial) debe recibir un rechazo.
- Un Supervisor de Almacén que intenta consultar el contrato o las ausencias de un operativo de su propio equipo (datos de Personas) debe recibir un rechazo.
