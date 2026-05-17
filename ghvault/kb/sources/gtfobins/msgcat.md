---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msgcat](../../tools/linux/msgcat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msgcat |
| name | msgcat |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msgcat/ |

## Preserved Source Material

```yaml
_body: ''
_name: msgcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgcat
functions:
  file-read:
  - binary: false
    code: msgcat -P /path/to/input-file
    comment: The file is parsed and displayed as a Java `.properties` file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
