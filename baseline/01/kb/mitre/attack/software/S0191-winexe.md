---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0191
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0191-winexe
---

## Description

[[kb/mitre/attack/software/S0191-winexe|Winexe]] is a lightweight, open source tool similar to [[kb/mitre/attack/software/S0029-psexec|PsExec]] designed to allow system administrators to execute commands on remote servers. [^2]  [[kb/mitre/attack/software/S0191-winexe|Winexe]] is unique in that it is a GNU/Linux based client. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0191-winexe\|Winexe]] installs a service on the remote system, executes the command, then uninstalls the service.[^1]  |

 [^1]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
 [^2]: [Winexe Github Sept 2013](https://github.com/skalkoto/winexe/)
 [^3]: [Secpod Winexe June 2017](https://web.archive.org/web/20211019012628/https://www.secpod.com/blog/winexe/)
