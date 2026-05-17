---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gcc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gcc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gcc](../../tools/linux/gcc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gcc |
| name | gcc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gcc/ |

## Preserved Source Material

```yaml
_body: ''
_name: gcc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc
functions:
  file-read:
  - binary: false
    code: gcc -x c -E /path/to/input-file
    contexts:
      sudo: null
      unprivileged: null
  - binary: false
    code: gcc @/path/to/input-file
    comment: The file is read and parsed as a list of files (one per line), the content is displayed as error messages.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: gcc -x c /dev/null -o /path/to/input-file
    comment: This actually deletes the file.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: gcc -wrapper /bin/sh,-s x
    comment: In some older versions, the `x` argument must instead reference any existing file.
    contexts:
      sudo: null
      unprivileged: null
```
