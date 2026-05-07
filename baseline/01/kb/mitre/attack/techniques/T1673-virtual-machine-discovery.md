---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1673
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1673-virtual-machine-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [[kb/mitre/attack/techniques/T1059.012-hypervisor-cli|Hypervisor CLI]] such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).[^2] [^1]  Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1673-virtual-machine-discovery|Virtual Machine Discovery]] during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as [[kb/mitre/attack/techniques/T1489-service-stop|Service Stop]] or [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]].[^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1096](https://attack.mitre.org/software/S1096) | Cheerscrypt | Cheerscrypt has leveraged `esxcli vm process list` in order to gather a list of running virtual machines to terminate them.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA can target specific guest virtual machines for script execution.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can detect virtual machine environments including ESXi hosts, datacenters, and clusters within vCenter environments.[^1] [^2]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can identify virtual machines by querying the WMI object Win32_ComputerSystem for manufacturer and model and check it against the regular expression Microsoft\|VMWare\|Virtual.[^1]  |

 [^1]: [TrendMicro Play](https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html)
 [^2]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^3]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^4]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^5]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^6]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^7]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
