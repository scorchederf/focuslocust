---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1047
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1047-windows-management-instrumentation
tactic:
    - Execution
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.[^4]  WMI is an administration feature that provides a uniform environment to access Windows system components.<br><br>The WMI service enables both local and remote access, though the latter is facilitated by [[kb/mitre/attack/techniques/T1021-remote-services|Remote Services]] such as [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model|Distributed Component Object Model]] and [[kb/mitre/attack/techniques/T1021.006-windows-remote-management|Windows Remote Management]].[^4]  Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.[^4]  [^2] <br><br>An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [[kb/mitre/attack/tactics/TA0007-discovery|Discovery]] as well as [[kb/mitre/attack/tactics/TA0002-execution|Execution]] of commands and payloads.[^2]  For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [[kb/mitre/attack/techniques/T1490-inhibit-system-recovery|Inhibit System Recovery]]).[^3] <br><br>**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] as the primary WMI interface.[^5]  In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.[^5] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | The DustySky dropper uses Windows Management Instrumentation to extract information about the operating system and whether an anti-virus is active.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | A BlackEnergy 2 plug-in uses WMI to gather victim host details.[^1]  |
| [S0151](https://attack.mitre.org/software/S0151) | HALFBAKED | HALFBAKED can use WMI queries to gather system information.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can use WMI to deliver a payload to a remote host.[^2] [^3] [^1]  |
| [S0156](https://attack.mitre.org/software/S0156) | KOMPROGO | KOMPROGO is capable of running WMI queries.[^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may use WMI when collecting information about a victim.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-WmiCommand` CodeExecution module uses WMI to execute and retrieve the output from a PowerShell payload.[^1] [^2]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can use WMI queries to retrieve data from compromised hosts.[^1] [^2]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT collects various information via WMI requests, including CPU information in the Win32_Processor entry (Processor ID, Name, Manufacturer and the clock speed).[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA uses WMI to perform process monitoring.[^1] [^2]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use WMI to execute commands.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | One variant of Zebrocy uses WMI queries to gather information.[^1]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito's installer uses WMI to search for antivirus display names.[^1]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE uses WMI to perform discovery techniques.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar obtains a list of running processes through WMI querying.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT uses WMI to query the Windows Registry.[^1]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin uses various WMI queries to check if the sample is running in a sandbox.[^1] [^2]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT uses WMIC to identify anti-virus products installed on the victim’s machine and to obtain firewall details.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has used wmi queries to gather information from the system.[^1]   |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia searches for anti-virus software and firewall products installed on the victim’s machine using WMI.[^1] [^2]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus has used wmic.exe for local discovery information.[^1]  |
| [[kb/mitre/attack/software/S0357-impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-impacket\|Impacket]]'s `wmiexec` module can be used to execute commands through WMI.[^1] [^2]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use WMI to deliver a payload to a remote host.[^1]   |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer uses WMI to help propagate itself across a network.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry utilizes `wmic` to delete shadow copies.[^3] [^1] [^2]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has used WMI to execute powershell.exe.[^1]  |
| [S0368](https://attack.mitre.org/software/S0368) | NotPetya | NotPetya can use `wmic` to help propagate itself across a network.[^1] [^2]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth uses WMIC to execute payloads. [^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi executes received commands with wmic.exe (for WMI commands). [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has used WMI to recompile the Managed Object Format (MOF) files in the WMI repository.[^1] 	 |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has a number of modules that use WMI to execute tasks.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has used the WMI command-line (WMIC) utility to run tasks.[^1]  |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy leverages WMI to enumerate anti-virus on the victim.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif droppers have used WMI classes to execute [[kb/mitre/attack/techniques/T1059.001-powershell\|PowerShell]] commands.[^1]  |
| [S0396](https://attack.mitre.org/software/S0396) | EvilBunny | EvilBunny has used WMI to gather information about the system.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has used WMI to attempt to delete the shadow volumes on a machine, and to connect a virtual machine to the network domain of the victim organization's network.[^1] [^2]   |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can use WMI to delete Shadow Volumes.[^1] 	 |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can use `wmic process call create` in a scheduled task to launch plugins and for execution.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has used WMI to execute binaries.[^2] [^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can execute remote commands using Windows Management Instrumentation.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can use WMI to monitor for and kill specific processes listed in its configuration file.[^1] [^2]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can use WMI to log into remote machines for propagation.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can execute a WMI query to gather information about the installed antivirus engine.[^1] [^2]  |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage can use WMI for execution.[^1] [^2]  |
| [S0553](https://attack.mitre.org/software/S0553) | MoleNet | MoleNet can perform WMI commands on the system.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST used the WMI query `Select * From Win32_SystemDriver` to retrieve a driver listing.[^1]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM has used the Windows Management Instrumentation (WMI) tool to enumerate infected machines.[^1]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot has used WMI to discover network connections and configurations. Sibot has also used the Win32_Process class to execute a malicious DLL.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet used WMI with an `explorer.exe` token to execute on a remote share.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS can use Windows Mangement Instrumentation (WMI) calls to execute operations.[^1]  |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM has the ability to use WMI to delete volume shadow copies.[^1]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY can use WMI to delete volume shadow copies.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS can use WMI to delete files on a  target machine.[^1] [^2]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon uses wmic.exe to delete shadow copies.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can execute WMI queries to gather information.[^1]  |
| [S0654](https://attack.mitre.org/software/S0654) | ProLock | ProLock can use WMIC to execute scripts on targeted hosts.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can use WMI for execution on a compromised host.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can use WMI to execute commands.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can use `wmic` to gather information from a system.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can use `wmic.exe` as part of its effort to delete shadow copies.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use WMI for lateral movement.[^1]  |
| [S0698](https://attack.mitre.org/software/S0698) | HermeticWizard | HermeticWizard can use WMI to create a new process on a remote machine via `C:\windows\system32\cmd.exe /c start C:\windows\system32\\regsvr32.exe /s /iC:\windows\<filename>.dll`.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT can use WMI to gather AV products installed on an infected host.[^1]  |
| [S1032](https://attack.mitre.org/software/S1032) | PyDCrypt | PyDCrypt has attempted to execute with WMIC.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can use WMI to gather system information and to spawn processes for code injection.[^3] [^2] [^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can use WMI to open a Windows command shell on a remote machine.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use WMI to move laterally.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can use `WMI` queries to detect the presence of a virtual machine environment.[^1]   |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can use WMI queries to obtain system information.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can use `wmic.exe` to delete shadow copies on compromised networks.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta has used WMI to execute files over the network.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can utilize WMI to collect system information, create new processes, and run malicious PowerShell scripts on a compromised machine.[^1] [^2]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic can use WMI to execute PowerShell commands on a compromised machine.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 can query the WMI class `Win32_ComputerSystem` to gather information.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate has used WMI to execute files over the network and to obtain information about the domain.[^1]   |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish has used WMI calls for script execution and system profiling.[^1]   |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira will leverage COM objects accessed through WMI during execution to evade detection.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin can execute via LNK containing a command to run a legitimate executable, such as wmic.exe, to download a malicious Windows Installer (MSI) package.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware has the ability to use wmic.exe to spread to multiple endpoints within a compromised environment.[^2] [^1] <br> |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can use WMI queries for discovery on the victim host.[^1]  |
| [S1152](https://attack.mitre.org/software/S1152) | IMAPLoader | IMAPLoader uses WMI queries to query system information on victim hosts.[^1]  |
| [[kb/mitre/attack/software/S1155-covenant\|S1155]] | Covenant | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can utilize WMI to install new Grunt listeners through XSL files or command one-liners.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus has used WMI in malicious email infection chains to facilitate the installation of remotely-hosted files.[^2] [^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker uses WMI to query information about the victim operating system.[^1]  |
| [S1193](https://attack.mitre.org/software/S1193) | TAMECAT | TAMECAT has used Windows Management Instrumentation (WMI) to query anti-virus products.[^1]   |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can use wmic.exe to delete volume shadow copies.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has used `wmic` to gather information from the victim device.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has used WMI queries to gather information from the system.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can use WMIC to change the Volume Shadow Copy Service (VSS) startup type to manual.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can execute commands with WMI.[^1] [^2]  |
| [S9026](https://attack.mitre.org/software/S9026) | ROAMINGHOUSE | ROAMINGHOUSE can use WMI to launch a legitimate executable later used to enable DLL sideloading.[^2] [^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag can use a .NET program to execute WMI queries and send unique victim IDs to  C2.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can use wmic to collect system information.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | By default, only administrators are allowed to connect remotely using WMI. Restrict other users who are allowed to connect, or disallow all users to connect remotely to WMI. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Prevent credential overlap across systems of administrator and privileged accounts. [^1]  |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use application control configured to block execution of `wmic.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `wmic.exe` application and to prevent abuse.[^1]  |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block processes created by WMI commands from running. Note: many legitimate tools and applications utilize WMI for command execution. [^1]  |

 [^1]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)
 [^2]: [Mandiant WMI](https://www.mandiant.com/resources/reports)
 [^3]: [WMI 6](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^4]: [WMI 1-3](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page?redirectedfrom=MSDN)
 [^5]: [WMI 7,8](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/wmi-command-line-wmic-utility-deprecation-next-steps/ba-p/4039242)
 [^6]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^7]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^8]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^9]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
 [^10]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^11]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^12]: [Securelist BlackEnergy Feb 2015](https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/)
 [^13]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^14]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
 [^15]: [Carbon Black Emotet Apr 2019](https://www.carbonblack.com/2019/04/24/cb-tau-threat-intelligence-notification-emotet-utilizing-wmi-to-launch-powershell-encoded-code/)
 [^16]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^17]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^18]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^19]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
 [^20]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^21]: [Bitdefender Agent Tesla April 2020](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
 [^22]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^23]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^24]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^25]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
 [^26]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^27]: [Github Covenant](https://github.com/cobbr/Covenant)
 [^28]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
 [^29]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^30]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^31]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^32]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^33]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
 [^34]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^35]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^36]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
 [^37]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^38]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^39]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^40]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^41]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^42]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
 [^43]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^44]: [ATTACKIQ MUSTANG PANDA TONESHELL March 2023](https://www.attackiq.com/2023/03/23/emulating-the-politically-motivated-chinese-apt-mustang-panda/)
 [^45]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^46]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
 [^47]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
 [^48]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
 [^49]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^50]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^51]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
 [^52]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
 [^53]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^54]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^55]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^56]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^57]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^58]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^59]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
 [^60]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^61]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
 [^62]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^63]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^64]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^65]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
 [^66]: [US-CERT NotPetya 2017](https://www.us-cert.gov/ncas/alerts/TA17-181A)
 [^67]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
 [^68]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^69]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^70]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^71]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^72]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)
 [^73]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
 [^74]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^75]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^76]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^77]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^78]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^79]: [DFIR_Sodinokibi_Ransomware](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)
 [^80]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
 [^81]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^82]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
 [^83]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^84]: [Cybereason Lockbit 2.0](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)
 [^85]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
 [^86]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^87]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^88]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^89]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
 [^90]: [Hornet Security Avaddon June 2020](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
 [^91]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^92]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^93]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^94]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^95]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^96]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^97]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
 [^98]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^99]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^100]: [Bromium Ursnif Mar 2017](https://www.bromium.com/how-ursnif-evades-detection/)
 [^101]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
 [^102]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^103]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^104]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^105]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^106]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
 [^107]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^108]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^109]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^110]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)
 [^111]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^112]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^113]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^114]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^115]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^116]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^117]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^118]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^119]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^120]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^121]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
