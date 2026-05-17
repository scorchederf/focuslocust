---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dd](../../tools/linux/dd.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dd |
| name | dd |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dd/ |

## Preserved Source Material

```yaml
_body: ''
_name: dd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dd
functions:
  file-read:
  - code: dd if=/path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: echo DATA | dd of=/path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
