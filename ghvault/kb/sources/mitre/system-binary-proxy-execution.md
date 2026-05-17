---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Binary Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218 |
| name | System Binary Proxy Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with
  signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that
  they have been either downloaded from Microsoft or are already native in the operating system.(Citation: LOLBAS Project)
  Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature
  validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of
  other files or commands.


  Similarly, on Linux systems adversaries may abuse trusted binaries such as <code>split</code> to proxy execution of malicious
  commands.(Citation: split man page)(Citation: GTFO split)'
external_references:
- external_id: T1218
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218
- description: GTFOBins. (2020, November 13). split. Retrieved April 18, 2022.
  source_name: GTFO split
  url: https://gtfobins.github.io/gtfobins/split/
- description: Oddvar Moe et al. (2022, February).  Living Off The Land Binaries, Scripts and Libraries. Retrieved March 7,
    2022.
  source_name: LOLBAS Project
  url: https://github.com/LOLBAS-Project/LOLBAS#criteria
- description: Torbjorn Granlund, Richard M. Stallman. (2020, March null). split(1) — Linux manual page. Retrieved March 25,
    2022.
  source_name: split man page
  url: https://man7.org/linux/man-pages/man1/split.1.html
id: attack-pattern--457c7820-d331-465a-915e-42f85500ccc4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:37:10.607Z'
name: System Binary Proxy Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Hans Christoffer Gaardløs
- Nishan Maharjan, @loki248
- Praetorian
- Wes Hurd
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '4.0'
```
