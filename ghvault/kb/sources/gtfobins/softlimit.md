---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# softlimit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `softlimit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/softlimit` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [softlimit](../../tools/linux/softlimit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | softlimit |
| name | softlimit |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/softlimit/ |

## Preserved Source Material

```yaml
_body: ''
_name: softlimit
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/softlimit
functions:
  shell:
  - code: softlimit /bin/sh
    contexts:
      sudo: null
      suid:
        code: softlimit /bin/sh -p
        shell: false
      unprivileged: null
```
