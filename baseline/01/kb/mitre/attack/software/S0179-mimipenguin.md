---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0179
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0179-mimipenguin
---

## Description

[[kb/mitre/attack/software/S0179-mimipenguin|MimiPenguin]] is a credential dumper, similar to [[kb/mitre/attack/software/S0002-mimikatz|Mimikatz]], designed specifically for Linux platforms. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.007-proc-filesystem\|T1003.007]] | Proc Filesystem | [[kb/mitre/attack/software/S0179-mimipenguin\|MimiPenguin]] can use the `<PID>/maps` and `<PID>/mem` file to search for regex patterns and dump the process memory.[^1] [^2]  |

 [^1]: [MimiPenguin GitHub May 2017](https://github.com/huntergregal/mimipenguin)
 [^2]: [Picus Labs Proc cump 2022](https://www.picussecurity.com/resource/the-mitre-attck-t1003-os-credential-dumping-technique-and-its-adversary-use)
