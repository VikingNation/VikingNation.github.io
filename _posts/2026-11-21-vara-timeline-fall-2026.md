---
layout: post
title: "VARA Timeline, Fall 2026"
date: 2026-11-21 18:55:00 -0500
categories: [hamradio, vara]
tags: [vara, xara, varac, winlink, nomoresecrets]
description: "Key events in the VARA space, from the release of the open-source XARA modem on October 21 to the No More Secrets specification on November 21, 2026."
---

**BLUF:** In one month an open-source VARA-compatible modem appeared and disappeared. VARA shipped an update that would break compatibility on January 1, 2027, then walked it back. An anonymous group then published the full VARA specification. This timeline collects the key events, videos and posts in one place.
{: .prompt-tip }

## XARA arrives (October 21 to November 3)

**October 21: x0rro releases XARA 0.1.0, an open-source VARA-compatible modem.** MIT-licensed, written in Rust, for Linux. It claims full compatibility with VARA HF 4.9.0 and VARA FM 4.4.0. Updates follow on October 25, 29 and 31 (0.1.1 to 0.1.3), adding macOS and FreeBSD support from community contributors.

**October 24: XARA release post on Reddit.**
[r/HamRadio: XARA, a VARA-compatible HF/VHF modem for Linux](https://www.reddit.com/r/HamRadio/comments/1xecpml/xara_a_varacompatible_hfvhf_modem_for_linux/){:target="_blank" rel="noopener noreferrer"}

**October 27: XARA comes to YouTube.** KM6LYW introduces XARA. The same day, NR5P shows it ported to iOS, Android and macOS.
- [KM6LYW Radio: Introducing XARA! VARA-Compatible Modem](https://www.youtube.com/watch?v=azalmc_KFvU){:target="_blank" rel="noopener noreferrer"}
- [NR5P: XARA ported to iOS, Android and macOS](https://www.youtube.com/watch?v=LXDKiaxk5mI){:target="_blank" rel="noopener noreferrer"}

**October 31: K3JSJ demonstrates XARA running on Windows.** A Windows port with flrig PTT and a configuration tool, tested on an IC-7300 on 40 m.
- [K3JSJ: XARA VARA HF/FM Windows demonstration](https://www.youtube.com/watch?v=JTrr5qSqTOc){:target="_blank" rel="noopener noreferrer"}
- [Blog post: Release: XARA modem and Windows port]({% post_url 2026-10-31-xara-modem-Windows %})

## The 2027 break (November 4 to 18)

**November 4: VARA developer releases VARA HF 4.9.1 and VARA FM 4.4.1.** Posted with no release notes. The HF ChangeLog says only "New changes, update all your stations to this new version." Testing later shows that from January 1, 2027 these versions no longer connect to earlier VARA versions or to XARA.
- [Winlink VARA downloads](https://downloads.winlink.org/VARA%20Products/){:target="_blank" rel="noopener noreferrer"}

**November 7: KM6LYW posts a XARA demo and deep dive.**
- [KM6LYW Radio: VARA-Compatible Modem! Demo & Deep Dive](https://www.youtube.com/watch?v=hOXPHpYweSU){:target="_blank" rel="noopener noreferrer"}

**November 8 (about 2300 UTC): x0rro shutters the XARA project.** The source code is removed and the GitHub repository is marked "discontinued". Many forks and copies survive, including NR5P/xara, finitor/xara, N4EAC's xara-for-macos and an Arch Linux package. Later come xara-streisand (from November 15) and XaraNext (mirrored November 19).
- [x0rro/xara](https://github.com/x0rro/xara){:target="_blank" rel="noopener noreferrer"} · [NR5P/xara](https://github.com/NR5P/xara){:target="_blank" rel="noopener noreferrer"} · [finitor/xara](https://github.com/finitor/xara){:target="_blank" rel="noopener noreferrer"} · [N4EAC/xara-for-macos](https://github.com/N4EAC/xara-for-macos){:target="_blank" rel="noopener noreferrer"} · [AUR xara](https://aur.archlinux.org/packages/xara){:target="_blank" rel="noopener noreferrer"} · [xara-streisand](https://github.com/Tom-Neverwinter/xara-streisand){:target="_blank" rel="noopener noreferrer"}
- [K3JSJ: XARA Discontinued!](https://www.youtube.com/watch?v=ywDRTkhIuY8){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-08-xara-project-shuttered %})

**November 8: "XARA discontinued" thread on Reddit.**
[r/amateurradio: XARA discontinued](https://www.reddit.com/r/amateurradio/comments/1xrb2ul/xara_discontinued/){:target="_blank" rel="noopener noreferrer"}

**November 8: Reddit post announces the January 1, 2027 compatibility break.**
[r/amateurradio: VARA breaks compatibility on 2027-01-01](https://www.reddit.com/r/amateurradio/comments/1xqutu9/vara_breaks_compatibility_on_20270101/){:target="_blank" rel="noopener noreferrer"}

**November 8 onward: community debate opens on VARA or open-source alternatives.** Widespread discussion on YouTube, Reddit, the Winlink Programs forum, Groups.io and other platforms about the community adopting alternative modems to VARA. Modems discussed include Mercury, Data2G, Aether and Modem73.
- [SCARCS: Mercury as a VARA alternative](https://scarcs.ca/blog/2026-11-10/mercury_vara_alternative){:target="_blank" rel="noopener noreferrer"}

**November 11: K3JSJ, "VARA Breaks 2027, Part 1".** Shows that VARA HF 4.9.1 and FM 4.4.1 stop working with earlier versions on January 1, 2027.
- [K3JSJ: VARA Breaks 2027, Part 1](https://www.youtube.com/watch?v=k6nM-s64TcI){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-11-vara-breaks-compatibility-2027 %})

**November 12: The Tech Prepper tests the break.** VARA HF 4.9.1 links with VARA 4.8.9 while the clock reads 2026, and fails once the clock is set to January 1, 2027.
- [The Tech Prepper: Will VARA 4.9.1 Break Compatibility on January 1, 2027?](https://www.youtube.com/watch?v=VMuqRQzl_2M){:target="_blank" rel="noopener noreferrer"}

**November 13: K3JSJ, "VARA Breaks 2027, Part 2", an on-air demo of what breaks.** One station upgrades, the other does not. The same night, VarAC announces a Rust port with Linux and macOS versions.
- [K3JSJ: VARA Breaks 2027, Part 2](https://www.youtube.com/watch?v=mAaGDBfwq6Y){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-13-vara-breaks-2027-part2 %})
- [K3JSJ: VarAC Rust, Linux / macOS port underway](https://www.youtube.com/watch?v=bCvaufbpjbg){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-13-varac-rust-linux-macos-port %})

**November 14: 1,072 Winlink RMS gateways offer VARA, 360 of them VARA only.**
- [K3JSJ: Map of Winlink RMS that could be impacted](https://www.youtube.com/watch?v=oXg20fUvPMs){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-14-winlink-rms-vara-exposure %})
- [Zero Retries 0269](https://www.zeroretries.org/p/zero-retries-0269){:target="_blank" rel="noopener noreferrer"} · [KE9V: Tower of Babel](https://ke9v.net/2026/11/14/babel.html){:target="_blank" rel="noopener noreferrer"}

**November 18 to 19: operators push back on upgrading.** CN86Radio reports that AmRRON, The Tech Prepper, AJ6LG and KM4ACK say they will not upgrade to 4.9.1.
- [CN86Radio: VARA HF v4.9.1 Update](https://cn86radio.substack.com/p/vara-hf-v491-update){:target="_blank" rel="noopener noreferrer"} · [CN86Radio: NO to the VARA 4.9.1 Upgrade?](https://cn86radio.substack.com/p/no-to-the-vara-491-upgrade){:target="_blank" rel="noopener noreferrer"}

## The walk-back (November 19 to 20)

**November 19: VARA HF 4.9.2 and FM 4.4.2 released "compatible with the older versions". Native macOS and Linux VARA announced.** The developer's page tells users to replace 4.9.1 and 4.4.1, and says: "We are working in a VARA multiplatform to have native macOS and Linux VARA versions available with Winlink and VarAC."
- [EA5HVK VARA page](https://rosmodem.wordpress.com/){:target="_blank" rel="noopener noreferrer"}
- [K3JSJ: Compatibility restored and macOS & Linux announcement](https://www.youtube.com/watch?v=GpE25zZVynY){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-19-vara-compatibility-restored-macos-linux %})

**November 19: featured video, "VARA WARS! Open-source and closed-source software in ham radio".** Jason (K3JSJ) highlights recent events with VARA and XARA, discusses Part 97 and how it applies to closed-source and proprietary designs, and looks at the impact the VARA / XARA fallout may have on the ham radio community.

{% include embed/youtube.html id='gnnIarbDIS8' %}

<a href="https://youtu.be/gnnIarbDIS8" target="_blank" rel="noopener noreferrer">Watch on YouTube: VARA WARS!</a> · [Blog post]({% post_url 2026-11-19-vara-wars-open-closed-source %})

**November 19 to 20: operators upgrade to 4.9.2 and report problems connecting.** In operator testing, 4.9.2 does not connect to stations running older versions, and at least one operator reports it hanging when connecting to a gateway that has not updated.
- [EtherHam Weekly Report, November 19](https://etherham.com/weekly-report-november-19-2026/){:target="_blank" rel="noopener noreferrer"} · [Random Wire 209](https://www.randomwire.us/p/random-wire-209-second-chances-for){:target="_blank" rel="noopener noreferrer"}

**November 20: VARA developer releases the fix, VARA HF 4.9.3 and FM 4.4.3.** Users are told to replace 4.9.1 and 4.9.2 with 4.9.3, and 4.4.1 and 4.4.2 with 4.4.3. Lab tests show 4.9.3 and 4.4.3 stay on the old format after January 1, 2027.
- [K3JSJ: VARA Update, HF 4.9.3 & FM 4.4.3](https://www.youtube.com/watch?v=vbowhcR_EuQ){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-20-vara-hf-493-fm-443-release %})
- [N2EC: Amateur Radio News and Notes](https://mvarc.substack.com/p/amateur-radio-news-and-notes-11202026){:target="_blank" rel="noopener noreferrer"}

## No More Secrets (November 21)

**November 21: "No More Secrets" publishes the full VARA specification.** An anonymous group releases four PDFs: the VARA HF and FM Air Interface and Host Network Interface specifications, in English and Spanish. They cover modulation, coding, interleavers, the link protocol and the 2027 waveform, and say they are independent work, not affiliated with VARA's author.
- [VARA-MODEM groups.io thread](https://groups.io/g/VARA-MODEM/topic/complete_documentation_of/122380838){:target="_blank" rel="noopener noreferrer"}
- [K3JSJ: No More Secrets, the VARA mystery continues](https://www.youtube.com/watch?v=wX48lt14xr8){:target="_blank" rel="noopener noreferrer"} · [Blog post]({% post_url 2026-11-21-no-more-secrets-vara-mystery %})
- [Zero Retries 0270](https://www.zeroretries.org/p/zero-retries-0270){:target="_blank" rel="noopener noreferrer"}

**November 21: No More Secrets suggests "prohibited" callsigns.** The No More Secrets group posted on VARA Modem (HF and FM) suggesting that the updated VARA modem software contains a list of prohibited operators who must contact the developer.
- [VARA-MODEM groups.io thread](https://groups.io/g/VARA-MODEM/topic/complete_documentation_of/122380838){:target="_blank" rel="noopener noreferrer"}

**ALLEGED.** This claim is not confirmed as of November 21, 2026.
{: .prompt-warning }

## Notes

Video dates are YouTube upload dates. VARA release dates come from the Winlink download listing and the developer's page. Reddit post dates are confirmed by K3JSJ.

Subscribe to the <a href="https://www.youtube.com/@K3JSJ" target="_blank" rel="noopener noreferrer">"Ham Radio Community" YouTube channel</a> for continued coverage.

Jason, K3JSJ
