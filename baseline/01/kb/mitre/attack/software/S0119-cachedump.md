---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0119
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0119-cachedump
---

## Description

[[kb/mitre/attack/software/S0119-cachedump|Cachedump]] is a publicly-available tool that program extracts cached password hashes from a system’s registry. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.005-cached-domain-credentials\|T1003.005]] | Cached Domain Credentials | [[kb/mitre/attack/software/S0119-cachedump\|Cachedump]] can extract cached password hashes from cache entry information.[^1]  |

 [^1]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
