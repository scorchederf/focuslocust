---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0193
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0193-forfiles
---

## Description

[[kb/mitre/attack/software/S0193-forfiles|Forfiles]] is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^1]  |
| [[kb/mitre/attack/techniques/T1202-indirect-command-execution\|T1202]] | Indirect Command Execution | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to subvert controls and possibly conceal command execution by not directly invoking [[kb/mitre/attack/software/S0106-cmd\|cmd]].[^2] [^1]  |

 [^1]: [Microsoft Forfiles Aug 2016](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc753551(v=ws.11))
 [^2]: [Evi1cg Forfiles Nov 2017](https://x.com/Evi1cg/status/935027922397573120)
 [^3]: [VectorSec ForFiles Aug 2017](https://x.com/vector_sec/status/896049052642533376)
 [^4]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
