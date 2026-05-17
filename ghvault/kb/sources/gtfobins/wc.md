---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wc](../../tools/linux/wc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wc |
| name | wc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/wc/ |

## Preserved Source Material

```yaml
_body: ''
_name: wc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wc
functions:
  file-read:
  - binary: false
    code: wc --files0-from /path/to/input-file
    comment: The file content is parsed as a sequence of `\x00` separated paths. On error the file content appears in a message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
