---
title: "Optimize Ubuntu on a VPS to use RAM more efficiently"
description: "Measure base RAM on Ubuntu 22.04, disable unused cloud-unneeded services with systemctl, optionally stop Snap, then verify you freed about 150–250 MB before running heavier apps."
author: "@marcogonzalo"
tags: ["Ubuntu", "VPS", "systemctl", "Linux", "RAM"]
---

# Optimize Ubuntu on a VPS to use RAM more efficiently

<!-- hide -->

_Estas instrucciones también están disponibles en [español](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/optimize-ubuntu-vps-ram-efficiency/optimize-ubuntu-vps-ram-efficiency.es.md)._

<!-- endhide -->

You rent a small VPS (often **1–2 GB of RAM**). You install tools, start a process, and the machine feels slow — or the OOM killer stops your app — even though you barely started working. Ubuntu is not “broken”; it is running many **background services** meant for laptops and desktops, not a bare cloud server.

This lesson shows how to **measure** that waste, **turn off** services that do nothing useful on a typical VPS, and **check** that free RAM went up. That headroom matters later when you run heavier workloads (databases, containers, AI assistants such as OpenClaw, build tools, and similar).

## What you will achieve

- Read RAM usage with `free -h` before and after changes.
- Understand what a **systemd service** is and how `systemctl` starts, stops, and disables it.
- Safely disable common unused services on Ubuntu 22.04 on a VPS.
- Optionally reduce Snap-related RAM use.
- Confirm nothing critical for SSH and basic networking broke.

```mermaid
flowchart LR
  measure[Measure RAM]
  stop[Disable unused services]
  snap[Optional: stop Snap]
  verify[Measure RAM again]
  measure --> stop --> snap --> verify
```

## Requirements

- An **Ubuntu 22.04** VPS (or similar Ubuntu server image).
- SSH access and a terminal (local terminal or Remote SSH in your editor).
- Permission to run `sudo` (admin rights on that machine).
- Basic CLI comfort: you can run a command, read its output, and paste the next one.

> **Safety:** Only disable services listed here on a **cloud VPS**. Do not copy this blindly onto a physical office PC that needs printers, Bluetooth, or local network discovery.

---

## 1. What is wasting RAM?

A **service** is a program the OS starts in the background and keeps running. Ubuntu ships with many of them so a desktop install “just works.” On a VPS you usually have:

- No printer
- No Bluetooth
- No local Wi‑Fi modem
- No need to discover printers/TVs on a home LAN

Those services still sit in RAM. Disabling them does not uninstall Ubuntu; it only stops them from starting at boot and frees memory for **your** work.

### Quick glossary

| Term              | Meaning                                                                        |
| ----------------- | ------------------------------------------------------------------------------ |
| **RAM**           | Working memory. When it fills up, the system swaps to disk or kills processes. |
| **service**       | Background program managed by **systemd**.                                     |
| **systemd**       | The init system on modern Ubuntu — starts services at boot.                    |
| **`systemctl`**   | CLI tool to start, stop, enable, or disable services.                          |
| **disable --now** | Stop the service **now** and prevent it from starting on next boot.            |

---

## 2. Measure RAM before you change anything

Connect to the VPS over SSH, then run:

```bash
free -h
```

Look at the **available** (or free) column on the `Mem:` line. Write that number down (or leave the terminal scrollback open). You will compare it after the cleanup.

Optional: list running services so you see what is active:

```bash
systemctl list-units --type=service --state=running
```

You do not need to understand every name. You only need a before/after RAM number.

---

## 3. Services that are safe to turn off on a typical VPS

Grouped by why they exist. On most small cloud servers, none of these are required.

### Desktop / hardware (useless in the cloud)

| Service        | What it does                                    | Why you can drop it         |
| -------------- | ----------------------------------------------- | --------------------------- |
| `cups`         | Print server                                    | No printer on a VPS         |
| `avahi-daemon` | Discovers devices on a local network (ZeroConf) | Cloud VPS is not a home LAN |
| `modemmanager` | Manages mobile modems                           | No 4G/5G modem attached     |
| `bluetooth`    | Bluetooth stack                                 | No Bluetooth hardware       |

### Automatic management

| Service               | What it does                           | Trade-off                                                                                                                                                   |
| --------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `snapd`               | Runs Snap packages                     | Uses a lot of RAM/CPU. If you install software via `apt`, official repos, or version managers (for example NVM for Node), you often do not need Snap.       |
| `unattended-upgrades` | Applies security updates automatically | Convenient, but can spike CPU/RAM at random times. Safer for learning: turn it off and run `sudo apt update` / `sudo apt upgrade` yourself when you choose. |

### Diagnostics and telemetry

| Service              | What it does                        | Why you can drop it                               |
| -------------------- | ----------------------------------- | ------------------------------------------------- |
| `apport`             | Error reporting                     | Extra RAM you do not need on a server you control |
| `popularity-contest` | Sends package-usage stats to Ubuntu | Optional telemetry                                |

### Storage multipath

| Service      | What it does                            | Why you can drop it                                              |
| ------------ | --------------------------------------- | ---------------------------------------------------------------- |
| `multipathd` | Handles multiple paths to the same disk | Common on enterprise SAN setups; rare on small single-disk VPSes |

If a name is **not installed**, `systemctl` will say the unit was not found. That is fine — skip it and continue.

---

## 4. Disable the unused services

### Step A — stop and disable the common set

Copy and paste this as one block (or line by line if you prefer):

```bash
sudo systemctl disable --now cups avahi-daemon modemmanager bluetooth apport popularity-contest
```

What this does:

1. **Stops** each service immediately (`--now`).
2. **Disables** it so it does not start again after reboot (`disable`).

If Ubuntu reports that a unit does not exist, ignore that line of output and keep going.

### Step B — optional: turn off automatic upgrades

Only if you accept updating packages yourself:

```bash
sudo systemctl disable --now unattended-upgrades
```

Then, when you want updates:

```bash
sudo apt update
sudo apt upgrade
```

### Step C — optional but high impact: Snap

Snap (`snapd`) is often the biggest RAM win on minimal VPSes. Disable it if you do **not** rely on Snap packages:

```bash
sudo systemctl disable --now snapd.service snapd.socket
```

Check whether anything you care about is a Snap:

```bash
snap list
```

If the list is empty or you only see packages you do not use, disabling Snap is usually fine. If a critical tool is installed only as a Snap, leave `snapd` alone or reinstall that tool another way first.

### Step D — multipath (common on VPSes)

```bash
sudo systemctl disable --now multipathd.service
```

---

## 5. Verify the result

### Confirm services are inactive

Replace `SERVICE` with a name from the list (example: `cups`):

```bash
systemctl is-active cups
systemctl is-enabled cups
```

Expect something like `inactive` / `disabled` (wording can vary slightly by unit).

Or check several at once:

```bash
systemctl is-active cups avahi-daemon modemmanager bluetooth apport snapd multipathd
```

### Measure RAM again

```bash
free -h
```

Compare **available** memory with your earlier number. Freeing about **150–250 MB** of base RAM is a realistic range after this cleanup (exact gain depends on the image and what was running).

### Confirm you can still use the server

Stay connected over SSH. Run a simple check:

```bash
uptime
hostname
```

If SSH still works and those commands respond, you did not break the basics. Reboot once when convenient and SSH in again to confirm services stay off after boot:

```bash
sudo reboot
```

Wait a minute, reconnect, then run `free -h` again.

---

## 6. What not to disable (for this lesson)

Leave these alone unless an instructor or guide says otherwise:

- Networking (`systemd-networkd`, NetworkManager if that is what your image uses)
- SSH (`ssh` / `sshd`)
- Logging (`rsyslog` or `systemd-journald`)
- Cron / timers you rely on for backups or jobs
- Docker, databases, reverse proxies, or app runtimes **you installed on purpose**

When unsure: **measure first**, disable one group, measure again. Prefer small steps over one giant paste on a production machine you cannot afford to lock out of.

---

## VPS RAM optimization checklist

```text
□ Connected to the Ubuntu VPS over SSH
□ Recorded free -h (available RAM) before changes
□ Disabled desktop/hardware services (cups, avahi-daemon, modemmanager, bluetooth)
□ Disabled apport and popularity-contest (if present)
□ Decided on unattended-upgrades (kept or disabled + manual apt upgrades)
□ Decided on snapd (disabled only if Snap packages are not required)
□ Disabled multipathd if unused
□ Ran free -h again and saw more available RAM (often ~150–250 MB)
□ Confirmed SSH still works after changes (and after reboot if you rebooted)
```

## Conclusion

Ubuntu on a VPS often wastes RAM on services built for physical desktops and complex networks. Measure with `free -h`, turn off the safe list with `systemctl disable --now`, optionally drop Snap and noisy auto-upgrades, then measure again. The goal is a lighter base system so later heavy apps — from databases and containers to assistants like OpenClaw — have room to run without fighting the OS for memory.
