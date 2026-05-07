---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1057
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1057-process-discovery
tactic:
    - Discovery
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

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from [[kb/mitre/attack/techniques/T1057-process-discovery|Process Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>In Windows environments, adversaries could obtain details on running processes using the [[kb/mitre/attack/software/S0057-tasklist|Tasklist]] utility via [[kb/mitre/attack/software/S0106-cmd|cmd]] or `Get-Process` via [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]]. Information about processes can also be extracted from the output of [[kb/mitre/attack/techniques/T1106-native-api|Native API]] calls such as `CreateToolhelp32Snapshot`. In Mac and Linux, this is accomplished with the `ps` command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.[^4] [^2] <br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands such as `show processes` can be used to display current running processes.[^3] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can use `GetCurrentProcessId` for process discovery.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module to list the processes running on a machine.[^1]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe can list running processes.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to enumerate running processes and identify their owners.[^1]  |
| [S0018](https://attack.mitre.org/software/S0018) | Sykipot | Sykipot may gather a list of running processes by running `tasklist /v`.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi collects current and parent process IDs.[^1] [^2]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use its `Process List` command to enumerate processes on compromised hosts.[^1]  |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak lists running processes.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | BACKSPACE may collect information about running processes.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has the capability to list processes.[^1]  |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | NETEAGLE can send process listings over the C2 channel.[^1]  |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | The discovery modules used with Duqu can collect information on process details.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | JHUHUGIT obtains a list of running processes on the victim.[^1] [^2]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL can list running processes.[^1]  |
| [S0049](https://attack.mitre.org/software/S0049) | GeminiDuke | GeminiDuke collects information on running processes and environment variables from the victim.[^1]  |
| [[kb/mitre/attack/software/S0057-tasklist\|S0057]] | Tasklist | [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] can be used to discover processes running on a system.[^1]  |
| [S0059](https://attack.mitre.org/software/S0059) | WinMM | WinMM sets a WH_CBT Windows hook to collect information on process creation.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky collects information about running processes from victims.[^1] [^2]  |
| [S0063](https://attack.mitre.org/software/S0063) | SHOTPUT | SHOTPUT has a command to obtain a process listing.[^1]  |
| [S0064](https://attack.mitre.org/software/S0064) | ELMER | ELMER is capable of performing process listings.[^1]  |
| [S0065](https://attack.mitre.org/software/S0065) | 4H RAT | 4H RAT has the capability to obtain a listing of running processes (including loaded modules).[^1]  |
| [S0069](https://attack.mitre.org/software/S0069) | BLACKCOFFEE | BLACKCOFFEE has the capability to discover processes.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder has a command to upload information about all running processes to its C2 server.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | Elise enumerates processes via the `tasklist` command.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to search for a given process name in processes currently running in the system.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has gathered a process list by using [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]].exe.[^1] [^2] [^3]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `tasklist /v` command to obtain a list of processes.[^1] [^2]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea collects information about running processes.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can use [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] to collect a list of running tasks.[^1] [^2]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to list processes.[^2] [^1] [^3] 	  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can obtain a process list from the victim.[^1]  |
| [S0127](https://attack.mitre.org/software/S0127) | BBSRAT | BBSRAT can list running processes.[^1]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has a command to list the victim's processes.[^1]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | Winnti for Windows can check if the explorer.exe process is responsible for calling its install function.[^1]  |
| [S0142](https://attack.mitre.org/software/S0142) | StreamEx | StreamEx has the ability to enumerate processes.[^1]  |
| [S0144](https://attack.mitre.org/software/S0144) | ChChes | ChChes collects its process identifier (PID) on the victim.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can obtain information about process integrity levels.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind has a command to return a list of running processes.[^1]  |
| [S0151](https://attack.mitre.org/software/S0151) | HALFBAKED | HALFBAKED can obtain information about running processes on the victim.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike's Beacon payload can collect information on process details.[^2] [^1] [^3]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the getProcessList function to run `ps aux` to get running processes.[^1]  |
| [S0162](https://attack.mitre.org/software/S0162) | Komplex | The OsInfo function in Komplex collects a running process list.[^1]  |
| [S0170](https://attack.mitre.org/software/S0170) | Helminth | Helminth has used [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] to get information on processes.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can gather a list of processes.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher checks its parent process for indications that it is running in a sandbox setup.[^2] [^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may collect process information by running `tasklist` on a victim.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can list the running processes and get the process ID and parent process’s ID.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^1] [^2]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can discover processes on compromised hosts.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can list running processes.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can monitor processes.[^1] [^2]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can retrieve lists of running processes.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can retrieve a list of running processes.[^1]  |
| [S0216](https://attack.mitre.org/software/S0216) | POORAIM | POORAIM can enumerate processes.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can enumerate processes.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS has used `get_tasklist` to discover processes on the compromised host.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can gather a process list from the victim.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of running services with the command `tasklist /v`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT lists the running processes on the system.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc lists processes running on the system.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot identifies processes and collects the process ids.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can list the current running processes on the system.[^1] [^2]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA lists the system’s processes.[^1] [^2]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck enumerates all running processes.[^1] [^2]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie uses the `tasklist` to view running processes on the victim’s machine.[^1]  |
| [S0247](https://attack.mitre.org/software/S0247) | NavRAT | NavRAT uses `tasklist /v` to check running processes.[^1]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty gets an output of running processes using the `tasklist` command.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon checks the running processes on the victim’s machine.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy uses the `tasklist` and `wmic process get Capture, ExecutablePath` commands to gather the processes running on the system.[^1] [^2] [^3] [^4] [^5]  |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince lists the running processes.[^1]  |
| [S0254](https://attack.mitre.org/software/S0254) | PLAINTEE | PLAINTEE performs the `tasklist` command to list running processes.[^1]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito runs `tasklist` to obtain running processes.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN can get a list of the processes and running tasks on the system.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can obtain a list of running processes.[^1] [^2]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar obtains a list of running processes through WMI querying and the `ps` command.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot uses module networkDll for process list discovery.[^1] [^2]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT collects a list of running processes.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal can obtain a list of running processes on the victim’s machine.[^1] [^2] [^3]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin checks the running processes for evidence it may be running in a sandbox environment. It specifically enumerates processes for Wireshark and Sysinternals.[^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE can obtain a list of running processes on the system.[^1]  |
| [S0273](https://attack.mitre.org/software/S0273) | Socksbot | Socksbot can list all running processes.[^1]  |
| [S0277](https://attack.mitre.org/software/S0277) | FruitFly | FruitFly has the ability to list processes on the system.[^1]  |
| [S0278](https://attack.mitre.org/software/S0278) | iKitten | iKitten lists the current processes running.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can query and kill system processes.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda checks for running processes on the victim’s machine.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can list the current running processes on the system.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can discover running processes on compromised machines.[^1] <br> |
| [S0333](https://attack.mitre.org/software/S0333) | UBoatRAT | UBoatRAT can list running processes on the system.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can list active processes running on the victim’s machine.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon can list the processes on the victim’s machine.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can collect a list of running processes by calling CreateToolhelp32Snapshot.[^1] [^2]  |
| [S0345](https://attack.mitre.org/software/S0345) | Seasalt | Seasalt has a command to perform a process listing.[^1]  |
| [S0346](https://attack.mitre.org/software/S0346) | OceanSalt | OceanSalt can collect the name and ID for every process running on the system.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT contains watchdog functionality that ensures its process is always running, else spawns a new instance.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can obtain a list of processes running on the system.[^1] [^2]  |
| [S0355](https://attack.mitre.org/software/S0355) | Final1stspy | Final1stspy obtains a list of running processes.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has used the command `cmd /c tasklist` to get a snapshot of the current processes on the target machine.[^1] [^2]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can find information about processes running on local and remote systems.[^2] [^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has been observed enumerating local processes.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth searches for different processes on the system.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can search a list of running processes for Tr.exe.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has gathered information about running processes.[^1] [^2]  |
| [S0393](https://attack.mitre.org/software/S0393) | PowerStallion | PowerStallion has been used to monitor process lists.[^1]  |
| [S0396](https://attack.mitre.org/software/S0396) | EvilBunny | EvilBunny has used EnumProcesses() to identify how many process are running in the environment.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete has a component to check for running processes to look for web browsers.[^1]   |
| [S0410](https://attack.mitre.org/software/S0410) | Fysbis | Fysbis can collect information about running processes.[^1]   |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell has a command, ps, to obtain a listing of processes on the system.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has executed the `tasklist` command.[^1] 	 |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has the ability to list all running processes.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to list running processes on the infected host.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to list processes on the compromised host.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to list processes on the infected host.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has the ability to deploy a reconnaissance module to retrieve a list of the active processes.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] listed all running processes on the machine.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has called `CreateToolhelp32Snapshot` to enumerate all running processes.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can enumerate all running processes and process information on an infected machine.[^1] 	 |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has gathered all of the running system processes.[^1] 	 |
| [S0451](https://attack.mitre.org/software/S0451) | LoudMiner | LoudMiner used the `ps` command to monitor the running processes on the system.[^1] 	 |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can use `tasklist` to gather information about the process running on the infected system.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has performed process name checks and has monitored applications.[^1]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to enumerate loaded modules for a process.[^1] . |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can gather a list of running processes by using [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]].[^1]  |
| [S0460](https://attack.mitre.org/software/S0460) | Get2 | Get2 has the ability to identify running processes on an infected host.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot can enumerate a list of running processes on a compromised machine.[^1]  |
| [S0464](https://attack.mitre.org/software/S0464) | SYSCON | SYSCON has the ability to use [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] to list running processes.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to identify running processes and associated plugins on an infected host.[^1]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has monitored critical processes to ensure resiliency.[^1]   |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to list running processes on a compromised host.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to use [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] to identify running processes.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to enumerate running processes on a compromised host.[^1]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has checked for the Google Updater process to ensure Goopy was loaded properly.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore has used the `ps` command to list processes.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has collected a list of running processes.[^1]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan can use the `ps` command to discover other cryptocurrency miners active on the system.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can determine if a user is logged in by checking to see if explorer.exe is running.[^1]  |
| [S0497](https://attack.mitre.org/software/S0497) | Dacls | Dacls can collect data on running and parent processes.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can iterate over the running processes to find a suitable injection target.[^1]  |
| [S0503](https://attack.mitre.org/software/S0503) | FrameworkPOS | FrameworkPOS can enumerate and exclude selected processes on a compromised host to speed execution of memory scraping.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can list running processes on the localhost.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can enumerate processes on a victim machine through use of [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]].[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint can iterate through running processes every six seconds collecting a list of processes to capture from later.[^1] 	 |
| [S0528](https://attack.mitre.org/software/S0528) | Javali | Javali can monitor processes for open browsers and custom banking applications.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can identify installed security tools based on process names.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can identify the process that owns remote connections.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has enumerated processes by ID, name, or privileges.[^1]   |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can identity the current process on a compromised host.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected a list of process names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists.[^1]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT monitored running processes for instances of `MsBuild.exe` by hashing the name of each running process and comparing it to the corresponding value `0x53D525`. It also extracted command-line arguments and individual arguments from the running `MsBuild.exe` process to identify the directory path of the Orion software Visual Studio solution.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack’s dropper can list all running processes.[^1] [^2]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can gather a list of processes running on the machine.[^1]   |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can enumerate through all open processes to search for any that have the string “sql” in their process name.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can identify the process for a specific security product.[^1]  |
| [[kb/mitre/attack/software/S0581-ironnetinjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can identify processes via C# methods such as `GetProcessesByName` and running [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] with the Python `os.popen` function.[^1]  |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can list running processes.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can execute `ProcessList` for process discovery.[^1]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest obtains a list of running processes using the function `kill_unwanted`.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has collected the PID of a malicious process.[^1]  |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing has used ps to list processes.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has searched for the current process’s PID.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS looks for processes from a hard-coded list.[^1] [^2] [^3]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit can enumerate all running processes to compare hashes.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk has called `GetCurrentProcess`.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can enumerate all processes on the victim's machine.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can use the `getprocesslist` command to enumerate processes on a compromised host.[^1] [^2] [^3]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY can search for specific processes to terminate.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can enumerate the current process on a compromised host.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can enumerate processes running on a victim's machine.[^1]  |
| [S0626](https://attack.mitre.org/software/S0626) | P8RAT | P8RAT can check for specific processes associated with virtual environments.[^1]  |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster can search a list of running processes.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can enumerate processes on a target system.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae can enumerate processes on a target system.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk has the ability to check running processes on a targeted system.[^1] [^2] [^3]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has collected information about running processes.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can check for blocklisted process names on a compromised host.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to check running processes.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can search for different processes on a system.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can collect process filenames and SID authority level.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has used `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next` API calls to enumerate the running processes in the system.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can enumerate processes on a targeted system.[^1]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb's loader can enumerate all Common Language Runtimes (CLRs) and running Application Domains in the compromised AD FS server's `Microsoft.IdentityServer.ServiceHost.exe` process.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can identify processes based on PID.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect information about running processes.[^1]  |
| [S0664](https://attack.mitre.org/software/S0664) | Pandora | Pandora can monitor processes on a compromised host.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can enumerate running processes.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can obtain a list of processes on a compromised host.[^1]  |
| [S0672](https://attack.mitre.org/software/S0672) | Zox | Zox has the ability to list processes.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower has the ability to list running processes through the use of `tasklist`.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has a plugin designed to obtain a list of processes.[^2] [^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can enumerate the process it is currently running under.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can check if a specific process is running, such as Kaspersky's `avp.exe`.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^1]  |
| [S0693](https://attack.mitre.org/software/S0693) | CaddyWiper | CaddyWiper can obtain a list of current processes.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can enumerate and examine running processes to determine if a debugger is present.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] includes subprojects that enumerate and identify information about [[kb/mitre/attack/techniques/T1055-process-injection\|Process Injection]] candidates.[^1] 	 |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to run the `tasklist` command on a compromised system.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ has created a snapshot of running processes using `CreateToolhelp32Snapshot`.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can enumerate running processes.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can identify running processes on a compromised host.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has enumerated running processes on a compromised host to determine if it is running under the process name `dfrgui.exe`.[^1]  |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can gather process information.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can identify processes associated with analytical tools.[^2] [^1] [^3]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream has the ability to discover processes, including `Bka.exe` and `BkavUtil.exe`.[^1]  |
| [S1048](https://attack.mitre.org/software/S1048) | macOS.OSAMiner | macOS.OSAMiner has used `ps ax \| grep <name> \| grep -v grep \| ...` and `ps ax \| grep -E...` to conduct process discovery.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can obtain a list of running processes on a compromised host.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has discovered system processes by calling `RmGetList`.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can enumerate the processes that run on the platform.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can enumerate running processes on a machine.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can enumerate all processes and locate specific process IDs (PIDs).[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can collect a list of running processes from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can call `NtQuerySystemProcessInformation` with `SystemProcessInformation` to enumerate all running processes, including associated information such as PID, parent PID, image name, and owner.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can enumerate a list of running processes on a compromised system.[^1]  |
| [S1072](https://attack.mitre.org/software/S1072) | Industroyer2 | Industroyer2 has the ability to cyclically enumerate running processes such as PServiceControl.exe, PService_PDD.exe, and other targets supplied through a hardcoded configuration.[^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can use `GetCurrentProcess` to enumerate processes.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can enumerate current running processes on the targeted machine.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro can monitor the `/proc/[PID]` directory of known RotaJakiro processes as a part of its persistence when executing with non-root permissions. If the process is found dead, it resurrects the process. RotaJakiro processes can be matched to an associated Advisory Lock, in the `/proc/locks` folder, to ensure it doesn't spawn more than one process.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can retrieve a list of running processes from a compromised machine.[^1]   |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to execute the `tasklist` command.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can examine running processes to determine if a debugger is present.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub has the ability to use `GetWindowThreadProcessId` to identify the process behind a specified window.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can enumerate processes on a targeted host.[^1] [^2]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER will query running process information to determine subsequent program execution flow.[^1]  |
| [S1107](https://attack.mitre.org/software/S1107) | NKAbuse | NKAbuse will check victim systems to ensure only one copy of the malware is running.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate performs various checks for running processes, including security software by looking for hard-coded process name values.[^1] [^2]   |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can identify running processes and their names.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu can enumerate the running processes on a compromised host.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can list processes on targeted hosts.[^1]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira verifies the deletion of volume shadow copies by checking for the existence of the process ID related to the process created to delete these items.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin can identify processes running on the victim machine, such as security software, during execution.[^1] [^2]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper can identify the process it is currently running under and its number, and pass this back to a command and control node.[^1]  |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle retrieves a list of all running processes on a victim host, and stops all services containing the string "sql," likely to propagate ransomware activity to database files.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can use the Microsoft Win32 Restart Manager to kill processes with a specific handle or that are accessing resources it wants to encrypt.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb has used shell commands to list running processes.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes a module for establishing a process watchdog for itself, identifying if the MgBot process is still running.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor can collect information on installed applications via Windows registry keys, as well as collecting information on running processes.[^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can check if a process name contains “creensaver.”[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can use `ps aux` to enumerate running processes.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can enumerate running processes.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus can enumerate running processes including process grandchildren on targeted hosts.[^2] [^3] [^1]  |
| [S1164](https://attack.mitre.org/software/S1164) | UPSTYLE | UPSTYLE has the ability to read `/proc/self/cmdline` to see if it is running as a monitored process.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker checks whether the Bitlocker Drive Encryption Tools service is running.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | If sent the command `16002`, LightSpy uses the `NSWorkspace runningApplications()` method to collect the process ID, path to the executable, bundle information, and the filename of the executable for all running applications.[^1]  |
| [S1191](https://attack.mitre.org/software/S1191) | Megazord | Megazord can terminate a list of specified services and processes.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can determine if a running process has administrative privileges and terminate processes that interfere with encryption or exfiltration.[^1] [^2]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can identify and terminate specific services.[^2] [^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex identifies the `explorer.exe` process on the executing system.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can stop processes associated with files currently in use to maximize the impact of encryption.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has used `tasklist` to gather running processes on victim host.[^1]  PUBLOAD has also leveraged the `OpenEventA` Windows API function to check whether the same process was already running.[^2]   |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can enumerate processes on targeted hosts.[^2] [^1] [^3]  |
| [S1230](https://attack.mitre.org/software/S1230) | HIUPAN | HIUPAN has conducted process discovery to identify the PUBLOAD malware under the process WCBrowserWatcher.exe and will launch it from an install directory if it is not found.[^1]  |
| [S1233](https://attack.mitre.org/software/S1233) | PAKLOG | PAKLOG has detected and logged the full path of processes active in the foreground using Windows API calls.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has checked the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler.[^2]  TONESHELL has also searched for running antivirus processes to include ESET’s antivirus associated executables ekrn.exe and egui.exe.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can define specific processes to be terminated or left alone at execution.[^3] [^4] [^1] [^2] [^6] [^5]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has utilized an encoded list of the processes that it detects and terminates.[^1] [^2] [^3]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has the capability to query installed programs and running processes.[^1]  InvisibleFerret has also identified running processes using the Python project “psutil”.[^2]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has utilized MS4Killer to detect running processes on the victim device.[^2]  Embargo has also captured a snapshot of active running processes using the Windows API `CreateToolHelp32Snapshot()`.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has the ability to enumerate running processes.[^1]    |
| [S9012](https://attack.mitre.org/software/S9012) | TRAILBLAZE | TRAILBLAZE has conducted process discovery by searching for specific named processes such as `/home/bin/web`.[^1] [^2]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has the ability to check if it is running as an active child process through the detection of a specific environment variable.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can enumerate processes on compromised hosts.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can kill a process using specific process ID.[^1] [^2]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can check running processes against a list of blocklisted applications.[^1] <br> |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has searched for running processes to include web or dsmdm.[^1] [^2]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag AshenOrchestrator component has process management functionality.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has the ability to collect running processes.[^1]      |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can gather process information on targeted systems.[^1] [^2]  |
| [S9036](https://attack.mitre.org/software/S9036) | LP-Notes | LP-Notes has searched for the process taskhostw.exe.[^1]  |

 [^1]: [show_processes_cisco_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_monitor_permit_list_through_show_process_memory.html#wp3599497760)
 [^2]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^3]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^4]: [Sygnia ESXi Ransomware 2025](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)
 [^5]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^6]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^7]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^8]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^9]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^10]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^11]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^12]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^13]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^14]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^15]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^16]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
 [^17]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^18]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^19]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^20]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^21]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^22]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
 [^23]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^24]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^25]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)
 [^26]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^27]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
 [^28]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^29]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^30]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^31]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^32]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^33]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^34]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^35]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^36]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^37]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^38]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
 [^39]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
 [^40]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)
 [^41]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
 [^42]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^43]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^44]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^45]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^46]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^47]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^48]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^49]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^50]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^51]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^52]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^53]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^54]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^55]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^56]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^57]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^58]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^59]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^60]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^61]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^62]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^63]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^64]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^65]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
 [^66]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)
 [^67]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^68]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^69]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^70]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^71]: [ESET BlackEnergy Jan 2016](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)
 [^72]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^73]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)
 [^74]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^75]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^76]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^77]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)
 [^78]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^79]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^80]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^81]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^82]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^83]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^84]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^85]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^86]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^87]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^88]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
 [^89]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^90]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^91]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^92]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^93]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
 [^94]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^95]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
 [^96]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
 [^97]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)
 [^98]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
 [^99]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^100]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^101]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^102]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^103]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
 [^104]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^105]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^106]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^107]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^108]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^109]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^110]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)
 [^111]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^112]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
 [^113]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^114]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^115]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^116]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^117]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^118]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^119]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^120]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^121]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^122]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^123]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^124]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^125]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^126]: [Donut Github](https://github.com/TheWover/donut)
 [^127]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^128]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
 [^129]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^130]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)
 [^131]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^132]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^133]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^134]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^135]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^136]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^137]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
 [^138]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^139]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^140]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^141]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^142]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^143]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^144]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^145]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^146]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^147]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
 [^148]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^149]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)
 [^150]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^151]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^152]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^153]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^154]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^155]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^156]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^157]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^158]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)
 [^159]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
 [^160]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
 [^161]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^162]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^163]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^164]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^165]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
 [^166]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^167]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)
 [^168]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
 [^169]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
 [^170]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^171]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^172]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^173]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
 [^174]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^175]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^176]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^177]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^178]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^179]: [Industroyer2 Mandiant April 2022](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)
 [^180]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^181]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^182]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^183]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
 [^184]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^185]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^186]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^187]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^188]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^189]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^190]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^191]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^192]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^193]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^194]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^195]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^196]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^197]: [Cato LAMEHUG JUL 2025](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)
 [^198]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^199]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^200]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^201]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^202]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^203]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
 [^204]: [ESET Trickbot Oct 2020](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)
 [^205]: [Bitdefender Trickbot March 2020](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)
 [^206]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^207]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
 [^208]: [FireEye Hacking Team](https://www.fireeye.com/blog/threat-research/2015/07/demonstrating_hustle.html)
 [^209]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^210]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^211]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^212]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^213]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^214]: [CISA RansomHub AUG 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
 [^215]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^216]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^217]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^218]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^219]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^220]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^221]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^222]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^223]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
 [^224]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
 [^225]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
 [^226]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
 [^227]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
 [^228]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)
 [^229]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^230]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^231]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^232]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^233]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^234]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^235]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^236]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^237]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^238]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
 [^239]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^240]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^241]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^242]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^243]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^244]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^245]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^246]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^247]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^248]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^249]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^250]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^251]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^252]: [Palo Alto MidnightEclipse APR 2024](https://unit42.paloaltonetworks.com/cve-2024-3400/)
 [^253]: [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)
 [^254]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^255]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^256]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^257]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^258]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
 [^259]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^260]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^261]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^262]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^263]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^264]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^265]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^266]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^267]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^268]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^269]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
 [^270]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^271]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^272]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^273]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^274]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^275]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^276]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^277]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
 [^278]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
 [^279]: [ASEC Emotet 2017](https://global.ahnlab.com/global/upload/download/asecreport/ASEC%20REPORT_vol.88_ENG.pdf)
 [^280]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^281]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
 [^282]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^283]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
 [^284]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^285]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^286]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^287]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^288]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^289]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^290]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^291]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^292]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^293]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^294]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^295]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^296]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
 [^297]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^298]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^299]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^300]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^301]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^302]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^303]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
 [^304]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^305]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^306]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^307]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^308]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
 [^309]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^310]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^311]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^312]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^313]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
 [^314]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^315]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^316]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^317]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
