---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1222
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1222-file-and-directory-permissions-modification
tactic:
    - Defense Impairment
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.[^2] [^3]  File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).<br><br>Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [[kb/mitre/attack/techniques/T1546.008-accessibility-features|Accessibility Features]], [[kb/mitre/attack/techniques/T1037-boot-or-logon-initialization-scripts|Boot or Logon Initialization Scripts]], [[kb/mitre/attack/techniques/T1546.004-unix-shell-configuration-modification|Unix Shell Configuration Modification]], or tainting/hijacking other instrumental binary/configuration files via [[kb/mitre/attack/techniques/T1574-hijack-execution-flow|Hijack Execution Flow]].<br><br>Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.[^7] [^4] [^1] [^6] [^5]  

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can use symbolic links to redirect file paths for remote and local objects and can use  `chmod +x` to make its payload binary executable.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Applying more restrictive permissions to files and directories could prevent adversaries from modifying their access control lists. Additionally, ensure that user settings regarding local and remote symbolic links are properly set or disabled where unneeded.[^1]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Ensure critical system files as well as those known to be abused by adversaries have restrictive permissions and are owned by an appropriately privileged account, especially if access is not required by users nor will inhibit system functionality. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1222.002-linux-and-mac-permissions\|T1222.002]] | Linux and Mac Permissions |
| [[kb/mitre/attack/techniques/T1222.001-windows-permissions\|T1222.001]] | Windows Permissions |

 [^1]: [falconoverwatch_blackcat_attack](https://www.crowdstrike.com/blog/falcon-overwatch-contributes-to-blackcat-protection/)
 [^2]: [Hybrid Analysis Icacls1 June 2018](https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100)
 [^3]: [Hybrid Analysis Icacls2 May 2018](https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110)
 [^4]: [bad_luck_blackcat](https://go.kaspersky.com/rs/802-IJN-240/images/TR_BlackCat_Report.pdf)
 [^5]: [fsutil_behavior](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-behavior)
 [^6]: [blackmatter_blackcat](https://blog.talosintelligence.com/2022/03/from-blackmatter-to-blackcat-analyzing.html)
 [^7]: [new_rust_based_ransomware](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-alphv-rust-ransomware)
 [^8]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)
 [^9]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^10]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
