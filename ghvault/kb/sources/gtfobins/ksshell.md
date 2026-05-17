---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ksshell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ksshell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ksshell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ksshell](../../tools/linux/ksshell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ksshell |
| name | ksshell |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ksshell/ |

## Preserved Source Material

```yaml
_body: ''
_name: ksshell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ksshell
functions:
  file-read:
  - code: ksshell -i /path/to/input-file
    comment: Each line is corrupted by a prefix string. Also consider that lines are actually parsed as `kickstart` scripts
      thus some file contents may lead to unexpected results.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
