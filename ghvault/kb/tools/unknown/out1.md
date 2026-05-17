---
parsed_by: focuslocust
source: mitre
type: generated
---
# Out1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0594` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Out1 is a remote access tool written in python and used by MuddyWater since at least 2021.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/out1.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) can copy files and Registry data from compromised hosts.(Citation: Trend Micro Muddy Water March 2021) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) has the ability to encode data.(Citation: Trend Micro Muddy Water March 2021) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) can use native command line for execution.(Citation: Trend Micro Muddy Water March 2021) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) can use HTTP and HTTPS in communications with remote hosts.(Citation: Trend Micro Muddy Water March 2021) |
| [T1114.001 - Local Email Collection](../../attack/techniques/T1114.001-local-email-collection.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) can parse e-mails on a target machine.(Citation: Trend Micro Muddy Water March 2021) |

## Source Verification

[source record](../../sources/mitre/out1.md)

## Evidence Excerpt

```text
created: '2021-03-19T13:11:50.666Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Out1](https://attack.mitre.org/software/S0594) is a remote access tool written in python and used by [MuddyWater](https://attack.mitre.org/groups/G0069)
since at least 2021.(Citation: Trend Micro Muddy Water March 2021)'
external_references:
- external_id: S0594
source_name: mitre-attack
url: https://attack.mitre.org/software/S0594
```
