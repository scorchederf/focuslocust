---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1495 - Firmware Corruption

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1495` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system. Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable. Depending on the device, this attack may also result in Data Destruction.

## Source Verification

[source record](../../sources/mitre/firmware-corruption.md)

## Evidence Excerpt

```text
created: '2019-04-12T18:28:15.451Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached
to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or
the system.(Citation: Symantec Chernobyl W95.CIH) Firmware is software that is loaded and executed from non-volatile memory
on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard
drive, or video cards.
In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices.
```
