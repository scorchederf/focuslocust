---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1622
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1622-debugger-evasion
tactic:
    - Discovery
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.[^7] <br><br>Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]], if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.<br><br>Specific checks will vary based on the target and/or adversary. On Windows, this may involve [[kb/mitre/attack/techniques/T1106-native-api|Native API]] function calls such as `IsDebuggerPresent()` and ` NtQueryInformationProcess()`, or manually checking the `BeingDebugged` flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools.[^4] [^8]  Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).[^3] [^5] [^9] <br><br>Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue.[^1] <br><br>Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping [[kb/mitre/attack/techniques/T1106-native-api|Native API]] function calls such as `OutputDebugStringW()`.[^6] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has made calls to Windows API `CheckRemoteDebuggerPresent` and exits if it detects a debugger.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can check for debugging tools.[^2] [^3] [^1]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest uses a function named `is_debugging` to perform anti-debugging logic. The function invokes `sysctl` checking the returned value of `P_TRACED`. ThiefQuest also calls `ptrace` with the `PTRACE_DENY_ATTACH` flag to prevent debugging.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can use `IsDebuggerPresent` to detect whether a debugger is present on a victim.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has used `is_debugger_present` as part of its environmental checks.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can search for tools used in static analysis.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can search for debugging tools on a compromised host.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can detect debuggers by using functions such as `DebuggerIsAttached` and `DebuggerIsLogging`. DarkTortilla can also detect profilers by verifying the `COR_ENABLE_PROFILING` environment variable is present and active.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | The Black Basta dropper can check system flags, CPU registers, CPU instructions, process timing, system libraries, and APIs to determine if a debugger is present.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate checks the `BeingDebugged` flag in the PEB structure during execution to identify if the malware is being debugged.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin leverages anti-debugging mechanisms through the use of `ThreadHideFromDebugger`.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot features several methods to evade debugging by analysts, including checks for active debuggers, the use of breakpoints during execution, and checking various system information items such as system memory and the number of processors.[^1] [^2] [^3]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | <br>Latrodectus has the ability to check for the presence of debuggers.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer variants include functionality to identify and evade debuggers.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can detect it is being run in the context of a debugger.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can check heap memory parameters for indications of a debugger and stop the flow of events to the attached debugger in order to hinder dynamic analysis.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader uses anti-debugging mechanisms such as calling `NtQueryInformationProcess` with `InfoClass=7`, referencing `ProcessDebugPort`, to determine if it is being analyzed.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has checked for debugger strings by invoking `GetForegroundWindow` and looks for strings containing “x32dbg”, “x64dbg”, “windbg”, “ollydbg”, “dnspy”, “immunity debugger”, “hyperdbg”, “debug”, “debugger”, “cheat engine”, “cheatengine” and “ida”.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has embedded debug strings with messages to distract analysts.[^1] [^2]   PUBLOAD has leveraged `OutputDebugStringW` and `OutputDebugStringA` functions.[^2]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has leveraged custom exception handlers to hide code flow and stop execution of a debugger.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter has the ability to call `CheckRemoteDebuggerPresent`.[^1]  |
| [S9027](https://attack.mitre.org/software/S9027) | ANELLDR | ANELLDR can call `ZwSetInformationThread` with the second argument set to `ThreadHideFromDebugger (0x11)` to evade being debugged.[^1]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has registered a Vectored Exception Handler (VEH) to catch debugging efforts.[^1]  |

 [^1]: [Apriorit](https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software)
 [^2]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^3]: [hasherezade debug](https://github.com/hasherezade/malware_training_vol1/blob/main/slides/module3/Module3_2_fingerprinting.pdf)
 [^4]: [Cado Security P2PInfect 2023](https://www.cadosecurity.com/blog/p2pinfect-new-variant-targets-mips-devices)
 [^5]: [AlKhaser Debug](https://github.com/LordNoteworthy/al-khaser/tree/master/al-khaser/AntiDebug)
 [^6]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^7]: [ProcessHacker Github](https://github.com/processhacker/processhacker)
 [^8]: [Positive Technologies Hellhounds 2023](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/hellhounds-operation-lahat)
 [^9]: [vxunderground debug](https://web.archive.org/web/20250904153443/https://github.com/vxunderground/VX-API/tree/main#anti-debug)
 [^10]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^11]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^12]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
 [^13]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^14]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^15]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^16]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
 [^17]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^18]: [Logpoint Pikabot 2024](https://www.logpoint.com/wp-content/uploads/2024/02/logpoint-etpr-pikabot.pdf)
 [^19]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^20]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
 [^21]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^22]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^23]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^24]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^25]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^26]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^27]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^28]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^29]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^30]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^31]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^32]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^33]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^34]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^35]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^36]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
