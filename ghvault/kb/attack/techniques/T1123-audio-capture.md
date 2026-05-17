---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1123 - Audio Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1123` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote microphone monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-MicrophoneAudio</code> Exfiltration module can record system microphone audio.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can record sound with the microphone.(Citation: GitHub Pupy) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can capture data from the system’s microphone.(Citation: Fortinet Remcos Feb 2017)(Citation: Fortinet Remcos Campaign NOV 2024) |

## Source Verification

[source record](../../sources/mitre/audio-capture.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:34.528Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary can leverage a computer''s peripheral devices (e.g., microphones and webcams) or applications (e.g.,
voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to
gather information.(Citation: ESET Attor Oct 2019)
Malware or scripts may be used to interact with the devices through an available API provided by the operating system or
an application to capture audio. Audio files may be written to disk and exfiltrated later.'
external_references:
```
