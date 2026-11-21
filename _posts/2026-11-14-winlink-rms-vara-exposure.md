---
layout: post
title: "How many Winlink RMS gateways the VARA 1/1/2027 change could affect"
date: 2026-11-14
categories: [hamradio, vara]
tags: [vara, winlink, rms]
description: "Of 1,588 Winlink RMS stations in the public channel lists, 1,072 offer VARA and 360 offer nothing but VARA. These are the stations a VARA version mismatch could affect once the January 1, 2027 compatibility change takes effect."
image:
  path: /images/2026/vara-rms/vara-rms-movie-final-frame.jpg
  alt: "World map of Winlink RMS stations, with the 1,072 VARA stations marked impacted and the 516 non-VARA stations unmarked."
---

**BLUF:** Of the **1,588** Winlink RMS stations in the public channel lists, **1,072 (67.5%)** offer VARA HF and/or VARA FM, and **360 (22.7%)** offer **nothing but VARA**. These are the stations a VARA version mismatch could affect once the January 1, 2027 compatibility change takes effect.
{: .prompt-warning }

I covered this analysis in a YouTube video:

{% include embed/youtube.html id='oXg20fUvPMs' %}

<a href="https://youtu.be/oXg20fUvPMs" target="_blank" rel="noopener noreferrer">Watch on YouTube: How many Winlink RMS gateways the VARA 1/1/2027 change could affect</a>

In my [last post]({% post_url 2026-11-11-vara-breaks-compatibility-2027 %}) I covered VARA HF 4.9.1 and VARA FM 4.4.1. From January 1, 2027 they will not connect to earlier VARA versions. This post asks how much of the Winlink RMS gateway network depends on VARA, using the channel lists that Winlink Express downloads.

- **Data:** Winlink Express channel lists, downloaded 11 Nov 2026
- **Scope:** public channels only; private or unlisted gateways are not included
- **Analysis date:** 14 Nov 2026

## Key figures

Counted by unique callsign: one per station or sysop, with SSIDs merged. The per-SSID counts are shown alongside.

| | Unique callsigns | Share | SSIDs | Share | VARA is the only service¹ |
|---|---:|---:|---:|---:|---:|
| **Offer VARA (HF and/or FM)** | **1,072** | 67.5% | 1,354 | 64.0% | 360 callsigns / 647 SSIDs |
| **No VARA service** | **516** | 32.5% | 761 | 36.0% | |
| **All RMS stations** | **1,588** | 100% | **2,115** | 100% | |

¹ **VARA is the only service** is a subset of the "Offer VARA" row, not an extra row in the totals.
- **Callsigns:** 360 of the 1,072 VARA callsigns (33.6%) offer nothing but VARA. That is 22.7% of all 1,588 RMS callsigns. Of those 360, 67 offer VARA HF only, 257 VARA FM only and 36 both.
- **SSIDs:** 647 of the 1,354 VARA SSIDs (47.8%) offer nothing but VARA. That is 30.6% of all 2,115 SSIDs.
- **The rest:** the other 712 callsigns and 707 SSIDs that offer VARA also offer Packet, PACTOR or ARDOP.

## How the network splits

| | VARA is the only service | VARA plus Packet, PACTOR or ARDOP | No VARA | Total |
|---|---:|---:|---:|---:|
| Unique callsigns | 360 | 712 | 516 | 1,588 |
| SSIDs (each gateway separately) | 647 | 707 | 761 | 2,115 |

Stations offering VARA plus another mode stay reachable on that other mode when VARA versions don't match, if the user's own station supports it.

## What is changing

**Reported:**

- VARA HF v4.9.1, VARA FM v4.4.1 and VARA Chat v1.4.3 were posted to the Winlink downloads directory on November 4, 2026.
- From 12:00 AM local time on January 1, 2027, the new versions will not connect to earlier VARA versions. The date comes from each computer's clock.
- Public reporting describes the HF case, reproduced by advancing one computer's clock. Based on my own findings, VARA FM 4.4.1 is also affected.

**Not established:**

- No official statement from the VARA developer (EA5HVK) or the Winlink team, as of November 14, 2026.
- No published reason for the change and no detailed changelog.
- How many gateways run which VARA version. The channel lists don't record modem versions.

**What "affected" means here.** A version mismatch makes VARA connections fail. It does not take a gateway off the air. Stations and users running matching versions are unaffected. The counts in this post measure exposure to the change, not predicted outages.
{: .prompt-info }

## 1. Stations that provide VARA

| Service offered | SSIDs | Unique callsigns |
|---|---:|---:|
| VARA HF only | 145 | 67 |
| VARA FM only | 484 | 257 |
| VARA HF + FM only | 18 | 36 |
| **VARA is the only service** | **647** | **360** |
| VARA HF + a non-VARA mode | 161 | 108 |
| VARA FM + a non-VARA mode | 511 | 463 |
| VARA HF + FM + a non-VARA mode | 35 | 141 |
| **VARA plus at least one non-VARA mode** | **707** | **712** |
| **Total providing VARA** | **1,354** | **1,072** |
| *Offers VARA HF (any combination)* | *359* | *352* |
| *Offers VARA FM (any combination)* | *1,048* | *897* |

## 2. Stations with no VARA

| Modes offered | SSIDs | Unique callsigns |
|---|---:|---:|
| Packet (AX.25) only | 735 | 493 |
| PACTOR only | 21 | 10 |
| Packet + PACTOR | 0 | 9 |
| Packet + ARDOP | 2 | 2 |
| Packet + Robust Packet | 1 | 1 |
| Packet + PACTOR + Robust Packet | 0 | 1 |
| PACTOR + Robust Packet | 2 | 0 |
| **Total with no VARA** | **761** | **516** |

A 0 in one column is expected. Sysops often put each mode on its own SSID. A station with Packet on `-10` and PACTOR on its bare callsign shows per SSID as one "Packet only" and one "PACTOR only", but by callsign as one "Packet + PACTOR".

## Two ways to count

**Each SSID separately.** `W1ABC-10` and `W1ABC-11` are two stations. This counts the individual gateways a user can connect to: **2,115** in total.

**By unique callsign.** `W1ABC-10` and `W1ABC-11` are one station. This roughly counts sites or sysops: **1,588** in total. The animation below uses this count.

Neither is wrong; use one consistently and say which.

- 183 callsigns have VARA on some SSIDs and other modes on others. That is why "VARA is the only service" is 647 per SSID but 360 per callsign.
- 1,202 callsigns have a single SSID.
- 67 SSIDs appear in both the HF and VHF lists and are counted once.
- 31 callsigns, mostly club calls, operate from more than one 4-character grid square.

### Stations per mode

| Mode | Each SSID | By callsign |
|---|---:|---:|
| Packet (AX.25) | 1,279 | 1,138 |
| VARA FM | 1,048 | 897 |
| VARA HF | 359 | 352 |
| PACTOR | 139 | 137 |
| ARDOP | 119 | 115 |
| Robust Packet (HF) | 7 | 7 |
| *Sum of mode rows (multi-mode stations counted more than once)* | *2,951* | *2,646* |
| **Unique RMS stations (each counted once)** | **2,115** | **1,588** |

## The animation

![Final frame of the animation: world map of Winlink RMS stations, with 1,072 VARA stations marked impacted and 516 non-VARA stations unmarked.]({{ '/images/2026/vara-rms/vara-rms-movie-final-frame.jpg' | relative_url }})
_Final frame of the 30-second animation._

The animation follows midnight on January 1, 2027 across real time zones, including summer time, from UTC+14 to UTC−12. Each VARA station is marked when its local midnight arrives. Non-VARA stations are shown in white and are not marked.

## Method and sources

The data is the Winlink Express channel lists, `RMS Channels.dat` (HF) and `RMS VHF Channels.dat` (VHF/UHF), downloaded 11 Nov 2026. They hold 4,724 channel entries, all marked public.

Modes are identified by their Winlink mode codes:

| Mode | Codes |
|---|---|
| VARA HF | 50, 53, 54 |
| VARA FM | 51, 52 |
| Packet | 0–5 |
| PACTOR | 11–20 |
| ARDOP | 40–44 |
| Robust Packet | 30 |

A station "provides VARA" if any of its channels uses a VARA mode. Private or unlisted gateways are not included. Counts reflect the public channel lists as of 11 Nov 2026 and will change as gateways come and go.

**Sources**

1. <a href="https://www.zeroretries.org/p/zero-retries-0269" target="_blank" rel="noopener noreferrer">Zero Retries 0269</a>: report of the January 1, 2027 compatibility change
2. <a href="https://downloads.winlink.org/VARA%20Products/" target="_blank" rel="noopener noreferrer">Winlink downloads: VARA Products</a>: release files dated November 4, 2026
3. <a href="https://oh8stn.org/blog/2026/11/10/vara-or-open-source-xara-what-do-you-think/" target="_blank" rel="noopener noreferrer">OH8STN: VARA or Open-Source XARA?</a>: background on earlier VARA compatibility changes
4. <a href="https://github.com/evansiroky/timezone-boundary-builder" target="_blank" rel="noopener noreferrer">timezone-boundary-builder</a>: time-zone boundaries used for the animation
