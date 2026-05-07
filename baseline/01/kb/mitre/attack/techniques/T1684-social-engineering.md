---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1684
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1684-social-engineering
tactic:
    - Stealth
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

Adversaries may use social engineering techniques to influence users to take actions that result in unauthorized access, approval of changes, disclosure of sensitive information, or execution of adversary-supplied instructions (i.e., introduction of malicious payloads or software), while minimizing technical indicators. <br><br>Adversaries may leverage trust-building methods across multiple channels (e.g., executive, vendor, or help desk scenarios, including AI-enabled voice interactions) to prompt user-authorized actions such as password resets, MFA changes, financial approvals, or the disclosure of sensitive information. Adversaries may also leverage common business communications and workflows such as email, collaboration platforms, voice communications, recruiting processes, help desk interactions, and SaaS consent mechanisms to make malicious requests appear routine and legitimate.[^3] [^6] [^1] <br><br>Additionally, adversaries have persuaded victims to take actions through references of current events, harnessing relevant themes to the work role or the organizations mission. For example, adversaries may use scare tactics (i.e., threaten repercussions for non-compliance) or otherwise incite victims’ emotions in order to generate a sense of urgency to take action.[^4] [^5] <br><br>This technique may include common social engineering patterns such as [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] and [[kb/mitre/attack/techniques/T1566.004-spearphishing-voice|Spearphishing Voice]], often supported by convincing and targeted narratives.[^6] [^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Reduces success of phishing/vishing/impersonation and modern “human interface” lures.[^3] [^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1036-account-use-policies\|M1036]] | Account Use Policies | Adds verification for helpdesk resets, approvals, and app consents commonly targeted by impersonation.[^2] [^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Enables correlation of email/identity/SaaS/endpoint activity that appears legitimate.[^1] [^2]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1684.001-impersonation\|T1684.001]] | Impersonation |
| [[kb/mitre/attack/techniques/T1684.002-email-spoofing\|T1684.002]] | Email Spoofing |

 [^1]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)
 [^2]: [Fortinet Trends 25-26](https://www.fortinet.com/uk/resources/cyberglossary/recent-cyber-attacks)
 [^3]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)
 [^4]: [SE Proofpoint](https://www.proofpoint.com/us/threat-reference/social-engineering)
 [^5]: [SE SentinelOne](https://www.sentinelone.com/blog/social-engineering-attacks-how-to-recognize-and-resist-the-bait/)
 [^6]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)
 [^7]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)
 [^8]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)
