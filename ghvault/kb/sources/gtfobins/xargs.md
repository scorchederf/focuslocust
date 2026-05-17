---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xargs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xargs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xargs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xargs](../../tools/linux/xargs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xargs |
| name | xargs |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xargs/ |

## Preserved Source Material

```yaml
_body: ''
_name: xargs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xargs
functions:
  file-read:
  - binary: false
    code: xargs -a /path/to/input-file -0
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  shell:
  - code: xargs -a /dev/null /bin/sh
    contexts:
      sudo: null
      suid:
        code: xargs -a /dev/null /bin/sh -p
        shell: false
      unprivileged: null
    version: GNU
  - code: xargs -a /dev/null /bin/sh
    contexts:
      sudo: null
      suid:
        code: xargs -a /dev/null /bin/sh -p
        shell: false
      unprivileged: null
  - code: echo x | xargs -o -a /dev/null /bin/sh
    contexts:
      sudo: null
      suid:
        code: echo x | xargs -o -a /dev/null /bin/sh -p
        shell: false
      unprivileged: null
```
