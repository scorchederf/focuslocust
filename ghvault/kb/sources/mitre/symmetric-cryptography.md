---
parsed_by: focuslocust
source: mitre
type: generated
---
# Symmetric Cryptography

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1573.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Symmetric Cryptography](../../attack/techniques/T1573.001-symmetric-cryptography.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1573.001 |
| name | Symmetric Cryptography |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1573/001 |

## Preserved Source Material

```yaml
created: '2020-03-16T15:45:17.032Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than
  relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key
  for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, DES, 3DES, Blowfish,
  and RC4.
external_references:
- external_id: T1573.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1573/001
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--24bfaeba-cb0d-4525-b3dc-507c77ecec41
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:32.429Z'
name: Symmetric Cryptography
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
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.2'
```
