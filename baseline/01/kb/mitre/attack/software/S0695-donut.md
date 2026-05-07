---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0695
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0695-donut
---

## Description

[[kb/mitre/attack/software/S0695-donut|Donut]] is an open source framework used to generate position-independent shellcode.[^3] [^2]  [[kb/mitre/attack/software/S0695-donut|Donut]] generated code has been used by multiple threat actors to inject and load malicious payloads into memory.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.002-software-packing\|T1027.002]] | Software Packing | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate packed code modules.[^1] 	 |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted/Encoded File | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^1]  |
| [[kb/mitre/attack/techniques/T1027.015-compression\|T1027.015]] | Compression | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0695-donut\|Donut]] includes a subproject `DonutTest` to inject shellcode into a target process.[^1] 	 |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0695-donut\|Donut]] includes subprojects that enumerate and identify information about [[kb/mitre/attack/techniques/T1055-process-injection\|Process Injection]] candidates.[^1] 	 |
| [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter\|T1059]] | Command and Scripting Interpreter | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via Ruby.[^1] 	 |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via PowerShell.[^1] 	 |
| [[kb/mitre/attack/techniques/T1059.005-visual-basic\|T1059.005]] | Visual Basic | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via VBScript.[^1] 	 |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via Python.[^1] 	 |
| [[kb/mitre/attack/techniques/T1059.007-javascript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate shellcode outputs that execute via JavaScript or JScript.[^1] 	 |
| [[kb/mitre/attack/techniques/T1070-indicator-removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0695-donut\|Donut]] can erase file references to payloads in-memory after being reflectively loaded and executed.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0695-donut\|Donut]] can use HTTP to download previously staged shellcode payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0695-donut\|Donut]] can download and execute previously staged shellcode payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S0695-donut\|Donut]] code modules use various API functions to load and inject code.[^1] 	 |
| [[kb/mitre/attack/techniques/T1620-reflective-code-loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S0695-donut\|Donut]] can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [[kb/mitre/attack/techniques/T1106-native-api\|Native API]] functions to avoid process termination.[^1] 	 |

 [^1]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^2]: [Introducing Donut](https://thewover.github.io/Introducing-Donut/)
 [^3]: [Donut Github](https://github.com/TheWover/donut)
