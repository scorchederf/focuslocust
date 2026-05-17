---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dotnet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dotnet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dotnet` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dotnet covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dotnet.md)
- Source verification: [source record](../../sources/gtfobins/dotnet.md)

## Aliases

- `dotnet`

## Source Verification

[source record](../../sources/gtfobins/dotnet.md)

## Evidence Excerpt

```text
_body: ''
_name: dotnet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dotnet
functions:
file-read:
- code: 'dotnet fsi
System.IO.File.ReadAllText("/path/to/input-file");;'
contexts:
```
