---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pic](../../tools/linux/pic.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pic |
| name | pic |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pic/ |

## Preserved Source Material

```yaml
_body: ''
_name: pic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pic
functions:
  file-read:
  - binary: false
    code: pic /path/to/input-file
    comment: The output is prefixed with some content.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'pic -U

      .PS

      sh X sh X'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
