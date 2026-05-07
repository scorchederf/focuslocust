---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0361
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0361-expand
---

## Description

[[kb/mitre/attack/software/S0361-expand|Expand]] is a Windows utility used to expand one or more compressed CAB files.[^1]  It has been used by BBSRAT to decompress a CAB file into executable content.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information\|T1140]] | Deobfuscate/Decode Files or Information | [[kb/mitre/attack/software/S0361-expand\|Expand]] can be used to decompress a local or remote CAB file into an executable.[^1]  |
| [[kb/mitre/attack/techniques/T1564.004-ntfs-file-attributes\|T1564.004]] | NTFS File Attributes | [[kb/mitre/attack/software/S0361-expand\|Expand]] can be used to download or copy a file into an alternate data stream.[^1]  |
| [[kb/mitre/attack/techniques/T1570-lateral-tool-transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0361-expand\|Expand]] can be used to download or upload a file over a network share.[^1]  |

 [^1]: [Microsoft Expand Utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)
 [^2]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
 [^3]: [LOLBAS Expand](https://lolbas-project.github.io/lolbas/Binaries/Expand/)
