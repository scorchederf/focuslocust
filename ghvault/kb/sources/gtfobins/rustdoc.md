---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rustdoc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rustdoc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustdoc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rustdoc](../../tools/linux/rustdoc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rustdoc |
| name | rustdoc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rustdoc/ |

## Preserved Source Material

```yaml
_body: ''
_name: rustdoc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustdoc
functions:
  file-read:
  - binary: false
    code: rustdoc /path/to/input-file
    comment: Partial content is displayed as error messages.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - binary: false
    code: 'echo ''//! DATA'' >/path/to/temp-file

      rustdoc /path/to/temp-file -o /path/to/output-dir/'
    comment: This command creates a number of documentation files in the target directory, and the data is written in multiple
      locations, e.g., `src/temp_file/temp-file.html`, amidst other content.
    contexts:
      sudo: null
      unprivileged: null
```
