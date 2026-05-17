---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1006 - Direct Volume Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. 

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell. Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and esentutl) to create shadow copies or backups of data from system volumes.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [esentutl](../../tools/unknown/esentutl.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.(Citation: LOLBAS Esentutl)(Citation: Cary Esentutl) |

## Source Verification

[source record](../../sources/mitre/direct-volume-access.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:20.934Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows
allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly
from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well
as file system monitoring tools. (Citation: Hakobyan 2009)
Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries
may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [esentutl](https://attack.mitre.org/software/S0404))
```
