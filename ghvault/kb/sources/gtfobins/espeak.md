---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# espeak

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `espeak` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/espeak` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [espeak](../../tools/linux/espeak.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | espeak |
| name | espeak |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/espeak/ |

## Preserved Source Material

```yaml
_body: ''
_name: espeak
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/espeak
functions:
  file-read:
  - binary: false
    code: espeak -qXf /path/to/input-file
    comment: The file content appears in the middle of other textual information as phonemes.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
