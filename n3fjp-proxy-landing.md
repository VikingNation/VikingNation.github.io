---
layout: page
title: N3FJP Proxy
permalink: /software/n3fjp-proxy
---

N3FJP Proxy is a free Windows application that bridges **N3FJP Amateur Contact Log** and **FLRIG**, enabling seamless frequency, mode, and PTT synchronization between your logging software and your radio — without requiring a direct hardware CAT connection.

---

## Download

 <a href="https://downloads.k3jsj.net/n3fjp-proxy/n3fjp-proxy-1.0.0-beta.zip">n3fjp-proxy-beta-1.0.0.zip</a> (MD5SUM: <code>9fc43f150cc20e81843f350d92bf97262f006b6beb268e65b9df3c025a078f33</code>

 <a href="https://downloads.k3jsj.net/n3fjp-proxy/n3fjp-proxy-1.0.0-beta.zip.sig">n3fjp-proxy-beta-1.0.0.zip.sig</a>  (Digital Signature)

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

3. **N3FJP Proxy** — Set IP address of FLRIG (127.0.0.1 or remote IP), Set FLRIG port to **12345**, Proxy port to **11000**
   *(File → Config)*

4. Click **Start Proxy**, then click **Test** in N3FJP — your radio's
   frequency and mode should appear.

See note below about Firewall & Antivirus

---

## Package Contents

The download includes:

- `n3fjp-proxy.exe` — Application executable
- `n3fjp-proxy.exe.sig` - Digital signature of the n3fjp-proxy.exe
- `README.txt` — Version, setup summary, and file integrity information
- `DISCLAIMER.TXT` — Full terms of use

---

## Firewall & Antivirus

N3FJP Proxy opens a TCP server socket to accept connections from N3FJP. Windows Firewall may prompt you to allow access the first time you start the proxy, or may silently block it. If N3FJP cannot connect, add a firewall exception for `n3fjp-proxy.exe`:

> **Windows Security → Firewall & network protection → Allow an app through firewall → Add n3fjp-proxy.exe**

If you use a third-party security suite (e.g. Norton, Bitdefender, McAfee), it may include its own firewall that blocks the proxy independently of Windows Firewall. Add an exception for `n3fjp-proxy.exe` in that product's firewall settings as well. Consult your security product's help documentation for details.

Your antivirus software may also flag or quarantine the executable because it is unsigned. If the proxy fails to start or disappears after download, add an exception in your antivirus product for `n3fjp-proxy.exe` or the folder it is stored in. Consult your antivirus product's help documentation for instructions specific to your software.

---

## Open Source Components

N3FJP Proxy includes the following open source library:

| Library | Purpose | License |
|---|---|---|
| [pystray](https://github.com/moses-palmer/pystray) | System tray integration | [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.txt) |

In accordance with the LGPLv3, you may obtain the pystray source code at the link above and recompile or relink it with this application if desired.

---

## Disclaimer

N3FJP Proxy is an independent, community-created tool. It is not affiliated
with or endorsed by Scott Davis (N3FJP) or Dave Freese (W1HKJ / FLRIG).
See `DISCLAIMER.TXT` for full terms.

---
## Contact me
Jason Johnson &lt;[k3jsj@arrl.net](mailto:k3jsj@arrl.net)&gt;
