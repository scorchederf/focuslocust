---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1602
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/network_devices
mitre-attack: kb/mitre/attack/techniques/T1602-data-from-configuration-repository
tactic:
    - Collection
platforms:
    - Network Devices
permissions required:
    - none
---

## Description

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.<br><br>Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.[^3] [^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Segregate SNMP traffic on a separate management network.[^1]  |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Configure intrusion prevention devices to detect SNMP queries and commands from unauthorized sources.[^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Apply extended ACLs to block unauthorized protocols outside the trusted network.[^1]  |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Configure SNMPv3 to use the highest level of security (authPriv) available.[^1]  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Keep system images and software updated and migrate to SNMPv3.[^1]  |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Allowlist MIB objects and implement SNMP views.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1602.002-network-device-configuration-dump\|T1602.002]] | Network Device Configuration Dump |
| [[kb/mitre/attack/techniques/T1602.001-snmp-mib-dump\|T1602.001]] | SNMP (MIB Dump) |

 [^1]: [Cisco Advisory SNMP v3 Authentication Vulnerabilities](https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20080610-SNMPv3)
 [^2]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)
 [^3]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^4]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
 [^5]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)
