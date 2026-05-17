---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msguniq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msguniq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msguniq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msguniq](../../tools/linux/msguniq.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msguniq |
| name | msguniq |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msguniq/ |

## Preserved Source Material

```yaml
_body: ''
_name: msguniq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msguniq
functions:
  file-read:
  - binary: false
    code: msguniq -P /path/to/input-file
    comment: The file is parsed and displayed as a Java `.properties` file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
