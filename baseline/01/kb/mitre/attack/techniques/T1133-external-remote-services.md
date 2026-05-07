---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1133
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/persistence
    - attack/type/technique
    - platform/containers
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1133-external-remote-services
tactic:
    - Initial Access
    - Persistence
platforms:
    - Containers
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [[kb/mitre/attack/techniques/T1021.006-windows-remote-management|Windows Remote Management]] and [[kb/mitre/attack/techniques/T1021.005-vnc|VNC]] can also be used externally.[^2] <br><br>Access to [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.[^1]  Access to remote services may be used as a redundant or persistent access mechanism during an operation.<br><br>Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.[^6] [^3] <br><br>Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access.[^5]  Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0362](https://attack.mitre.org/software/S0362) | Linux Rabbit | Linux Rabbit attempts to gain access to the server via SSH.[^1]  |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing was executed in an Ubuntu container deployed via an open Docker daemon API.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki was executed through an open Docker daemon API port.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard was executed through an unsecure kubelet that allowed anonymous access to the victim environment.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can establish an SSH connection from a compromised host to a server.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Restrict all traffic to and from public Tor nodes. [^1]  |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use strong two-factor or multi-factor authentication for remote service accounts to mitigate an adversary's ability to leverage stolen credentials, but be aware of [[kb/mitre/attack/techniques/T1111-multi-factor-authentication-interception\|Multi-Factor Authentication Interception]] techniques for some two-factor authentication implementations. |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable or block remotely available services that may be unnecessary. |

 [^1]: [Volexity Virtual Private Keylogging](https://www.volexity.com/blog/2015/10/07/virtual-private-keylogging-cisco-web-vpns-leveraged-for-access-and-persistence/)
 [^2]: [MacOS VNC software for Remote Desktop](https://support.apple.com/guide/remote-desktop/set-up-a-computer-running-vnc-software-apdbed09830/mac)
 [^3]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^4]: [Russian threat actors dig in, prepare to seize on war fatigue](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/russian-threat-actors-dig-in-prepare-to-seize-on-war-fatigue)
 [^5]: [The BadPilot campaign](https://www.microsoft.com/en-us/security/blog/2025/02/12/the-badpilot-campaign-seashell-blizzard-subgroup-conducts-multiyear-global-access-operation/?ref=thestack.technology)
 [^6]: [Trend Micro Exposed Docker Server](https://www.trendmicro.com/en_us/research/20/f/xorddos-kaiji-botnet-malware-variants-target-exposed-docker-servers.html)
 [^7]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
 [^8]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^9]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)
 [^10]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^11]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
