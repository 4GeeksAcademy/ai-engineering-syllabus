# CONTEXT — Directorio de Proveedores · HealthCore

_These instructions are also available in [English](./CONTEXT-healthcore.en.md)._

> **Milestone:** 09 — Lightweight Storage API  
> **Ruta en el repositorio:** `09-lightweight-storage/CONTEXT-healthcore.md`

---

## Tu empresa

Eres parte del equipo **HealthCore Digital**, la unidad tecnológica interna de HealthCore, una red de **12 clínicas ambulatorias** con operaciones en Estados Unidos (Texas, Florida, Georgia) y el Reino Unido (Londres y Manchester). Tu tech lead es **James Osei**, CTO, y el proyecto ha sido solicitado conjuntamente por **Diane Foster** (VP of People) y **Claire Whitfield** (Chief Compliance Officer).

HealthCore trabaja con proveedores externos en dos categorías amplias: proveedores clínicos y operacionales (material médico, laboratorio, limpieza) y proveedores tecnológicos (software, plataformas, servicios en la nube). Hasta ahora, cada departamento gestiona su propio listado en hojas de cálculo separadas. Claire, además, necesita tener visibilidad de todos los proveedores tecnológicos para verificar que tienen firmados los acuerdos de cumplimiento requeridos (BAA en USA, DPA en UK). Este proyecto crea el registro centralizado que da respuesta a ambas necesidades.

---

## Modelo de proveedor

Cada proveedor en el directorio de HealthCore tiene la siguiente estructura:

| Campo                   | Tipo                                  | Descripción                                                                                |
| ----------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------ |
| `name`                  | string, requerido                     | Nombre comercial del proveedor o plataforma                                                |
| `country`               | string, requerido                     | País del contrato: `"USA"` o `"UK"`                                                        |
| `categories`            | lista de strings, requerido, mínimo 1 | Tipo de servicio o producto que provee (ver lista válida)                                  |
| `monthly_rate`          | float, requerido, > 0                 | Coste mensual vigente en la moneda del contrato                                            |
| `currency`              | string, requerido                     | `"USD"` para USA, `"GBP"` para UK                                                          |
| `rate_updated_at`       | datetime, generado por el sistema     | Timestamp de la última actualización de tarifa                                             |
| `status`                | string, requerido                     | `"active"` o `"suspended"`                                                                 |
| `compliance_agreement`  | string, opcional                      | Tipo de acuerdo de cumplimiento firmado: `"BAA"`, `"DPA"`, `"both"`, o `null` si no aplica |
| `contract_renewal_date` | string, opcional                      | Fecha de renovación del contrato (formato `YYYY-MM-DD`)                                    |
| `contact_email`         | string, opcional                      | Email del account manager del proveedor                                                    |
| `notes`                 | string, opcional                      | Observaciones internas                                                                     |

### Categorías válidas

```python
VALID_CATEGORIES = [
    "medical_supplies",
    "laboratory_services",
    "pharmaceutical",
    "clinical_software",
    "it_infrastructure",
    "hr_and_payroll_software",
    "cleaning_and_facilities",
    "patient_communication",
    "billing_and_coding_software",
    "training_platforms"
]
```

### Estados válidos

```python
VALID_STATUSES = ["active", "suspended"]
```

---

## Datos iniciales del seeder

El seeder debe cargar exactamente los siguientes proveedores, que representan el estado actual del directorio combinado de Diane y Claire.

```python
SUPPLIERS_SEED = [
    {
        "name": "McKesson Medical Supplies",
        "country": "USA",
        "categories": ["medical_supplies"],
        "monthly_rate": 4200.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contract_renewal_date": "2025-06-30",
        "contact_email": "accounts@mckesson.com",
        "notes": "Proveedor principal de material clínico para las 9 clínicas de USA."
    },
    {
        "name": "NHS Supply Chain",
        "country": "UK",
        "categories": ["medical_supplies"],
        "monthly_rate": 2800.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contact_email": "enquiries@supplychain.nhs.uk"
    },
    {
        "name": "Quest Diagnostics",
        "country": "USA",
        "categories": ["laboratory_services"],
        "monthly_rate": 3100.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contract_renewal_date": "2025-12-15",
        "contact_email": "business@questdiagnostics.com",
        "notes": "Procesamiento de laboratorio para clínicas de Texas y Florida."
    },
    {
        "name": "Synnovis UK",
        "country": "UK",
        "categories": ["laboratory_services"],
        "monthly_rate": 1950.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contact_email": "contracts@synnovis.co.uk"
    },
    {
        "name": "Epic Systems",
        "country": "USA",
        "categories": ["clinical_software"],
        "monthly_rate": 8500.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contract_renewal_date": "2026-01-01",
        "contact_email": "enterprise@epic.com",
        "notes": "EHR principal para las clínicas de USA. Contrato de largo plazo."
    },
    {
        "name": "EMIS Health",
        "country": "UK",
        "categories": ["clinical_software"],
        "monthly_rate": 3400.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contract_renewal_date": "2025-09-01",
        "contact_email": "accounts@emishealth.com",
        "notes": "EHR para las clínicas de Londres y Manchester."
    },
    {
        "name": "Availity",
        "country": "USA",
        "categories": ["billing_and_coding_software"],
        "monthly_rate": 1200.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contact_email": "enterprise@availity.com",
        "notes": "Plataforma de verificación de elegibilidad y envío de claims."
    },
    {
        "name": "Twilio",
        "country": "USA",
        "categories": ["patient_communication"],
        "monthly_rate": 680.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contract_renewal_date": "2025-10-31",
        "contact_email": "healthcare@twilio.com",
        "notes": "SMS y email automatizados para recordatorios de citas."
    },
    {
        "name": "AWS Healthcare",
        "country": "USA",
        "categories": ["it_infrastructure"],
        "monthly_rate": 5600.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": "BAA",
        "contact_email": "aws-health@amazon.com",
        "notes": "Infraestructura cloud principal. BAA firmado y auditado anualmente."
    },
    {
        "name": "Microsoft Azure UK",
        "country": "UK",
        "categories": ["it_infrastructure"],
        "monthly_rate": 2100.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contact_email": "enterprise@microsoft.com"
    },
    {
        "name": "Workday",
        "country": "USA",
        "categories": ["hr_and_payroll_software"],
        "monthly_rate": 2400.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": None,
        "contract_renewal_date": "2025-08-15",
        "contact_email": "enterprise@workday.com",
        "notes": "HRIS para toda la plantilla de USA. No maneja PHI."
    },
    {
        "name": "Sage Payroll UK",
        "country": "UK",
        "categories": ["hr_and_payroll_software"],
        "monthly_rate": 890.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contact_email": "business@sage.co.uk"
    },
    {
        "name": "ServiceMaster Clean",
        "country": "USA",
        "categories": ["cleaning_and_facilities"],
        "monthly_rate": 3800.0,
        "currency": "USD",
        "status": "active",
        "compliance_agreement": None,
        "contact_email": "healthcare@servicemaster.com",
        "notes": "Limpieza clínica para las 9 ubicaciones de USA."
    },
    {
        "name": "Healthstream LMS",
        "country": "USA",
        "categories": ["training_platforms"],
        "monthly_rate": 1100.0,
        "currency": "USD",
        "status": "suspended",
        "compliance_agreement": "BAA",
        "contact_email": "enterprise@healthstream.com",
        "notes": "Suspendido. Diane está evaluando reemplazarlo por una solución interna."
    },
    {
        "name": "Nuffield Health Supplies",
        "country": "UK",
        "categories": ["medical_supplies", "cleaning_and_facilities"],
        "monthly_rate": 1650.0,
        "currency": "GBP",
        "status": "active",
        "compliance_agreement": "DPA",
        "contact_email": "procurement@nuffieldhealth.com"
    }
]
```

---

## Restricciones de negocio

- **Moneda por país:** Un proveedor de `"USA"` debe tener `currency = "USD"`. Un proveedor de `"UK"` debe tener `currency = "GBP"`. La API rechaza combinaciones inconsistentes.
- **Acuerdo de cumplimiento:** El campo `compliance_agreement` es opcional, pero los proveedores con categorías `clinical_software`, `it_infrastructure`, `patient_communication` o `billing_and_coding_software` deberían tenerlo registrado. No es una validación automática de la API, sino una responsabilidad de quien registra el proveedor.
- **Trazabilidad de tarifas:** Cada actualización de `monthly_rate` debe registrar `rate_updated_at`. Claire usa este dato en auditorías para verificar que los cambios de coste tienen trazabilidad.
- **Suspensión, no borrado:** Los proveedores no se eliminan del directorio. Se suspenden. Mantener el historial es especialmente relevante en HealthCore por el entorno regulatorio: una auditoría puede preguntar con qué proveedores se trabajó en un período determinado.

---

## Lo que verán Diane y Claire en el frontend

La página del directorio debe permitirles:

1. Ver todos los proveedores con categoría, tarifa mensual, acuerdo de cumplimiento y estado.
2. Filtrar por país (USA / UK) para gestionar cada mercado de forma independiente.
3. Filtrar por categoría para localizar rápidamente proveedores de una tipología concreta.
4. Distinguir visualmente los proveedores activos de los suspendidos.
5. Registrar un proveedor nuevo desde un formulario.
6. Actualizar la tarifa mensual de un proveedor y ver el cambio reflejado inmediatamente.
7. Activar o suspender un proveedor con un control visible en cada fila.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
