---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1542
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1542-pre-os-boot
tactic:
    - Persistence
    - Stealth
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.[^1] <br><br>Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Ensure proper permissions are in place to help prevent adversary access to privileged accounts necessary to perform these actions |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Prevent access to file shares, remote access to systems, unnecessary services. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc. |
| [[kb/mitre/attack/mitigations/M1046-boot-integrity\|M1046]] | Boot Integrity | Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised. Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. [^1]  [^2]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Patch the BIOS and EFI as necessary. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1542.001-system-firmware\|T1542.001]] | System Firmware |
| [[kb/mitre/attack/techniques/T1542.003-bootkit\|T1542.003]] | Bootkit |
| [[kb/mitre/attack/techniques/T1542.005-tftp-boot\|T1542.005]] | TFTP Boot |
| [[kb/mitre/attack/techniques/T1542.002-component-firmware\|T1542.002]] | Component Firmware |
| [[kb/mitre/attack/techniques/T1542.004-rommonkit\|T1542.004]] | ROMMONkit |

 [^1]: [Wikipedia Booting](https://en.wikipedia.org/wiki/Booting)
 [^2]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)
 [^3]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)
