---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1005
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1005-data-from-local-system
tactic:
    - Collection
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.<br><br>Adversaries may do this using a [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]], such as [[kb/mitre/attack/software/S0106-cmd|cmd]] as well as a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]], which have functionality to interact with the file system to gather information.[^1]  Adversaries may also use [[kb/mitre/attack/techniques/T1119-automated-collection|Automated Collection]] on the local system.<br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0009](https://attack.mitre.org/software/S0009) | Hikit | Hikit can upload files from compromised machines.[^1]  |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can upload data and files from a victim's machine.[^1]  |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy creates a backdoor through which remote attackers can steal system information.[^1]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe can collect data from a local system.[^1]  |
| [S0020](https://attack.mitre.org/software/S0020) | China Chopper | China Chopper's server component can upload local files.[^2] [^3] [^4] [^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use its `Get` command to exfiltrate specified files from the compromised system.[^1]  |
| [S0036](https://attack.mitre.org/software/S0036) | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on the local system. FLASHFLOOD will scan the My Recent Documents, Desktop, Temporary Internet Files, and TEMP directories. FLASHFLOOD also collects information stored in the Windows Address Book.[^1]  |
| [S0048](https://attack.mitre.org/software/S0048) | PinchDuke | PinchDuke collects user files from the compromised host based on predefined file extensions.[^1]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke steals user files from local hard drives with file extensions that match a predefined list.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder exfiltrates data collected from the victim mobile device.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat has collected files and data from a compromised host.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has collected files and data from a compromised host.[^1]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover searches for files on local drives based on a predefined list of file extensions.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can collect information from a compromised host.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | When it first starts, BADNEWS crawls the victim's local drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt.[^1] [^2]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can collect data from a local system.[^1] [^2]  |
| [S0169](https://attack.mitre.org/software/S0169) | RawPOS | RawPOS dumps memory from specific processes on a victim system, parses the dumped files, and scrapes them for credit card data.[^1] [^2] [^3]  |
| [[kb/mitre/attack/software/S0193-forfiles\|S0193]] | Forfiles | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^1] [^2]  |
| [S0197](https://attack.mitre.org/software/S0197) | PUNCHTRACK | PUNCHTRACK scrapes memory for properly formatted payment card data.[^2] [^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can read data from files.[^1] [^2]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can retrieve files.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can obtain data from local systems.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can upload files from compromised hosts.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can collect local files from the system .[^1]   |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc searches the local system and gathers data.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot collects files from the local system.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can collect host data and specific file types.[^1] [^2] [^3]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty collects files with the following extensions: .ppt, .pptx, .pdf, .doc, .docx, .xls, .xlsx, .docm, .rtf, .inp, .xlsm, .csv, .odt, .pps, .vcf and sends them back to the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can download files off the target system to send back to the server.[^2] [^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can collect data from the system, and can monitor changes in specified directories.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can retrieve files from compromised client machines.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar uploads files from a specified directory to the C2 server.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot collects local files and information from the victim’s local machine.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has collected information from a compromised host.[^1]   |
| [S0274](https://attack.mitre.org/software/S0274) | Calisto | Calisto can collect data from user directories.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT can upload files to the C2 from infected machines.[^2] [^1]  |
| [S0337](https://attack.mitre.org/software/S0337) | BadPatch | BadPatch collects files from the local system that have the following extensions, then prepares them for exfiltration: .xls, .xlsx, .pdf, .mdb, .rar, .zip, .doc, .docx.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can exfiltrate files from the system using a documents collector tool.[^1]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has the ability to upload files from a compromised host.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has stored collected information and discovered processes in a tmp file.[^1]  |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy has collected information and files from a compromised machine.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can collect data from a local system.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has collected files from victim machines, including certificates and cookies.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron can collect files from a local system.[^1]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to collect data from local file systems.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete searches the File system for files of interest.[^1]   |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can transfer files from a compromised host.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat has the capability to upload collected files to a C2.[^1] 	 |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun has collected data and files from a compromised host.[^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can collect information from an air-gapped host machine.[^1] 	 |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can collect Microsoft Word documents from the target's file system, as well as `.txt`, `.doc`, and `.xls` files from the Internet Explorer cache.[^1] [^2] 	 |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to access the file system on a compromised host.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to steal documents from the local system including the print spooler queue.[^1]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has the ability to exfiltrate documents from infected systems.[^1] 	 |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner has retrieved iPhone text messages from iTunes phone backup files.[^1]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic can retrieve files from the local file system.[^1]  |
| [[kb/mitre/attack/software/S0500-mcmd\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] has the ability to upload files from an infected device.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub can transfer files from the victim machine.[^1]  |
| [S0503](https://attack.mitre.org/software/S0503) | FrameworkPOS | FrameworkPOS can collect elements related to credit card data from process memory.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can copy files and directories from a compromised host.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can send files from the victim machine to C2.[^1] [^2]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can exfiltrate files from the victim machine.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has collected credit card data using native API functions.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN |  BLINDINGCAN has uploaded files from victim machines.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can send a file containing victim system information to C2.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has uploaded files and information from victim machines.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can retrieve information from the infected machine.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch can exfiltrate files from compromised systems.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected information from a compromised host.[^1] [^2]  |
| [S0564](https://attack.mitre.org/software/S0564) | BlackMould | BlackMould can copy files on a compromised host.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can collect a variety of information from victim machines.[^1]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a module to collect information from the local database.[^1]   |
| [[kb/mitre/attack/software/S0594-out1\|S0594]] | Out1 | [[kb/mitre/attack/software/S0594-out1\|Out1]] can copy files and Registry data from compromised hosts.[^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell has the ability to copy files on a compromised host.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has the ability to upload files from a compromised host.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has collected data and files from a compromised host.[^1] [^2]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can collect data on a compromised host.[^1] [^2]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can use a file exfiltration tool to collect recently changed files on a compromised host.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae has the capability to upload collected files to C2.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can collect data and files from a compromised host.[^1]  |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout can collect sensitive NTLM material from a compromised host.[^1]  |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK has uploaded files from victims' machines.[^1]  |
| [[kb/mitre/attack/software/S0645-wevtutil\|S0645]] | Wevtutil | [[kb/mitre/attack/software/S0645-wevtutil\|Wevtutil]] can be used to export events from a specific log.[^2] [^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette has collected data and other information from a compromised host.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use a variety of commands, including esentutl.exe to steal sensitive data from Internet Explorer and Microsoft Edge, to acquire information that is subsequently exfiltrated.[^1] [^2]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon can upload files from a compromised host.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can upload data from the victim's machine to the C2 server.[^1]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has uploaded files from victims' machines.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET collects contacts and application data from files in Desktop, Documents, Downloads, Dropbox, and WeChat folders.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can collect information from a compromised host.[^1]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can retrieve configuration data from a compromised AD FS server.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can collect data from a compromised host.[^1] [^2]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect information and files from a compromised host.[^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can collect data and files from a compromised host.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can collect data from a compromised host.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can collect data from a local system.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla can upload files from a compromised host.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can collect data from a compromised host.[^1]  |
| [S0671](https://attack.mitre.org/software/S0671) | Tomiris | Tomiris has the ability to collect recent files matching a hardcoded list of extensions prior to exfiltration.[^1]  |
| [S0672](https://attack.mitre.org/software/S0672) | Zox | Zox has the ability to upload files from a targeted system.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can collect files from a compromised host.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can collect data and files from a compromised host.[^1]  |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve can collect files from a compromised host.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can upload files from a compromised host.[^1]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can collect data from a compromised host.[^1]  |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can upload files from a victim's machine.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can collect information from a compromised host.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can collect data from a compromised host, including Windows authentication information.[^1]  |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess has the ability to exfiltrate data, including Chrome and Edge browser database files, from compromised machines.[^1] <br> |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ can collect data from a compromised host.[^1]  |
| [S1014](https://attack.mitre.org/software/S1014) | DanBot | DanBot can upload files from compromised hosts.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can upload files from a compromised host.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can collect then exfiltrate files from the compromised system.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can collect information from a compromised host.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can collect files and information from a compromised host.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can upload files to its C2.[^2] [^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can upload logs and other data from a compromised host.[^1]  |
| [S1021](https://attack.mitre.org/software/S1021) | DnsSystem | DnsSystem can upload files from infected machines after receiving a command with `uploaddd` in the string.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | IceApple can collect files, passwords, and other data from a compromised host.[^1]  |
| [S1023](https://attack.mitre.org/software/S1023) | CreepyDrive | CreepyDrive can upload files to C2 from victim machines.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey can collect information from a compromised host.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall has the ability to upload files from victim's machines.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT can collect local data from an infected machine.[^1]  |
| [S1029](https://attack.mitre.org/software/S1029) | AuTo Stealer | AuTo Stealer can collect data such as PowerPoint files, Word documents, Excel files, PDF files, text files, database files, and image files from an infected machine.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can collect data from a compromised host.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can collect data from a compromised host.[^1]  |
| [S1037](https://attack.mitre.org/software/S1037) | STARWHALE | STARWHALE can collect data from an infected local host.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can capture and compress stolen credentials from the Registry and volume shadow copies.[^1]  |
| [S1043](https://attack.mitre.org/software/S1043) | ccf32 | ccf32 can collect files from a compromised host.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can upload files from victims' machines.[^2] [^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can collect files and information from a compromised host.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can collect files and system information from a compromised host.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can collect files and information from a compromised host.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | <br>[[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to upload files from a compromised system.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can collect data from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can collect information from a compromised host.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can gather information from compromised hosts.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to collect data from a compromised machine to deliver to the attacker.[^1]   |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco has dropped a recent-files stealer plugin to `C:\Users\Public\WinSrcNT\It11.exe`.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can use a file monitor to steal specific files from targeted systems.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can leverage an exfiltration module to download arbitrary files from compromised machines.[^1]  |
| [S1101](https://attack.mitre.org/software/S1101) | LoFiSe | LoFiSe can collect files of interest from targeted systems.[^1]  |
| [S1102](https://attack.mitre.org/software/S1102) | Pcexter | Pcexter can upload files from targeted systems.[^1]  |
| [S1110](https://attack.mitre.org/software/S1110) | SLIGHTPULSE | SLIGHTPULSE can read files specified on the local system.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate has stolen `sitemanager.xml` and `recentservers.xml` from `%APPDATA%\FileZilla\` if present.[^1]   |
| [S1113](https://attack.mitre.org/software/S1113) | RAPIDPULSE | RAPIDPULSE retrieves files from the victim system via encrypted commands sent to the web shell.[^1]  |
| [[kb/mitre/attack/software/S1131-nppspy\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] records data entered from the local system logon at Winlogon to capture credentials in cleartext.[^1]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper can identify specific files and folders for follow-on exfiltration.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for collecting files from local systems based on a given set of properties and filenames.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer collects data from victim machines based on configuration information received from command and control nodes.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can collect files from compromised hosts.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can gather data from infected systems.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can collect data from a compromised host using a stealer module.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer gathers information from infected systems such as SSH information from the victim's `.ssh` directory.[^2]  Troll Stealer collects information from local FileZilla installations and Microsoft Sticky Note.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can upload data and files to the LockBit victim-shaming site.[^2] [^1]  |
| [S1224](https://attack.mitre.org/software/S1224) | CASTLETAP | CASTLETAP can execute a C2 command to transfer files from victim machines.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can download files from the victim's computer.[^2] [^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has collected data stored locally including chat logs and files associated with chat services such as Steam, Discord, and Telegram.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has collected data utilizing a script that contained a list of excluded files and directory names and naming patterns of interest such as environment and configuration files, documents, spreadsheets, and other files that contained the words secret, wallet, private, and password.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has exfiltrated data collected from local systems.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has gathered data from home directories of the victim environment.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has collected local data from a compromised host to include desktop cryptocurrency wallet data, and documents from within Desktop, Documents, and Downloads.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has commands that allow the actor download files from the compromised host to the C2 server, and to also download specific sections of a file.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can upload files from infected hosts to the C2.[^2] [^1] [^3]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can upload files from the victim machine to C2 nodes.[^2] [^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has extracted the device’s Linux kernel image (vmlinux).[^1] [^2] [^3]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG has the ability to collect system information and files of interest from compromised systems.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1057-data-loss-prevention\|M1057]] | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |

 [^1]: [show_run_config_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733)
 [^2]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)
 [^3]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^4]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^5]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^6]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^7]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^8]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^9]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^10]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)
 [^11]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^12]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^13]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^14]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^15]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^16]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)
 [^17]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^18]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^19]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
 [^20]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)
 [^21]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
 [^22]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^23]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
 [^24]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^25]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^26]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
 [^27]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^28]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^29]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)
 [^30]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^31]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^32]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^33]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^34]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^35]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^36]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^37]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^38]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^39]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
 [^40]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^41]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^42]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^43]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^44]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^45]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^46]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^47]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^48]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^49]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^50]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^51]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^52]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^53]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^54]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
 [^55]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^56]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^57]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^58]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^59]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^60]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^61]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^62]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^63]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^64]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^65]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^66]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^67]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^68]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^69]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^70]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^71]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^72]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
 [^73]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^74]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^75]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
 [^76]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^77]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^78]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^79]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^80]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^81]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^82]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
 [^83]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^84]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^85]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^86]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^87]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^88]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^89]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^90]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^91]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^92]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
 [^93]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^94]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
 [^95]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^96]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^97]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
 [^98]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
 [^99]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^100]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^101]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^102]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^103]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^104]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^105]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^106]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^107]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^108]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^109]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^110]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^111]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^112]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
 [^113]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)
 [^114]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^115]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^116]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^117]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^118]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^119]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^120]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
 [^121]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^122]: [Kroll RawPOS Jan 2017](https://www.kroll.com/en/insights/publications/malware-analysis-report-rawpos-malware)
 [^123]: [TrendMicro RawPOS April 2015](http://sjc1-te-ftp.trendmicro.com/images/tex/pdf/RawPOS%20Technical%20Brief.pdf)
 [^124]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)
 [^125]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
 [^126]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
 [^127]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^128]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^129]: [F-Secure Lazarus Cryptocurrency Aug 2020](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)
 [^130]: [Wevtutil Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)
 [^131]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^132]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^133]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^134]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^135]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^136]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^137]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^138]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^139]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^140]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^141]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^142]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
 [^143]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^144]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^145]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^146]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^147]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^148]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^149]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^150]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^151]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^152]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^153]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^154]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^155]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^156]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^157]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
 [^158]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)
 [^159]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^160]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)
 [^161]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^162]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^163]: [Kaspersky APT Trends Q1 2020](https://securelist.com/apt-trends-report-q1-2020/96826/)
 [^164]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^165]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
 [^166]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^167]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^168]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^169]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^170]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^171]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^172]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^173]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^174]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^175]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^176]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^177]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^178]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
 [^179]: [Red Canary 2021 Threat Detection Report March 2021](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)
 [^180]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^181]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^182]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^183]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^184]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^185]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^186]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^187]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^188]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^189]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^190]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^191]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^192]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^193]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^194]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^195]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^196]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
