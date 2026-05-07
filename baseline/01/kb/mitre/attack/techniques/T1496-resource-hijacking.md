---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1496
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1496-resource-hijacking
tactic:
    - Impact
platforms:
    - Windows
    - IaaS
    - Linux
    - macOS
    - Containers
    - SaaS
permissions required:
    - none
---

## Description

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. <br><br>Resource hijacking may take a number of different forms. For example, adversaries may:<br><br>* Leverage compute resources in order to mine cryptocurrency<br>* Sell network bandwidth to proxy networks<br>* Generate SMS traffic for profit<br>* Abuse cloud-based messaging services to send large quantities of spam messages<br><br>In some cases, adversaries may leverage multiple types of Resource Hijacking at once.[^1] 

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1496.003-sms-pumping\|T1496.003]] | SMS Pumping |
| [[kb/mitre/attack/techniques/T1496.002-bandwidth-hijacking\|T1496.002]] | Bandwidth Hijacking |
| [[kb/mitre/attack/techniques/T1496.004-cloud-service-hijacking\|T1496.004]] | Cloud Service Hijacking |
| [[kb/mitre/attack/techniques/T1496.001-compute-hijacking\|T1496.001]] | Compute Hijacking |

 [^1]: [Sysdig Cryptojacking Proxyjacking 2023](https://sysdig.com/blog/labrat-cryptojacking-proxyjacking-campaign/)
