---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nano

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nano` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nano](../../tools/linux/nano.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nano |
| name | nano |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nano/ |

## Preserved Source Material

```yaml
_body: ''
_name: nano
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano
functions:
  file-read:
  - binary: false
    code: nano /path/to/input-file
    comment: The file content is displayed in the terminal interface.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'nano /path/to/output-file

      DATA

      ^O'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'nano

      ^R^X

      reset; sh 1>&0 2>&0'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: 'nano -s /bin/sh

      /bin/sh

      ^T^T'
    comment: The `SPELL` environment variable can be used in place of the `-s` option if the command line cannot be changed.
    contexts:
      sudo: null
      suid:
        code: 'nano -s ''/bin/sh -p''

          /bin/sh -p

          ^T^T'
        shell: false
      unprivileged: null
```
