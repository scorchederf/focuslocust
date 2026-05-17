---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1125 - Video Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1125` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from Screen Capture due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can record screen content on targeted systems.(Citation: AsyncRAT GitHub) |
| [ConnectWise](../../tools/unknown/connectwise.md) | explicit | source | [ConnectWise](https://attack.mitre.org/software/S0591) can record video on remote hosts.(Citation: Anomali Static Kitten February 2021) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can capture webcam data on Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote webcam monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can capture camera video as part of its collection process.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can access a connected webcam and capture pictures.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can perform webcam viewing.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [Quick Assist](../../tools/unknown/quick-assist.md) | explicit | source | [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to view the interactive session of the running machine, including full screen activity.(Citation: Microsoft Quick Assist 2024)(Citation: Microsoft Storm-1811 2024) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can access a system’s webcam and take pictures.(Citation: Fortinet Remcos Feb 2017) |

## Source Verification

[source record](../../sources/mitre/video-capture.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:37.917Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary can leverage a computer''s peripheral devices (e.g., integrated cameras or webcams) or applications
(e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured
from devices or applications, potentially in specified intervals, in lieu of video files.
Malware or scripts may be used to interact with the devices through an available API provided by the operating system or
an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique
differs from [Screen Capture](https://attack.mitre.org/techniques/T1113) due to use of specific devices or applications
```
