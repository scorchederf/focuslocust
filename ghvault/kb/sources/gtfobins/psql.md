---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# psql

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `psql` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/psql` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [psql](../../tools/linux/psql.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | psql |
| name | psql |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/psql/ |

## Preserved Source Material

```yaml
_body: ''
_name: psql
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/psql
comment: A valid PostgreSQL server must be available to connect to.
functions:
  inherit:
  - code: 'psql

      \?'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
  shell:
  - code: 'psql

      \! /bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
