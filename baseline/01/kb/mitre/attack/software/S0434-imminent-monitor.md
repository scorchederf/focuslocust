---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0434
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0434-imminent-monitor
---

## Description

[[kb/mitre/attack/software/S0434-imminent-monitor|Imminent Monitor]] was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a module for performing remote desktop access.[^1]  |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.[^1]  |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has uploaded a file containing debugger logs, network information and system information to the C2.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a keylogging module.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.[^1]  |
| [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter\|T1059]] | Command and Scripting Interpreter | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.[^1]  |
| [[kb/mitre/attack/techniques/T1070.004-file-deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has deleted files related to its dynamic debugger feature.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.[^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has leveraged CreateProcessW() call to execute the debugger.[^1]  |
| [[kb/mitre/attack/techniques/T1123-audio-capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a remote microphone monitoring capability.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a remote webcam monitoring capability.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information\|T1140]] | Deobfuscate/Decode Files or Information | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has decoded malware components that are then dropped to the system.[^1]  |
| [[kb/mitre/attack/techniques/T1496.001-compute-hijacking\|T1496.001]] | Compute Hijacking | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has the capability to run a cryptocurrency miner on the victim machine.[^1]  |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a PasswordRecoveryPacket module for recovering browser passwords.[^1]  |
| [[kb/mitre/attack/techniques/T1564.001-hidden-files-and-directories\|T1564.001]] | Hidden Files and Directories | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a dynamic debugging feature to set the file attribute to hidden.[^1]  |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a feature to disable Windows Task Manager.[^1] 	 |

 [^1]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
 [^2]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
