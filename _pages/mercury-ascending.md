---
layout: page
title: Mercury Ascending
permalink: /software/mercury-ascending
---

> **DISCLAIMER:** This is beta software to help configure Mercury and VarAC for
> testing with the Mercury modem.

**Early observations from November 16 at 0130 UTC:**

- **BUSY INDICATOR:** VarAC's BUSY indicator does not show as active when Mercury
  is on frequency and someone is transmitting. Testing is needed to find out whether
  1) the modem is not detecting the busy channel, or 2) the modem is not passing the
  BUSY condition to VarAC.
- **CALLING STATION:** The VARA modem normally tries 15 times and, if it does not
  connect, sends a CW ID. The Mercury modem does not give up on connecting to the
  station, and VarAC thinks it is still trying to connect.
- **STANDALONE CLIENT:** With VarAC closed, I used the Mercury client. I had to set
  up CAT to use Hamlib, COM3 and IC-7300. PTT worked and audio went out.

---

![Mercury Ascending animated title]({{ site.baseurl }}/images/2026/mercury-ascending/mercury-ascending.gif)

**Mercury Ascending Installer** is a free, open source Windows tool that sets up the
open source [Mercury HF modem](https://github.com/Rhizomatica/mercury) (by Rhizomatica)
to work with [VarAC](https://www.varac-hamradio.com/) (by Irad Deutsch, 4Z1AC). It
downloads and installs Mercury, adds it to VarAC's Applications Launcher, and makes
Mercury listen on the ports VarAC already uses. It backs up your settings first and
can put them back with one click.

This is a **beta** release. Please report problems to <k3jsj@arrl.net> and include
the log file (**Open Log Folder** in the tool).

---

## Download

Version 0.9.3. Release date: November 15, 2026

<a href="https://downloads.k3jsj.net/mercury-ascending/mercury-ascending-0.9.3.zip" download>mercury-ascending-0.9.3.zip</a>
(SHA256SUM: <code>f19de985a11ce59631fad528204040fd9db724482c7796524b3974b3676b10a2</code>)

<a href="https://downloads.k3jsj.net/mercury-ascending/mercury-ascending-0.9.3.zip.sig" download>mercury-ascending-0.9.3.zip.sig</a>
(Digital Signature)

Check the SHA256 sum of the ZIP file before you use it. The ZIP file is also signed
with my GnuPG key. To verify it, get
[my public GnuPG key](https://keyserver.ubuntu.com/pks/lookup?search=K3JSJ%40arrl.net&fingerprint=on&op=index)
and run:

```
gpg --verify mercury-ascending-0.9.3.zip.sig mercury-ascending-0.9.3.zip
```

The signing key's fingerprint is `7E21 10D4 9069 0025 4539  C982 59C2 D5C7 F425 E802`.

---

## Installation

1. Download the ZIP file and unzip it into a folder in your Windows profile,
   e.g. `Documents\mercury-ascending`.
2. Close VarAC.
3. Double-click **`Mercury-Ascending-VarAC-Installer.bat`**.
4. Accept the Terms of Use. You are asked once for each new version.

**Requirements:**
- Windows 10 or 11, with Windows PowerShell 5.1 (built in).
- VarAC already installed.
- An internet connection.
- Administrator rights, but only when the Mercury installer runs.

---

## Screenshots

![Mercury Ascending main window]({{ site.baseurl }}/images/2026/mercury-ascending/main-window.png)

Figure 1 - Main window. The tool finds your VarAC instances and profiles at startup.

![Download Mercury page]({{ site.baseurl }}/images/2026/mercury-ascending/download-mercury.png)

Figure 2 - Download Mercury: pick a release from GitHub, then download and install it.

![Configure VarAC and Mercury page]({{ site.baseurl }}/images/2026/mercury-ascending/configure-varac.png)

Figure 3 - Configure VarAC & Mercury: VarAC's ports are read from its VARA tab and
written into Mercury's settings.

![Update available window]({{ site.baseurl }}/images/2026/mercury-ascending/update-available.png)

Figure 4 - Update check: release information is signature-verified before it is shown.

---

## What it does

1. **Download Mercury:** lists Mercury releases from GitHub, downloads the Windows
   installer you pick and runs it.
2. **Configure VarAC & Mercury:**
   - Adds Mercury to VarAC's Applications Launcher and switches the launcher on, so
     VarAC starts Mercury before it starts itself.
   - Sets Mercury's ports in `mercury.ini` to match VarAC's (control 8300, data 8301
     and KISS 8100 by default).
   - Can switch off VARA HF entries in the launcher.
   - Doesn't change VarAC's VARA tab.
3. **Restore VarAC settings:** every change is backed up first. Pick a backup to put
   your settings back.

**Other features:**
- Works with several VarAC instances and with VarAC profiles (custom config files).
- **Launch VarAC** starts any instance or profile and shows which modem it will use.
- Warns you when VarAC is running, because VarAC saves its settings on exit and
  would overwrite the changes.
- **Checks for updates** and verifies each download's GnuPG signature before using it.
- Keeps a log file of everything it does.

---

## License

Mercury Ascending Installer is open source, released under the **MIT License**.
Copyright (c) 2026 Jason Johnson (K3JSJ). The `LICENSE` and `THIRD-PARTY-NOTICES.md`
files are in the ZIP. The included Michroma font is under the SIL Open Font License 1.1.

Mercury and VarAC are separate programs with their own licenses. This tool is not
affiliated with or endorsed by Rhizomatica or VarAC.

This tool was created with the help of [Claude Code](https://claude.com/claude-code),
an AI coding assistant from Anthropic.

---

## Version history

**0.9.3** (2026-11-15)
- Released under the MIT License.
- The About window shows the license and third-party notices.

**0.9.2** (2026-11-15)
- Checks for updates. Release information and downloads are verified with GnuPG
  signatures.

**0.9.1** (2026-11-15)
- New "Mercury Ascending" animated title.
- Faster VarAC search at startup.
- Terms of Use agreement.
