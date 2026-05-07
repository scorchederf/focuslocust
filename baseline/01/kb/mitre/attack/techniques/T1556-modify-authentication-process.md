---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1556
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/tactic/defense_impairment
    - attack/tactic/persistence
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1556-modify-authentication-process
tactic:
    - Credential Access
    - Defense Impairment
    - Persistence
platforms:
    - IaaS
    - Identity Provider
    - Linux
    - macOS
    - Network Devices
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]].<br><br>Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury can intercept private keys using a trojanized `ssh-add` function.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has trojanized the <sode>ssh_login` and `user-auth_pubkey` functions to steal plaintext credentials.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.[^1]  |
| [S9013](https://attack.mitre.org/software/S9013) | DRYHOOK | DRYHOOK has intercepted and logged user credentials by modifying the Perl module in Ivanti Connect Secure VPN edge-devices located within `/home/perl/DSAuth.pm`.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure that proper policies are implemented to dictate the the secure enrollment and deactivation of authentication mechanisms, such as MFA, for user accounts. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Restrict write access to the `/Library/Security/SecurityAgentPlugins` directory. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[kb/mitre/attack/mitigations/M1025-privileged-process-integrity\|M1025]] | Privileged Process Integrity | Enabled features, such as Protected Process Light (PPL), for LSA.[^1]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [^2]  [^3]  These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [^4] <br><br>Limit access to the root account and prevent users from modifying protected components through proper privilege separation (ex SELinux, grsecurity, AppArmor, etc.) and limiting Privilege Escalation opportunities.<br><br>Limit on-premises accounts with access to the hybrid identity solution in place. For example, limit Azure AD Global Administrator accounts to only those required, and ensure that these are dedicated cloud-only accounts rather than hybrid ones.[^1]  |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Ensure that `AllowReversiblePasswordEncryption` property is set to disabled unless there are application requirements.[^1]  |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (`C:\Windows\System32\` by default) of a domain controller and/or local computer with a corresponding entry in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages`. <br><br>Starting in Windows 11 22H2, the `EnableMPRNotifications` policy can be disabled through Group Policy or through a configuration service provider to prevent Winlogon from sending credentials to network providers.[^1]  |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs.  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Review authentication logs to ensure that mechanisms such as enforcement of MFA are functioning as intended.<br><br>Periodically review the hybrid identity solution in use for any discrepancies. For example, review all Pass Through Authentication (PTA) agents in the Azure Management Portal to identify any unwanted or unapproved ones.[^2]  If ADFS is in use, review DLLs and executable files in the AD FS and Global Assembly Cache directories to ensure that they are signed by Microsoft. Note that in some cases binaries may be catalog-signed, which may cause the file to appear unsigned when viewing file properties.[^1] <br><br>Periodically review for new and unknown network provider DLLs within the Registry (`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<NetworkProviderName>\NetworkProvider\ProviderPath`). Ensure only valid network provider DLLs are registered. The name of these can be found in the Registry key at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`, and have corresponding service subkey pointing to a DLL at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentC ontrolSet\Services\<NetworkProviderName>\NetworkProvider`. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1556.003-pluggable-authentication-modules\|T1556.003]] | Pluggable Authentication Modules |
| [[kb/mitre/attack/techniques/T1556.002-password-filter-dll\|T1556.002]] | Password Filter DLL |
| [[kb/mitre/attack/techniques/T1556.007-hybrid-identity\|T1556.007]] | Hybrid Identity |
| [[kb/mitre/attack/techniques/T1556.008-network-provider-dll\|T1556.008]] | Network Provider DLL |
| [[kb/mitre/attack/techniques/T1556.006-multi-factor-authentication\|T1556.006]] | Multi-Factor Authentication |
| [[kb/mitre/attack/techniques/T1556.009-conditional-access-policies\|T1556.009]] | Conditional Access Policies |
| [[kb/mitre/attack/techniques/T1556.001-domain-controller-authentication\|T1556.001]] | Domain Controller Authentication |
| [[kb/mitre/attack/techniques/T1556.005-reversible-encryption\|T1556.005]] | Reversible Encryption |
| [[kb/mitre/attack/techniques/T1556.004-network-device-authentication\|T1556.004]] | Network Device Authentication |

 [^1]: [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
 [^2]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)
 [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^4]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^5]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^6]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^7]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)
 [^8]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)
 [^9]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)
 [^10]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)
 [^11]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
 [^12]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)
 [^13]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)
