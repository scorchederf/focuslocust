---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pax

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pax` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pax` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pax](../../tools/linux/pax.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pax |
| name | pax |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pax/ |

## Preserved Source Material

```yaml
_body: ''
_name: pax
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pax
functions:
  file-read:
  - code: pax -w /path/to/input-file | tar -xO
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
