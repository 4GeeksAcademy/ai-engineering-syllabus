# Ejemplo en Clase: Ping Rápido de Salud por Código de Barras

> **Nota para el instructor:** Ejemplo en vivo para clase que enseña los conceptos del proyecto `n8n-snackcheck-nutrition`. Úsalo en clase para guiar webhook → API → IF → IA → Respond. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Acotado a una sesión en vivo. Mismo stack y patrones centrales que el proyecto oficial, pero omite requisitos secundarios (CHANGELOG SemVer completo, suite `TC-XXX` completa, nodo Code de puntuación de preocupación, enrutamiento multi-tono de IA). Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Un fundador quiere un **demo mínimo** para inversores: pegar un código de barras y recibir una frase corta — saludable o no — con datos reales de Open Food Facts y una línea de Groq.

**Qué vas a aprender:**

- Webhook `POST` + Respond to Webhook
- HTTP GET sin clave a Open Food Facts
- Ramificación IF para producto no encontrado vs éxito
- Un nodo Groq para redactar una frase amigable
- Por qué continue-on-error importa ante un `404` de producto no encontrado

---

## Requisitos previos

- Espacio de trabajo n8n funcionando
- Credencial de Groq ya creada en el curso de integración de IA
- Sin registro ni clave en Open Food Facts

---

## Tareas paso a paso

### 1. Diagrama (5 minutos)

- [ ] Bosqueja: Webhook → Validar código presente → HTTP Request → IF (¿encontrado?) → Set fields → Groq → Respond
- [ ] Dibuja la salida de no encontrado hacia un Respond JSON

### 2. Webhook + validación

- [ ] Crea webhook `POST` en la ruta `/nutrition-check-demo`
- [ ] Si el cuerpo no tiene `barcode`, Respond con un JSON corto de uso

### 3. Open Food Facts

- [ ] HTTP Request GET: `https://world.openfoodfacts.org/api/v2/product/{{barcode}}.json?fields=product_name,nutriscore_grade,nutriments`
- [ ] Configura continue on error / ramificación para que un `404` no mate la ejecución
- [ ] Si no se encuentra: Respond JSON `{ "error": "product not found" }` con status `404`

### 4. Veredicto IA de una línea

- [ ] Set: nombre del producto + `nutriscore_grade`
- [ ] Groq: una frase alentadora o cautelosa solo a partir de la letra (simple para clase)
- [ ] Respond texto plano `200`

### 5. Códigos de demo en vivo

- [ ] Nutella `3017620422003`
- [ ] Un producto Nutri-Score `a` que elija el instructor en vivo

---

## Qué deben hacer aún en casa

Reglas completas de SnackCheck (semáforos + la peor de dos lecturas), puntuación de preocupación, prompts de IA con tono enrutado, README / registro de pruebas / CHANGELOG profesionales, y nombres `[Acción] - [Propósito]` — ver el `README.md` / `README.es.md` de la raíz.
