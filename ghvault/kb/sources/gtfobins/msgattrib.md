---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgattrib

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgattrib` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgattrib` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msgattrib](../../tools/linux/msgattrib.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msgattrib |
| name | msgattrib |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msgattrib/ |

## Preserved Source Material

```yaml
_body: ''
_name: msgattrib
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgattrib
functions:
  file-read:
  - binary: false
    code: msgattrib -P /path/to/input-file
    comment: The file is parsed and displayed as a Java `.properties` file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
