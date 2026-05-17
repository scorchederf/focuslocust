---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dotnet.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dotnet.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

dotnet.exe comes with .NET Framework

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dotnet.md)
- Source verification: [source record](../../sources/lolbas/dotnet.exe.md)

## Aliases

- `Dotnet.exe`
- `dotnet.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1059 - Command and Scripting Interpreter](../../attack/techniques/T1059-command-and-scripting-interpreter.md) | explicit | source | Command metadata lists T1059: dotnet.exe fsi |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: dotnet.exe msbuild {PATH:.csproj} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dotnet.exe.md)

## Source Verification

[source record](../../sources/lolbas/dotnet.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@_felamos'
Person: felamos
- Handle: '@bohops'
Person: Jimmy
- Handle: '@mavinject'
Person: yamalon
Author: felamos
```
