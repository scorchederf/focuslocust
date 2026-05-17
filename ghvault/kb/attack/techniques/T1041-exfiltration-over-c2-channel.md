---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1041 - Exfiltration Over C2 Channel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1041` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can send data gathered from a target through the command and control channel.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has uploaded a file containing debugger logs, network information and system information to the C2.(Citation: QiAnXin APT-C-36 Feb2019) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can upload files and information from a compromised host to its C2 servers.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.(Citation: GitHub Pupy) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can transfer files from an infected host to the C2 server.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) sent generated reports to the C2 via HTTP POST requests.(Citation: FOX-IT May 2016 Mofang) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can exfiltrate files from the victim using the <code>download</code> command.(Citation: GitHub Sliver Download) |

## Source Verification

[source record](../../sources/mitre/exfiltration-over-c2-channel.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:41.804Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded
into the normal communications channel using the same protocol as command and control communications.
external_references:
- external_id: T1041
source_name: mitre-attack
url: https://attack.mitre.org/techniques/T1041
```
