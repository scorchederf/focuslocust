---
parsed_by: focuslocust
source: mitre
type: generated
---
# Bind Mounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.013` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bind Mounts](../../attack/techniques/T1564.013-bind-mounts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.013 |
| name | Bind Mounts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/013 |

## Preserved Source Material

```yaml
created: '2025-01-30T21:01:16.340Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse bind mounts on file structures to hide their activity and artifacts from native utilities.\
  \ A bind mount maps a directory or file from one location on the filesystem to another, similar to a shortcut on Windows.\
  \ It’s commonly used to provide access to specific files or directories across different environments, such as inside containers\
  \ or chroot environments, and requires sudo access. \n\nAdversaries may use bind mounts to map either an empty directory\
  \ or a benign `/proc` directory to a malicious process’s `/proc` directory. Using the commands `mount –o bind /proc/benign-process\
  \ /proc/malicious-process` (or `mount –B`), the malicious process's `/proc` directory is overlayed with the contents of\
  \ a benign process's `/proc` directory. When system utilities query process activity, such as `ps` and `top`, the kernel\
  \ follows the bind mount and presents the benign directory’s contents instead of the malicious process's actual `/proc`\
  \ directory. As a result, these utilities display information that appears to come from the benign process, effectively\
  \ hiding the malicious process's metadata, executable, or other artifacts from detection.(Citation: Cado Security Commando\
  \ Cat 2024)(Citation: Ahn Lab CoinMiner 2023)"
external_references:
- external_id: T1564.013
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/013
- description: Ahn Lab. (2023, April 24). CoinMiner (KONO DIO DA) Distributed to Linux SSH Servers. Retrieved April 4, 2025.
  source_name: Ahn Lab CoinMiner 2023
  url: https://asec.ahnlab.com/en/51908/
- description: 'Nate Bill & Matt Muir. (2024, February 1). The Nine Lives of Commando Cat: Analysing a Novel Malware Campaign
    Targeting Docker. Retrieved April 4, 2025.'
  source_name: Cado Security Commando Cat 2024
  url: https://www.cadosecurity.com/blog/the-nine-lives-of-commando-cat-analysing-a-novel-malware-campaign-targeting-docker
id: attack-pattern--5bd41255-a224-4425-a2e2-e9d293eafe1c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:17:48.263Z'
name: Bind Mounts
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Lê Phương Nam, Group-IB
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
x_mitre_version: '2.0'
```
