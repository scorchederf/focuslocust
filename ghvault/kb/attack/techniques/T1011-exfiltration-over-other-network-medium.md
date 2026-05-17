---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1011 - Exfiltration Over Other Network Medium

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1011` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Source Verification

[source record](../../sources/mitre/exfiltration-over-other-network-medium.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:25.159Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel.
If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi
connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.
Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or
defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.'
external_references:
```
