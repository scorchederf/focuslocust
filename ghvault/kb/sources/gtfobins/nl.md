---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nl](../../tools/linux/nl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nl |
| name | nl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nl/ |

## Preserved Source Material

```yaml
_body: ''
_name: nl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nl
functions:
  file-read:
  - binary: false
    code: nl -bn -w1 -s '' /path/to/input-file
    comment: The read file content is corrupted by a leading space added to each line.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
