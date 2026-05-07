---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1585
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1585-establish-accounts
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may create and cultivate accounts with services that can be used during targeting. Adversaries can create accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations. This development could be applied to social media, website, or other publicly available information that could be referenced and scrutinized for legitimacy over the course of an operation using that persona or identity.[^2] [^4] <br><br>For operations incorporating social engineering, the utilization of an online persona may be important. These personas may be fictitious or impersonate real people. The persona may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, GitHub, Docker Hub, etc.). Establishing a persona may require development of additional documentation to make them seem real. This could include filling out profile information, developing social networks, or incorporating photos.[^2] [^4] <br><br>Establishing accounts can also include the creation of accounts with email providers, which may be directly leveraged for [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]] or [[kb/mitre/attack/techniques/T1566-phishing|Phishing]].[^3]  In addition, establishing accounts may allow adversaries to abuse free services, such as registering for trial periods to [[kb/mitre/attack/techniques/T1583-acquire-infrastructure|Acquire Infrastructure]] for malicious purposes.[^1] <br>

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1585.002-email-accounts\|T1585.002]] | Email Accounts |
| [[kb/mitre/attack/techniques/T1585.003-cloud-accounts\|T1585.003]] | Cloud Accounts |
| [[kb/mitre/attack/techniques/T1585.001-social-media-accounts\|T1585.001]] | Social Media Accounts |

 [^1]: [Free Trial PurpleUrchin](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/)
 [^2]: [NEWSCASTER2014](https://www.securityweek.com/iranian-hackers-targeted-us-officials-elaborate-social-media-attack-operation)
 [^3]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^4]: [BlackHatRobinSage](http://media.blackhat.com/bh-us-10/whitepapers/Ryan/BlackHat-USA-2010-Ryan-Getting-In-Bed-With-Robin-Sage-v1.0.pdf)
