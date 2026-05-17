---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgmerge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgmerge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgmerge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msgmerge](../../tools/linux/msgmerge.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msgmerge |
| name | msgmerge |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msgmerge/ |

## Preserved Source Material

```yaml
_body: ''
_name: msgmerge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgmerge
functions:
  file-read:
  - binary: false
    code: msgmerge -P /path/to/input-file /dev/null
    comment: The file is parsed and displayed as a Java `.properties` file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
