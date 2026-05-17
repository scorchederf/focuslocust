---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# last

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `last` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/last` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [last](../../tools/linux/last.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | last |
| name | last |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/last/ |

## Preserved Source Material

```yaml
_body: ''
_name: last
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/last
functions:
  file-read:
  - code: last -a -f /path/to/input-file
    comment: The output might be corrupted or incomplete if the file does not follow the expected database format.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
