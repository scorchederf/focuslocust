---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1539
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1539-steal-web-session-cookie
tactic:
    - Credential Access
platforms:
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.<br><br>Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.[^6] <br><br>There are several examples of malware targeting cookies from web browsers on the local system.[^3] [^2]  Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]] by tricking victims into running malicious JavaScript in their browser.[^7] [^1] <br><br>There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle|Adversary-in-the-Middle]]) that can be set up by an adversary and used in phishing campaigns.[^4] [^5] <br><br>After an adversary acquires a valid cookie, they can then perform a [[kb/mitre/attack/techniques/T1550.004-web-session-cookie|Web Session Cookie]] technique to login to the corresponding web application.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to steal web session cookies from Internet Explorer, Netscape Navigator, FireFox and RealNetworks applications.[^1]  |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner can steal Google Chrome and Apple Safari browser cookies from the victim’s machine. [^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can steal the victim's cookies to use for duplicating the active session from another device.[^1]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can harvest cookies and upload them to the C2 server.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has used a script that extracts the web session cookie and sends it to the C2 server.[^1]   |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to capture web session cookies.[^1] [^2]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can harvest cookies from Internet Explorer, Edge, Chrome, and Naver Whale browsers.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET uses `scp` to access the `~/Library/Cookies/Cookies.binarycookies` file.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate attempts to steal Opera cookies, if present, after terminating the related process.[^1]    |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Spica has the ability to steal cookies from Chrome, Firefox, Opera, and Edge browsers.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules that can steal cookies from Firefox, Chrome, and Edge web browsers.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer attempts to steal cookies and related information in browser history.[^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has exfiltrated updated cookies from Google, Naver, Kakao or Daum to the C2 server.[^1]   |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can capture web session cookies and session information from victim browsers.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has harvested cookies from various browsers.[^3] [^2] [^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has stolen browser cookies and settings.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can collect information on each session with a victim including the session cookie.[^2] [^1] <br> |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has harvested Safari cookies stored within `/Library/Containers/com.apple.Safari/Data/Library/Cookies/ Cookies.binarycookies`.[^2]   GlassWorm has also stolen cookies within Chromium and Firefox browsers.[^1] [^2]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can list the contents of `%LocalAppData%\Google\Chrome\User Data\` and `%LocalAppData%\Microsoft\Edge\User Data\` to obtain cookies.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users to identify aspects of phishing attempts where they're asked to enter credentials into a site that has the incorrect domain for the application they are logging into. Additionally, train users not to run untrusted JavaScript in their browser, such as by copying and pasting code or dragging and dropping bookmarklets. |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Deploy hardware-based token (e.g., YubiKey or FIDO key), which incorporates the target login domain as part of the negotiation protocol, will prevent session cookie theft through proxy methods.<br><br>Implement Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. This mitigates the risk of session cookie replay attacks by ensuring that stolen tokens cannot be reused on unauthorized devices. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Implement auditing for authentication activities and user logins to detect the use of stolen session cookies. Monitor for impossible travel scenarios and anomalous behavior that could indicate the use of compromised session tokens or cookies. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Configure browsers or tasks to regularly delete persistent cookies.<br><br>Additionally, minimize the length of time a web cookie is viable to potentially reduce the impact of stolen cookies while also increasing the needed frequency of cookie theft attempts – providing defenders with additional chances at detection.[^1]  For example, use non-persistent cookies to limit the duration a session ID will remain on the web client cache where an attacker could obtain it.[^2]  |

 [^1]: [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
 [^2]: [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^3]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^4]: [Github evilginx2](https://github.com/kgretzky/evilginx2)
 [^5]: [GitHub Mauraena](https://github.com/muraenateam/muraena)
 [^6]: [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)
 [^7]: [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)
 [^8]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
 [^9]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)
 [^10]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
 [^11]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^12]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^13]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^14]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^15]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
 [^16]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
 [^17]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^18]: [Kroll Qakbot June 2020](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)
 [^19]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^20]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^21]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^22]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^23]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^24]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
 [^25]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^26]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^27]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^28]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^29]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^30]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^31]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^32]: [TrendMicro LummaStealer 2025](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)
 [^33]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^34]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^35]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
