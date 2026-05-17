---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pidstat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pidstat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pidstat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pidstat](../../tools/linux/pidstat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pidstat |
| name | pidstat |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pidstat/ |

## Preserved Source Material

```yaml
_body: ''
_name: pidstat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pidstat
functions:
  shell:
  - code: pidstat -e /bin/sh
    contexts:
      sudo: null
      suid:
        code: pidstat -e /bin/sh -p
        shell: false
      unprivileged: null
```
