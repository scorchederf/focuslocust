---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ss

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ss` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ss` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ss](../../tools/linux/ss.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ss |
| name | ss |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ss/ |

## Preserved Source Material

```yaml
_body: ''
_name: ss
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ss
functions:
  file-read:
  - binary: false
    code: ss -a -F /path/to/input-file
    comment: The file content is actually parsed so only a part of the first line is returned as a part of an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
