---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0190
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0190-bitsadmin
---

## Description

[[kb/mitre/attack/software/S0190-bitsadmin|BITSAdmin]] is a command line tool used to create and manage [[kb/mitre/attack/techniques/T1197-bits-jobs|BITS Jobs]]. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to upload files from a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to upload and/or download files.[^1]  |
| [[kb/mitre/attack/techniques/T1197-bits-jobs\|T1197]] | BITS Jobs | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to launch a malicious process.[^1]  |
| [[kb/mitre/attack/techniques/T1570-lateral-tool-transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to upload and/or download files from SMB file servers.[^1]  |

 [^1]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)
 [^2]: [Microsoft About BITS](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)
 [^3]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)
