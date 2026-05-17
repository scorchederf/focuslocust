---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tcsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tcsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tcsh](../../tools/linux/tcsh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tcsh |
| name | tcsh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tcsh/ |

## Preserved Source Material

```yaml
_body: ''
_name: tcsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcsh
functions:
  file-write:
  - code: tcsh -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid:
        code: tcsh -bc 'echo DATA >/path/to/output-file'
      unprivileged: null
  shell:
  - code: tcsh
    contexts:
      sudo: null
      suid:
        code: tcsh -b
      unprivileged: null
```
