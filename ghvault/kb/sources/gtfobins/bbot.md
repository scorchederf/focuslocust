---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bbot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bbot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bbot` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bbot](../../tools/linux/bbot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bbot |
| name | bbot |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bbot/ |

## Preserved Source Material

```yaml
_body: ''
_name: bbot
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bbot
functions:
  file-read:
  - binary: false
    code: bbot -d -cy /path/to/input-file
    comment: The file is displayed in the debug log.
    contexts:
      sudo: null
      unprivileged: null
```
