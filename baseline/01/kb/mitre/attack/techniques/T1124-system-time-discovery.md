---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1124
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
mitre-attack: kb/mitre/attack/techniques/T1124-system-time-discovery
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

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or `systemsetup` on macOS.[^9] [^8] [^1]  These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.[^5] [^2] <br><br>System time information may be gathered in a number of ways, such as with [[kb/mitre/attack/software/S0039-net|Net]] on Windows by performing `net time \\hostname` to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using `w32tm /tz`.[^8]  In addition, adversaries can discover device uptime through functions such as `GetTickCount()` to determine how long it has been since the system booted up.[^12] <br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands such as `show clock detail` can be used to see the current time configuration.[^4]  On ESXi servers, `esxcli system clock get` can be used for the same purpose.<br><br>In addition, system calls – such as `time()` – have been used to collect the current time on Linux devices.[^3]  On macOS systems, adversaries may use commands such as `systemsetup -gettimezone` or `timeIntervalSinceNow` to gather current time zone information or current date and time.[^11] [^6] <br><br>This information could be useful for performing other techniques, such as executing a file with a [[kb/mitre/attack/techniques/T1053-scheduled-task-job|Scheduled Task/Job]][^10] , or to discover locality information based on time zone to assist in victim targeting (i.e. [[kb/mitre/attack/techniques/T1614-system-location-discovery|System Location Discovery]]). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.[^7] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can use `GetLocalTime` and `GetSystemTime` to collect system time.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has identified system time through its GetSystemInfo command.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to collect the system `UPTIME`.[^1]  |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | The `net time` command can be used in [[kb/mitre/attack/software/S0039-net\|Net]] to determine the local or remote system time.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `net time` command  to get the system time from the machine and collect the current date and time zone information.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 gathers and beacons the system time during installation.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson has the ability to determine the date and time on a compromised host.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT has checked the victim system's date and time to perform tasks during business hours (9 to 5, Monday to Friday).[^1]   |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has commands to get the time the machine was built, the time, and the time zone.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon obtains the system time and will only activate if it is greater than a preset date.[^1] [^2]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can obtain the victim time zone.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind obtains the victim's current time.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT can obtain the date and time of a system.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | As part of the data reconnaissance phase, Proxysvc grabs the system time to send back to the control server.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy gathers the current time zone and date information from the system.[^1] [^2]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole gathers the local system time from the victim’s machine.[^1] [^2]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE checks to see if the system is configured with "Daylight" time and checks for a specific region to be set for the timezone.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT gathers the time zone information from the victim’s machine.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal can check the system time set on the infected host.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT has the capability to obtain the time zone information and the current timestamp of the victim’s machine.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda collects the current system time (UTC) and sends it back to the C2 server.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can collect the timestamp from the victim’s machine.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon uses the command `net time \\127.0.0.1` to get information the system’s time.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can collect the time zone information from the system.[^1] [^2]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can collect the current time zone information from the victim’s machine.[^1]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI can collect the current timestamp of the victim's machine.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth collects the timestamp from the infected machine. [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has been observed collecting system time from victim machines.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill can obtain the current date and time of the victim machine.[^1] 	 |
| [S0396](https://attack.mitre.org/software/S0396) | EvilBunny | EvilBunny has used the API calls NtQuerySystemTime, GetSystemTimeAsFileTime, and GetTickCount to gather time metrics as part of its checks to see if the malware is running in a sandbox.[^1]  |
| [S0417](https://attack.mitre.org/software/S0417) | GRIFFON | GRIFFON has used a reconnaissance module that can be used to retrieve the date and time of the system.[^1] 	 |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum can obtain the date and time of the compromised system.[^1]  |
| [S0450](https://attack.mitre.org/software/S0450) | SHARPSTATS | SHARPSTATS has the ability to identify the current date and time on the compromised host.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo uses JavaScript to get the system time.[^1]   |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail has the ability to generate the current date and time.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to determine local time on a compromised host.[^1]  |
| [S0471](https://attack.mitre.org/software/S0471) | build_downer | build_downer has the ability to determine the local time to ensure malware installation only happens during the hours that the infected system is active.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can send time zone information from a compromised host to C2.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can determine the time on the victim machine via IPinfo.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can collect the time on the compromised host.[^1] [^2]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor contains functionality to query the local/system time.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected device `UPTIME`.[^1] [^2]  |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear has the ability to determine local time on a compromised host.[^1]   |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can execute `GetLocalTime` for time discovery.[^1]  |
| [S0588](https://attack.mitre.org/software/S0588) | GoldMax | GoldMax can check the current date-time value of the compromised system, comparing it to the hardcoded execution trigger and can send the current timestamp to the C2 server.[^1] [^2]   |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has collected the current date and time of the victim system.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet collects the time and date of a system when it is infected.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker uses the current UTC victim system date for domain generation and connects to time servers to determine the current date.[^1] [^2]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can execute `getinfo`  to discover the current time on a compromised host.[^1] [^2]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can pull a timestamp from the victim's machine.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can identify the system time on a targeted host.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can collect the local time on a compromised host.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can determine the current time.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can collect time zone information and system `UPTIME`.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma can collect the current time on a victim machine.[^1]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can collect the date and time from a compromised host.[^1] [^2]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect start time information from a compromised host.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can use the `GetTickCount` and `GetSystemTimeAsFileTime` API calls to inspect system time.[^1]  |
| [S1033](https://attack.mitre.org/software/S1033) | DCSrv | DCSrv can compare the current time on an infected host with a configuration value to determine when to start the encryption process.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can collect the time zone from the victim's machine.[^1]  |
| [S1043](https://attack.mitre.org/software/S1043) | ccf32 | ccf32 can determine the local time on targeted machines.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can check system time to help determine when changes were made to specified files.[^1]  |
| [S1051](https://attack.mitre.org/software/S1051) | KEYPLUG | KEYPLUG can obtain the current tick count of an infected computer.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has checked the system time before and after encryption.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can collect time zone information.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can obtain the `DATETIME` and `UPTIME` from a compromised machine.[^1]    |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check whether the current system hour and day of the week are within operating hours defined it its configuration.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate creates a log file for capturing keylogging, clipboard, and related data using the victim host's current date for the filename.[^1]  DarkGate queries victim system epoch time during execution.[^1]  DarkGate captures system time information as part of automated profiling on initial installation.[^2]  |
| [S1134](https://attack.mitre.org/software/S1134) | DEADWOOD | DEADWOOD will set a timestamp value to determine when wiping functionality starts. When the timestamp is met on the system, a trigger file is created on the operating system allowing for execution to proceed. If the timestamp is in the past, the wiper will execute immediately.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor can identify the system local time information.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer gathers victim machine timezone information.[^2] [^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP reads the infected system's current time and writes it to a log file during execution.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker retrieves a system timestamp that is used in generating an encryption key.[^1]  |
| [S1227](https://attack.mitre.org/software/S1227) | StarProxy | StarProxy has utilized the windows API call `GetLocalTime()` to retrieve a SystemTime structure to generate a seed value.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has collected the machine’s tick count through the use of `GetTickCount`.[^1]  |
| [S1233](https://attack.mitre.org/software/S1233) | PAKLOG | PAKLOG has collected a timestamp to log the precise time a key was pressed, formatted as %Y-%m-%d %H:%M:%S.[^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has discovered device uptime through `GetTickCount()`.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has obtained and sent the current timestamp associated with the victim device to C2.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has leveraged the time of the device to create a text file with a filename that uses the function of `uniqid(time()).‘.txt`, consisting of the 10 character UNIX timestamp and 13 hexadecimal characters.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has the ability to check the system’s time zone on the victim device.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can capture system time to send to the C2.[^1]  |

 [^1]: [systemsetup mac time](https://support.apple.com/en-gb/guide/remote-desktop/apd95406b8d/mac)
 [^2]: [linux system time](https://wiki.archlinux.org/title/System_time)
 [^3]: [MAGNET GOBLIN](https://research.checkpoint.com/2024/magnet-goblin-targets-publicly-facing-servers-using-1-day-vulnerabilities/)
 [^4]: [show_clock_detail_cisco_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s2.html#wp1896741674)
 [^5]: [Mac Time Sync](https://www.macinstruct.com/tutorials/synchronize-your-macs-clock-with-a-time-server/)
 [^6]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^7]: [AnyRun TimeBomb](https://any.run/cybersecurity-blog/time-bombs-malware-with-delayed-execution/)
 [^8]: [Technet Windows Time Service](https://technet.microsoft.com/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-time-service-tools-and-settings)
 [^9]: [MSDN System Time](https://msdn.microsoft.com/ms724961.aspx)
 [^10]: [RSA EU12 They're Inside](https://www.rsaconference.com/writable/presentations/file_upload/ht-209_rivner_schwartz.pdf)
 [^11]: [System Information Discovery Technique](https://www.picussecurity.com/resource/the-system-information-discovery-technique-explained-mitre-attack-t1082)
 [^12]: [Virtualization/Sandbox Evasion](https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis)
 [^13]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^14]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^15]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^16]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
 [^17]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^18]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^19]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^20]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^21]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
 [^22]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^23]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^24]: [TechNet Net Time](https://technet.microsoft.com/bb490716.aspx)
 [^25]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^26]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^27]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^28]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
 [^29]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
 [^30]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^31]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^32]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^33]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^34]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
 [^35]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^36]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
 [^37]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^38]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^39]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^40]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^41]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)
 [^42]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^43]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
 [^44]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)
 [^45]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^46]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^47]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^48]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^49]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^50]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^51]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^52]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^53]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^54]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^55]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^56]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^57]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^58]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^59]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^60]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^61]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^62]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^63]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^64]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^65]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^66]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^67]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^68]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^69]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^70]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^71]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^72]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^73]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^74]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^75]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^76]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^77]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
 [^78]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^79]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^80]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^81]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^82]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^83]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^84]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^85]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
 [^86]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^87]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^88]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^89]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^90]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^91]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^92]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^93]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
 [^94]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^95]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^96]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^97]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^98]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^99]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^100]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^101]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^102]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^103]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^104]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)
