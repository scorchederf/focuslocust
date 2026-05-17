---
parsed_by: focuslocust
source: mitre
type: generated
---
# Runtime Data Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1565.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Runtime Data Manipulation](../../attack/techniques/T1565.003-runtime-data-manipulation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1565.003 |
| name | Runtime Data Manipulation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1565/003 |

## Preserved Source Material

```yaml
created: '2020-03-02T14:30:05.252Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user,
  thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating
  runtime data, adversaries may attempt to affect a business process, organizational understanding, and decision making.


  Adversaries may alter application binaries used to display data in order to cause runtime manipulations. Adversaries may
  also conduct [Change Default File Association](https://attack.mitre.org/techniques/T1546/001) and [Masquerading](https://attack.mitre.org/techniques/T1036)
  to cause a similar effect. The type of modification and the impact it will have depends on the target application and process
  as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise
  and possibly access to specialized software related to the system that would typically be gained through a prolonged information
  gathering campaign in order to have the desired impact.'
external_references:
- external_id: T1565.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1565/003
- description: Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK.
    Retrieved March 29, 2019.
  source_name: DOJ Lazarus Sony 2018
  url: https://www.justice.gov/opa/press-release/file/1092091/download
- description: 'FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.'
  source_name: FireEye APT38 Oct 2018
  url: https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf
id: attack-pattern--32ad5c86-2bcf-47d8-8fdc-d7f3d79a7490
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-11-13T19:21:05.132Z'
name: Runtime Data Manipulation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Integrity
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
