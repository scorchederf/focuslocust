---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tac

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tac` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tac` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tac](../../tools/linux/tac.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tac |
| name | tac |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tac/ |

## Preserved Source Material

```yaml
_body: ''
_name: tac
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tac
functions:
  file-read:
  - binary: false
    code: tac -s 'RANDOM' /path/to/input-file
    comment: Make sure that `RANDOM` does not appear into the file to read otherwise the content of the file is corrupted
      by reversing the order of `RANDOM`-separated chunks.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
