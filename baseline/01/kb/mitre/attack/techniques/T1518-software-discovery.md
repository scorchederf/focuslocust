---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1518
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1518-software-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [[kb/mitre/attack/techniques/T1518-software-discovery|Software Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Such software may be deployed widely across the environment for configuration management or security reasons, such as [[kb/mitre/attack/techniques/T1072-software-deployment-tools|Software Deployment Tools]], and may allow adversaries broad access to infect devices or move laterally.<br><br>Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation|Exploitation for Privilege Escalation]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to identify installed programs on a compromised host.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky lists all installed software for the infected machine.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT can check the victim's default browser to determine which process to inject its communications module into.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can scan victim drives to look for specific banking software on the machine to determine next actions.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | The Cobalt Strike System Profiler can discover applications through the browser and identify the version of Java the target has.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can gather the victim's Internet Explorer version.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can collect information about installed software used by specific users, software executed on user login, and software executed by each system.[^1] [^2]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex has collected a list of installed software on the system.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant can retrieve a list of applications from the `SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` registry key.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] gathered a list of installed software on the infected host.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has searched the compromised system for banking applications.[^1] [^2]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to identify the Internet Explorer (IE) version on an infected host.[^1]  |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to gather information on installed applications.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore has the ability to enumerate what browser is being used as well as version information for Safari.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can collect information on installed applications.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can query the Registry for installed applications.[^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell can list PHP server configuration details.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape searches for the kubectl binary.[^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette can enumerate running software on a targeted system.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can enumerate a list of installed programs.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can check for the Telegram installation directory by enumerating the files on disk.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET uses `ps aux` with the `grep` command to enumerate common browsers and system processes potentially impacting XCSSET's exfiltration capabilities.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can list the installed applications on a compromised host.[^1]  |
| [S1042](https://attack.mitre.org/software/S1042) | SUGARDUMP | SUGARDUMP can identify Chrome, Opera, Edge Chromium, and Firefox browsers, including version number, on a compromised host.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can collect a list of installed software from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can collect .NET, PowerShell, and Python information from an infected host.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can check for the presence and version of the .NET framework.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can identify the victim's browser in order to serve the correct fake update page.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can list installed software on compromised systems.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer is capable of identifying running software on victim machines.[^2] [^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | <br>Cuckoo Stealer has the ability to search systems for installed applications.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer variants use COM objects to enumerate installed applications from the "AppsFolder" on victim machines.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | If sent the command `16001`, LightSpy uses the `NSFileManger contentsOfDirectoryAtPath()` to enumerate the Applications folder to collect the bundle name, bundle identifier, and version information from each application's `info.plist` file. The results are then converted into a JSON blob for exfiltration.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has used several commands executed in sequence via `cmd` in a short interval to gather software versions including querying Registry keys.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can get a list of programs on the victim device.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has gathered installed programs and running processes.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has searched for existing wallet applications to include Ledger Live and Trezor Suite.[^1]  |
| [S9029](https://attack.mitre.org/software/S9029) | IronWind | IronWind can list installed software on targeted hosts.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1518.002-backup-software-discovery\|T1518.002]] | Backup Software Discovery |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery |

 [^1]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^2]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^3]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^4]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^5]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^6]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^7]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^8]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^9]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^10]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^11]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^12]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^13]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^14]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^15]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^16]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^17]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^18]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^19]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^20]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^21]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^22]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^23]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^24]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^25]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^26]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^27]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^28]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^29]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^30]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^31]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^32]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^33]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^34]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^35]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^36]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^37]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^38]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^39]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^40]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^41]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
