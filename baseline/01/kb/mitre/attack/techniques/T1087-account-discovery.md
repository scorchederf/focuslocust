---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1087
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1087-account-discovery
tactic:
    - Discovery
platforms:
    - ESXi
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

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]]).<br><br>Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.<br><br>For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.[^1] [^2]  On hosts, adversaries can use default [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] listed all non-privileged and privileged accounts available on the machine.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET attempts to discover accounts from various locations such as a user's Evernote, AppleID, Telegram, Skype, and WeChat data.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can identify administrator accounts on an infected machine.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can identify privileged user accounts on infected systems.[^1] <br> |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL included functionality to retrieve a list of user accounts.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Manage the creation, modification, use, and permissions associated to user accounts. |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located `HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\EnumerateAdministrators`. It can be disabled through GPO: Computer Configuration > [Policies] > Administrative Templates > Windows Components > Credential User Interface: E numerate administrator accounts on elevation. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account |
| [[kb/mitre/attack/techniques/T1087.003-email-account\|T1087.003]] | Email Account |
| [[kb/mitre/attack/techniques/T1087.004-cloud-account\|T1087.004]] | Cloud Account |

 [^1]: [AWS List Users](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)
 [^2]: [Google Cloud - IAM Servie Accounts List API](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)
 [^3]: [Elastic - Koadiac Detection with EQL](https://www.elastic.co/security-labs/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
 [^4]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^5]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)
 [^6]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^7]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
 [^8]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^9]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
