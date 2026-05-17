---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cpulimit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cpulimit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpulimit` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cpulimit](../../tools/linux/cpulimit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cpulimit |
| name | cpulimit |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cpulimit/ |

## Preserved Source Material

```yaml
_body: ''
_name: cpulimit
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpulimit
functions:
  shell:
  - code: cpulimit -l 100 -f -- /bin/sh
    contexts:
      sudo: null
      suid:
        code: cpulimit -l 100 -f -- /bin/sh -p
      unprivileged: null
```
