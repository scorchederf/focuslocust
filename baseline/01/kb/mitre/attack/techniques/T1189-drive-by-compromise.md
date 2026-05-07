---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1189
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1189-drive-by-compromise
tactic:
    - Initial Access
platforms:
    - Identity Provider
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. Multiple ways of delivering exploit code to a browser exist (i.e., [[kb/mitre/attack/techniques/T1608.004-drive-by-target|Drive-by Target]]), including:<br><br>* A legitimate website is compromised, allowing adversaries to inject malicious code<br>* Script files served to a legitimate website from a publicly writeable cloud storage bucket are modified by an adversary<br>* Malicious ads are paid for and served through legitimate ad providers (i.e., [[kb/mitre/attack/techniques/T1583.008-malvertising|Malvertising]])<br>* Built-in web application interfaces that allow user-controllable content are leveraged for the insertion of malicious scripts or iFrames (e.g., cross-site scripting)<br><br>Browser push notifications may also be abused by adversaries and leveraged for malicious code injection via [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]]. By clicking "allow" on browser push notifications, users may be granting a website permission to run JavaScript code on their browser.[^3] [^2] [^4] <br><br>Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or a particular region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.[^1] <br><br>Typical drive-by compromise process:<br><br>1. A user visits a website that is used to host the adversary controlled content.<br>2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. The user may be required to assist in this process by enabling scripting, notifications, or active website components and ignoring warning dialog boxes.<br>3. Upon finding a vulnerable version, exploit code is delivered to the browser.<br>4. If exploitation is successful, the adversary will gain code execution on the user's system unless other protections are in place. In some cases, a second visit to the website after the initial scan is required before exploit code is delivered.<br><br>Unlike [[kb/mitre/attack/techniques/T1190-exploit-public-facing-application|Exploit Public-Facing Application]], the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0215](https://attack.mitre.org/software/S0215) | KARAE | KARAE was distributed through torrent file-sharing websites to South Korean victims, using a YouTube video downloader application as a lure.[^1]  |
| [S0216](https://attack.mitre.org/software/S0216) | POORAIM | POORAIM has been delivered through compromised sites acting as watering holes.[^1]  |
| [S0451](https://attack.mitre.org/software/S0451) | LoudMiner | LoudMiner is typically bundled with pirated copies of Virtual Studio Technology (VST) for Windows and macOS.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore has been spread through malicious advertisements on websites.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has cloned legitimate websites/applications to distribute the malware.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil has infected victim machines through compromised websites and exploit kits.[^1] [^2] [^3] [^4]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro has used compromised websites and Google Ads to bait victims into downloading its installer.[^1] [^2]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit spread through watering holes on popular sites by injecting JavaScript into the HTML body or a `.js` file.[^1] [^2]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 has been delivered to targets via downloads from malicious domains.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish has been distributed through compromised websites with malicious content often masquerading as browser updates.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction. |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Adblockers can help prevent malicious code served through ads from executing in the first place. Script blocking extensions can also help to prevent the execution of JavaScript. <br><br>Consider disabling browser push notifications from certain applications and browsers.[^2] [^1] [^3]  |
| [[kb/mitre/attack/mitigations/M1048-application-isolation-and-sandboxing\|M1048]] | Application Isolation and Sandboxing | Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist.[^1] [^2] <br><br>Other types of virtualization and application microsegmentation may also mitigate the impact of client-side exploitation. The risks of additional exploits and weaknesses in implementation may still exist for these types of systems.[^2]  |
| [[kb/mitre/attack/mitigations/M1050-exploit-protection\|M1050]] | Exploit Protection | Security applications that look for behavior used during exploitation such as Windows Defender Exploit Guard (WDEG) and the Enhanced Mitigation Experience Toolkit (EMET) can be used to mitigate some exploitation behavior.[^1]  Control flow integrity checking is another way to potentially identify and stop a software exploit from occurring.[^2]  Many of these protections depend on the architecture and target application binary for compatibility. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Ensuring that all browsers and plugins are kept updated can help prevent the exploit phase of this technique. Use modern browsers with security features turned on.[^1] <br> |

 [^1]: [Shadowserver Strategic Web Compromise](http://blog.shadowserver.org/2012/05/15/cyber-espionage-strategic-web-compromises-trusted-websites-serving-dangerous-results/)
 [^2]: [push notification -mcafee](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/scammers-impersonating-windows-defender-to-push-malicious-windows-apps/)
 [^3]: [Push notifications - viruspositive](https://viruspositive.com/resources/blogs/the-dark-side-of-web-push-notifications)
 [^4]: [push notifications - malwarebytes](https://www.malwarebytes.com/blog/news/2019/01/browser-push-notifications-feature-asking-abused)
 [^5]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)
 [^6]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)
 [^7]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^8]: [Trendmicro_IcedID](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)
 [^9]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^10]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)
 [^11]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)
 [^12]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)
 [^13]: [ESET Bad Rabbit](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)
 [^14]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)
 [^15]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)
 [^16]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)
 [^17]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)
 [^18]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
 [^19]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^20]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^21]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^22]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
 [^23]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^24]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^25]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
 [^26]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
