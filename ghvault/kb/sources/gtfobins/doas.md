---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# doas

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `doas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/doas` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [doas](../../tools/linux/doas.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | doas |
| name | doas |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/doas/ |

## Preserved Source Material

```yaml
_body: ''
_name: doas
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/doas
functions:
  shell:
  - code: doas -u root /bin/sh
    comment: The user must be allowed to use `doas`.
    contexts:
      sudo: null
      unprivileged: null
```
