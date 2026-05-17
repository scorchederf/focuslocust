---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nasm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nasm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nasm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nasm](../../tools/linux/nasm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nasm |
| name | nasm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nasm/ |

## Preserved Source Material

```yaml
_body: ''
_name: nasm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nasm
functions:
  file-read:
  - code: nasm -@ /path/to/input-file
    comment: The file content is treated as command line options and disclosed throught error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
