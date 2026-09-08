---
layout: post
title: "Release: Deckbuilder v1.1"
date: 2026-09-07
categories: [software, hamradio]
tags: [software, deckbuilder, superstation, radio-packs, openpgp]
author: Jason Johnson (K3JSJ)
---

I'm pleased to announce the **official public release of Deckbuilder v1.1**.

Deckbuilder is a stand-alone Windows tool for creating **radio pack folders** — themed sets of equipment artwork that players can install in the [SUPERSTATION]({{ "/software/superstation" | relative_url }}) application. A pack replaces the default card art for four equipment slots (Computer, Radio, Amplifier, and Antenna) across five level tiers.

See the [Deckbuilder software page]({{ "/software/deckbuilder" | relative_url }}) for full details, or browse all of my amateur radio software on the [Software]({{ "/software" | relative_url }}) page.

👇 **Download the release here:**
**[deckbuilder-1.1-64bit.zip](https://downloads.k3jsj.net/deckbuilder/deckbuilder-1.1-64bit.zip)**

👇 **Watch the walkthrough here:**
**<a href="https://youtu.be/Sf6rplA0cYI" target="_blank">Deckbuilder walkthrough</a>**

---

# 🚀 What Deckbuilder Does

- **Assembles and validates your image assets** for all four equipment slots across five level tiers
- **Generates the `pack.json` manifest** with metadata and SHA-256 image hashes
- **Signs the manifest with an OpenPGP key** so SUPERSTATION can verify authenticity
- **Verifies the integrity** of your own or someone else's pack before distribution

---

# 🎥 Video

Watch the walkthrough: <a href="https://youtu.be/Sf6rplA0cYI" target="_blank">Deckbuilder walkthrough</a>

---

# 📥 Download

Deckbuilder is a stand-alone executable for 64-bit Windows 10 and Windows 11.

👇 **[deckbuilder-1.1-64bit.zip](https://downloads.k3jsj.net/deckbuilder/deckbuilder-1.1-64bit.zip)** sha256:`a618c92803573662302ba2bf0a453e8afe20db1ad0b2f9a48195fef661d22bf6`

Verify the file with the accompanying [digital signature](https://downloads.k3jsj.net/deckbuilder/deckbuilder-1.1-64bit.zip.sig) and my [public GnuPG key](https://keyserver.ubuntu.com/pks/lookup?search=K3JSJ%40arrl.net&fingerprint=on&op=index).

---
