---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nroff

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nroff` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nroff` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nroff](../../tools/linux/nroff.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nroff |
| name | nroff |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nroff/ |

## Preserved Source Material

```yaml
_body: ''
_name: nroff
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nroff
functions:
  file-read:
  - binary: false
    code: nroff /path/to/input-file
    comment: The file is typeset and some warning messages may appear.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: 'echo /bin/sh >groff

      chmod +x groff

      GROFF_BIN_PATH=. nroff'
    contexts:
      sudo: null
      unprivileged: null
```
