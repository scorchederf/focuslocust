---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1535
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1535-unused-unsupported-cloud-regions
tactic:
    - Stealth
platforms:
    - IaaS
permissions required:
    - none
---

## Description

Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure.<br><br>Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.<br><br>A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity.<br><br>An example of adversary use of unused AWS regions is to mine cryptocurrency through [[kb/mitre/attack/techniques/T1496-resource-hijacking|Resource Hijacking]], which can cost organizations substantial amounts of money over time depending on the processing power used.[^1] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Cloud service providers may allow customers to deactivate unused regions.[^1]  |

 [^1]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)
