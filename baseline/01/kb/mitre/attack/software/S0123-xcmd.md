---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0123
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0123-xcmd
---

## Description

[[kb/mitre/attack/software/S0123-xcmd|xCmd]] is an open source tool that is similar to [[kb/mitre/attack/software/S0029-psexec|PsExec]] and allows the user to execute applications on remote systems. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0123-xcmd\|xCmd]] can be used to execute binaries on remote systems by creating and starting a service.[^1]  |

 [^1]: [xCmd](https://ashwinrayaprolu.wordpress.com/2011/04/12/xcmd-an-alternative-to-psexec/)
