---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pdb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pdb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pdb](../../tools/linux/pdb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pdb |
| name | pdb |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pdb/ |

## Preserved Source Material

```yaml
_body: ''
_name: pdb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdb
functions:
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      pdb /path/to/temp-file

      cont'
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: python
```
