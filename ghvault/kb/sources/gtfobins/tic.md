---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tic](../../tools/linux/tic.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tic |
| name | tic |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tic/ |

## Preserved Source Material

```yaml
_body: ''
_name: tic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tic
functions:
  file-read:
  - code: tic -C /path/to/input-file
    comment: This translates a terminfo file from source format into compiled format. It will attempt to translate an arbitrary
      file and output the contents of the file on failure.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
