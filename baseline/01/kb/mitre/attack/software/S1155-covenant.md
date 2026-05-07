---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S1155
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1155-covenant
---

## Description

[[kb/mitre/attack/software/S1155-covenant|Covenant]] is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as HAFNIUM during operations. [[kb/mitre/attack/software/S1155-covenant|Covenant]] functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.[^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can utilize WMI to install new Grunt listeners through XSL files or command one-liners.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can create PowerShell-based launchers for Grunt installation.[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] provides access to a Command Shell in Windows environments for follow-on command execution and tasking.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can establish command and control via HTTP.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] implants can gather basic information on infected systems.[^1]  |
| [[kb/mitre/attack/techniques/T1218.004-installutil\|T1218.004]] | InstallUtil | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can create launchers via an InstallUtil XML file to install new Grunt listeners.[^1]  |
| [[kb/mitre/attack/techniques/T1218.005-mshta\|T1218.005]] | Mshta | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can create HTA files to install Grunt listeners.[^1]  |
| [[kb/mitre/attack/techniques/T1218.010-regsvr32\|T1218.010]] | Regsvr32 | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can create SCT files for installation via `Regsvr32` to deploy new Grunt listeners.[^1]  |
| [[kb/mitre/attack/techniques/T1571-non-standard-port\|T1571]] | Non-Standard Port | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] listeners and controllers can be configured to use non-standard ports.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] can utilize SSL to encrypt command and control traffic.[^1]  |

 [^1]: [Github Covenant](https://github.com/cobbr/Covenant)
 [^2]: [Microsoft HAFNIUM March 2020](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)
