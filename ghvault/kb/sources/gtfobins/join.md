---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# join

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `join` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/join` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [join](../../tools/linux/join.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | join |
| name | join |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/join/ |

## Preserved Source Material

```yaml
_body: ''
_name: join
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/join
functions:
  file-read:
  - binary: false
    code: join -a 2 /dev/null /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
