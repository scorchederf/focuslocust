---
parsed_by: focuslocust
source: mitre
type: generated
---
# Inhibit System Recovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1490` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Inhibit System Recovery](../../attack/techniques/T1490-inhibit-system-recovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1490 |
| name | Inhibit System Recovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1490 |

## Preserved Source Material

```yaml
created: '2019-04-02T13:54:43.136Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted
  system to prevent recovery.(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) This may deny access
  to available backups and recovery options.


  Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies,
  and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [Data
  Destruction](https://attack.mitre.org/techniques/T1485) and [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation:
  Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) Furthermore, adversaries may disable recovery notifications,
  then corrupt backups.(Citation: disable_notif_synology_ransom)


  A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:


  * <code>vssadmin.exe</code> can be used to delete all volume shadow copies on a system - <code>vssadmin.exe delete shadows
  /all /quiet</code>

  * [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) can be used to delete volume shadow copies
  - <code>wmic shadowcopy delete</code>

  * <code>wbadmin.exe</code> can be used to delete the Windows Backup Catalog - <code>wbadmin.exe delete catalog -quiet</code>

  * <code>bcdedit.exe</code> can be used to disable automatic Windows recovery features by modifying boot configuration data
  - <code>bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no</code>

  * <code>REAgentC.exe</code> can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected
  system

  * <code>diskshadow.exe</code> can be used to delete all volume shadow copies on a system - <code>diskshadow delete shadows
  all</code> (Citation: Diskshadow) (Citation: Crytox Ransomware)


  On network devices, adversaries may leverage [Disk Wipe](https://attack.mitre.org/techniques/T1561) to delete backup firmware
  images and reformat the file system, then [System Shutdown/Reboot](https://attack.mitre.org/techniques/T1529) to reload
  the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.


  On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486),
  preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`).(Citation: Cybereason)


  Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or
  through folders that sync to cloud services.(Citation: ZDNet Ransomware Backups 2020) In cloud environments, adversaries
  may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of
  objects designed to be used in disaster recovery scenarios.(Citation: Dark Reading Code Spaces Cyber Attack)(Citation: Rhino
  Security Labs AWS S3 Ransomware)'
external_references:
- external_id: T1490
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1490
- description: ' Brian Prince. (2014, June 20). Code Hosting Service Shuts Down After Cyber Attack. Retrieved March 21, 2023.'
  source_name: Dark Reading Code Spaces Cyber Attack
  url: https://www.darkreading.com/attacks-breaches/code-hosting-service-shuts-down-after-cyber-attack
- description: Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.
  source_name: FireEye WannaCry 2017
  url: https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html
- description: Cybereason Nocturnus. (n.d.). Cybereason vs. BlackCat Ransomware. Retrieved March 26, 2025.
  source_name: Cybereason
  url: https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware
- description: Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved
    March 14, 2019.
  source_name: Talos Olympic Destroyer 2018
  url: https://blog.talosintelligence.com/2018/02/olympic-destroyer.html
- description: Microsoft Windows Server. (2023, February 3). Diskshadow. Retrieved November 21, 2023.
  source_name: Diskshadow
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow
- description: Romain Dumont . (2022, September 21). Technical Analysis of Crytox Ransomware. Retrieved November 22, 2023.
  source_name: Crytox Ransomware
  url: https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware
- description: 'Spencer Gietzen. (n.d.). AWS Simple Storage Service S3 Ransomware Part 2: Prevention and Defense. Retrieved
    March 21, 2023.'
  source_name: Rhino Security Labs AWS S3 Ransomware
  url: https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/
- description: Steve Ranger. (2020, February 27). Ransomware victims thought their backups were safe. They were wrong. Retrieved
    March 21, 2023.
  source_name: ZDNet Ransomware Backups 2020
  url: https://www.zdnet.com/article/ransomware-victims-thought-their-backups-were-safe-they-were-wrong/
- description: TheDFIRReport. (2022, March 1). Disabling notifications on Synology servers before ransom. Retrieved September
    12, 2024.
  source_name: disable_notif_synology_ransom
  url: https://x.com/TheDFIRReport/status/1498657590259109894
id: attack-pattern--f5d8eed6-48a9-4cdf-a3d7-d1ffa99c3d2a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:49:37.297Z'
name: Inhibit System Recovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Yonatan Gotlib, Deep Instinct
- Austin Clark, @c2defense
- Pallavi Sivakumaran, WithSecure
- Joey Lei
- Harjot Shah Singh
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.6'
```
