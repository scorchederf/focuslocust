---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1561 - Disk Wipe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1561` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts, OS Credential Dumping, and SMB/Windows Admin Shares.

On network devices, adversaries may wipe configuration files and other data from the device using Network Device CLI commands such as `erase`.

## Source Verification

[source record](../../sources/mitre/disk-wipe.md)

## Evidence Excerpt

```text
created: '2020-02-20T22:02:20.372Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt
availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions
of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot
record (MBR). A complete wipe of all disk sectors may be attempted.
To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware
used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like
```
