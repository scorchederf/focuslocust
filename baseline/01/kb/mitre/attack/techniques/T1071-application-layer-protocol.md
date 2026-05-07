---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1071
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1071-application-layer-protocol
tactic:
    - Command And Control
platforms:
    - Linux
    - macOS
    - Windows
    - Network Devices
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. <br><br>Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.[^2]  

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | Adversaries can also use NETEAGLE to establish an RDP connection with a controller over TCP/7519. |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | Duqu uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can use the Stratum protocol on port 10001 for communication between the cryptojacking bot and the mining server.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has used an IRC channel for C2 communications.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape connects to an IRC server for C2.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can utilize the Wireguard VPN protocol for command and control.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to use Telnet for communication.[^1]  |
| [S1084](https://attack.mitre.org/software/S1084) | QUIETEXIT | QUIETEXIT can use an inverse negotiated SSH connection as part of its C2.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin is capable of contacting the TOR network for delivering second-stage payloads.[^2] [^1] [^3]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor uses TCP and UDP communication for command and control traffic.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1071.004-dns\|T1071.004]] | DNS |
| [[kb/mitre/attack/techniques/T1071.005-publish-subscribe-protocols\|T1071.005]] | Publish／Subscribe Protocols |
| [[kb/mitre/attack/techniques/T1071.003-mail-protocols\|T1071.003]] | Mail Protocols |
| [[kb/mitre/attack/techniques/T1071.002-file-transfer-protocols\|T1071.002]] | File Transfer Protocols |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^3]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^4]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^5]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^6]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^7]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
 [^8]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^9]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^10]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
 [^11]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^12]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^13]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
