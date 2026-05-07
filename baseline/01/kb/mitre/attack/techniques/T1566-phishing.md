---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1566
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1566-phishing
tactic:
    - Initial Access
platforms:
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

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.<br><br>Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [[kb/mitre/attack/techniques/T1564.008-email-hiding-rules|Email Hiding Rules]]).[^5] [^8]  Another way to accomplish this is by [[kb/mitre/attack/techniques/T1684.002-email-spoofing|Email Spoofing]][^7]  the identity of the sender, which can be used to fool both the human recipient as well as automated security tools,[^3]  or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking").[^1] <br><br>Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,[^6] [^2]  or install adversary-accessible remote management tools onto their computer (i.e., [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]]).[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0009](https://attack.mitre.org/software/S0009) | Hikit | Hikit has been spread through spear phishing.[^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal has been spread through the use of phishing campaigns including "call back phishing" where victims are lured into calling a number provided through email.[^2] [^3] [^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware campaigns have used spearphishing emails for initial access.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Users can be trained to identify social engineering techniques and phishing emails. |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Determine if certain websites or attachment types (ex: .scr, .exe, .pif, .cpl, etc.) that can be used for phishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion prevention systems and systems designed to scan and remove malicious email attachments or links can be used to block activity. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Anti-virus can automatically quarantine suspicious files. |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^2] [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1566.002-spearphishing-link\|T1566.002]] | Spearphishing Link |
| [[kb/mitre/attack/techniques/T1566.001-spearphishing-attachment\|T1566.001]] | Spearphishing Attachment |
| [[kb/mitre/attack/techniques/T1566.004-spearphishing-voice\|T1566.004]] | Spearphishing Voice |
| [[kb/mitre/attack/techniques/T1566.003-spearphishing-via-service\|T1566.003]] | Spearphishing via Service |

 [^1]: [phishing-krebs](https://krebsonsecurity.com/2024/03/thread-hijacking-phishes-that-prey-on-your-curiosity/)
 [^2]: [CISA Remote Monitoring and Management Software](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a)
 [^3]: [cyberproof-double-bounce](https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends)
 [^4]: [Unit42 Luna Moth](https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/)
 [^5]: [Microsoft OAuth Spam 2022](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/)
 [^6]: [sygnia Luna Month](https://blog.sygnia.co/luna-moth-false-subscription-scams)
 [^7]: [Proofpoint-spoof](https://www.proofpoint.com/us/threat-reference/email-spoofing)
 [^8]: [Palo Alto Unit 42 VBA Infostealer 2014](https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/)
 [^9]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^10]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)
 [^11]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
 [^12]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
 [^13]: [CISA Royal AA23-061A March 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)
 [^14]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^15]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
