---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1218
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1218-system-binary-proxy-execution
tactic:
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system.[^2]  Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands.<br><br>Similarly, on Linux systems adversaries may abuse trusted binaries such as `split` to proxy execution of malicious commands.[^3] [^1] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Restrict execution of particularly vulnerable binaries to privileged accounts or groups that need to use it to lessen the opportunities for malicious usage. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Consider using application control to prevent execution of binaries that are susceptible to abuse and not required for a given system or network. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Many native binaries may not be necessary within a given environment. |
| [[kb/mitre/attack/mitigations/M1050-exploit-protection\|M1050]] | Exploit Protection | Microsoft's Enhanced Mitigation Experience Toolkit (EMET) Attack Surface Reduction (ASR) feature can be used to block methods of using using trusted binaries to bypass application control. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1218.011-rundll32\|T1218.011]] | Rundll32 |
| [[kb/mitre/attack/techniques/T1218.013-mavinject\|T1218.013]] | Mavinject |
| [[kb/mitre/attack/techniques/T1218.004-installutil\|T1218.004]] | InstallUtil |
| [[kb/mitre/attack/techniques/T1218.007-msiexec\|T1218.007]] | Msiexec |
| [[kb/mitre/attack/techniques/T1218.003-cmstp\|T1218.003]] | CMSTP |
| [[kb/mitre/attack/techniques/T1218.002-control-panel\|T1218.002]] | Control Panel |
| [[kb/mitre/attack/techniques/T1218.015-electron-applications\|T1218.015]] | Electron Applications |
| [[kb/mitre/attack/techniques/T1218.008-odbcconf\|T1218.008]] | Odbcconf |
| [[kb/mitre/attack/techniques/T1218.012-verclsid\|T1218.012]] | Verclsid |
| [[kb/mitre/attack/techniques/T1218.005-mshta\|T1218.005]] | Mshta |
| [[kb/mitre/attack/techniques/T1218.001-compiled-html-file\|T1218.001]] | Compiled HTML File |
| [[kb/mitre/attack/techniques/T1218.010-regsvr32\|T1218.010]] | Regsvr32 |
| [[kb/mitre/attack/techniques/T1218.009-regsvcs-regasm\|T1218.009]] | Regsvcs／Regasm |
| [[kb/mitre/attack/techniques/T1218.014-mmc\|T1218.014]] | MMC |

 [^1]: [GTFO split](https://gtfobins.github.io/gtfobins/split/)
 [^2]: [LOLBAS Project](https://github.com/LOLBAS-Project/LOLBAS#criteria)
 [^3]: [split man page](https://man7.org/linux/man-pages/man1/split.1.html)
