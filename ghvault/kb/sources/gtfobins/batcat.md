---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# batcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `batcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/batcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [batcat](../../tools/linux/batcat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | batcat |
| name | batcat |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/batcat/ |

## Preserved Source Material

```yaml
_body: ''
_name: batcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/batcat
functions:
  inherit:
  - code: batcat --paging always /etc/hosts
    comment: '`--paging always` can be omitted provided that the output doesn''t fit the screen.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
```
