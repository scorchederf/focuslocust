---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0160
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0160-certutil
---

## Description

[[kb/mitre/attack/software/S0160-certutil|certutil]] is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to download files from a given URL.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information\|T1140]] | Deobfuscate/Decode Files or Information | [[kb/mitre/attack/software/S0160-certutil\|certutil]] has been used to decode binaries hidden inside certificate files as Base64 information.[^1]  |
| [[kb/mitre/attack/techniques/T1553.004-install-root-certificate\|T1553.004]] | Install Root Certificate | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to install browser root certificates as a precursor to performing [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle\|Adversary-in-the-Middle]] between connections to banking websites. Example command: `certutil -addstore -f -user ROOT ProgramData\cert512121.der`.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0160-certutil\|certutil]] may be used to Base64 encode collected data.[^2] [^1]  |

 [^1]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)
 [^2]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)
 [^3]: [Palo Alto Retefe](https://researchcenter.paloaltonetworks.com/2015/08/retefe-banking-trojan-targets-sweden-switzerland-and-japan/)
 [^4]: [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)
