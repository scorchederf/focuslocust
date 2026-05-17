---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dstat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dstat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dstat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dstat](../../tools/linux/dstat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dstat |
| name | dstat |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dstat/ |

## Preserved Source Material

```yaml
_body: ''
_name: dstat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dstat
functions:
  inherit:
  - code: dstat --xxx
    comment: '`dstat` allows you to run arbitrary Python scripts loaded as "external plugins" if they are located in one of
      the directories, stated in the `dstat` man page under "FILES":


      - `~/.dstat/`

      - `(path of binary)/plugins/`

      - `/usr/share/dstat/`

      - `/usr/local/share/dstat/`


      Pick the one that you can write into. The plugin named `xxx` file name must be defined in the `dstat_xxx.py` file.'
    contexts:
      sudo: null
      unprivileged: null
    from: python
```
