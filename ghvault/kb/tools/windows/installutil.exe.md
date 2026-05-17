---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Installutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `installutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The Installer tool is a command-line utility that allows you to install and uninstall server resources by executing the installer components in specified assemblies

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/installutil.md)
- Source verification: [source record](../../sources/lolbas/installutil.exe.md)

## Aliases

- `Installutil.exe`
- `installutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: InstallUtil.exe {REMOTEURL} |
| [T1218.004 - InstallUtil](../../attack/techniques/T1218.004-installutil.md) | explicit | source | Command metadata lists T1218.004: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/installutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/installutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@C_h4ck_0'
Person: Nir Chako (Pentera)
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
```
