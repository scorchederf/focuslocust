---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1669
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1669-wi-fi-networks
tactic:
    - Initial Access
platforms:
    - Linux
    - Network Devices
    - Windows
    - macOS
permissions required:
    - none
---

## Description

Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] — belonging to a target organization.[^2] [^1]  Establishing a connection to a Wi-Fi access point requires a certain level of proximity to both discover and maintain a stable network connection. <br><br>Adversaries may establish a wireless connection through various methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass the need for physical proximity, adversaries may attempt to remotely compromise nearby third-party systems that have both wired and wireless network connections available (i.e., dual-homed systems). These third-party compromised devices can then serve as a bridge to connect to a target’s Wi-Fi network.[^1] <br><br>Once an initial wireless connection is achieved, adversaries may leverage this access for follow-on activities in the victim network or further targeting of specific devices on the network. Adversaries may perform [[kb/mitre/attack/techniques/T1040-network-sniffing|Network Sniffing]] or [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle|Adversary-in-the-Middle]] activities for [[kb/mitre/attack/tactics/TA0006-credential-access|Credential Access]] or [[kb/mitre/attack/tactics/TA0007-discovery|Discovery]].

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. Separate networking environments for Wi-Fi and Ethernet-wired networks, particularly where Ethernet-based networks allow for access to sensitive resources. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Harden access requirements for Wi-Fi networks through using two or more pieces of evidence to authenticate, such as a username and password in addition to a token from a physical smart card or token generator. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure that web traffic that may contain credentials is protected by SSL/TLS. |

 [^1]: [Nearest Neighbor Volexity](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
 [^2]: [DOJ GRU Charges 2018](https://www.justice.gov/archives/opa/pr/us-charges-russian-gru-officers-international-hacking-and-related-influence-and)
