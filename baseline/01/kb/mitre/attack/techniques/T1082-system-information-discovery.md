---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1082
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1082-system-information-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [[kb/mitre/attack/techniques/T1680-local-storage-discovery|Local Storage Discovery]] which is an adversary's discovery of local drive, disks and/or volumes.<br><br>Tools such as [[kb/mitre/attack/software/S0096-systeminfo|Systeminfo]] can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] on network devices to gather detailed system information (e.g. `show version`).[^8]  On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.[^4] [^3] <br><br>Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.[^1] [^2] [^5] <br><br>[[kb/mitre/attack/techniques/T1082-system-information-discovery|System Information Discovery]] combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.[^7] [^6]  

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has collected system information including OS version, processor information, RAM size, location, host name, IP, and screen size of the infected host.[^1]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe collects the computer name of the victim's system during the initial infection.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to collect the processor type, operation system, computer name, and whether the system is a laptop or PC.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi gathers the name of the local host, version of GNU Compiler Collection (GCC), and the system information about the CPU, machine, and operating system.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos has the ability to gather basic system information and run the POSIX API `gethostbyname`.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to identify the computer name, OS version, and hardware configuration on a compromised host.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | During its initial execution, BACKSPACE extracts operating system information from the infected host.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has gathered system architecture, processor, OS configuration, and installed hardware information.[^1]  |
| [S0043](https://attack.mitre.org/software/S0043) | BUBBLEWRAP | BUBBLEWRAP collects system information, including the operating system version and hostname.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL can run [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]] to gather information about the victim.[^1] [^2]  |
| [S0046](https://attack.mitre.org/software/S0046) | CozyCar | A system info module in CozyCar gathers information on the victim host’s configuration.[^1]  |
| [S0048](https://attack.mitre.org/software/S0048) | PinchDuke | PinchDuke gathers system configuration information.[^1]  |
| [S0051](https://attack.mitre.org/software/S0051) | MiniDuke | MiniDuke can gather the hostname on a compromised machine.[^1]  |
| [S0058](https://attack.mitre.org/software/S0058) | SslMM | SslMM sends information to its hard-coded C2, including OS version, service pack information, processor speed, system name, and OS install date.[^1]  |
| [S0059](https://attack.mitre.org/software/S0059) | WinMM | WinMM collects the system name, OS version including service pack, and system install date and sends the information to the C2 server.[^1]  |
| [S0060](https://attack.mitre.org/software/S0060) | Sys10 | Sys10 collects the computer name, OS versioning information, and OS install date and sends the information to the C2.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky extracts basic information about the operating system.[^1]  |
| [S0065](https://attack.mitre.org/software/S0065) | 4H RAT | 4H RAT sends an OS version identifier in its beacons.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder has a command to upload to its C2 server victim mobile device information, including IMEI, IMSI, SIM card serial number, phone number, Android version, and other information.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | Elise executes `systeminfo` after initial communication is made to the remote server.[^1]  |
| [S0082](https://attack.mitre.org/software/S0082) | Emissary | Emissary has the capability to execute ver and systeminfo commands.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | The initial beacon packet for Misdat contains the operating system version of the victim.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | The initial beacon packet for Mis-Type contains the operating system version and file system of the victim.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | The initial beacon packet for S-Type contains the operating system version and file system of the victim.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has the ability to enumerate system information.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to obtain a victim's system name and operating system version.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has used [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]] to gather the OS version, as well as information on the system configuration, BIOS, the motherboard, and the processor.[^1] [^2]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic collects the OS version, hardware information, computer name, available system memory status, and system and user language settings.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea collects information about the OS and computer name.[^1] [^2]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can capture information regarding the victim's OS, security, and hardware configuration.[^1]  |
| [[kb/mitre/attack/software/S0096-systeminfo\|S0096]] | Systeminfo | [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]] can be used to gather information about the operating system.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 gathers and beacons the operating system build number and CPU Architecture (32-bit/64-bit) during installation.[^1]  |
| [[kb/mitre/attack/software/S0105-dsquery\|S0105]] | dsquery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.[^1]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to find information about the operating system.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects information from the victim about Windows OS version, computer name, battery info, and physical memory.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to collect the victim PC name and operating system.[^2] [^1] [^3]  |
| [S0124](https://attack.mitre.org/software/S0124) | Pisloader | Pisloader has a command to collect victim system information, including the system name and OS version.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can obtain the OS version information, computer name, processor architecture, machine role, and OS edition.[^1]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger can obtain information about the victim computer name, physical memory, country, and date.[^1]  |
| [S0137](https://attack.mitre.org/software/S0137) | CORESHELL | CORESHELL collects hostname and OS version data from the victim and sends the information to its C2 server.[^1]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has commands to get information about the victim's name, build, version, serial number, and memory usage.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon obtains the victim's operating system version and keyboard layout and sends the information to the C2 server.[^1] [^2]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | Winnti for Windows can determine if the OS on a compromised host is newer than Windows XP.[^1]  |
| [S0142](https://attack.mitre.org/software/S0142) | StreamEx | StreamEx has the ability to enumerate system information.[^1]  |
| [S0144](https://attack.mitre.org/software/S0144) | ChChes | ChChes collects the victim hostname, window resolution, and Microsoft Windows version.[^1] [^2]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can obtain the computer name, OS version, and default language identifier.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind can obtain the victim hostname, Windows version, RAM amount, and screen resolution.[^1]  |
| [S0151](https://attack.mitre.org/software/S0151) | HALFBAKED | HALFBAKED can obtain information about the OS, processor, and BIOS.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can gather extended system information including the hostname, OS version number, platform, memory information, time elapsed since system startup, and CPU information.[^2] [^1]  |
| [S0155](https://attack.mitre.org/software/S0155) | WINDSHIELD | WINDSHIELD can gather the victim computer name.[^1]  |
| [S0156](https://attack.mitre.org/software/S0156) | KOMPROGO | KOMPROGO is capable of retrieving information about the infected system.[^1]  |
| [S0157](https://attack.mitre.org/software/S0157) | SOUNDBITE | SOUNDBITE is capable of gathering system information.[^1]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the getInstalledAPP function to run `ls -la /Applications` to gather what applications are installed.[^1]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo discovers information about the infected machine.[^1]  |
| [S0171](https://attack.mitre.org/software/S0171) | Felismus | Felismus collects the system information, including hostname and OS version, and sends it to the C2 server.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Reaver collects system information from the victim, including CPU speed, computer name, ANSI code page, OEM code page identifier for the OS, Microsoft Windows version, and memory information.[^1]  |
| [S0176](https://attack.mitre.org/software/S0176) | Wingbird | Wingbird checks the victim OS version after executing to determine where to drop files based on whether the victim is 32-bit or 64-bit.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can gather system information, the computer name, OS version, drive and serial information from the victim's machine.[^2] [^1] [^3]  |
| [S0181](https://attack.mitre.org/software/S0181) | FALLCHILL | FALLCHILL can collect operating system (OS) version information, processor information, and system name from the victim.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher checks if the victim OS is 32 or 64-bit.[^2] [^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may collect information about the system by running `hostname` and `systeminfo` on a victim.[^1]  |
| [S0186](https://attack.mitre.org/software/S0186) | DownPaper | DownPaper collects the victim host name and serial number, and then sends the information to the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can grab a system’s information including the OS version, architecture, etc.[^1]  |
| [S0196](https://attack.mitre.org/software/S0196) | PUNCHBUGGY | PUNCHBUGGY can gather system information such as computer names.[^1] 	 |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can discover and collect victim system information.[^1]  |
| [S0199](https://attack.mitre.org/software/S0199) | TURNEDUP | TURNEDUP is capable of gathering system information.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can obtain system information such as OS version and disk space.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve information such as computer name, OS version, processor speed, memory size, and CPU speed.[^1]  |
| [S0205](https://attack.mitre.org/software/S0205) | Naid | Naid collects a unique identifier (UID) from a compromised host.[^1]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can retrieve information like hostname.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can retrieve system information.[^1]  |
| [S0214](https://attack.mitre.org/software/S0214) | HAPPYWORK | can collect system information, including computer name, system manufacturer, IsDebuggerPresent state, and execution path.[^1]  |
| [S0215](https://attack.mitre.org/software/S0215) | KARAE | KARAE can collect system information.[^1]  |
| [S0216](https://attack.mitre.org/software/S0216) | POORAIM | POORAIM can identify system information, including battery status.[^1]  |
| [S0217](https://attack.mitre.org/software/S0217) | SHUTTERSPEED | SHUTTERSPEED can collect system information.[^1]  |
| [S0218](https://attack.mitre.org/software/S0218) | SLOWDRIFT | SLOWDRIFT collects and sends system information to its C2.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can gather information about the host.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can retrieve OS name/architecture and computer/domain name information from compromised hosts.[^1] [^2]  |
| [S0228](https://attack.mitre.org/software/S0228) | NanHaiShu | NanHaiShu can gather the victim computer name and serial number.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can gather the victim OS version and whether it is 64 or 32 bit.[^1]  |
| [S0230](https://attack.mitre.org/software/S0230) | ZeroT | ZeroT gathers the victim's computer name, Windows version, and system language, and then sends it to its C2 server.[^1]  |
| [S0233](https://attack.mitre.org/software/S0233) | MURKYTOP | MURKYTOP has the capability to retrieve information about the OS.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects OS version information such as registered owner details, manufacturer details, processor type, available storage, installed patches, hostname, version info, system date, and other system information by using the commands `systeminfo`, `net config workstation`, `hostname`, `ver`, `set`, and `date /t`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT collects the MAC address, computer name, and CPU information.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc collects the OS version, country name, MAC address, computer name, and physical memory statistics.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot gathers system information, network addresses, and the operation system version.[^1] [^2]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can gather the hostname and the OS version to ensure it doesn’t run on a Windows XP or Windows Server 2003 systems.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA gathers information about the OS architecture, OS name, and OS version/Service pack.[^1] [^2]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck gathers computer names, OS version info, and also checks installed keyboard layouts to estimate if it has been launched from a certain list of countries.[^1]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie collects the hostname of the victim machine.[^1]  |
| [S0245](https://attack.mitre.org/software/S0245) | BADCALL | BADCALL collects the computer name and host name on the compromised system.[^1]  |
| [S0247](https://attack.mitre.org/software/S0247) | NavRAT | NavRAT uses `systeminfo` on a victim’s machine.[^1]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty gathers the computer name, CPU information, Microsoft Windows version, and runs the command `systeminfo`.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon collects endpoint information using the `systeminfo` command.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can obtain the OS version and build, computer name, and processor architecture from a compromised host.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy collects the OS version and computer name. Zebrocy also runs the `systeminfo` command to gather system information. [^7] [^5] [^4] [^6] [^3] [^1] [^2]  |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince collects hard drive content and system configuration information.[^1]  |
| [S0253](https://attack.mitre.org/software/S0253) | RunningRAT | RunningRAT gathers the OS version and processor information.[^1]  |
| [S0254](https://attack.mitre.org/software/S0254) | PLAINTEE | PLAINTEE collects general system enumeration data about the infected machine and checks the OS version.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN collects the OS name, machine name, and architecture information.[^1]  |
| [S0259](https://attack.mitre.org/software/S0259) | InnaputRAT | InnaputRAT gathers system information.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can gather information on the OS version, computer name, DEP policy, and memory size.[^1] [^2]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can gather system information from the victim’s machine including the OS type.[^1]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE checks for information on the CPU fan, temperature, mouse, hard disk, and motherboard as part of its anti-VM checks.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar gathers information on the system.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot gathers the OS version, machine name, CPU type, amount of RAM available, and UEFI/BIOS firmware information from the victim’s machine.[^1] [^2] [^3] [^4]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT collects the victim’s computer name, processor architecture, OS version, and system type.[^2] [^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has used commands and API calls to gather system information.[^1] [^3] [^2]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin gathers BIOS versions and manufacturers, the number of CPU cores, the total physical memory, and the computer name.[^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE has the capability to collect the computer name, language settings, the OS version, CPU information, and time elapsed since system start.[^1]  |
| [S0272](https://attack.mitre.org/software/S0272) | NDiskMonitor | NDiskMonitor obtains the victim computer name and encrypts the information to send over its C2 channel.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT has the capability to gather the system’s hostname and OS version.[^2] [^1]  |
| [S0280](https://attack.mitre.org/software/S0280) | MirageFox | MirageFox can collect CPU and architecture information from the victim’s machine.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT collects information about the OS (version, build type, install date) as well as system up-time upon receiving a connection from a backdoor.[^1]  |
| [S0284](https://attack.mitre.org/software/S0284) | More_eggs | More_eggs has the capability to gather the OS version and computer name.[^1] [^2]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda collects the OS version, system architecture, computer name, product ID, install date, and information on the keyboard mapping to determine the language used on the system.[^1] [^2]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can collect the system's computer name and also has the capability to collect information on the processor, memory, OS, and video card from the system.[^1] [^2] [^3]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can collect the OS version and process architecture of compromised hosts.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can collect the computer name, RAM used, and operating system version from the victim’s machine.[^1] [^2]  |
| [S0337](https://attack.mitre.org/software/S0337) | BadPatch | BadPatch collects the OS system, OS version, MAC address, and the computer name from the victim’s machine.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia gathers the hostname and OS version from the victim’s machine.[^1] [^2]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can collect the computer name, OS version, and OS architecture information.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can collect the machine information, system architecture, the OS version, computer name, Windows product name, the number of CPU cores, video card information, and the system language.[^1] [^2]  |
| [S0346](https://attack.mitre.org/software/S0346) | OceanSalt | OceanSalt can collect the computer name from the system.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can collect the hostname, Microsoft Windows version, and processor architecture from a victim machine.[^1]  |
| [S0350](https://attack.mitre.org/software/S0350) | zwShell | zwShell can obtain the victim PC name and OS version.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can gather system information from the victim’s machine such as the OS version, and machine name.[^1] [^2]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D collects processor information, memory information, computer name, hardware UUID, serial number, and operating system version. OSX_OCEANLOTUS.D has used the `ioreg` command to gather some of this information.[^1] [^2] [^3]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI can gather information on the operating system on the victim’s machine.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis collects OS information and the computer name from the victim’s machine.[^1] [^2]  |
| [S0355](https://attack.mitre.org/software/S0355) | Final1stspy | Final1stspy obtains victim Microsoft Windows version information and CPU architecture.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can gather the OS version, architecture information, hostname, and RAM size information from the victim’s machine and has used `cmd /c systeminfo` command to get a snapshot of the current system state of the target machine.[^2] [^1] [^3]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^2] [^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth collects the machine name and keyboard language from the system. [^1] [^2]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp uses the `cat /proc/cpuinfo \| grep -c “cpu family” 2>&1` command to gather system information. [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has been observed collecting victim machine information like OS version.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT collects the CPU information, OS information, and system language.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has the capability to discover the system OS, Windows version, architecture and environment.[^1] 	 |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy can collect the victim's operating system and computer name during the initial infection.[^1]  |
| [S0382](https://attack.mitre.org/software/S0382) | ServHelper | ServHelper will attempt to enumerate Windows version and system architecture.[^1]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex has collected the computer name and OS architecture information from the system.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT enumerates the victim operating system and computer name during the initial infection.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]] to gather system information.[^1]  |
| [S0387](https://attack.mitre.org/software/S0387) | KeyBoy | KeyBoy can gather extended system information, such as information about the operating system and memory.[^2] [^1]  |
| [S0388](https://attack.mitre.org/software/S0388) | YAHOYAH | YAHOYAH checks for the system’s Windows OS version and hostname.[^1]  |
| [S0391](https://attack.mitre.org/software/S0391) | HAWKBALL | HAWKBALL can collect the OS version, architecture information, and computer name.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron gathers the victim computer name using the Win32 API call `GetComputerName`.[^1]  |
| [S0402](https://attack.mitre.org/software/S0402) | OSX/Shlayer | OSX/Shlayer has collected the IOPlatformUUID, session UID, and the OS version using the command `sw_vers -productVersion`.[^1] [^2]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete collects the hostname of the target computer.[^1]   |
| [S0410](https://attack.mitre.org/software/S0410) | Fysbis | Fysbis has used the command `ls /etc \| egrep -e"fedora\*\|debian\*\|gentoo\*\|mandriva\*\|mandrake\*\|meego\*\|redhat\*\|lsb-\*\|sun-\*\|SUSE\*\|release"` to determine which Linux OS version is running.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can collect the local hostname, operating system details, CPU speed, and total physical memory.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has executed the `ver` command.[^1] 	 |
| [S0417](https://attack.mitre.org/software/S0417) | GRIFFON | GRIFFON has used a reconnaissance module that can be used to retrieve information about a victim's computer, including the resolution of the workstation .[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has the ability to gather information about the compromised host.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to determine if the current user is an administrator, Windows product name, processor name, screen resolution, and physical RAM of the infected host.[^1]  |
| [S0433](https://attack.mitre.org/software/S0433) | Rifdoor | Rifdoor has the ability to identify the Windows version on the compromised host.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum can collect computer name, locale information, and information about the OS and architecture.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has collected system information on the infected host.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] gathered the operating system name and specific Windows version of an infected machine.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has the ability to discover the computer name and Windows product name/version.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can detect the computer name and operating system.[^1] 	 |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has checked the language of the infected system using the "GetUSerDefaultUILanguage" function.[^1]  |
| [S0450](https://attack.mitre.org/software/S0450) | SHARPSTATS | SHARPSTATS has the ability to identify the IP address, machine name, and OS of the compromised host.[^1]  |
| [S0451](https://attack.mitre.org/software/S0451) | LoudMiner | LoudMiner has monitored CPU usage.[^1] 	 |
| [S0453](https://attack.mitre.org/software/S0453) | Pony | Pony has collected the Service Pack, language, and region information to send to the C2.[^1] 	 |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to discover information about the compromised host.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has collected the hostname and operating system version from the compromised host.[^1] [^2] [^3]  |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to identify the hostname, computer name, Windows version, processor speed, and machine GUID on a compromised host.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can determine the system architecture it is running on to choose which version of the DLL to use.[^1]  |
| [S0460](https://attack.mitre.org/software/S0460) | Get2 | Get2 has the ability to identify the computer name and Windows version of an infected host.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to identify the OS version, OS bit information and computer name.[^2] [^1]  |
| [S0462](https://attack.mitre.org/software/S0462) | CARROTBAT | CARROTBAT has the ability to determine the operating system of the compromised host and whether Windows is being run with x86 or x64 architecture.[^1] [^2]  |
| [S0464](https://attack.mitre.org/software/S0464) | SYSCON | SYSCON has the ability to use [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]] to identify system information.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to identify hardware information, the computer name, and OS information on an infected host.[^1]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has the ability to check whether the infected system’s OS is Debian or RHEL/CentOS to determine which cryptocurrency miner it should use.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to identify the OS architecture on a compromised host.[^1]  |
| [S0475](https://attack.mitre.org/software/S0475) | BackConfig | BackConfig has the ability to gather the victim's computer name.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can determine the Windows version and computer name on a compromised host.[^2] [^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore will enumerate the macOS version to determine which follow-on behaviors to execute using `/usr/bin/sw_vers -productVersion`.[^1] [^2]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has the ability to identify the computer name and OS version on a compromised host.[^2] [^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has collected the operating system version from the infected system.[^1]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan has discovered the OS version, CPU model, and RAM size of the system it has been installed on.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has collected the system architecture, OS version, and MAC address information.[^1]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy has gathered operating system information.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can identify the username, machine name, system language, keyboard layout, and OS version on a compromised host.[^5] [^2] [^7] [^6] [^6] [^4] [^3] [^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can collect and send OS version and computer name as a part of its C2 beacon.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor can determine the hostname and linux version on a compromised host.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can collect the user name, Windows version, computer name, and available space on discs from a compromised host.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke can enumerate the CPUID and BIOS version on a compromised system.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can identify the computer name of a compromised host.[^1] [^2]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can collect the hostname, operating system configuration, and product ID on victim machines by executing [[kb/mitre/attack/software/S0096-systeminfo\|Systeminfo]].[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has collected from a victim machine the system name, processor information, and OS version.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can collect the computer name and OS version from a compromised host.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can collect the computer name, system architecture, default language, and processor frequency of a compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has collected system name, OS version, adapter information, and memory usage from a victim machine.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can fingerprint architecture, computer name, and OS version on the compromised host. Bazar can also check if the Russian language is installed on the infected machine and terminate if it is found.[^1] [^2]  |
| [S0543](https://attack.mitre.org/software/S0543) | Spark | Spark can collect the hostname, keyboard layout, and language from the system.[^1]   |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage has checked the system settings to see if Arabic is the configured language.[^1]  |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook has checked for the presence of Arabic language in the infected machine's settings.[^1]   |
| [S0553](https://attack.mitre.org/software/S0553) | MoleNet | MoleNet can collect information about the about the system.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor can perform a language check of the infected system and can query the CPU information (cupid).[^1] [^2]  |
| [S0556](https://attack.mitre.org/software/S0556) | Pay2Key | Pay2Key has the ability to gather the hostname of the victim machine.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected hostname and OS version.[^1] [^2]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can collect the victim's computer name, hostname and adapter information to create a unique identifier.[^1] [^2]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can obtain the computer name from the victim's system.[^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has collected the computer name from the infected host.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a module to gather information from the compromised asset, including the computer version, computer name, IIS version, and more.[^1]   |
| [S0584](https://attack.mitre.org/software/S0584) | AppleJeus | AppleJeus has collected the victim host information after infection.[^1]  |
| [S0585](https://attack.mitre.org/software/S0585) | Kerrdown | Kerrdown has the ability to determine if the compromised host is running a 32 or 64 bit OS architecture.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can report the file system type of a compromised host to C2.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has discovered system information including memory status, CPU frequency, and OS versions.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has collected the host's OS, CPU, and memory information.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet collects system information including computer and domain names, OS version, and S7P paths.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer collects the victim machine’s Windows GUID.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist can collect the computer name of a targeted system.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can execute `getinfo` to enumerate the computer name and OS version of a compromised system.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can identify the OS version of a targeted system.[^1]  |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster can enumerate the host name and OS version on a target system.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has collected system information, including the machine name and OS version.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can collect the OS, and build version on a compromised host.[^1]  |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout can determine whether the ISO payload was received by a Windows or iOS device.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can enumerate the hostname, domain, and IP of a compromised host.[^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos can record the hostname and kernel version of the target machine.[^1]  |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK has captured victim computer name, memory space, and CPU details.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT has the ability to check for blocklisted computer names on infected endpoints.[^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette can identify the system name of a compromised host.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can retrieve system information including OS version, memory usage, local hostname, and system adapter information.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has used the `systeminfo` command on a compromised host.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can collect system information including the OS version and domain on a compromised host.[^1] [^4] [^2] [^3]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can obtain the computer name from a compromised host.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT has collected the computer name and OS version from victim machines.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET identifies the macOS version and uses `ioreg` to determine serial number.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can collect the computer name and OS version from the system.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can discover the hostname, computer name, and Windows version of a targeted machine.[^1] [^2]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can gather system information from a compromised host.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect a system's architecture, operating system version, and hostname.[^2] [^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can collect system profile information from a compromised host.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can determine the operating system and whether a targeted machine has a 32 or 64 bit architecture.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme has the ability to obtain the computer name of a compromised host.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS has checked the OS version using `wmic.exe` and the `find` command.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can collect compromised host information, including OS version, PC name, RAM size, and CPU details.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can collect the OS version, system architecture, and computer name.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can enumerate the OS version and computer name on a targeted system.[^1]  |
| [S0679](https://attack.mitre.org/software/S0679) | Ferocious | Ferocious can use `GET.WORKSPACE` in Microsoft Excel to determine the OS version of the compromised host.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower has the ability to enumerate the OS architecture.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can collect the computer name from the machine.[^1] [^2]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink has the ability to query device information.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor has the ability to discover the hostname of a compromised host.[^1]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can use `uname` to identify the operating system name, version, and processor type.[^1] [^2]    |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can collect the OS version and computer name from a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect information related to a compromised host, including OS version.[^1]  |
| [S0693](https://attack.mitre.org/software/S0693) | CaddyWiper | CaddyWiper can use `DsRoleGetPrimaryDomainInformation` to determine the role of the infected machine. CaddyWiper can also halt execution if the compromised host is identified as a domain controller.[^1] [^2]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can determine the OS version and bitness on a targeted host.[^3] [^4] [^2] [^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ has collected the host name and operating system product name from a compromised machine.[^1]   |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can enumerate the targeted machine's name and GUID.[^2] [^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can collect information about a compromised computer, including: Hardware UUID, Mac serial number, and macOS version.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can identify the OS version, CPU, and other details from a victim's machine.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can collect the GUID of a targeted machine.[^2] [^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can enumerate the OS version and hostname of a targeted machine.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | The IceApple Server Variable Dumper module iterates over all server variables present for the current request and returns them to the adversary.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has collected the computer name and OS version from a compromised machine.[^1] [^2]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall can retrieve the hostname via `gethostbyname`.[^1] <br> |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT has the ability to collect the hostname, OS version, and OS architecture of an infected host.[^1]  |
| [S1029](https://attack.mitre.org/software/S1029) | AuTo Stealer | AuTo Stealer has the ability to collect the hostname and OS information from an infected host.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has gathered victim computer information and configurations.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can retrieve the hostname of a compromised host.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can collect the OS version, architecture, and machine name to create a unique token for the infected host.[^1]  |
| [S1037](https://attack.mitre.org/software/S1037) | STARWHALE | STARWHALE can gather the computer name of an infected host.[^2] [^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can enumerate the OS version and domain on a targeted system.[^3] [^2] [^1]  |
| [S1048](https://attack.mitre.org/software/S1048) | macOS.OSAMiner | macOS.OSAMiner can gather the device serial number.[^1]  |
| [S1052](https://attack.mitre.org/software/S1052) | DEADEYE | DEADEYE can enumerate a victim computer's volume serial number and host name.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can collect the computer name from a compromised host.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can collect the computer name of a compromised host.[^1] [^2]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady has the ability to collect information such as computer name, computer manufacturer, BIOS, operating system, and firmware, including through the use of `systeminfo.exe`.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can retrieve the following information from an infected machine: OS, architecture, computer name, OS build version, and environment variables.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can obtain system information by querying the `Win32_ComputerSystem`, `Win32_BIOS`, `Win32_MotherboardDevice`, `Win32_PnPEntity`, and `Win32_DiskDrive` WMI objects.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can obtain the computer name and UUID.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can collect system boot configuration and CPU information.[^2] [^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal |  Royal can use `GetNativeSystemInfo` to enumerate system processors.[^1] [^2]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro executes a set of commands to collect device information, including `uname`.  Another example is the `cat /etc/*release \| uniq` command used to collect the current OS distribution.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can obtain current system information from a compromised machine such as the `SHELL PID`, `PSVERSION`, `HOSTNAME`, `LOGONSERVER`, `LASTBOOTUP`, OS type/version, bitness, and hostname.[^1] [^2]   |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to collect the computer name, and CPU manufacturer name from a compromised machine. Sardonic also has the ability to execute the `ver` and `systeminfo` commands.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 has the ability to query `Win32_ComputerSystem` for system information. [^1]   |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can obtain the computer name and information on the OS from targeted hosts.[^1] [^2]  |
| [S1107](https://attack.mitre.org/software/S1107) | NKAbuse | NKAbuse conducts multiple system checks and includes these in subsequent "heartbeat" messages to the malware's command and control server.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate will gather various system information such as domain, display adapter description, operating system type and version, processor type, and RAM amount.[^1] [^2]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can check the type of Ivanti VPN device it is running on by executing `first_run()` to identify the first four bytes of the motherboard serial number.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu collects the OS version, computer name, and language ID.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish has the ability to enumerate system information including the victim computer name.[^1] [^2] [^3]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira uses the `GetSystemInfo` Windows function to determine the number of processors on a victim machine.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin performs several system checks as part of anti-analysis mechanisms, including querying the operating system build number, processor vendor and type, video controller, and CPU temperature.[^1]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | Gootloader can inspect the User-Agent string in GET request header information to determine the operating system of targeted systems.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can use WMI queries and shell commands such as systeminfo.exe to collect the operating system, BIOS version, and domain name of the targeted system.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can capture environmental variables on compromised hosts.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot performs a variety of system checks and gathers system information, including commands such as `whoami`.[^1] [^2]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor gathers information on the victim system such as CPU and Computer name as well as device drivers.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer gathers information on infected systems such as operating system, processor information, RAM, and display information.[^2] [^1]  |
| [S1152](https://attack.mitre.org/software/S1152) | IMAPLoader | IMAPLoader uses WMI queries to gather information about the victim machine.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can gather information about the OS version and hardware on compromised hosts.[^1] [^2]  |
| [[kb/mitre/attack/software/S1155-covenant\|S1155]] | Covenant | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] implants can gather basic information on infected systems.[^1]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka performs basic system profiling actions to fingerprint and register the victim system with the C2 controller.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP reads the value of the infected system's `HKLM\SYSTEM\Microsoft\Cryptography\MachineGUID` value.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus can gather operating system information.[^2] [^3] [^3] [^1]  |
| [S1166](https://attack.mitre.org/software/S1166) | Solar | Solar can send basic information about the infected host to C2.[^1]  |
| [S1167](https://attack.mitre.org/software/S1167) | AcidPour | AcidPour can identify various system locations and mapped devices on Linux systems as a precursor to wiping activity.[^1]  |
| [S1168](https://attack.mitre.org/software/S1168) | SampleCheck5000 | SampleCheck5000 can create unique victim identifiers by using the compromised system’s computer name.[^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango can collect the machine name of a compromised system which is later used as part of a unique victim identifier.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can identify the compromised system's hostname which is used to create a unique identifier.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker uses WMI queries to gather various information about the victim machine and operating system.[^1] [^2]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware gathers victim system information to generate a unique victim identifier.[^1]  |
| [S1182](https://attack.mitre.org/software/S1182) | MagicRAT | MagicRAT collects basic system information from victim machines.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer variants collect victim system information for exfiltration.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE performs system survey actions following initial execution.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | LightSpy's second stage implant uses the `DeviceInformation` class to collect system information, including CPU usage, battery statistics, memory allocations, screen size, etc.[^1]  |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer can gather system configuration information by running the native `show configuration` command.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka utilizes WinAPI calls and registry queries to gather system information.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer can collect local system information.[^1] [^2]  |
| [S1198](https://attack.mitre.org/software/S1198) | Gomir | Gomir collects information on infected systems such as hostname, username, CPU, and RAM information.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can enumerate system information including hostname and domain information.[^2] [^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can enumerate the computer name and domain membership of the compromised system.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can enumerate system hostname and domain.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can collect system information and supported language information from the victim machine.[^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex gathers information from the infected system such as hostname.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can retrieve information about virtual machines.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has gathered various system information from victim machines.[^3] [^2] [^1]  |
| [S1222](https://attack.mitre.org/software/S1222) | RIFLESPINE | RIFLESPINE can collect system information after installation on infected systems.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has collected and sent system information including volume serial number, computer name, and system uptime to designated C2.[^1] [^2]   PUBLOAD has also used several commands executed in sequence via `cmd` in a short interval to gather system information about the infected host including `systeminfo`.[^3]  PUBLOAD has decrypted shellcode that collects the computer name.[^4]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can gather system information including hostname, domain, and OS details.[^1]  |
| [S1234](https://attack.mitre.org/software/S1234) | SplatCloak | SplatCloak has collected the Windows build number using the windows kernel API `RtlGetVersion` to determine if the response is 19000 or higher (Windows 10 version 2004 or later).[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has the ability to retrieve the name of the infected machine.[^1] [^2] [^3]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can collect information about the local system.[^1] [^2] [^3] [^4]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can detect whether a system is running FreeBSD, VMkernel (ESXi), Nutanix AHV, or a standard Linux distribution to enable platform-specific encryption behaviors.[^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has collected data from the SMBIOS firmware table using `GetSystemFirmwareTable`.[^1]    |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has collected OS type, hostname and system version through the "pay" module.[^1] [^3]  InvisibleFerret has also queried the victim device using Python scripts to obtain the User and Hostname.[^2] [^4]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has been known to collect basic system information.[^1] [^3]  BeaverTail has also collected data to include hostname and current timestamp prior to uploading data to the API endpoint `/uploads` on the C2 server.[^2]  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader has the ability to collect the hostname, OS Username, Geolocation, and OS version of an infected host.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has identified the OS and MAC address of victim device through host fingerprinting scripting.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has collected username  , build number and serial number, then sent the information to the C2 server.[^2] [^1]  SystemBC has also gathered device name, operating system, and processor type.[^3]  |
| [[kb/mitre/attack/software/S9002-diskpart\|S9002]] | Diskpart | [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^1]   |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has gathered victim system information.[^1] [^2]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has the ability to check the OS of the victim host.[^1] [^2]   GlassWorm has checked whether the OS platform value includes `darwin` prior to execution of macOS specific scripts.[^1] [^2]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can enumerate a targeted system's SerialNumber and Version.[^2] [^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can disover machine information including OS architecture, the ANSI code page (ACP) identifier, and hostname.[^1] [^2]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can enumerate the hostname and username of the compromised system.[^1] [^3] [^2]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has obtained system information such as release, uptime, and current time.[^1]    |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can discover the device ID and hostname from the targeted machine to use for encryption keys.[^1]  |
| [S9029](https://attack.mitre.org/software/S9029) | IronWind | IronWind can capture the OS version and computer name of the compromised host.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag loader and AshenOrchestrator components can collect reconnaissance data from victim machines.[^1]  |
| [S9034](https://attack.mitre.org/software/S9034) | Tsundere Botnet | Tsundere Botnet has collected the machine’s MAC address, total memory, GPU information and other system information.[^1]   |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG has the ability to execute Windows commands returned from C2 to gather system information.[^1] [^2]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has gathered the victim machine’s computer name.[^1]      |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper has used `[System.Net.Dns]::GetHostName()` and `$env:COMPUTERNAME` to enumerate the hostname of a system and determine if it is a domain controller.[^1]  |

 [^1]: [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
 [^2]: [Google Instances Resource](https://cloud.google.com/compute/docs/reference/rest/v1/instances)
 [^3]: [Varonis](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)
 [^4]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^5]: [Microsoft Virutal Machine API](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)
 [^6]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^7]: [OSX.FairyTale](https://www.sentinelone.com/blog/trail-osx-fairytale-adware-playing-malware/)
 [^8]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^9]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
 [^10]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^11]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^12]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^13]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^14]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^15]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^16]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^17]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
 [^18]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^19]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^20]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^21]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
 [^22]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^23]: [Eclypsium Trickboot December 2020](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)
 [^24]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^25]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
 [^26]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
 [^27]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^28]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
 [^29]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^30]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
 [^31]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^32]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^33]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^34]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^35]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^36]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^37]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^38]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^39]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^40]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^41]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^42]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)
 [^43]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)
 [^44]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
 [^45]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^46]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^47]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^48]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
 [^49]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^50]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^51]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^52]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^53]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^54]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^55]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^56]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^57]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
 [^58]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
 [^59]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^60]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^61]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^62]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)
 [^63]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^64]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^65]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^66]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^67]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
 [^68]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^69]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^70]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^71]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^72]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)
 [^73]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^74]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^75]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^76]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^77]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
 [^78]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^79]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^80]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)
 [^81]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^82]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^83]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^84]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)
 [^85]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^86]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^87]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^88]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^89]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^90]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^91]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^92]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
 [^93]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^94]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^95]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^96]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^97]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
 [^98]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^99]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^100]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
 [^101]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^102]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^103]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^104]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^105]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^106]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
 [^107]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^108]: [Securelist Denis April 2017](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)
 [^109]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^110]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
 [^111]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^112]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^113]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^114]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^115]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^116]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^117]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^118]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^119]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^120]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^121]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^122]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^123]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^124]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^125]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
 [^126]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^127]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^128]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^129]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)
 [^130]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^131]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^132]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
 [^133]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^134]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^135]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^136]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
 [^137]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^138]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^139]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^140]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^141]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
 [^142]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^143]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^144]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^145]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^146]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^147]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^148]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^149]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
 [^150]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^151]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^152]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^153]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^154]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^155]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^156]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^157]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^158]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^159]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
 [^160]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
 [^161]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^162]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^163]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^164]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
 [^165]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^166]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^167]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^168]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^169]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^170]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)
 [^171]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^172]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
 [^173]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
 [^174]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^175]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^176]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
 [^177]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^178]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^179]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^180]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^181]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^182]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^183]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^184]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^185]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)
 [^186]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
 [^187]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^188]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^189]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
 [^190]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
 [^191]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^192]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^193]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^194]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^195]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^196]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^197]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
 [^198]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
 [^199]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^200]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^201]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^202]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^203]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^204]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^205]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)
 [^206]: [AhnLab_SystemBC_Apr2022](https://asec.ahnlab.com/en/33600/)
 [^207]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^208]: [HarmonProofpoint_SystemBC_Aug2019](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)
 [^209]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^210]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^211]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^212]: [Github Covenant](https://github.com/cobbr/Covenant)
 [^213]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^214]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
 [^215]: [Cisco CaddyWiper March 2022](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)
 [^216]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
 [^217]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^218]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^219]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^220]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)
 [^221]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^222]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^223]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^224]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^225]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
 [^226]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
 [^227]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^228]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
 [^229]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^230]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
 [^231]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^232]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)
 [^233]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^234]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^235]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^236]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
 [^237]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
 [^238]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^239]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
 [^240]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^241]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^242]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^243]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^244]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^245]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^246]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^247]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^248]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^249]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
 [^250]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^251]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^252]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
 [^253]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
 [^254]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^255]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^256]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^257]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^258]: [Fysbis Palo Alto Analysis](https://researchcenter.paloaltonetworks.com/2016/02/a-look-into-fysbis-sofacys-linux-backdoor/)
 [^259]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^260]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^261]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^262]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^263]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^264]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
 [^265]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
 [^266]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
 [^267]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^268]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^269]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^270]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^271]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^272]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
 [^273]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
 [^274]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^275]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^276]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)
 [^277]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^278]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^279]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^280]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
 [^281]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^282]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^283]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^284]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^285]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^286]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
 [^287]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^288]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^289]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^290]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^291]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^292]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^293]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^294]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^295]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^296]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^297]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^298]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^299]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^300]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^301]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^302]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
 [^303]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
 [^304]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^305]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
 [^306]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^307]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)
 [^308]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
 [^309]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^310]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
 [^311]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^312]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^313]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^314]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^315]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^316]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^317]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^318]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)
 [^319]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
 [^320]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^321]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^322]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^323]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^324]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^325]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^326]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^327]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^328]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^329]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^330]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^331]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^332]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
 [^333]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^334]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^335]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
 [^336]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^337]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
 [^338]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^339]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^340]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^341]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)
 [^342]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^343]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^344]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^345]: [TechNet Systeminfo](https://technet.microsoft.com/en-us/library/bb491007.aspx)
 [^346]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^347]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^348]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^349]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^350]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^351]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^352]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^353]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^354]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^355]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^356]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
 [^357]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^358]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^359]: [Acronis XLoader 2021](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)
 [^360]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^361]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
 [^362]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^363]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^364]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^365]: [Talos ROKRAT 2](https://blog.talosintelligence.com/2017/11/ROKRAT-Reloaded.html)
 [^366]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
 [^367]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^368]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^369]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^370]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
 [^371]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^372]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^373]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
 [^374]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^375]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
 [^376]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^377]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
 [^378]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^379]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^380]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^381]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^382]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^383]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^384]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^385]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^386]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^387]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)
 [^388]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^389]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^390]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^391]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^392]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^393]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^394]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^395]: [McAfee Netwire Mar 2015](https://securingtomorrow.mcafee.com/mcafee-labs/netwire-rat-behind-recent-targeted-attacks/)
 [^396]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
 [^397]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^398]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
 [^399]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
 [^400]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^401]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^402]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
 [^403]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^404]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^405]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)
 [^406]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^407]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
 [^408]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^409]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^410]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^411]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
 [^412]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^413]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^414]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^415]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^416]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^417]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)
 [^418]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^419]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^420]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^421]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
 [^422]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
 [^423]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
 [^424]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^425]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^426]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^427]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^428]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^429]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^430]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^431]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^432]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^433]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)
 [^434]: [TrendMicro LummaStealer 2025](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)
 [^435]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^436]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^437]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^438]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^439]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^440]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
