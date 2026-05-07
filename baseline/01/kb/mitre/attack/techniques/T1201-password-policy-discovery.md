---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1201
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1201-password-policy-discovery
tactic:
    - Discovery
platforms:
    - Windows
    - Linux
    - macOS
    - IaaS
    - Network Devices
    - Identity Provider
    - SaaS
    - Office Suite
permissions required:
    - none
---

## Description

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through [[kb/mitre/attack/techniques/T1110-brute-force|Brute Force]]. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).<br><br>Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as `net accounts (/domain)`, `Get-ADDefaultDomainPasswordPolicy`, `chage -l <username>`, `cat /etc/pam.d/common-password`, and `pwpolicy getaccountpolicies` [^3]  [^2] . Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] on network devices to discover password policy information (e.g. `show aaa`, `show aaa common-criteria policy all`).[^4] <br><br>Password policies can be discovered in cloud environments using available APIs such as `GetAccountPasswordPolicy` in AWS [^1] .

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | The `net accounts` and `net accounts /domain` commands with [[kb/mitre/attack/software/S0039-net\|Net]] can be used to obtain password policy information.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects password policy information with the command `net accounts`.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use `Get-PassPol` to enumerate the domain password policy.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover the password policies applied to the target system.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (`C:\Windows\System32\` by default) of a domain controller and/or local computer with a corresponding entry in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages`. [^1]  |

 [^1]: [AWS GetPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html)
 [^2]: [Jamf User Password Policies](https://www.jamf.com/jamf-nation/discussions/18574/user-password-policies-on-non-ad-machines)
 [^3]: [Superuser Linux Password Policies](https://superuser.com/questions/150675/how-to-display-password-policy-information-for-a-user-ubuntu)
 [^4]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^5]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
 [^6]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^7]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^8]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)
 [^9]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
