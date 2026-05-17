---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over Unencrypted Non-C2 Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1048.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over Unencrypted Non-C2 Protocol](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1048.003 |
| name | Exfiltration Over Unencrypted Non-C2 Protocol |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1048/003 |

## Preserved Source Material

```yaml
created: '2020-03-15T15:37:47.583Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing
  command and control channel. The data may also be sent to an alternate network location from the main command and control
  server.(Citation: copy_cmd_cisco)


  Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted
  (such as HTTP, FTP, or DNS). This may include custom or publicly available encoding/compression algorithms (such as base64)
  as well as embedding data within protocol headers and fields. '
external_references:
- external_id: T1048.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1048/003
- description: Cisco. (2022, August 16). copy - Cisco IOS Configuration Fundamentals Command Reference . Retrieved July 13,
    2022.
  source_name: copy_cmd_cisco
  url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/C_commands.html#wp1068167689
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--fb8d023d-45be-47e9-bc51-f56bcae6435b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:39.079Z'
name: Exfiltration Over Unencrypted Non-C2 Protocol
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- William Cain
- Austin Clark, @c2defense
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
x_mitre_version: '2.2'
```
