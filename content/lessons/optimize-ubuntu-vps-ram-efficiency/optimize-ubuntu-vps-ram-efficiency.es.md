---
title: "Optimizar Ubuntu en un VPS para usar la RAM de forma más eficiente"
description: "Mide la RAM base en Ubuntu 22.04, desactiva con systemctl servicios innecesarios en la nube, opcionalmente detén Snap y verifica que liberaste unos 150–250 MB antes de apps pesadas."
author: "@marcogonzalo"
tags: ["Ubuntu", "VPS", "systemctl", "Linux", "RAM"]
---

# Optimizar Ubuntu en un VPS para usar la RAM de forma más eficiente

<!-- hide -->

_These instructions are also available in [English](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/optimize-ubuntu-vps-ram-efficiency/optimize-ubuntu-vps-ram-efficiency.md)._

<!-- endhide -->

Alquilas un VPS pequeño (a menudo **1–2 GB de RAM**). Instalas herramientas, arrancas un proceso y la máquina va lenta — o el sistema mata tu app por falta de memoria — aunque apenas hayas empezado. Ubuntu no está “roto”: está ejecutando muchos **servicios en segundo plano** pensados para portátiles y escritorios, no para un servidor en la nube.

Esta lección enseña a **medir** ese desperdicio, **apagar** servicios que no aportan en un VPS típico y **comprobar** que la RAM libre subió. Ese margen importa después, cuando ejecutes cargas más pesadas (bases de datos, contenedores, asistentes de IA como OpenClaw, herramientas de build y similares).

## Qué vas a conseguir

- Leer el uso de RAM con `free -h` antes y después de los cambios.
- Entender qué es un **servicio de systemd** y cómo `systemctl` lo arranca, para o desactiva.
- Desactivar con seguridad servicios habituales e inútiles en Ubuntu 22.04 en un VPS.
- Reducir, si quieres, el consumo de RAM relacionado con Snap.
- Confirmar que SSH y la red básica siguen funcionando.

```mermaid
flowchart LR
  measure[Medir RAM]
  stop[Desactivar servicios inútiles]
  snap[Opcional: parar Snap]
  verify[Medir RAM otra vez]
  measure --> stop --> snap --> verify
```

## Requisitos

- Un VPS con **Ubuntu 22.04** (o una imagen similar de Ubuntu Server).
- Acceso SSH y una terminal (local o Remote SSH en tu editor).
- Permiso para usar `sudo` (administrador en esa máquina).
- Comodidad básica con la CLI: puedes ejecutar un comando, leer la salida y pegar el siguiente.

> **Seguridad:** Desactiva solo los servicios de esta lista en un **VPS en la nube**. No copies esto a ciegas en un PC de oficina que necesite impresoras, Bluetooth o descubrimiento en la red local.

---

## 1. ¿Qué está gastando RAM?

Un **servicio** es un programa que el sistema operativo arranca en segundo plano y mantiene en marcha. Ubuntu trae muchos para que un escritorio “funcione solo”. En un VPS normalmente tienes:

- Sin impresora
- Sin Bluetooth
- Sin módem Wi‑Fi / móvil
- Sin necesidad de descubrir impresoras o TVs en una LAN doméstica

Esos servicios siguen ocupando RAM. Desactivarlos no desinstala Ubuntu; solo evita que arranquen al reiniciar y libera memoria para **tu** trabajo.

### Glosario rápido

| Término           | Significado                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| **RAM**           | Memoria de trabajo. Si se llena, el sistema usa disco (swap) o mata procesos. |
| **servicio**      | Programa en segundo plano gestionado por **systemd**.                         |
| **systemd**       | El sistema de inicio en Ubuntu moderno — arranca servicios al boot.           |
| **`systemctl`**   | Herramienta de CLI para arrancar, parar, habilitar o deshabilitar servicios.  |
| **disable --now** | Para el servicio **ahora** y evita que arranque en el próximo reinicio.       |

---

## 2. Mide la RAM antes de cambiar nada

Conéctate al VPS por SSH y ejecuta:

```bash
free -h
```

Mira la columna **available** (o free) en la línea `Mem:`. Anota ese número (o deja el historial de la terminal visible). Lo compararás después de la limpieza.

Opcional: lista servicios en ejecución para ver qué hay activo:

```bash
systemctl list-units --type=service --state=running
```

No hace falta entender cada nombre. Solo necesitas un número de RAM antes/después.

---

## 3. Servicios que puedes apagar con seguridad en un VPS típico

Agrupados por el motivo por el que existen. En la mayoría de servidores cloud pequeños, ninguno es obligatorio.

### Escritorio / hardware (inútiles en la nube)

| Servicio       | Qué hace                                         | Por qué puedes quitarlo                   |
| -------------- | ------------------------------------------------ | ----------------------------------------- |
| `cups`         | Servidor de impresión                            | No hay impresora en un VPS                |
| `avahi-daemon` | Descubre dispositivos en la red local (ZeroConf) | Un VPS en la nube no es una LAN doméstica |
| `modemmanager` | Gestiona módems móviles                          | No hay módem 4G/5G                        |
| `bluetooth`    | Pila Bluetooth                                   | No hay hardware Bluetooth                 |

### Gestión automática

| Servicio              | Qué hace                                 | Compromiso                                                                                                                                                 |
| --------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `snapd`               | Ejecuta paquetes Snap                    | Consume mucha RAM/CPU. Si instalas software con `apt`, repos oficiales o gestores de versión (por ejemplo NVM para Node), a menudo no necesitas Snap.      |
| `unattended-upgrades` | Aplica actualizaciones de seguridad solo | Cómodo, pero puede disparar CPU/RAM en momentos raros. Más seguro al aprender: apágalo y ejecuta tú `sudo apt update` / `sudo apt upgrade` cuando quieras. |

### Diagnóstico y telemetría

| Servicio             | Qué hace                                       | Por qué puedes quitarlo                                 |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------- |
| `apport`             | Reportes de errores                            | RAM extra que no necesitas en un servidor que controlas |
| `popularity-contest` | Envía estadísticas de uso de paquetes a Ubuntu | Telemetría opcional                                     |

### Multipath de almacenamiento

| Servicio     | Qué hace                             | Por qué puedes quitarlo                                              |
| ------------ | ------------------------------------ | -------------------------------------------------------------------- |
| `multipathd` | Gestiona varias rutas al mismo disco | Habitual en SAN empresariales; raro en VPS pequeños de un solo disco |

Si un nombre **no está instalado**, `systemctl` dirá que la unit no existe. No pasa nada: sáltalo y sigue.

---

## 4. Desactiva los servicios innecesarios

### Paso A — parar y deshabilitar el conjunto habitual

Copia y pega este bloque (o línea a línea si prefieres):

```bash
sudo systemctl disable --now cups avahi-daemon modemmanager bluetooth apport popularity-contest
```

Qué hace:

1. **Para** cada servicio al momento (`--now`).
2. Lo **deshabilita** para que no arranque tras un reinicio (`disable`).

Si Ubuntu dice que una unit no existe, ignora esa línea de salida y continúa.

### Paso B — opcional: apagar actualizaciones automáticas

Solo si aceptas actualizar paquetes a mano:

```bash
sudo systemctl disable --now unattended-upgrades
```

Cuando quieras actualizar:

```bash
sudo apt update
sudo apt upgrade
```

### Paso C — opcional pero con mucho impacto: Snap

Snap (`snapd`) suele ser el mayor ahorro de RAM en VPS mínimos. Desactívalo si **no** dependes de paquetes Snap:

```bash
sudo systemctl disable --now snapd.service snapd.socket
```

Comprueba si algo importante es un Snap:

```bash
snap list
```

Si la lista está vacía o solo ves paquetes que no usas, desactivar Snap suele estar bien. Si una herramienta crítica solo está como Snap, deja `snapd` o reinstálala de otra forma primero.

### Paso D — multipath (muy común en VPS)

```bash
sudo systemctl disable --now multipathd.service
```

---

## 5. Verifica el resultado

### Confirma que los servicios están inactivos

Sustituye `SERVICE` por un nombre de la lista (ejemplo: `cups`):

```bash
systemctl is-active cups
systemctl is-enabled cups
```

Espera algo como `inactive` / `disabled` (el texto exacto puede variar un poco según la unit).

O comprueba varios a la vez:

```bash
systemctl is-active cups avahi-daemon modemmanager bluetooth apport snapd multipathd
```

### Mide la RAM otra vez

```bash
free -h
```

Compara la memoria **available** con el número anterior. Liberar unos **150–250 MB** de RAM base es un rango realista tras esta limpieza (la ganancia exacta depende de la imagen y de lo que estuviera en marcha).

### Confirma que sigues pudiendo usar el servidor

Mantén la sesión SSH. Ejecuta una comprobación simple:

```bash
uptime
hostname
```

Si SSH sigue y esos comandos responden, no rompiste lo básico. Cuando puedas, reinicia una vez y vuelve a entrar por SSH para confirmar que los servicios siguen apagados tras el boot:

```bash
sudo reboot
```

Espera un minuto, reconéctate y vuelve a ejecutar `free -h`.

---

## 6. Qué no debes desactivar (en esta lección)

No toques esto salvo que un instructor o una guía diga lo contrario:

- Red (`systemd-networkd`, NetworkManager si tu imagen lo usa)
- SSH (`ssh` / `sshd`)
- Logs (`rsyslog` o `systemd-journald`)
- Cron / timers que uses para backups o tareas
- Docker, bases de datos, reverse proxies o runtimes de apps que **instalaste a propósito**

Si dudas: **mide primero**, desactiva un grupo, mide otra vez. Mejor pasos pequeños que un pegado enorme en una máquina de producción de la que no te puedes quedar fuera.

---

## Checklist de optimización de RAM en el VPS

```text
□ Conectado al VPS Ubuntu por SSH
□ Anotado free -h (RAM available) antes de los cambios
□ Desactivados servicios de escritorio/hardware (cups, avahi-daemon, modemmanager, bluetooth)
□ Desactivados apport y popularity-contest (si existen)
□ Decidido sobre unattended-upgrades (mantenerlo o desactivarlo + apt manual)
□ Decidido sobre snapd (desactivado solo si no necesitas paquetes Snap)
□ Desactivado multipathd si no se usa
□ Ejecutado free -h otra vez con más RAM available (a menudo ~150–250 MB)
□ Confirmado que SSH sigue tras los cambios (y tras reiniciar, si reiniciaste)
```

## Conclusión

Ubuntu en un VPS suele gastar RAM en servicios pensados para escritorios físicos y redes complejas. Mide con `free -h`, apaga la lista segura con `systemctl disable --now`, opcionalmente quita Snap y las actualizaciones automáticas ruidosas, y vuelve a medir. El objetivo es una base más ligera para que después apps pesadas — desde bases de datos y contenedores hasta asistentes como OpenClaw — tengan sitio sin pelearse con el sistema operativo por memoria.
