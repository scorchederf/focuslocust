---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# atobm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `atobm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/atobm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [atobm](../../tools/linux/atobm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | atobm |
| name | atobm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/atobm/ |

## Preserved Source Material

```yaml
_body: ''
_name: atobm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/atobm
functions:
  file-read:
  - code: atobm /path/to/input-file
    comment: Outputs only the first line of the file to standard error without the `-` and `#` characters, this can be customized
      with the `-c` option, by default is `-c -#`. Content can be retrieved with `awk -F "'" '{printf "%s", $2}'`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
