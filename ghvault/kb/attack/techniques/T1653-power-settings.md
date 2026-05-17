---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1653 - Power Settings

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1653` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity.

Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering a state, such as standby, that can terminate malicious activity.

For example, `powercfg` controls all configurable power system settings on a Windows system and can be abused to prevent an infected host from locking or shutting down. Adversaries may also extend system lock screen timeout settings. Other relevant settings, such as disk and hibernate timeout, can be similarly abused to keep the infected machine running even if no user is active.

Aware that some malware cannot survive system reboots, adversaries may entirely delete files used to invoke system shut down or reboot.

## Source Verification

[source record](../../sources/mitre/power-settings.md)

## Evidence Excerpt

```text
created: '2023-06-05T15:52:52.467Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may impair a system''s ability to hibernate, reboot, or shut down in order to extend access to infected
machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt
malicious activity.(Citation: Sleep, shut down, hibernate)
Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering
a state, such as standby, that can terminate malicious activity.(Citation: Microsoft: Powercfg command-line options)(Citation:
systemdsleep Linux)
```
