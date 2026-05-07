---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1599
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/network_devices
mitre-attack: kb/mitre/attack/techniques/T1599-network-boundary-bridging
tactic:
    - Defense Impairment
platforms:
    - Network Devices
permissions required:
    - none
---

## Description

Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.<br><br>Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks.  They achieve this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections.  Restriction of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify applications.  To participate with the rest of the network, these devices can be directly addressable or transparent, but their mode of operation has no bearing on how the adversary can bypass them when compromised.<br><br>When an adversary takes control of such a boundary device, they can bypass its policy enforcement to pass normally prohibited traffic across the trust boundary between the two separated networks without hinderance.  By achieving sufficient rights on the device, an adversary can reconfigure the device to allow the traffic they want, allowing them to then further achieve goals such as command and control via [[kb/mitre/attack/techniques/T1090.003-multi-hop-proxy|Multi-hop Proxy]] or exfiltration of data via [[kb/mitre/attack/techniques/T1020.001-traffic-duplication|Traffic Duplication]]. Adversaries may also target internal devices responsible for network segmentation and abuse these in conjunction with [[kb/mitre/attack/techniques/T1090.001-internal-proxy|Internal Proxy]] to achieve the same goals.[^1]   In the cases where a border device separates two separate organizations, the adversary can also facilitate lateral movement into new victim environments.

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles.  Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Refer to NIST guidelines when creating password policies. [^1]  |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control.[^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Upon identifying a compromised network device being used to bridge a network boundary, block the malicious packets using an unaffected network device in path, such as a firewall or a router that has not been compromised.  Continue to monitor for additional activity and to ensure that the blocks are indeed effective. |
| [[kb/mitre/attack/mitigations/M1043-credential-access-protection\|M1043]] | Credential Access Protection | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats.  Ensure that, where available, local passwords are always encrypted, per vendor recommendations.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1599.001-network-address-translation-traversal\|T1599.001]] | Network Address Translation Traversal |

 [^1]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^2]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)
 [^3]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)
 [^4]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)
