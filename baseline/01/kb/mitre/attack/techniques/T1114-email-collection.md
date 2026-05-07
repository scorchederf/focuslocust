---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1114
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1114-email-collection
tactic:
    - Collection
platforms:
    - Windows
    - macOS
    - Linux
    - Office Suite
permissions required:
    - none
---

## Description

Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses.[^3] [^1]  Adversaries can collect or forward email from mail servers or clients. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has been observed leveraging a module that can scrape email addresses from Outlook.[^2] [^3] [^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has exfiltrated collected email addresses to the C2 server.[^1]   |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis.<br><br>In an Exchange environment, Administrators can use Get-InboxRule to discover and remove potentially malicious auto-forwarding rules.[^1]   |
| [[kb/mitre/attack/mitigations/M1060-out-of-band-communications-channel\|M1060]] | Out-of-Band Communications Channel | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email to prevent adversaries from collecting data through compromised email accounts.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1114.001-local-email-collection\|T1114.001]] | Local Email Collection |
| [[kb/mitre/attack/techniques/T1114.003-email-forwarding-rule\|T1114.003]] | Email Forwarding Rule |
| [[kb/mitre/attack/techniques/T1114.002-remote-email-collection\|T1114.002]] | Remote Email Collection |

 [^1]: [CISA AA20-352A 2021](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)
 [^2]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)
 [^3]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)
 [^4]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^5]: [CIS Emotet Dec 2018](https://www.cisecurity.org/white-papers/ms-isac-security-primer-emotet/)
 [^6]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
 [^7]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
