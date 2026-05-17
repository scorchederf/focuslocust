---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmdb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmdb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmdb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rpmdb](../../tools/linux/rpmdb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rpmdb |
| name | rpmdb |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rpmdb/ |

## Preserved Source Material

```yaml
_body: ''
_name: rpmdb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmdb
functions:
  inherit:
  - code: rpmdb --eval '%{lua:...}'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
    version: Some older version is required.
  shell:
  - code: rpmdb --eval '%(/bin/sh 1>&2)'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
