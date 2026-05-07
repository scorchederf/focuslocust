---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1055
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1055-process-injection
tactic:
    - Privilege Escalation
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. <br><br>There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. <br><br>More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to directly inject its code into the web browser process.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT can inject malicious code into process created by the “Command_Create&Inject” function.[^1]  |
| [[kb/mitre/attack/software/S0040-htran\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can inject into into running processes.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | JHUHUGIT performs code injection injecting its own functions to browser processes.[^1] [^2]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has been injected directly into a running process, including `explorer.exe`.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea injects itself into explorer.exe.[^1] [^2]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can inject a variety of payloads into processes dynamically chosen by the adversary.[^2] [^3] [^1]  |
| [S0168](https://attack.mitre.org/software/S0168) | Gazer | Gazer injects its communication module into an Internet accessible process through which it performs C2.[^1] [^2]  |
| [S0176](https://attack.mitre.org/software/S0176) | Wingbird | Wingbird performs multiple process injections to hijack system processes and execute malicious code.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can inject code into system processes including notepad.exe, svchost.exe, and vbc.exe.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can inject content into lsass.exe to load a module.[^1]  |
| [S0206](https://attack.mitre.org/software/S0206) | Wiarp | Wiarp creates a backdoor through which remote attackers can inject files into running processes.[^1]  |
| [S0226](https://attack.mitre.org/software/S0226) | Smoke Loader | Smoke Loader injects into the Internet Explorer process.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can use `VirtualAlloc`, `WriteProcessMemory`, and then `CreateRemoteThread` to execute shellcode within the address space of `Notepad.exe`.[^1]  |
| [S0247](https://attack.mitre.org/software/S0247) | NavRAT | NavRAT copies itself into a running Internet Explorer process to evade detection.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can inject itself into another process to avoid detection including use of a technique called ListPlanting that customizes the sorting algorithm in a ListView structure.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot has used `Nt*` [[kb/mitre/attack/techniques/T1106-native-api\|Native API]] functions to inject code into legitimate processes such as `wermgr.exe`.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can inject into known, vulnerable binaries on targeted hosts.[^1]   |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has a command to hide itself by injecting into another process.[^1]  |
| [S0347](https://attack.mitre.org/software/S0347) | AuditCred | AuditCred can inject code from files to other running processes.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT injects into a newly spawned process created from a native Windows executable.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has injected into running processes.[^1] 	 |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has relied on injecting its payload directly into the process memory of the victim's preferred browser.[^1]  |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro can run shellcode it injects into a newly created process.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to inject code into the svchost.exe, iexplorer.exe, explorer.exe, and default browser processes.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's dispatcher can inject itself into running processes to gain higher privileges and to evade detection.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has injected itself into remote processes to encrypt files using a combination of `VirtualAlloc`, `WriteProcessMemory`, and `CreateRemoteThread`.[^1]  |
| [S0469](https://attack.mitre.org/software/S0469) | ABK | ABK has the ability to inject shellcode into svchost.exe.[^1]  |
| [S0470](https://attack.mitre.org/software/S0470) | BBK | BBK has the ability to inject shellcode into svchost.exe.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to inject shellcode into svchost.exe.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can inject itself into running processes on a compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA can inject into running processes on a compromised host.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can inject code through calling `VirtualAllocExNuma`.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor can inject its payload into iexplore.exe process.[^1]  |
| [S0561](https://attack.mitre.org/software/S0561) | GuLoader | GuLoader has the ability to inject shellcode into a donor processes that is started in a suspended state. GuLoader has previously used RegAsm as a donor process.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can inject decrypted shellcode into the LanmanServer service.[^1]  |
| [[kb/mitre/attack/software/S0581-ironnetinjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has injected an install module into a newly created process.[^1]  |
| [S0614](https://attack.mitre.org/software/S0614) | CostaBricks | CostaBricks can inject a payload into the memory of a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.[^4] [^2] [^3] [^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can inject itself into processes including explore.exe, Iexplore.exe, Mobsync.exe., and wermgr.exe.[^3] [^4] [^5] [^2] [^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can inject into the `svchost.exe` process for execution.[^1]  |
| [S0664](https://attack.mitre.org/software/S0664) | Pandora | Pandora can start and inject code into a new `svchost` process.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT has the ability to inject malicious DLLs into a specific process for privilege escalation.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can migrate the loader into another process.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can inject shellcode directly into Excel.exe or a specific process.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] includes a subproject `DonutTest` to inject shellcode into a target process.[^1] 	 |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can inject code into multiple processes on infected endpoints.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | The [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can inject the loader file, Speech02.db, into a process.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can inject code into a targeted process by writing to the remote memory of an infected system and then create a remote thread.[^1]   |
| [S1074](https://attack.mitre.org/software/S1074) | ANDROMEDA | ANDROMEDA can inject into the `wuauclt.exe` process to perform C2 actions.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can inject itself into an existing explorer.exe process by using `RtlCreateUserThread`.[^1] [^2]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja has the ability to inject an agent module into a new process and arbitrary shellcode into running processes.[^1] [^2]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER includes a binary labeled `authd` that can inject a library into a running process and then hook an existing function within that process with a new function from that library.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu's binary is injected into memory via `WriteProcessMemory`.[^1] [^2]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP compromises the `.text` section of a legitimate system DLL in `%windir%` to hold the contents of retrieved plug-ins.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware injects into a newly-created `svchost.exe` process prior to device encryption.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can inject its final stage into another process on the targeted system.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can inject shellcode into the memory of compromised hosts.[^2] [^1] [^3]  |
| [S9021](https://attack.mitre.org/software/S9021) | DOWNIISSA | DOWNIISSA can inject shellcode directly into process memory including WINWORD.exe and msiexec.exe.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can inject code directly into legitimate applications.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can inject decrypted payloads into processes including wuauclt.exe., rdrleakdiag.exe, and tabcal.exe.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Utilize Yama (ex: /proc/sys/kernel/yama/ptrace_scope) to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux, grsecurity, and AppArmor. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of process injection based on common sequences of behavior that occur during the injection process. For example, on Windows 10, Attack Surface Reduction (ASR) rules may prevent Office applications from code injection. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1055.011-extra-window-memory-injection\|T1055.011]] | Extra Window Memory Injection |
| [[kb/mitre/attack/techniques/T1055.003-thread-execution-hijacking\|T1055.003]] | Thread Execution Hijacking |
| [[kb/mitre/attack/techniques/T1055.013-process-doppelg-nging\|T1055.013]] | Process Doppelgänging |
| [[kb/mitre/attack/techniques/T1055.004-asynchronous-procedure-call\|T1055.004]] | Asynchronous Procedure Call |
| [[kb/mitre/attack/techniques/T1055.002-portable-executable-injection\|T1055.002]] | Portable Executable Injection |
| [[kb/mitre/attack/techniques/T1055.014-vdso-hijacking\|T1055.014]] | VDSO Hijacking |
| [[kb/mitre/attack/techniques/T1055.012-process-hollowing\|T1055.012]] | Process Hollowing |
| [[kb/mitre/attack/techniques/T1055.009-proc-memory\|T1055.009]] | Proc Memory |
| [[kb/mitre/attack/techniques/T1055.005-thread-local-storage\|T1055.005]] | Thread Local Storage |
| [[kb/mitre/attack/techniques/T1055.008-ptrace-system-calls\|T1055.008]] | Ptrace System Calls |
| [[kb/mitre/attack/techniques/T1055.015-listplanting\|T1055.015]] | ListPlanting |
| [[kb/mitre/attack/techniques/T1055.001-dynamic-link-library-injection\|T1055.001]] | Dynamic-link Library Injection |

 [^1]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^2]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
 [^3]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^4]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^5]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)
 [^6]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^7]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^8]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^9]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
 [^10]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)
 [^11]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
 [^12]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)
 [^13]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)
 [^14]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^15]: [JPCert BlackTech Malware September 2019](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)
 [^16]: [McAfee REvil October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-crescendo/)
 [^17]: [Donut Github](https://github.com/TheWover/donut)
 [^18]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^19]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
 [^20]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^21]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^22]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
 [^23]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^24]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^25]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^26]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^27]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
 [^28]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^29]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^30]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
 [^31]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^32]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^33]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^34]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^35]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)
 [^36]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
 [^37]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^38]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^39]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^40]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)
 [^41]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^42]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^43]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
 [^44]: [Kroll Qakbot June 2020](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)
 [^45]: [Trend Micro Qakbot December 2020](https://success.trendmicro.com/en-US/solution/KA-0011282)
 [^46]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^47]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^48]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)
 [^49]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)
 [^50]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^51]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^52]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^53]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^54]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^55]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
 [^56]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^57]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^58]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^59]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^60]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^61]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^62]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^63]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^64]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^65]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^66]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^67]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^68]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^69]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^70]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^71]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^72]: [F-Secure Sofacy 2015](https://labsblog.f-secure.com/2015/09/08/sofacy-recycles-carberp-and-metasploit-code/)
 [^73]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
 [^74]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^75]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)
 [^76]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
 [^77]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^78]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)
 [^79]: [Cyble Egregor Oct 2020](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
 [^80]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^81]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
