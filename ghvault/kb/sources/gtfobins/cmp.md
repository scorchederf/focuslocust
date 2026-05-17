---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cmp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cmp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cmp](../../tools/linux/cmp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmp |
| name | cmp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cmp/ |

## Preserved Source Material

```yaml
_body: ''
_name: cmp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmp
functions:
  file-read:
  - binary: false
    code: cmp /path/to/input-file /dev/zero -b -l
    comment: Dump the bytes of the input file that are different from the NUL byte in a tabular format.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
