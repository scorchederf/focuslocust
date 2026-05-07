---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1105
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1105-ingress-tool-transfer
tactic:
    - Command And Control
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

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [[kb/mitre/attack/software/S0095-ftp|ftp]]. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [[kb/mitre/attack/techniques/T1570-lateral-tool-transfer|Lateral Tool Transfer]]). <br><br>On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [[kb/mitre/attack/software/S0160-certutil|certutil]], and [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] commands such as `IEX(New-Object Net.WebClient).downloadString()` and `Invoke-WebRequest`. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.[^5]   A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).[^2] <br><br>Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]] (typically after interacting with [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] lures).[^1] <br><br>Files can also be transferred using various [[kb/mitre/attack/techniques/T1102-web-service|Web Service]]s as well as native or otherwise present tools on the victim system.[^6]  In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0009](https://attack.mitre.org/software/S0009) | Hikit | Hikit has the ability to download files to a compromised host.[^1]  |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor has downloaded additional files onto a compromised host.[^1]  |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy creates a backdoor through which remote attackers can upload files.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module to download and execute files on the compromised machine.[^1] [^2] [^3] [^4]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe can download and execute additional files.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to download a file from the C2 server.[^1]  |
| [S0020](https://attack.mitre.org/software/S0020) | China Chopper | China Chopper's server component can download remote files.[^3] [^4] [^5] [^2] [^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use a `Put` command to write files to an infected machine.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK is capable of performing remote file transmission.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has a command to download and executes additional files.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT can download files to the victim’s machine.[^1] [^2]  |
| [S0042](https://attack.mitre.org/software/S0042) | LOWBALL | LOWBALL uses the Dropbox API to request two files, one of which is the same file as the one dropped by the malicious email attachment. This is most likely meant to be a mechanism to update the compromised host with a new version of the LOWBALL malware.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | JHUHUGIT can retrieve an additional payload from its C2 server.[^1] [^2]  JHUHUGIT has a command to download files to the victim’s machine.[^3]  |
| [S0051](https://attack.mitre.org/software/S0051) | MiniDuke | MiniDuke can download additional encrypted backdoors onto the victim via GIF files.[^2] [^1]  |
| [S0053](https://attack.mitre.org/software/S0053) | SeaDuke | SeaDuke is capable of uploading and downloading files.[^1]  |
| [S0054](https://attack.mitre.org/software/S0054) | CloudDuke | CloudDuke downloads and executes additional malware from either a Web address or a Microsoft OneDrive account.[^1]  |
| [S0055](https://attack.mitre.org/software/S0055) | RARSTONE | RARSTONE downloads its backdoor component from a C2 server and loads it directly into memory.[^1]  |
| [S0070](https://attack.mitre.org/software/S0070) | HTTPBrowser | HTTPBrowser is capable of writing a file to the compromised system from the C2 server.[^1]  |
| [S0074](https://attack.mitre.org/software/S0074) | Sakula | Sakula has the capability to download files.[^1]  |
| [S0077](https://attack.mitre.org/software/S0077) | CallMe | CallMe has the capability to download a file to the victim from the C2 server.[^1]  |
| [S0078](https://attack.mitre.org/software/S0078) | Psylo | Psylo has a command to download a file to the system from its C2 server.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder has a command to download a file from the C2 server to the victim mobile device's SD card.[^1]  |
| [S0080](https://attack.mitre.org/software/S0080) | Mivast | Mivast has the capability to download and execute .exe files.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | Elise can download additional files from the C2 server for execution.[^1]  |
| [S0082](https://attack.mitre.org/software/S0082) | Emissary | Emissary has the capability to download files from the C2 server.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat is capable of downloading files from the C2.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has downloaded additional malware and files onto a compromised host.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type can download additional files onto a compromised host.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has the ability to download files.[^1]  |
| [S0087](https://attack.mitre.org/software/S0087) | Hi-Zor | Hi-Zor has the ability to upload and download files from its C2 server.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to download and execute additional files.[^1]  |
| [S0092](https://attack.mitre.org/software/S0092) | Agent.btz | Agent.btz attempts to download an encrypted binary from a specified domain.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea can download additional modules from C2.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can upload, download, and execute files on the victim.[^1] [^2]  |
| [[kb/mitre/attack/software/S0095-ftp\|S0095]] | ftp | [[kb/mitre/attack/software/S0095-ftp\|ftp]] may be abused by adversaries to transfer tools or files from an external system into a compromised environment.[^1] [^2]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to copy files to/from a remotely connected external system.[^1]  |
| [S0109](https://attack.mitre.org/software/S0109) | WEBC2 | WEBC2 can download and execute a file.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to retrieve files from its C2 server.[^2] [^1] [^3]  |
| [S0118](https://attack.mitre.org/software/S0118) | Nidiran | Nidiran can download and execute files.[^1]  |
| [S0124](https://attack.mitre.org/software/S0124) | Pisloader | Pisloader has a command to upload a file to the victim machine.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec contains a network loader to receive executable modules from remote attackers and run them on the local victim. It can also upload and download files over HTTP and HTTPS.[^1] [^2]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS is capable of downloading additional files through C2 channels, including a new version of itself.[^1] [^2] [^3]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger is capable of downloading remote files.[^1]  |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 contains a command to download and execute a file from a remotely hosted URL using WinINet HTTP requests.[^1]  |
| [S0134](https://attack.mitre.org/software/S0134) | Downdelph | After downloading its main config file, Downdelph downloads multiple payloads from C2 servers.[^1]  |
| [S0137](https://attack.mitre.org/software/S0137) | CORESHELL | CORESHELL downloads another dropper from its C2 server.[^1]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has a command to download a file.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon can download an executable to run on the victim.[^1]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | The Winnti for Windows dropper can place malicious payloads on targeted systems.[^1]  |
| [S0144](https://attack.mitre.org/software/S0144) | ChChes | ChChes is capable of downloading files, including additional modules.[^2] [^3] [^1]  |
| [S0145](https://attack.mitre.org/software/S0145) | POWERSOURCE | POWERSOURCE has been observed being used to download TEXTMATE and the Cobalt Strike Beacon payload onto victims.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon can download and execute additional files.[^1] [^2] [^3]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can download additional files.[^1] [^2]  |
| [S0150](https://attack.mitre.org/software/S0150) | POSHSPY | POSHSPY downloads and executes additional PowerShell code and Windows binaries.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves is capable of downloading a file from a specified URL.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can deliver additional payloads to victim machines.[^1] [^2]  |
| [[kb/mitre/attack/software/S0160-certutil\|S0160]] | certutil | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to download files from a given URL.[^1] [^2]  |
| [S0164](https://attack.mitre.org/software/S0164) | TDTESS | TDTESS has a command to download and execute an additional file.[^1]  |
| [S0166](https://attack.mitre.org/software/S0166) | RemoteCMD | RemoteCMD copies a file over to the remote system before execution.[^1]  |
| [S0168](https://attack.mitre.org/software/S0168) | Gazer | Gazer can execute a task to download a file.[^1] [^2]  |
| [S0170](https://attack.mitre.org/software/S0170) | Helminth | Helminth can download additional files.[^1]  |
| [S0171](https://attack.mitre.org/software/S0171) | Felismus | Felismus can download files from remote servers.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can download remote files and additional payloads to the victim's machine.[^2] [^1] [^3]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER can download or upload files from its C2 server.[^1]  |
| [S0185](https://attack.mitre.org/software/S0185) | SEASHARPEE | SEASHARPEE can download remote files onto victims.[^1]  |
| [S0187](https://attack.mitre.org/software/S0187) | Daserf | Daserf can download remote files.[^1] [^2]  |
| [[kb/mitre/attack/software/S0190-bitsadmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to upload and/or download files.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can upload and download to/from a victim machine.[^1]  |
| [S0196](https://attack.mitre.org/software/S0196) | PUNCHBUGGY | PUNCHBUGGY can download additional files and payloads to compromised hosts.[^1] [^2]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can downloaded payloads from C2 to the compromised host.[^1] [^2]  |
| [S0199](https://attack.mitre.org/software/S0199) | TURNEDUP | TURNEDUP is capable of downloading additional files.[^1]  |
| [S0200](https://attack.mitre.org/software/S0200) | Dipsind | Dipsind can download remote files.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can download files and upgrade itself.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can download files and additional malware components.[^1] [^2]  |
| [S0204](https://attack.mitre.org/software/S0204) | Briba | Briba downloads files onto infected hosts.[^1]  |
| [S0206](https://attack.mitre.org/software/S0206) | Wiarp | Wiarp creates a backdoor through which remote attackers can download files.[^1]  |
| [S0207](https://attack.mitre.org/software/S0207) | Vasport | Vasport can download files.[^1]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can upload files.[^1]  |
| [S0210](https://attack.mitre.org/software/S0210) | Nerex | Nerex creates a backdoor through which remote attackers can download files onto a compromised host.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can download files onto compromised hosts.[^1]  |
| [S0213](https://attack.mitre.org/software/S0213) | DOGCALL | DOGCALL can download and execute additional payloads.[^1]  |
| [S0214](https://attack.mitre.org/software/S0214) | HAPPYWORK | can download and execute a second-stage payload.[^1]  |
| [S0215](https://attack.mitre.org/software/S0215) | KARAE | KARAE can upload and download files, including second-stage malware.[^1]  |
| [S0217](https://attack.mitre.org/software/S0217) | SHUTTERSPEED | SHUTTERSPEED can download and execute an arbitary executable.[^1]  |
| [S0218](https://attack.mitre.org/software/S0218) | SLOWDRIFT | SLOWDRIFT downloads additional payloads.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can retrieve and execute additional [[kb/mitre/attack/techniques/T1059.001-powershell\|PowerShell]] payloads from the C2 server.[^1]  |
| [S0226](https://attack.mitre.org/software/S0226) | Smoke Loader | Smoke Loader downloads a new version of itself once it has installed. It also downloads additional plugins.[^1]  |
| [S0228](https://attack.mitre.org/software/S0228) | NanHaiShu | NanHaiShu can download additional files from URLs.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can download files onto the victim.[^1]  |
| [S0230](https://attack.mitre.org/software/S0230) | ZeroT | ZeroT can download additional payloads onto the victim.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can download files to the system.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs downloads additional files from C2 servers.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot uploads files and secondary payloads to the victim's machine.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can retrieve additional malicious payloads from its C2 server.[^1] [^2] [^3] [^4]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA uploads and downloads information.[^1] [^2]  |
| [S0247](https://attack.mitre.org/software/S0247) | NavRAT | NavRAT can download files remotely.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon can download additional components from the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can download additional files and tools.[^2] [^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy obtains additional code to execute on the victim's machine, including the downloading of a secondary payload.[^1] [^2] [^3] [^4]  |
| [S0254](https://attack.mitre.org/software/S0254) | PLAINTEE | PLAINTEE has downloaded and executed additional plugins.[^1]  |
| [S0255](https://attack.mitre.org/software/S0255) | DDKONG | DDKONG downloads and uploads files on the victim’s machine.[^1]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito can upload and download files to the victim.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN can download and upload files to the victim's machine.[^1]  |
| [S0258](https://attack.mitre.org/software/S0258) | RGDoor | RGDoor uploads and downloads files to and from the victim’s machine.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can upload files to the victim's machine for operations.[^1] [^2]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can download files to the victim’s machine and execute them.[^1] [^2]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | TYPEFRAME can upload and download files to the victim’s machine.[^1]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE can download files from its C2 server to the victim's machine.[^1] [^2]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar downloads additional plug-ins to load on the victim’s machine, including the ability to upgrade and replace its own binary.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot downloads several additional files and saves them to the victim's machine.[^1] [^2]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT downloads and uploads files to and from the victim’s machine.[^2] [^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has the capability to download files to execute on the victim’s machine.[^1] [^2] [^3]   |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin can save a new file to the system from the C2 server.[^1] [^2]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE can upload files to the victim’s machine and can download additional payloads.[^1]  |
| [S0272](https://attack.mitre.org/software/S0272) | NDiskMonitor | NDiskMonitor can download and execute a file from given URL.[^1]  |
| [S0274](https://attack.mitre.org/software/S0274) | Calisto | Calisto has the capability to upload and download files to the victim's machine.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT can download and upload files to and from the victim’s machine.[^3] [^2] [^1] <br> |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can download and execute files.[^1] [^2] [^3]  |
| [S0284](https://attack.mitre.org/software/S0284) | More_eggs | More_eggs can download and launch additional payloads.[^1] [^2]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda can download additional malware plug-in modules and execute them on the victim’s machine.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can download additional files for execution on the victim’s machine.[^1] [^2]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can upload and download files to and from the victim’s machine.[^1] [^2]  |
| [S0333](https://attack.mitre.org/software/S0333) | UBoatRAT | UBoatRAT can upload and download files to the victim’s machine.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can load any files onto the infected machine to execute.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore has the capability to download and activate additional modules for execution.[^1] [^2]  |
| [S0337](https://attack.mitre.org/software/S0337) | BadPatch | BadPatch can download and execute or update malware.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia can download and execute an executable from the C2 server.[^1] [^2]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can download additional files and tools onto the victim’s machine.[^1] [^2] [^3]  |
| [S0341](https://attack.mitre.org/software/S0341) | Xbash | Xbash can download additional malicious files from its C2 server.[^1]  |
| [S0342](https://attack.mitre.org/software/S0342) | GreyEnergy | GreyEnergy can download additional modules and payloads.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can download and execute additional files. Azorult has also downloaded a ransomware payload called Hermes.[^1] [^2]  |
| [S0345](https://attack.mitre.org/software/S0345) | Seasalt | Seasalt has a command to download additional files.[^1] [^1]  |
| [S0347](https://attack.mitre.org/software/S0347) | AuditCred | AuditCred can download files and additional malware.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can download and execute additional payloads.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can download a payload for execution.[^1]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has a command to download and execute a file on the victim’s machine.[^1] [^2]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI has downloaded a remote module for execution.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis deploys additional backdoors and hacking tools to the system.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can download files and execute them on the victim’s machine.[^1] [^2]   |
| [S0360](https://attack.mitre.org/software/S0360) | BONDUPDATER | BONDUPDATER can download or upload files from its C2 server.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can upload and download to and from a victim machine.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet can download follow-on payloads and items via malicious `url` parameters in obfuscated PowerShell code.[^1]  |
| [S0369](https://attack.mitre.org/software/S0369) | CoinTicker | CoinTicker executes a Python script to download its second stage.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth uses [[kb/mitre/attack/software/S0160-certutil\|certutil]] and [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] to download additional malware. [^1] [^3] [^2]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp downloads and executes additional files from a remote server. [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has the ability to connect to a remote host in order to upload and download files.[^1] 	 |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT has the ability to upload and download files.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has downloaded and dropped temporary files containing scripts; it additionally has a function to upload files from the victims machine.[^1] 	 |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy can transfer files from C2.[^1]  |
| [S0382](https://attack.mitre.org/software/S0382) | ServHelper | ServHelper may download additional files to execute.[^1] [^2]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can download files to the victim’s machine.[^1] [^3]  APT-C-36 has used modified versions of njRAT to enable the download of .NET assemblies.[^2]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has dropped payload and configuration files to disk. Ursnif has also been used to download and execute additional payloads.[^1] [^2]  |
| [S0387](https://attack.mitre.org/software/S0387) | KeyBoy | KeyBoy has a download and upload functionality.[^2] [^1]  |
| [S0388](https://attack.mitre.org/software/S0388) | YAHOYAH | YAHOYAH uses HTTP GET requests to download other files that are executed in memory.[^1]  |
| [S0390](https://attack.mitre.org/software/S0390) | SQLRat | SQLRat can make a direct SQL connection to a Microsoft database controlled by the attackers, retrieve an item from the bindata table, then write and execute the file on disk.[^1] 	 |
| [S0394](https://attack.mitre.org/software/S0394) | HiddenWasp | HiddenWasp downloads a tar compressed archive from a download server to the system.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron has the ability to download and execute additional files.[^1]  |
| [S0396](https://attack.mitre.org/software/S0396) | EvilBunny | EvilBunny has downloaded additional Lua scripts from the C2.[^1]  |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro has the ability to download additional files.[^1]  |
| [S0401](https://attack.mitre.org/software/S0401) | Exaramel for Linux | Exaramel for Linux has a command to download a file from  and to a remote C2 server.[^1] [^2]  |
| [S0402](https://attack.mitre.org/software/S0402) | OSX/Shlayer | OSX/Shlayer can download payloads, and extract bytes from files. OSX/Shlayer uses the `curl -fsL "$url" >$tmp_path` command to download malicious payloads into a temporary directory.[^1] [^3] [^4] [^2]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files from a given URL.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete |  Machete can download additional files for execution on the victim’s machine.[^1]   |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell has a command to transfer files from a remote host.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has downloaded additional files from the C2.[^1] [^2]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has the ability to copy files and download/upload files into C2 channels using FTP and HTTPS.[^1] [^2]  |
| [S0430](https://attack.mitre.org/software/S0430) | Winnti for Linux | Winnti for Linux has the ability to deploy modules directly from command and control (C2) servers, possibly for remote command execution, file exfiltration, and socks5 proxying on the infected host. [^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to upload a file from the command and control (C2) server to the victim machine.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to upload and download files to and from an infected host.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to upload and download files to and from the infected host.[^1]  |
| [S0437](https://attack.mitre.org/software/S0437) | Kivars | Kivars has the ability to download and execute files.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor can download additional plugins, updates and other files. [^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum has built-in commands for uploading, downloading, and executing files to the system.[^1]  |
| [S0442](https://attack.mitre.org/software/S0442) | VBShower | VBShower has the ability to download VBS files to the target computer.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat can download additional files.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] had the ability to download additional payloads.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot downloaded several staged items onto the victim's machine.[^1]   |
| [S0450](https://attack.mitre.org/software/S0450) | SHARPSTATS | SHARPSTATS has the ability to upload and download files.[^1]  |
| [S0451](https://attack.mitre.org/software/S0451) | LoudMiner | LoudMiner used SCP to update the miner from the C2.[^1]  |
| [S0453](https://attack.mitre.org/software/S0453) | Pony | Pony can download additional files onto the infected system.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has used MSI files to download additional files to execute.[^1] [^2] [^3] [^4]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to download additional payloads from C2.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Operators deploying Netwalker have used psexec and certutil to retrieve the Netwalker payload.[^1]  |
| [S0459](https://attack.mitre.org/software/S0459) | MechaFlounder | MechaFlounder has the ability to upload and download files to and from a compromised host.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to download a DLL from C2 to a compromised host.[^1]  |
| [S0462](https://attack.mitre.org/software/S0462) | CARROTBAT | CARROTBAT has the ability to download and execute a remote file via [[kb/mitre/attack/software/S0160-certutil\|certutil]].[^1]  |
| [[kb/mitre/attack/software/S0465-carrotball\|S0465]] | CARROTBALL | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has the ability to download and install a remote payload.[^1]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has the ability to download files on an infected host.[^1]   |
| [S0469](https://attack.mitre.org/software/S0469) | ABK | ABK has the ability to download files from C2.[^1]  |
| [S0470](https://attack.mitre.org/software/S0470) | BBK | BBK has the ability to download files from C2 to the infected host.[^1]  |
| [S0471](https://attack.mitre.org/software/S0471) | build_downer | build_downer has the ability to download files from C2 to the infected host.[^1]  |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to download files to the compromised host.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to download files from C2 to a compromised host.[^1]  |
| [S0475](https://attack.mitre.org/software/S0475) | BackConfig | BackConfig can download and execute additional payloads on a compromised host.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has downloaded a variety of modules and payloads to the compromised host, including IcedID and NetSupport Manager RAT-based malware.[^1] [^2]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore can download and execute new versions of itself.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has the ability to download additional modules and a configuration file from C2.[^2] [^3] [^1] [^4]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp can download and execute new plugins from the C2 server. [^1] [^2]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan can download additional modules from the C2 server.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel can download additional modules from the C2 server.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can download files to specified targets.[^1]  |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner can download additional scripts from a web server.[^1]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy constantly attempts to download and execute files from the remote C2, including GoldenSpy itself if not found on the system.[^1] 	 |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT can download files via DNS.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can download a copy of itself from an attacker controlled IP address to the victim machine.[^1] [^2] [^3]  |
| [S0497](https://attack.mitre.org/software/S0497) | Dacls | Dacls can download its payload from a C2 server.[^1] [^2]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic has the ability to send and receive files.[^1]  |
| [S0499](https://attack.mitre.org/software/S0499) | Hancitor | Hancitor has the ability to download additional files from C2.[^1]  |
| [[kb/mitre/attack/software/S0500-mcmd\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can upload additional files to a compromised host.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can install additional modules via C2 commands.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub can download files to a compromised host.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor can download additional payloads.[^1] [^2]  |
| [S0511](https://attack.mitre.org/software/S0511) | RegDuke | RegDuke can download files from C2.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke has the ability to download files.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can write files to a compromised host.[^1] [^2]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can receive data and executable scripts from C2.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can download additional payloads from C2.[^1] [^2]  |
| [S0518](https://attack.mitre.org/software/S0518) | PolyglotDuke | PolyglotDuke can retrieve payloads from the C2 server.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has downloaded files to a victim machine.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY has the ability to download and execute code from remote servers.[^1]  |
| [[kb/mitre/attack/software/S0527-cspy-downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can download additional tools to a compromised host.[^1]  |
| [S0528](https://attack.mitre.org/software/S0528) | Javali | Javali can download payloads from remote C2 servers.[^1]  |
| [S0530](https://attack.mitre.org/software/S0530) | Melcoz | Melcoz has the ability to download additional files to a compromised host.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can download its second stage from a hardcoded URL within the loader's code.[^1] [^2]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can download and execute a replica of itself using [[kb/mitre/attack/software/S0160-certutil\|certutil]].[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has downloaded files onto a victim machine.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can download and deploy additional payloads, including ransomware and post-exploitation frameworks such as Cobalt Strike.[^1] [^2] [^3] [^4]  |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage has the ability to download and execute additional payloads via a DropBox API.[^1] [^2]  |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook can download and execute additional files.[^1] [^2]  |
| [S0553](https://attack.mitre.org/software/S0553) | MoleNet | MoleNet can download additional payloads from the C2.[^1]   |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has the ability to download files from its C2 server.[^1] [^2]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST delivered different payloads, including TEARDROP in at least one instance.[^1]  |
| [S0561](https://attack.mitre.org/software/S0561) | GuLoader | GuLoader can download further malware for execution on the victim's machine.[^1]  |
| [S0564](https://attack.mitre.org/software/S0564) | BlackMould | BlackMould has the ability to download files to the victim's machine.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack’s can download and upload a file to the victim’s computer.[^1] [^2]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can download and upload files to the victim's computer.[^2] [^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has a function to download a file to the infected system.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a module to download and upload files to the system.[^1]   |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear is designed to download an implant from a C2 server.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can receive and load executables from remote C2 servers.[^1]  |
| [S0585](https://attack.mitre.org/software/S0585) | Kerrdown | Kerrdown can download specific payloads to a compromised host based on OS architecture.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can download additional modules from its C2 server.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can execute the command code `do_download` to retrieve remote files from C2.[^1]  |
| [S0588](https://attack.mitre.org/software/S0588) | GoldMax | GoldMax can download and execute additional files.[^1] [^2]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot can download and execute a payload onto a compromised system.[^1]  |
| [[kb/mitre/attack/software/S0592-remoteutilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can upload and download files to and from a target machine.[^1]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest can download and execute payloads in-memory or from disk.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has downloaded code from a C2 server.[^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell can upload and download files to and from compromised hosts.[^1]  |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing has downloaded additional lateral movement scripts from C2.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has downloaded scripts from C2.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has downloaded additional scripts that build and run Monero cryptocurrency miners.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer downloads a shellcode payload from a remote C2 server and loads it into memory.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker downloads an HTTP server to the infected machine.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has the ability to download additional files.[^1]  |
| [S0613](https://attack.mitre.org/software/S0613) | PS1 | CostaBricks can download additional payloads onto a compromised host.[^1]  |
| [S0614](https://attack.mitre.org/software/S0614) | CostaBricks | CostaBricks has been used to load SombRAT onto a compromised host.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has the ability to download and execute additional payloads.[^1] [^2] [^3]  |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM can download files to a compromised host.[^1]  |
| [S0624](https://attack.mitre.org/software/S0624) | Ecipekac | Ecipekac can download additional payloads to a compromised host.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can download files from its C2 server.[^1]  |
| [S0626](https://attack.mitre.org/software/S0626) | P8RAT | P8RAT can download additional payloads to a target system.[^1]  |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster has the ability to download additional payloads from C2 to the targeted system.[^1]  |
| [S0628](https://attack.mitre.org/software/S0628) | FYAnti | FYAnti can download additional payloads to a compromised host.[^1] 	  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can download files to a compromised host.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae can download files from C2.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes can download additional files onto an infected machine.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent has the ability to download and execute additional payloads.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can download additional content and files from the [[kb/mitre/attack/software/S0633-sliver\|Sliver]] server to the client residing on the victim machine using the `upload` command.[^1] [^2]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox has the ability to download next stage malware components to a compromised system.[^1]  |
| [S0636](https://attack.mitre.org/software/S0636) | VaporRage | VaporRage has the ability to download malicious shellcode to compromised systems.[^1]  |
| [S0639](https://attack.mitre.org/software/S0639) | Seth-Locker | Seth-Locker has the ability to download and execute files on a compromised host.[^1]  |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK has download files from its C2 server.[^1]  |
| [S0643](https://attack.mitre.org/software/S0643) | Peppy | Peppy can download and execute remote files.[^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette can download malicious files from threat actor controlled AWS URL's.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can download additional files and tools from its C2.[^1]  |
| [S0648](https://attack.mitre.org/software/S0648) | JSS Loader | JSS Loader has the ability to download malicious executables to a compromised host.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has used Powershell to download UltraVNC and [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] from third-party file sharing sites.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to download additional components and malware.[^5] [^1] [^6] [^2] [^4] [^3]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon can download files.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can download additional files and tools from its C2 server, including through the use of [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]].[^1]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has a command to download files to the victim's machine.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can download additional files onto the host.[^1]   |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET downloads browser specific AppleScript modules using a constructed URL with the `curl` command, ` & domain & "/agent/scripts/" & moduleName & ".applescript`.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can receive configuration updates and additional payloads including wscpy.exe from C2.[^1]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can receive additional malicious components from an actor controlled C2 server and execute them on a compromised AD FS server.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession has the ability to drop additional files to an infected machine.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate has the ability to download files to a compromised host.[^2] [^1]  |
| [S0664](https://attack.mitre.org/software/S0664) | Pandora | Pandora can load additional drivers and files onto a victim machine.[^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can download additional tools to enable lateral movement.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can download additional plug-ins to a compromised host.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can download its code from C2.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla has the ability to act as a second-stage dropper used to infect the system with additional malware.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS has executed a PowerShell command to download a file to the system.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can download and execute additional files.[^1]  |
| [S0671](https://attack.mitre.org/software/S0671) | Tomiris | Tomiris can download files and execute them on a victim's system.[^1]  |
| [S0672](https://attack.mitre.org/software/S0672) | Zox | Zox can download files to a compromised machine.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower has the ability to download additional modules to a compromised host.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower has the ability to download payloads containing system commands to a compromised host.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can download additional plugins, files, and tools.[^1] [^2] [^3]  |
| [S0685](https://attack.mitre.org/software/S0685) | PowerPunch | PowerPunch can download payloads from adversary infrastructure.[^1]  |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve can download and execute payloads on a target host.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink has the ability to download files to target systems.[^2] [^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor has the ability to download additional files for execution on the victim's machine.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can download additional stages of malware from a Discord CDN channel.[^3] [^2] [^1] [^4]  |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can download additional files onto a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can load additional files and tools, including [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]].[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can deploy additional tools onto an infected machine.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] can download and execute previously staged shellcode payloads.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can download additional malware from the C2 server.[^1]  |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess can download additional payloads to a compromised host.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ can download and execute additional files.[^1]  |
| [S1014](https://attack.mitre.org/software/S1014) | DanBot | DanBot can download additional files to a targeted system.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan has received files from C2 and stored them in log folders beginning with the character sequence `a9850d2f`.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has downloaded additional files, including an exploit for used privilege escalation.[^1] [^2]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can download files from its C2 server.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can download additional files onto a compromised host.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark  can download additional files from its C2 via HTTP or DNS.[^2] [^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can download files to the compromised host.[^1]  |
| [S1021](https://attack.mitre.org/software/S1021) | DnsSystem | DnsSystem can download files to compromised systems after receiving a command with the string `downloaddd`.[^1]  |
| [S1023](https://attack.mitre.org/software/S1023) | CreepyDrive | CreepyDrive can download files to the compromised host.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey can download and execute files to further infect a host machine with additional malware.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall can download files to targeted systems.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT has the ability to download additional payloads onto an infected machine.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has downloaded and executed additional encoded payloads.[^1] [^2]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can download updates and auxiliary modules.[^1]  |
| [S1035](https://attack.mitre.org/software/S1035) | Small Sieve | Small Sieve has the ability to download files.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can download and execute additional payloads including through the use of a `Dex` command.[^3] [^2] [^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can download additional files onto a compromised host.[^1]  |
| [S1048](https://attack.mitre.org/software/S1048) | macOS.OSAMiner | macOS.OSAMiner has used `curl` to download a [[kb/mitre/attack/techniques/T1027.008-stripped-payloads\|Stripped Payloads]] from a public facing adversary-controlled webpage.  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can download files onto compromised systems.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can download additional files onto the compromised host.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | <br>[[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can download files to compromised hosts.[^2] [^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady has the ability to download additional tools such as the RedLine Stealer to an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can download files from its C2 server, including the .NET DLLs, `WoodySharpExecutor` and `WoodyPowerSession`.[^1]   |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can download additional packages for keylogging, cryptocurrency mining, and other capabilities; it can also retrieve malicious payloads such as Agent Tesla, AsyncRat, NanoCore, RedLine, Cobalt Strike, and Metasploit.[^1]  |
| [S1074](https://attack.mitre.org/software/S1074) | ANDROMEDA | ANDROMEDA can download additional payloads from C2.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH has the ability to load a second stage malicious DLL file onto a compromised machine.[^1]   |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to upload additional malicious files to a compromised machine.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 can download additional payloads to compromised systems.[^2] [^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to download files including over SFTP.[^2] [^1]  |
| [S1088](https://attack.mitre.org/software/S1088) | Disco | Disco can download files to targeted systems via SMB.[^1]  |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco has been used to download a Python interpreter to `C:\Users\Public\WinTN\WinTN.exe` as well as other plugins from external sources.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can load multiple additional plugins on an infected host.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai has been used to deploy other malware including Ninja.[^1]  |
| [S1110](https://attack.mitre.org/software/S1110) | SLIGHTPULSE | RAPIDPULSE can transfer files to and from compromised hosts.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate retrieves cryptocurrency mining payloads and commands in encrypted traffic from its command and control server.[^1]  DarkGate uses Windows Batch scripts executing the `curl` command to retrieve follow-on payloads.[^2]  DarkGate has stolen `sitemanager.xml` and `recentservers.xml` from `%APPDATA%\FileZilla\` if present.[^3]   |
| [S1112](https://attack.mitre.org/software/S1112) | STEADYPULSE | STEADYPULSE can add lines to a Perl script on a targeted server to import additional Perl modules.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can download files to be saved on the compromised system.[^2] [^1]  |
| [S1115](https://attack.mitre.org/software/S1115) | WIREFIRE | WIREFIRE has the ability to download files to compromised devices.[^1]  |
| [S1118](https://attack.mitre.org/software/S1118) | BUSHWALK | BUSHWALK can write malicious payloads sent through a web request’s command parameter.[^2] [^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can download additional malware to infected hosts.[^1] [^2]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin retrieves its second stage payload in a variety of ways such as through msiexec.exe abuse, or running the curl command to download the payload to the victim's `%AppData%` folder.[^2] [^1]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | Gootloader can fetch second stage code from hardcoded web domains.[^2] [^1]  |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Spica can upload and download files to and from compromised hosts.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer downloads various library files enabling interaction with various data stores and structures to facilitate follow-on information theft.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can download additional files from C2.[^1]  |
| [S1152](https://attack.mitre.org/software/S1152) | IMAPLoader | IMAPLoader is a loader used to retrieve follow-on payload encoded in email messages for execution on victim systems.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can retrieve and load additional payloads.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can download and execute PEs, DLLs, and shellcode from C2.[^2] [^3] [^1]  |
| [S1166](https://attack.mitre.org/software/S1166) | Solar | Solar has the ability to download and execute files.[^1]  |
| [S1168](https://attack.mitre.org/software/S1168) | SampleCheck5000 | SampleCheck5000 can download additional payloads to compromised hosts.[^2] [^1]  |
| [S1170](https://attack.mitre.org/software/S1170) | ODAgent | ODAgent has the ability to download and execute files on compromised systems.[^1]  |
| [S1171](https://attack.mitre.org/software/S1171) | OilCheck | OilCheck can download staged payloads from an actor-controlled infrastructure.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can download and execute files from an actor-controlled OneDrive account.[^1]  |
| [S1173](https://attack.mitre.org/software/S1173) | PowerExchange | PowerExchange can decode Base64-encoded files and call `WriteAllBytes` to write the files to compromised hosts.[^1]  |
| [S1182](https://attack.mitre.org/software/S1182) | MagicRAT | MagicRAT can import and execute additional payloads.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer installers have used obfuscated PowerShell scripts to retrieve follow-on payloads from WebDAV servers.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | On macOS, LightSpy downloads a `.json` file from the C2 server. The `.json` file contains metadata about the plugins to be downloaded, including their URL, name, version, and MD5 hash. LightSpy retrieves the plugins specified in the `.json` file, which are compiled `.dylib` files. These `.dylib` files provide task and platform specific functionality. LightSpy also imports open-source libraries to manage socket connections.[^1]  |
| [S1187](https://attack.mitre.org/software/S1187) | reGeorg | reGeorg has the ability to download files to targeted systems.[^1]  |
| [S1189](https://attack.mitre.org/software/S1189) | Neo-reGeorg | Neo-reGeorg has the ability to download files to targeted systems.[^1]  |
| [S1192](https://attack.mitre.org/software/S1192) | NICECURL | NICECURL has the ability to download additional content onto an infected machine, e.g. by using `curl`.[^1]   |
| [S1193](https://attack.mitre.org/software/S1193) | TAMECAT | TAMECAT has used `wget` and `curl` to download additional content.[^1]   |
| [S1211](https://attack.mitre.org/software/S1211) | Hannotog | Hannotog can download additional files to the victim machine.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA has the ability to upload and download files.[^1]  |
| [S1222](https://attack.mitre.org/software/S1222) | RIFLESPINE | RIFLESPINE can download and execute files.[^1]  |
| [S1224](https://attack.mitre.org/software/S1224) | CASTLETAP | CASTLETAP can transfer files to compromised network devices.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has acted as a stager that can download the next-stage payload from its C2 server.[^1] [^2] [^3] [^5] [^6]  PUBLOAD has also delivered FDMTP as a secondary control tool and PTSOCKET for exfiltration to some infected systems.[^4]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc has the ability to upload files to infected systems.[^2] [^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has the ability to download additional files to the victim device.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has the ability download additional payloads.[^1] [^2]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has downloaded “AnyDesk.exe” into the user’s home directory from the C2 server when checks for the service fail to identify its presence in the victim environment.[^1]  InvisibleFerret has also been configured to download additional payloads using a command which calls to the /bow URI.[^2] [^3]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has been used to download a malicious payload to include Python based malware InvisibleFerret.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader has been used to download a malicious payload to include BeaverTail.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has been used to download a malicious payload to include BeaverTail.[^1] [^2] [^3]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has downloaded additional files for execution on the victim’s machine.[^1] [^2]  The server component of SystemBC has the ability to send additional files to victim machines.[^2]  |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has the ability to download files from C2 using the `down <FILENAME>` command.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has downloaded packages from code repositories.[^1] [^3] [^5] [^6]  Shai-Hulud has also downloaded and executed the secrets-discovery tool [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] to gather sensitive data.[^2] [^3] [^4] [^5] [^6]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has downloaded additional payloads from C2.[^1] [^2] [^3] [^4]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has the ability to upload files onto the compromised appliance.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has the ability to download files from the Adversaries C2 server to the compromised system.[^1] [^2] [^3] [^4]  |
| [S9016](https://attack.mitre.org/software/S9016) | Caminho | Caminho has the ability to download files onto compromised hosts.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can download additional payloads for execution on the compromised host.[^2] [^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO has the ability to download additional files from the C2.[^2] [^1] [^3]  |
| [S9021](https://attack.mitre.org/software/S9021) | DOWNIISSA | DOWNIISSA can download files to the compromised host.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can download files from the C2 to victim systems.[^2] [^1]  |
| [S9028](https://attack.mitre.org/software/S9028) | PHPsert | PHPsert has the ability to retrieve remote payloads.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag stager component can retrieve and execute the main payload.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has the ability to download files from the C2 server. Additionally, MuddyViper has the ability to download a file in chunks with sleep time between each chunk.[^1]       |
| [S9034](https://attack.mitre.org/software/S9034) | Tsundere Botnet | Tsundere Botnet’s loader component has downloaded the zip file node-v18.17.0-win-x64.zip from the official Node.js website, as well as pm2, a Node.js process management tool.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools.[^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Use network filtering to block outbound traffic from compromised systems to unapproved external destinations. Restricting access to known, trusted IP addresses and protocols can prevent attackers from downloading malicious tools or payloads onto compromised servers after gaining initial access. |

 [^1]: [T1105: Trellix_search-ms](https://www.trellix.com/blogs/research/beyond-file-search-a-novel-method/)
 [^2]: [Google Cloud Threat Intelligence COSCMICENERGY 2023](https://cloud.google.com/blog/topics/threat-intelligence/cosmicenergy-ot-malware-russian-response/)
 [^3]: [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)
 [^4]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^5]: [t1105_lolbas](https://lolbas-project.github.io/#t1105)
 [^6]: [PTSecurity Cobalt Dec 2016](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)
 [^7]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
 [^8]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^9]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^10]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
 [^11]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
 [^12]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^13]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^14]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^15]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
 [^16]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^17]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^18]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^19]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^20]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
 [^21]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^22]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
 [^23]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
 [^24]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
 [^25]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^26]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^27]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^28]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)
 [^29]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^30]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^31]: [TrendMicro PE_URSNIF.A2](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279)
 [^32]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^33]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)
 [^34]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
 [^35]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^36]: [Symantec Vasport May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-5938-99)
 [^37]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^38]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^39]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^40]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)
 [^41]: [Symantec Ristol May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3909-99)
 [^42]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^43]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^44]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^45]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^46]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^47]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
 [^48]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^49]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)
 [^50]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^51]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
 [^52]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^53]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^54]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^55]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
 [^56]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^57]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)
 [^58]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^59]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^60]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)
 [^61]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^62]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
 [^63]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
 [^64]: [Fidelis INOCNATION](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)
 [^65]: [Unit42 BabyShark Apr 2019](https://unit42.paloaltonetworks.com/babyshark-malware-part-two-attacks-continue-using-kimjongrat-and-pcrat/)
 [^66]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
 [^67]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)
 [^68]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
 [^69]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^70]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
 [^71]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^72]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^73]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^74]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^75]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)
 [^76]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^77]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^78]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^79]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^80]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^81]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
 [^82]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^83]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^84]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^85]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
 [^86]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^87]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^88]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^89]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^90]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)
 [^91]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
 [^92]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
 [^93]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^94]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^95]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^96]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^97]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
 [^98]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^99]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^100]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^101]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^102]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
 [^103]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^104]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)
 [^105]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
 [^106]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^107]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^108]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^109]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^110]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
 [^111]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^112]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^113]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^114]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
 [^115]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^116]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
 [^117]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^118]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
 [^119]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^120]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^121]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^122]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^123]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
 [^124]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^125]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^126]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)
 [^127]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^128]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
 [^129]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)
 [^130]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^131]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^132]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^133]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^134]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^135]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
 [^136]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)
 [^137]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
 [^138]: [Symantec Briba May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)
 [^139]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^140]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
 [^141]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^142]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^143]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^144]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^145]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^146]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^147]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
 [^148]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^149]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^150]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
 [^151]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^152]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^153]: [Symantec Calisto July 2018](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)
 [^154]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
 [^155]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^156]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^157]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^158]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^159]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^160]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
 [^161]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)
 [^162]: [Symantec Backdoor.Nidiran](https://www.symantec.com/security_response/writeup.jsp?docid=2015-120123-5521-99)
 [^163]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)
 [^164]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^165]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^166]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^167]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^168]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^169]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
 [^170]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
 [^171]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^172]: [Socket Shai-Hulud Trufflehog September 2025](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)
 [^173]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^174]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^175]: [Symantec Dyre June 2015](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)
 [^176]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^177]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^178]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^179]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^180]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^181]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^182]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^183]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
 [^184]: [Malwarebytes SmokeLoader 2016](https://blog.malwarebytes.com/threat-analysis/2016/08/smoke-loader-downloader-with-a-smokescreen-still-alive/)
 [^185]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^186]: [Aquino RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/rarstone-found-in-targeted-attacks/)
 [^187]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^188]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
 [^189]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^190]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^191]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^192]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
 [^193]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
 [^194]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^195]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
 [^196]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)
 [^197]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^198]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
 [^199]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^200]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^201]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^202]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^203]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^204]: [Unit 42 SeaDuke 2015](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)
 [^205]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)
 [^206]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^207]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^208]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
 [^209]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
 [^210]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^211]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^212]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
 [^213]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^214]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^215]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
 [^216]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
 [^217]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^218]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^219]: [Pincus Emotet 2020](https://medium.com/picus-security/an-analysis-of-emotet-malware-powershell-unobfuscation-4f46b50dcf2b)
 [^220]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^221]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^222]: [sentinelone operationDigitalEye Dec 2024](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
 [^223]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^224]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^225]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
 [^226]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^227]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
 [^228]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^229]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^230]: [Securelist MiniDuke Feb 2013](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)
 [^231]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^232]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^233]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^234]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^235]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^236]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
 [^237]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^238]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
 [^239]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^240]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
 [^241]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^242]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
 [^243]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^244]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
 [^245]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^246]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^247]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^248]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^249]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)
 [^250]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^251]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^252]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^253]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^254]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^255]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^256]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^257]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
 [^258]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^259]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
 [^260]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)
 [^261]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)
 [^262]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)
 [^263]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^264]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
 [^265]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^266]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^267]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^268]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^269]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^270]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^271]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^272]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^273]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
 [^274]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
 [^275]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
 [^276]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^277]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^278]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^279]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^280]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^281]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^282]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
 [^283]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^284]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)
 [^285]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^286]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^287]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)
 [^288]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
 [^289]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^290]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^291]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
 [^292]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
 [^293]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^294]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^295]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)
 [^296]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
 [^297]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^298]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^299]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^300]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^301]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)
 [^302]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)
 [^303]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
 [^304]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)
 [^305]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^306]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^307]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^308]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
 [^309]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^310]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^311]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
 [^312]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
 [^313]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^314]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^315]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^316]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^317]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
 [^318]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
 [^319]: [JPCERT ChChes Feb 2017](https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html)
 [^320]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^321]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^322]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
 [^323]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)
 [^324]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
 [^325]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^326]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
 [^327]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
 [^328]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^329]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^330]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^331]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^332]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^333]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^334]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^335]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^336]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
 [^337]: [Symantec Security Center Trojan.Kwampirs](https://www.symantec.com/security-center/writeup/2016-081923-2700-99)
 [^338]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
 [^339]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^340]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)
 [^341]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
 [^342]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)
 [^343]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)
 [^344]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^345]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
 [^346]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^347]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^348]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^349]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^350]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^351]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
 [^352]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^353]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^354]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^355]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^356]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^357]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^358]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^359]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
 [^360]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
 [^361]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
 [^362]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
 [^363]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
 [^364]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^365]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
 [^366]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
 [^367]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)
 [^368]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^369]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^370]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
 [^371]: [Trend Micro Qakbot December 2020](https://success.trendmicro.com/en-US/solution/KA-0011282)
 [^372]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^373]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^374]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^375]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^376]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^377]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^378]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
 [^379]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^380]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^381]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^382]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
 [^383]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
 [^384]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)
 [^385]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^386]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^387]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^388]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^389]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^390]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^391]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)
 [^392]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)
 [^393]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^394]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^395]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^396]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^397]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
 [^398]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
 [^399]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
 [^400]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)
 [^401]: [Linux FTP](https://linux.die.net/man/1/ftp)
 [^402]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
 [^403]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^404]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
 [^405]: [objectivesee osx.shlayer apple approved 2020](https://objective-see.com/blog/blog_0x4E.html)
 [^406]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
 [^407]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^408]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
 [^409]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
 [^410]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^411]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
 [^412]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^413]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^414]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^415]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^416]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
 [^417]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^418]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^419]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^420]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
 [^421]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^422]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
 [^423]: [Donut Github](https://github.com/TheWover/donut)
 [^424]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^425]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)
 [^426]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
 [^427]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
 [^428]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^429]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^430]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
 [^431]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
 [^432]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
 [^433]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
 [^434]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^435]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^436]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^437]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
 [^438]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^439]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)
 [^440]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^441]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^442]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)
 [^443]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
 [^444]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
 [^445]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^446]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^447]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^448]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^449]: [Rapid7 Fake W2 July 2024](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)
 [^450]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^451]: [Symantec Backdoor.Mivast](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)
 [^452]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^453]: [Koi Glassworm Extensions November 2025](https://www.koi.ai/blog/glassworm-returns-new-wave-openvsx-malware-expose-attacker-infrastructure)
 [^454]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^455]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
 [^456]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
 [^457]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^458]: [Trend Micro Totbrick Oct 2016](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)
 [^459]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
 [^460]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^461]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^462]: [Palo Alto OilRig Sep 2018](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)
 [^463]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^464]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^465]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^466]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^467]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^468]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^469]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)
 [^470]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
 [^471]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^472]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^473]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^474]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
 [^475]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^476]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
 [^477]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^478]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
 [^479]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
 [^480]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
 [^481]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^482]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^483]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^484]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^485]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^486]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
 [^487]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
 [^488]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^489]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^490]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
 [^491]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
 [^492]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)
 [^493]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^494]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^495]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)
 [^496]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^497]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
 [^498]: [Securelist ShadowPad Aug 2017](https://securelist.com/shadowpad-in-corporate-networks/81432/)
 [^499]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^500]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^501]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
 [^502]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)
 [^503]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
