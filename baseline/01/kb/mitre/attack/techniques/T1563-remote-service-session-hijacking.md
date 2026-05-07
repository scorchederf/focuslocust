---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1563
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1563-remote-service-session-hijacking
tactic:
    - Lateral Movement
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.<br><br>Adversaries may commandeer these sessions to carry out actions on remote systems. [[kb/mitre/attack/techniques/T1563-remote-service-session-hijacking|Remote Service Session Hijacking]] differs from use of [[kb/mitre/attack/techniques/T1021-remote-services|Remote Services]] because it hijacks an existing session rather than creating a new session using [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]].[^1] [^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit remote user permissions if remote access is necessary. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Do not allow remote access to services as a privileged account unless necessary. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Set and enforce secure password policies for accounts. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Enable firewall rules to block unnecessary traffic between network security zones within a network. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable the remote service (ex: SSH, RDP, etc.) if it is unnecessary. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1563.001-ssh-hijacking\|T1563.001]] | SSH Hijacking |
| [[kb/mitre/attack/techniques/T1563.002-rdp-hijacking\|T1563.002]] | RDP Hijacking |

 [^1]: [RDP Hijacking Medium](https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6)
 [^2]: [Breach Post-mortem SSH Hijack](https://matrix.org/blog/2019/05/08/post-mortem-and-remediations-for-apr-11-security-incident/)
