---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bridge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bridge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bridge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bridge](../../tools/linux/bridge.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bridge |
| name | bridge |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bridge/ |

## Preserved Source Material

```yaml
_body: ''
_name: bridge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bridge
functions:
  file-read:
  - code: bridge -b /path/to/input-file
    comment: Outputs the first line of the file (until the first whitespace) inside an error message to stdandard error.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
