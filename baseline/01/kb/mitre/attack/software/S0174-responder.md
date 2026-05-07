---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0174
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0174-responder
---

## Description

Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1040-network-sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0174-responder\|Responder]] captures hashes and credentials that are sent to the system after the name services have been poisoned.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0174-responder\|Responder]] is used to poison name services to gather hashes and credentials from systems within a local network.[^1]  |

 [^1]: [GitHub Responder](https://github.com/SpiderLabs/Responder)
