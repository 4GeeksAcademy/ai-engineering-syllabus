# In-class example: Prep a café Wi‑Fi router VPS twin (Class Example)

> **For instructors:** Live demo parallel to `vps-ssh-resource-optimization`. Same spine — SSH, inventory, safe `systemctl` cleanup, after evidence — different story. **Do not assign as homework.** Target ~60–90 minutes including discussion.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The scenario

### Scope note

Shorter than the student project: one guided VPS, one after TXT file, no optional reboot deep-dive unless time allows. Students still follow the full root `README.md`.

A neighborhood café runs an Ubuntu cloud box that only hosts a simple status page. The owner complains the box feels “full” even with almost no traffic. In class you will SSH in, measure RAM/disk, turn off unused desktop-style services, and save an after snapshot that says the box is ready and what resources remain.

**What you are teaching:**

- SSH as the normal way to reach a server
- Reading `free -h` / `df -h` / OS release
- Safe vs unsafe services to disable on a VPS
- Delivering after evidence as a text file

---

## Prerequisites

- Instructor VPS credentials
- Terminal or editor with Remote SSH
- Course lesson on Ubuntu VPS RAM efficiency open for copy/paste commands

---

## Step-by-step tasks

### 1. Connect

- [ ] `ssh cafe_user@vps_ip`
- [ ] Run `hostname` and `whoami`

### 2. Inventory before (demo only)

- [ ] `cat /etc/os-release`
- [ ] `free -h`
- [ ] `df -h`
- [ ] Optional: `systemctl list-units --type=service --state=running | head`

### 3. Optimize

- [ ] Apply the lesson’s safe `systemctl disable --now ...` list
- [ ] Decide live with the class whether to touch Snap / multipath
- [ ] Confirm SSH still works

### 4. Capture after evidence

- [ ] Create `resources-after.txt` on the laptop (or on the VPS then download) with `free -h` and `df -h` after cleanup
- [ ] Show the file in the editor as the “delivery” shape students must push to GitHub

---

## Discussion questions

1. Why measure **before** if the graded delivery is only **after**?
2. Which services would you **never** disable on a VPS used only over SSH, and why?
3. When would keeping `unattended-upgrades` be the better ops choice than turning it off for RAM?
