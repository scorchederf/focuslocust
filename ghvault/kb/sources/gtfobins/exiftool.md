---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# exiftool

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `exiftool` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [exiftool](../../tools/linux/exiftool.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | exiftool |
| name | exiftool |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/exiftool/ |

## Preserved Source Material

```yaml
_body: ''
_name: exiftool
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool
functions:
  file-read:
  - code: 'exiftool -filename=/path/to/output-file /path/to/input-file

      cat /path/to/output-file'
    comment: If the permissions allow it, files are moved (instead of copied) to the destination.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: exiftool -filename=/path/to/output-file /path/to/input-file
    comment: If the permissions allow it, files are moved (instead of copied) to the destination.
    contexts:
      sudo: null
      unprivileged: null
  - binary: false
    code: exiftool "-description<=/path/to/input-file --filename /path/to/output-file
    comment: The output file must exists, either empty or be a supported image file. The content is written amidst other content.
    contexts:
      sudo: null
      unprivileged: null
  - binary: false
    code: exiftool "-description=DATA --filename /path/to/output-file
    comment: The output file must exists, either empty or be a supported image file. The content is written amidst other content.
    contexts:
      sudo: null
      unprivileged: null
  - binary: false
    code: exiftool -description -W /path/to/output-file --filename /path/to/input-file
    comment: Writes the metadata tags of the input file in textual format to the output.
    contexts:
      sudo: null
      unprivileged: null
  inherit:
  - code: exiftool -if '...' /etc/passwd
    comment: This allows to run Perl code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: perl
```
