---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nsenter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nsenter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nsenter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nsenter](../../tools/linux/nsenter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nsenter |
| name | nsenter |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nsenter/ |

## Preserved Source Material

```yaml
_body: ''
_name: nsenter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nsenter
functions:
  shell:
  - code: nsenter /bin/sh
    comment: The shell command can be omitted.
    contexts:
      sudo: null
      suid:
        code: nsenter /bin/sh -p
        shell: false
      unprivileged: null
```
