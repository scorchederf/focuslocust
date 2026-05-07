---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1484
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/identity_provider
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1484-domain-or-tenant-policy-modification
tactic:
    - Defense Impairment
    - Privilege Escalation
platforms:
    - Windows
    - Identity Provider
permissions required:
    - none
---

## Description

Adversaries may modify the configuration settings of a domain or identity tenant to evade defenses and/or escalate privileges in centrally managed environments. Such services provide a centralized means of managing identity resources such as devices and accounts, and often include configuration settings that may apply between domains or tenants such as trust relationships, identity syncing, or identity federation.<br><br>Modifications to domain or tenant settings may include altering domain Group Policy Objects (GPOs) in Microsoft Active Directory (AD) or changing trust settings for domains, including federation trusts relationships between domains or tenants.<br><br>With sufficient permissions, adversaries can modify domain or tenant policy settings. Since configuration settings for these services apply to a large number of identity resources, there are a great number of potential attacks malicious outcomes that can stem from this abuse. Examples of such abuse include:  <br><br>* modifying GPOs to push a malicious [[kb/mitre/attack/techniques/T1053.005-scheduled-task|Scheduled Task]] to computers throughout the domain environment[^1] [^4] [^5] <br>* modifying domain trusts to include an adversary-controlled domain, allowing adversaries to  forge access tokens that will subsequently be accepted by victim domain resources[^2] <br>* changing configuration settings within the AD environment to implement a [[kb/mitre/attack/techniques/T1207-rogue-domain-controller|Rogue Domain Controller]].<br>* adding new, adversary-controlled federated identity providers to identity tenants, allowing adversaries to authenticate as any user managed by the victim tenant [^3] <br><br>Adversaries may temporarily modify domain or tenant policy, carry out a malicious action(s), and then revert the change to remove suspicious indicators.

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Consider implementing WMI and security filtering to further tailor which users and computers a GPO will apply to.[^1] [^2] [^3]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Use least privilege and protect administrative access to the Domain Controller and Active Directory Federation Services (AD FS) server. Do not create service accounts with administrative privileges. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] (version 1.5.1 and later)[^1] . |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1484.002-trust-modification\|T1484.002]] | Trust Modification |
| [[kb/mitre/attack/techniques/T1484.001-group-policy-modification\|T1484.001]] | Group Policy Modification |

 [^1]: [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)
 [^2]: [Microsoft - Customer Guidance on Recent Nation-State Cyber Attacks](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)
 [^3]: [Okta Cross-Tenant Impersonation 2023](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection)
 [^4]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)
 [^5]: [Harmj0y Abusing GPO Permissions](https://blog.harmj0y.net/redteaming/abusing-gpo-permissions/)
 [^6]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)
 [^7]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)
 [^8]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)
