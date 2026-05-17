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

## Generated Concept Page

- [dotnet](../../tools/linux/dotnet.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dotnet |
| name | dotnet |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dotnet/ |

## Preserved Source Material

```yaml
_body: ''
_name: dotnet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dotnet
functions:
  file-read:
  - code: 'dotnet fsi

      System.IO.File.ReadAllText("/path/to/input-file");;'
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'dotnet fsi

      System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;'
    contexts:
      sudo: null
      unprivileged: null
```
