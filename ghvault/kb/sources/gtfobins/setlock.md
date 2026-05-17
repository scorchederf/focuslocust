---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setlock

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setlock` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setlock` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [setlock](../../tools/linux/setlock.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setlock |
| name | setlock |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/setlock/ |

## Preserved Source Material

```yaml
_body: ''
_name: setlock
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setlock
functions:
  shell:
  - code: setlock - /bin/sh
    contexts:
      sudo: null
      suid:
        code: setlock - /bin/sh -p
        shell: true
      unprivileged: null
```
