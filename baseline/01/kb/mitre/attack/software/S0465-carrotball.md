---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0465
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0465-carrotball
---

## Description

[[kb/mitre/attack/software/S0465-carrotball|CARROTBALL]] is an FTP downloader utility that has been in use since at least 2019. [[kb/mitre/attack/software/S0465-carrotball|CARROTBALL]] has been used as a downloader to install SYSCON.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has used a custom base64 alphabet to decode files.[^1]  |
| [[kb/mitre/attack/techniques/T1071.002-file-transfer-protocols\|T1071.002]] | File Transfer Protocols | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has the ability to use FTP in C2 communications.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has the ability to download and install a remote payload.[^1]  |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has been executed through users being lured into opening malicious e-mail attachments.[^1]  |

 [^1]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
