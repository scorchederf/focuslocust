---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1113 - Screen Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1113` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>, <code>xwd</code>, or <code>screencapture</code>.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to view the screen on compromised hosts.(Citation: AsyncRAT GitHub) |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can take screenshots on compromised hosts.(Citation: Palo Alto Brute Ratel July 2022) |
| [ConnectWise](../../tools/unknown/connectwise.md) | explicit | source | [ConnectWise](https://attack.mitre.org/software/S0591) can take screenshots on remote hosts.(Citation: Anomali Static Kitten February 2021) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) is capable of capturing screenshots on Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can take screen shots of a compromised machine.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-TimedScreenshot</code> Exfiltration module can take screenshots at regular intervals.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Psr.exe](../../tools/windows/psr.exe.md) | explicit | source | Command metadata lists T1113: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0 |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.(Citation: GitHub Pupy) |
| [Quick Assist](../../tools/unknown/quick-assist.md) | explicit | source | [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to take screenshots of the running system.(Citation: Microsoft Quick Assist 2024) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) takes automated screenshots of the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [RemoteUtilities](../../tools/unknown/remoteutilities.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can take screenshots on a compromised host.(Citation: Trend Micro Muddy Water March 2021) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can take a screenshot of the current desktop.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can take screenshots of the victim’s active display.(Citation: GitHub Sliver Screen) |

## Source Verification

[source record](../../sources/mitre/screen-capture.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:25.060Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation.
Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations.
Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>,
<code>xwd</code>, or <code>screencapture</code>.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)
'
external_references:
```
