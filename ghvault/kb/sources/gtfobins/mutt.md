---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mutt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mutt` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mutt` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mutt](../../tools/linux/mutt.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mutt |
| name | mutt |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mutt/ |

## Preserved Source Material

```yaml
_body: ''
_name: mutt
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mutt
functions:
  file-read:
  - binary: false
    code: mutt -F /path/to/input-file
    comment: The file is leaked as error messages.
    contexts:
      sudo: null
      unprivileged: null
```
