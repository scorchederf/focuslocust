---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1567
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1567-exfiltration-over-web-service
tactic:
    - Exfiltration
platforms:
    - ESXi
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.<br><br>Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been used by threat actors to configure servers for data exfiltration.[^1]  |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook has used legitimate web services to exfiltrate data.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has exfiltrated files using web services.[^1]  |
| [S1168](https://attack.mitre.org/software/S1168) | SampleCheck5000 | SampleCheck5000 can use the Microsoft Office Exchange Web Services API to access an actor-controlled account and retrieve files for exfiltration.[^2] [^1]  |
| [S1171](https://attack.mitre.org/software/S1171) | OilCheck | OilCheck can upload documents from compromised hosts to a shared Microsoft Office 365 Outlook email account for exfiltration.[^1]  |
| [S1179](https://attack.mitre.org/software/S1179) | Exbyte | Exbyte exfiltrates collected data to online file hosting sites such as `Mega.co.nz`.[^2] [^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has leveraged Telegram chat to upload stolen data using the Telegram API with a bot token.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[kb/mitre/attack/mitigations/M1057-data-loss-prevention\|M1057]] | Data Loss Prevention | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1567.004-exfiltration-over-webhook\|T1567.004]] | Exfiltration Over Webhook |
| [[kb/mitre/attack/techniques/T1567.001-exfiltration-to-code-repository\|T1567.001]] | Exfiltration to Code Repository |
| [[kb/mitre/attack/techniques/T1567.003-exfiltration-to-text-storage-sites\|T1567.003]] | Exfiltration to Text Storage Sites |
| [[kb/mitre/attack/techniques/T1567.002-exfiltration-to-cloud-storage\|T1567.002]] | Exfiltration to Cloud Storage |

 [^1]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^2]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^3]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^4]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)
 [^5]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^6]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^7]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
 [^8]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^9]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
