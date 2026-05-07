---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1495
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1495-firmware-corruption
tactic:
    - Impact
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system.[^4]  Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.<br><br>In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable.[^2] [^1]  Depending on the device, this attack may also result in [[kb/mitre/attack/techniques/T1485-data-destruction|Data Destruction]]. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot module "Trickboot" can write or erase the UEFI/BIOS firmware of a compromised device.[^1]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit has used an executable that installs a modified bootloader to prevent normal boot-up.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Prevent adversary access to privileged accounts or access necessary to replace system firmware. |
| [[kb/mitre/attack/mitigations/M1046-boot-integrity\|M1046]] | Boot Integrity | Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Patch the BIOS and other firmware as necessary to prevent successful use of known vulnerabilities. |

 [^1]: [cisa_malware_orgs_ukraine](https://www.cisa.gov/uscert/ncas/alerts/aa22-057a)
 [^2]: [dhs_threat_to_net_devices](https://cyber.dhs.gov/assets/report/ar-16-20173.pdf)
 [^3]: [MITRE Trustworthy Firmware Measurement](http://www.mitre.org/publications/project-stories/going-deep-into-the-bios-with-mitre-firmware-security-research)
 [^4]: [Symantec Chernobyl W95.CIH](https://web.archive.org/web/20190508170055/https://www.symantec.com/security-center/writeup/2000-122010-2655-99)
 [^5]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)
 [^6]: [Eclypsium Trickboot December 2020](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)
