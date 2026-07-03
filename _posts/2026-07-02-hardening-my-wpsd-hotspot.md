---
title: "Hardening My WPSD Hotspot"
date: 2026-07-02
layout: post
categories: [software]
tags: [dmr, wpsd]
---

I have a DMR radio and have been running a DMR hotspot. The hotspot allows you to make contacts with ham radio operators all over the world. I have been using the [WPSD](https://w1chp.net/wpsd/) (W0CHP-PiStar-Dashboard) for a while now.  WPSD is the software that ties together DMR, YSF, P25, NXDN, and D-STAR digital voice modes and gives you a slick web dashboard to manage it all. It works great out of the box. Working "works great out of the box" and "is the most secure" aren't always the same thing. I used an Artificial Intelligence Large Language Model (Claude Sonnet) to perform an audit in order to identify any items that could be improved from a security point of view.

This post is a rundown of what I found, what I fixed, and — just as importantly — what I *didn't* fix and why.

## TLDR;
Claude Code (Sonnet) helped me secure my WPSD Hotspot in about six hours. The hotspot now runs HTTPS, password-less sudo access is disabled, and blanket passwordless root access in WPSD dashboard has been replaced with per command based approach.

## Why bother hardening a hotspot?

It's tempting to think of a ham radio hotspot as a low-value network target: it's not a bank, it's not holding anyone's personal data, worst case someone figures out the input frequency and uses your hotspot, right? But the hotspot is a full Linux box on your home network, running a web-facing PHP admin dashboard, with a shell login exposed over the browser (shellinabox). If that dashboard has a code execution bug — and web dashboards do, regularly — whatever privileges the web server has become the attacker's privileges. On a stock WPSD install, those privileges turned out to be a lot bigger than they needed to be.

## The big one: a root shell hiding behind the web server

The single worst finding was this line, sitting quietly in `/etc/sudoers`:

```
www-data ALL=(ALL) NOPASSWD: ALL
```

`www-data` is the user the web server (and therefore all the dashboard's PHP code) runs as. This line means that user can run *anything* as root, with no password. In practice, this exists because the dashboard needs to do legitimately privileged things — restart services, write config files, reboot the Pi, flash modem firmware, and so on. But granting blanket root access to do that is like giving the mail carrier a master key to your house because they occasionally need to leave a package inside.

The fix wasn't to remove the sudo access — the dashboard genuinely needs some of it — it was to replace the blanket grant with an explicit allowlist. I used Claude Code to review all 156 PHP files in the dashboard, catalogued every single `sudo` invocation, and grouped them into categories: WPSD's own wrapper scripts, file operations, service management, network management, hardware control. Each category became a `Cmnd_Alias` in a sudoers drop-in file, and the blanket rule was deleted.

The one holdout was `sudo bash`. Four code paths in the dashboard used `sudo bash -c '...'` to run small shell snippets — collecting logs, gzipping dmesg output, running a factory-reset script. There's no way to scope `sudo bash` down safely in sudoers itself; if you can run `bash`, you can run anything. Since these code paths always used fixed, internally-computed commands rather than raw user input, the practical risk was theoretical rather than proven — but "theoretical today" has a way of becoming "exploitable tomorrow" once someone finds an unrelated bug that lets them influence those variables.

So Claude wrote small wrapper scripts that do exactly what those bash snippets did, with no arguments and no shell meta characters, and swapped the four `sudo bash` calls for calls to the wrapper scripts instead. Same functionality, but now a compromised PHP process is capped at "run this one fixed script" instead of "run anything."

## Everything else that got fixed

The bash-elimination story is the most interesting one, but it was one item out of a much longer list. Some other highlights:

- **Shellinabox was serving a browser-based shell over plain HTTP.** Login credentials and terminal sessions were going out in clear text. Fixed by installing Let's Encrypt certificate and automatic renewal.
- **The dashboard itself had no HTTPS.** Same fix — Let's Encrypt cert, with a renewal hook that keeps the web server's cert in sync automatically.
- **SSH allowed an unused, out-of-the-box `debian` account with passwordless sudo.** Deleted — There was a debain user account with passwordless sudo. It appeared that this account was not being used. I deleted the account.
- **`fail2ban` wasn't installed at all.** Fail2ban will detect if someone is trying to guess the password and block the IP address for some time.  SSH and the dashboard's auth were both wide open to unlimited brute-force attempts. Installed fail2ban and jails for both.
- **Old TLS versions (1.0/1.1) and weak ciphers were still accepted.** Restricted to TLS 1.2/1.3 with a modern cipher suite.
- **Basic security headers were missing from HTTP responses.** Added some security headers based upon recommended best practices
- **Nginx logging was disabled entirely**, so there was no way to see who was hitting the box or what was failing. Re-enabled with proper log rotation.
- **The `pi-star` login user also had passwordless sudo**, meaning any process running as that user — not just an intentional terminal session — could silently become root. Now requires a password.

## What I chose *not* to fix

Not every finding gets fixed, and I think it's worth being honest about that instead of pretending everything gets a clean check mark. A few items were consciously accepted as risk:

- **SSH password authentication is still enabled** alongside key-based auth (via .ssh/authorized_keys). I kept password authentication as a fallback in case my key ever becomes unavailable, and it's mitigated by the sudo password requirement above plus fail2ban.
- **AppArmor isn't active.** Raspberry Pi OS ships the module but doesn't enable it by default (unlike Ubuntu), and turning it on requires a boot parameter change and a reboot, with no guarantee that meaningful profiles even exist for the services I care about (nginx, PHP-FPM, shellinabox). Not worth the operational risk for an unverified benefit.
- **PHP's `allow_url_fopen` is on.** This lets PHP code fetch remote URLs directly, which is technically a class of SSRF risk. But grepping the dashboard source showed it's used pervasively and legitimately — talkgroup lookups, repeater API calls, remote themes — and Claude couldn't find an actual user-controlled injection point that would turn this into a real vulnerability. Turning it off would silently break working features to defend against a risk I couldn't demonstrate.
- **Some firewall findings (an overly permissive FORWARD chain policy, a couple of open NetBIOS ports) were left alone** because WPSD manages its own iptables rules and rewrites them on every reboot. Any manual fix would just get silently reverted at the next restart — fixing it properly means going through WPSD's own firewall mechanism, which is a bigger project than the fix itself justifies. I will probably revisit this in the future.
- **SSH is still on the default port.** Moving it buys obscurity, not security — the box is already protected by key-based auth, a sudo password requirement, and fail2ban. The operational hassle of remembering a non-standard port wasn't worth it.

## How can SSH-Agent helped you jump start the process?
I setup ssh-agent and connected to my hotspot. I then loaded Claude in that terminal. The ssh-agent enabled Claude to remotely connect to my WPSD hotspot without me needing to provide the login password. Claude run the Linux commands to audit the security of the hotspot.

## What did I prompt AI to get started?
The prompt was something like "Please perform a security audit of my WPSD hotspot running on hostname X. Please provide a recommendations on what needs to be fixed to improve security. Document things as you go. There is a git repo in the directory you are running."

## How much time did all of this take?
The initial audit took Claude around 45-60 minutes. It came back with a list of seventeen recommendations to fix. Recommendations were grouped by category (Critical, High, Medium, Low). I reviewed each recommendation and the recommended course of action. I run ssh key based authentication and the public key is on my WPSD hotspot. The private key running on my Windows laptop is protected with a password. The passwordless sudo, default setting of WPSD, allowed Claude to fully execute commands without me needing to enter the password for the pi-star user account. Claude was able to quickly update and test that updates worked.

Some of the updates required me to test the functionality of the WPSD dashboard and hotspot to confirm that updates didn't break anything. Once the password less 'sudo' was removed things slowed down. This is due to needing for me to execute any sudo commands on the hotspot myself. Claude gave me the exact list of commands. I just needed to run and copy/paste output into Claude window and it verified everything was worked.

It took me about six hours to go through all seventeen recommendations. I think it would have taken me five to six times longer to cover a large number of these. The sudoers review required looking through 156 files. That would have taken me several weeks to complete.

## Where did things get stuck?
For this particular tasks, did not have the AI agent getting 'stuck' or going down a rabbit whole.

One area that did get stuck is with shellinabox. Shellinabox required the HTTPS key to be in a certain format. It took about 45 minutes trying, testing, and updating things until they got worked through. Several files needed to be created on the hotspot as part of the process.  I asked Claude to create those files and secure copy them over to the hotspot. This helped eliminate potential typos / errors by copy/pasting large amounts of information between the Claude terminal and the SSH session running in another window.

## Where things stand now

Every finding from the original audit — critical, high, medium, and low severity — has either been fixed and verified, or deliberately accepted with a documented reason. The dashboard can no longer hand out a root shell through a code execution bug, remote access is encrypted end to end, and there's actual logging and rate-limiting in place to notice and slow down anyone trying to poke at it.

