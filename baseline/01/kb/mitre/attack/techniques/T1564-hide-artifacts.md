---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1564
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
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1564-hide-artifacts
tactic:
    - Stealth
platforms:
    - ESXi
    - Linux
    - macOS
    - Office Suite
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.[^3] [^1] [^2] <br><br>Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can modify file attributes to hide the file.[^1]  |
| [S0402](https://attack.mitre.org/software/S0402) | OSX/Shlayer | OSX/Shlayer has used the `mktemp` utility to make random and unique filenames for payloads, such as `export tmpDir="$(mktemp -d /tmp/XXXXXXXXXXXX)"` or `mktemp -t Installer`.[^2] [^3] [^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore uses the `mktemp` utility to make unique file and directory names for payloads, such as `TMP_DIR=`mktemp -d -t x`.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can masquerade the Process Environment Block on a compromised host to hide its attempts to elevate privileges through `IFileOperation`.[^1]  |
| [S1011](https://attack.mitre.org/software/S1011) | Tarrask | Tarrask is able to create “hidden” scheduled tasks by deleting the Security Descriptor (`SD`) registry value.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla has used `%HiddenReg%` and `%HiddenKey%` as part of its persistence via the Windows registry.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can hide services used to aid execution.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-application-developer-guidance\|M1013]] | Application Developer Guidance | Application developers should consider limiting the requirements for custom or otherwise difficult to manage file/folder exclusions. Where possible, install applications to trusted system folder paths that are already protected by restricted file and directory permissions. |
| [[kb/mitre/attack/mitigations/M1033-limit-software-installation\|M1033]] | Limit Software Installation | Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Periodically audit virtual machines for abnormalities. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Review and audit file/folder exclusions, and limit scope of exclusions to only what is required where possible.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1564.012-file-path-exclusions\|T1564.012]] | File／Path Exclusions |
| [[kb/mitre/attack/techniques/T1564.008-email-hiding-rules\|T1564.008]] | Email Hiding Rules |
| [[kb/mitre/attack/techniques/T1564.011-ignore-process-interrupts\|T1564.011]] | Ignore Process Interrupts |
| [[kb/mitre/attack/techniques/T1564.013-bind-mounts\|T1564.013]] | Bind Mounts |
| [[kb/mitre/attack/techniques/T1564.014-extended-attributes\|T1564.014]] | Extended Attributes |
| [[kb/mitre/attack/techniques/T1564.002-hidden-users\|T1564.002]] | Hidden Users |
| [[kb/mitre/attack/techniques/T1564.009-resource-forking\|T1564.009]] | Resource Forking |
| [[kb/mitre/attack/techniques/T1564.006-run-virtual-instance\|T1564.006]] | Run Virtual Instance |
| [[kb/mitre/attack/techniques/T1564.007-vba-stomping\|T1564.007]] | VBA Stomping |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window |
| [[kb/mitre/attack/techniques/T1564.005-hidden-file-system\|T1564.005]] | Hidden File System |
| [[kb/mitre/attack/techniques/T1564.001-hidden-files-and-directories\|T1564.001]] | Hidden Files and Directories |
| [[kb/mitre/attack/techniques/T1564.004-ntfs-file-attributes\|T1564.004]] | NTFS File Attributes |
| [[kb/mitre/attack/techniques/T1564.010-process-argument-spoofing\|T1564.010]] | Process Argument Spoofing |

 [^1]: [Cybereason OSX Pirrit](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)
 [^2]: [MalwareBytes ADS July 2015](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)
 [^3]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
 [^4]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^5]: [Shlayer jamf gatekeeper bypass 2021](https://www.jamf.com/blog/shlayer-malware-abusing-gatekeeper-bypass-on-macos/)
 [^6]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
 [^7]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^8]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^9]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^10]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)
 [^11]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^12]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)
 [^13]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
