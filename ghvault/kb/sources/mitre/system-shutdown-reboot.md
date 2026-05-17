---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Shutdown／Reboot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1529` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Shutdown／Reboot](../../attack/techniques/T1529-system-shutdown-reboot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1529 |
| name | System Shutdown／Reboot |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1529 |

## Preserved Source Material

```yaml
created: '2019-10-04T20:42:28.541Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems.\
  \ Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these\
  \ commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008)\
  \ (e.g. <code>reload</code>).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) They may also include shutdown/reboot\
  \ of a virtual machine via hypervisor / cloud consoles or command line tools.\n\nShutting down or rebooting systems may\
  \ disrupt access to computer resources for legitimate users while also impeding incident response/recovery.\n\nAdversaries\
  \ may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut\
  \ down or reboot.(Citation: CrowdStrike Blog)(Citation: Unit42 Agrius 2023) Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError`\
  \ Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of\
  \ death” (BSOD) to a system.(Citation: SonicWall)(Citation: NtRaiseHardError)(Citation: NotMe-BSOD) In order to leverage\
  \ these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [Access Token Manipulation](https://attack.mitre.org/techniques/T1134)).(Citation:\
  \ Unit42 Agrius 2023)\n In some cases, the system may not be able to boot again. \n\nAdversaries may attempt to shutdown/reboot\
  \ a system after impacting it in other ways, such as [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002)\
  \ or [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490), to hasten the intended effects on system availability.(Citation:\
  \ Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)"
external_references:
- external_id: T1529
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1529
- description: Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26,
    2019.
  source_name: Talos Nyetya June 2017
  url: https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html
- description: CISA. (2018, April 20). Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved
    February 14, 2022.
  source_name: alert_TA18_106A
  url: https://www.cisa.gov/uscert/ncas/alerts/TA18-106A
- description: lzcapp. (n.d.). Retrieved September 22, 2025.
  source_name: NotMe-BSOD
  url: https://github.com/lzcapp/NotMe-BSOD
- description: Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved
    March 14, 2019.
  source_name: Talos Olympic Destroyer 2018
  url: https://blog.talosintelligence.com/2018/02/olympic-destroyer.html
- description: Microsoft. (2017, October 15). Shutdown. Retrieved October 4, 2019.
  source_name: Microsoft Shutdown Oct 2017
  url: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown
- description: NtDoc. (n.d.). NtRaiseHardError - NtDoc. Retrieved September 22, 2025.
  source_name: NtRaiseHardError
  url: https://ntdoc.m417z.com/ntraiseharderror
- description: Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting
    the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.
  source_name: Unit42 Agrius 2023
  url: https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/
- description: 'SecurityNews. (2024, July 12). Disarming DarkGate: A Deep Dive into Thwarting the Latest DarkGate Variant.
    Retrieved September 22, 2025.'
  source_name: SonicWall
  url: https://www.sonicwall.com/blog/disarming-darkgate-a-deep-dive-into-thwarting-the-latest-darkgate-variant
- description: William Thomas, Adrian Liviu Arsene, Farid Hendi. (2022, February 25). CrowdStrike Falcon® Protects from New
    Wiper Malware Used in Ukraine Cyberattacks. Retrieved September 22, 2025.
  source_name: CrowdStrike Blog
  url: https://www.crowdstrike.com/en-us/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/
id: attack-pattern--ff73aa03-0090-4464-83ac-f89e233c02bc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:49:40.145Z'
name: System Shutdown/Reboot
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Austin Clark, @c2defense
- Hubert Mank
- Janantha Marasinghe
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.5'
```
