---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# guile

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `guile` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/guile` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [guile](../../tools/linux/guile.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | guile |
| name | guile |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/guile/ |

## Preserved Source Material

```yaml
_body: ''
_name: guile
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/guile
functions:
  shell:
  - code: guile -c '(system "/bin/sh")'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
