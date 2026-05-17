---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# neofetch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `neofetch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [neofetch](../../tools/linux/neofetch.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | neofetch |
| name | neofetch |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/neofetch/ |

## Preserved Source Material

```yaml
_body: ''
_name: neofetch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch
functions:
  file-read:
  - binary: false
    code: neofetch --ascii /path/to/input-file
    comment: The file content is used as the logo while some other information is displayed on its right.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'echo ''exec /bin/sh'' >/path/to/temp-file

      neofetch --config /path/to/temp-file'
    contexts:
      sudo: null
      unprivileged: null
```
