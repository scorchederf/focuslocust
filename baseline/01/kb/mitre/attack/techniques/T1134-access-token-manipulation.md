---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1134
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1134-access-token-manipulation
tactic:
    - Privilege Escalation
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.<br><br>An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [[kb/mitre/attack/techniques/T1134.001-token-impersonation-theft|Token Impersonation/Theft]]) or used to spawn a new process (i.e. [[kb/mitre/attack/techniques/T1134.002-create-process-with-token|Create Process with Token]]). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.[^1] <br><br>Any standard user can use the `runas` command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | Duqu examines running system processes for tokens that have specific system privileges. If it finds one, it will copy the token and store it for later use. Eventually it will start new processes with the stored token attached. It can also steal tokens to acquire administrative privileges.[^1]  |
| [S0058](https://attack.mitre.org/software/S0058) | SslMM | SslMM contains a feature to manipulate process privileges and tokens.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-TokenManipulation` Exfiltration module can be used to manipulate tokens.[^1] [^2]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can adjust token privileges.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-TokenManipulation` to manipulate access tokens.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use Invoke-TokenManipulation for manipulating tokens.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has attempted to adjust its token privileges to have the `SeDebugPrivilege`.[^1]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT modified its security token to grants itself debugging privileges by adding `SeDebugPrivilege`.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex can enable `SeDebugPrivilege` and adjust token privileges.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk has attempted to get the access token of a process by calling `OpenProcessToken`. If KillDisk gets the access token, then it attempt to modify the token privileges with `AdjustTokenPrivileges`.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can gain system level privilege by passing `SeDebugPrivilege` to the `AdjustTokenPrivilege` API.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba has used `SeDebugPrivilege` and `AdjustTokenPrivileges` to elevate privileges.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has the ability to manipulate user tokens on targeted Windows systems.[^1] [^2]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can use token manipulation to bypass UAC on Windows7 systems.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can use `AdjustTokenPrivileges` to grant itself privileges for debugging with `SeDebugPrivilege`, creating backups with `SeBackupPrivilege`, loading drivers with `SeLoadDriverPrivilege`, and shutting down a local system with `SeShutdownPrivilege`.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can use `AdjustTokenPrivileges()` to elevate privileges.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat has the ability modify access tokens.[^2] [^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex finds the `explorer.exe` process after execution and uses it to change the token of its executing thread.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can use an embedded [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] module for token manipulation.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | An adversary must already have administrator level access on the local system to make full use of this technique; be sure to restrict users and accounts to the least privileges they require.   |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^1]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^2] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^3]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1134.002-create-process-with-token\|T1134.002]] | Create Process with Token |
| [[kb/mitre/attack/techniques/T1134.001-token-impersonation-theft\|T1134.001]] | Token Impersonation／Theft |
| [[kb/mitre/attack/techniques/T1134.003-make-and-impersonate-token\|T1134.003]] | Make and Impersonate Token |
| [[kb/mitre/attack/techniques/T1134.004-parent-pid-spoofing\|T1134.004]] | Parent PID Spoofing |
| [[kb/mitre/attack/techniques/T1134.005-sid-history-injection\|T1134.005]] | SID-History Injection |

 [^1]: [Pentestlab Token Manipulation](https://pentestlab.blog/2017/04/03/token-manipulation/)
 [^2]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^3]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^4]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^5]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^6]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^7]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^8]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^9]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)
 [^10]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)
 [^11]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^12]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^13]: [Kaspersky Duqu 2.0](https://web.archive.org/web/20150906233433/https://securelist.com/files/2015/06/The_Mystery_of_Duqu_2_0_a_sophisticated_cyberespionage_actor_returns.pdf)
 [^14]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^15]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)
 [^16]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)
 [^17]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)
 [^18]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^19]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^20]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^21]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^22]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^23]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
 [^24]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^25]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^26]: [Sophos BlackCat Jul 2022](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
 [^27]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
