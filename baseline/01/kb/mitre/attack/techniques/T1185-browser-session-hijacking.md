---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1185
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1185-browser-session-hijacking
tactic:
    - Collection
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.[^4] <br><br>A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions, and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet.[^2] [^1]  Executing browser-based behaviors such as pivoting may require specific process permissions, such as `SeDebugPrivilege` and/or high-integrity/administrator rights.<br><br>Another example involves pivoting browser traffic from the adversary's browser through the user's browser by setting up a proxy which will redirect web traffic. This does not alter the user's traffic in any way, and the proxy connection can be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet, such as [[kb/mitre/attack/techniques/T1213.002-sharepoint|Sharepoint]] or webmail, that is accessible through the browser and which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can perform browser pivoting and inject into a user's browser to inherit cookies, authenticated HTTP sessions, and client SSL certificates.[^1] [^2]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot uses web injects and browser redirection to trick the user into providing their login credentials on a fake or modified web page.[^1] [^2] [^3] [^4]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has the ability to use form-grabbing to extract data from web data forms.[^1]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex can perform browser attacks via web injects to steal information such as credentials, certificates, and cookies.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has injected HTML codes into banking sites to steal sensitive online banking information (ex: usernames and passwords).[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has used web injection attacks to redirect victims to spoofed sites designed to harvest banking and other credentials.  IcedID can use a self signed TLS certificate in connection with the spoofed site and simultaneously maintains a live connection with the legitimate site to display the correct URL and certificates in the browser.[^1] [^2]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has captured credentials when a user performs login through a SSL session.[^1] [^2]  |
| [S0530](https://attack.mitre.org/software/S0530) | Melcoz | Melcoz can monitor the victim's browser for online banking sessions and display an overlay window to manipulate the session in the background.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields.[^1] [^2] [^3]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has used the Puppeteer module to hook and monitor the Chrome web browser to collect user information from infected hosts.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use advanced web injects to steal web banking credentials.[^1] [^2]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has the ability to use form-grabbing and event-listening to extract data from web data forms.[^1]   |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can conduct form grabbing, steal cookies, and extract data from HTTP sessions.[^1]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Close all browser sessions regularly and when they are no longer needed. |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Since browser pivoting requires a high integrity process to launch from, restricting user permissions and addressing Privilege Escalation and [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|Bypass User Account Control]] opportunities can limit the exposure to this technique. |

 [^1]: [ICEBRG Chrome Extensions](https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses)
 [^2]: [Cobalt Strike Browser Pivot](https://www.cobaltstrike.com/help-browser-pivoting)
 [^3]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^4]: [Wikipedia Man in the Browser](https://en.wikipedia.org/wiki/Man-in-the-browser)
 [^5]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
 [^6]: [IBM TrickBot Nov 2016](https://securityintelligence.com/tricks-of-the-trade-a-deeper-look-into-trickbots-machinations/)
 [^7]: [Microsoft Totbrick Oct 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/Totbrick)
 [^8]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
 [^9]: [Dell Dridex Oct 2015](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)
 [^10]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^11]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
 [^12]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^13]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^14]: [Bitdefender Agent Tesla April 2020](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
 [^15]: [Breakdev Evilginx 2.2 NOV 2018](https://breakdev.org/evilginx-2-2-jolly-winter-update)
 [^16]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
 [^17]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^18]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^19]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)
 [^20]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^21]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^22]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
 [^23]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
 [^24]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^25]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
