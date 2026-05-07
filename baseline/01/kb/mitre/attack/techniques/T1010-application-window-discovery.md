---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1010
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1010-application-window-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.[^2]  For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([[kb/mitre/attack/techniques/T1518.001-security-software-discovery|Security Software Discovery]]) to evade.[^1] <br><br>Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]] commands and [[kb/mitre/attack/techniques/T1106-native-api|Native API]] functions.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy captures window titles.[^1]  |
| [S0033](https://attack.mitre.org/software/S0033) | NetTraveler | NetTraveler reports window names along with keylogger information to provide application context.[^1]  |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | The discovery modules used with Duqu can collect information on open windows.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can monitor the titles of open windows to identify specific keywords.[^1] 	  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has a command to get text of the current foreground window.[^1]  |
| [S0157](https://attack.mitre.org/software/S0157) | SOUNDBITE | SOUNDBITE is capable of enumerating application windows.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can discover and close windows on controlled systems.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can enumerate active windows.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can use  the `GetForegroundWindow` and `GetWindowText` APIs to discover where the user is typing.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can enumerate windows and child windows on a compromised host.[^1] [^2]  |
| [S0261](https://attack.mitre.org/software/S0261) | Catchamas | Catchamas obtains application windows titles and then determines which windows to perform [[kb/mitre/attack/techniques/T1113-screen-capture\|Screen Capture]] on.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | APT-C-36 used a customized version of [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] to monitor browser windows for strings relating to specific Colombian financial institutions.[^1] <br> |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar gathers information about opened windows.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can list all windows on victim systems.[^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi has a command to capture active windows on the machine and retrieve window titles.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT gathers information about opened windows during the initial infection.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete saves the window names.[^1]   |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to list the names of all open windows on the infected host.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to list open windows on the compromised host.[^1] [^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor can obtain application window titles and then determines which windows to perform Screen Capture on.[^1]  |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to identify open windows on the compromised host.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo can enumerate all windows on the victim’s machine.[^1] [^2]  |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to identify the titles of running windows on a compromised host.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can identify installed security tools based on window names.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to enumerate windows on a compromised host.[^1] <br> |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman reports window names along with keylogger information to provide application context.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can check the name of the window displayed on the system.[^1]   |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream has the ability to discover application windows via execution of `EnumWindows`.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can use `GetForegroundWindow` to enumerate the active window.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate will search for cryptocurrency wallets by examining application window names for specific strings.[^1]  DarkGate extracts information collected via NirSoft tools from the hosting process's memory by first identifying the window through the `FindWindow` API function.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can enumerate running application windows.[^1]  |
| [S1233](https://attack.mitre.org/software/S1233) | PAKLOG | PAKLOG has used `GetForegroundWindow` to access the foreground window. [^1]   PAKLOG has also captured text from the foreground windows.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has used `GetForegroundWindow` to detect virtualization or sandboxes by calling the API twice and comparing each window handle.[^1]  |

 [^1]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^2]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^3]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^4]: [Kaspersky NetTraveler](https://web.archive.org/web/20160326004042/http://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/kaspersky-the-net-traveler-part1-final.pdf)
 [^5]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^6]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^7]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^8]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^9]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^10]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^11]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^12]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^13]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^14]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^15]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^16]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^17]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^18]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^19]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^20]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^21]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^22]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^23]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^24]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^25]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^26]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^27]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^28]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^29]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^30]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
 [^31]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^32]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^33]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^34]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)
 [^35]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
 [^36]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
