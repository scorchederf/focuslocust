---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bconsole

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bconsole` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bconsole` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bconsole](../../tools/linux/bconsole.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bconsole |
| name | bconsole |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bconsole/ |

## Preserved Source Material

```yaml
_body: ''
_name: bconsole
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bconsole
functions:
  file-read:
  - code: bconsole -c /path/to/file-input
    comment: The file is actually parsed and the first wrong line is returned in an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'bconsole

      @exec /bin/sh'
    contexts:
      sudo: null
      unprivileged: null
```
