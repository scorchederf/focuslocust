---
parsed_by: focuslocust
source: mitre
type: generated
---
# Quick Assist

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1209` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Quick Assist is a remote assistance tool primarily for Microsoft Windows, although a macOS version also exists. Quick Assist allows for remote screen sharing and, with end user approval, remote control and command execution on the enabling device.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/quick-assist.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Quick Assist](https://attack.mitre.org/software/S1209) communicates over TCP 443 via HTTPS to a remote session server, under which RDP traffic is transferred.(Citation: Microsoft Quick Assist 2024) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to take screenshots of the running system.(Citation: Microsoft Quick Assist 2024) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to view the interactive session of the running machine, including full screen activity.(Citation: Microsoft Quick Assist 2024)(Citation: Microsoft Storm-1811 2024) |

## Source Verification

[source record](../../sources/mitre/quick-assist.md)

## Evidence Excerpt

```text
created: '2025-03-14T19:13:01.957Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Quick Assist](https://attack.mitre.org/software/S1209) is a remote assistance tool primarily for Microsoft
Windows, although a macOS version also exists. [Quick Assist](https://attack.mitre.org/software/S1209) allows for remote
screen sharing and, with end user approval, remote control and command execution on the enabling device.(Citation: Microsoft
Storm-1811 2024)(Citation: Microsoft Quick Assist 2024)'
external_references:
- external_id: S1209
```
