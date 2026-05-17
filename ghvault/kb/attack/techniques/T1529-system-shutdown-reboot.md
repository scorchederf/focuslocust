---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1529 - System Shutdown／Reboot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1529` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via Network Device CLI (e.g. <code>reload</code>). They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot. Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system. In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via Access Token Manipulation).
 In some cases, the system may not be able to boot again. 

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as Disk Structure Wipe or Inhibit System Recovery, to hasten the intended effects on system availability.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can shutdown and restart remote devices.(Citation: Fortinet Remcos Campaign NOV 2024) |

## Source Verification

[source record](../../sources/mitre/system-shutdown-reboot.md)

## Evidence Excerpt

```text
created: '2019-10-04T20:42:28.541Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems.\
\ Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these\
\ commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008)\
\ (e.g. <code>reload</code>).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) They may also include shutdown/reboot\
\ of a virtual machine via hypervisor / cloud consoles or command line tools.\n\nShutting down or rebooting systems may\
\ disrupt access to computer resources for legitimate users while also impeding incident response/recovery.\n\nAdversaries\
```
