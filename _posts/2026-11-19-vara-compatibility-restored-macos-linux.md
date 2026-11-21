---
layout: post
title: "VARA compatibility restored, plus native macOS and Linux versions announced"
date: 2026-11-19 17:46:22 -0500
categories: [software]
tags: [software, vara, winlink, varac, macos, linux]
description: "VARA HF v4.9.2 and VARA FM v4.4.2 are out and are compatible with older versions, so the January 1, 2027 compatibility break no longer applies. The developer also announced native macOS and Linux VARA versions in the works for Winlink and VarAC."
image:
  path: /images/2026/vara-compatibility-restored-macos-linux/vara-compatibility-restored-macos-linux.png
  alt: "Breaking News video thumbnail: a cheering crowd faces a stage screen reading \"New VARA release! Restores compatibility, native macOS and Linux versions!\", with the caption \"Compatibility restored, Linux / macOS support\"."
---

**BLUF:** New releases **VARA HF v4.9.2** and **VARA FM v4.4.2** are **compatible with older versions**. They replace HF v4.9.1 and FM v4.4.1, the releases that would have stopped working with earlier versions on **January 1, 2027**. The developer also announced work on a **multiplatform VARA**, with **native macOS and Linux versions** for use with Winlink and VarAC.
{: .prompt-tip }

I covered this news in a YouTube video:

{% include embed/youtube.html id='GpE25zZVynY' %}

<a href="https://youtu.be/GpE25zZVynY" target="_blank" rel="noopener noreferrer">Watch on YouTube: VARA - Compatibility restored and macOS & Linux announcement!</a>

## Compatibility restored

In my [post from November 11]({% post_url 2026-11-11-vara-breaks-compatibility-2027 %}) I covered VARA HF 4.9.1 and VARA FM 4.4.1. They were released on November 4, 2026 without any notes, and from January 1, 2027 they would no longer have worked with earlier VARA versions. In my [follow-up post]({% post_url 2026-11-14-winlink-rms-vara-exposure %}) I counted **1,072** Winlink RMS stations that offer VARA, **360** of which offer nothing but VARA.

That break is now off the table. The VARA developer's page, [rosmodem.wordpress.com](https://rosmodem.wordpress.com/){:target="_blank" rel="noopener noreferrer"}, now says:

> **ATTENTION!**
> A new versions just released, compatible with the older versions. Replace VARA HF v4.9.1 by v4.9.2 and VARA FM v4.4.1 by v4.4.2.

| Product | Replace | With |
|---|---|---|
| VARA HF | v4.9.1 | **v4.9.2** |
| VARA FM | v4.4.1 | **v4.4.2** |

The other VARA products listed on the page were not part of this change: VARA SAT v4.4.5, VARA Chat v1.4.2 and VARA Terminal v1.2.2.

**What to do:** if you installed VARA HF 4.9.1 or VARA FM 4.4.1, replace them with 4.9.2 and 4.4.2. Sysops of RMS gateways should do the same. The downloads are linked from [rosmodem.wordpress.com](https://rosmodem.wordpress.com/){:target="_blank" rel="noopener noreferrer"} and hosted at [downloads.winlink.org](https://downloads.winlink.org/VARA%20Products/){:target="_blank" rel="noopener noreferrer"}.
{: .prompt-info }

## Native macOS and Linux VARA announced

The same page announces a multiplatform VARA:

> We are working in a VARA multiplatform to have native macOS and Linux VARA versions available with Winlink and VarAC.

Today, running VARA on a Mac or on Linux means running the Windows build under Wine or in a virtual machine. A native build would remove that step for Winlink and VarAC users on those platforms.

No release date, beta schedule or licensing details have been published yet. The page only says the work is in progress. I will post an update when more is known.
{: .prompt-warning }

## Sources

- VARA developer page: <https://rosmodem.wordpress.com/>
- VARA downloads: <https://downloads.winlink.org/VARA%20Products/>
- Video: <https://youtu.be/GpE25zZVynY>
