---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1124 - System Time Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1124` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or <code>systemsetup</code> on macOS. These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.

System time information may be gathered in a number of ways, such as with Net on Windows by performing <code>net time \\hostname</code> to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using <code>w32tm /tz</code>. In addition, adversaries can discover device uptime through functions such as <code>GetTickCount()</code> to determine how long it has been since the system booted up.

On network devices, Network Device CLI commands such as `show clock detail` can be used to see the current time configuration. On ESXi servers, `esxcli system clock get` can be used for the same purpose.

In addition, system calls – such as <code>time()</code> – have been used to collect the current time on Linux devices. On macOS systems, adversaries may use commands such as <code>systemsetup -gettimezone</code> or <code>timeIntervalSinceNow</code> to gather current time zone information or current date and time.

This information could be useful for performing other techniques, such as executing a file with a Scheduled Task/Job, or to discover locality information based on time zone to assist in victim targeting (i.e. System Location Discovery). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check whether the current system hour and day of the week are within operating hours defined it its configuration.(Citation: ESET MirrorFace 2025) |
| [Net](../../tools/unknown/net.md) | explicit | source | The <code>net time</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to determine the local or remote system time.(Citation: TechNet Net Time) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect start time information from a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/system-time-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:37.450Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may gather the system time and/or time zone settings from a local or remote system. The system
time is set and stored by services, such as the Windows Time Service on Windows or <code>systemsetup</code> on macOS.(Citation:
MSDN System Time)(Citation: Technet Windows Time Service)(Citation: systemsetup mac time) These time settings may also be
synchronized between systems and services in an enterprise network, typically accomplished with a network time server within
a domain.(Citation: Mac Time Sync)(Citation: linux system time)
System time information may be gathered in a number of ways, such as with [Net](https://attack.mitre.org/software/S0039)
```
