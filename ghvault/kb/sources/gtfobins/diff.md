---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# diff

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `diff` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/diff` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [diff](../../tools/linux/diff.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | diff |
| name | diff |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/diff/ |

## Preserved Source Material

```yaml
_body: ''
_name: diff
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/diff
functions:
  file-read:
  - binary: false
    code: diff --line-format=%L /dev/null /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: diff --recursive /path/to/empty-dir /path/to/input-dir/
    comment: This lists the content of a directory. `/path/to/empty-dir` can be any directory, but for convenience it is better
      to use an empty directory to avoid noise output.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
