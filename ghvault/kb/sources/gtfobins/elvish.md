---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# elvish

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `elvish` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/elvish` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [elvish](../../tools/linux/elvish.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | elvish |
| name | elvish |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/elvish/ |

## Preserved Source Material

```yaml
_body: ''
_name: elvish
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/elvish
functions:
  file-read:
  - code: elvish -c 'print (slurp </path/to/input-file)'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: elvish -c 'print DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: elvish
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
