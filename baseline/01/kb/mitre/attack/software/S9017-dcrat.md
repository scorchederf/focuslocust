---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S9017
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S9017-dcrat
---

## Description

[[kb/mitre/attack/software/S9017-dcrat|DCRAT]] is a variant of the open-source [[kb/mitre/attack/software/S1087-asyncrat|AsyncRAT]] developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted/Encoded File | The [[kb/mitre/attack/software/S9017-dcrat\|DCRAT]] configuration file is encrypted using AES-256.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S9017-dcrat\|DCRAT]] can log keystrokes on targeted systems.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S9017-dcrat\|DCRAT]] can use certificate-based authentication for C2 servers.[^1] <br> |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S9017-dcrat\|DCRAT]] can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.[^1]  |

 [^1]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
