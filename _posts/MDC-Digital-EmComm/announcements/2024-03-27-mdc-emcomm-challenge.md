---
layout: post
title: "MDC Section EMCOMM Challenge, 4-8 April 2023"
date: 2024-03-27
categories: [mdc-emcomm-challenge]
author: "MDCWINLINK-1"
permalink: /mdc-emcomm-challenge/2024-03-27-mdc-section-emcomm-challenge-4-8-april-2023/
tags: [winlink, varac, fldigi, emcomm, mdc-section]
---

**Source:** MDCWINLINK-1@winlink.org


## Purpose

In the April Challenge you will simulate participation in an ARES Mutual Assistance Team (ARESMAT) event and provide Health and Welfare (H&W) status messages from a simulated tornado disaster zone. In this Challenge participants will gain familiarity with Winlink and Fldigi Radiogram Forms and practice Winlink, VarAC, and Fldigi Peer-to-Peer (P2P) messaging and EMCOMM Post Office deliveries.  Since different ARESMAT teams use differing messaging software, it is important to gain familiarity with as many of them as you can. It is only with trial and error and repeated practice that operator proficiency can be maintained. The emphasis on P2P messaging and EMCOMM Post Office services in Challenges is because, when the internet goes down and Ham communications services are called upon, these are the primary methods that will be available. HF Radio-only (RO) services are also available, but other than routine exercise of your Message Pickup Stations (MPS), should only be used in the event of massive internet outages of national impact.			                      

SCENARIO:
A simulated EF4 Tornado has devasted communities from LaPlata to Waldorf, MD, traversing near Route 301. First responders are on scene, the internet is down in the area. ARESMAT assistance from Maryland and Delaware has been requested. MDC Section Winlink, VarAC, and Fldigi Target Stations will be providing H&W message relays of message traffic from the disaster zone.


## Planning

In Task P, you will simulate ARESMAT coordination and request a Target Station List to use for Tasks 1, 2, and 3. Task P is a prerequisite to participation in Tasks 1, 2, and/or 3, and can be done stand-alone. 

For Tasks 1,2, and 3, the following modes of transmission will be supported by Target Stations:  
1. Winlink messaging: Packet P2P, Vara FM P2P, Vara HF P2P, and the WX3F EMCOMM Post Office. 
2. VarAC messaging VarAC HF and VarAC FM. 
3. Fldigi messaging: Fldigi HF MT63-500S,  PSK-31, and others.

Carefully review


## Task 3

Fldigi messaging: You are simulating an ARESMAT operator deployed to a tornado disaster zone. Use the RADIOGRAM Form found in FLMSG and create a H&W status report message from a person in the disaster zone (see attachments). Your creativity on the particulars of your status report is welcome. Address the form (see ADDRESS INFO above). Identify the message as an EXERCISE MESSAGE in the OP


## Execution

INCIDENT: MDC APRIL CHALLENGE  
DATE: 4-8 April, 2024

Task P: ARESMAT Preparations:
1. Participants will submit a Winlink Check-in form. Address the Check-in form to tactical address MDCWINLINK-1. The Comments section of the form should contain the following: Subject: TARGET STATION LIST REQUEST and state if the participant is able, or unable, to deploy with ARESMAT in the Comments section.
 
2. The Check-in may occur any time during the Challenge and the Target Station Lists will be provided. Try to get your request in on day one, or as early in the Challenge as possible. 

3. The internet is available for this task. Telnet or any standard RMS Channel session type should be used. Be sure to use the Winlink Check-in form.


## Task 1

Winlink messaging: You are simulating an ARESMAT operator deployed to a Tornado disaster zone. Use the RADIOGRAM & RRI Forms template of your choice and create a H&W status report message from a person in the disaster zone. Your creativity on the particulars of your status report is welcome. Address the form (see ADDRESS INFO below) and send it as a Winlink P2P message to a Target Station for relay, or drop it off at the WX3F EMCOMM Post Office. Identify the message as an EXERCISE MESSAGE in the Op Note(s).


## Task 2

VarAC messaging: You are simulating an ARESMAT operator deployed to a Tornado disaster zone.  Compose a VMail containing a H&W status report message from a person in the disaster zone. Your creativity on the particulars of your status report is welcome.  Address the VMail to N3XL and park it at a VarAC Target Station for relay (see PARK VMAIL FOR RELAY/PICKUP below). A short message length (<500 characters) is required for VMail. Identify the message as an EXERCISE MESSAGE and include the ADDRESS INFO below in the message text. 

ADDRESS INFO:
To: Bill Smith, Bowie, MD 20715 
N3XL@ARRL.NET

SAMPLE MESSAGE TEXT
Everyone safe here. Please don't worry. (ARL ONE)
Property damage very severe in this area. (ARL SIXTEEN)
Will contact you as soon as possible. (ARL SIX)
Participant Name KB3XYZ
Participant Location in Challenge Tornado Zone.


## Notes

* We are in need of VHF and/or HF Target Stations in the DC/Northern VA area, and Northeastern (Baltimore) Maryland areas. The main requirement is the capability to provide some manner of service for Winlink, VarAC, and/or Fldigi HF.  Modest stations are welcome. Winlink Target Stations using VHF can serve strictly direct peer-to-peer, if no digipeater is available.  Target Station Instructions are issued with each Challenge and we will have a Zoom training session to help any new Target Stations get going. If interested, or if you have any questions, please let me know.

* A VarAC alert_tags.conf file is attached.  Copy and paste this file into your VarAC program directory to receive MDC Bulletins and Target Station alerts.

Tip Sheets on Winlink, VarAC, ?Brevity in Emergency Communications? are available on Google Drive: https://drive.google.com/drive/folders/1qU3Yj9wuxuxIRzHk9MVRqQZbiptVqADA?usp=sharing

If you have any ideas for the content of future Challenges, or suggestions for improvements, let me know.

73 and GL in the Challenge,
Bill N3XL, MDCWINLINK-1
?Learn by doing.?


## Flmsg Tips

a. Save your Radiogram in FLMSG using ?File > Save?. 
b. You may view sent and received Radiograms, File > Open C:\Users\userx\NBEMS.files\ICS\messages. 
c. To send again, use ?File > Open? and double-click on the message > AutoSend. 
d. Once your message is open, you will find File > View > Plain Text to be a handy way to copy and paste you message into VarAC. 

* ESTABLISHING FLDIGI CONNECTIONS (P = Participant. TS = Target Station)
P - Tune radio to TS dial frequency. Use QSY button to adjust frequency to the 1500 sweet spot.
TS - QST QST de WX3F WX3F, QST QST de WX3F WX3F K (call periodically, QST=calling all stations).
P - Precisely align cursor to TS signal, to obtain good copy. The display center frequency will normally be at, or near, 1500. 
P - Once good copy of the Target Station is established, respond WX3F WX3F de KB3XYZ KB3XYZ, I have traffic K
TS - RR KB3XYZ good copy, pls send your traffic K.
P ? Send Radiogram using AutoSend.
TS ? Brief acknowledgement, or request to resend, etc.

* PARK VMAIL FOR RELAY / PICKUP:
1. Before making a VarAC connection with a Target Station, it is recommended to prepare the message for relay (SEND VMAIL button). Address the message to the ultimate destination callsign and enter desired text. Once prepared, post the VMail to your Outbox. Connect to a Target/Relay Station, once connected go to your Outbox, right click on the message, and select "Relay now through connected station". 

2. For short messages that require no preparation ahead of time (or if you have text copied and ready insert), connect to a Target Station, address the message to the ultimate destination callsign enter the message text, click on the SEND VMAIL button. The system will ask if you want to "Relay now through connected station".

3. Parking alleviates the need to request a relay in the message when the addressee is a Ham with a callsign. However, this by no means precludes requesting a relay to a specific destination in the text or subject line, especially since the Radiogram addressee is usually NOT going to be a Ham. So, parking has an advantage if the addressee is a Ham, but not so much if the addressee isn?t a Ham.

RECOGNITION:
N3XL will provide message acknowledgements to participants for all tasks that have been successfully completed. Participants are encouraged to complete all tasks, but do what you can. Participation will be documented in the MDC Section Winlink/VarAC Challenge Report and in the ARRL MDC Section Newsletter.  * HIT A HOMERUN: Everyone completing all 4 tasks will be recognized for hitting a homerun.
