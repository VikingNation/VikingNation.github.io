---
layout: page
title: N3FJP Proxy
permalink: /software/n3fjp-proxy
---

N3FJP Proxy is a free Windows application that bridges **N3FJP Amateur Contact Log** and **FLRIG**, enabling seamless frequency, mode, and PTT synchronization between your logging software and your radio — without requiring a direct hardware CAT connection.

---

## Download

 <a href="https://downloads.k3jsj.net/n3fjp-proxy-1.0-beta.zip">n3fjp-proxy-beta-1.0.zip</a> (MD5SUM: <code>cd5eeaf106c482333075dc5a7a0e2b85a6014a36f0661d6c52855607f8128164</code>)

 <a href="https://downloads.k3jsj.net/n3fjp-proxy-1.0-beta.zip.sig">n3fjp-proxy-beta-1.0.zip.sig</a>  (Digital Signature)

---

## Screenshots

![N3FJP Proxy Main Window]({{ site.baseurl }}/images/2026/n3fjp-proxy/setup_proxy_02.png)

---

N3FJP Proxy sits between N3FJP Amateur Contact Log and FLRIG, translating the N3FJP API protocol into FLRIG XML-RPC commands. When you change frequency or mode in FLRIG, or other applications using FLRIG, N3FJP updates automatically — and vice versa.

**Key features:**

- Real-time frequency and mode synchronization between N3FJP and FLRIG
- Built-in step-by-step setup guide (View → Setup Instructions)
- Status indicators showing proxy, FLRIG, and N3FJP connection state
- System tray support — runs quietly in the background
- Configurable proxy and FLRIG ports
- Accessible font size controls (A+ / A−) for comfortable reading
- Saves window position across monitors and sessions
- Detailed log viewer with filter and export

---

## System Requirements

| | |
|---|---|
| **Operating System** | Windows 10 or Windows 11 (64-bit) |
| **FLRIG** | Any recent version with XML-RPC server enabled |
| **N3FJP** | Amateur Contact Log (any recent version) |
| **Installation** | None — single executable, no installer required |

---

## Quick Setup

N3FJP Proxy includes a built-in setup guide (View → Setup Instructions). The short version:

1. **FLRIG** — Enable the XML-RPC server at port **12345**
   *(Config → Setup → Server)*

2. **N3FJP** — Set the rig interface to **N3FJP API** at port **11000**
   *(Settings → Rig Interface)*

3. **N3FJP Proxy** — Set FLRIG port to **12345**, Proxy port to **11000**
   *(File → Config)*

4. Click **Start Proxy**, then click **Test** in N3FJP — your radio's
   frequency and mode should appear.

---

## Package Contents

The download includes:

- `n3fjp-proxy.exe` — Application executable
- `README.txt` — Version, setup summary, and file integrity information
- `DISCLAIMER.TXT` — Full terms of use

---

## Disclaimer

N3FJP Proxy is an independent, community-created tool. It is not affiliated
with or endorsed by Scott Davis (N3FJP) or Dave Freese (W1HKJ / FLRIG).
See `DISCLAIMER.TXT` for full terms.

---
## Contact me
Jason Johnson &lt;[k3jsj@arrl.net](mailto:k3jsj@arrl.net)&gt;
