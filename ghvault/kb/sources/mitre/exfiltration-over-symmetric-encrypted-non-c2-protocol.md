---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over Symmetric Encrypted Non-C2 Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1048.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over Symmetric Encrypted Non-C2 Protocol](../../attack/techniques/T1048.001-exfiltration-over-symmetric-encrypted-non-c2-protocol.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1048.001 |
| name | Exfiltration Over Symmetric Encrypted Non-C2 Protocol |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1048/001 |

## Preserved Source Material

```yaml
created: '2020-03-15T15:30:42.378Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that\
  \ of the existing command and control channel. The data may also be sent to an alternate network location from the main\
  \ command and control server. \n\nSymmetric encryption algorithms are those that use shared or the same keys/secrets on\
  \ each end of the channel. This requires an exchange or pre-arranged agreement/possession of the value used to encrypt and\
  \ decrypt data. \n\nNetwork protocols that use asymmetric encryption often utilize symmetric encryption once keys are exchanged,\
  \ but adversaries may opt to manually share keys and implement symmetric cryptographic algorithms (ex: RC4, AES) vice using\
  \ mechanisms that are baked into a protocol. This may result in multiple layers of encryption (in protocols that are natively\
  \ encrypted such as HTTPS) or encryption in protocols that not typically encrypted (such as HTTP or FTP). "
external_references:
- external_id: T1048.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1048/001
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--79a4052e-1a89-4b09-aea6-51f1d11fe19c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:48:59.332Z'
name: Exfiltration Over Symmetric Encrypted Non-C2 Protocol
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- ESXi
x_mitre_version: '1.1'
```
