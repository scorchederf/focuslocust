---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pg](../../tools/linux/pg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pg |
| name | pg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pg/ |

## Preserved Source Material

```yaml
_body: ''
_name: pg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pg
functions:
  file-read:
  - code: pg /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'pg /etc/hosts

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
