---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0500
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0500-mcmd
---

## Description

[[kb/mitre/attack/software/S0500-mcmd|MCMD]] is a remote access tool that provides remote command shell capability used by Dragonfly.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] has the ability to upload files from an infected device.[^1]  |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can Base64 encode output strings prior to sending to C2.[^1]  |
| [[kb/mitre/attack/techniques/T1036.005-match-legitimate-resource-name-or-location\|T1036.005]] | Match Legitimate Resource Name or Location | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] has been named Readme.txt to appear legitimate.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can use scheduled tasks for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can launch a console process (cmd.exe) with redirected standard input and output.[^1]  |
| [[kb/mitre/attack/techniques/T1070.009-clear-persistence\|T1070.009]] | Clear Persistence | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] has the ability to remove set Registry Keys, including those used for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can use HTTPS in communication with C2 web servers.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can upload additional files to a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can use Registry Run Keys for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can modify processes to prevent them from being visible on the desktop.[^1]  |

 [^1]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)
