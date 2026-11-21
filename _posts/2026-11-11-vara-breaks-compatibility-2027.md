---
layout: post
title: "VARA developer breaks compatibility 1/1/2027"
date: 2026-11-11
categories: [hamradio, vara]
tags: [vara, winlink]
description: "VARA HF 4.9.1 and VARA FM 4.4.1 were released on November 4, 2026 with no information. On January 1, 2027 the modems will no longer work with past revisions unless users upgrade."
image:
  path: /images/2026/vara-breaks-compatibility-2027/vara-breaks-compatibility-2027.png
  alt: "\"VARA Breaks! 2027\" video thumbnail: a Winlink map of North America with many RMS stations marked with red X's."
---

**BLUF:** On **November 4, 2026**, VARA HF (4.9.1) and VARA FM (4.4.1) were released with no information about what changed. The VARA HF/FM modems currently work with past revisions, but on **January 1, 2027** the modem will no longer work with past revisions unless users upgrade. There is speculation this release has to do with the open source release of the XARA Modem.
{: .prompt-warning }

I covered this topic in a YouTube video:

{% include embed/youtube.html id='k6nM-s64TcI' %}

<a href="https://youtu.be/k6nM-s64TcI" target="_blank" rel="noopener noreferrer">Watch on YouTube: VARA breaks compatibility on January 1, 2027</a>

Here is a full analysis of past times when VARA releases broke compatibility.

## VARA past compatibility breaks: timelines and sources

This section covers every documented case where José Alberto Nieto Ros, EA5HVK, released a VARA version that would no longer connect to the previous one. For each case it gives when the change was announced, when it shipped, and when the break actually took effect.

- **Research date:** 11 Nov 2026
- **Products:** VARA HF · VARA FM · VARA SAT
- **Confidence key:** *Confirmed* = dated primary source · *Second-hand* = dated report quoting EA5HVK / Winlink · *Unverified* = flagged as such

| Figure | What it means |
|---|---|
| **5** | Documented, dated compatibility breaks, plus narrower KISS / VarAC-only breaks |
| **40 days** | Lead time for the textbook case: HF 4.0 announced 21 May 2020, cut-over 30 June 2020, installer time-locked |
| **~0–1 day** | Warning for FM 4.01: released 28 Nov 2020 with no central cut-over ("managed locally") |
| **6 months** | EA5HVK's stated minimum notice for a "critical" update, relayed 22 Mar 2023 |

**The pattern is not a one-off.** The breaks repeat across HF, FM and SAT from 2019 to 2024, but the handling varies sharply: a network-wide, time-locked cut-over (HF 4.0), a same-day release with local cut-overs (FM 4.01), and a staged two-step migration with "transitional" bridge releases (the 2021 32-bit hash change). The 4 Nov 2026 releases (HF 4.9.1 / FM 4.4.1) were **not** announced as breaking or transitional, and no changelog explanation was found.
{: .prompt-info }

## At a glance: every break on one timeline

The cut-over / effective date comes first. "Announced" is when users and sysops were first told.

| Effective date | Break | Details | Confidence |
|---|---|---|---|
| Jul 2019 (beta, no cut-over set) | VARA HF 3.0 (beta) vs 2.2.1 | Announced 9 Jul 2019 on the Winlink blog; WDT promised a future switchover date after testing | Confirmed |
| 30 Jun 2020 (announced 21 May 2020) | VARA HF 4.0 vs VARA 3 (and VARA 2) | 40 days' lead; installer would not install/use until 30 June; full Winlink RMS network cut-over | Confirmed |
| 28 Nov 2020, 1700 UTC (same day) | VARA FM 4.01 vs FM 3.x | No central cut-over ("managed locally"); ARES LAX / Ventura ACS picked 4 Dec 2020 | Confirmed |
| Mar–Aug 2021 (staged, 2 steps) | 32-bit callsign hash: HF 4.4.3 · SAT 4.1.0 · FM 4.1.3 | Bridge releases first (HF 4.4.0 / 4.4.2, FM 4.1.2), then breaking releases; SAT cut-over 4 Apr 2021; HF 16-bit support finally removed in 4.4.5 on 3 Aug 2021 | Confirmed |
| 1 Jan 2024 (KISS scope) | VARA HF 4.8.1: new KISS TCP interface | Changelog: "not longer compatible with old versions"; KISS/APRS scope as worded, not stated as a Winlink ARQ break | Confirmed, narrow |
| 2 Jan 2024 (VarAC scope) | VarAC broadcasts / pathfinder / relay: HF 4.8.1 · FM 4.3.2 · SAT 4.4.0 | Each version can only decode same-version broadcasts; normal Winlink / VarAC QSO sessions not stated to be affected | Confirmed, narrow |
| 4 Nov 2026 (for context) | VARA HF 4.9.1 / FM 4.4.1 | Not announced as breaking or transitional; Zero Retries notes no change information on any official download page or changelog | Not announced as a break |

## EA5HVK's stated policy on critical updates

This was relayed by Scott Currie, NS7C, on 22 Mar 2023, quoting José. It is the benchmark to measure the lead times below against.

> "When an update is critical for the future the automatic notification is activated. There is a period of 6 months minimum to give time to sysops to update it. When the update is not critical the automatic notification is not activated."

*Second-hand, quoting José.* Source: [VARA-MODEM, 22 Mar 2023](https://groups.io/g/VARA-MODEM/message/5600)

## The breaks, case by case

Each case shows the same three dates: **announced → released → break took effect**, plus lead time, technical change, Winlink coordination, and source URLs.

### 1 · VARA HF 3.0 beta vs 2.2.1 (July 2019)

**Confirmed** · NEW: VARA HF 3.0 beta (3.0.2 in use) ✕ OLD: VARA 2.2.1

This is the earliest documented break. It was a beta, not a cut-over: test stations ran both versions in parallel, and Winlink promised to set a switchover date later.

| Announced | Released | Break took effect |
|---|---|---|
| **9 July 2019**: Winlink blog, N6KZB: "Jose sent a note this morning telling us that he has a new version of Vara HF available for testing!" | **9 July 2019, beta only**: available for testing by WDT beta stations (XE2BNC, XE1CRG, N5TW); 3.0.2 in use by 21 July 2019 | **No cut-over date set**: "After we get some testing under our belts for a few weeks and assuming it is successful, WDT will post a date for a switchover…" No follow-up was located; HF 4.0 superseded it in 2020. |

- **Lead time:** none (beta only)
- **Installer lock:** none
- N5TW ran 3.0 and 2.2.1 in parallel on different setups / frequencies.
- **What changed technically:** sensitivity in poor conditions. "Vara 2.2.1 was very fast in good conditions but not so sensitive in poor ones and this new version is to address that." No protocol detail was given.
- **Winlink coordination:** yes. The Winlink Development Team (WDT) ran the beta and promised a future switchover date.

**Sources**
- Winlink blog, 9 Jul 2019: <https://www.winlink.org/node/1161>
- VE7RBH blog, 21 Jul 2019: <https://www.winlink.org/blogs/ve7rbh?page=4> ("now using VARA 3.0.2 which is not compatible with earlier VARA versions")

### 2 · VARA HF 4.0 vs VARA 3 (cut-over 30 June 2020)

**Confirmed · lead case** · NEW: VARA HF 4.0 ✕ OLD: VARA 3 and VARA 2

This is the textbook case: a single network-wide cut-over date, announced in advance, with the installer deliberately time-locked so no one could switch early.

| Announced | Released | Break took effect (cut-over) |
|---|---|---|
| **21 May 2020**: Winlink announcement. Caveat: winlink.org's tag page shows no publication date; 21 May comes from the dated groups.io mirror of the same text. The 40-day lead depends on that date. | **Available early** from rosmodem.wordpress.com, downloadable before 30 June (but see the lock). | **30 June 2020**: "ON JUNE 30, 2020, Winlink VARA HF RMS stations will switch to use VARA HF 4.0." "RMS running VARA HF 4.0 will not communicate with VARA 3-equipped clients." |

- **Lead time:** 40 days (21 May → 30 June)
- **Installer locked / time-gated:** yes, explicitly

> "To avoid early incompatibilities this package will not allow installation and use until June 30. This delay is to allow critical information to flow about the upcoming breaking change, and to allow users who intend to be offline on the cutover date to download it now for installation on or after June 30."

- **What changed technically:** "Major upgrade that offers additional speed, robustness and utility, including a new robust 500 Hz narrow bandwidth mode." No handshake / protocol detail was in the announcement. Slide decks from the time said: "The current version of VARA HF is not backward compatible with VARA 2 and VARA 3."
- **Winlink coordination:** full network cut-over. RMS operators were told to put the cut-over notice in a `BANNER.txt` file in Trimode / other RMS apps. Winlink Express could already use the new version.

**Sources**
- Winlink VARA tag page: <https://winlink.org/tags/vara>
- Dated mirror of the Winlink announcement, 21 May 2020: <https://w6ek.groups.io/g/SFARC/message/6090>
- Early download: <https://rosmodem.wordpress.com>

### 3 · VARA FM 4.01 vs FM 3.x (28 November 2020)

**Confirmed** · NEW: VARA FM 4.01 ✕ OLD: all previous FM, incl. 3.1.x / 3.1.1

This was handled the opposite way from HF 4.0: the announcement and the release happened at the same moment, and there was deliberately *no* central cut-over date. It was announced in advance as "VARA FM 4.0", but the file actually posted was numbered 4.01.

| Announced | Released | Break took effect |
|---|---|---|
| **28 Nov 2020, 1700 UTC**: "Jose Alberto Nieto Ros EA5HVK has released VARA FM version 4.01 as of 1700UTC November 28, 2020." A 27 Nov post said "VARA FM 4.0 will be released tomorrow", about 1 day's warning. | **28 Nov 2020**, the same moment as the announcement. No advance notice and no time-gate. Users at the time contrasted this with HF 4.0's "plenty of advanced notice… with a heavily publicized scheduled full implementation date." | **No central date ("managed locally")**: Winlink and EA5HVK "decided against a set cutover date for all" (K6OLI, 29 Nov 2020). Local dates: ARES LAX & Ventura ACS **4 Dec 2020**; W7PLC-10 upgraded 3 Dec 2020; W6RH upgraded his gateway 7 Dec 2020. |

- **Lead time:** none documented (~1 day's warning)
- **Installer lock:** none
- Clients that upgraded first could no longer use a V3 gateway, and vice versa.
- **What changed technically:** digipeater capability (up to 2 digipeaters), a lower data-rate speed level for weak signals, improvements for cheap HTs and voice repeaters, callsign display, and a new Ping feature (VU + S/N). No protocol / handshake detail was given.
- **Winlink coordination:** Winlink announced it, but coordination was deliberately local, not network-wide. Gateway sysops upgraded individually.

**Sources**
- Winlink, VARA FM 4.01 released: <https://winlink.org/content/vara_fm_version_401_released>
- Gateway still on V3.1.1, rollout question, 28 Nov 2020: <https://groups.io/g/Winlink/message/1111>
- K6OLI reply re 4 Dec local cut-over, 29 Nov 2020: <https://groups.io/g/Winlink/messages?msgnum=1100>
- W7PLC-10 upgrade, 3 Dec 2020: <https://winlink.org/content/upgrade_vara_fm_401_w7plc_10>
- "New VARA FM v4.0.1", 29 Nov 2020: <https://digitalradio.groups.io/g/main/message/51398>

### 4 · The 2021 32-bit hash transition (HF, SAT & FM)

**Confirmed · one break, three products** · 16-bit hash ✕ 32-bit hash: "IS INCOMPATIBLE … and the reverse"

This was one technical break: the callsign hash grew from 16-bit to 32-bit. It was rolled out in **two stages per product**, with explicit "transitional" bridge releases that understood both. The cause: John Wiseman (G8BPQ) found a case where the 16-bit hash resolved the wrong callsign (1-in-6553 error rate). Stage 1 put sysops on the bridge version "for about 2 months". Stage 2 was the breaking release.

**Shared sources**
- EA5HVK changelog (via VARA-MODEM attachment): <https://groups.io/g/VARA-MODEM/attachment/7213/2/ChangeLog-28-02-2024.txt>
- SPARKS, Mar 2021, Stage 1 / Stage 2 explanation (PDF): <http://w9og.net/attachments/article/291/2021-03-Sparks.pdf>

#### 4a · VARA HF: 4.4.0 → 4.4.2 → 4.4.3 → 4.4.5

**Transitional → breaking** · BRIDGE: HF 4.4.0 / 4.4.2 → BREAKING: HF 4.4.3 ✕ anything before 4.4.2

| Transitional | Bridge | Breaking release |
|---|---|---|
| **4.4.0, 26 Feb 2021**: "Compatibility with future changes in the next VARA version. Necessary sysops update this v4.4.0 as soon as be possible, before releasing the next VARA version with important innovations." | **4.4.2, 19 Mar 2021**: "This version ensures compatibility with the changes projected in the future v4.4.3… It's very important all the sysops run VARA HF v4.4.2 in order to VARA HF v4.4.3 can be released for all the users." Announced 21 Mar 2021. | **4.4.3, 10 Apr 2021**: the first version to *initiate* connections with the 32-bit hash. It also added VARA Compression (registered users only, ~2× faster at Speed Level 1). There was no single network cut-over date; the rollout was staged. |

- **Final removal:** HF 4.4.5, 3 Aug 2021: "compatibility with old 16-bit hash versions have been definitevely [sic] removed"
- **Who was cut off:** "Users still running code before version 4.4.2 will not be able to receive station calls from users running version 4.4.3… Peer to Peer or Trimode/BPQ stations MUST be on at least 4.4.2 to continue to function."
- **Winlink coordination:** sysop-first rollout. Trimode/BPQ gateways had to be on the bridge version before clients migrated, and Winlink Express needed the compression-command fix in 4.4.2. No winlink.org network cut-over announcement was found.

**Sources**
- HF 4.4.2 bridge announcement, 21 Mar 2021: <https://groups.io/g/VARA-MODEM/message/1409>
- OHD3 ARES, HF 4.4.3, Apr 2021: <https://ohd3ares.org/wp/?page_id=4964>
- NM5PB gateway, HF 4.4.3 Stage 2: <https://www.nm5pb.com/hf-rms-gateway-vara-updated-to-4-4-3-stage-2/>
- Changelog (4.4.0–4.4.5): <https://groups.io/g/VARA-MODEM/attachment/7213/2/ChangeLog-28-02-2024.txt>

#### 4b · VARA SAT 4.1.0 (cut-over 4 April 2021)

**Confirmed · dated cut-over** · NEW: VARA SAT 4.1.0 ✕ OLD: VARA SAT 4.0.2

This is the cleanest small-network example: users could download the new version immediately but kept using the old one until the single gateway switched.

| Announced | Released | Break took effect (cut-over) |
|---|---|---|
| **19 Mar 2021**: José EA5HVK, forwarded 20 Mar 2021. The changelog date for 4.1.0 is also 19 Mar 2021. | **19 Mar 2021, download now, don't switch yet**: users were told to *save the setup file and keep using 4.0.2* until the cut-over. | **4 Apr 2021**: "It will be operative on IS0GRB since April 4… After April 4th, the v4.0.2 will not longer be compatible." IS0GRB was the SAT gateway. |

- **Lead time:** 16 days (19 Mar → 4 Apr)
- **What changed technically:** Huffman compression (registered users only, faster Winlink throughput at slow levels 1–5), 32-bit hash, less latency at high speed levels, a BREAK-loop fix, and a Swap RX Channels option.

**Sources**
- VARA-MODEM, SAT 4.1.0 announcement: <https://groups.io/g/VARA-MODEM/message/1408>

#### 4c · VARA FM: transitional 4.1.2 → breaking 4.1.3 (July 2021)

**Confirmed · one date gap** · BRIDGE: FM 4.1.2 → BREAKING: FM 4.1.3 ✕ FM 4.1.1 and older

| Transitional | Breaking release | Later confirmation |
|---|---|---|
| **FM 4.1.2, on the download site ~16 May 2021**: reported 19 May 2021; replaced 4.0.5. A gateway sysop (17 May 2021) called it "a transitional version with the mission of moving to a 32 bit hash for call sign" and "backwards compatible by one version." W7OWO tested it and found **no issues** with v4.0.5 as server or client, wide and narrow, VHF and UHF. In practice, 4.1.2 did *not* break compatibility. | **FM 4.1.3, gateway upgrade reported 22 July 2021**: "This an all 32 bit hash (password protection system) that is not compatible in any way with 4.1.1. 4.1.2 will connect but…" **Date gap:** the exact release date of 4.1.3 was not verified; 22 July is when a gateway upgraded to it. | **1 Aug 2021, José via Graham G0NBD**: "These VARA FM stations and repeaters are not compatible with new VARA FM versions. I would recommend update to a new VARA FM version as soon as be possible to accept new connections." |

- **Cut-over:** no central date; gateway by gateway, July 2021

**Sources**
- FM 4.1.2 transitional, 17 May 2021: <https://groups.io/g/gaares/topic/kx4mat_10_fm_vara_rms_gateway/82883763>
- FM 4.1.2 vs 4.0.5 test, 19 May 2021: <https://groups.io/g/VARA-MODEM/topic/82946618>
- FM 4.1.3 gateway upgrade, 22 July 2021: <https://groups.io/g/gaares/message/272>
- José on FM stations / repeaters, 1 Aug 2021: <https://groups.io/g/VARA-MODEM/messages?expanded=1&msgnum=1938>

### 5a · VARA HF 4.8.1: new KISS TCP interface (1 January 2024)

**Confirmed · KISS scope** · NEW: VARA HF 4.8.1 KISS ✕ OLD: previous KISS versions

> "v4.8.1 (01/01/2024) A new KISS TCP implementation supports 2+8 call signs. This new KISS interface is not longer compatible with old versions. Update as soon as possible."

- **Scope (read carefully):** as worded, this covers the KISS TCP interface only (APRS, VarAC broadcasts, etc.). The changelog does *not* say Winlink ARQ sessions broke, and no Winlink cut-over announcement was found.
- **Related transitional release:** HF 4.7.6 is described as "compatible with future changes". The changelog also lists a RETRIES command for a new Winlink Express feature. **There is a date discrepancy, so don't treat this as firm:** the Feb 2024 changelog dates 4.7.6 as 08/06/2023, while a Mar 2023 post quotes it as 10/03/2023. No later break that 4.7.6 was preparing for was identified; the 4.8.1 changelog floor is 4.7.3, not 4.7.6.

**Sources**
- EA5HVK HF changelog to 28 Feb 2024: <https://groups.io/g/VARA-MODEM/attachment/7213/2/ChangeLog-28-02-2024.txt>
- 4.7.6 date discrepancy post, Mar 2023: <https://groups.io/g/VARA-MODEM/messages?expanded=1&msgnum=5512>

### 5b · VarAC broadcasts / pathfinder / relay notifications (2 January 2024)

**Confirmed · VarAC scope only** · HF 4.8.1 · FM 4.3.2 · SAT 4.4.0 ✕ older broadcasts only

This was announced by Irad Deutsch, 4Z1AC (the VarAC author), and forwarded to TARA on 2 Jan 2024.

> "A new VARA-HF V4.8.1 was recently released along with new versions also for VARA-FM and VARA-SAT. THESE VERSIONS ARE NOT COMPATIBLE WITH OLDER VERSIONS OF VARA MODEMS WHEN IT COMES TO VARAC BROADCASTS, PATHFINDER AND RELAY NOTIFICATIONS. In other words — VARA-HF V4.8.1 can only decode V4.8.1 broadcasts / pathfinders and relay notifications."

The announcement names companion versions **VARA FM 4.3.2 and VARA SAT 4.4.0**, but their release dates were not independently verified. Normal Winlink / VarAC QSO sessions are not stated to be affected; only broadcasts are.

**Sources**
- TARA, VarAC broadcast break, 2 Jan 2024: <https://groups.io/g/TARA-n7tar/message/325>
- Also: a KISS header change required HF 4.6.6 / FM 4.2.6 for VarAC V6.3.3, 24 Nov 2022 (inferred, VarAC scope only): <https://www.varac-hamradio.com/varac-releases>. No VARA changelog statement calling 4.6.6 / 4.2.6 incompatible was found, and the Feb 2024 HF changelog jumps from 4.6.5 to 4.6.8 without listing 4.6.6.

### Context · the 4 Nov 2026 releases were not announced as a break

**Not announced as breaking** · HF 4.9.1 · FM 4.4.1, released 4 Nov 2026

This is included so the past pattern isn't misread onto the current release. As of 11 Nov 2026, public web sources don't show whether 4.9.1 / 4.4.1 are breaking or transitional.

- **What shipped:** on **4 Nov 2026, ~13:11–13:12** (downloads.winlink.org timestamps): VARA HF v4.9.1, VARA FM v4.4.1, VARA Chat v1.4.3, VARA Terminal v1.2.2. VARA SAT v4.4.5 (7 Jan 2026) was unchanged. The previous versions were HF 4.9.0 (7 Jan 2026) and FM 4.4.0 (31 Jan 2026). Chat 1.4.3 (14 Feb 2026) and Terminal 1.2.2 (12 Sep 2025) kept *the same version numbers as before*; they were only re-uploaded on 4 Nov.
- **What was (not) said:** Zero Retries 0268 (Steve Stroh, N8GNJ): "There's no information provided on what has changed in these newer versions on any of the 'official' VARA download pages — downloads.winlink.org, varamodem.com, and rosmodem.wordpress.com. Nor, reportedly, is there any explanation in the changelogs of each changed app." The "minor, maintenance release" wording that appears elsewhere is VA3CJO's speculation, not a developer statement. No compatibility warning was found in the VARA-MODEM thread or in searches for "VARA HF 4.9.1 changelog / not compatible / transitional."

**Sources**
- Downloads listing: <https://downloads.winlink.org/VARA%20Products/>
- Zero Retries 0268 (VARA section): <https://www.zeroretries.org/p/zero-retries-0268>
- VARA-MODEM thread, 5 Nov 2026 (mainly install / antivirus discussion): <https://groups.io/g/VARA-MODEM/topics?threadid=96735209>

## Rumored but not confirmed

Each of these was claimed somewhere, but the research found no confirming primary source, or the sources directly conflict.

| Case | Why it is not confirmed | Source |
|---|---|---|
| **VARA HF 4.4.4**: "Winlink is sitting on 4.4.4 as its not backwards compatible" (Jul 2021) | A single second-hand groups.io comment, 11 July 2021. No release note, changelog entry or Winlink announcement was found. It may have been a held / unreleased Winlink-only build. | [VARA-MODEM #1811](https://groups.io/g/VARA-MODEM/message/1811) |
| **VARA FM 4.1.8 vs 4.2.8**: a user could not connect (Mar 2023) | One user report: an FM 4.1.8 client failed sessions to a 4.2.8 gateway while ping/autotune worked, and updating fixed it. The reporter notes the changelogs back to 4.1.8 don't mention backward compatibility, and there is no developer confirmation. It could be an undocumented break or a misdiagnosis. | [VARA-MODEM #5589](https://groups.io/g/VARA-MODEM/message/5589) · policy reply: [#5600](https://groups.io/g/VARA-MODEM/message/5600) |
| **VARA FM 4.1.2** "is not backward compatible" (claimed 2023) | Wes WB7BR (Mar 2023) said the FM changelog notes it, but W7OWO's May 2021 test at the time found 4.1.2 worked with 4.0.5 both ways. The likeliest reading: 4.1.2 was transitional, and any such note refers to the 4.1.3 step. | [VARA-MODEM #5593](https://groups.io/g/VARA-MODEM/messages?page=111&after=1679597679940182469&subsort=1) vs [topic/82946618](https://groups.io/g/VARA-MODEM/topic/82946618) |
| **VARA HF 4.8.3 vs 4.8.2** (Feb 2024), conflicting | The changelog says 4.8.3 (7 Feb 2024) is "Compatible with v4.7.3 or newer." Isaac W7BSB (8 Feb 2024, APRS-beacon thread) said "4.8.3 is not backwards compatible with 4.8.2," and Wes WB7BR replied that the changelog says otherwise. The context was APRS/KISS beacons, not Winlink sessions. Later entries (4.8.5, 24 Feb 2024: "New KISS frame format…") suggest the KISS format was still changing. | [HF changelog](https://groups.io/g/VARA-MODEM/attachment/7213/2/ChangeLog-28-02-2024.txt) · [VARA-MODEM #6999](https://groups.io/g/VARA-MODEM/messages?msgnum=6999) |
| **VARA FM 3.0.5 vs FM 1.3.0** | A Mar 2020 setup guide states "VARA FM 3.0.5 and higher are not compatible with VARA FM 1.3.0 or lower", but the release date of FM 3.0.5 and any announcement were not found. The guide's last-update date (9 Mar 2020) only proves the break existed by then. | [Delco ARES guide (PDF)](https://www.delcoares.org/download/attachments/301031225/vara_fm_for_winlink_with_signalink_on_windows_v4_0.pdf?api=v2) |
| **Any 2025–2026 break before 4 Nov 2026** | No incompatible version was found for 2025–2026 in searches of winlink.org, VARA-MODEM, Zero Retries and the changelogs. The Feb 2024 changelog is the latest full changelog located; later changelogs live inside the installers and were not retrievable. Absence of evidence is not proof of absence. | — |

## Open questions: what could not be verified

- **Winlink.org publication date for the HF 4.0 announcement:** the tag page shows no date; 21 May 2020 comes from the groups.io mirror. The 40-day lead time depends on it.
- **Exact release date of VARA FM 4.1.3:** only the 22 July 2021 gateway upgrade is dated; the release itself may be days earlier.
- **Exact release dates of VARA FM 4.3.2 and VARA SAT 4.4.0** (named in the 2 Jan 2024 VarAC announcement) were not independently verified.
- **VARA FM 3.0.5 release date** and any announcement were not found.
- **What, if anything, changed in HF 4.9.1 / FM 4.4.1 (4 Nov 2026):** no changelog or developer note was found; the changelogs are inside the installers.
- **Whether a switchover date was ever set for HF 3.0** after the July 2019 beta: one was promised "after a few weeks", but no follow-up was located.
- **rosmodem.wordpress.com**, as crawled 16 Oct 2026, lists only old posts and no usable dated release announcements for these versions. Release notes live in the installers' Help → Changelog, which is why the Feb 2024 changelog attachment on groups.io is the best changelog source found. Zero Retries 0268 says **varamodem.com** carried no change information for Nov 2026; this research did not check it separately.

## All sources

- <https://winlink.org/tags/vara>: Winlink VARA tag page (FM 4.01 + HF 4.0 announcements)
- <https://winlink.org/content/vara_fm_version_401_released>: Winlink, FM 4.01
- <https://w6ek.groups.io/g/SFARC/message/6090>: HF 4.0 announcement, 21 May 2020
- <https://www.winlink.org/node/1161>: HF 3.0 beta, 9 Jul 2019
- <https://www.winlink.org/blogs/ve7rbh?page=4>: VARA 3.0.2, 21 Jul 2019
- <https://groups.io/g/VARA-MODEM/attachment/7213/2/ChangeLog-28-02-2024.txt>: EA5HVK HF changelog to 28 Feb 2024
- <https://groups.io/g/VARA-MODEM/message/1409>: HF 4.4.2 bridge, 21 Mar 2021
- <https://groups.io/g/VARA-MODEM/message/1408>: SAT 4.1.0, cut-over 4 Apr 2021
- <http://w9og.net/attachments/article/291/2021-03-Sparks.pdf>: SPARKS, Mar 2021
- <https://ohd3ares.org/wp/?page_id=4964>: OHD3 ARES, HF 4.4.3
- <https://www.nm5pb.com/hf-rms-gateway-vara-updated-to-4-4-3-stage-2/>: NM5PB, HF 4.4.3 Stage 2
- <https://groups.io/g/gaares/topic/kx4mat_10_fm_vara_rms_gateway/82883763>: FM 4.1.2, 17 May 2021
- <https://groups.io/g/VARA-MODEM/topic/82946618>: FM 4.1.2 test, 19 May 2021
- <https://groups.io/g/gaares/message/272>: FM 4.1.3, 22 Jul 2021
- <https://groups.io/g/VARA-MODEM/messages?expanded=1&msgnum=1938>: José, 1 Aug 2021
- <https://groups.io/g/VARA-MODEM/message/1811>: HF 4.4.4 held, 11 Jul 2021
- <https://groups.io/g/Winlink/message/1111>: FM V4 rollout, 28 Nov 2020
- <https://groups.io/g/Winlink/messages?msgnum=1100>: FM local cut-over 4 Dec 2020
- <https://winlink.org/content/upgrade_vara_fm_401_w7plc_10>: W7PLC-10, 3 Dec 2020
- <https://digitalradio.groups.io/g/main/message/51398>: FM v4.0.1, 29 Nov 2020
- <https://groups.io/g/VARA-MODEM/message/5589>: FM 4.1.8 vs 4.2.8, 19 Mar 2023
- <https://groups.io/g/VARA-MODEM/message/5600>: 6-month policy, 22 Mar 2023
- <https://groups.io/g/VARA-MODEM/messages?msgnum=6999>: HF 4.8.3 dispute, 8 Feb 2024
- <https://groups.io/g/TARA-n7tar/message/325>: VarAC break, 2 Jan 2024
- <https://www.varac-hamradio.com/varac-releases>: VarAC V6.3.3 KISS header
- <https://www.delcoares.org/download/attachments/301031225/vara_fm_for_winlink_with_signalink_on_windows_v4_0.pdf?api=v2>: FM 3.0.5 note
- <https://downloads.winlink.org/VARA%20Products/>: 4 Nov 2026 files
- <https://www.zeroretries.org/p/zero-retries-0268>: Zero Retries 0268
- <https://groups.io/g/VARA-MODEM/topics?threadid=96735209>: Nov 2026 thread
- <https://rosmodem.wordpress.com/>: EA5HVK blog (no dated announcements found for these versions)

*Research snapshot: 11 Nov 2026. Dates and quotes are as given in the sources linked in each case; where a date rests on a mirror, a gateway report, or a conflicting changelog, the case says so. "Confirmed" means a dated primary source (winlink.org, EA5HVK's changelog as republished on VARA-MODEM, or a dated groups.io post by EA5HVK) was found. It does not mean the software behavior was re-tested.*
