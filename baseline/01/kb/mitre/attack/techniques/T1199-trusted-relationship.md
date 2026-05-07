---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1199
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1199-trusted-relationship
tactic:
    - Initial Access
platforms:
    - IaaS
    - Identity Provider
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.<br><br>Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] used by the other party for access to internal network systems may be compromised and used.[^1] <br><br>In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.[^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Properly manage accounts and permissions used by parties in trusted relationships to minimize potential abuse by the party and if the party is compromised by an adversary. In Office 365 environments, partner relationships and roles can be viewed under the “Partner Relationships” page.[^1] <br> |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Require MFA for all delegated administrator accounts.[^1]  |

 [^1]: [CISA IT Service Providers](https://us-cert.cisa.gov/APTs-Targeting-IT-Service-Provider-Customers)
 [^2]: [Office 365 Delegated Administration](https://support.microsoft.com/en-us/topic/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e?ui=en-us&rs=en-us&ad=us)
 [^3]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)
 [^4]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)
