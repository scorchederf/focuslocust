---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dash](../../tools/linux/dash.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dash |
| name | dash |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dash/ |

## Preserved Source Material

```yaml
_body: ''
_name: dash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dash
functions:
  file-write:
  - code: dash -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: dash
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
