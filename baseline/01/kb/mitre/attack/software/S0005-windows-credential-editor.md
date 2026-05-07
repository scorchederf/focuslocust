---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0005
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0005-windows-credential-editor
---

## Description

[[kb/mitre/attack/software/S0005-windows-credential-editor|Windows Credential Editor]] is a password dumping tool. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0005-windows-credential-editor\|Windows Credential Editor]] can dump credentials.[^1]  |

 [^1]: [Amplia WCE](https://web.archive.org/web/20240904163410/https://www.ampliasecurity.com/research/wcefaq.html)
