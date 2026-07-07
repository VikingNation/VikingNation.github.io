---
layout: post
title: "MDC Digital EMCOMM Challenge, 9 - 12 July 2026"
date: 2026-07-06 12:00:00 -0400
categories: [mdc-emcomm-challenge]
permalink: /mdc-emcomm-challenge/2026-07-06-mdc-digital-emcomm-challenge-9-12-july-2026/
tags: [winlink, varac, fldigi, emcomm, mdc-section]
---

**Dates:** Thursday, July 9 – Sunday, July 12, 2026 (00:00 ET Thu to 20:00 ET Sun)
**Incident:** MDC EMCOMM CHALLENGE
**Subject:** IMAGE XFER – RELAY TO N3XL
**Contact:** B. Smith, N3XL, PRGE AEC Operations

This announcement may be forwarded to anyone interested in getting on the ARRL
Maryland-DC (MDC) Section Winlink message distribution list and participating in
MDC Digital EMCOMM training activities. Interested parties should send a Winlink
message request to **MDCWINLINK-1** to be added to the distribution list. Challenge
Announcements are sent approximately two weeks before each Challenge.

## Scope

MDC Digital EMCOMM Challenges provide training opportunities for Winlink, VarAC,
and/or Fldigi radio operators to sharpen their skills for service in the Amateur
Radio Emergency Service (ARES), or other public service organizations. Challenges
simulate internet-down scenarios, such as natural disasters or terrorist attacks,
and primarily use peer-to-peer (P2P) messaging protocols that require relays.
Winlink VARA FM, VARA HF, and HF Radio-only are supported. VarAC HF and VarAC FM
provide feature-rich EMCOMM platforms. Fldigi HF messaging is incorporated for
interoperability with ARES groups using the ARRL Narrow Band Emergency Messaging
System (NBEMS).

## Purpose

The July Challenge requires the use of photo resizing tools built into the Winlink
(Task 1), VarAC (Task 2), and Fldigi (Task 3) programs. You'll learn how to adjust
an image as necessary to achieve reasonable transmission times, while still sending
the highest quality image possible. This exercise also helps familiarize you with
the [National Weather Service Online SKYWARN Spotter's Field Guide](https://www.weather.gov/spotterguide/).

## Planning

File size limitations to achieve reasonable RF transmission times will vary
depending on connection quality, propagation conditions, and equipment. A nominal
file size limit for Winlink and VarAC files is 100 KB, which is too large for RF
transmission. Suggested targets:

- **VARA FM:** resize below 30 KB
- **HF modes:** resize below 15 KB
- Adjust further if the transmission fails or takes too long

Send images to as many Target Stations as possible. Carefully observe the modes,
frequencies, dates, and times of operation in the schedule tables below.

Winlink VARA FM P2P and VarAC FM users should consider digipeating to extend range
beyond VHF line-of-sight (a VARA license is required to digipeat using VARA FM). A
VARA license is also recommended to unlock the latest features and optimal
performance.

**Make sure your software is up to date:**

- [VARA](https://rosmodem.wordpress.com)
- [VarAC](https://www.varac-hamradio.com)
- [Winlink Express](https://www.winlink.org/WinlinkExpress)
- [Fldigi](https://sourceforge.net/projects/fldigi/files)

## Tasks

### Task 1 — Winlink Image Transfer
1. Save one of the Landspout images from the [NOAA spotter guide](https://www.weather.gov/spotterguide/non_supercell/) as a JPG.
2. Suggested procedure: Create Message → New Message → Select Attachments → Add your image → Edit/Resize Image → Change Size → Make your changes → Save → Save Changes → Finished.
3. Address a P2P message and post it to your Outbox. Send via a Target Station for relay, or directly to N3XL.
4. When relaying via a Target Station, put **IMAGE XFER - RELAY TO N3XL** in the subject line. Well-defined subject lines support meaningful Winlink 309 logs and efficient message handling — build the habit now.

### Task 2 — VarAC Image Transfer
1. Save one of the Landspout images from the [NOAA spotter guide](https://www.weather.gov/spotterguide/non_supercell/) as a JPG.
2. Set up incoming/outgoing file directories in the QSO tab of Settings (e.g. `C:\VarAC\Incoming_Files` and `C:\VarAC\Outgoing_Files`).
3. Suggested procedure: Tools → Image Shrinker → Load Image → resize using Resolution/Quality sliders → check "My callsign" → Save to Disk, then copy the saved file into `C:\VarAC\Outgoing_Files`.
4. If relaying via a Target Station, type **RELAY TO N3XL** in the "New message" box at the bottom of the main window to inform the Target Station, then send the file.

### Task 3 — Fldigi HF Image Transfer (mode MFSK32)
1. Review the [image transfer training video](https://drive.google.com/file/d/11WT6GyQkOqavS0-ejTaqqcBO4KkEoJOG/view?usp=sharing).
2. Establish a connection with your Target Station (see "Establishing Fldigi Connections" below).
3. In the blue transmit area, right-click and select "Send Image?" Press "Load" and select your resized image (the dialog includes a preview).
4. Send your picture via a Target Station for relay, or directly to N3XL. Secure the Tx/Rx function using the Rx button afterward.
5. If transmission fails using X1, resize the image with the X2 button, or use a grayscale image. X2 shrinks the image size at the receiving end.
6. If relaying via a Target Station, type **RELAY TO N3XL** in the send window, before or after sending the image.

#### Establishing Fldigi Connections (P = Participant, TS = Target Station)
1. **P** – Tune radio to TS dial frequency. Use the QSY button to adjust to the 1500 Hz sweet spot.
2. **TS** – "QST QST de WX3F MDC Digital EMCOMM Challenge, K" (called periodically).
3. **P** – Precisely align cursor to TS signal for good copy; center frequency should be near 1500.
4. **P** – Once good copy is established: "WX3F de KB3XYZ, I HAVE TRAFFIC FOR RELAY TO N3XL K."
5. **TS** – "KB3XYZ de WX3F good copy pls send your traffic K."
6. **P** – Send traffic; terminate transmission when the transfer is complete.
7. **TS** – Brief acknowledgement, or request to resend, etc.

## Challenge Credit

N3XL will provide message acknowledgements to participants for messages
successfully delivered. Participants are encouraged to complete all three tasks
but should do what they can — use as many modes and Target Stations as possible.
Participation will be documented in the MDC Digital EMCOMM Challenge Report and
in the [ARRL MDC Section News](https://arrl-mdc.org/section-news/).

**Hit a Home Run:** Everyone completing all 3 tasks will be recognized for hitting
a home run!

---

## Target Station Schedules

Times are ET unless otherwise noted. Always check for beacons on dial frequencies —
flexible operating schedules may apply.

### Winlink HF Target Stations

| Callsign | Mode | Band / Frequency | Dates / Hours (ET) |
|---|---|---|---|
| N3XL | VARA HF Radio-only | Any Radio-only capable RMS | 9–12 July, 24 Hr |
| AC3EW | VARA HF P2P (500 Hz BW) | 40m, 7.091.000 MHz | 9 July, 0900–1200 |
| AC3EW | VARA HF P2P (500 Hz BW) | 20m, 14.098.000 MHz | 9 July, 1300–1500 |
| AC3EW | VARA HF P2P (500 Hz BW) | 30m, 10.128.000 MHz | 9 July, 1500–1700 |
| AC3EW | VARA HF P2P (500 Hz BW) | 80m, 3.577.000 MHz | 9 July, 2000–2130 |
| KD2QAR | VARA HF P2P (500/2300 Hz BW) | 30m, 10.142.500 MHz | 9 July, 0800–1700 |
| KD2QAR | VARA HF P2P (500/2300 Hz BW) | 40m, 7.085.000 MHz | 10 July, 0800–1700 |
| KD2QAR | VARA HF P2P (500/2300 Hz BW) | 80m, 3.589.500 MHz | 9 July 0000–0600; 9 July 2000 – 10 July 0600 |
| KB3SPH | VARA HF P2P (500 Hz BW) | 40m, 7.065.000 MHz | 9 & 10 July, 0000–1830 & 2030–2400 |
| KN3U | VARA HF P2P (500 Hz BW) | 80m, 3.591.5 MHz | 9–10 July, 0800–2200 |
| KG4K | VARA HF P2P (500 Hz BW) | 40m, 7.085.000 MHz | 10 July, 1900–2100 |

### Winlink VHF/UHF Target Stations

| Callsign | Mode | Band / Frequency | Dates / Hours (ET) | Digipeater Path |
|---|---|---|---|---|
| AC3EW | VARA FM P2P | 70cm, 441.000 MHz | 9 July 2200 – 10 July 1000 | via KF3AK-11, or W8IS-11 KF3AK-11, or N3XL-11 KF3AK-11 |
| KB3SPH | VARA FM P2P | 2m, 145.090 MHz | 9–10 July, 24 Hrs | via WM3M-10, or KD3JA-10 WM3M-10 |
| N3WOF | VARA FM P2P | 2m, 145.010 MHz | 9–10 July, 1700–2200 | via W3AAC-11, or N3HU-10 W3AAC-11 |
| KN3U | VARA FM P2P | 2m, 145.750 MHz | 9–10 July, 0800–2200 | via WA3YOO-9 |
| N3XL | VARA FM P2P | 70cm, 441.000 MHz | 9–10 July, 24 Hr | via KF3AK-11 |

### VarAC HF Target Stations

Primary group — **KD2QAR, KB3SPH, N3XL, KN3U** — Advanced/AWAY:

| Band | Slot | Frequency | Notes |
|---|---|---|---|
| 80m | Slot 13 | 3.597.250 MHz | Various — see notes below |
| 40m | Slot 13 | 7.107.250 MHz | Various — see notes below |
| 30m | Slot 3 | 10.130.750 MHz | Various — see notes below |
| 20m | Slot 13 | 14.107.250 MHz | Various — see notes below |

N3HU: available 24 Hr except 0730–0830 and 1830–1930 (Local).

Limited-availability stations (less than 6 continuous hours on frequency):

| Callsign | Mode | Band / Frequency | Dates / Hours (ET) |
|---|---|---|---|
| AC3EW | Advanced AWAY/VMail – Beaconing | 30m, Slot 3, 10.130.750 MHz | 11 July, 1100–1300 |
| AC3EW | Advanced AWAY/VMail – Beaconing | 20m, Slot 13, 14.107.250 MHz | 11 July, 1300–1500 |
| AC3EW | Advanced AWAY/VMail – Beaconing | 40m, Slot 13, 7.107.250 MHz | 11 July, 1500–1700 |
| AC3EW | Advanced AWAY/VMail – Beaconing | 80m, Slot 13, 3.597.250 MHz | 11 July, 1700–1900 |
| KG4K | Advanced AWAY – Beaconing | 20m (14.107.250) or 40m (7.107.250), Slot 13 | 11 July, 1200–1700 |

**Notes:**
- Look for beacons on dial frequencies; flexible op schedules will be used.
- Target Stations may send op schedule info in Winlink Position Reports — view at [winlink.org/userPositions](https://www.winlink.org/userPositions). [Training video](https://drive.google.com/file/d/1eVBXJZboM3Dz7H9IkpvJv97QZ-_Y5e0k/view?usp=sharing) on capturing VarAC HF Target Station position reports.
- The VarAC PSK Reporter Map and Pathfinder features can help locate Target Stations.
- Suggested PSKReporter map string for the MDC area: `&hidenight=1&hidelight=1&showsnr=1&hidelines=1&noautozoom=1&mapCenter=38.82724661878609,-76.66809540326848,8.357781738381872`
- Copy the updated `VarAC_alert_tags.conf` file into your VarAC directory for audible Target Station beacon alerts.
- Suggested additions to your VarAC HF frequency drop-down list: `14.107.250|Slot 13`, `7.107.250|Slot 13`, `3.597.250|Slot 13`, `10.130.750|Slot 3`. In the QSO tab, ensure "Consider entire frequency list as CF" is **unchecked** — no QSYs required for Challenge frequencies.

### VarAC FM Target Stations

| Callsign | Mode | Band / Frequency | Dates / Hours (ET) | Digipeater Path |
|---|---|---|---|---|
| AC3EW | Advanced AWAY/VMail | 2m, 146.640 MHz | 10 July, 1030–1700 | K3ERM 146.04/64 repeater, input tone 156.7 |
| AC3EW | Advanced AWAY/VMail | 70cm, 441.000 MHz | 10 July 2200 – 11 July 1000 | via KF3AK-11, or W8IS-11 KF3AK-11, or N3XL-11 KF3AK-11 |
| KB3SPH | Advanced AWAY | 2m, 145.090 MHz | 11 July 0000 – 12 July 2000 | via WM3M-10, or KD3JA-10 WM3M-10 |
| N3WOF | Advanced AWAY | 2m, 145.010 MHz | 11 July, 1700–2200 | via W3AAC-11, or N3HU-10 W3AAC-11 |
| KN3U | Advanced AWAY | 2m, 145.750 MHz | 11–12 July, 0800–2000 | via WA3YOO-9 |
| N3XL | Advanced AWAY | 70cm, 441.000 MHz | 11–12 July, 24 Hr | via KF3AK-11 |
| KG4K | Advanced AWAY – Beaconing | 2m, 145.010 MHz | 11 July, 1200–1700 | via W3AAC-11, or W3AAC-10 |

### Fldigi HF Target Stations (MFSK32)

| Callsign | Band / Frequency | Dates / Hours (ET) |
|---|---|---|
| KB3SPH | 40m, 7.066.000 MHz | 9 & 10 July, 1900–2000 |
| KD2QAR | 80m, 3.582.000 MHz | 10 July, 1900–2000 |
| N3XL | 40m, 7.066.000 MHz | 11–12 July, 0900–1100 |
| KG4K | 40m, 7.066.000 MHz | 11–12 July, 1100–1200 |

---

## Additional Notes

- Tips on Winlink HF/FM, VarAC HF/FM, and Fldigi are available on [Google Drive](https://drive.google.com/drive/folders/1qU3Yj9wuxuxIRzHk9MVRqQZbiptVqADA?usp=sharing).
- A training video on capturing VarAC HF Target Station position reports with detailed op schedule information is [available here](https://drive.google.com/drive/my-drive?q=type:video%20parent:0AIPvCh5P6nmCUk9PVA).
- A VarAC `alert_tags.conf` file is sent with the Target Station lists — copy it into your VarAC program directory for Target Station alerts.
- Challenges are conducted Thursday through Sunday preceding the second Tuesday of each month, except October, which is reserved for ARRL SET activities.
- Have ideas for future Challenge content or improvements? Let Bill know.

73 and GL in the Challenge,
**Bill, N3XL — MDCWINLINK-1**
