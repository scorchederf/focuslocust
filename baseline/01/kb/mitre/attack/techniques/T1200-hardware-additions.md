---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1200
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1200-hardware-additions
tactic:
    - Initial Access
platforms:
    - Windows
    - Linux
    - macOS
permissions required:
    - none
---

## Description

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. [[kb/mitre/attack/techniques/T1091-replication-through-removable-media|Replication Through Removable Media]]), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.<br><br>While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle|Adversary-in-the-Middle]]), keystroke injection, kernel memory reading via DMA, addition of new wireless access points to an existing network, and others.[^1] [^2] [^4] [^3] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1034-limit-hardware-installation\|M1034]] | Limit Hardware Installation | Block unknown devices and accessories by endpoint security configuration and monitoring agent. |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Establish network access control policies, such as using device certificates and the 802.1x standard. [^1]  Restrict use of DHCP to registered devices to prevent unregistered devices from communicating with trusted systems. |

 [^1]: [Ossmann Star Feb 2011](https://ossmann.blogspot.com/2011/02/throwing-star-lan-tap.html)
 [^2]: [Aleks Weapons Nov 2015](https://www.youtube.com/watch?v=lDvf4ScWbcQ)
 [^3]: [McMillan Pwn March 2012](https://arstechnica.com/information-technology/2012/03/the-pwn-plug-is-a-little-white-box-that-can-hack-your-network/)
 [^4]: [Frisk DMA August 2016](https://www.youtube.com/watch?v=fXthwl6ShOg)
 [^5]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)
