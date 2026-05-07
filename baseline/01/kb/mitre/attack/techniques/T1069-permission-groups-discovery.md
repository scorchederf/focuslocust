---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1069
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1069-permission-groups-discovery
tactic:
    - Discovery
platforms:
    - Containers
    - IaaS
    - Identity Provider
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.<br><br>Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.[^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0233](https://attack.mitre.org/software/S0233) | MURKYTOP | MURKYTOP has the capability to retrieve information about groups.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can identify the groups the user on a compromised host belongs to.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon uses the `net group` command.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] gathered the local privileges for the infected host.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has the ability to identify Workgroup membership.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape checks for Kubernetes node permissions.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1069.003-cloud-groups\|T1069.003]] | Cloud Groups |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups |
| [[kb/mitre/attack/techniques/T1069.001-local-groups\|T1069.001]] | Local Groups |

 [^1]: [K8s Authorization Overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
 [^2]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
 [^3]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
 [^4]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
 [^5]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^6]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^7]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^8]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
