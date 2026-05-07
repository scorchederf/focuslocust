---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1480
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1480-execution-guardrails
tactic:
    - Stealth
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.[^3]  Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.[^1] <br><br>Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]]. While use of [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]] may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.<br><br>Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.[^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor can terminate itself if specific execution flags are not present.[^1]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT only replaces SolarWinds Orion source code if the MD5 checksums of both the original source code file and backdoored replacement source code match hardcoded values.[^1]   |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer compares file names and paths to a list of excluded names and directory names during encryption.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet checks for specific operating systems on 32-bit machines, Registry keys, and dates for vulnerabilities, and will exit execution if the values are not met.[^1]  |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout can call `window.location.pathname` to ensure that embedded files are being executed from the C: drive, and will terminate if they are not.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can check its current working directory and for the presence of a specific file and terminate if specific values are not found.[^1]  |
| [S0636](https://attack.mitre.org/software/S0636) | VaporRage | VaporRage has the ability to check for the presence of a specific DLL and terminate if it is not found.[^1]  |
| [S0637](https://attack.mitre.org/software/S0637) | NativeZone | NativeZone can check for the presence of KM.EkeyAlmaz1C.dll and will halt execution unless it is in the same directory as the rest of the malware's components.[^1] [^2]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma is only delivered to a compromised host if the victim's IP address is on an allow-list.[^1]  |
| [S1035](https://attack.mitre.org/software/S1035) | Small Sieve | Small Sieve can only execute correctly if the word `Platypus` is passed to it on the command line.[^1]  |
| [S1052](https://attack.mitre.org/software/S1052) | DEADEYE | DEADEYE can ensure it executes only on intended systems by identifying the victim's volume serial number, hostname, and/or DNS domain.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate uses per-victim links for hosting malicious archives, such as ZIP files, in services such as SharePoint to prevent other entities from retrieving them.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin will check for the presence of several security products on victim machines and will avoid UAC bypass mechanisms if they are identified.[^1]  Raspberry Robin can use specific cookie values in HTTP requests to command and control infrastructure to validate that requests for second stage payloads originate from the initial downloader script.[^2]  |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle's ransomware variant requires that a base64-encoded argument is passed when executed, that is used as the Public Key for subsequent encryption operations. If Apostle is executed without this argument, it automatically runs a self-delete function.[^1]  |
| [S1143](https://attack.mitre.org/software/S1143) | LunarLoader | LunarLoader can use the DNS domain name of a compromised host to create a decryption key to ensure a malicious payload can only execute against the intended targets.[^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can execute a task which leads to execution if it finds a process name containing “creensaver.”[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP requires four command line arguments to execute correctly, otherwise it will produce a message box and halt execution.[^2] [^1] [^3] <br> |
| [S1161](https://attack.mitre.org/software/S1161) | BPFDoor | BPFDoor creates a zero byte PID file at `/var/run/haldrund.pid`. BPFDoor uses this file to determine if it is already running on a system to ensure only one instance is executing at a time.[^1]   |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker will exit its "main" function if the victim domain name does not match provided criteria.[^1]  |
| [S1179](https://attack.mitre.org/software/S1179) | Exbyte | Exbyte checks for the presence of a configuration file before completing execution.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware creates a mutex value with a hard-coded name, and terminates if that mutex already exists on the victim system. BlackByte Ransomware checks the system language to see if it matches one of a list of hard-coded values; if a match is found, the malware will terminate.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer variants only execute if the keyboard layout or language matches a set list of variables.[^1] [^2]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE verifies it is executing from a specific path during execution.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | On macOS, LightSpy checks the existence of a process identification number (PID) file, `/Users/Shared/irc.pid`, to verify if LightSpy is currently running.[^1]  |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | Akira _v2 will fail to execute if the targeted `/vmfs/volumes/` path does not exist or is not defined.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 will not execute on hosts where the system language is set to a language spoken in the Commonwealth of Independent States region.[^2] [^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit will execute an empty infinite loop if it detects it is being run in the context of a debugger.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can make execution dependent on specific parameters including a unique passphrase and the system language of the targeted host not being found on a set exclusion list. [^1] [^3] [^2]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex uses a "servicemain" function to verify its environment to ensure it can only be executed as a service, as well as the existence of a configuration file in a specified directory.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub will terminate without proceeding to encryption if the infected machine is on a list of allowlisted machines specified in its configuration.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has an exception handler that executes when ESET antivirus applications `ekrn.exe` and `egui.exe` are not found and directly injects its code into waitfor.exe using Native Windows API including `WriteProcessMemory` and `CreateRemoteThreadEx`.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has built in settings to not operate based on geolocation or country of the victim host.[^1] [^2]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can require a specific password to be passed by command-line argument during execution which must match a pre-defined value in the configuration in order for it to continue execution.[^1] [^2]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has checked if the last characters of DNS server names end in .bit before initializing C2 communication.[^2]  SystemBC has identified running processes associated with anti-virus solutions to include `a2guard.exe` to determine whether it executes or not.[^1]    |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has utilized logic to avoid executing on Russian based devices.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter code contains an ExclusionRegionNames option where it can compare the results of `kernel32!GetGeoInfo` with a list of regions.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can halt execution if the “en_US” locale is identified on a victim's machine.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can check for the presence of specific analysis tools and will terminate itself if they are found.[^1]  |
| [S9026](https://attack.mitre.org/software/S9026) | ROAMINGHOUSE | ROAMINGHOUSE can change its execution method to create a batch file in the startup folder that executes a legitimate executable if a McAfee product is detected.[^1]  |
| [S9034](https://attack.mitre.org/software/S9034) | Tsundere Botnet | Tsundere Botnet has checked the victim machine’s location to avoid infecting in the Commonwealth of Independent States (CIS) region.[^1]   |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper can halt execution if `[System.Net.Dns]::GetHostName()` or `$env:COMPUTERNAME` contains `“pe-dc”`.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1055-do-not-mitigate\|M1055]] | Do Not Mitigate | [[kb/mitre/attack/techniques/T1480-execution-guardrails\|Execution Guardrails]] likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1480.002-mutual-exclusion\|T1480.002]] | Mutual Exclusion |
| [[kb/mitre/attack/techniques/T1480.001-environmental-keying\|T1480.001]] | Environmental Keying |

 [^1]: [FireEye Outlook Dec 2019](https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html)
 [^2]: [Trellix-Qakbot](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)
 [^3]: [FireEye Kevin Mandia Guardrails](https://www.cyberscoop.com/kevin-mandia-fireeye-u-s-malware-nice/)
 [^4]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^5]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^6]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^7]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^8]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
 [^9]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^10]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^11]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^12]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^13]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
 [^14]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^15]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^16]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^17]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^18]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^19]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^20]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
 [^21]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^22]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^23]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)
 [^24]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^25]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^26]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^27]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^28]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^29]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^30]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^31]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^32]: [HarmonProofpoint_SystemBC_Aug2019](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)
 [^33]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^34]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^35]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^36]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^37]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^38]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^39]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^40]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^41]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^42]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
 [^43]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^44]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)
 [^45]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
 [^46]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
 [^47]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^48]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^49]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^50]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^51]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^52]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
