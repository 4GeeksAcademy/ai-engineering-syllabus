# BRIEFING — Hito 5: Gestión de Inventario Backend
## Empresa: HealthCore

**Ruta:** `05-backend-inventory-orm/healthcore-BRIEFING.es.md`

---

## Tu Empresa

**HealthCore** es una empresa de servicios sanitarios ambulatorios con 12 clínicas repartidas entre EE.UU. (Texas, Florida, Georgia) y el Reino Unido (Londres, Mánchester). Cada clínica consume material sanitario a diario — jeringas, EPI, material de curas, tests de diagnóstico rápido y medicamentos — y recibe reposiciones de proveedores sanitarios certificados.

Controlar qué material hay disponible en cada clínica es tanto una necesidad operativa como un requisito de cumplimiento normativo. Quedarse sin EPI a mitad de turno o usar material caducado supone un riesgo clínico. Hasta ahora, cada centro ha gestionado el stock en una hoja de cálculo local sin visibilidad central.

**James Osei (CTO)** ha dado prioridad a esto como parte de la construcción de la plataforma HealthCore Digital.

> **De James (CTO) — Ticket Jira HCR-0188:**
> "Necesitamos una API de inventario de material sanitario como base para el panel de operaciones clínicas. Las entradas de suministros son entregas de proveedores. Las salidas son consumos clínicos registrados por el personal de la clínica. El stock siempre es el neto de entradas menos salidas — no se permite la modificación directa. Todas las rutas bajo `/inventory`. Los UUIDs de usuario vienen de TinyDB. Claire ha confirmado: los datos de inventario de suministros son operativos, no PHI — no hay barreras HIPAA en esta API, pero el acceso debe estar autenticado."

---

## Nombres de Entidades y Especificación de Campos

Usa estos nombres exactamente en tus modelos, schemas y respuestas de la API.

### `MedicalSupply` (equivale a `Product` del README)

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `name` | `str` | Ej.: `"Guantes de nitrilo (caja de 100)"`, `"Test rápido de estreptococo"` |
| `sku` | `str` | Código de catálogo interno, ej.: `"HCR-PPE-001"`, `"HCR-DIAG-003"` |
| `category` | `str` | `"ppe"`, `"wound_care"`, `"diagnostics"`, `"medications"`, `"consumables"` |
| `unit` | `str` | `"box"`, `"unit"`, `"pack"`, `"vial"` |
| `country` | `str` | `"US"` o `"UK"` — jurisdicción regulatoria |
| `current_stock` | `int` | **Campo calculado — no almacenado.** Derivado de los movimientos de suministros. Incluir solo en el schema de respuesta. |

### `SupplyDelivery` (equivale a `InboundOrder` del README)

Un envío de proveedor recibido en una clínica HealthCore.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `supply_id` | `int` (FK → MedicalSupply) | |
| `quantity` | `int` | Unidades recibidas |
| `vendor_name` | `str` | Ej.: `"MedLine Industries"`, `"Cardinal Health UK"` |
| `clinic_id` | `int` | Clínica receptora (1–12). No es FK — los datos de clínicas se gestionan por separado. |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del administrador de la clínica que confirmó la entrega (de TinyDB) |

### `SupplyConsumption` (equivale a `OutboundOrder` del README)

Un evento de uso clínico: suministros consumidos durante la atención al paciente.

| Campo | Tipo | Notas |
|-------|------|-------|
| `id` | `int` (PK) | Autoincremental |
| `supply_id` | `int` (FK → MedicalSupply) | |
| `quantity` | `int` | Unidades consumidas |
| `consumption_type` | `str` | `"clinical_use"` (usado en atención al paciente) o `"expiry_waste"` (caducado y desechado) |
| `clinic_id` | `int` | Clínica donde ocurrió el consumo |
| `created_at` | `datetime` | Se establece automáticamente al crear |
| `user_uuid` | `str` | UUID del personal clínico o administrativo que registró el consumo (de TinyDB) |

---

## Router de la API

Todos los endpoints deben registrarse bajo el prefijo `/inventory`. El archivo del router se encuentra en `services/routers/inventory.py`.

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/inventory/products` | Lista todos los suministros médicos con `current_stock` |
| `POST` | `/inventory/products` | Registra un nuevo suministro |
| `GET` | `/inventory/products/{id}` | Obtiene un suministro con su stock actual |
| `POST` | `/inventory/orders/inbound` | Registra una entrega de proveedor (`SupplyDelivery`) |
| `POST` | `/inventory/orders/outbound` | Registra un consumo clínico (`SupplyConsumption`) |
| `GET` | `/inventory/orders` | Lista todas las entregas y consumos con datos del suministro |

---

## Reglas de Negocio

1. **`current_stock` siempre se calcula**, nunca se almacena. Para cualquier suministro: `current_stock = SUMA(SupplyDelivery.quantity) − SUMA(SupplyConsumption.quantity)`.
2. **No se puede registrar un `SupplyConsumption` si resultaría en stock negativo.** Devuelve `HTTP 400` con el mensaje: `"Insufficient stock for supply '{name}'. Available: {available}, requested: {quantity}."`. Rechazar antes de escribir.
3. **`consumption_type` debe ser `"clinical_use"` o `"expiry_waste"`**. Validar en el schema de request.
4. **Sin tabla de usuarios en Supabase.** Los campos `user_uuid` referencian usuarios de TinyDB. No crear un modelo User en SQLModel.
5. **Los suministros de EE.UU. y del Reino Unido coexisten en la misma tabla.** El campo `country` (`"US"` o `"UK"`) identifica la jurisdicción regulatoria. Debe estar presente tanto en el modelo como en el schema de respuesta.
6. **Los IDs de clínicas van del 1 al 12** (9 clínicas en EE.UU., 3 en el Reino Unido). Se almacenan como enteros, no como claves foráneas en este hito.

---

## Datos Semilla

Crea los siguientes registros al configurar tu base de datos de desarrollo local.

### MedicalSupplies (mínimo 6)

| name | sku | category | unit | country |
|------|-----|----------|------|---------|
| Guantes de nitrilo (caja de 100) | HCR-PPE-001 | ppe | box | US |
| Mascarilla quirúrgica (pack de 50) | HCR-PPE-002 | ppe | pack | UK |
| Apósito adhesivo para heridas | HCR-WND-001 | wound_care | box | US |
| Test rápido de estreptococo | HCR-DIAG-001 | diagnostics | unit | US |
| Tiras reactivas glucemia (50) | HCR-DIAG-002 | diagnostics | box | UK |
| Solución salina 0,9% 500ml | HCR-MED-001 | medications | vial | US |

### SupplyDeliveries (mínimo 4)

Registra al menos 2 entregas para `HCR-PPE-001` con cantidades diferentes. Usa nombres de proveedor como `"MedLine Industries"`, `"Cardinal Health UK"`, `"Bound Tree Medical"`. Mezcla IDs de clínica de ambos países.

### SupplyConsumptions (mínimo 3)

Incluye al menos un evento de `"clinical_use"` y uno de `"expiry_waste"`. Las cantidades no deben superar las entregas sembradas para el suministro afectado. Usa valores de `user_uuid` de tu instancia TinyDB.

---

## Estructura de Archivos (dentro de `services/`)

```
services/
├── main.py
├── database.py          # Cliente TinyDB + motor SQLModel + dependencia get_db
├── models.py            # MedicalSupply, SupplyDelivery, SupplyConsumption (SQLModel)
├── schemas.py           # Schemas Pydantic de request/response
└── routers/
    └── inventory.py     # APIRouter(prefix="/inventory")
```

---

## Notas de Evaluación para HealthCore

- El evaluador registrará un `SupplyConsumption` que supere el stock disponible y esperará `HTTP 400`.
- El evaluador intentará un `SupplyConsumption` con un valor de `consumption_type` inválido y esperará un error de validación.
- El evaluador verificará que `current_stock` en `GET /inventory/products` refleja el neto de las entregas y consumos sembrados.
- El campo `country` debe estar presente tanto en el modelo como en el schema de respuesta.
- El campo `clinic_id` debe estar presente tanto en `SupplyDelivery` como en `SupplyConsumption`.

---

_Documento interno — 4Geeks Academy · Track de Ingeniería de IA_
_Hito 5 · Escenario HealthCore_
