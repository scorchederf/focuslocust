---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# hexdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `hexdump` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hexdump` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [hexdump](../../tools/linux/hexdump.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hexdump |
| name | hexdump |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/hexdump/ |

## Preserved Source Material

```yaml
_body: ''
_name: hexdump
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hexdump
functions:
  file-read:
  - code: hd /path/to/input-file
    comment: The output is actually an hex dump.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
