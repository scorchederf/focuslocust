---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1650
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1650-acquire-access
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems.[^4] [^2] [^1]  In some cases, adversary groups may form partnerships to share compromised systems with each other.[^3] <br><br>Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., [[kb/mitre/attack/techniques/T1505.003-web-shell|Web Shell]]) or established access via [[kb/mitre/attack/techniques/T1133-external-remote-services|External Remote Services]]. In some cases, access brokers will implant compromised systems with a “load” that can be used to install additional malware for paying customers.[^4] <br><br>By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector.[^4] [^2] <br><br>In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]], [[kb/mitre/attack/techniques/T1111-multi-factor-authentication-interception|Multi-Factor Authentication Interception]], or even [[kb/mitre/attack/techniques/T1195-supply-chain-compromise|Supply Chain Compromise]].<br><br>**Note:** while this technique is distinct from other behaviors such as [[kb/mitre/attack/techniques/T1597.002-purchase-technical-data|Purchase Technical Data]] and [[kb/mitre/attack/techniques/T1589.001-credentials|Credentials]], they may often be used in conjunction (especially where the acquired foothold requires [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls.  |

 [^1]: [Krebs Access Brokers Fortune 500](https://krebsonsecurity.com/2012/10/service-sells-access-to-fortune-500-firms/)
 [^2]: [CrowdStrike Access Brokers](https://www.crowdstrike.com/blog/access-brokers-targets-and-worth/)
 [^3]: [CISA Karakurt 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-152a)
 [^4]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
