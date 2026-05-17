---
parsed_by: focuslocust
source: mitre
type: generated
---
# ConnectWise

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0591` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ConnectWise is a legitimate remote administration tool that has been used since at least 2016 by threat actors including MuddyWater and GOLD SOUTHFIELD to connect to and conduct lateral movement in target environments.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/connectwise.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [ConnectWise](https://attack.mitre.org/software/S0591) can be used to execute PowerShell commands on target machines.(Citation: Anomali Static Kitten February 2021) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [ConnectWise](https://attack.mitre.org/software/S0591) can take screenshots on remote hosts.(Citation: Anomali Static Kitten February 2021) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [ConnectWise](https://attack.mitre.org/software/S0591) can record video on remote hosts.(Citation: Anomali Static Kitten February 2021) |

## Source Verification

[source record](../../sources/mitre/connectwise.md)

## Evidence Excerpt

```text
created: '2021-03-18T13:39:27.676Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been
used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115)
to connect to and conduct lateral movement in target environments.(Citation: Anomali Static Kitten February 2021)(Citation:
Trend Micro Muddy Water March 2021)'
external_references:
- external_id: S0591
```
