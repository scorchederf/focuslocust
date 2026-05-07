---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0581
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0581-ironnetinjector
---

## Description

[[kb/mitre/attack/software/S0581-ironnetinjector|IronNetInjector]] is a Turla toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including ComRAT.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted/Encoded File | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1036.004-masquerade-task-or-service\|T1036.004]] | Masquerade Task or Service | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] has been disguised as a legitimate service using the name PythonUpdateSrvc.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] has used a task XML file named `mssch.xml` to run an IronPython script when a user logs in or when specific system events are created.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.[^1]  |
| [[kb/mitre/attack/techniques/T1055.001-dynamic-link-library-injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] has the ability to inject a DLL into running processes, including the [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] DLL into explorer.exe.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can identify processes via C# methods such as `GetProcessesByName` and running [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] with the Python `os.popen` function.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] can use IronPython scripts to load payloads with the help of a .NET injector.[^1]  |
| [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information\|T1140]] | Deobfuscate/Decode Files or Information | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] has the ability to decrypt embedded .NET and PE payloads.[^1]  |

 [^1]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)
