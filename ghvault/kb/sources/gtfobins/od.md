---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# od

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `od` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/od` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [od](../../tools/linux/od.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | od |
| name | od |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/od/ |

## Preserved Source Material

```yaml
_body: ''
_name: od
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/od
functions:
  file-read:
  - code: od -An -c -w999 /path/to/input-file
    comment: Three spaces are added before each character in the read file (wrapped at the specified value, i.e., `999`),
      and non-printable chars are printed as backslash escape sequences.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
