---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1667
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1667-email-bombing
tactic:
    - Impact
platforms:
    - Linux
    - Office Suite
    - Windows
    - macOS
permissions required:
    - none
---

## Description

Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate emails in a flood of spam and disrupt business operations.[^2] [^1] <br><br>An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively overloads the victim’s inbox.[^1] [^4] <br><br>By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence, or ongoing scams.[^4]  This behavior can also be used as a tool of harassment.[^1] <br><br>This behavior may be a precursor for [[kb/mitre/attack/techniques/T1566.004-spearphishing-voice|Spearphishing Voice]]. For example, an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social engineering may lead to the use of Remote Access Software to steal credentials, deploy ransomware, conduct [[kb/mitre/attack/techniques/T1657-financial-theft|Financial Theft]][^2] , or engage in other malicious activity.[^3] <br>

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful social engineering via e-mail bombing. |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^2] [^1]  Note that additional filtering may be necessary if emails are coming from legitimate sources.  |

 [^1]: [krebs-email-bombing](https://krebsonsecurity.com/2016/08/massive-email-bombs-target-gov-addresses/)
 [^2]: [sophos-bombing](https://news.sophos.com/en-us/2025/01/21/sophos-mdr-tracks-two-ransomware-campaigns-using-email-bombing-microsoft-teams-vishing/)
 [^3]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
 [^4]: [hhs-email-bombing](https://www.hhs.gov/sites/default/files/email-bombing-sector-alert-tlpclear.pdf)
 [^5]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
 [^6]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
