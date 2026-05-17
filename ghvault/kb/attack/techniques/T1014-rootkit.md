---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1014 - Rootkit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information.  

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or System Firmware.  Rootkits have been seen for Windows, Linux, and Mac OS X systems.  

Rootkits that reside or modify boot sectors are known as Bootkits and specifically target the boot process of the operating system.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [HTRAN](../../tools/unknown/htran.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can install a rootkit to hide network connections from the host OS.(Citation: NCSC Joint Report Public Tools) |

## Source Verification

[source record](../../sources/mitre/rootkit.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:26.496Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers,\
\ and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying\
\ operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) \n\nRootkits or rootkit\
\ enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor\
\ or [System Firmware](https://attack.mitre.org/techniques/T1542/001). (Citation: Wikipedia Rootkit) Rootkits have been\
\ seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)\n\
```
