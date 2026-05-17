---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nice

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nice` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nice` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nice](../../tools/linux/nice.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nice |
| name | nice |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nice/ |

## Preserved Source Material

```yaml
_body: ''
_name: nice
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nice
functions:
  shell:
  - code: nice /bin/sh
    contexts:
      sudo: null
      suid:
        code: nice /bin/sh -p
        shell: false
      unprivileged: null
```
