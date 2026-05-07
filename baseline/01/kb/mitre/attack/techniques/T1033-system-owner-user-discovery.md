---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1033
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1033-system-owner-user-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [[kb/mitre/attack/techniques/T1003-os-credential-dumping|OS Credential Dumping]]. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery|System Owner/User Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.<br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands such as `show users` and `show ssh` can be used to display users currently logged into the device.[^1] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has the ability to gather the username from the victim’s machine.[^1]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe collects the username from the victim’s machine.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to gather the username from the system.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | A Linux version of Derusbi checks if the victim user ID is anything other than zero (normally used for root), and the malware will not execute if it does not have root privileges. Derusbi also gathers the username of the victim.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to identify the users on a compromised host.[^1]  |
| [S0058](https://attack.mitre.org/software/S0058) | SslMM | SslMM sends the logged-on username to its hard-coded C2.[^1]  |
| [S0059](https://attack.mitre.org/software/S0059) | WinMM | WinMM uses NetUser-GetInfo to identify that it is running under an “Admin” account on the local system.[^1]  |
| [S0060](https://attack.mitre.org/software/S0060) | Sys10 | Sys10 collects the account name of the logged-in user and sends it to the C2.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type runs tests to determine the privilege level of the compromised user.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type has run tests to determine the privilege level of the compromised user.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic collects the user name from the victim’s machine.[^1]  |
| [S0092](https://attack.mitre.org/software/S0092) | Agent.btz | Agent.btz obtains the victim username and saves it to a file.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea collects the current username from the victim.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can gather information about the user on a compromised host.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 gathers and beacons the username of the logged in account during installation. It will also gather the username of running processes to determine if it is running as SYSTEM.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects information from the victim about the current user name.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can identify the user on a targeted system.[^2] [^1] [^3]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can obtain information about the current user.[^1]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger can obtain information about the victim usernames.[^1]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has commands to get the current user's name and SID.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can obtain the victim username and permissions.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind obtains the victim username.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can obtain information about the logged on user both locally and for Remote Desktop sessions.[^1]  |
| [S0155](https://attack.mitre.org/software/S0155) | WINDSHIELD | WINDSHIELD can gather the victim user name.[^1]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the getInfoOSX function to return the OS X version as well as the current user.[^1]  |
| [S0162](https://attack.mitre.org/software/S0162) | Komplex | The OsInfo function in Komplex collects the current running username.[^1]  |
| [S0168](https://attack.mitre.org/software/S0168) | Gazer | Gazer obtains the current user's security identifier.[^1]  |
| [S0171](https://attack.mitre.org/software/S0171) | Felismus | Felismus collects the current username and sends it to the C2 server.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Reaver collects the victim's username.[^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may collect information about the currently logged in user by running `whoami` on a victim.[^1]  |
| [S0186](https://attack.mitre.org/software/S0186) | DownPaper | DownPaper collects the victim username and sends it to the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can obtain the victim user name.[^1]  |
| [S0214](https://attack.mitre.org/software/S0214) | HAPPYWORK | can collect the victim user name.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can gather information on the victim username.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS has the ability to identify the username on the compromised host.[^1]  |
| [S0228](https://attack.mitre.org/software/S0228) | NanHaiShu | NanHaiShu collects the username from the victim.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects registered owner details by using the commands `systeminfo` and `net config workstation`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT collects the victim username along with other account information (account type, description, full name, SID and status).[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can collect the username from a compromised host.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA runs the `whoami` and `query user` commands.[^1]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck gathers user names from infected hosts.[^1]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty collects the victim’s username.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon collects the endpoint victim's username and uses it as a basis for downloading additional components from the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can identify logged in users across the domain and views user sessions.[^2] [^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy gets the username from the system.[^1] [^2]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito runs `whoami` on the victim’s machine.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN gathers the username from the victim’s machine.[^1]  |
| [S0258](https://attack.mitre.org/software/S0258) | RGDoor | RGDoor executes the `whoami` on the victim’s machine.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole lists local users and session information.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can enumerate the username and account type.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar gathers information on users.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can identify the user and groups the user belongs to on a compromised host.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT collects the username from the victim’s machine.[^2] [^1]  |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT gathers the victim username.[^1]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin collects the victim’s username and whether that user is an admin.[^1]  |
| [S0272](https://attack.mitre.org/software/S0272) | NDiskMonitor | NDiskMonitor obtains the victim username and encrypts the information to send over its C2 channel.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT has the capability to collect the current logged on user’s username from a machine.[^1]  |
| [S0280](https://attack.mitre.org/software/S0280) | MirageFox | MirageFox can gather the username from the victim’s machine.[^1]  |
| [S0284](https://attack.mitre.org/software/S0284) | More_eggs | More_eggs has the capability to gather the username from the victim's machine.[^1] [^2]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can collect the username from the victim’s machine.[^1] [^2] [^3]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can enumerate the username on targeted hosts.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet gathers the username from the victim’s machine.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia collects the username from the victim’s machine.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can collect the username from the victim’s machine.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can collect the username from the victim’s machine.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can collect the username from a victim machine.[^1]  |
| [S0350](https://attack.mitre.org/software/S0350) | zwShell | zwShell can obtain the name of the logged-in user on the victim.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can gather the username from the system.[^1]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI can collect the username from the victim’s machine.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis enumerates and collects the username from the victim’s machine.[^1] [^2]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can collect the username from the victim’s machine.[^1]  |
| [S0362](https://attack.mitre.org/software/S0362) | Linux Rabbit | Linux Rabbit opens a socket on port 22 and if it receives a response it attempts to obtain the machine's hostname and Top-Level Domain. [^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate the username on targeted hosts.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has enumerated all users connected to network shares. |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp uses the `whoami` command. [^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT gathers the username from the system.[^1]  |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy enumerates the current user during the initial infection.[^2] [^1]  |
| [S0382](https://attack.mitre.org/software/S0382) | ServHelper | ServHelper will attempt to enumerate the username of the victim.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT enumerates the current user during the initial infection.[^1]  |
| [S0391](https://attack.mitre.org/software/S0391) | HAWKBALL | HAWKBALL can collect the user name of the system.[^1]  |
| [S0401](https://attack.mitre.org/software/S0401) | Exaramel for Linux | Exaramel for Linux can run `whoami` to identify the system owner.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can collect the owner and organization information from the target workstation.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has executed the `whoami` command.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT sent username, computer name, and the previously generated UUID in reply to a "who" command from C2.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to collect the username on the infected host.[^1]  |
| [S0433](https://attack.mitre.org/software/S0433) | Rifdoor | Rifdoor has the ability to identify the username on the compromised host.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum can collect the victim username.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has the ability to identify the current user on the infected host.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has the ability to discover the username on the infected host.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can detect the username of the infected host.[^1] 	 |
| [S0450](https://attack.mitre.org/software/S0450) | SHARPSTATS | SHARPSTATS has the ability to identify the username on the compromised host.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has collected the username from the victim's machine.[^1]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to identify the username on a compromised host.[^1]  |
| [S0459](https://attack.mitre.org/software/S0459) | MechaFlounder | MechaFlounder has the ability to identify the username and hostname on a compromised host.[^1]  |
| [S0460](https://attack.mitre.org/software/S0460) | Get2 | Get2 has the ability to identify the current username of an infected host.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to identify the user on a compromised host.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can gather information regarding the user.[^1]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has the ability to enumerate the infected system's user name.[^1]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan has discovered the username of the user running the backdoor.[^1]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic can gather data on the user of a compromised host.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke can enumerate the account name on a targeted system.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can collect the username on the victim machine to send to C2.[^1]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can identify the current username on the victim system.[^1]  |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can collect information on user sessions.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can collect the username from the victim's machine.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer has the ability to identify the username on a compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has collected the username from a victim machine.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can identify the username of the infected user.[^1]  |
| [S0543](https://attack.mitre.org/software/S0543) | Spark | Spark has run the whoami command and has a built-in command to identify the user logged in.[^1]   |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has used tools to gather information about users.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected the username from a compromised host.[^1] [^2]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can obtain the username from the victim's machine.[^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has collected the username from the infected host.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can obtain a list of user accounts from a victim's machine.[^1]  |
| [[kb/mitre/attack/software/S0590-nbtscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-nbtscan\|NBTscan]] can list active users on the system.[^1] [^2] 	 |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has collected the username of the victim system.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist can collect the username on a targeted system.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can execute `getinfo`  to identify the username on a compromised host.[^1] [^2]  |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster can identify the username on a compromised host.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has collected the username and UID from the infected machine.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can identify the user id on a target machine.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can enumerate the username on a compromised host.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can check for blocklisted usernames on infected endpoints.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can retrieve usernames.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has used `whoami` commands to identify system owners.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can identify the user name on a compromised system.[^2] [^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can retrieve the victim’s username.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can collect the username on a compromised host.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can collect the username from a compromised host.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can identify the username on a compromised host.[^1] [^2]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can gather system owner information, including user and administrator privileges.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect the username from a compromised host.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium has the ability to distinguish between a standard user and an administrator on a compromised host.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can retrieve the username from a targeted system.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman has collected the username from a victim machine.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower can determine if the current user has admin privileges.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can collect the username from the system.[^1] [^2]   |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can collect the user name from a victim's machine.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can gather a list of logged on users.[^1]   |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can obtain a list of users from an infected machine.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to run the `whoami` command on the system.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ can collect the username from a compromised host.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can identify users registered to a targeted machine.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can collect the username from the compromised machine.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can collect the username from a compromised host.[^1]  |
| [S1021](https://attack.mitre.org/software/S1021) | DnsSystem | DnsSystem can use the Windows user name to create a unique identification for infected users and systems.[^1]  |
| [S1024](https://attack.mitre.org/software/S1024) | CreepySnail | CreepySnail can execute `getUsername` on compromised systems.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has collected the user name from a compromised host using `GetUserNameA`.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT |  Action RAT has the ability to collect the username from an infected host.[^1]  |
| [S1029](https://attack.mitre.org/software/S1029) | AuTo Stealer | AuTo Stealer has the ability to collect the username from an infected host.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle can collect the user name from a compromised host.[^1]  |
| [S1032](https://attack.mitre.org/software/S1032) | PyDCrypt | PyDCrypt has probed victim machines with `whoami` and has collected the username from the machine.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can collect the user name from the victim's machine.[^1]  |
| [S1035](https://attack.mitre.org/software/S1035) | Small Sieve | Small Sieve can obtain the id of a logged in user.[^1]  |
| [S1037](https://attack.mitre.org/software/S1037) | STARWHALE | STARWHALE can gather the username from an infected host.[^2] [^1]   |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee has the ability to identify the user name.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream has the ability to gather user information from the targeted system using `whoami/upn&whoami/fqdn&whoami/logonid&whoami/all`.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can collect the username from a compromised host.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can collect the username from a compromised host.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can collect the username from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can retrieve a list of user accounts and usernames from an infected machine.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can utilize `net use` commands to discover the user name on a compromised host.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can conduct basic network reconnaissance on the victim machine with `whoami`, to get user details.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can obtain logged user information from a compromised machine and can execute the command `whoami.exe`.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check if the current user of a compromised system is an administrator. [^1]  |
| [S1106](https://attack.mitre.org/software/S1106) | NGLite | NGLite will run the `whoami` command to gather system information and return this to the command and control server.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can use `whoami` to obtain the username from a compromised host.[^1] [^2] [^3]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin determines whether it is successfully running on a victim system by querying the running account information to determine if it is running in Session 0, indicating running with elevated privileges.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can collect user information from the targeted host.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for identifying local users and administrators on victim machines.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor gathers information on victim system users and usernames.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer gathers information on the infected system owner and user.[^3] [^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP has included the victim's computer name and username in C2 messages sent to actor-owned infrastructure.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can discover and send the username from a compromised host to C2.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can discover the username of an infected host.[^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango can collect the user name from a compromised system which is used to create a unique victim identifier.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can identify the compromised system's username which is then used as part of a unique identifier.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can identify the username from a victim machine.[^1]  |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has obtained the username from an infected host. [^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has obtained the username from an infected host.[^1] [^2] [^3] [^4]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can trigger exection of `whoami` on the target host to display the current user.[^1] [^2]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has obtained the username from an infected host.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has obtained the username from the victim’s machine.[^1] [^2] [^3]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has identified the user’s UUID and username through the "pay" module.[^1] [^2] [^3]   |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader has collected the username from the victim host.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has collected the username from the victim host.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can retrieve the username from targeted machines.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can identify the associated username on targeted machines.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can collect the username associated with the compromised host.[^1] <br> |
| [S9029](https://attack.mitre.org/software/S9029) | IronWind | IronWind can enumerate the username on victim's systems.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can use `whoami` to enumerate the system user.[^1]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has gathered the victim machine’s username.[^1]     |

 [^1]: [show_ssh_users_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html)
 [^2]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)
 [^3]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^4]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^5]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^6]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^7]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^8]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^9]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^10]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
 [^11]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)
 [^12]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^13]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
 [^14]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^15]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^16]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^17]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^18]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^19]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^20]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^21]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^22]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
 [^23]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^24]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^25]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^26]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^27]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^28]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^29]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^30]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^31]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)
 [^32]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
 [^33]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^34]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^35]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^36]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^37]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^38]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^39]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^40]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^41]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^42]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)
 [^43]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^44]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^45]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^46]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^47]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^48]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
 [^49]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^50]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^51]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^52]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^53]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
 [^54]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^55]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^56]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^57]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^58]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^59]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^60]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^61]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^62]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^63]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^64]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^65]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^66]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^67]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^68]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^69]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^70]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
 [^71]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^72]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^73]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^74]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^75]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
 [^76]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^77]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^78]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^79]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
 [^80]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^81]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^82]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^83]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^84]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^85]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^86]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^87]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^88]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^89]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^90]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^91]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^92]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^93]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^94]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^95]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^96]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
 [^97]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^98]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^99]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^100]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^101]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^102]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^103]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
 [^104]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^105]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^106]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
 [^107]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^108]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
 [^109]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^110]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^111]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^112]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^113]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
 [^114]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^115]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^116]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^117]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
 [^118]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^119]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^120]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^121]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^122]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
 [^123]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^124]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^125]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)
 [^126]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^127]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^128]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^129]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^130]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^131]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^132]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
 [^133]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
 [^134]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^135]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^136]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^137]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^138]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)
 [^139]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^140]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)
 [^141]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^142]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
 [^143]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
 [^144]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^145]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
 [^146]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^147]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^148]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^149]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^150]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^151]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^152]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^153]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^154]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
 [^155]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
 [^156]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^157]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^158]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^159]: [Securelist Denis April 2017](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)
 [^160]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^161]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^162]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
 [^163]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^164]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^165]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^166]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^167]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)
 [^168]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^169]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^170]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
 [^171]: [Acronis XLoader 2021](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)
 [^172]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^173]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^174]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^175]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^176]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)
 [^177]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^178]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^179]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^180]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^181]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^182]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^183]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^184]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^185]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^186]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^187]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^188]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^189]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^190]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^191]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^192]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^193]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^194]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^195]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^196]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^197]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
 [^198]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^199]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^200]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^201]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
 [^202]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
 [^203]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^204]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^205]: [fsecure NanHaiShu July 2016](https://www.f-secure.com/documents/996508/1030745/nanhaishu_whitepaper.pdf)
 [^206]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^207]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^208]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^209]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^210]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^211]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
