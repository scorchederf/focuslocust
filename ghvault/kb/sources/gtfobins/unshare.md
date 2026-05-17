---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unshare

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unshare` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unshare` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [unshare](../../tools/linux/unshare.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | unshare |
| name | unshare |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/unshare/ |

## Preserved Source Material

```yaml
_body: ''
_name: unshare
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unshare
functions:
  shell:
  - code: unshare /bin/sh
    contexts:
      sudo: null
      suid:
        code: unshare -r /bin/sh
      unprivileged: null
```
