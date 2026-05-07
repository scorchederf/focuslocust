---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0592
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0592-remoteutilities
---

## Description

[[kb/mitre/attack/software/S0592-remoteutilities|RemoteUtilities]] is a legitimate remote administration tool that has been used by MuddyWater since at least 2021 for execution on target machines.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can enumerate files and directories on a target machine.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can upload and download files to and from a target machine.[^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can take screenshots on a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1218.007-msiexec\|T1218.007]] | Msiexec | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can use Msiexec to install a service.[^1]  |

 [^1]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
