---
layout: post
title: "MDC Digital EMCOMM Challenge, 5-8 DECEMBER 2024"
date: 2024-11-21
categories: [mdc-emcomm-challenge]
author: "MDCWINLINK-1"
permalink: /mdc-emcomm-challenge/2024-11-21-mdc-digital-emcomm-challenge-5-8-december-2024/
tags: [winlink, varac, fldigi, emcomm, mdc-section]
---

**Source:** MDCWINLINK-1@winlink.org


## Purpose

This exercise requires the use of photo resizing tools that are built into the Winlink (


## Task 1

Winlink File Xfer:
a.The Winlink attachment Image 'Resizing Tool' will be used. Suggested procedures:  Create 'Message' > 'New Message' > select Attachments > 'Add' provided image > 'Edit/Resize-Image' > 'Change Size' > make your changes > Save > 'Save Changes' > 'Finished' > Address and post to your Outbox. Send your message requesting relay to N3XL via Target Stations.
b. Place IMAGE XFER -  PLS RELAY TO N3XL in the Subject line. (Well defined subject lines are a good habit as they are needed to achieve meaningful Winlink 309 message logs that are routinely needed in after action reports).


## Task 2

VarAC File Xfer: 
a.The VarAC 'Image Shrinker' tool will be used. Suggested procedures: go to Tools > Image Shrinker > LOAD IMAGE > resize the image using the Resolution and Quality sliders > check the My callsign box > SAVE TO DISK. The file will be saved to your Outgoing files directory by default. 
b. Once connected to your Target Station, use the SEND FILE button, select the file from the Outgoing files directory (or elsewhere). 
c. While connected, either before or after the file transfer, type IMAGE XFER - PLS RELAY TO N3XL in the New Message window at the bottom of the main window and then SEND.


## Task 3

Fldigi (mode MFSK64) File Xfer: 
a. Establish a connection with your Target Station, see ESTABLISHING FLDIGI CONNECTIONS below.
b. In blue transmit area of the screen, right click and select Send Image > Press the Load button in the dialog window and select the provided image. The file selection dialog has a preview capability, so you will see what the image looks like. (Alternatively, if using a previously resized image, you may open a Windows file browser and drag and drop the image in the blue SEND window.)
c. If the transmission fails using X1, be prepared to resize the image using the X2 or X4 buttons in the dialog window.
d. Type IMAGE XFER - PLS RELAY TO N3XL in the SEND window, before or after sending the image.

* ESTABLISHING FLDIGI CONNECTIONS (P = Participant. TS = Target Station)
P - Tune radio to TS dial frequency. 
TS - QST QST de WX3F WX3F, QST QST de WX3F WX3F K (call periodically, QST=calling all stations).
P - Precisely align cursor to TS signal, to obtain good copy. The display center frequency will normally be at, or near, 1500. 
P - Once good copy of the Target Station is established, respond WX3F de KB3XYZ, I HAVE IMAGE FOR RELAY TO N3XL K.
TS - RR good copy, Pls send your image K.
P -  Send image. Terminate the transmission when image xfer is completed.
TS -  Brief acknowledgement, or request to resend, etc.


## Planning

An image file that will require resizing for RF transmission will be provided as an attachment, along with the HF and VHF-UHF Target Station Lists, on 3 December 2024.

File size limitations to achieve reasonable RF transmission times will vary, depending on the quality of your connection, propagation conditions, and equipment limitations. The nominal file size limit for Winlink and VarAC is 100 Kbytes, which is generally too large for RF transmissions. We are suggesting that you resize the provided image, starting at approximately 50 Kbytes for VHF-UHF transmissions and 20 Kbytes for HF, resizing as necessary if the transmission fails or takes too long.

You are encouraged to send images to as many Target Stations as possible. Carefully observe the Target Station modes, frequencies, dates, and times of operation provided in the Target Station Lists.

Winlink Packet P2P and Vara FM P2P users should consider the use of digipeating to extend their range beyond VHF line-of-sight. A VARA license is required to digipeat using Vara FM. The extra hop(s) used to digipeat will probably require additional resizing for successful transmissions.

Ensure that your VARA, VarAC, and Winlink software programs are up-to-date.
VARA - https://rosmodem.wordpress.com
VarAC - https://www.varac-hamradio.com
Winlink - https://www.winlink.org/WinlinkExpress
Fldigi - https://sourceforge.net/projects/fldigi/files/

Set up Incoming and Outgoing files directories in the QSO tab of your VarAC Settings. C:\VarAC\Incoming_Files and C:\VarAC\Outgoing_Files are suggested. The Incoming directory is where you will find any incoming image files. Images can be loaded for resizing from any directory.


## Execution

INCIDENT: MDC DECEMBER CHALLENGE
SUBJECT: IMAGE XFER - PLS RELAY TO N3XL
DATES: 5-8 DECEMBER 2024
TIMES: EST (ET)


## Challenge Credit

N3XL will provide message acknowledgements to participants for images that have been successfully relayed. Participants are encouraged to complete all three tasks in the December Challenge, but do what you can. You are encouraged to connect with as many Target Stations as you can. Participation will be documented in the MDC Section Winlink/VarAC Challenge Report and in the ARRL MDC Section Newsletter.  * HIT A HOMERUN: Everyone completing all 3 tasks will be recognized for hitting a homerun.


## Notes

* We are in need of VHF and/or HF Target Stations. The main requirement is the capability to provide some manner of service for Winlink, and/or VarAC, and/or Fldigi.  Modest stations are welcome. Winlink Target Stations using VHF-UHF can serve strictly peer-to-peer, if no digipeater is available.  Target Station Instructions are issued with each Challenge and we will have a Zoom training session to help any new Target Stations get going. If interested, or if you have any questions, please let me know.

* A VarAC alert_tags.conf file is attached.  Copy and paste this file into your VarAC program directory to receive Target Station alerts.

Tip Sheets on Winlink, VarAC, Fldigi and Brevity in Emergency Communications are available on Google Drive: https://drive.google.com/drive/folders/1qU3Yj9wuxuxIRzHk9MVRqQZbiptVqADA?usp=sharing

If you have any ideas for the content of future Challenges, or suggestions for improvements, let me know.

73 and GL in the Challenge,
Bill N3XL, MDCWINLINK-1
Learn by doing.
