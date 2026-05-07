---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0121
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0121-lslsass
---

## Description

[[kb/mitre/attack/software/S0121-lslsass|Lslsass]] is a publicly-available tool that can dump active logon session password hashes from the lsass process. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0121-lslsass\|Lslsass]] can dump active logon session password hashes from the lsass process.[^1]  |

 [^1]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
