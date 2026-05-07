---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1003
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1003-os-credential-dumping
tactic:
    - Credential Access
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.[^10]  Credentials can then be used to perform [[kb/mitre/attack/tactics/TA0008-lateral-movement|Lateral Movement]] and access restricted information.<br><br>Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.<br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak obtains Windows logon password details.[^1]  |
| [S0048](https://attack.mitre.org/software/S0048) | PinchDuke | PinchDuke steals credentials from compromised hosts. PinchDuke's credential stealing functionality is believed to be based on the source code of the Pinch credential stealing malware (also known as LdPinch). Credentials targeted by PinchDuke include ones associated many sources such as WinInet Credential Cache, and Lightweight Directory Access Protocol (LDAP).[^1]  |
| [S0052](https://attack.mitre.org/software/S0052) | OnionDuke | OnionDuke steals credentials from its victims.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can dump passwords and save them into `\ProgramData\Mail\MailAg\pwds.txt`.[^1]  |
| [S0232](https://attack.mitre.org/software/S0232) | HOMEFRY | HOMEFRY can perform credential dumping.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT has a plugin for credential harvesting.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for dumping and capturing credentials from process memory.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-active-directory-configuration\|M1015]] | Active Directory Configuration | <br>Manage the access control list for “Replicating Directory Changes All” and other permissions associated with domain controller replication. [^1]  [^3]  Consider adding users to the "Protected Users" Active Directory security group. This can help limit the caching of users' plaintext credentials.[^2]  |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[kb/mitre/attack/mitigations/M1025-privileged-process-integrity\|M1025]] | Privileged Process Integrity | <br>On Windows 8.1 and Windows Server 2012 R2, enable Protected Process Light for LSA.[^1]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Windows:<br>Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers.[^1] <br><br>Linux:<br>Scraping the passwords from memory requires root privileges. Follow best practices in restricting access to privileged accounts to avoid hostile programs from accessing such sensitive regions of memory. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | <br>Consider disabling or restricting NTLM.[^1]  Consider disabling WDigest authentication.[^2]  |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to secure LSASS and prevent credential stealing. [^1]  |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Ensure Domain Controller backups are properly secured. |
| [[kb/mitre/attack/mitigations/M1043-credential-access-protection\|M1043]] | Credential Access Protection | With Windows 10, Microsoft implemented new protections called Credential Guard to protect the LSA secrets that can be used to obtain credentials through forms of credential dumping. It is not configured by default and has hardware and firmware system requirements. [^1]  It also does not protect against all forms of credential dumping. [^2]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1003.002-security-account-manager\|T1003.002]] | Security Account Manager |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets |
| [[kb/mitre/attack/techniques/T1003.007-proc-filesystem\|T1003.007]] | Proc Filesystem |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory |
| [[kb/mitre/attack/techniques/T1003.005-cached-domain-credentials\|T1003.005]] | Cached Domain Credentials |
| [[kb/mitre/attack/techniques/T1003.008-etc-passwd-and-etc-shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow |
| [[kb/mitre/attack/techniques/T1003.003-ntds\|T1003.003]] | NTDS |
| [[kb/mitre/attack/techniques/T1003.006-dcsync\|T1003.006]] | DCSync |

 [^1]: [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)
 [^2]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)
 [^3]: [Microsoft DRSR Dec 2017](https://msdn.microsoft.com/library/cc228086.aspx)
 [^4]: [Microsoft NRPC Dec 2017](https://msdn.microsoft.com/library/cc237008.aspx)
 [^5]: [Microsoft GetNCCChanges](https://msdn.microsoft.com/library/dd207691.aspx)
 [^6]: [Microsoft SAMR](https://msdn.microsoft.com/library/cc245496.aspx)
 [^7]: [Powersploit](https://github.com/mattifestation/PowerSploit)
 [^8]: [Samba DRSUAPI](https://wiki.samba.org/index.php/DRSUAPI)
 [^9]: [Harmj0y DCSync Sept 2015](http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)
 [^10]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
 [^11]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^12]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^13]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^14]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^15]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^16]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^17]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)
 [^18]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
 [^19]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^20]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)
 [^21]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)
 [^22]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)
 [^23]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)
 [^24]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)
 [^25]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)
