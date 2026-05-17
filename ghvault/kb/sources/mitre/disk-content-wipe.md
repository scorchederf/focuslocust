---
parsed_by: focuslocust
source: mitre
type: generated
---
# Disk Content Wipe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1561.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disk Content Wipe](../../attack/techniques/T1561.001-disk-content-wipe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1561.001 |
| name | Disk Content Wipe |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1561/001 |

## Preserved Source Material

```yaml
created: '2020-02-20T22:06:41.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to
  interrupt availability to system and network resources.


  Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through
  the storage interface.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware)(Citation: DOJ Lazarus
  Sony 2018) Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions
  of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily
  sized portions of disk with random data.(Citation: Novetta Blockbuster Destructive Malware) Adversaries have also been observed
  leveraging third-party drivers like [RawDisk](https://attack.mitre.org/software/S0364) to directly access disk content.(Citation:
  Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware) This behavior is distinct from [Data Destruction](https://attack.mitre.org/techniques/T1485)
  because sections of the disk are erased instead of individual files.


  To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware
  used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques
  like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003),
  and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive
  Malware)'
external_references:
- external_id: T1561.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1561/001
- description: Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK.
    Retrieved March 29, 2019.
  source_name: DOJ Lazarus Sony 2018
  url: https://www.justice.gov/opa/press-release/file/1092091/download
- description: 'Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved
    November 17, 2024.'
  source_name: Novetta Blockbuster Destructive Malware
  url: https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf
- description: 'Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the
    Sony Attack. Retrieved February 25, 2016.'
  source_name: Novetta Blockbuster
  url: https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf
- description: Russinovich, M. & Garnier, T. (2017, May 22). Sysmon v6.20. Retrieved December 13, 2017.
  source_name: Microsoft Sysmon v6 May 2017
  url: https://docs.microsoft.com/sysinternals/downloads/sysmon
id: attack-pattern--fb640c43-aa6b-431e-a961-a279010424ac
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:49:38.983Z'
name: Disk Content Wipe
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.2'
```
