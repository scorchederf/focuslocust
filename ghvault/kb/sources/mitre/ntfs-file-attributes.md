---
parsed_by: focuslocust
source: mitre
type: generated
---
# NTFS File Attributes

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.004 |
| name | NTFS File Attributes |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/004 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:33:00.009Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New
  Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory
  on the partition. (Citation: SpectorOps Host-Based Jul 2017) Within MFT entries are file attributes, (Citation: Microsoft
  NTFS File Attributes Aug 2010) such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more
  than one Data attribute is present], that can be used to store arbitrary data (and even complete files). (Citation: SpectorOps
  Host-Based Jul 2017) (Citation: Microsoft File Streams) (Citation: MalwareBytes ADS July 2015) (Citation: Microsoft ADS
  Mar 2014)


  Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done
  to evade some defenses, such as static indicator scanning tools and anti-virus. (Citation: Journey into IR ZeroAccess NTFS
  EA) (Citation: MalwareBytes ADS July 2015)'
external_references:
- external_id: T1564.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/004
- description: Arntz, P. (2015, July 22). Introduction to Alternate Data Streams. Retrieved March 21, 2018.
  source_name: MalwareBytes ADS July 2015
  url: https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/
- description: Atkinson, J. (2017, July 18). Host-based Threat Modeling & Indicator Design. Retrieved March 21, 2018.
  source_name: SpectorOps Host-Based Jul 2017
  url: https://posts.specterops.io/host-based-threat-modeling-indicator-design-a9dbbb53d5ea
- description: Harrell, C. (2012, December 11). Extracting ZeroAccess from NTFS Extended Attributes. Retrieved June 3, 2016.
  source_name: Journey into IR ZeroAccess NTFS EA
  url: http://journeyintoir.blogspot.com/2012/12/extracting-zeroaccess-from-ntfs.html
- description: Hughes, J. (2010, August 25). NTFS File Attributes. Retrieved March 21, 2018.
  source_name: Microsoft NTFS File Attributes Aug 2010
  url: https://blogs.technet.microsoft.com/askcore/2010/08/25/ntfs-file-attributes/
- description: Marlin, J. (2013, March 24). Alternate Data Streams in NTFS. Retrieved March 21, 2018.
  source_name: Microsoft ADS Mar 2014
  url: https://blogs.technet.microsoft.com/askcore/2013/03/24/alternate-data-streams-in-ntfs/
- description: Microsoft. (n.d.). File Streams. Retrieved September 12, 2024.
  source_name: Microsoft File Streams
  url: https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams
id: attack-pattern--f2857333-11d4-45bf-b064-2c28d8525be5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:24:50.745Z'
name: NTFS File Attributes
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Oddvar Moe, @oddvarmoe
- Red Canary
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
