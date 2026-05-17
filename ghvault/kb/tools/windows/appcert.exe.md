---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppCert.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appcert.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appcert.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows App Certification Kit command-line tool.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/appcert.md)
- Source verification: [source record](../../sources/lolbas/appcert.exe.md)

## Aliases

- `AppCert.exe`
- `appcert.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml} |
| [T1218.007 - Msiexec](../../attack/techniques/T1218.007-msiexec.md) | explicit | source | Command metadata lists T1218.007: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml} |

## Source Verification

[source record](../../sources/lolbas/appcert.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
Description: Execute an executable file via the Windows App Certification Kit command-line tool.
```
