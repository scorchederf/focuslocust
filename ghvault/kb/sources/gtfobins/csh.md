---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [csh](../../tools/linux/csh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | csh |
| name | csh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/csh/ |

## Preserved Source Material

```yaml
_body: ''
_name: csh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csh
functions:
  file-write:
  - code: csh -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid:
        code: csh -c 'echo DATA >/path/to/output-file' -b
      unprivileged: null
  shell:
  - code: csh
    contexts:
      sudo: null
      suid:
        code: csh -b
      unprivileged: null
```
