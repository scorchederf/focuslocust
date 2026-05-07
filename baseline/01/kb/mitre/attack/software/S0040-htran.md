---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0040
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0040-htran
---

## Description

[[kb/mitre/attack/software/S0040-htran|HTRAN]] is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. [^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1014-rootkit\|T1014]] | Rootkit | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can install a rootkit to hide network connections from the host OS.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can inject into into running processes.[^1]  |
| [[kb/mitre/attack/techniques/T1090-proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can proxy TCP socket connections to obfuscate command and control infrastructure.[^1] [^2]  |

 [^1]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)
 [^2]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
