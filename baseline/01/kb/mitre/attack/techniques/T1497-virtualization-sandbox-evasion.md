---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1497
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion
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

Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]] during automated discovery to shape follow-on behaviors.[^2] <br><br>Adversaries may use several methods to accomplish [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]] such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox.[^1] <br><br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK  includes runtime checks to identify an analysis environment and prevent execution on it.[^1]  |
| [S0046](https://attack.mitre.org/software/S0046) | CozyCar | Some versions of CozyCar will check to ensure it is not being executed inside a virtual machine or a known malware analysis sandbox environment. If it detects that it is, it will exit.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon has the ability to use anti-detection functions to identify sandbox environments.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can detect if it is running within a sandbox or other virtualized analysis environment.[^1] 	 |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal can check to determine if the compromised system is running on VMware.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla |  Agent Tesla has the ability to perform anti-sandboxing and anti-virtualization checks.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has used several anti-emulation techniques to prevent automated analysis by emulators or sandboxes.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has embedded a "vmdetect.exe" executable to identify virtual machines at the beginning of execution.[^1]   |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has manipulated Keitaro Traffic Direction System to filter researcher and sandbox traffic.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has removed various hooks before installing the trojan or bootkit to evade sandbox analysis or other analysis software.[^1]  |
| [S0499](https://attack.mitre.org/software/S0499) | Hancitor | Hancitor has used a macro to check that an ActiveDocument shape object in the lure message is present. If this object is not found, the macro will exit without downloading additional payloads.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can attempt to overload sandbox analysis by sending 1550 calls to `printf`.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has used multiple anti-analysis and anti-sandbox techniques to prevent automated analysis by sandboxes.[^1] [^2]   |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can use junk code to generate random activity to obscure malware behavior.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can sleep for a time interval between C2 communication attempts.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has contained a hardcoded list of IP addresses to block that belong to sandboxes and analysis platforms.[^1] [^2]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee has the ability to perform anti-virtualization checks.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can make a random number of calls to the `kernel32.beep` function to hinder log analysis.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin contains real and fake second-stage payloads following initial execution, with the real payload only delivered if the malware determines it is not running in a virtualized environment.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer payloads have used control flow obfuscation techniques such as excessively long code blocks of mathematical instructions to defeat sandboxing and related analysis methods.[^1] [^2]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can utilize decoy command and control domains within the malware configuration to circumvent sandbox analysis.[^2] [^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has an anti-sandbox technique that requires the malware to consistently check with the C2 server, if the communication fails RedLine Stealer will not continue execution.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1497.001-system-checks\|T1497.001]] | System Checks |
| [[kb/mitre/attack/techniques/T1497.003-time-based-checks\|T1497.003]] | Time Based Checks |
| [[kb/mitre/attack/techniques/T1497.002-user-activity-based-checks\|T1497.002]] | User Activity Based Checks |

 [^1]: [Unit 42 Pirpi July 2015](https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^2]: [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
 [^3]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^4]: [Trendmicro_IcedID](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)
 [^5]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^6]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^7]: [ESET Carberp March 2012](https://www.eset.com/fileadmin/eset/US/resources/docs/white-papers/white-papers-win-32-carberp.pdf)
 [^8]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^9]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^10]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^11]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^12]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^13]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^14]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^15]: [CheckPoint XLoader 2022](https://research.checkpoint.com/2022/xloader-botnet-find-me-if-you-can/)
 [^16]: [ANY.RUN XLoader 2023](https://any.run/cybersecurity-blog/xloader-formbook-encryption-analysis-and-malware-decryption/)
 [^17]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
 [^18]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^19]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^20]: [Cyble Egregor Oct 2020](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
 [^21]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^22]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)
 [^23]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^24]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^25]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
 [^26]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^27]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
 [^28]: [FireEye Hancitor](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
