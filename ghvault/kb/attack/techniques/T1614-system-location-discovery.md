---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1614 - System Location Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1614` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from System Location Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings. Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host. In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can determine the country a victim host is located in.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can identify the location of targeted devices.(Citation: Fortinet Remcos Campaign NOV 2024) |

## Source Verification

[source record](../../sources/mitre/system-location-discovery.md)

## Evidence Excerpt

```text
created: '2021-04-01T16:42:08.735Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '
Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may
use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery
to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.
Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout,
and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer
```
