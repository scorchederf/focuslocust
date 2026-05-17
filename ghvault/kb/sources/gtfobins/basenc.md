---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# basenc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `basenc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/basenc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [basenc](../../tools/linux/basenc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | basenc |
| name | basenc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/basenc/ |

## Preserved Source Material

```yaml
_body: ''
_name: basenc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/basenc
functions:
  file-read:
  - code: basenc --base64 /path/to/input-file | basenc -d --base64
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
