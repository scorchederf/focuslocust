---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pwsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pwsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pwsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pwsh](../../tools/linux/pwsh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pwsh |
| name | pwsh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pwsh/ |

## Preserved Source Material

```yaml
_body: ''
_name: pwsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pwsh
functions:
  file-write:
  - code: pwsh -c '"DATA" | Out-File /path/to/output-file'
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: pwsh
    contexts:
      sudo: null
      unprivileged: null
```
