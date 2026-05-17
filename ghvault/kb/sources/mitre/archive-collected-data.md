---
parsed_by: focuslocust
source: mitre
type: generated
---
# Archive Collected Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1560` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Archive Collected Data](../../attack/techniques/T1560-archive-collected-data.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1560 |
| name | Archive Collected Data |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1560 |

## Preserved Source Material

```yaml
created: '2020-02-20T20:53:45.725Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data
  can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment
  Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less
  conspicuous upon inspection by a defender.


  Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library,
  or custom method.'
external_references:
- external_id: T1560
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1560
- description: Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved
    November 17, 2024.
  source_name: DOJ GRU Indictment Jul 2018
  url: https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf
- description: Wikipedia. (2016, March 31). List of file signatures. Retrieved April 22, 2016.
  source_name: Wikipedia File Header Signatures
  url: https://en.wikipedia.org/wiki/List_of_file_signatures
id: attack-pattern--53ac20cd-aca3-406e-9aa0-9fc7fdc60a5a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:48.023Z'
name: Archive Collected Data
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
