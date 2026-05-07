---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1559
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1559-inter-process-communication
tactic:
    - Execution
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. <br><br>Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [[kb/mitre/attack/techniques/T1559.002-dynamic-data-exchange|Dynamic Data Exchange]] or [[kb/mitre/attack/techniques/T1559.001-component-object-model|Component Object Model]]. Linux environments support several different IPC mechanisms, two of which being sockets and pipes.[^2]  Higher level execution mediums, such as those of [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]]s, may also leverage underlying IPC mechanisms. Adversaries may also use [[kb/mitre/attack/techniques/T1021-remote-services|Remote Services]] such as [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model|Distributed Component Object Model]] to facilitate remote IPC execution.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos has the ability to move data between its kernel and user mode components, generally using named pipes.[^1]  |
| [S0537](https://attack.mitre.org/software/S0537) | HyperStack | HyperStack can connect to the IPC$ share on remote machines.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink has the ability to create a pipe to enable inter-process communication.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | When executing with non-root permissions, RotaJakiro uses the the `shmget API` to create shared memory between other known RotaJakiro processes. This allows processes to communicate with each other and share their PID.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can use pipes to redirect the standard input and the standard output.[^1]  |
| [S1123](https://attack.mitre.org/software/S1123) | PITSTOP | PITSTOP can listen over the Unix domain socket located at `/data/runtime/cockpit/wd.fd`.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin contains an embedded custom [[kb/mitre/attack/software/S0183-tor\|Tor]] network client that communicates with the primary payload via shared process memory.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can retrieve output from arbitrary processes and shell commands via a pipe.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can pipe command output to a targeted process.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can read the results of command line execution via an unnamed pipe connected to the process.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can use interprocess communication (IPC) to enable the designation of multiple files for exfiltration in a scalable manner.[^1] <br> |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | The Havoc SMB demon can use named pipes for communication through a parent demon.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has facilitated inter-process communication between DLL components via the use of pipes.[^2]  TONESHELL has also created a reverse shell using two anonymous pipes to write data to stdin and read data from stdout and stderr.[^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has leveraged the `CreatePipe` API to enable inter-process communication.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has leveraged IPC using a UNIX domain socket between the dsmdm process and the web process.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-application-developer-guidance\|M1013]] | Application Developer Guidance | Enable the Hardened Runtime capability when developing applications. Do not include the `com.apple.security.get-task-allow` entitlement with the value set to any variation of true.  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{AppID_GUID}` associated with the process-wide security of individual COM applications.[^1] <br><br>Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Ole` associated with system-wide security defaults for all COM applications that do no set their own process-wide security.[^2]  [^3]  |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs.[^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [^1] [^2] [^3]  Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel.[^4]  |
| [[kb/mitre/attack/mitigations/M1048-application-isolation-and-sandboxing\|M1048]] | Application Isolation and Sandboxing | Ensure all COM alerts and Protected View are enabled.[^1]  |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Consider disabling embedded files in Office programs, such as OneNote, that do not work with Protected View.[^1] [^2]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1559.002-dynamic-data-exchange\|T1559.002]] | Dynamic Data Exchange |
| [[kb/mitre/attack/techniques/T1559.001-component-object-model\|T1559.001]] | Component Object Model |
| [[kb/mitre/attack/techniques/T1559.003-xpc-services\|T1559.003]] | XPC Services |

 [^1]: [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
 [^2]: [Linux IPC](https://www.geeksforgeeks.org/inter-process-communication-ipc/#:~:text=Inter%2Dprocess%20communication%20(IPC),of%20co%2Doperation%20between%20them.)
 [^3]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)
 [^4]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)
 [^5]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)
 [^6]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)
 [^7]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^8]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^9]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^10]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)
 [^11]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^12]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^13]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^14]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)
 [^15]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^16]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^17]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^18]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^19]: [JPCERT SPAWNCHIMERA Ivanti February 2025](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
 [^20]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
 [^21]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)
 [^22]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)
 [^23]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)
 [^24]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)
 [^25]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^26]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^27]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^28]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^29]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
