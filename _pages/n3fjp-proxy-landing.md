---
layout: page
title: N3FJP Proxy
permalink: /software/n3fjp-proxy
---

N3FJP Proxy is a free Windows application that bridges **N3FJP Amateur Contact Log** and **FLRIG**, enabling seamless frequency, mode, and PTT synchronization between your logging software and your radio — without requiring a direct hardware CAT connection.

---

## Download

Release Date: July 14, 2026

 <a href="https://downloads.k3jsj.net/n3fjp-proxy/n3fjp-proxy-1.0.1-64bit.zip">n3fjp-proxy-1.0.1-64bit.zip</a> (SHA256SUM: <code>3e58dc56d1b7da5f66c170432448094d007fd85e9864cbe33261d860471dfe67</code>)

 <a href="https://downloads.k3jsj.net/n3fjp-proxy/n3fjp-proxy-1.0.1-64bit.zip.sig">n3fjp-proxy-1.0.1-64bit.zip.sig</a>  (Digital Signature)

It is recommended to verify the sha256sum of the ZIP file. The author has also signed the zip file using his PGP key (K3JSJ@ARRLNET).

---

## Installation
Download the ZIP file and unzip into a folder in your Windows profile (e.g., Desktop\, or Downloads\). The application does not require admintrator rights and it should be executed using normal user permissions.


---

## Screenshots

![N3FJP Proxy Main Window]({{ site.baseurl }}/images/2026/n3fjp-proxy/setup_proxy_02.png)

Figure 1 - Main screen of N3FJP Proxy

![N3FJP Proxy Config Window]({{ site.baseurl }}/images/2026/n3fjp-proxy/setup_proxy_01.png)

Figure 2 - Configuration menu (File => Config)


---

## Software Overview

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

** Updates 1.0.1 **
- TX Power now updates live in N3FJP's QSO entry screen (previously never worked - required a new connection into N3FJP's own API)
- Detect Settings - one-click auto-detect of IP/Port and installed apps, with guided setup
- App Launcher - auto-start/stop FLRIG, N3FJP, WSJT-X, Fldigi, VarAC, and FreeDV alongside the proxy
- Frequency Config editor with ARRL band-plan auto-populate
- Background/manual software update checker (this notice!)
- Separate status indicators for N3FJP Rig vs. N3FJP API connections
- Live power/frequency/mode display, N3FJP program name and version shown
- Accessibility improvements: keyboard navigation, contrast, colorblind-friendly status indicators, adjustable text size

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

N3FJP Proxy includes a built-in setup guide (View → Setup Instructions).

---

## Package Contents

The download includes:

- `n3fjp-proxy.exe` — Application executable
- `n3fjp-proxy.exe.sig` — Digital signature of application
- `README.txt` — Version, setup summary, and file integrity information
- `DISCLAIMER.TXT` — Full terms of use
- `sha256sum.txt`  — SHA256SUM of n3fjp-proxy.exe
- `docs\user-guide.html` - Full user guide
- `docs\images` - Folder containing images from user guide

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

It also includes the following permissively-licensed open source libraries (no source disclosure required):

| Library | Purpose | License |
|---|---|---|
| [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) | Themed widgets for tkinter | MIT AND (Apache-2.0 OR BSD-2-Clause) |
| [Pillow](https://python-pillow.github.io) | Image handling | MIT-CMU |
| [psutil](https://github.com/giampaolo/psutil) | Process and system utilities | BSD-3-Clause |
| [PGPy](https://github.com/SecurityInnovation/PGPy) | Registration-file signature verification | BSD-3-Clause |
| [cryptography](https://github.com/pyca/cryptography) | Cryptographic primitives (used by PGPy) | Apache-2.0 OR BSD-3-Clause |
| [pyasn1](https://github.com/pyasn1/pyasn1) | ASN.1 encoding/decoding (used by PGPy) | BSD-2-Clause |
| [cffi](https://github.com/python-cffi/cffi) | Foreign function interface (used by cryptography) | MIT |
| [pycparser](https://github.com/eliben/pycparser) | C parser in Python (used by cffi) | BSD-3-Clause |
| [pyperclip](https://github.com/asweigart/pyperclip) | Clipboard access | BSD |
| [truststore](https://github.com/sethmlarson/truststore) | Native OS certificate trust store verification | MIT |
| [six](https://github.com/benjaminp/six) | Python 2/3 compatibility shim (used by pystray) | MIT |

---

## Disclaimer

N3FJP Proxy is an independent, community-created tool. It is not affiliated
with or endorsed by Scott Davis (N3FJP) or Dave Freese (W1HKJ / FLRIG).
See `DISCLAIMER.TXT` for full terms.

---

## Contact me
Jason Johnson &lt;[k3jsj@arrl.net](mailto:k3jsj@arrl.net)&gt;

---

*Copyright 2026 Jason Johnson (K3JSJ) — All rights reserved*
