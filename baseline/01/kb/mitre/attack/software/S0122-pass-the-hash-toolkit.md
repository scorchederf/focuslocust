---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0122
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0122-pass-the-hash-toolkit
---

## Description

[[kb/mitre/attack/software/S0122-pass-the-hash-toolkit|Pass-The-Hash Toolkit]] is a toolkit that allows an adversary to "pass" a password hash (without knowing the original password) to log in to systems. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1550.002-pass-the-hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0122-pass-the-hash-toolkit\|Pass-The-Hash Toolkit]] can perform pass the hash.[^1]  |

 [^1]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
