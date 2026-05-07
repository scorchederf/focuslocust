---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1534
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1534-internal-spearphishing
tactic:
    - Lateral Movement
platforms:
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [[kb/mitre/attack/techniques/T1684.001-impersonation|Impersonation]].[^2] <br><br>For example, adversaries may leverage [[kb/mitre/attack/techniques/T1566.001-spearphishing-attachment|Spearphishing Attachment]] or [[kb/mitre/attack/techniques/T1566.002-spearphishing-link|Spearphishing Link]] as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [[kb/mitre/attack/techniques/T1056-input-capture|Input Capture]] on sites that mimic login interfaces.<br><br>Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can send its Setup.exe file as an attachment to other addresses in the same compromised organization.[^1]  |

 [^1]: [Int SP - chat apps](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/)
 [^2]: [Trend Micro - Int SP](https://www.trendmicro.com/en_us/research.html)
 [^3]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
