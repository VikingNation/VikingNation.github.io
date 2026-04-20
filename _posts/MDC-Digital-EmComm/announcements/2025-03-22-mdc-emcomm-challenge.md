---
layout: post
title: "MDC Digital EMCOMM Challenge, 3-6 April 2025"
date: 2025-03-22
categories: [mdc-emcomm-challenge]
author: "MDCWINLINK-1"
permalink: /mdc-emcomm-challenge/2025-03-22-mdc-digital-emcomm-challenge-3-6-april-2025/
tags: [winlink, varac, fldigi, emcomm, mdc-section]
---

**Source:** MDCWINLINK-1@winlink.org


## Purpose

MDC Digital EMCOMM Challenges are designed to improve operator skills that will be needed when the internet and cell towers go down. Target Stations support the following Winlink modes: 
Vara HF P2P, Vara FM P2P, Vara HF Radio-only, and EMCOMM Post Office. VarAC HF, VarAC FM, and Fldigi HF are also supported.

Imagine a hurricane striking your community with extensive wind damage and flooding. Internet and cellular communications have been knocked out and the devastation is widespread. You will assist in recovery operations by providing your local damages assessment.

Use the attached damage assessment checklist, which was extracted from Montgomery County, MD, Fire and Rescue Service WINDSHIELD ASSESSMENT SURVEY, and create an ICS-213 providing a description of an affected locations in your community and the extent of simulated damages. You will also provide the accurate geographic location of your message origination for mapping. Target Stations will perform message relays to MDC Assistent Emergency Coordinator (AEC) for Operations, N3XL for coordination via served agencies.


## Planning

info. Preparation will make things much more pleasant and productive for you.

2. If you are a mobile or portable station operator, you really should have GPS capability to take advantage of the built-in locator features in Winlink and VarAC. If you do not have GPS already, I suggest Googling for a USB GPS Puck and procuring one from your favorite vendor and plugging it into your computer. Prices vary, but around $20 or less should work for you - a bit more for a mobile mag mount.

3. VarAC users can configure a custom map (reference: VarAC User Manual) of the MDC area to use as a default map for PSKReporter. This will assist you in locating the Target Stations, all of which are in the MDC area. Go to Settings > Logging > PSKReporter. Check the Upload box. To make the MDC area your default map and avoid the pain of zooming in repeatedly, copy and paste the following string in the Custom map box: &hidenight=1&hidelight=1&showsnr=1&hidelines=1&noautozoom=1&mapCenter=38.82724661878609,-76.66809540326848,8.357781738381872

4. Configurations for Poisition Reporting:
To support multiple applications accessing your GPS's comm port, such as your time sync and messaging applications, Enterlogic's VSPE (Virtual Serial Port Emulator), is a solution. It provides a splitter function that can support up to 10 applications. As an alternative to VSPE,  com0com  is another option. Info on how to set up com0com can be found at: https://mcacs.net/training-resources/gps-hockey-puck/ 

- Winlink: a. Set up your GPS / Position Report settings. See how to at https://www.youtube.com/watch?v=MAg-iP0A1D0. b. Go to Settings > Preferences > Message sending options, and check the box for: Include your location in message headers. This will automatically provide your location in the headers of all of your Winlink messages. In this exercise, also place your location in the ICS-213, as it theoretically would be going to a served agency who would not see the Winlink header.

- VarAC: Go to Settings > Rig control and VARA Config > GPS Tab > Set up the comm port that your GPS is using. Put the tag <GPSLOC> in the ICS-213 message to describe your location.

- If you do not have GPS, you can get an accurate location for your messages from Google Maps ( https://www.google.com/maps/). Enter your address in the search bar > left click on pin for details > right-click on the detailed map's pin > the coordinates are at the top of the pop-up list > left click and they will be copied to the clipboard > paste these coordinates into your message. Alternatively, provide your 6 digit grid square in the message, for a less accurate approximate location. 

5. Carefully observe the Target Station modes, frequencies, dates, and times of operation provided in the Target Station Lists, in PSKReporter, and additional information in Winlink.org Position Reports. The Target Station lists will be provided to the MDC Winlink distribution list on Monday, 31 MAR 2025. 

6. VarAC HF Target Stations can be identified in PSKReporter. With 4 bands being used and with no fixed Target Station time schedules, using PSKReporter is a must for


## Task 2

VarAC messaging. Utilize EMCOMM mode. Before making your connection to a Target Station, prepare your message: SEND VMAIL > Load Template > choose ICS-213 General Message > address To: Target Station > Subject: EmComm General Message - EXERCISE MSG > in the MESSAGE block use these Incident Name, To, and Subject as indicated above > for item 7. use the WINDSHIELD ASSESSMENT SURVEY checklist and provide the following:  a. location description of the affected areas, b. simulated damages assessment, and c. the geographic coordinates of message origination > approve and SEND  > message will post to your Outbox > make your connection to theTarget Station and the message will be delivered.


## Execution

Incident Name: MDC EMCOMM CHALLENGE
To: N3XL, PRGE AEC OPERATIONS
Subject: HURRICANE DAMAGE ASSESSMENT - EXERCISE MSG
Date/Time: 3 APR 2025, 00:00 ET  to  6 APR 2025, 23:59  
GMT Offset: -4 Hr.


## Task 1

Winlink messaging. Use an ICS-213 general message template.  Use the checkbox provided on the form to mark your message as Exercise traffic. Use Incident Name, To, and Subject as indicated above > In in block 7. use the WINDSHIELD ASSESSMENT SURVEY checklist and provide the following: a. location description of the affected areas, b. simulated damages assessment, and c. the geographic coordinates of message origination > approve the form and Submit > address the message to a Target Station and post to your Outbox > make your connection to theTarget Station and the message will be delivered.


## Task 3

Fldigi messaging. Use an ICS-213 form found in the FLMSG application. For Inc:, use Incident Name, To, and Subject, as indicated above. > address the form to N3XL, AEC-Operations > in the Message Block use the WINDSHIELD ASSESSMENT SURVEY checklist, provide the following:  a. location description of the affected areas, b. simulated damages assessment, and c. the geographic coordinates of message origination >  make your connection to a Target Station. > verify that your modem type in FLMSG and Fldigi match up, and send your message using FLMSG ?Autosend? at the top of the form. Your message will be acknowledged by the Target Station and relayed.


## Challenge Credit

N3XL will provide message acknowledgements to participants for messages that have been successfully delivered. Participants are encouraged to complete all three tasks in the April Challenge, but do what you can. You are encouraged to use as many modes and Target Stations as you can. Participation will be documented in the MDC Digital EMCOMM Challenge Report and in the ARRL MDC Section News, https://arrl-mdc.org/section-news/.
HIT A HOMERUN: Everyone completing all 3 tasks will be recognized for hitting a homerun.

Your message acknowledgement will contain a Scorecard, as follows:
- Your ICS-213 was / was not marked an EXERCISE message.
- Your ICS-213 described / failed to describe the LOCATION where simulated damages occurred.
- Your ICS-213 described / failed to describe the EXTENT of simulated damages.
- Your ICS-213 provided / failed to provide the GEOGRAPHIC COORDINATES of message origination.


## Notes

* A VarAC alert_tags.conf file will be sent with the Target Station Lists. Copy and paste this file into your VarAC program directory to receive MDC Bulletins and Target Station alerts.

* Tip Sheets on Winlink, VarAC,  Brevity in Emergency Communications and an up-to-date Winlink Power Point presentation are available on Google Drive: https://drive.google.com/drive/folders/1qU3Yj9wuxuxIRzHk9MVRqQZbiptVqADA?usp=sharing

* Challenges are conducted on the Thursday through Sunday preceding the second Tuesday of each month, except in October which is reserved for ARRL SET activities. (The second Tuesdays are MDC Section Check-ins.)

* If you have any ideas for the content of future Challenges, or suggestions for improvements, let me know.

73 and GL in the Challenge,
Bill N3XL, MDCWINLINK-1
 Learn by doing.
