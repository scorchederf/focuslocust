---
parsed_by: focuslocust
source: mitre
type: generated
---
# RemoteUtilities

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0592` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

RemoteUtilities is a legitimate remote administration tool that has been used by MuddyWater since at least 2021 for execution on target machines.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/remoteutilities.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can enumerate files and directories on a target machine.(Citation: Trend Micro Muddy Water March 2021) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can upload and download files to and from a target machine.(Citation: Trend Micro Muddy Water March 2021) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can take screenshots on a compromised host.(Citation: Trend Micro Muddy Water March 2021) |
| [T1218.007 - Msiexec](../../attack/techniques/T1218.007-msiexec.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can use Msiexec to install a service.(Citation: Trend Micro Muddy Water March 2021) |

## Source Verification

[source record](../../sources/mitre/remoteutilities.md)

## Evidence Excerpt

```text
created: '2021-03-18T14:57:34.628Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[RemoteUtilities](https://attack.mitre.org/software/S0592) is a legitimate remote administration tool that has
been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021 for execution on target machines.(Citation:
Trend Micro Muddy Water March 2021)'
external_references:
- external_id: S0592
source_name: mitre-attack
```
