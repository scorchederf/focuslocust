---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1041
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel
tactic:
    - Exfiltration
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has exfiltrated stolen data and files to its C2 server.[^1] [^2]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to send information staged on a compromised host externally to C2.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | Adversaries can direct BACKSPACE to upload files to the C2 Server.[^1]  |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | NETEAGLE is capable of reading files over the C2 channel.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL exfiltrates data over the same channel used for C2.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky has exfiltrated data to the C2 server.[^1]  |
| [S0077](https://attack.mitre.org/software/S0077) | CallMe | CallMe exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |
| [S0078](https://attack.mitre.org/software/S0078) | Psylo | Psylo exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat has uploaded files and data to its C2 servers.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has transmitted collected files and data to its C2 server.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type has uploaded data and files from a compromised host to its C2 servers.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has sent data and files from a compromised host to its C2 servers.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can exfiltrate stolen information over its C2.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon exfiltrates screenshot files to its C2 server.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook can upload files from a victim's machine over the C2 channel.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc performs data exfiltration over the control server channel using a custom protocol.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot exfiltrates data over its C2 channel.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can send collected files back over same C2 channel.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy has exfiltrated data to the designated C2 server using HTTP POST requests.[^1] [^2]   |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE can upload files from the victim's machine to its C2 server.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can send information about the compromised host and upload data to a hardcoded C2 server.[^1] [^2]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal |  Bisonal has added the exfiltrated data to the URL over the C2 channel.[^1]   |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus has uploaded stolen files and data from a victim's machine over its C2 channel.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon exfiltrates collected data over email via SMTP/S and POP3/S C2 channels.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has sent data and files to its C2 server.[^1] [^3] [^2]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can send data gathered from a target through the command and control channel.[^2] [^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has exfiltrated data over its C2 channel.[^2] [^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth exfiltrates collected information from its r1.log file to the external C2 server. [^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi performs exfiltration over [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]], which is also used for the C2 channel.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has used its C2 channel to exfiltrate data.[^1] 	 |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury exfiltrates a list of outbound and inbound SSH sessions using OpenSSH's `known_host` files and `wtmp` records. Ebury can exfiltrate SSH credentials through custom DNS queries or use the command `Xcat` to send the process's ssh session's credentials to the C2 server.[^1] [^2]   |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy has sent data collected from a compromised host to its C2 servers.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT has used C2 infrastructure to receive stolen information from the infected machine including screenshots and other system information.[^2] [^1] 	 |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used HTTP POSTs to exfil gathered information.[^1] [^3] [^2]  |
| [S0391](https://attack.mitre.org/software/S0391) | HAWKBALL | HAWKBALL has sent system information and files over the C2 channel.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron exfiltrates data over its email C2 channel.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete's collected data is exfiltrated over the same channel used for C2.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has exfiltrated data over the C2 channel.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to download files from the infected host to the command and control (C2) server.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has uploaded a file containing debugger logs, network information and system information to the C2.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has exfiltrated data over the C2 channel.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Data exfiltration is done by Okrum using the already opened channel with the C2 server.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has used a PowerShell document stealer module to pack and exfiltrate .txt, .pdf, .xls or .doc files smaller than 5MB that were modified during the past two days.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] sent generated reports to the C2 via HTTP POST requests.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has the ability to initiate contact with command and control (C2) to exfiltrate stolen data.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can send data gathered from the infected machine via HTTP POST request to the C2.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo can send the data it collects to the C2 server.[^1]   |
| [S0459](https://attack.mitre.org/software/S0459) | MechaFlounder | MechaFlounder has the ability to send the compromised user's account name and hostname within a URL to C2.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has sent collected data from a compromised host to its C2 servers.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to send collected files over its C2.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to exfiltrate data over the C2 channel.[^3] [^1] [^2]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has the ability to exfiltrate data over the Microsoft Outlook C2 channel.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has exfiltrated data via HTTP to already established C2 servers.[^1] [^2]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has exfiltrated information gathered from the infected system to the C2 server.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can exfiltrate collected documents through C2 channels.[^1] [^2]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy has exfiltrated host environment information to an external C2 domain via port 9006.[^1] 	 |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT can exfiltrate data gathered from the infected system via the established Exchange Web Services API C2 channel.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can exfiltrate host and malware information to C2 servers.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub can exfiltrate files over C2 infrastructure.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has sent user and system information to a C2 server via HTTP POST requests.[^1] [^2]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can exfiltrate collected information from the host to the C2 server.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can send data it retrieves to the C2 server.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has sent system information to a C2 server via HTTP and HTTPS POST requests.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch can exfiltrate data over the primary C2 channel (Dropbox HTTP API).[^1]  |
| [S0543](https://attack.mitre.org/software/S0543) | Spark | Spark has exfiltrated data over the C2 channel.[^1]   |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can upload files over the C2 channel from the infected host.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can upload files over the C2 channel.[^1]   |
| [S0584](https://attack.mitre.org/software/S0584) | AppleJeus | AppleJeus has exfiltrated collected host information to a C2 server.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can execute the command code `do_upload` to send files to C2.[^1]  |
| [S0588](https://attack.mitre.org/software/S0588) | GoldMax | GoldMax can exfiltrate files over the existing C2 channel.[^1] [^2]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest exfiltrates targeted file extensions in the `/Users/` folder to the command and control server via unencrypted HTTP. Network packets contain a string with two pieces of information: a file path and the contents of the file in a base64 encoded string.[^1] [^2]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has used Ngrok to establish C2 and exfiltrate data.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet sends compromised victim information via HTTP.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer sends information about hardware profiles and previously-received commands back to the C2 server in a POST-request.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has exfiltrated data over its C2 channel.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has uploaded collected data and files from a compromised host to its C2 server.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can exfiltrate files via the C2 channel.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent has sent data related to a compromise host over its C2 channel.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can exfiltrate files from the victim using the `download` command.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has exfiltrated data to its C2 server.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can send stolen information to C2 nodes including passwords, accounts, and emails.[^1]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon uploads files and data from a compromised host over the existing C2 channel.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can exfiltrate locally stored data via its C2.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT has exfiltrated data over its C2 channel.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET retrieves files that match the pattern defined in the INAME_QUERY variable within the user's home directory, such as `*test.txt`, and are below a specific size limit. It then archives the files and exfiltrates the data over its C2 channel.[^1] [^2]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can remotely exfiltrate sensitive information from a compromised AD FS server.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate has exfiltrated data over its C2 channel.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can exfiltrate collected data via C2.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can send collected victim data to its C2 server.[^1]  |
| [S0671](https://attack.mitre.org/software/S0671) | Tomiris |  Tomiris can upload files matching a hardcoded set of extensions, such as .doc, .docx, .pdf, and .rar, to its C2 server.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can exfiltrate gathered data to a hardcoded C2 URL via HTTP POST.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma can send victim data to an actor-controlled C2 server.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower can send collected data, including screenshots, over its C2 channel.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink has the ability to upload exfiltrated files to a C2 server.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can transfer files from an infected host to the C2 server.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has exfiltrated data to the C2 server.[^1]   |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa exfiltrates data from a supplied path over its C2 channel.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can upload files from a compromised host over its C2 channel.[^1]   |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark has the ability to upload files from the compromised host over a DNS or HTTP C2 channel.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can send data from the victim host through a DNS C2 channel.[^1]  |
| [S1021](https://attack.mitre.org/software/S1021) | DnsSystem | DnsSystem can exfiltrate collected data to its C2 server.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | IceApple's Multi File Exfiltrator module can exfiltrate multiple files from a compromised host as an HTTP response over C2.[^1]   |
| [S1024](https://attack.mitre.org/software/S1024) | CreepySnail | CreepySnail can connect to C2 for data exfiltration.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has sent victim data to its C2 servers.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall can upload files and information from a compromised host to its C2 server.[^1]  |
| [S1029](https://attack.mitre.org/software/S1029) | AuTo Stealer | AuTo Stealer can exfiltrate data over actor-controlled C2 servers via HTTP or TCP.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has exfiltrated victim data using HTTP POST requests to its C2 servers.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull has the ability to exfiltrate stolen victim data through its C2 channel.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can send data and files from a compromised host to its C2 server.[^1]  |
| [S1037](https://attack.mitre.org/software/S1037) | STARWHALE | STARWHALE can exfiltrate collected data to its C2 servers.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can send collected data in JSON format to C2.[^1]  |
| [S1042](https://attack.mitre.org/software/S1042) | SUGARDUMP | SUGARDUMP has sent stolen credentials and other data to its C2 server.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can execute commands, including gathering user information, and send the results to C2.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can upload files and information from a compromised host to its C2 servers.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can upload collected files and data to its C2 server.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can send network system data and files to its C2 server.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can send collected data in JSON format to its C2 server.[^1]   |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can exfiltrate files from an infected machine to its C2 server.[^1]   |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK has exfiltrated collected data to its C2 via POST requests.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro sends device and other collected data back to the C2 using the established C2 channels over TCP. [^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can exfiltrate data over the C2 channel.[^1] [^2]   |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco can load a plugin to exfiltrate stolen files to SMB shares also used in C2.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can use SMTP and DNS for file exfiltration and C2.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate uses existing command and control channels to retrieve captured cryptocurrency wallet credentials.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu can sends the collected financial data to the C2 server.[^1] [^2]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper exfiltrates specific files through its command and control framework.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can use email image attachments with embedded data for receiving C2 commands and data exfiltration.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | During the initial Pikabot command and control check-in, Pikabot will transmit collected system information encrypted using RC4.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer uses existing HTTP-based command and control channels for exfiltration.[^3] [^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP  can upload collected files to the command-and-control server.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can send information about the targeted system to C2 including captured passwords, OS build, hostname, and username.[^1]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka data exfiltration takes place over HTTP channels.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can exfiltrate collected data over C2 channels.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus can exfiltrate encrypted system information to the C2 server.[^2] [^1]  |
| [S1166](https://attack.mitre.org/software/S1166) | Solar | Solar can send staged files to C2 for exfiltration.[^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango can use its HTTP C2 channel for exfiltration.[^1]  |
| [S1170](https://attack.mitre.org/software/S1170) | ODAgent | ODAgent can use an attacker-controlled OneDrive account to receive C2 commands and to exfiltrate files.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can use an actor-controlled OneDrive account for C2 communication and exfiltration.[^1]  |
| [S1173](https://attack.mitre.org/software/S1173) | PowerExchange | PowerExchange can exfiltrate files via its email C2 channel.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker will exfiltrate victim system information along with the encryption key via an HTTP POST.[^1] [^2]  |
| [S1182](https://attack.mitre.org/software/S1182) | MagicRAT | MagicRAT exfiltrates data via HTTP over existing command and control channels.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer exfiltrates collected email credentials via HTTP POST to command and control servers.[^2] [^1] [^3] [^4]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | To exfiltrate data, LightSpy configures each module to send an obfuscated JSON blob to hardcoded URL endpoints or paths aligned to the module name.[^1]  |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer exfiltrates collected data via command and control channels.[^1]  |
| [S1188](https://attack.mitre.org/software/S1188) | Line Runner | Line Runner utilizes HTTP to retrieve and exfiltrate information staged using Line Dancer.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer exfiltrates collected information to its command and control infrastructure.[^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has exfiltrated collected credentials to the C2 server.[^1]   |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex encrypts collected system data then exfiltrates via existing command and control channels.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has exfiltrated collected data over existing HTTP and HTTPS C2 channels.[^2] [^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has sent victim data to its C2 server or RedLine panel server.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has used HTTP communications to the “/Uploads” URI for file exfiltration.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has exfiltrated data collected from victim devices to C2 servers.[^1] [^2] [^3]  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^1] [^2]  |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has exfiltrated encrypted data over the C2 channel using the `up <FILENAME>` command.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has used POST to exfiltrate secrets from the victim environment to an attacker-controlled URL.[^1] [^2] [^3]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has the ability to exfiltrate data from the victim appliance.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has uploaded files from the victim system to C2 servers.[^1] [^2] [^3] [^4] [^5] [^6] [^7]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can exfiltrate collected credentials and browser cookies to the C2 server.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag has exfiltrated reconnaissance data on targeted systems to C2 servers.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has uploaded files to the C2 server. Additionally, MuddyViper has the ability to upload the specified file in chunks with sleep time between each chunk.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can exfiltrate collected system information and documents to C2.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [^1]  |
| [[kb/mitre/attack/mitigations/M1057-data-loss-prevention\|M1057]] | Data Loss Prevention | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^3]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
 [^4]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^5]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^6]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
 [^7]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^8]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^9]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^10]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^11]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
 [^12]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^13]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^14]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^15]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^16]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^17]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^18]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^19]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^20]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
 [^21]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^22]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^23]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^24]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
 [^25]: [Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)
 [^26]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^27]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^28]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
 [^29]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^30]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
 [^31]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
 [^32]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^33]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
 [^34]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^35]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^36]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^37]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^38]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^39]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^40]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
 [^41]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^42]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^43]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^44]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^45]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
 [^46]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^47]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^48]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^49]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
 [^50]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^51]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^52]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^53]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^54]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^55]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^56]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^57]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
 [^58]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^59]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^60]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^61]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^62]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
 [^63]: [FireEye Ursnif Nov 2017](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)
 [^64]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)
 [^65]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^66]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^67]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^68]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^69]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^70]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^71]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^72]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^73]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^74]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^75]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^76]: [Trend Micro Emotet Jan 2019](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)
 [^77]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^78]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^79]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^80]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^81]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^82]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^83]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^84]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^85]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^86]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^87]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^88]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^89]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^90]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^91]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^92]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^93]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^94]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^95]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^96]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^97]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^98]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
 [^99]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^100]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
 [^101]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^102]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^103]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^104]: [reed thiefquest ransomware analysis](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)
 [^105]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^106]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^107]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^108]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)
 [^109]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^110]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^111]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^112]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^113]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^114]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^115]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^116]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^117]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^118]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^119]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^120]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)
 [^121]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^122]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^123]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^124]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^125]: [Qualys LummaStealer 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)
 [^126]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^127]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^128]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^129]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^130]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)
 [^131]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^132]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^133]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^134]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^135]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^136]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^137]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^138]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
 [^139]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^140]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^141]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^142]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^143]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^144]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^145]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
 [^146]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
 [^147]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^148]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
 [^149]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^150]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^151]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^152]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^153]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^154]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^155]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^156]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^157]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)
 [^158]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^159]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^160]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^161]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^162]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^163]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^164]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^165]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^166]: [Malwarebytes KONNI Evolves Jan 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/)
 [^167]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^168]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)
 [^169]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^170]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
 [^171]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^172]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^173]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^174]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^175]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^176]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
 [^177]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^178]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
 [^179]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^180]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^181]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^182]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
 [^183]: [ESET Windigo Mar 2014](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)
 [^184]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
 [^185]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^186]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^187]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^188]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^189]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^190]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^191]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^192]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^193]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
