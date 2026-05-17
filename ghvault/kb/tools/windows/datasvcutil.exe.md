---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DataSvcUtil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `datasvcutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/DataSvcUtil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

DataSvcUtil.exe is a command-line tool provided by WCF Data Services that consumes an Open Data Protocol (OData) feed and generates the client data service classes that are needed to access a data service from a .NET Framework client application.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/datasvcutil.md)
- Source verification: [source record](../../sources/lolbas/datasvcutil.exe.md)

## Aliases

- `DataSvcUtil.exe`
- `datasvcutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1567 - Exfiltration Over Web Service](../../attack/techniques/T1567-exfiltration-over-web-service.md) | explicit | source | Command metadata lists T1567: DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/datasvcutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/datasvcutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@NtSetDefault'
Person: Ialle Teixeira
Author: Ialle Teixeira
Code_Sample:
- Code: https://gist.github.com/teixeira0xfffff/837e5bfed0d1b0a29a7cb1e5dbdd9ca6
Commands:
- Category: Upload
```
