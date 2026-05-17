---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ptx

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ptx` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ptx` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ptx](../../tools/linux/ptx.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ptx |
| name | ptx |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ptx/ |

## Preserved Source Material

```yaml
_body: ''
_name: ptx
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ptx
comment: While the program is capable of reading the file, it outputs a "permuted index" of its content, thus altering it.
  Adjusting the options could yield more readable outputs.
functions:
  file-read:
  - binary: false
    code: ptx -w 999 /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
