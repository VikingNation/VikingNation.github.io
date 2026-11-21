---
layout: post
title: "Mercury and VarAC testing, part 1: where the link stops working"
date: 2026-11-17
categories: [hamradio, vara]
tags: [mercury, varac, vara, hf, digital-modes]
description: "I ran VarAC with two Mercury HF modems on an audio loopback bench, adding fixed noise and lowering the signal until the link failed. Mercury connected down to about -11 to -13 dB SNR in 2.5 kHz. The tests also found four problems worth fixing."
image:
  path: /images/2026/mercury-varac-testing/mercury-snr-vs-rate.png
  alt: "Chart of Mercury data speed against measured SNR for both directions of a loopback test, from 321 BPS at high SNR down to no connection below about -13 dB."
---

**BLUF:** On an audio loopback bench, VarAC and the [Mercury HF modem](https://github.com/Rhizomatica/mercury) worked together. Mercury **connected down to about -11 to -13 dB SNR** (measured in 2.5 kHz) and was **practical down to about -4 to -6 dB**, with no lost frames and about 30 seconds per short message. Below about -13 dB the call was not heard at all. The tests also turned up four problems: data dropped at disconnect but reported as sent, stray null bytes, data carried into the next QSO, and an odd choice of speed.
{: .prompt-info }

Two days ago I released the beta of [Mercury Ascending]({{ '/software/mercury-ascending' | relative_url }}), a tool that sets up Mercury to work with VarAC. This post covers the first round of testing.

- **Software:** VarAC with Mercury, set up with Mercury Ascending; VARA HF for the on-air comparison
- **Bench:** two Mercury instances on one Windows PC, linked through VB-Audio Voicemeeter
- **Test date:** 17 Nov 2026

## Why a loopback bench

My first on-air attempts with Mercury didn't connect. The same VarAC setup with VARA HF did. I captured the TCP traffic between VarAC and the modem in both cases: the command port (8300), the data port (8301) and the KISS port (8100).

- **With VARA**, the modem reported `CONNECTED` about 8 seconds after VarAC's `CONNECT`, and the chat ran normally.
- **With Mercury**, the modem accepted every setup command and the `CONNECT`, then sent calls at speed 16 (30 BPS) and later long 27-second calls at speed 103 (31 BPS). It never reported an `SN` or `CONNECTED`.

That pattern fits Mercury not hearing the other station at all. It could also have been a VarAC-Mercury interface problem. To separate the two, I needed a test where I control both ends and the noise.

## The bench

- **Two stations on one PC:** K3JSJ on TCP ports 8300/8301/8100, and K3BWA on 8400/8401/8101. K3JSJ called K3BWA in every test.
- **Audio:** each modem's transmit audio goes to its own Voicemeeter strip and from there to the other modem's receive bus.
- **Noise:** a white Gaussian noise generator on a third strip, mixed into both receive buses at a fixed level.
- **Signal level:** only the two modem strip faders were moved, both by the same amount, so lowering them lowers the SNR.
- **Logging:** a packet capture of all six TCP ports for every test, decoded into a timeline of what VarAC and the modems said to each other.

The first loopback test settled the interface question. K3JSJ connected to K3BWA first time, both modems reported `CONNECTED K3JSJ K3BWA 500`, and chat went both ways. **VarAC and Mercury work together. The on-air failure was a radio-path or far-station problem.**

## Measuring the real SNR

A fader setting is not an SNR. "-24 dB" on the fader means 24 dB below the modem's normal output, not 24 dB below the noise. So I wrote a small script that records each modem's receive bus and compares the spectrum during transmissions with the spectrum in the gaps. That gives the signal level, the noise level, and the SNR in 2.5 kHz, in 500 Hz, and in the band Mercury actually occupies.

With the faders at 0 dB:

| | K3JSJ → K3BWA | K3BWA → K3JSJ |
|---|---:|---:|
| Mercury signal at the receiving bus | -17.1 dBFS | -17.4 dBFS |
| Noise at the receiving bus | -35.0 dBFS | -34.9 dBFS |
| SNR in 2.5 kHz | 26.5 dB | 24.9 dB |
| SNR in 500 Hz | 37.0 dB | 35.6 dB |

Mercury's signal is centred on 1506 Hz, and 99% of its power falls within about 670-740 Hz. Since Voicemeeter mixes in floating point, the SNR at any fader setting is the SNR at 0 dB plus the fader value.

**One setup gotcha:** I set the noise generator to -30 dBFS, but it arrived at the buses at -35 dBFS. The cause was the Windows playback volume in `mmsys.cpl`, which was 94% on all three Voicemeeter inputs. Because the noise and both modems were turned down by the same amount, the SNR was unaffected. If you build a bench like this, measure what actually reaches the receiving modem instead of trusting the generator setting.
{: .prompt-tip }

## The sweep

![Mercury data speed versus measured SNR in 2.5 kHz, for both directions. 321 BPS down to about +3 dB, 68 and 87 BPS around +1 to +2 dB, 31 BPS from about -4 to -13 dB, and no connection below about -13 dB.]({{ '/images/2026/mercury-varac-testing/mercury-snr-vs-rate.svg' | relative_url }})

Each marker is the data speed Mercury used in one test, for one direction. SNR is in 2.5 kHz. Add about 10.5 dB for a 500 Hz figure.

| Faders | SNR K3JSJ→K3BWA | SNR K3BWA→K3JSJ | Mercury's `SN` | Data speed | Result |
|---:|---:|---:|---:|---|---|
| -3.1 dB | +23.4 | +21.8 | 16.3 | 321 BPS | Good |
| -15.1 dB | +11.4 | +9.8 | 7.5 | 321 BPS | Works; 2 missed frames resent; 2 messages lost at disconnect |
| -18.2 dB | +8.3 | +6.7 | 4.2 | 321 BPS | Works; up to 37 s per message |
| -21.2 dB | +5.3 | +3.7 | 4.1 | 321 BPS | Works, no losses |
| -24.4 dB | +2.1 | +0.5 | 0.5 | 68/87 BPS, and back up to 321 one way | 19 of 19 messages |
| **-30.6 dB** | **-4.1** | **-5.7** | -5.3 | 31 BPS | **Practical limit:** 8 of 8, 27-40 s each |
| -36.4 dB | -9.9 | -11.5 | -8.6 | 31 BPS | Barely usable; up to 90 s per message |
| **-37.9 dB** | **-11.4** | **-13.0** | -8.7 | 31 BPS | **Edge:** 256 s to connect |
| -39.5 dB | -13.0 | -14.6 | - | - | No connect, call not heard |
| -42.6 dB | -16.1 | -17.7 | - | - | No connect, call not heard |

What stood out:

- **The connect fails before the data does.** At -37.9 dB every 31 BPS data frame decoded once the link was up. But K3BWA's replies to the call were missed twice, and the connect took 256 seconds, close to Mercury's default 300-second call limit (`call_max_s`). Three dB lower, the call was not detected at all.
- **The failed bench tests look exactly like my on-air attempt.** The same short calls, then 27-second calls at speed 103, with no `SN` and no answer.
- **Mercury's `SN` reading is a good guide when signals are weak.** From +5 down to -12 dB it stays within about 1.5 dB of the measured SNR in 2.5 kHz. On strong signals it reads low: 16 at a real +22 dB.
- **Speeds:** 321 BPS down to about +3 dB, then 68 and 87 BPS, then 31 BPS from about -4 dB down. At 31 BPS each data frame takes about 27 seconds.

## Problems found

These came out of the TCP captures. They're worth reporting to the Mercury developers.

1. **Data dropped at disconnect, but reported as sent.** When both stations disconnect while data is still queued, Mercury throws the data away and still reports `BUFFER 0`. VarAC can't tell the message never arrived. Separately, the station that disconnects never resends its own disconnect frame if it's lost. At -15.1 dB that caused a 30-second stall, which matches `disconnect_drain_timeout_s = 30`. At -36.4 dB a disconnect took 114 seconds.
2. **Stray null bytes.** Whenever a port has been quiet for 30 seconds, Mercury sends a single `0x00` byte on it, on both the command and data ports, even during a QSO. VARA doesn't do this, and VarAC's data port expects length-prefixed `NN text` messages.
3. **Data carried into the next QSO.** Two bytes VarAC wrote after a `DISCONNECTED` were held by Mercury and delivered to the other station at the start of the next session, 27 minutes later.
4. **Speed choice that doesn't follow the signal.** At -24.4 dB both stations started on the robust speeds. K3BWA then stepped back up to 321 BPS and decoded every frame, even though its path was the weaker one (+0.5 vs +2.1 dB). K3JSJ stayed on 68/87 BPS for the whole session. Messages longer than 24 bytes took 25-41 seconds from K3JSJ, against about 17 seconds from K3BWA.

There are also smaller interface differences that VarAC tolerates. Mercury formats the `BITRATE` line differently from VARA (`BITRATE (3) 321 BPS`, without the RX/TX suffix), and it never sends `BUSY ON/OFF` with the default `busy_detect = false`. That matches the BUSY indicator problem noted on the [Mercury Ascending]({{ '/software/mercury-ascending' | relative_url }}) page.

## How does this compare with VARA?

I don't have a like-for-like answer yet. The 2018 VARA HF specification lists speed levels and data rates but no SNR thresholds, and its level numbering doesn't match VARA 4.x. Winlink's [July 2020 simulator comparison](https://winlink.org/sites/default/files/a_winlink_digital_mode_performance_comparison_based_on_the_ionis_sim_hf_vhf_channel_simulator_-_july_5_2020_0.pdf) tested VARA 500 down to -5 dB SNR in 3 kHz, its lowest test point, where VARA 500 still passed traffic. That puts VARA 500 and Mercury both working at about -5 dB, but it says nothing about where VARA stops. Part 2 will run the same sweep with VARA HF on the same bench.

## Limitations

- **One test per level.** Each test had 4 to about 80 frames, so a single lost frame at the stronger levels could be chance. The connect limit is narrowed to about 1.5 dB.
- **White noise only.** No fading, multipath or interference. Real HF paths will do worse than this bench.
- **One PC, two instances.** Both modems share the same sound engine and clock, so timing and frequency offsets you'd see on air are absent.

## Next

- Run the same sweep with VARA HF for a direct comparison.
- Repeat the -24.4 dB test with K3BWA calling, to see whether the speed step-up depends on which station called.
- Try `disconnect_drain_timeout_s` at about 10 seconds to see whether disconnects get faster without losing data.
- Back on air, now that I know what a Mercury station that isn't being heard looks like.
